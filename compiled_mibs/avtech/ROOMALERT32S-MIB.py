# SNMP MIB module (ROOMALERT32S-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\avtech\ROOMALERT32S-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:15 2025
# On host DESKTOP-ORUUBP9 platform Windows version 11 by user speterman
# Using Python version 3.12.8 (tags/v3.12.8:2dc476b, Dec  3 2024, 19:30:04) [MSC v.1942 64 bit (AMD64)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 enterprises,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Avtech_ObjectIdentity = ObjectIdentity
avtech = _Avtech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1)
)
_Roomalert32S_ObjectIdentity = ObjectIdentity
roomalert32S = _Roomalert32S_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1)
)
_Internal_ObjectIdentity = ObjectIdentity
internal = _Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1)
)
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 1)
)


class _Internal_tempf_Type(Integer32):
    """Custom type internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_tempf_Type.__name__ = "Integer32"
_Internal_tempf_Object = MibScalar
internal_tempf = _Internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 1, 1),
    _Internal_tempf_Type()
)
internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_tempf.setStatus("mandatory")


class _Internal_tempc_Type(Integer32):
    """Custom type internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_tempc_Type.__name__ = "Integer32"
_Internal_tempc_Object = MibScalar
internal_tempc = _Internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 1, 2),
    _Internal_tempc_Type()
)
internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_tempc.setStatus("mandatory")
_Humidity_ObjectIdentity = ObjectIdentity
humidity = _Humidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 2)
)


class _Internal_humidity_Type(Integer32):
    """Custom type internal_humidity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_humidity_Type.__name__ = "Integer32"
_Internal_humidity_Object = MibScalar
internal_humidity = _Internal_humidity_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 2, 1),
    _Internal_humidity_Type()
)
internal_humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_humidity.setStatus("mandatory")
_Power_ObjectIdentity = ObjectIdentity
power = _Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 3)
)


class _Internal_power_Type(Integer32):
    """Custom type internal_power based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Internal_power_Type.__name__ = "Integer32"
_Internal_power_Object = MibScalar
internal_power = _Internal_power_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 3, 1),
    _Internal_power_Type()
)
internal_power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_power.setStatus("mandatory")
_Heat_index_ObjectIdentity = ObjectIdentity
heat_index = _Heat_index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 4)
)


class _Internal_heat_index_Type(Integer32):
    """Custom type internal_heat_index based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_heat_index_Type.__name__ = "Integer32"
_Internal_heat_index_Object = MibScalar
internal_heat_index = _Internal_heat_index_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 4, 1),
    _Internal_heat_index_Type()
)
internal_heat_index.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_heat_index.setStatus("optional")


class _Internal_heat_indexC_Type(Integer32):
    """Custom type internal_heat_indexC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_heat_indexC_Type.__name__ = "Integer32"
_Internal_heat_indexC_Object = MibScalar
internal_heat_indexC = _Internal_heat_indexC_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 4, 2),
    _Internal_heat_indexC_Type()
)
internal_heat_indexC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_heat_indexC.setStatus("optional")
_Analog_ObjectIdentity = ObjectIdentity
analog = _Analog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 5)
)


class _Internal_analog1_Type(Integer32):
    """Custom type internal_analog1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_analog1_Type.__name__ = "Integer32"
_Internal_analog1_Object = MibScalar
internal_analog1 = _Internal_analog1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 5, 1),
    _Internal_analog1_Type()
)
internal_analog1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_analog1.setStatus("mandatory")


class _Internal_analog2_Type(Integer32):
    """Custom type internal_analog2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_analog2_Type.__name__ = "Integer32"
_Internal_analog2_Object = MibScalar
internal_analog2 = _Internal_analog2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 5, 2),
    _Internal_analog2_Type()
)
internal_analog2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_analog2.setStatus("mandatory")
_Relay_ObjectIdentity = ObjectIdentity
relay = _Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 6)
)


class _Internal_relay1_Type(Integer32):
    """Custom type internal_relay1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Internal_relay1_Type.__name__ = "Integer32"
_Internal_relay1_Object = MibScalar
internal_relay1 = _Internal_relay1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 6, 1),
    _Internal_relay1_Type()
)
internal_relay1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internal_relay1.setStatus("mandatory")


class _Internal_relay2_Type(Integer32):
    """Custom type internal_relay2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Internal_relay2_Type.__name__ = "Integer32"
_Internal_relay2_Object = MibScalar
internal_relay2 = _Internal_relay2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 6, 2),
    _Internal_relay2_Type()
)
internal_relay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internal_relay2.setStatus("mandatory")
_Dew_point_ObjectIdentity = ObjectIdentity
dew_point = _Dew_point_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 7)
)


class _Internal_dew_point_c_Type(Integer32):
    """Custom type internal_dew_point_c based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_dew_point_c_Type.__name__ = "Integer32"
_Internal_dew_point_c_Object = MibScalar
internal_dew_point_c = _Internal_dew_point_c_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 7, 1),
    _Internal_dew_point_c_Type()
)
internal_dew_point_c.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_dew_point_c.setStatus("optional")


class _Internal_dew_point_f_Type(Integer32):
    """Custom type internal_dew_point_f based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_dew_point_f_Type.__name__ = "Integer32"
_Internal_dew_point_f_Object = MibScalar
internal_dew_point_f = _Internal_dew_point_f_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 1, 7, 2),
    _Internal_dew_point_f_Type()
)
internal_dew_point_f.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_dew_point_f.setStatus("optional")
_Digital_ObjectIdentity = ObjectIdentity
digital = _Digital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2)
)
_Digital_sen1_ObjectIdentity = ObjectIdentity
digital_sen1 = _Digital_sen1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 1)
)


