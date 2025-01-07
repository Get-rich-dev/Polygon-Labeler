# -*- coding: utf-8 -*-
"""
/***************************************************************************
 PolygonLabeler
                                 A QGIS plugin
 Automatically generate and label polygons with custom names, and add the labels as a new attribute field to the attribute table.
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2025-01-06
        copyright            : (C) 2025 by Peter Boateng
        email                : peterboateng06@gmail.com
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load PolygonLabeler class from file PolygonLabeler.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .PolygonLabeler import PolygonLabeler
    return PolygonLabeler(iface)
