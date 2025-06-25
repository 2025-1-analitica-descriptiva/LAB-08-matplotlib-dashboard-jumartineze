# pylint: disable=line-too-long
"""
Escriba el codigo que ejecute la accion solicitada.
"""


from ._internals.create_visual_for_average_customer_rating import create_visual_for_average_customer_rating
from ._internals.create_visual_for_mode_of_shipment import create_visual_for_mode_of_shipment
from ._internals.create_visual_for_shipping_per_warehouse import create_visual_for_shipping_per_warehouse
from ._internals.create_visual_for_weight_distribution import create_visual_for_weight_distribution
from ._internals.load_data import load_data


def pregunta_01():
    """
    El archivo `files//shipping-data.csv` contiene información sobre los envios
    de productos de una empresa. Cree un dashboard estático en HTML que
    permita visualizar los siguientes campos:

    * `Warehouse_block`

    * `Mode_of_Shipment`

    * `Customer_rating`

    * `Weight_in_gms`

    El dashboard generado debe ser similar a este:

    https://github.com/jdvelasq/LAB_matplotlib_dashboard/blob/main/shipping-dashboard-example.png

    Para ello, siga las instrucciones dadas en el siguiente video:

    https://youtu.be/AgbWALiAGVo

    Tenga en cuenta los siguientes cambios respecto al video:

    * El archivo de datos se encuentra en la carpeta `data`.

    * Todos los archivos debe ser creados en la carpeta `docs`.

    * Su código debe crear la carpeta `docs` si no existe.
    """
    df = load_data()
    create_visual_for_shipping_per_warehouse(df)
    create_visual_for_mode_of_shipment(df)
    create_visual_for_average_customer_rating(df)
    create_visual_for_weight_distribution(df)