class _Digital_sen1_1_Type(Integer32):
    """Custom type digital_sen1_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_1_Type.__name__ = "Integer32"
_Digital_sen1_1_Object = MibScalar
digital_sen1_1 = _Digital_sen1_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 1, 1),
    _Digital_sen1_1_Type()
)
digital_sen1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_1.setStatus("mandatory")


class _Digital_sen1_2_Type(Integer32):
    """Custom type digital_sen1_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_2_Type.__name__ = "Integer32"
_Digital_sen1_2_Object = MibScalar
digital_sen1_2 = _Digital_sen1_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 1, 2),
    _Digital_sen1_2_Type()
)
digital_sen1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_2.setStatus("mandatory")


class _Digital_sen1_3_Type(Integer32):
    """Custom type digital_sen1_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_3_Type.__name__ = "Integer32"
_Digital_sen1_3_Object = MibScalar
digital_sen1_3 = _Digital_sen1_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 1, 3),
    _Digital_sen1_3_Type()
)
digital_sen1_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_3.setStatus("mandatory")


class _Digital_sen1_4_Type(Integer32):
    """Custom type digital_sen1_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_4_Type.__name__ = "Integer32"
_Digital_sen1_4_Object = MibScalar
digital_sen1_4 = _Digital_sen1_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 1, 4),
    _Digital_sen1_4_Type()
)
digital_sen1_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_4.setStatus("mandatory")


class _Digital_sen1_5_Type(Integer32):
    """Custom type digital_sen1_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_5_Type.__name__ = "Integer32"
_Digital_sen1_5_Object = MibScalar
digital_sen1_5 = _Digital_sen1_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 1, 5),
    _Digital_sen1_5_Type()
)
digital_sen1_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_5.setStatus("mandatory")


class _Digital_sen1_6_Type(Integer32):
    """Custom type digital_sen1_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_6_Type.__name__ = "Integer32"
_Digital_sen1_6_Object = MibScalar
digital_sen1_6 = _Digital_sen1_6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 1, 6),
    _Digital_sen1_6_Type()
)
digital_sen1_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_6.setStatus("mandatory")


class _Digital_sen1_7_Type(Integer32):
    """Custom type digital_sen1_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen1_7_Type.__name__ = "Integer32"
_Digital_sen1_7_Object = MibScalar
digital_sen1_7 = _Digital_sen1_7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 1, 7),
    _Digital_sen1_7_Type()
)
digital_sen1_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_7.setStatus("mandatory")
_Digital_sen2_ObjectIdentity = ObjectIdentity
digital_sen2 = _Digital_sen2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 2)
)


class _Digital_sen2_1_Type(Integer32):
    """Custom type digital_sen2_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_1_Type.__name__ = "Integer32"
_Digital_sen2_1_Object = MibScalar
digital_sen2_1 = _Digital_sen2_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 2, 1),
    _Digital_sen2_1_Type()
)
digital_sen2_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_1.setStatus("mandatory")


class _Digital_sen2_2_Type(Integer32):
    """Custom type digital_sen2_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_2_Type.__name__ = "Integer32"
_Digital_sen2_2_Object = MibScalar
digital_sen2_2 = _Digital_sen2_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 2, 2),
    _Digital_sen2_2_Type()
)
digital_sen2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_2.setStatus("mandatory")


class _Digital_sen2_3_Type(Integer32):
    """Custom type digital_sen2_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_3_Type.__name__ = "Integer32"
_Digital_sen2_3_Object = MibScalar
digital_sen2_3 = _Digital_sen2_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 2, 3),
    _Digital_sen2_3_Type()
)
digital_sen2_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_3.setStatus("mandatory")


class _Digital_sen2_4_Type(Integer32):
    """Custom type digital_sen2_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_4_Type.__name__ = "Integer32"
_Digital_sen2_4_Object = MibScalar
digital_sen2_4 = _Digital_sen2_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 2, 4),
    _Digital_sen2_4_Type()
)
digital_sen2_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_4.setStatus("mandatory")


class _Digital_sen2_5_Type(Integer32):
    """Custom type digital_sen2_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_5_Type.__name__ = "Integer32"
_Digital_sen2_5_Object = MibScalar
digital_sen2_5 = _Digital_sen2_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 2, 5),
    _Digital_sen2_5_Type()
)
digital_sen2_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_5.setStatus("mandatory")


class _Digital_sen2_6_Type(Integer32):
    """Custom type digital_sen2_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_6_Type.__name__ = "Integer32"
_Digital_sen2_6_Object = MibScalar
digital_sen2_6 = _Digital_sen2_6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 2, 6),
    _Digital_sen2_6_Type()
)
digital_sen2_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_6.setStatus("mandatory")


class _Digital_sen2_7_Type(Integer32):
    """Custom type digital_sen2_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen2_7_Type.__name__ = "Integer32"
_Digital_sen2_7_Object = MibScalar
digital_sen2_7 = _Digital_sen2_7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 2, 7),
    _Digital_sen2_7_Type()
)
digital_sen2_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_7.setStatus("mandatory")
_Digital_sen3_ObjectIdentity = ObjectIdentity
digital_sen3 = _Digital_sen3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 3)
)


class _Digital_sen3_1_Type(Integer32):
    """Custom type digital_sen3_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_1_Type.__name__ = "Integer32"
_Digital_sen3_1_Object = MibScalar
digital_sen3_1 = _Digital_sen3_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 3, 1),
    _Digital_sen3_1_Type()
)
digital_sen3_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_1.setStatus("mandatory")


class _Digital_sen3_2_Type(Integer32):
    """Custom type digital_sen3_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_2_Type.__name__ = "Integer32"
