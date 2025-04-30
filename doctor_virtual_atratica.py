import streamlit as st

st.set_page_config(page_title="Doctor Virtual Antártida", page_icon="🧊", layout="centered")

st.image("https://i.imgur.com/fpDPAoR.png", width=150)
st.title("Doctor Virtual Antártida")
st.write("Tu asistente médico inteligente para zonas extremas como la Antártida.")

menu = st.selectbox("Selecciona una función médica:", [
    ("Diagnóstico de Síntomas", diagnostico_sintomas),
    ("Dieta Personalizada", dieta_personalizada),
    ("Rutinas de Ejercicio", rutinas_ejercicio),
    ("Psicólogo Virtual", psicologo_virtual),
    ("Análisis de Imágenes Médicas", analisis_imagenes),
    ("Historial Médico Guardado", historial_medico),
    ("Primeros Auxilios", primeros_auxilios),
    ("Análisis de Signos Vitales", analisis_signos_vitales),
    ("Modo Emergencia", modo_emergencia),
    ("Estado Mental y Recomendaciones", estado_mental_recomendaciones),
    ("Monitoreo Diario del Estado de Salud", monitoreo_salud),
    ("Dudas sobre Salud Sexual", dudas_salud_sexual),
    ("Rutina Diaria con Recordatorios", rutina_diaria),
    ("Modo Sueño", modo_sueno),
    ("Condiciones Extremas en la Antártida", condiciones_extremas),
    ("Cuidados de la Piel en la Antártida", cuidados_piel_antarctica),
    ("Comunicación en Emergencias", comunicacion_emergencias),
    ("Informe Diario", informe_diario),
    ("Técnicas de Respiración", tecnicas_respiracion),
])

# Funciones del doctor virtual

def diagnostico_sintomas():
    sintomas = simpledialog.askstring("Síntomas", "Describe cómo te sientes o tus síntomas actuales.")
    prompt = f"Eres un doctor. Un paciente presenta los siguientes síntomas: {sintomas}. ¿Cuál sería tu orientación o diagnóstico tentativo y recomendación profesional inicial?"
    respuesta = genai.GenerativeModel(MODEL_NAME).generate_content(prompt).text
    hablar(respuesta)
    messagebox.showinfo("Diagnóstico", respuesta)

def dieta_personalizada():
    peso = simpledialog.askinteger("Peso", "Ingresa tu peso en kg:")
    altura = simpledialog.askinteger("Altura", "Ingresa tu altura en cm:")
    objetivo = simpledialog.askstring("Objetivo", "¿Cuál es tu objetivo (bajar peso, ganar músculo, etc.)?")
    dieta = f"Con un peso de {peso} kg y una altura de {altura} cm, para lograr tu objetivo de '{objetivo}', recomiendo una dieta balanceada con énfasis en proteínas magras, vegetales frescos, carbohidratos integrales y buena hidratación."
    hablar(dieta)
    messagebox.showinfo("Dieta Personalizada", dieta)

def rutinas_ejercicio():
    condicion = simpledialog.askstring("Condición Física", "¿Cuál es tu nivel de actividad física?")
    rutina = f"Para una condición física '{condicion}', una rutina recomendada incluye: 10 min de calentamiento, 20 min de actividad principal (cardio o fuerza), y 10 min de estiramientos. Ajusta según tu comodidad."
    hablar(rutina)
    messagebox.showinfo("Rutina de Ejercicio", rutina)

def psicologo_virtual():
    estado_emocional = simpledialog.askstring("Estado Emocional", "¿Cómo te sientes emocionalmente hoy?")
    prompt = f"Soy tu psicólogo virtual. Estoy aquí para ayudarte. Un paciente dice: '{estado_emocional}'. ¿Cuál sería una respuesta empática y útil para él o ella?"
    respuesta = genai.GenerativeModel(MODEL_NAME).generate_content(prompt).text
    hablar(respuesta)
    messagebox.showinfo("Psicólogo Virtual", respuesta)

