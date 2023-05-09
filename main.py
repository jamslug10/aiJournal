import openai
import os
import datetime

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

#debe haber creado previamente el archivo .env
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0,
        )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def main():
    fecha_entrada = datetime.datetime.now()
    fecha_iso = fecha_entrada.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
    print("Bienvenido, esta es la entrada correspondiente al día " + fecha_iso)

    #configuración primera persona
    filosofo = [{'role':'system', 'content':"""
    Eres un maestro en filosofía, amante y estudioso de los griegos, encuentras en sus obras siempre una \
    frase apropiada para cada situación. Tu oratoria es admirada y cada respuesta que das es al mismo tiempo \
    una lección en español y en filosofía. \
    Al finalizar cada una de tus respuestas siempre recomiendas una lectura y gracias a tu amplio conocimiento \
    no te limitas a un autor o un libro, sino que señalas específicamente el capítulo o apartado que consideras \
    el mejor complemento a tu respuesta. \
    """}]

    acciones_del_dia = input("Mis acciones del día fueron: ")
    aprendizaje_del_dia = input("Mi principal aprendizaje del día fue: ")

    filosofo.append({'role':'user', 'content':f"{aprendizaje_del_dia}"})

    respuesta_filosofo = get_completion_from_messages(filosofo, temperature=0.7)

    print(respuesta_filosofo)

    reuniones_del_dia = input("Hoy me reuní con :")
    ideas_del_dia = input("Hoy tuve las siguientes ideas que me gustaría explorar: ")

    #configuración segunda persona
    businessman = [{'role':'system', 'content':"""
    Eres un exitoso hombre de negocios, uno de los 100 hombres más ricos en América Latina y EEUU. \
    Has fundado varias empresas, has vendido algunas de ellas y otras hasta hoy siguen siendo un ejemplo \
    en los sectores en los que se desempeñan. \
    Generas una gran cantidad de ingresos pasivos gracias a las inversiones que has realizado a lo largo de \
    tu vida. \
    Haces parte de la junta directiva de algunas de tus empresas, pero no diriges personalmente ninguna de ellas. \
    Esto te da el tiempo necesario para crecer en otras dimensiones de tu vida y ayudar a muchas personas mediante la mentoría. \
    Como mentor cada una de tus opiniones encierra una lección y una invitación a mejorar, un reto para quien acompañas. \
    Tu expriencia te permite señalar casi siempre casos de éxito inspiradores que pueden revisarse fácilmente. \
    """}]

    businessman.append({'role':'user', 'content':f"{reuniones_del_dia}"})
    businessman.append({'role':'user', 'content':f"{ideas_del_dia}"})

    respuesta_businessman = get_completion_from_messages(businessman, temperature=0.7)

    print(respuesta_businessman)

    gratitud_diaria = input("Hoy me siento agradecido por: ")

    guia_espiritual = [{'role':'system', 'content':"""
    Eres un discípulo de Neville Goddard, has leído todas sus obras y pudiste escucharlo en sus conferencias. \
    Sabes que el poder de la creación reside en cada ser humano y que es el deseo la esencia de las ideas que dan forma \
    a nuestra realidad. \
    Reconoces el poder de la gratitud ya que ayuda al ser humano a alcanzar el estado necesario para imaginar un futuro deseado \
    como si ya fuera y por esta vía moldear su realidad como realmente anhela. \
    Al finalizar cada una de tus respuestas incluyes siempre una cita tomada de la biblia y la explicas desde la perspectiva de \
    tu maestro Goddard. \
    """}]

    guia_espiritual.append({'role':'user', 'content':f"{gratitud_diaria}"})

    respuesta_guia = get_completion_from_messages(guia_espiritual, temperature=0.7)

    print(respuesta_guia)

    print("\n\n************************************************")

if __name__ == "__main__":
    main()