_Digital_sen3_2_Object = MibScalar
digital_sen3_2 = _Digital_sen3_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 3, 2),
    _Digital_sen3_2_Type()
)
digital_sen3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_2.setStatus("mandatory")


class _Digital_sen3_3_Type(Integer32):
    """Custom type digital_sen3_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_3_Type.__name__ = "Integer32"
_Digital_sen3_3_Object = MibScalar
digital_sen3_3 = _Digital_sen3_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 3, 3),
    _Digital_sen3_3_Type()
)
digital_sen3_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_3.setStatus("mandatory")


class _Digital_sen3_4_Type(Integer32):
    """Custom type digital_sen3_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_4_Type.__name__ = "Integer32"
_Digital_sen3_4_Object = MibScalar
digital_sen3_4 = _Digital_sen3_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 3, 4),
    _Digital_sen3_4_Type()
)
digital_sen3_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_4.setStatus("mandatory")


class _Digital_sen3_5_Type(Integer32):
    """Custom type digital_sen3_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_5_Type.__name__ = "Integer32"
_Digital_sen3_5_Object = MibScalar
digital_sen3_5 = _Digital_sen3_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 3, 5),
    _Digital_sen3_5_Type()
)
digital_sen3_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_5.setStatus("mandatory")


class _Digital_sen3_6_Type(Integer32):
    """Custom type digital_sen3_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_6_Type.__name__ = "Integer32"
_Digital_sen3_6_Object = MibScalar
digital_sen3_6 = _Digital_sen3_6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 3, 6),
    _Digital_sen3_6_Type()
)
digital_sen3_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_6.setStatus("mandatory")


class _Digital_sen3_7_Type(Integer32):
    """Custom type digital_sen3_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen3_7_Type.__name__ = "Integer32"
_Digital_sen3_7_Object = MibScalar
digital_sen3_7 = _Digital_sen3_7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 3, 7),
    _Digital_sen3_7_Type()
)
digital_sen3_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_7.setStatus("mandatory")
_Digital_sen4_ObjectIdentity = ObjectIdentity
digital_sen4 = _Digital_sen4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 4)
)


class _Digital_sen4_1_Type(Integer32):
    """Custom type digital_sen4_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_1_Type.__name__ = "Integer32"
_Digital_sen4_1_Object = MibScalar
digital_sen4_1 = _Digital_sen4_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 4, 1),
    _Digital_sen4_1_Type()
)
digital_sen4_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_1.setStatus("mandatory")


class _Digital_sen4_2_Type(Integer32):
    """Custom type digital_sen4_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_2_Type.__name__ = "Integer32"
_Digital_sen4_2_Object = MibScalar
digital_sen4_2 = _Digital_sen4_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 4, 2),
    _Digital_sen4_2_Type()
)
digital_sen4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_2.setStatus("mandatory")


class _Digital_sen4_3_Type(Integer32):
    """Custom type digital_sen4_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_3_Type.__name__ = "Integer32"
_Digital_sen4_3_Object = MibScalar
digital_sen4_3 = _Digital_sen4_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 4, 3),
    _Digital_sen4_3_Type()
)
digital_sen4_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_3.setStatus("mandatory")


class _Digital_sen4_4_Type(Integer32):
    """Custom type digital_sen4_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_4_Type.__name__ = "Integer32"
_Digital_sen4_4_Object = MibScalar
digital_sen4_4 = _Digital_sen4_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 4, 4),
    _Digital_sen4_4_Type()
)
digital_sen4_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_4.setStatus("mandatory")


class _Digital_sen4_5_Type(Integer32):
    """Custom type digital_sen4_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_5_Type.__name__ = "Integer32"
_Digital_sen4_5_Object = MibScalar
digital_sen4_5 = _Digital_sen4_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 4, 5),
    _Digital_sen4_5_Type()
)
digital_sen4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_5.setStatus("mandatory")


class _Digital_sen4_6_Type(Integer32):
    """Custom type digital_sen4_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_6_Type.__name__ = "Integer32"
_Digital_sen4_6_Object = MibScalar
digital_sen4_6 = _Digital_sen4_6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 4, 6),
    _Digital_sen4_6_Type()
)
digital_sen4_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_6.setStatus("mandatory")


class _Digital_sen4_7_Type(Integer32):
    """Custom type digital_sen4_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen4_7_Type.__name__ = "Integer32"
_Digital_sen4_7_Object = MibScalar
digital_sen4_7 = _Digital_sen4_7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 4, 7),
    _Digital_sen4_7_Type()
)
digital_sen4_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_7.setStatus("mandatory")
_Digital_sen5_ObjectIdentity = ObjectIdentity
digital_sen5 = _Digital_sen5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 5)
)


class _Digital_sen5_1_Type(Integer32):
    """Custom type digital_sen5_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_1_Type.__name__ = "Integer32"
_Digital_sen5_1_Object = MibScalar
digital_sen5_1 = _Digital_sen5_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 5, 1),
    _Digital_sen5_1_Type()
)
digital_sen5_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_1.setStatus("mandatory")


class _Digital_sen5_2_Type(Integer32):
    """Custom type digital_sen5_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_2_Type.__name__ = "Integer32"
_Digital_sen5_2_Object = MibScalar
digital_sen5_2 = _Digital_sen5_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 5, 2),
    _Digital_sen5_2_Type()
)
digital_sen5_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_2.setStatus("mandatory")


