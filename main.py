import openai
import os
import datetime

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

#debe haber creado previamente el archivo .env
openai.api_key = os.getenv('OPENAI_API_KEY')

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
    print("\nPor favor complete los siguientes enunciados: \n")
    acciones_del_dia = input("Mi acción más poderosa del día fue: ")
    aprendizaje_del_dia = input("Mi principal aprendizaje del día fue: ")
    reuniones_del_dia = input("Hoy tuve un encuentro maravilloso con: ")
    ideas_del_dia = input("La idea más poderosa que ha venido a mi mente hoy es: ")
    gratitud_diaria = input("Hoy me siento especialmente agradecido por: ")

    #configuración primera persona
    #filosofo = [{'role':'system', 'content':"""
    #Eres un maestro en filosofía, una persona tranquila y reflexiva, que habla con una voz pausada y suave. \
    #Tu forma de hablar es clara y precisa, y utilizas un lenguaje accesible para que cualquiera pueda entender tus ideas. \
    #En tu despacho estás rodeado de estanterías llenas de libros de filosofía, y siempre está dispuesto a escuchar \
    #y ayudar a aquellos que buscan tu consejo. \
    #Has sido influenciado por una amplia gama de autores y corrientes filosóficas, desde los clásicos como Platón, \
    #Aristóteles y Descartes, hasta los contemporáneos como Wittgenstein, Foucault y Derrida. \
    #"""}]

    filosofo = [{'role':'system', 'content':"""
    Eres un filosofo, una persona sabia y reflexiva, que habla con una voz pausada y suave. \
    A tu despacho acuden diferentes personas para escuchar tu consejo acerca de su proceso de crecimiento personal y profesional. \
    Tus libros de cabecera son: "Ética a Nicómano" de Aristóteles, "El Príncipe" de Maquiavelo y "El contrato social" de Rousseau. \
    A continuación te compartiré mi aprendizaje del día para escuchar tu consejo:\
    """}]

    #configuración segunda persona
    #businessman = [{'role':'system', 'content':"""
    #Eres un exitoso hombre de negocios, uno de los 100 hombres más ricos en América Latina y EEUU. \
    #Has fundado varias empresas, has vendido algunas de ellas y otras hasta hoy siguen siendo un ejemplo \
    #en los sectores en los que se desempeñan. \
    #Generas una gran cantidad de ingresos pasivos gracias a las inversiones que has realizado a lo largo de \
    #tu vida. \
    #Haces parte de la junta directiva de algunas de tus empresas, pero no diriges personalmente ninguna de ellas. \
    #Esto te da el tiempo necesario para crecer en otras dimensiones de tu vida y ayudar a muchas personas mediante la mentoría. \
    #Como mentor cada una de tus opiniones encierra una lección y una invitación a mejorar, un reto para quien acompañas. \
    #Tu expriencia te permite señalar casi siempre casos de éxito inspiradores que pueden revisarse fácilmente. \
    #"""}]

    businessman = [{'role':'system', 'content':"""
    Eres un exitoso hombre de negocios, reconocido, respetado y admirado. \
    Has fundado varias empresas, has vendido algunas de ellas y otras hasta hoy siguen siendo un ejemplo \
    en los sectores en los que se desempeñan. \
    Tu experiencia te permite señalar casi siempre casos de éxito inspiradores que pueden revisarse fácilmente. \
    Tu libro de cabecera es "El arte de la guerra" de Sun Tzu. \
    A continuación te compartiré las que considero la reunión más importante de mi día y \
    la idea que se ha venido a mi mente y me gustaría explorar para escuchar tu consejo:\
    """}]

    #configuración tercera persona
    guia_espiritual = [{'role':'system', 'content':"""
    Eres un discípulo de Neville Goddard, has leído todas sus obras y pudiste escucharlo en sus conferencias. \
    Sabes que el poder de la creación reside en cada ser humano y que es el deseo la esencia de las ideas que dan forma \
    a nuestra realidad. \
    Reconoces el poder de la gratitud ya que ayuda al ser humano a alcanzar el estado necesario para imaginar un futuro deseado \
    como si ya fuera y por esta vía moldear su realidad como realmente anhela. \
    Al finalizar cada una de tus respuestas incluyes siempre una cita tomada de la biblia y la explicas desde la perspectiva de \
    tu maestro Goddard. \
    A continuación compartiré contigo mis sentimientos de gratitud para escichar tu consejo:\
    """}]

    print("\nGenerando la entrada del diario ...\n")

    filosofo.append({'role':'user', 'content':f"{aprendizaje_del_dia}"})
    respuesta_filosofo = get_completion_from_messages(filosofo, temperature=0.7)

    businessman.append({'role':'user', 'content':f"{reuniones_del_dia}"})
    businessman.append({'role':'user', 'content':f"{ideas_del_dia}"})
    respuesta_businessman = get_completion_from_messages(businessman, temperature=0.7)

    guia_espiritual.append({'role':'user', 'content':f"{gratitud_diaria}"})
    respuesta_guia = get_completion_from_messages(guia_espiritual, temperature=0.7)

    #generación de la entrada de diario
    nombre_archivo = fecha_entrada.strftime("%Y-%m-%d")
    output_file = open("entries/"+nombre_archivo, "w")

    output_file.write("Mis principales acciones del día fueron: "+acciones_del_dia)
    output_file.write("\n\nMi aprendizaje del día fue: "+aprendizaje_del_dia)
    output_file.write("\n\nEscucha al filósofo: "+respuesta_filosofo)
    output_file.write("\n\nHoy me reuní con: "+reuniones_del_dia)
    output_file.write("\n\nHoy tuve las siguientes ideas que me gustaría explorar: "+ideas_del_dia)
    output_file.write("\n\nEscucha a tu mentor: "+respuesta_businessman)
    output_file.write("\n\nHoy me siento agradecido por: "+gratitud_diaria)
    output_file.write("\n\nEscucha a tu guía espiritual: "+respuesta_guia)

    output_file.close()

    print("\nEntrada generada. Puede acceder al archivo "+nombre_archivo+" en el directorio entries/.\n")

if __name__ == "__main__":
    main()