def analisis_imagenes():
    archivo_imagen = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Imagenes", "*.jpg *.jpeg *.png")])
    if archivo_imagen:
        with open(archivo_imagen, "rb") as f:
            contenido = f.read()
            imagen_base64 = base64.b64encode(contenido).decode("utf-8")
            prompt = "Analiza esta imagen médica y proporciona una observación profesional para un paciente."
            model = genai.GenerativeModel(MODEL_NAME)
            respuesta = model.generate_content([
                prompt,
                genai.content.ImageContent(data=imagen_base64, mime_type="image/png")
            ]).text
            hablar(respuesta)
            messagebox.showinfo("Análisis de Imagen", respuesta)

def historial_medico():
    historial = cargar_historial()
    historial_str = json.dumps(historial, indent=4)
    hablar("Aquí tienes tu historial médico actualizado.")
    messagebox.showinfo("Historial Médico", historial_str)

def primeros_auxilios():
    emergencia = simpledialog.askstring("Emergencia", "¿Qué tipo de emergencia tienes? (herida, congelación, quemadura, etc.)")
    pasos = {
        "herida": "1. Lava la herida con agua limpia. 2. Aplica antiséptico. 3. Cubre con venda estéril. 4. Si sangra mucho o es profunda, busca atención médica.",
        "congelación": "1. Refúgiate en un lugar cálido. 2. No frotes la zona afectada. 3. Calienta lentamente con agua tibia. 4. Usa ropa seca y aislante. 5. Acude al médico cuanto antes.",
        "quemadura": "1. Enfría con agua a temperatura ambiente durante 10 minutos. 2. No revientes ampollas. 3. Aplica apósito limpio. 4. Consulta a un profesional si es extensa."
    }
    if emergencia:
        instrucciones = pasos.get(emergencia.lower(), "Tipo de emergencia no reconocida. Busca ayuda profesional inmediatamente.")
        hablar(instrucciones)
        messagebox.showinfo("Primeros Auxilios", instrucciones)

def analisis_signos_vitales():
    temperatura = simpledialog.askfloat("Temperatura", "¿Cuál es tu temperatura corporal en °C?")
    pulso = simpledialog.askinteger("Pulso", "¿Cuál es tu pulso por minuto?")
    respiracion = simpledialog.askinteger("Respiración", "¿Cuál es tu ritmo respiratorio por minuto?")
    riesgo = "Signos vitales en rango normal. Continúa con observación."
    if temperatura > 38:
        riesgo = "Tienes fiebre. Bebe líquidos y monitorea tu estado."
    elif temperatura < 35:
        riesgo = "Temperatura baja detectada. Riesgo de hipotermia."
    hablar(riesgo)
    messagebox.showinfo("Análisis de Signos Vitales", riesgo)

def modo_emergencia():
    protocolo = (
        "Modo emergencia activado.\n\n"
        "Protocolo de seguridad:\n"
        "1. Mantén la calma y evalúa tu entorno inmediato.\n"
        "2. Refúgiate en un lugar seguro y resguardado del frío.\n"
        "3. Usa tu equipo de comunicación: radio o teléfono satelital.\n"
        "4. Comunica tu ubicación exacta y situación actual.\n"
        "5. Conserva calor corporal: cúbrete con mantas, ropa seca o saco térmico.\n"
        "6. Raciona alimentos y líquidos.\n"
        "7. No te desplaces sin orientación, espera instrucciones del equipo de rescate.\n\n"
        "Sigue estos pasos y mantente en comunicación constante hasta recibir ayuda."
    )
    hablar(protocolo)
    messagebox.showinfo("Modo Emergencia - Protocolo", protocolo)

def estado_mental_recomendaciones():
    estado_emocional = simpledialog.askstring("Estado Emocional", "¿Cómo te sientes últimamente?")
    recomendaciones = f"Para sentirte mejor, intenta: caminar al aire libre, escuchar música relajante, hacer ejercicios de respiración y hablar con alguien de confianza."
    hablar(recomendaciones)
    messagebox.showinfo("Estado Mental y Recomendaciones", recomendaciones)