class _Digital_sen5_3_Type(Integer32):
    """Custom type digital_sen5_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_3_Type.__name__ = "Integer32"
_Digital_sen5_3_Object = MibScalar
digital_sen5_3 = _Digital_sen5_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 5, 3),
    _Digital_sen5_3_Type()
)
digital_sen5_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_3.setStatus("mandatory")


class _Digital_sen5_4_Type(Integer32):
    """Custom type digital_sen5_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_4_Type.__name__ = "Integer32"
_Digital_sen5_4_Object = MibScalar
digital_sen5_4 = _Digital_sen5_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 5, 4),
    _Digital_sen5_4_Type()
)
digital_sen5_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_4.setStatus("mandatory")


class _Digital_sen5_5_Type(Integer32):
    """Custom type digital_sen5_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_5_Type.__name__ = "Integer32"
_Digital_sen5_5_Object = MibScalar
digital_sen5_5 = _Digital_sen5_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 5, 5),
    _Digital_sen5_5_Type()
)
digital_sen5_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_5.setStatus("mandatory")


class _Digital_sen5_6_Type(Integer32):
    """Custom type digital_sen5_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_6_Type.__name__ = "Integer32"
_Digital_sen5_6_Object = MibScalar
digital_sen5_6 = _Digital_sen5_6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 5, 6),
    _Digital_sen5_6_Type()
)
digital_sen5_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_6.setStatus("mandatory")


class _Digital_sen5_7_Type(Integer32):
    """Custom type digital_sen5_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen5_7_Type.__name__ = "Integer32"
_Digital_sen5_7_Object = MibScalar
digital_sen5_7 = _Digital_sen5_7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 5, 7),
    _Digital_sen5_7_Type()
)
digital_sen5_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_7.setStatus("mandatory")
_Digital_sen6_ObjectIdentity = ObjectIdentity
digital_sen6 = _Digital_sen6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 6)
)


class _Digital_sen6_1_Type(Integer32):
    """Custom type digital_sen6_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_1_Type.__name__ = "Integer32"
_Digital_sen6_1_Object = MibScalar
digital_sen6_1 = _Digital_sen6_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 6, 1),
    _Digital_sen6_1_Type()
)
digital_sen6_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_1.setStatus("mandatory")


class _Digital_sen6_2_Type(Integer32):
    """Custom type digital_sen6_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_2_Type.__name__ = "Integer32"
_Digital_sen6_2_Object = MibScalar
digital_sen6_2 = _Digital_sen6_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 6, 2),
    _Digital_sen6_2_Type()
)
digital_sen6_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_2.setStatus("mandatory")


class _Digital_sen6_3_Type(Integer32):
    """Custom type digital_sen6_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_3_Type.__name__ = "Integer32"
_Digital_sen6_3_Object = MibScalar
digital_sen6_3 = _Digital_sen6_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 6, 3),
    _Digital_sen6_3_Type()
)
digital_sen6_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_3.setStatus("mandatory")


class _Digital_sen6_4_Type(Integer32):
    """Custom type digital_sen6_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_4_Type.__name__ = "Integer32"
_Digital_sen6_4_Object = MibScalar
digital_sen6_4 = _Digital_sen6_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 6, 4),
    _Digital_sen6_4_Type()
)
digital_sen6_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_4.setStatus("mandatory")


class _Digital_sen6_5_Type(Integer32):
    """Custom type digital_sen6_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_5_Type.__name__ = "Integer32"
_Digital_sen6_5_Object = MibScalar
digital_sen6_5 = _Digital_sen6_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 6, 5),
    _Digital_sen6_5_Type()
)
digital_sen6_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_5.setStatus("mandatory")


class _Digital_sen6_6_Type(Integer32):
    """Custom type digital_sen6_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_6_Type.__name__ = "Integer32"
_Digital_sen6_6_Object = MibScalar
digital_sen6_6 = _Digital_sen6_6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 6, 6),
    _Digital_sen6_6_Type()
)
digital_sen6_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_6.setStatus("mandatory")


class _Digital_sen6_7_Type(Integer32):
    """Custom type digital_sen6_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen6_7_Type.__name__ = "Integer32"
_Digital_sen6_7_Object = MibScalar
digital_sen6_7 = _Digital_sen6_7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 6, 7),
    _Digital_sen6_7_Type()
)
digital_sen6_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_7.setStatus("mandatory")
_Digital_sen7_ObjectIdentity = ObjectIdentity
digital_sen7 = _Digital_sen7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 7)
)


class _Digital_sen7_1_Type(Integer32):
    """Custom type digital_sen7_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen7_1_Type.__name__ = "Integer32"
_Digital_sen7_1_Object = MibScalar
digital_sen7_1 = _Digital_sen7_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 7, 1),
    _Digital_sen7_1_Type()
)
digital_sen7_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen7_1.setStatus("mandatory")


class _Digital_sen7_2_Type(Integer32):
    """Custom type digital_sen7_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen7_2_Type.__name__ = "Integer32"
_Digital_sen7_2_Object = MibScalar
digital_sen7_2 = _Digital_sen7_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 7, 2),
    _Digital_sen7_2_Type()
)
digital_sen7_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen7_2.setStatus("mandatory")


class _Digital_sen7_3_Type(Integer32):
    """Custom type digital_sen7_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen7_3_Type.__name__ = "Integer32"
_Digital_sen7_3_Object = MibScalar
digital_sen7_3 = _Digital_sen7_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 7, 3),
    _Digital_sen7_3_Type()
)
digital_sen7_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen7_3.setStatus("mandatory")


class _Digital_sen7_4_Type(Integer32):
    """Custom type digital_sen7_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen7_4_Type.__name__ = "Integer32"
_Digital_sen7_4_Object = MibScalar
digital_sen7_4 = _Digital_sen7_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 7, 4),
    _Digital_sen7_4_Type()
)
digital_sen7_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen7_4.setStatus("mandatory")


