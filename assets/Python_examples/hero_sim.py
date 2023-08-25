import uaibot as ub
import numpy as np
import os 

dt = 0.01
t = 0
tmax = 12


def get_configuration(robot):
  return robot.q


def set_configuration_speed(robot, qdot_des):
  q_next = robot.q + qdot_des * dt
  robot.add_ani_frame(time=t + dt, q=q_next)


# As inicializações (ex: parâmetros do controlador) virão aqui
robot = ub.Robot.create_kuka_kr5()

# Especifica a posição desejada para o efetuador
#como uma função de t
#Também fornece a derivada, que vai ser utilizada no feedforward
R = 0.2
y_c = 0.6
z_c = 0.6
omega_d = np.pi/2
s_d = lambda tt: np.matrix([R * np.cos(omega_d * tt), y_c, z_c + R * np.sin(omega_d * tt)]).reshape((3, 1))
s_d_dot = lambda tt: np.matrix([-R * omega_d * np.sin(omega_d * tt), 0, R * omega_d * np.cos(omega_d * tt)]).reshape((3, 1))


# Especifica a orientação desejada para o eixo z do efetuador
z_d = np.matrix([0,1,0]).reshape((3,1))

# Cria uma nuvem de pontos para visualizarmos a parte de posição da referência
pc = np.matrix(np.zeros((3,0)))
for i in range(200):
  pc = np.block([pc, s_d(2*np.pi*i/199)])

target_pos_pc = ub.PointCloud(points=pc, size=0.03, color="purple")

#Cria uma esfera para mostrar que o robô está rastreando a trajetória
ball_tr = ub.Ball(htm = np.identity(4), radius=0.02, color="cyan")

# Cria a simulação
sim = ub.Simulation([robot, target_pos_pc, ball_tr])

# Captura o número de juntas do robô
n = np.shape(robot.q)[0]

# Cria a função F:
def fun_F(r):
    A = 0.25
    w_tol = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01]
    F = np.matrix(np.zeros((4, 1)))
    for i in range(4):
        if abs(r[i, 0]) < w_tol[i]:
            F[i, 0] = -A * (r[i, 0] / w_tol[i])
        elif r[i, 0] >= w_tol[i]:
            F[i, 0] = -A
        else:
            F[i, 0] = A
    return F

# Cria uma matriz para o histórico de função de tarefa, da ação de controle
# e do tempo
hist_r = np.matrix(np.zeros((4, 0)))
hist_u = np.matrix(np.zeros((n, 0)))
hist_t = []

# Colocaremos aqui nosso "main" do controlador, que ficará em um laço
# durante um tempo tmax
for i in range(round(tmax / dt)):
  #################################
  # Início da lógica de controle  #
  #################################

  # Mede a configuração dos sensores
  q = get_configuration(robot)

  # Calcula a cinemática direta e Jacobiana para o efetuador nessa
  # configuração
  Jg, fk = robot.jac_geo(q)
  # Faz a extração de z_e e s_e
  z_e = fk[0:3, 2]
  s_e = fk[0:3, 3]

  # Monta o vetor de tarefa
  r = np.matrix(np.zeros((4, 1)))
  r[0:3] = s_e - s_d(t)
  r[3] = 1 - z_d.T * z_e

  # Monta a Jacobiana de tarefa
  Jr = np.matrix(np.zeros((4, n)))

  # Monta o termo de feedforward
  ff = np.block([[-s_d_dot(t)],[0]])

  Jr[0:3, :] = Jg[0:3, :]
  Jr[3, :] = z_d.T * ub.Utils.S(z_e) * Jg[3:6, :]


  # Calcula a ação de controle
  u = ub.Utils.dp_inv(Jr, 0.001) * (fun_F(r)-ff)

  # Guarda informações no histórico
  hist_r = np.block([hist_r, r])
  hist_u = np.block([hist_u, u])
  hist_t.append(t)

  # Manda a ação de controle para o robô
  set_configuration_speed(robot, u)

  #################################
  # Fim da lógica de controle     #
  #################################

  # O tempo sempre vai passar no final do ciclo
  t += dt

  #Atualiza a posição da bola (apenas para visualização)
  ball_tr.add_ani_frame(time = t, htm = ub.Utils.trn(s_d(t)))

# Roda a simulação
sim.save(os.path.dirname(__file__), "HERO_sim")

# <div id='canvas_container_16520598357012613' style='width:100%; height:100%;position:relative'>
# <div id='loading_screen_16520598357012613' style='width:100%;height:100%;position:relative; background-color: #19bd39;text-align:center;align-items:center;display:flex;justify-content:center'> 
#  <img src='https://raw.githubusercontent.com/viniciusmgn/uaibot_content/master/contents/SVG/logo_uai_bot.svg' style='width:200px;height:114px'/>
#  </div>
# <script id='MathJax-script' async src='https://cdn.jsdelivr.net/npm/mathjax@3.0.1/es5/tex-mml-chtml.js'></script>
# <canvas id='scene_16520598357012613' style='width:100%; height:90%;position:relative'></canvas>
# <!-- USER DIVS GO HERE --><div class = 'controller' style='width:100%;height:30px;'></div>
# </div>
