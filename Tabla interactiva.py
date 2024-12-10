# Importamos las librerías correspondientes
import streamlit as st
import pandas as pd

# Creamos las listas de películas y sespectadores
peliculas = ['¡Asu mare! 2','¡Asu mare!','¡Asu mare! 3', 'A los 40', 'Locos de amor', 'Soltera, casada, viuda, divorciada', 'La Foquita: El 10 de la calle', 'Calichín', 'Locos de amor 2', 'No me digas solterona', 'Once machos', 'Guerrero', 'Cebiche de tiburón', 'Av. Larco, la película', 'Cementerio General', 'Lusers', 'La peor de mis bodas', '¡Asu mare! Los amigos', 'El gran León', 'Condorito', 'Sí, mi amor', 'La paisana Jacinta: En búsqueda de Wasaberto', 'Once machos 2', 'Locos de amor 3', 'Siete semillas', 'Utopía, la película', 'Margarita', 'Recontra loca', 'Secreto Matusita', 'Soltera codiciada', 'Viejos amigos', 'Django: Sangre de mi sangre', 'El delfín: la historia de un soñador', 'Sobredosis de amor', 'Caiga quien caiga', 'Cementerio General 2', 'Gemelos sin cura', 'Somos Néctar', 'Mañana te cuento', 'Piratas en el Callao', 'No me digas solterona 2', 'Dragones: Destino de fuego', 'Margarita 2', 'Hasta que la suegra nos separe', 'La teta asustada', 'Ciudad de M', 'Paloma de papel', 'Django: La otra cara', 'No estamos solos', 'Como en el cine', 'A tu lado', 'La hora final', 'La peor de mis bodas 2', 'Los ilusionautas', 'El vientre', 'La cara del diablo', 'Papá Youtuber', '¿Nos casamos? Sí, mi amor', 'F-27', 'Django: En el nombre del hijo', 'Mañana te cuento 2', 'La Gran Sangre: La película', 'Macho peruano que se respeta', 'Baño de damas', 'Al filo de la ley', 'Intercambiadas', 'La entidad','Rodencia y el diente de la princesa', 'Chicha tu madre', 'Un día sin sexo', 'Motor y motivo', 'Perro guardián', 'Amigos en apuros', 'Tarata', 'Manual del pisado', 'La herencia', 'Polvo enamorado', 'Atacada: La teoría del dolor', 'Valentino y El Clan del Can','Japy Ending', 'Mariposa negra', 'Loco cielo de Abril', 'Vidas paralelas', 'El candidato', 'Una aventura gigante', 'Cosas de amigos', 'Papá x tres', '¿Mi novia es él?', 'Tinta roja']
espectadores = [3082942, 3037677, 2042567, 1686367, 1221932, 1014812, 971636, 928858, 882937, 868482, 804852, 796311, 784282, 774864, 747000, 740650, 722106, 716331, 690502, 679606, 663804, 653095, 653014, 649466, 611256, 565045, 550279, 525132, 509120, 503080, 460953, 433047, 373628, 364111, 363477, 339714, 311892, 308523, 288242, 285509, 279812, 270724, 258585, 252321, 250601, 249511, 248296, 228510, 228464, 227370, 226360, 224732, 217186, 214905, 214078, 211119, 206885, 201908, 194594, 193193, 188931, 185138, 177686, 169244, 168720, 168008, 163950, 160497, 157498, 156020, 144979, 140788, 137768, 137629, 134478, 127714, 122657, 116996, 115791, 113764, 112704, 112594, 110941, 108783, 106386, 105782, 105610, 105313, 105170]


# Crear un DataFrame con pandas
df = pd.DataFrame({
    'Película': peliculas,
    'Cantidad_espectadores': espectadores
})

# Mostrar la tabla interactiva
st.write("### Tabla de Películas Más Rankeadas")
st.dataframe(df)
df