class _Digital_sen7_5_Type(Integer32):
    """Custom type digital_sen7_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen7_5_Type.__name__ = "Integer32"
_Digital_sen7_5_Object = MibScalar
digital_sen7_5 = _Digital_sen7_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 7, 5),
    _Digital_sen7_5_Type()
)
digital_sen7_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen7_5.setStatus("mandatory")


class _Digital_sen7_6_Type(Integer32):
    """Custom type digital_sen7_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen7_6_Type.__name__ = "Integer32"
_Digital_sen7_6_Object = MibScalar
digital_sen7_6 = _Digital_sen7_6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 7, 6),
    _Digital_sen7_6_Type()
)
digital_sen7_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen7_6.setStatus("mandatory")


class _Digital_sen7_7_Type(Integer32):
    """Custom type digital_sen7_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen7_7_Type.__name__ = "Integer32"
_Digital_sen7_7_Object = MibScalar
digital_sen7_7 = _Digital_sen7_7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 7, 7),
    _Digital_sen7_7_Type()
)
digital_sen7_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen7_7.setStatus("mandatory")
_Digital_sen8_ObjectIdentity = ObjectIdentity
digital_sen8 = _Digital_sen8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 8)
)


class _Digital_sen8_1_Type(Integer32):
    """Custom type digital_sen8_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen8_1_Type.__name__ = "Integer32"
_Digital_sen8_1_Object = MibScalar
digital_sen8_1 = _Digital_sen8_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 8, 1),
    _Digital_sen8_1_Type()
)
digital_sen8_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen8_1.setStatus("mandatory")


class _Digital_sen8_2_Type(Integer32):
    """Custom type digital_sen8_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen8_2_Type.__name__ = "Integer32"
_Digital_sen8_2_Object = MibScalar
digital_sen8_2 = _Digital_sen8_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 8, 2),
    _Digital_sen8_2_Type()
)
digital_sen8_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen8_2.setStatus("mandatory")


class _Digital_sen8_3_Type(Integer32):
    """Custom type digital_sen8_3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen8_3_Type.__name__ = "Integer32"
_Digital_sen8_3_Object = MibScalar
digital_sen8_3 = _Digital_sen8_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 8, 3),
    _Digital_sen8_3_Type()
)
digital_sen8_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen8_3.setStatus("mandatory")


class _Digital_sen8_4_Type(Integer32):
    """Custom type digital_sen8_4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen8_4_Type.__name__ = "Integer32"
_Digital_sen8_4_Object = MibScalar
digital_sen8_4 = _Digital_sen8_4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 8, 4),
    _Digital_sen8_4_Type()
)
digital_sen8_4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen8_4.setStatus("mandatory")


class _Digital_sen8_5_Type(Integer32):
    """Custom type digital_sen8_5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen8_5_Type.__name__ = "Integer32"
_Digital_sen8_5_Object = MibScalar
digital_sen8_5 = _Digital_sen8_5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 8, 5),
    _Digital_sen8_5_Type()
)
digital_sen8_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen8_5.setStatus("mandatory")


class _Digital_sen8_6_Type(Integer32):
    """Custom type digital_sen8_6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen8_6_Type.__name__ = "Integer32"
_Digital_sen8_6_Object = MibScalar
digital_sen8_6 = _Digital_sen8_6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 8, 6),
    _Digital_sen8_6_Type()
)
digital_sen8_6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen8_6.setStatus("mandatory")


class _Digital_sen8_7_Type(Integer32):
    """Custom type digital_sen8_7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Digital_sen8_7_Type.__name__ = "Integer32"
_Digital_sen8_7_Object = MibScalar
digital_sen8_7 = _Digital_sen8_7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 2, 8, 7),
    _Digital_sen8_7_Type()
)
digital_sen8_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen8_7.setStatus("mandatory")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3)
)


class _Switch_sen1_Type(Integer32):
    """Custom type switch_sen1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen1_Type.__name__ = "Integer32"
_Switch_sen1_Object = MibScalar
switch_sen1 = _Switch_sen1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 1),
    _Switch_sen1_Type()
)
switch_sen1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen1.setStatus("mandatory")


class _Switch_sen2_Type(Integer32):
    """Custom type switch_sen2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen2_Type.__name__ = "Integer32"
_Switch_sen2_Object = MibScalar
switch_sen2 = _Switch_sen2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 2),
    _Switch_sen2_Type()
)
switch_sen2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen2.setStatus("mandatory")


class _Switch_sen3_Type(Integer32):
    """Custom type switch_sen3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen3_Type.__name__ = "Integer32"
_Switch_sen3_Object = MibScalar
switch_sen3 = _Switch_sen3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 3),
    _Switch_sen3_Type()
)
switch_sen3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen3.setStatus("mandatory")


class _Switch_sen4_Type(Integer32):
    """Custom type switch_sen4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen4_Type.__name__ = "Integer32"
_Switch_sen4_Object = MibScalar
switch_sen4 = _Switch_sen4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 4),
    _Switch_sen4_Type()
)
switch_sen4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen4.setStatus("mandatory")


class _Switch_sen5_Type(Integer32):
    """Custom type switch_sen5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen5_Type.__name__ = "Integer32"
_Switch_sen5_Object = MibScalar
switch_sen5 = _Switch_sen5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 5),
    _Switch_sen5_Type()
)
switch_sen5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen5.setStatus("mandatory")


class _Switch_sen6_Type(Integer32):
    """Custom type switch_sen6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen6_Type.__name__ = "Integer32"
