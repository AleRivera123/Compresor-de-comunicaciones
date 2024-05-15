class CompresorRLE:
    # Método para comprimir una cadena usando codificación de longitud de ejecución (RLE)
    def comprimir(self, texto):
        if not texto:
            return "Por favor, ingrese algún texto para comprimir."
        
        resultado = []
        cuenta_actual = 1
        char_actual = texto[0]

        for char in texto[1:]:
            if char == char_actual:
                cuenta_actual += 1
            else:
                if cuenta_actual > 0:
                    resultado.append(f"{cuenta_actual}{char_actual}")
                char_actual = char
                cuenta_actual = 1
        
        # Asegurarse de añadir la última repetición acumulada
        if cuenta_actual > 0:
            resultado.append(f"{cuenta_actual}{char_actual}")
        
        texto_comprimido = ''.join(resultado)
        resultado_bytes = texto_comprimido.encode('utf-8')
        resultado_final = resultado_bytes.hex()
        return resultado_final

    # Método para descomprimir una cadena codificada con RLE
    def descomprimir(self, texto_hex):
        if not texto_hex:
            return "Por favor, ingrese algún texto para descomprimir."

        try:
            bytes_input = bytes.fromhex(texto_hex)
            texto_original = bytes_input.decode('utf-8')
        except ValueError:
            return "Formato hexadecimal inválido. Por favor, asegúrese de que el texto esté en formato hexadecimal correcto."

        resultado = []
        i = 0
        while i < len(texto_original):
            cuenta = 0
            # Acumular todos los dígitos hasta encontrar un carácter
            while i < len(texto_original) and texto_original[i].isdigit():
                cuenta = cuenta * 10 + int(texto_original[i])
                i += 1
            
            # Evitar errores si el conteo es 0 y asegurarse de no salir del rango
            if cuenta > 0 and i < len(texto_original):
                resultado.append(texto_original[i] * cuenta)
                i += 1
            else:
                # Si el conteo es 0 o se alcanza el final del texto, no hacer nada
                break

        texto_descomprimido = ''.join(resultado)
        return texto_descomprimido