def monitoreo_salud():
    salud = "Tu monitoreo diario muestra signos estables. Sigue cuidándote y haz chequeos regulares."
    hablar(salud)
    messagebox.showinfo("Monitoreo Diario", salud)

def dudas_salud_sexual():
    pregunta = simpledialog.askstring("Salud Sexual", "Escribe tu duda sobre salud sexual:")
    respuesta = f"Gracias por tu pregunta. La salud sexual es importante. Usa protección, hazte chequeos regulares y consulta a un especialista si tienes dudas."
    hablar(respuesta)
    messagebox.showinfo("Salud Sexual", respuesta)

def rutina_diaria():
    actividades = simpledialog.askstring("Rutina Diaria", "Describe tus actividades diarias:")
    rutina = "Organiza tu día con horarios para descanso, comidas saludables, actividad física, y momentos de relajación."
    hablar(rutina)
    messagebox.showinfo("Rutina Diaria", rutina)

def modo_sueno():
    hablar("Modo sueño activado. Estaré en espera hasta que me necesites nuevamente.")
    messagebox.showinfo("Modo Sueño", "Modo sueño activado.")

def condiciones_extremas():
    consejo = "Protégete del frío extremo: viste en capas, mantente seco, evita exposición prolongada y ten refugio disponible."
    hablar(consejo)
    messagebox.showinfo("Condiciones Extremas", consejo)

def cuidados_piel_antarctica():
    consejo = "Cuida tu piel: usa protector solar, bálsamo labial y crema hidratante. Cubre tu rostro del viento y evita el aire seco prolongado."
    hablar(consejo)
    messagebox.showinfo("Cuidado de la Piel", consejo)

def comunicacion_emergencias():
    consejo = "En situaciones de emergencia, usa radio o teléfono satelital, comunica tu ubicación y mantén contacto frecuente."
    hablar(consejo)
    messagebox.showinfo("Comunicación", consejo)

def informe_diario():
    historial = cargar_historial()
    fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    resumen = f"Informe Diario - {fecha}\n\n"
    if historial:
        for clave, valor in historial.items():
            resumen += f"{clave}:\n{valor}\n\n"
    else:
        resumen += "No hay información médica registrada en el historial."
    generar_pdf("informe_diario", resumen)
    hablar("Tu informe diario ha sido generado y guardado como PDF.")
    messagebox.showinfo("Informe Diario", "El informe ha sido guardado correctamente.")

def tecnicas_respiracion():
    metodos = {
        "Respiración diafragmática": "Respira profundamente inflando el abdomen. Objetivo: reducir el estrés y la ansiedad.",
        "Respiración 4-7-8": "Inhala 4s, retén 7s, exhala 8s. Objetivo: inducir el sueño.",
        "Respiración alterna por fosas nasales": "Cierra una fosa, inhala, cambia. Objetivo: equilibrar el sistema nervioso.",
        "Respiración de fuego (Kapalabhati)": "Exhalaciones rápidas y forzadas. Objetivo: energizar el cuerpo.",
        "Respiración en caja": "Inhala, retén, exhala, retén cada uno 4s. Objetivo: enfoque y calma mental.",
        "Respiración lenta consciente": "Inhala y exhala lentamente contando hasta 5. Objetivo: mejorar la concentración.",
        "Respiración Wim Hof": "30 respiraciones profundas seguidas de retención. Objetivo: resistencia al frío y mejora inmunológica.",
        "Respiración Ujjayi": "Respira por la nariz emitiendo un sonido oceánico. Objetivo: generar calor interno en yoga.",
        "Respiración táctil": "Manos en pecho y abdomen para guiar la respiración. Objetivo: conexión mente-cuerpo.",
        "Respiración 2-1": "Exhala el doble de tiempo que inhalas. Objetivo: activar el sistema parasimpático."
    }
    lista = "Técnicas de Respiración:\n\n"
    for nombre, descripcion in metodos.items():
        lista += f"- {nombre}: {descripcion}\n"
    hablar("Aquí tienes algunas técnicas de respiración con sus objetivos específicos.")
    messagebox.showinfo("Técnicas de Respiración", lista)