_Switch_sen6_Object = MibScalar
switch_sen6 = _Switch_sen6_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 6),
    _Switch_sen6_Type()
)
switch_sen6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen6.setStatus("mandatory")


class _Switch_sen7_Type(Integer32):
    """Custom type switch_sen7 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen7_Type.__name__ = "Integer32"
_Switch_sen7_Object = MibScalar
switch_sen7 = _Switch_sen7_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 7),
    _Switch_sen7_Type()
)
switch_sen7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen7.setStatus("mandatory")


class _Switch_sen8_Type(Integer32):
    """Custom type switch_sen8 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen8_Type.__name__ = "Integer32"
_Switch_sen8_Object = MibScalar
switch_sen8 = _Switch_sen8_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 8),
    _Switch_sen8_Type()
)
switch_sen8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen8.setStatus("mandatory")


class _Switch_sen9_Type(Integer32):
    """Custom type switch_sen9 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen9_Type.__name__ = "Integer32"
_Switch_sen9_Object = MibScalar
switch_sen9 = _Switch_sen9_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 9),
    _Switch_sen9_Type()
)
switch_sen9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen9.setStatus("mandatory")


class _Switch_sen10_Type(Integer32):
    """Custom type switch_sen10 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen10_Type.__name__ = "Integer32"
_Switch_sen10_Object = MibScalar
switch_sen10 = _Switch_sen10_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 10),
    _Switch_sen10_Type()
)
switch_sen10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen10.setStatus("mandatory")


class _Switch_sen11_Type(Integer32):
    """Custom type switch_sen11 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen11_Type.__name__ = "Integer32"
_Switch_sen11_Object = MibScalar
switch_sen11 = _Switch_sen11_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 11),
    _Switch_sen11_Type()
)
switch_sen11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen11.setStatus("mandatory")


class _Switch_sen12_Type(Integer32):
    """Custom type switch_sen12 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen12_Type.__name__ = "Integer32"
_Switch_sen12_Object = MibScalar
switch_sen12 = _Switch_sen12_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 12),
    _Switch_sen12_Type()
)
switch_sen12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen12.setStatus("mandatory")


class _Switch_sen13_Type(Integer32):
    """Custom type switch_sen13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen13_Type.__name__ = "Integer32"
_Switch_sen13_Object = MibScalar
switch_sen13 = _Switch_sen13_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 13),
    _Switch_sen13_Type()
)
switch_sen13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen13.setStatus("mandatory")


class _Switch_sen14_Type(Integer32):
    """Custom type switch_sen14 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen14_Type.__name__ = "Integer32"
_Switch_sen14_Object = MibScalar
switch_sen14 = _Switch_sen14_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 14),
    _Switch_sen14_Type()
)
switch_sen14.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen14.setStatus("mandatory")


class _Switch_sen15_Type(Integer32):
    """Custom type switch_sen15 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen15_Type.__name__ = "Integer32"
_Switch_sen15_Object = MibScalar
switch_sen15 = _Switch_sen15_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 15),
    _Switch_sen15_Type()
)
switch_sen15.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen15.setStatus("mandatory")


class _Switch_sen16_Type(Integer32):
    """Custom type switch_sen16 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen16_Type.__name__ = "Integer32"
_Switch_sen16_Object = MibScalar
switch_sen16 = _Switch_sen16_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 1, 3, 16),
    _Switch_sen16_Type()
)
switch_sen16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen16.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 2)
)
_Alarmmessage_Type = OctetString
_Alarmmessage_Object = MibScalar
alarmmessage = _Alarmmessage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 2, 1),
    _Alarmmessage_Type()
)
alarmmessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmmessage.setStatus("mandatory")
_Externalrelays_ObjectIdentity = ObjectIdentity
externalrelays = _Externalrelays_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3)
)
_Externalrelay1_ObjectIdentity = ObjectIdentity
externalrelay1 = _Externalrelay1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 1)
)


class _Externalrelay1_element_one_Type(Integer32):
    """Custom type externalrelay1_element_one based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay1_element_one_Type.__name__ = "Integer32"
_Externalrelay1_element_one_Object = MibScalar
externalrelay1_element_one = _Externalrelay1_element_one_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 1, 1),
    _Externalrelay1_element_one_Type()
)
externalrelay1_element_one.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay1_element_one.setStatus("mandatory")


class _Externalrelay1_element_two_Type(Integer32):
    """Custom type externalrelay1_element_two based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay1_element_two_Type.__name__ = "Integer32"
_Externalrelay1_element_two_Object = MibScalar
externalrelay1_element_two = _Externalrelay1_element_two_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 1, 2),
    _Externalrelay1_element_two_Type()
)
externalrelay1_element_two.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay1_element_two.setStatus("mandatory")


class _Externalrelay1_element_three_Type(Integer32):
    """Custom type externalrelay1_element_three based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay1_element_three_Type.__name__ = "Integer32"
_Externalrelay1_element_three_Object = MibScalar
externalrelay1_element_three = _Externalrelay1_element_three_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 1, 3),
    _Externalrelay1_element_three_Type()
)
externalrelay1_element_three.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay1_element_three.setStatus("mandatory")


class _Externalrelay1_element_four_Type(Integer32):
    """Custom type externalrelay1_element_four based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay1_element_four_Type.__name__ = "Integer32"
_Externalrelay1_element_four_Object = MibScalar
externalrelay1_element_four = _Externalrelay1_element_four_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 1, 4),
    _Externalrelay1_element_four_Type()
)
externalrelay1_element_four.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay1_element_four.setStatus("mandatory")


class _Externalrelay1_element_five_Type(Integer32):
    """Custom type externalrelay1_element_five based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay1_element_five_Type.__name__ = "Integer32"
_Externalrelay1_element_five_Object = MibScalar
externalrelay1_element_five = _Externalrelay1_element_five_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 1, 5),
    _Externalrelay1_element_five_Type()
)
externalrelay1_element_five.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay1_element_five.setStatus("mandatory")


class _Externalrelay1_element_six_Type(Integer32):
    """Custom type externalrelay1_element_six based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay1_element_six_Type.__name__ = "Integer32"
_Externalrelay1_element_six_Object = MibScalar
externalrelay1_element_six = _Externalrelay1_element_six_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 1, 6),
    _Externalrelay1_element_six_Type()
)
externalrelay1_element_six.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay1_element_six.setStatus("mandatory")


class _Externalrelay1_element_seven_Type(Integer32):
    """Custom type externalrelay1_element_seven based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay1_element_seven_Type.__name__ = "Integer32"
_Externalrelay1_element_seven_Object = MibScalar
externalrelay1_element_seven = _Externalrelay1_element_seven_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 1, 7),
    _Externalrelay1_element_seven_Type()
)
externalrelay1_element_seven.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay1_element_seven.setStatus("mandatory")


class _Externalrelay1_element_eight_Type(Integer32):
    """Custom type externalrelay1_element_eight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay1_element_eight_Type.__name__ = "Integer32"
_Externalrelay1_element_eight_Object = MibScalar
externalrelay1_element_eight = _Externalrelay1_element_eight_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 1, 8),
    _Externalrelay1_element_eight_Type()
)
externalrelay1_element_eight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay1_element_eight.setStatus("mandatory")
_Externalrelay2_ObjectIdentity = ObjectIdentity
externalrelay2 = _Externalrelay2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 2)
)


class _Externalrelay2_element_one_Type(Integer32):
    """Custom type externalrelay2_element_one based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay2_element_one_Type.__name__ = "Integer32"
_Externalrelay2_element_one_Object = MibScalar
externalrelay2_element_one = _Externalrelay2_element_one_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 2, 1),
    _Externalrelay2_element_one_Type()
)
externalrelay2_element_one.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay2_element_one.setStatus("mandatory")


class _Externalrelay2_element_two_Type(Integer32):
    """Custom type externalrelay2_element_two based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay2_element_two_Type.__name__ = "Integer32"
_Externalrelay2_element_two_Object = MibScalar
externalrelay2_element_two = _Externalrelay2_element_two_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 2, 2),
    _Externalrelay2_element_two_Type()
)
externalrelay2_element_two.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay2_element_two.setStatus("mandatory")


class _Externalrelay2_element_three_Type(Integer32):
    """Custom type externalrelay2_element_three based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay2_element_three_Type.__name__ = "Integer32"
_Externalrelay2_element_three_Object = MibScalar
externalrelay2_element_three = _Externalrelay2_element_three_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 2, 3),
    _Externalrelay2_element_three_Type()
)
externalrelay2_element_three.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay2_element_three.setStatus("mandatory")


class _Externalrelay2_element_four_Type(Integer32):
    """Custom type externalrelay2_element_four based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay2_element_four_Type.__name__ = "Integer32"
_Externalrelay2_element_four_Object = MibScalar
externalrelay2_element_four = _Externalrelay2_element_four_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 2, 4),
    _Externalrelay2_element_four_Type()
)
externalrelay2_element_four.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay2_element_four.setStatus("mandatory")


class _Externalrelay2_element_five_Type(Integer32):
    """Custom type externalrelay2_element_five based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay2_element_five_Type.__name__ = "Integer32"
_Externalrelay2_element_five_Object = MibScalar
externalrelay2_element_five = _Externalrelay2_element_five_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 2, 5),
    _Externalrelay2_element_five_Type()
)
externalrelay2_element_five.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay2_element_five.setStatus("mandatory")


class _Externalrelay2_element_six_Type(Integer32):
    """Custom type externalrelay2_element_six based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay2_element_six_Type.__name__ = "Integer32"
_Externalrelay2_element_six_Object = MibScalar
externalrelay2_element_six = _Externalrelay2_element_six_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 2, 6),
    _Externalrelay2_element_six_Type()
)
externalrelay2_element_six.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay2_element_six.setStatus("mandatory")


class _Externalrelay2_element_seven_Type(Integer32):
    """Custom type externalrelay2_element_seven based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay2_element_seven_Type.__name__ = "Integer32"
_Externalrelay2_element_seven_Object = MibScalar
externalrelay2_element_seven = _Externalrelay2_element_seven_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 2, 7),
    _Externalrelay2_element_seven_Type()
)
externalrelay2_element_seven.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay2_element_seven.setStatus("mandatory")


class _Externalrelay2_element_eight_Type(Integer32):
    """Custom type externalrelay2_element_eight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Externalrelay2_element_eight_Type.__name__ = "Integer32"
_Externalrelay2_element_eight_Object = MibScalar
externalrelay2_element_eight = _Externalrelay2_element_eight_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 11, 3, 2, 8),
    _Externalrelay2_element_eight_Type()
)
externalrelay2_element_eight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    externalrelay2_element_eight.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROOMALERT32S-MIB",
    **{"avtech": avtech,
       "products": products,
       "roomalert32S": roomalert32S,
       "sensors": sensors,
       "internal": internal,
       "temperature": temperature,
       "internal-tempf": internal_tempf,
       "internal-tempc": internal_tempc,
       "humidity": humidity,
       "internal-humidity": internal_humidity,
       "power": power,
       "internal-power": internal_power,
       "heat-index": heat_index,
       "internal-heat-index": internal_heat_index,
       "internal-heat-indexC": internal_heat_indexC,
       "analog": analog,
       "internal-analog1": internal_analog1,
       "internal-analog2": internal_analog2,
       "relay": relay,
       "internal-relay1": internal_relay1,
       "internal-relay2": internal_relay2,
       "dew-point": dew_point,
       "internal-dew-point-c": internal_dew_point_c,
       "internal-dew-point-f": internal_dew_point_f,
       "digital": digital,
       "digital-sen1": digital_sen1,
       "digital-sen1-1": digital_sen1_1,
       "digital-sen1-2": digital_sen1_2,
       "digital-sen1-3": digital_sen1_3,
       "digital-sen1-4": digital_sen1_4,
       "digital-sen1-5": digital_sen1_5,
       "digital-sen1-6": digital_sen1_6,
       "digital-sen1-7": digital_sen1_7,
       "digital-sen2": digital_sen2,
       "digital-sen2-1": digital_sen2_1,
       "digital-sen2-2": digital_sen2_2,
       "digital-sen2-3": digital_sen2_3,
       "digital-sen2-4": digital_sen2_4,
       "digital-sen2-5": digital_sen2_5,
       "digital-sen2-6": digital_sen2_6,
       "digital-sen2-7": digital_sen2_7,
       "digital-sen3": digital_sen3,
       "digital-sen3-1": digital_sen3_1,
       "digital-sen3-2": digital_sen3_2,
       "digital-sen3-3": digital_sen3_3,
       "digital-sen3-4": digital_sen3_4,
       "digital-sen3-5": digital_sen3_5,
       "digital-sen3-6": digital_sen3_6,
       "digital-sen3-7": digital_sen3_7,
       "digital-sen4": digital_sen4,
       "digital-sen4-1": digital_sen4_1,
       "digital-sen4-2": digital_sen4_2,
       "digital-sen4-3": digital_sen4_3,
       "digital-sen4-4": digital_sen4_4,
       "digital-sen4-5": digital_sen4_5,
       "digital-sen4-6": digital_sen4_6,
       "digital-sen4-7": digital_sen4_7,
       "digital-sen5": digital_sen5,
       "digital-sen5-1": digital_sen5_1,
       "digital-sen5-2": digital_sen5_2,
       "digital-sen5-3": digital_sen5_3,
       "digital-sen5-4": digital_sen5_4,
       "digital-sen5-5": digital_sen5_5,
       "digital-sen5-6": digital_sen5_6,
       "digital-sen5-7": digital_sen5_7,
       "digital-sen6": digital_sen6,
       "digital-sen6-1": digital_sen6_1,
       "digital-sen6-2": digital_sen6_2,
       "digital-sen6-3": digital_sen6_3,
       "digital-sen6-4": digital_sen6_4,
       "digital-sen6-5": digital_sen6_5,
       "digital-sen6-6": digital_sen6_6,
       "digital-sen6-7": digital_sen6_7,
       "digital-sen7": digital_sen7,
       "digital-sen7-1": digital_sen7_1,
       "digital-sen7-2": digital_sen7_2,
       "digital-sen7-3": digital_sen7_3,
       "digital-sen7-4": digital_sen7_4,
       "digital-sen7-5": digital_sen7_5,
       "digital-sen7-6": digital_sen7_6,
       "digital-sen7-7": digital_sen7_7,
       "digital-sen8": digital_sen8,
       "digital-sen8-1": digital_sen8_1,
       "digital-sen8-2": digital_sen8_2,
       "digital-sen8-3": digital_sen8_3,
       "digital-sen8-4": digital_sen8_4,
       "digital-sen8-5": digital_sen8_5,
       "digital-sen8-6": digital_sen8_6,
       "digital-sen8-7": digital_sen8_7,
       "switch": switch,
       "switch-sen1": switch_sen1,
       "switch-sen2": switch_sen2,
       "switch-sen3": switch_sen3,
       "switch-sen4": switch_sen4,
       "switch-sen5": switch_sen5,
       "switch-sen6": switch_sen6,
       "switch-sen7": switch_sen7,
       "switch-sen8": switch_sen8,
       "switch-sen9": switch_sen9,
       "switch-sen10": switch_sen10,
       "switch-sen11": switch_sen11,
       "switch-sen12": switch_sen12,
       "switch-sen13": switch_sen13,
       "switch-sen14": switch_sen14,
       "switch-sen15": switch_sen15,
       "switch-sen16": switch_sen16,
       "traps": traps,
       "alarmmessage": alarmmessage,
       "externalrelays": externalrelays,
       "externalrelay1": externalrelay1,
       "externalrelay1-element-one": externalrelay1_element_one,
       "externalrelay1-element-two": externalrelay1_element_two,
       "externalrelay1-element-three": externalrelay1_element_three,
       "externalrelay1-element-four": externalrelay1_element_four,
       "externalrelay1-element-five": externalrelay1_element_five,
       "externalrelay1-element-six": externalrelay1_element_six,
       "externalrelay1-element-seven": externalrelay1_element_seven,
       "externalrelay1-element-eight": externalrelay1_element_eight,
       "externalrelay2": externalrelay2,
       "externalrelay2-element-one": externalrelay2_element_one,
       "externalrelay2-element-two": externalrelay2_element_two,
       "externalrelay2-element-three": externalrelay2_element_three,
       "externalrelay2-element-four": externalrelay2_element_four,
       "externalrelay2-element-five": externalrelay2_element_five,
       "externalrelay2-element-six": externalrelay2_element_six,
       "externalrelay2-element-seven": externalrelay2_element_seven,
       "externalrelay2-element-eight": externalrelay2_element_eight}
)
