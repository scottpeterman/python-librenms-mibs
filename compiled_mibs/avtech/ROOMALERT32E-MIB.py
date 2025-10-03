# SNMP MIB module (ROOMALERT32E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\avtech\ROOMALERT32E-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:14 2025
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
 NotificationType,
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
    "NotificationType",
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
_Roomalert32E_ObjectIdentity = ObjectIdentity
roomalert32E = _Roomalert32E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1)
)
_Internal_ObjectIdentity = ObjectIdentity
internal = _Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1)
)
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 1, 2),
    _Internal_tempc_Type()
)
internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_tempc.setStatus("mandatory")
_Humidity_ObjectIdentity = ObjectIdentity
humidity = _Humidity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 2, 1),
    _Internal_humidity_Type()
)
internal_humidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_humidity.setStatus("mandatory")
_Power_ObjectIdentity = ObjectIdentity
power = _Power_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 3, 1),
    _Internal_power_Type()
)
internal_power.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_power.setStatus("mandatory")
_Heat_index_ObjectIdentity = ObjectIdentity
heat_index = _Heat_index_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 4)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 4, 2),
    _Internal_heat_indexC_Type()
)
internal_heat_indexC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_heat_indexC.setStatus("optional")
_Analog_ObjectIdentity = ObjectIdentity
analog = _Analog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 5, 2),
    _Internal_analog2_Type()
)
internal_analog2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_analog2.setStatus("mandatory")
_Relay_ObjectIdentity = ObjectIdentity
relay = _Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 6)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 6, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 1, 6, 2),
    _Internal_relay2_Type()
)
internal_relay2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    internal_relay2.setStatus("mandatory")
_Digital_ObjectIdentity = ObjectIdentity
digital = _Digital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2)
)
_Digital_sen1_ObjectIdentity = ObjectIdentity
digital_sen1 = _Digital_sen1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 1, 5),
    _Digital_sen1_5_Type()
)
digital_sen1_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_5.setStatus("mandatory")
_Digital_sen2_ObjectIdentity = ObjectIdentity
digital_sen2 = _Digital_sen2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 2)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 2, 5),
    _Digital_sen2_5_Type()
)
digital_sen2_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_5.setStatus("mandatory")
_Digital_sen3_ObjectIdentity = ObjectIdentity
digital_sen3 = _Digital_sen3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 3)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 3, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 3, 5),
    _Digital_sen3_5_Type()
)
digital_sen3_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_5.setStatus("mandatory")
_Digital_sen4_ObjectIdentity = ObjectIdentity
digital_sen4 = _Digital_sen4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 4)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 4, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 4, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 4, 5),
    _Digital_sen4_5_Type()
)
digital_sen4_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen4_5.setStatus("mandatory")
_Digital_sen5_ObjectIdentity = ObjectIdentity
digital_sen5 = _Digital_sen5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 5)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 5, 5),
    _Digital_sen5_5_Type()
)
digital_sen5_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen5_5.setStatus("mandatory")
_Digital_sen6_ObjectIdentity = ObjectIdentity
digital_sen6 = _Digital_sen6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 6)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 6, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 6, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 6, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 6, 5),
    _Digital_sen6_5_Type()
)
digital_sen6_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen6_5.setStatus("mandatory")
_Digital_sen7_ObjectIdentity = ObjectIdentity
digital_sen7 = _Digital_sen7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 7)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 7, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 7, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 7, 5),
    _Digital_sen7_5_Type()
)
digital_sen7_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen7_5.setStatus("mandatory")
_Digital_sen8_ObjectIdentity = ObjectIdentity
digital_sen8 = _Digital_sen8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 8)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 8, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 8, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 8, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 8, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 2, 8, 5),
    _Digital_sen8_5_Type()
)
digital_sen8_5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen8_5.setStatus("mandatory")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 6),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 7),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 8),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 9),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 10),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 11),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 12),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 13),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 14),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 15),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 3, 16),
    _Switch_sen16_Type()
)
switch_sen16.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen16.setStatus("mandatory")
_Wireless_ObjectIdentity = ObjectIdentity
wireless = _Wireless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4)
)
_Wish_1_ObjectIdentity = ObjectIdentity
wish_1 = _Wish_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1)
)


class _Wish_1_enabled_Type(Integer32):
    """Custom type wish_1_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_1_enabled_Type.__name__ = "Integer32"
_Wish_1_enabled_Object = MibScalar
wish_1_enabled = _Wish_1_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 1),
    _Wish_1_enabled_Type()
)
wish_1_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_enabled.setStatus("mandatory")
_Wish_1_serial_num_Type = OctetString
_Wish_1_serial_num_Object = MibScalar
wish_1_serial_num = _Wish_1_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 2),
    _Wish_1_serial_num_Type()
)
wish_1_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_serial_num.setStatus("mandatory")


class _Wish_1_updates_Type(Integer32):
    """Custom type wish_1_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_updates_Type.__name__ = "Integer32"
_Wish_1_updates_Object = MibScalar
wish_1_updates = _Wish_1_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 3),
    _Wish_1_updates_Type()
)
wish_1_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_updates.setStatus("mandatory")
_Wish_1_sensors_ObjectIdentity = ObjectIdentity
wish_1_sensors = _Wish_1_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4)
)
_Wish_1_internal_ObjectIdentity = ObjectIdentity
wish_1_internal = _Wish_1_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 1)
)


class _Wish_1_battery_voltage_Type(Integer32):
    """Custom type wish_1_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_battery_voltage_Type.__name__ = "Integer32"
_Wish_1_battery_voltage_Object = MibScalar
wish_1_battery_voltage = _Wish_1_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 1, 1),
    _Wish_1_battery_voltage_Type()
)
wish_1_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_battery_voltage.setStatus("mandatory")


class _Wish_1_internal_tempc_Type(Integer32):
    """Custom type wish_1_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_internal_tempc_Type.__name__ = "Integer32"
_Wish_1_internal_tempc_Object = MibScalar
wish_1_internal_tempc = _Wish_1_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 1, 2),
    _Wish_1_internal_tempc_Type()
)
wish_1_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_internal_tempc.setStatus("mandatory")


class _Wish_1_internal_tempf_Type(Integer32):
    """Custom type wish_1_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_internal_tempf_Type.__name__ = "Integer32"
_Wish_1_internal_tempf_Object = MibScalar
wish_1_internal_tempf = _Wish_1_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 1, 3),
    _Wish_1_internal_tempf_Type()
)
wish_1_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_internal_tempf.setStatus("mandatory")
_Wish_1_external_ObjectIdentity = ObjectIdentity
wish_1_external = _Wish_1_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2)
)
_Wish_1_external_1_ObjectIdentity = ObjectIdentity
wish_1_external_1 = _Wish_1_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 1)
)


class _Wish_1_external_1_type_Type(Integer32):
    """Custom type wish_1_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_1_type_Type.__name__ = "Integer32"
_Wish_1_external_1_type_Object = MibScalar
wish_1_external_1_type = _Wish_1_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 1, 1),
    _Wish_1_external_1_type_Type()
)
wish_1_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_1_type.setStatus("mandatory")


class _Wish_1_external_1_val1_Type(Integer32):
    """Custom type wish_1_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_1_val1_Type.__name__ = "Integer32"
_Wish_1_external_1_val1_Object = MibScalar
wish_1_external_1_val1 = _Wish_1_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 1, 2),
    _Wish_1_external_1_val1_Type()
)
wish_1_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_1_val1.setStatus("mandatory")


class _Wish_1_external_1_val2_Type(Integer32):
    """Custom type wish_1_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_1_val2_Type.__name__ = "Integer32"
_Wish_1_external_1_val2_Object = MibScalar
wish_1_external_1_val2 = _Wish_1_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 1, 3),
    _Wish_1_external_1_val2_Type()
)
wish_1_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_1_val2.setStatus("mandatory")


class _Wish_1_external_1_val3_Type(Integer32):
    """Custom type wish_1_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_1_val3_Type.__name__ = "Integer32"
_Wish_1_external_1_val3_Object = MibScalar
wish_1_external_1_val3 = _Wish_1_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 1, 4),
    _Wish_1_external_1_val3_Type()
)
wish_1_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_1_val3.setStatus("mandatory")


class _Wish_1_external_1_val4_Type(Integer32):
    """Custom type wish_1_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_1_val4_Type.__name__ = "Integer32"
_Wish_1_external_1_val4_Object = MibScalar
wish_1_external_1_val4 = _Wish_1_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 1, 5),
    _Wish_1_external_1_val4_Type()
)
wish_1_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_1_val4.setStatus("mandatory")


class _Wish_1_external_1_val5_Type(Integer32):
    """Custom type wish_1_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_1_val5_Type.__name__ = "Integer32"
_Wish_1_external_1_val5_Object = MibScalar
wish_1_external_1_val5 = _Wish_1_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 1, 6),
    _Wish_1_external_1_val5_Type()
)
wish_1_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_1_val5.setStatus("mandatory")
_Wish_1_external_2_ObjectIdentity = ObjectIdentity
wish_1_external_2 = _Wish_1_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 2)
)


class _Wish_1_external_2_type_Type(Integer32):
    """Custom type wish_1_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_2_type_Type.__name__ = "Integer32"
_Wish_1_external_2_type_Object = MibScalar
wish_1_external_2_type = _Wish_1_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 2, 1),
    _Wish_1_external_2_type_Type()
)
wish_1_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_2_type.setStatus("mandatory")


class _Wish_1_external_2_val1_Type(Integer32):
    """Custom type wish_1_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_2_val1_Type.__name__ = "Integer32"
_Wish_1_external_2_val1_Object = MibScalar
wish_1_external_2_val1 = _Wish_1_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 2, 2),
    _Wish_1_external_2_val1_Type()
)
wish_1_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_2_val1.setStatus("mandatory")


class _Wish_1_external_2_val2_Type(Integer32):
    """Custom type wish_1_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_2_val2_Type.__name__ = "Integer32"
_Wish_1_external_2_val2_Object = MibScalar
wish_1_external_2_val2 = _Wish_1_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 2, 3),
    _Wish_1_external_2_val2_Type()
)
wish_1_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_2_val2.setStatus("mandatory")


class _Wish_1_external_2_val3_Type(Integer32):
    """Custom type wish_1_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_2_val3_Type.__name__ = "Integer32"
_Wish_1_external_2_val3_Object = MibScalar
wish_1_external_2_val3 = _Wish_1_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 2, 4),
    _Wish_1_external_2_val3_Type()
)
wish_1_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_2_val3.setStatus("mandatory")


class _Wish_1_external_2_val4_Type(Integer32):
    """Custom type wish_1_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_2_val4_Type.__name__ = "Integer32"
_Wish_1_external_2_val4_Object = MibScalar
wish_1_external_2_val4 = _Wish_1_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 2, 5),
    _Wish_1_external_2_val4_Type()
)
wish_1_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_2_val4.setStatus("mandatory")


class _Wish_1_external_2_val5_Type(Integer32):
    """Custom type wish_1_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_1_external_2_val5_Type.__name__ = "Integer32"
_Wish_1_external_2_val5_Object = MibScalar
wish_1_external_2_val5 = _Wish_1_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 2, 6),
    _Wish_1_external_2_val5_Type()
)
wish_1_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_2_val5.setStatus("mandatory")


class _Wish_1_external_switch_Type(Integer32):
    """Custom type wish_1_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_1_external_switch_Type.__name__ = "Integer32"
_Wish_1_external_switch_Object = MibScalar
wish_1_external_switch = _Wish_1_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 1, 4, 2, 3),
    _Wish_1_external_switch_Type()
)
wish_1_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_1_external_switch.setStatus("mandatory")
_Wish_2_ObjectIdentity = ObjectIdentity
wish_2 = _Wish_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2)
)


class _Wish_2_enabled_Type(Integer32):
    """Custom type wish_2_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_2_enabled_Type.__name__ = "Integer32"
_Wish_2_enabled_Object = MibScalar
wish_2_enabled = _Wish_2_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 1),
    _Wish_2_enabled_Type()
)
wish_2_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_enabled.setStatus("mandatory")
_Wish_2_serial_num_Type = OctetString
_Wish_2_serial_num_Object = MibScalar
wish_2_serial_num = _Wish_2_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 2),
    _Wish_2_serial_num_Type()
)
wish_2_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_serial_num.setStatus("mandatory")


class _Wish_2_updates_Type(Integer32):
    """Custom type wish_2_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_updates_Type.__name__ = "Integer32"
_Wish_2_updates_Object = MibScalar
wish_2_updates = _Wish_2_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 3),
    _Wish_2_updates_Type()
)
wish_2_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_updates.setStatus("mandatory")
_Wish_2_sensors_ObjectIdentity = ObjectIdentity
wish_2_sensors = _Wish_2_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4)
)
_Wish_2_internal_ObjectIdentity = ObjectIdentity
wish_2_internal = _Wish_2_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 1)
)


class _Wish_2_battery_voltage_Type(Integer32):
    """Custom type wish_2_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_battery_voltage_Type.__name__ = "Integer32"
_Wish_2_battery_voltage_Object = MibScalar
wish_2_battery_voltage = _Wish_2_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 1, 1),
    _Wish_2_battery_voltage_Type()
)
wish_2_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_battery_voltage.setStatus("mandatory")


class _Wish_2_internal_tempc_Type(Integer32):
    """Custom type wish_2_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_internal_tempc_Type.__name__ = "Integer32"
_Wish_2_internal_tempc_Object = MibScalar
wish_2_internal_tempc = _Wish_2_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 1, 2),
    _Wish_2_internal_tempc_Type()
)
wish_2_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_internal_tempc.setStatus("mandatory")


class _Wish_2_internal_tempf_Type(Integer32):
    """Custom type wish_2_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_internal_tempf_Type.__name__ = "Integer32"
_Wish_2_internal_tempf_Object = MibScalar
wish_2_internal_tempf = _Wish_2_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 1, 3),
    _Wish_2_internal_tempf_Type()
)
wish_2_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_internal_tempf.setStatus("mandatory")
_Wish_2_external_ObjectIdentity = ObjectIdentity
wish_2_external = _Wish_2_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2)
)
_Wish_2_external_1_ObjectIdentity = ObjectIdentity
wish_2_external_1 = _Wish_2_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 1)
)


class _Wish_2_external_1_type_Type(Integer32):
    """Custom type wish_2_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_1_type_Type.__name__ = "Integer32"
_Wish_2_external_1_type_Object = MibScalar
wish_2_external_1_type = _Wish_2_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 1, 1),
    _Wish_2_external_1_type_Type()
)
wish_2_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_1_type.setStatus("mandatory")


class _Wish_2_external_1_val1_Type(Integer32):
    """Custom type wish_2_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_1_val1_Type.__name__ = "Integer32"
_Wish_2_external_1_val1_Object = MibScalar
wish_2_external_1_val1 = _Wish_2_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 1, 2),
    _Wish_2_external_1_val1_Type()
)
wish_2_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_1_val1.setStatus("mandatory")


class _Wish_2_external_1_val2_Type(Integer32):
    """Custom type wish_2_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_1_val2_Type.__name__ = "Integer32"
_Wish_2_external_1_val2_Object = MibScalar
wish_2_external_1_val2 = _Wish_2_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 1, 3),
    _Wish_2_external_1_val2_Type()
)
wish_2_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_1_val2.setStatus("mandatory")


class _Wish_2_external_1_val3_Type(Integer32):
    """Custom type wish_2_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_1_val3_Type.__name__ = "Integer32"
_Wish_2_external_1_val3_Object = MibScalar
wish_2_external_1_val3 = _Wish_2_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 1, 4),
    _Wish_2_external_1_val3_Type()
)
wish_2_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_1_val3.setStatus("mandatory")


class _Wish_2_external_1_val4_Type(Integer32):
    """Custom type wish_2_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_1_val4_Type.__name__ = "Integer32"
_Wish_2_external_1_val4_Object = MibScalar
wish_2_external_1_val4 = _Wish_2_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 1, 5),
    _Wish_2_external_1_val4_Type()
)
wish_2_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_1_val4.setStatus("mandatory")


class _Wish_2_external_1_val5_Type(Integer32):
    """Custom type wish_2_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_1_val5_Type.__name__ = "Integer32"
_Wish_2_external_1_val5_Object = MibScalar
wish_2_external_1_val5 = _Wish_2_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 1, 6),
    _Wish_2_external_1_val5_Type()
)
wish_2_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_1_val5.setStatus("mandatory")
_Wish_2_external_2_ObjectIdentity = ObjectIdentity
wish_2_external_2 = _Wish_2_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 2)
)


class _Wish_2_external_2_type_Type(Integer32):
    """Custom type wish_2_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_2_type_Type.__name__ = "Integer32"
_Wish_2_external_2_type_Object = MibScalar
wish_2_external_2_type = _Wish_2_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 2, 1),
    _Wish_2_external_2_type_Type()
)
wish_2_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_2_type.setStatus("mandatory")


class _Wish_2_external_2_val1_Type(Integer32):
    """Custom type wish_2_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_2_val1_Type.__name__ = "Integer32"
_Wish_2_external_2_val1_Object = MibScalar
wish_2_external_2_val1 = _Wish_2_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 2, 2),
    _Wish_2_external_2_val1_Type()
)
wish_2_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_2_val1.setStatus("mandatory")


class _Wish_2_external_2_val2_Type(Integer32):
    """Custom type wish_2_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_2_val2_Type.__name__ = "Integer32"
_Wish_2_external_2_val2_Object = MibScalar
wish_2_external_2_val2 = _Wish_2_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 2, 3),
    _Wish_2_external_2_val2_Type()
)
wish_2_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_2_val2.setStatus("mandatory")


class _Wish_2_external_2_val3_Type(Integer32):
    """Custom type wish_2_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_2_val3_Type.__name__ = "Integer32"
_Wish_2_external_2_val3_Object = MibScalar
wish_2_external_2_val3 = _Wish_2_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 2, 4),
    _Wish_2_external_2_val3_Type()
)
wish_2_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_2_val3.setStatus("mandatory")


class _Wish_2_external_2_val4_Type(Integer32):
    """Custom type wish_2_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_2_val4_Type.__name__ = "Integer32"
_Wish_2_external_2_val4_Object = MibScalar
wish_2_external_2_val4 = _Wish_2_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 2, 5),
    _Wish_2_external_2_val4_Type()
)
wish_2_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_2_val4.setStatus("mandatory")


class _Wish_2_external_2_val5_Type(Integer32):
    """Custom type wish_2_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_2_external_2_val5_Type.__name__ = "Integer32"
_Wish_2_external_2_val5_Object = MibScalar
wish_2_external_2_val5 = _Wish_2_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 2, 6),
    _Wish_2_external_2_val5_Type()
)
wish_2_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_2_val5.setStatus("mandatory")


class _Wish_2_external_switch_Type(Integer32):
    """Custom type wish_2_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_2_external_switch_Type.__name__ = "Integer32"
_Wish_2_external_switch_Object = MibScalar
wish_2_external_switch = _Wish_2_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 2, 4, 2, 3),
    _Wish_2_external_switch_Type()
)
wish_2_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_2_external_switch.setStatus("mandatory")
_Wish_3_ObjectIdentity = ObjectIdentity
wish_3 = _Wish_3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3)
)


class _Wish_3_enabled_Type(Integer32):
    """Custom type wish_3_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_3_enabled_Type.__name__ = "Integer32"
_Wish_3_enabled_Object = MibScalar
wish_3_enabled = _Wish_3_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 1),
    _Wish_3_enabled_Type()
)
wish_3_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_enabled.setStatus("mandatory")
_Wish_3_serial_num_Type = OctetString
_Wish_3_serial_num_Object = MibScalar
wish_3_serial_num = _Wish_3_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 2),
    _Wish_3_serial_num_Type()
)
wish_3_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_serial_num.setStatus("mandatory")


class _Wish_3_updates_Type(Integer32):
    """Custom type wish_3_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_updates_Type.__name__ = "Integer32"
_Wish_3_updates_Object = MibScalar
wish_3_updates = _Wish_3_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 3),
    _Wish_3_updates_Type()
)
wish_3_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_updates.setStatus("mandatory")
_Wish_3_sensors_ObjectIdentity = ObjectIdentity
wish_3_sensors = _Wish_3_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4)
)
_Wish_3_internal_ObjectIdentity = ObjectIdentity
wish_3_internal = _Wish_3_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 1)
)


class _Wish_3_battery_voltage_Type(Integer32):
    """Custom type wish_3_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_battery_voltage_Type.__name__ = "Integer32"
_Wish_3_battery_voltage_Object = MibScalar
wish_3_battery_voltage = _Wish_3_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 1, 1),
    _Wish_3_battery_voltage_Type()
)
wish_3_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_battery_voltage.setStatus("mandatory")


class _Wish_3_internal_tempc_Type(Integer32):
    """Custom type wish_3_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_internal_tempc_Type.__name__ = "Integer32"
_Wish_3_internal_tempc_Object = MibScalar
wish_3_internal_tempc = _Wish_3_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 1, 2),
    _Wish_3_internal_tempc_Type()
)
wish_3_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_internal_tempc.setStatus("mandatory")


class _Wish_3_internal_tempf_Type(Integer32):
    """Custom type wish_3_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_internal_tempf_Type.__name__ = "Integer32"
_Wish_3_internal_tempf_Object = MibScalar
wish_3_internal_tempf = _Wish_3_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 1, 3),
    _Wish_3_internal_tempf_Type()
)
wish_3_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_internal_tempf.setStatus("mandatory")
_Wish_3_external_ObjectIdentity = ObjectIdentity
wish_3_external = _Wish_3_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2)
)
_Wish_3_external_1_ObjectIdentity = ObjectIdentity
wish_3_external_1 = _Wish_3_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 1)
)


class _Wish_3_external_1_type_Type(Integer32):
    """Custom type wish_3_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_1_type_Type.__name__ = "Integer32"
_Wish_3_external_1_type_Object = MibScalar
wish_3_external_1_type = _Wish_3_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 1, 1),
    _Wish_3_external_1_type_Type()
)
wish_3_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_1_type.setStatus("mandatory")


class _Wish_3_external_1_val1_Type(Integer32):
    """Custom type wish_3_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_1_val1_Type.__name__ = "Integer32"
_Wish_3_external_1_val1_Object = MibScalar
wish_3_external_1_val1 = _Wish_3_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 1, 2),
    _Wish_3_external_1_val1_Type()
)
wish_3_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_1_val1.setStatus("mandatory")


class _Wish_3_external_1_val2_Type(Integer32):
    """Custom type wish_3_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_1_val2_Type.__name__ = "Integer32"
_Wish_3_external_1_val2_Object = MibScalar
wish_3_external_1_val2 = _Wish_3_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 1, 3),
    _Wish_3_external_1_val2_Type()
)
wish_3_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_1_val2.setStatus("mandatory")


class _Wish_3_external_1_val3_Type(Integer32):
    """Custom type wish_3_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_1_val3_Type.__name__ = "Integer32"
_Wish_3_external_1_val3_Object = MibScalar
wish_3_external_1_val3 = _Wish_3_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 1, 4),
    _Wish_3_external_1_val3_Type()
)
wish_3_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_1_val3.setStatus("mandatory")


class _Wish_3_external_1_val4_Type(Integer32):
    """Custom type wish_3_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_1_val4_Type.__name__ = "Integer32"
_Wish_3_external_1_val4_Object = MibScalar
wish_3_external_1_val4 = _Wish_3_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 1, 5),
    _Wish_3_external_1_val4_Type()
)
wish_3_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_1_val4.setStatus("mandatory")


class _Wish_3_external_1_val5_Type(Integer32):
    """Custom type wish_3_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_1_val5_Type.__name__ = "Integer32"
_Wish_3_external_1_val5_Object = MibScalar
wish_3_external_1_val5 = _Wish_3_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 1, 6),
    _Wish_3_external_1_val5_Type()
)
wish_3_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_1_val5.setStatus("mandatory")
_Wish_3_external_2_ObjectIdentity = ObjectIdentity
wish_3_external_2 = _Wish_3_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 2)
)


class _Wish_3_external_2_type_Type(Integer32):
    """Custom type wish_3_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_2_type_Type.__name__ = "Integer32"
_Wish_3_external_2_type_Object = MibScalar
wish_3_external_2_type = _Wish_3_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 2, 1),
    _Wish_3_external_2_type_Type()
)
wish_3_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_2_type.setStatus("mandatory")


class _Wish_3_external_2_val1_Type(Integer32):
    """Custom type wish_3_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_2_val1_Type.__name__ = "Integer32"
_Wish_3_external_2_val1_Object = MibScalar
wish_3_external_2_val1 = _Wish_3_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 2, 2),
    _Wish_3_external_2_val1_Type()
)
wish_3_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_2_val1.setStatus("mandatory")


class _Wish_3_external_2_val2_Type(Integer32):
    """Custom type wish_3_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_2_val2_Type.__name__ = "Integer32"
_Wish_3_external_2_val2_Object = MibScalar
wish_3_external_2_val2 = _Wish_3_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 2, 3),
    _Wish_3_external_2_val2_Type()
)
wish_3_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_2_val2.setStatus("mandatory")


class _Wish_3_external_2_val3_Type(Integer32):
    """Custom type wish_3_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_2_val3_Type.__name__ = "Integer32"
_Wish_3_external_2_val3_Object = MibScalar
wish_3_external_2_val3 = _Wish_3_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 2, 4),
    _Wish_3_external_2_val3_Type()
)
wish_3_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_2_val3.setStatus("mandatory")


class _Wish_3_external_2_val4_Type(Integer32):
    """Custom type wish_3_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_2_val4_Type.__name__ = "Integer32"
_Wish_3_external_2_val4_Object = MibScalar
wish_3_external_2_val4 = _Wish_3_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 2, 5),
    _Wish_3_external_2_val4_Type()
)
wish_3_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_2_val4.setStatus("mandatory")


class _Wish_3_external_2_val5_Type(Integer32):
    """Custom type wish_3_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_3_external_2_val5_Type.__name__ = "Integer32"
_Wish_3_external_2_val5_Object = MibScalar
wish_3_external_2_val5 = _Wish_3_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 2, 6),
    _Wish_3_external_2_val5_Type()
)
wish_3_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_2_val5.setStatus("mandatory")


class _Wish_3_external_switch_Type(Integer32):
    """Custom type wish_3_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_3_external_switch_Type.__name__ = "Integer32"
_Wish_3_external_switch_Object = MibScalar
wish_3_external_switch = _Wish_3_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 3, 4, 2, 3),
    _Wish_3_external_switch_Type()
)
wish_3_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_3_external_switch.setStatus("mandatory")
_Wish_4_ObjectIdentity = ObjectIdentity
wish_4 = _Wish_4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4)
)


class _Wish_4_enabled_Type(Integer32):
    """Custom type wish_4_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_4_enabled_Type.__name__ = "Integer32"
_Wish_4_enabled_Object = MibScalar
wish_4_enabled = _Wish_4_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 1),
    _Wish_4_enabled_Type()
)
wish_4_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_enabled.setStatus("mandatory")
_Wish_4_serial_num_Type = OctetString
_Wish_4_serial_num_Object = MibScalar
wish_4_serial_num = _Wish_4_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 2),
    _Wish_4_serial_num_Type()
)
wish_4_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_serial_num.setStatus("mandatory")


class _Wish_4_updates_Type(Integer32):
    """Custom type wish_4_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_updates_Type.__name__ = "Integer32"
_Wish_4_updates_Object = MibScalar
wish_4_updates = _Wish_4_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 3),
    _Wish_4_updates_Type()
)
wish_4_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_updates.setStatus("mandatory")
_Wish_4_sensors_ObjectIdentity = ObjectIdentity
wish_4_sensors = _Wish_4_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4)
)
_Wish_4_internal_ObjectIdentity = ObjectIdentity
wish_4_internal = _Wish_4_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 1)
)


class _Wish_4_battery_voltage_Type(Integer32):
    """Custom type wish_4_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_battery_voltage_Type.__name__ = "Integer32"
_Wish_4_battery_voltage_Object = MibScalar
wish_4_battery_voltage = _Wish_4_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 1, 1),
    _Wish_4_battery_voltage_Type()
)
wish_4_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_battery_voltage.setStatus("mandatory")


class _Wish_4_internal_tempc_Type(Integer32):
    """Custom type wish_4_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_internal_tempc_Type.__name__ = "Integer32"
_Wish_4_internal_tempc_Object = MibScalar
wish_4_internal_tempc = _Wish_4_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 1, 2),
    _Wish_4_internal_tempc_Type()
)
wish_4_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_internal_tempc.setStatus("mandatory")


class _Wish_4_internal_tempf_Type(Integer32):
    """Custom type wish_4_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_internal_tempf_Type.__name__ = "Integer32"
_Wish_4_internal_tempf_Object = MibScalar
wish_4_internal_tempf = _Wish_4_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 1, 3),
    _Wish_4_internal_tempf_Type()
)
wish_4_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_internal_tempf.setStatus("mandatory")
_Wish_4_external_ObjectIdentity = ObjectIdentity
wish_4_external = _Wish_4_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2)
)
_Wish_4_external_1_ObjectIdentity = ObjectIdentity
wish_4_external_1 = _Wish_4_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 1)
)


class _Wish_4_external_1_type_Type(Integer32):
    """Custom type wish_4_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_1_type_Type.__name__ = "Integer32"
_Wish_4_external_1_type_Object = MibScalar
wish_4_external_1_type = _Wish_4_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 1, 1),
    _Wish_4_external_1_type_Type()
)
wish_4_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_1_type.setStatus("mandatory")


class _Wish_4_external_1_val1_Type(Integer32):
    """Custom type wish_4_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_1_val1_Type.__name__ = "Integer32"
_Wish_4_external_1_val1_Object = MibScalar
wish_4_external_1_val1 = _Wish_4_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 1, 2),
    _Wish_4_external_1_val1_Type()
)
wish_4_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_1_val1.setStatus("mandatory")


class _Wish_4_external_1_val2_Type(Integer32):
    """Custom type wish_4_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_1_val2_Type.__name__ = "Integer32"
_Wish_4_external_1_val2_Object = MibScalar
wish_4_external_1_val2 = _Wish_4_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 1, 3),
    _Wish_4_external_1_val2_Type()
)
wish_4_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_1_val2.setStatus("mandatory")


class _Wish_4_external_1_val3_Type(Integer32):
    """Custom type wish_4_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_1_val3_Type.__name__ = "Integer32"
_Wish_4_external_1_val3_Object = MibScalar
wish_4_external_1_val3 = _Wish_4_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 1, 4),
    _Wish_4_external_1_val3_Type()
)
wish_4_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_1_val3.setStatus("mandatory")


class _Wish_4_external_1_val4_Type(Integer32):
    """Custom type wish_4_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_1_val4_Type.__name__ = "Integer32"
_Wish_4_external_1_val4_Object = MibScalar
wish_4_external_1_val4 = _Wish_4_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 1, 5),
    _Wish_4_external_1_val4_Type()
)
wish_4_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_1_val4.setStatus("mandatory")


class _Wish_4_external_1_val5_Type(Integer32):
    """Custom type wish_4_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_1_val5_Type.__name__ = "Integer32"
_Wish_4_external_1_val5_Object = MibScalar
wish_4_external_1_val5 = _Wish_4_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 1, 6),
    _Wish_4_external_1_val5_Type()
)
wish_4_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_1_val5.setStatus("mandatory")
_Wish_4_external_2_ObjectIdentity = ObjectIdentity
wish_4_external_2 = _Wish_4_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 2)
)


class _Wish_4_external_2_type_Type(Integer32):
    """Custom type wish_4_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_2_type_Type.__name__ = "Integer32"
_Wish_4_external_2_type_Object = MibScalar
wish_4_external_2_type = _Wish_4_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 2, 1),
    _Wish_4_external_2_type_Type()
)
wish_4_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_2_type.setStatus("mandatory")


class _Wish_4_external_2_val1_Type(Integer32):
    """Custom type wish_4_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_2_val1_Type.__name__ = "Integer32"
_Wish_4_external_2_val1_Object = MibScalar
wish_4_external_2_val1 = _Wish_4_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 2, 2),
    _Wish_4_external_2_val1_Type()
)
wish_4_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_2_val1.setStatus("mandatory")


class _Wish_4_external_2_val2_Type(Integer32):
    """Custom type wish_4_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_2_val2_Type.__name__ = "Integer32"
_Wish_4_external_2_val2_Object = MibScalar
wish_4_external_2_val2 = _Wish_4_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 2, 3),
    _Wish_4_external_2_val2_Type()
)
wish_4_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_2_val2.setStatus("mandatory")


class _Wish_4_external_2_val3_Type(Integer32):
    """Custom type wish_4_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_2_val3_Type.__name__ = "Integer32"
_Wish_4_external_2_val3_Object = MibScalar
wish_4_external_2_val3 = _Wish_4_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 2, 4),
    _Wish_4_external_2_val3_Type()
)
wish_4_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_2_val3.setStatus("mandatory")


class _Wish_4_external_2_val4_Type(Integer32):
    """Custom type wish_4_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_2_val4_Type.__name__ = "Integer32"
_Wish_4_external_2_val4_Object = MibScalar
wish_4_external_2_val4 = _Wish_4_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 2, 5),
    _Wish_4_external_2_val4_Type()
)
wish_4_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_2_val4.setStatus("mandatory")


class _Wish_4_external_2_val5_Type(Integer32):
    """Custom type wish_4_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_4_external_2_val5_Type.__name__ = "Integer32"
_Wish_4_external_2_val5_Object = MibScalar
wish_4_external_2_val5 = _Wish_4_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 2, 6),
    _Wish_4_external_2_val5_Type()
)
wish_4_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_2_val5.setStatus("mandatory")


class _Wish_4_external_switch_Type(Integer32):
    """Custom type wish_4_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_4_external_switch_Type.__name__ = "Integer32"
_Wish_4_external_switch_Object = MibScalar
wish_4_external_switch = _Wish_4_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 4, 4, 2, 3),
    _Wish_4_external_switch_Type()
)
wish_4_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_4_external_switch.setStatus("mandatory")
_Wish_5_ObjectIdentity = ObjectIdentity
wish_5 = _Wish_5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5)
)


class _Wish_5_enabled_Type(Integer32):
    """Custom type wish_5_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_5_enabled_Type.__name__ = "Integer32"
_Wish_5_enabled_Object = MibScalar
wish_5_enabled = _Wish_5_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 1),
    _Wish_5_enabled_Type()
)
wish_5_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_enabled.setStatus("mandatory")
_Wish_5_serial_num_Type = OctetString
_Wish_5_serial_num_Object = MibScalar
wish_5_serial_num = _Wish_5_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 2),
    _Wish_5_serial_num_Type()
)
wish_5_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_serial_num.setStatus("mandatory")


class _Wish_5_updates_Type(Integer32):
    """Custom type wish_5_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_updates_Type.__name__ = "Integer32"
_Wish_5_updates_Object = MibScalar
wish_5_updates = _Wish_5_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 3),
    _Wish_5_updates_Type()
)
wish_5_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_updates.setStatus("mandatory")
_Wish_5_sensors_ObjectIdentity = ObjectIdentity
wish_5_sensors = _Wish_5_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4)
)
_Wish_5_internal_ObjectIdentity = ObjectIdentity
wish_5_internal = _Wish_5_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 1)
)


class _Wish_5_battery_voltage_Type(Integer32):
    """Custom type wish_5_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_battery_voltage_Type.__name__ = "Integer32"
_Wish_5_battery_voltage_Object = MibScalar
wish_5_battery_voltage = _Wish_5_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 1, 1),
    _Wish_5_battery_voltage_Type()
)
wish_5_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_battery_voltage.setStatus("mandatory")


class _Wish_5_internal_tempc_Type(Integer32):
    """Custom type wish_5_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_internal_tempc_Type.__name__ = "Integer32"
_Wish_5_internal_tempc_Object = MibScalar
wish_5_internal_tempc = _Wish_5_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 1, 2),
    _Wish_5_internal_tempc_Type()
)
wish_5_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_internal_tempc.setStatus("mandatory")


class _Wish_5_internal_tempf_Type(Integer32):
    """Custom type wish_5_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_internal_tempf_Type.__name__ = "Integer32"
_Wish_5_internal_tempf_Object = MibScalar
wish_5_internal_tempf = _Wish_5_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 1, 3),
    _Wish_5_internal_tempf_Type()
)
wish_5_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_internal_tempf.setStatus("mandatory")
_Wish_5_external_ObjectIdentity = ObjectIdentity
wish_5_external = _Wish_5_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2)
)
_Wish_5_external_1_ObjectIdentity = ObjectIdentity
wish_5_external_1 = _Wish_5_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 1)
)


class _Wish_5_external_1_type_Type(Integer32):
    """Custom type wish_5_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_1_type_Type.__name__ = "Integer32"
_Wish_5_external_1_type_Object = MibScalar
wish_5_external_1_type = _Wish_5_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 1, 1),
    _Wish_5_external_1_type_Type()
)
wish_5_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_1_type.setStatus("mandatory")


class _Wish_5_external_1_val1_Type(Integer32):
    """Custom type wish_5_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_1_val1_Type.__name__ = "Integer32"
_Wish_5_external_1_val1_Object = MibScalar
wish_5_external_1_val1 = _Wish_5_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 1, 2),
    _Wish_5_external_1_val1_Type()
)
wish_5_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_1_val1.setStatus("mandatory")


class _Wish_5_external_1_val2_Type(Integer32):
    """Custom type wish_5_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_1_val2_Type.__name__ = "Integer32"
_Wish_5_external_1_val2_Object = MibScalar
wish_5_external_1_val2 = _Wish_5_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 1, 3),
    _Wish_5_external_1_val2_Type()
)
wish_5_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_1_val2.setStatus("mandatory")


class _Wish_5_external_1_val3_Type(Integer32):
    """Custom type wish_5_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_1_val3_Type.__name__ = "Integer32"
_Wish_5_external_1_val3_Object = MibScalar
wish_5_external_1_val3 = _Wish_5_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 1, 4),
    _Wish_5_external_1_val3_Type()
)
wish_5_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_1_val3.setStatus("mandatory")


class _Wish_5_external_1_val4_Type(Integer32):
    """Custom type wish_5_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_1_val4_Type.__name__ = "Integer32"
_Wish_5_external_1_val4_Object = MibScalar
wish_5_external_1_val4 = _Wish_5_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 1, 5),
    _Wish_5_external_1_val4_Type()
)
wish_5_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_1_val4.setStatus("mandatory")


class _Wish_5_external_1_val5_Type(Integer32):
    """Custom type wish_5_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_1_val5_Type.__name__ = "Integer32"
_Wish_5_external_1_val5_Object = MibScalar
wish_5_external_1_val5 = _Wish_5_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 1, 6),
    _Wish_5_external_1_val5_Type()
)
wish_5_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_1_val5.setStatus("mandatory")
_Wish_5_external_2_ObjectIdentity = ObjectIdentity
wish_5_external_2 = _Wish_5_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 2)
)


class _Wish_5_external_2_type_Type(Integer32):
    """Custom type wish_5_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_2_type_Type.__name__ = "Integer32"
_Wish_5_external_2_type_Object = MibScalar
wish_5_external_2_type = _Wish_5_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 2, 1),
    _Wish_5_external_2_type_Type()
)
wish_5_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_2_type.setStatus("mandatory")


class _Wish_5_external_2_val1_Type(Integer32):
    """Custom type wish_5_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_2_val1_Type.__name__ = "Integer32"
_Wish_5_external_2_val1_Object = MibScalar
wish_5_external_2_val1 = _Wish_5_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 2, 2),
    _Wish_5_external_2_val1_Type()
)
wish_5_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_2_val1.setStatus("mandatory")


class _Wish_5_external_2_val2_Type(Integer32):
    """Custom type wish_5_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_2_val2_Type.__name__ = "Integer32"
_Wish_5_external_2_val2_Object = MibScalar
wish_5_external_2_val2 = _Wish_5_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 2, 3),
    _Wish_5_external_2_val2_Type()
)
wish_5_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_2_val2.setStatus("mandatory")


class _Wish_5_external_2_val3_Type(Integer32):
    """Custom type wish_5_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_2_val3_Type.__name__ = "Integer32"
_Wish_5_external_2_val3_Object = MibScalar
wish_5_external_2_val3 = _Wish_5_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 2, 4),
    _Wish_5_external_2_val3_Type()
)
wish_5_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_2_val3.setStatus("mandatory")


class _Wish_5_external_2_val4_Type(Integer32):
    """Custom type wish_5_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_2_val4_Type.__name__ = "Integer32"
_Wish_5_external_2_val4_Object = MibScalar
wish_5_external_2_val4 = _Wish_5_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 2, 5),
    _Wish_5_external_2_val4_Type()
)
wish_5_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_2_val4.setStatus("mandatory")


class _Wish_5_external_2_val5_Type(Integer32):
    """Custom type wish_5_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_5_external_2_val5_Type.__name__ = "Integer32"
_Wish_5_external_2_val5_Object = MibScalar
wish_5_external_2_val5 = _Wish_5_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 2, 6),
    _Wish_5_external_2_val5_Type()
)
wish_5_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_2_val5.setStatus("mandatory")


class _Wish_5_external_switch_Type(Integer32):
    """Custom type wish_5_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_5_external_switch_Type.__name__ = "Integer32"
_Wish_5_external_switch_Object = MibScalar
wish_5_external_switch = _Wish_5_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 5, 4, 2, 3),
    _Wish_5_external_switch_Type()
)
wish_5_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_5_external_switch.setStatus("mandatory")
_Wish_6_ObjectIdentity = ObjectIdentity
wish_6 = _Wish_6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6)
)


class _Wish_6_enabled_Type(Integer32):
    """Custom type wish_6_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_6_enabled_Type.__name__ = "Integer32"
_Wish_6_enabled_Object = MibScalar
wish_6_enabled = _Wish_6_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 1),
    _Wish_6_enabled_Type()
)
wish_6_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_enabled.setStatus("mandatory")
_Wish_6_serial_num_Type = OctetString
_Wish_6_serial_num_Object = MibScalar
wish_6_serial_num = _Wish_6_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 2),
    _Wish_6_serial_num_Type()
)
wish_6_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_serial_num.setStatus("mandatory")


class _Wish_6_updates_Type(Integer32):
    """Custom type wish_6_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_updates_Type.__name__ = "Integer32"
_Wish_6_updates_Object = MibScalar
wish_6_updates = _Wish_6_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 3),
    _Wish_6_updates_Type()
)
wish_6_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_updates.setStatus("mandatory")
_Wish_6_sensors_ObjectIdentity = ObjectIdentity
wish_6_sensors = _Wish_6_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4)
)
_Wish_6_internal_ObjectIdentity = ObjectIdentity
wish_6_internal = _Wish_6_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 1)
)


class _Wish_6_battery_voltage_Type(Integer32):
    """Custom type wish_6_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_battery_voltage_Type.__name__ = "Integer32"
_Wish_6_battery_voltage_Object = MibScalar
wish_6_battery_voltage = _Wish_6_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 1, 1),
    _Wish_6_battery_voltage_Type()
)
wish_6_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_battery_voltage.setStatus("mandatory")


class _Wish_6_internal_tempc_Type(Integer32):
    """Custom type wish_6_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_internal_tempc_Type.__name__ = "Integer32"
_Wish_6_internal_tempc_Object = MibScalar
wish_6_internal_tempc = _Wish_6_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 1, 2),
    _Wish_6_internal_tempc_Type()
)
wish_6_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_internal_tempc.setStatus("mandatory")


class _Wish_6_internal_tempf_Type(Integer32):
    """Custom type wish_6_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_internal_tempf_Type.__name__ = "Integer32"
_Wish_6_internal_tempf_Object = MibScalar
wish_6_internal_tempf = _Wish_6_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 1, 3),
    _Wish_6_internal_tempf_Type()
)
wish_6_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_internal_tempf.setStatus("mandatory")
_Wish_6_external_ObjectIdentity = ObjectIdentity
wish_6_external = _Wish_6_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2)
)
_Wish_6_external_1_ObjectIdentity = ObjectIdentity
wish_6_external_1 = _Wish_6_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 1)
)


class _Wish_6_external_1_type_Type(Integer32):
    """Custom type wish_6_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_1_type_Type.__name__ = "Integer32"
_Wish_6_external_1_type_Object = MibScalar
wish_6_external_1_type = _Wish_6_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 1, 1),
    _Wish_6_external_1_type_Type()
)
wish_6_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_1_type.setStatus("mandatory")


class _Wish_6_external_1_val1_Type(Integer32):
    """Custom type wish_6_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_1_val1_Type.__name__ = "Integer32"
_Wish_6_external_1_val1_Object = MibScalar
wish_6_external_1_val1 = _Wish_6_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 1, 2),
    _Wish_6_external_1_val1_Type()
)
wish_6_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_1_val1.setStatus("mandatory")


class _Wish_6_external_1_val2_Type(Integer32):
    """Custom type wish_6_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_1_val2_Type.__name__ = "Integer32"
_Wish_6_external_1_val2_Object = MibScalar
wish_6_external_1_val2 = _Wish_6_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 1, 3),
    _Wish_6_external_1_val2_Type()
)
wish_6_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_1_val2.setStatus("mandatory")


class _Wish_6_external_1_val3_Type(Integer32):
    """Custom type wish_6_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_1_val3_Type.__name__ = "Integer32"
_Wish_6_external_1_val3_Object = MibScalar
wish_6_external_1_val3 = _Wish_6_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 1, 4),
    _Wish_6_external_1_val3_Type()
)
wish_6_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_1_val3.setStatus("mandatory")


class _Wish_6_external_1_val4_Type(Integer32):
    """Custom type wish_6_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_1_val4_Type.__name__ = "Integer32"
_Wish_6_external_1_val4_Object = MibScalar
wish_6_external_1_val4 = _Wish_6_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 1, 5),
    _Wish_6_external_1_val4_Type()
)
wish_6_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_1_val4.setStatus("mandatory")


class _Wish_6_external_1_val5_Type(Integer32):
    """Custom type wish_6_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_1_val5_Type.__name__ = "Integer32"
_Wish_6_external_1_val5_Object = MibScalar
wish_6_external_1_val5 = _Wish_6_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 1, 6),
    _Wish_6_external_1_val5_Type()
)
wish_6_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_1_val5.setStatus("mandatory")
_Wish_6_external_2_ObjectIdentity = ObjectIdentity
wish_6_external_2 = _Wish_6_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 2)
)


class _Wish_6_external_2_type_Type(Integer32):
    """Custom type wish_6_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_2_type_Type.__name__ = "Integer32"
_Wish_6_external_2_type_Object = MibScalar
wish_6_external_2_type = _Wish_6_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 2, 1),
    _Wish_6_external_2_type_Type()
)
wish_6_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_2_type.setStatus("mandatory")


class _Wish_6_external_2_val1_Type(Integer32):
    """Custom type wish_6_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_2_val1_Type.__name__ = "Integer32"
_Wish_6_external_2_val1_Object = MibScalar
wish_6_external_2_val1 = _Wish_6_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 2, 2),
    _Wish_6_external_2_val1_Type()
)
wish_6_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_2_val1.setStatus("mandatory")


class _Wish_6_external_2_val2_Type(Integer32):
    """Custom type wish_6_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_2_val2_Type.__name__ = "Integer32"
_Wish_6_external_2_val2_Object = MibScalar
wish_6_external_2_val2 = _Wish_6_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 2, 3),
    _Wish_6_external_2_val2_Type()
)
wish_6_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_2_val2.setStatus("mandatory")


class _Wish_6_external_2_val3_Type(Integer32):
    """Custom type wish_6_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_2_val3_Type.__name__ = "Integer32"
_Wish_6_external_2_val3_Object = MibScalar
wish_6_external_2_val3 = _Wish_6_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 2, 4),
    _Wish_6_external_2_val3_Type()
)
wish_6_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_2_val3.setStatus("mandatory")


class _Wish_6_external_2_val4_Type(Integer32):
    """Custom type wish_6_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_2_val4_Type.__name__ = "Integer32"
_Wish_6_external_2_val4_Object = MibScalar
wish_6_external_2_val4 = _Wish_6_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 2, 5),
    _Wish_6_external_2_val4_Type()
)
wish_6_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_2_val4.setStatus("mandatory")


class _Wish_6_external_2_val5_Type(Integer32):
    """Custom type wish_6_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_6_external_2_val5_Type.__name__ = "Integer32"
_Wish_6_external_2_val5_Object = MibScalar
wish_6_external_2_val5 = _Wish_6_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 2, 6),
    _Wish_6_external_2_val5_Type()
)
wish_6_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_2_val5.setStatus("mandatory")


class _Wish_6_external_switch_Type(Integer32):
    """Custom type wish_6_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_6_external_switch_Type.__name__ = "Integer32"
_Wish_6_external_switch_Object = MibScalar
wish_6_external_switch = _Wish_6_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 6, 4, 2, 3),
    _Wish_6_external_switch_Type()
)
wish_6_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_6_external_switch.setStatus("mandatory")
_Wish_7_ObjectIdentity = ObjectIdentity
wish_7 = _Wish_7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7)
)


class _Wish_7_enabled_Type(Integer32):
    """Custom type wish_7_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_7_enabled_Type.__name__ = "Integer32"
_Wish_7_enabled_Object = MibScalar
wish_7_enabled = _Wish_7_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 1),
    _Wish_7_enabled_Type()
)
wish_7_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_enabled.setStatus("mandatory")
_Wish_7_serial_num_Type = OctetString
_Wish_7_serial_num_Object = MibScalar
wish_7_serial_num = _Wish_7_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 2),
    _Wish_7_serial_num_Type()
)
wish_7_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_serial_num.setStatus("mandatory")


class _Wish_7_updates_Type(Integer32):
    """Custom type wish_7_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_updates_Type.__name__ = "Integer32"
_Wish_7_updates_Object = MibScalar
wish_7_updates = _Wish_7_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 3),
    _Wish_7_updates_Type()
)
wish_7_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_updates.setStatus("mandatory")
_Wish_7_sensors_ObjectIdentity = ObjectIdentity
wish_7_sensors = _Wish_7_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4)
)
_Wish_7_internal_ObjectIdentity = ObjectIdentity
wish_7_internal = _Wish_7_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 1)
)


class _Wish_7_battery_voltage_Type(Integer32):
    """Custom type wish_7_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_battery_voltage_Type.__name__ = "Integer32"
_Wish_7_battery_voltage_Object = MibScalar
wish_7_battery_voltage = _Wish_7_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 1, 1),
    _Wish_7_battery_voltage_Type()
)
wish_7_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_battery_voltage.setStatus("mandatory")


class _Wish_7_internal_tempc_Type(Integer32):
    """Custom type wish_7_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_internal_tempc_Type.__name__ = "Integer32"
_Wish_7_internal_tempc_Object = MibScalar
wish_7_internal_tempc = _Wish_7_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 1, 2),
    _Wish_7_internal_tempc_Type()
)
wish_7_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_internal_tempc.setStatus("mandatory")


class _Wish_7_internal_tempf_Type(Integer32):
    """Custom type wish_7_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_internal_tempf_Type.__name__ = "Integer32"
_Wish_7_internal_tempf_Object = MibScalar
wish_7_internal_tempf = _Wish_7_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 1, 3),
    _Wish_7_internal_tempf_Type()
)
wish_7_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_internal_tempf.setStatus("mandatory")
_Wish_7_external_ObjectIdentity = ObjectIdentity
wish_7_external = _Wish_7_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2)
)
_Wish_7_external_1_ObjectIdentity = ObjectIdentity
wish_7_external_1 = _Wish_7_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 1)
)


class _Wish_7_external_1_type_Type(Integer32):
    """Custom type wish_7_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_1_type_Type.__name__ = "Integer32"
_Wish_7_external_1_type_Object = MibScalar
wish_7_external_1_type = _Wish_7_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 1, 1),
    _Wish_7_external_1_type_Type()
)
wish_7_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_1_type.setStatus("mandatory")


class _Wish_7_external_1_val1_Type(Integer32):
    """Custom type wish_7_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_1_val1_Type.__name__ = "Integer32"
_Wish_7_external_1_val1_Object = MibScalar
wish_7_external_1_val1 = _Wish_7_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 1, 2),
    _Wish_7_external_1_val1_Type()
)
wish_7_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_1_val1.setStatus("mandatory")


class _Wish_7_external_1_val2_Type(Integer32):
    """Custom type wish_7_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_1_val2_Type.__name__ = "Integer32"
_Wish_7_external_1_val2_Object = MibScalar
wish_7_external_1_val2 = _Wish_7_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 1, 3),
    _Wish_7_external_1_val2_Type()
)
wish_7_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_1_val2.setStatus("mandatory")


class _Wish_7_external_1_val3_Type(Integer32):
    """Custom type wish_7_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_1_val3_Type.__name__ = "Integer32"
_Wish_7_external_1_val3_Object = MibScalar
wish_7_external_1_val3 = _Wish_7_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 1, 4),
    _Wish_7_external_1_val3_Type()
)
wish_7_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_1_val3.setStatus("mandatory")


class _Wish_7_external_1_val4_Type(Integer32):
    """Custom type wish_7_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_1_val4_Type.__name__ = "Integer32"
_Wish_7_external_1_val4_Object = MibScalar
wish_7_external_1_val4 = _Wish_7_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 1, 5),
    _Wish_7_external_1_val4_Type()
)
wish_7_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_1_val4.setStatus("mandatory")


class _Wish_7_external_1_val5_Type(Integer32):
    """Custom type wish_7_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_1_val5_Type.__name__ = "Integer32"
_Wish_7_external_1_val5_Object = MibScalar
wish_7_external_1_val5 = _Wish_7_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 1, 6),
    _Wish_7_external_1_val5_Type()
)
wish_7_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_1_val5.setStatus("mandatory")
_Wish_7_external_2_ObjectIdentity = ObjectIdentity
wish_7_external_2 = _Wish_7_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 2)
)


class _Wish_7_external_2_type_Type(Integer32):
    """Custom type wish_7_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_2_type_Type.__name__ = "Integer32"
_Wish_7_external_2_type_Object = MibScalar
wish_7_external_2_type = _Wish_7_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 2, 1),
    _Wish_7_external_2_type_Type()
)
wish_7_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_2_type.setStatus("mandatory")


class _Wish_7_external_2_val1_Type(Integer32):
    """Custom type wish_7_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_2_val1_Type.__name__ = "Integer32"
_Wish_7_external_2_val1_Object = MibScalar
wish_7_external_2_val1 = _Wish_7_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 2, 2),
    _Wish_7_external_2_val1_Type()
)
wish_7_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_2_val1.setStatus("mandatory")


class _Wish_7_external_2_val2_Type(Integer32):
    """Custom type wish_7_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_2_val2_Type.__name__ = "Integer32"
_Wish_7_external_2_val2_Object = MibScalar
wish_7_external_2_val2 = _Wish_7_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 2, 3),
    _Wish_7_external_2_val2_Type()
)
wish_7_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_2_val2.setStatus("mandatory")


class _Wish_7_external_2_val3_Type(Integer32):
    """Custom type wish_7_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_2_val3_Type.__name__ = "Integer32"
_Wish_7_external_2_val3_Object = MibScalar
wish_7_external_2_val3 = _Wish_7_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 2, 4),
    _Wish_7_external_2_val3_Type()
)
wish_7_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_2_val3.setStatus("mandatory")


class _Wish_7_external_2_val4_Type(Integer32):
    """Custom type wish_7_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_2_val4_Type.__name__ = "Integer32"
_Wish_7_external_2_val4_Object = MibScalar
wish_7_external_2_val4 = _Wish_7_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 2, 5),
    _Wish_7_external_2_val4_Type()
)
wish_7_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_2_val4.setStatus("mandatory")


class _Wish_7_external_2_val5_Type(Integer32):
    """Custom type wish_7_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_7_external_2_val5_Type.__name__ = "Integer32"
_Wish_7_external_2_val5_Object = MibScalar
wish_7_external_2_val5 = _Wish_7_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 2, 6),
    _Wish_7_external_2_val5_Type()
)
wish_7_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_2_val5.setStatus("mandatory")


class _Wish_7_external_switch_Type(Integer32):
    """Custom type wish_7_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_7_external_switch_Type.__name__ = "Integer32"
_Wish_7_external_switch_Object = MibScalar
wish_7_external_switch = _Wish_7_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 7, 4, 2, 3),
    _Wish_7_external_switch_Type()
)
wish_7_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_7_external_switch.setStatus("mandatory")
_Wish_8_ObjectIdentity = ObjectIdentity
wish_8 = _Wish_8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8)
)


class _Wish_8_enabled_Type(Integer32):
    """Custom type wish_8_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_8_enabled_Type.__name__ = "Integer32"
_Wish_8_enabled_Object = MibScalar
wish_8_enabled = _Wish_8_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 1),
    _Wish_8_enabled_Type()
)
wish_8_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_enabled.setStatus("mandatory")
_Wish_8_serial_num_Type = OctetString
_Wish_8_serial_num_Object = MibScalar
wish_8_serial_num = _Wish_8_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 2),
    _Wish_8_serial_num_Type()
)
wish_8_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_serial_num.setStatus("mandatory")


class _Wish_8_updates_Type(Integer32):
    """Custom type wish_8_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_updates_Type.__name__ = "Integer32"
_Wish_8_updates_Object = MibScalar
wish_8_updates = _Wish_8_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 3),
    _Wish_8_updates_Type()
)
wish_8_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_updates.setStatus("mandatory")
_Wish_8_sensors_ObjectIdentity = ObjectIdentity
wish_8_sensors = _Wish_8_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4)
)
_Wish_8_internal_ObjectIdentity = ObjectIdentity
wish_8_internal = _Wish_8_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 1)
)


class _Wish_8_battery_voltage_Type(Integer32):
    """Custom type wish_8_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_battery_voltage_Type.__name__ = "Integer32"
_Wish_8_battery_voltage_Object = MibScalar
wish_8_battery_voltage = _Wish_8_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 1, 1),
    _Wish_8_battery_voltage_Type()
)
wish_8_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_battery_voltage.setStatus("mandatory")


class _Wish_8_internal_tempc_Type(Integer32):
    """Custom type wish_8_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_internal_tempc_Type.__name__ = "Integer32"
_Wish_8_internal_tempc_Object = MibScalar
wish_8_internal_tempc = _Wish_8_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 1, 2),
    _Wish_8_internal_tempc_Type()
)
wish_8_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_internal_tempc.setStatus("mandatory")


class _Wish_8_internal_tempf_Type(Integer32):
    """Custom type wish_8_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_internal_tempf_Type.__name__ = "Integer32"
_Wish_8_internal_tempf_Object = MibScalar
wish_8_internal_tempf = _Wish_8_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 1, 3),
    _Wish_8_internal_tempf_Type()
)
wish_8_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_internal_tempf.setStatus("mandatory")
_Wish_8_external_ObjectIdentity = ObjectIdentity
wish_8_external = _Wish_8_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2)
)
_Wish_8_external_1_ObjectIdentity = ObjectIdentity
wish_8_external_1 = _Wish_8_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 1)
)


class _Wish_8_external_1_type_Type(Integer32):
    """Custom type wish_8_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_1_type_Type.__name__ = "Integer32"
_Wish_8_external_1_type_Object = MibScalar
wish_8_external_1_type = _Wish_8_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 1, 1),
    _Wish_8_external_1_type_Type()
)
wish_8_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_1_type.setStatus("mandatory")


class _Wish_8_external_1_val1_Type(Integer32):
    """Custom type wish_8_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_1_val1_Type.__name__ = "Integer32"
_Wish_8_external_1_val1_Object = MibScalar
wish_8_external_1_val1 = _Wish_8_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 1, 2),
    _Wish_8_external_1_val1_Type()
)
wish_8_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_1_val1.setStatus("mandatory")


class _Wish_8_external_1_val2_Type(Integer32):
    """Custom type wish_8_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_1_val2_Type.__name__ = "Integer32"
_Wish_8_external_1_val2_Object = MibScalar
wish_8_external_1_val2 = _Wish_8_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 1, 3),
    _Wish_8_external_1_val2_Type()
)
wish_8_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_1_val2.setStatus("mandatory")


class _Wish_8_external_1_val3_Type(Integer32):
    """Custom type wish_8_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_1_val3_Type.__name__ = "Integer32"
_Wish_8_external_1_val3_Object = MibScalar
wish_8_external_1_val3 = _Wish_8_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 1, 4),
    _Wish_8_external_1_val3_Type()
)
wish_8_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_1_val3.setStatus("mandatory")


class _Wish_8_external_1_val4_Type(Integer32):
    """Custom type wish_8_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_1_val4_Type.__name__ = "Integer32"
_Wish_8_external_1_val4_Object = MibScalar
wish_8_external_1_val4 = _Wish_8_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 1, 5),
    _Wish_8_external_1_val4_Type()
)
wish_8_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_1_val4.setStatus("mandatory")


class _Wish_8_external_1_val5_Type(Integer32):
    """Custom type wish_8_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_1_val5_Type.__name__ = "Integer32"
_Wish_8_external_1_val5_Object = MibScalar
wish_8_external_1_val5 = _Wish_8_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 1, 6),
    _Wish_8_external_1_val5_Type()
)
wish_8_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_1_val5.setStatus("mandatory")
_Wish_8_external_2_ObjectIdentity = ObjectIdentity
wish_8_external_2 = _Wish_8_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 2)
)


class _Wish_8_external_2_type_Type(Integer32):
    """Custom type wish_8_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_2_type_Type.__name__ = "Integer32"
_Wish_8_external_2_type_Object = MibScalar
wish_8_external_2_type = _Wish_8_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 2, 1),
    _Wish_8_external_2_type_Type()
)
wish_8_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_2_type.setStatus("mandatory")


class _Wish_8_external_2_val1_Type(Integer32):
    """Custom type wish_8_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_2_val1_Type.__name__ = "Integer32"
_Wish_8_external_2_val1_Object = MibScalar
wish_8_external_2_val1 = _Wish_8_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 2, 2),
    _Wish_8_external_2_val1_Type()
)
wish_8_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_2_val1.setStatus("mandatory")


class _Wish_8_external_2_val2_Type(Integer32):
    """Custom type wish_8_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_2_val2_Type.__name__ = "Integer32"
_Wish_8_external_2_val2_Object = MibScalar
wish_8_external_2_val2 = _Wish_8_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 2, 3),
    _Wish_8_external_2_val2_Type()
)
wish_8_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_2_val2.setStatus("mandatory")


class _Wish_8_external_2_val3_Type(Integer32):
    """Custom type wish_8_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_2_val3_Type.__name__ = "Integer32"
_Wish_8_external_2_val3_Object = MibScalar
wish_8_external_2_val3 = _Wish_8_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 2, 4),
    _Wish_8_external_2_val3_Type()
)
wish_8_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_2_val3.setStatus("mandatory")


class _Wish_8_external_2_val4_Type(Integer32):
    """Custom type wish_8_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_2_val4_Type.__name__ = "Integer32"
_Wish_8_external_2_val4_Object = MibScalar
wish_8_external_2_val4 = _Wish_8_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 2, 5),
    _Wish_8_external_2_val4_Type()
)
wish_8_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_2_val4.setStatus("mandatory")


class _Wish_8_external_2_val5_Type(Integer32):
    """Custom type wish_8_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_8_external_2_val5_Type.__name__ = "Integer32"
_Wish_8_external_2_val5_Object = MibScalar
wish_8_external_2_val5 = _Wish_8_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 2, 6),
    _Wish_8_external_2_val5_Type()
)
wish_8_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_2_val5.setStatus("mandatory")


class _Wish_8_external_switch_Type(Integer32):
    """Custom type wish_8_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_8_external_switch_Type.__name__ = "Integer32"
_Wish_8_external_switch_Object = MibScalar
wish_8_external_switch = _Wish_8_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 8, 4, 2, 3),
    _Wish_8_external_switch_Type()
)
wish_8_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_8_external_switch.setStatus("mandatory")
_Wish_9_ObjectIdentity = ObjectIdentity
wish_9 = _Wish_9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9)
)


class _Wish_9_enabled_Type(Integer32):
    """Custom type wish_9_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_9_enabled_Type.__name__ = "Integer32"
_Wish_9_enabled_Object = MibScalar
wish_9_enabled = _Wish_9_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 1),
    _Wish_9_enabled_Type()
)
wish_9_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_enabled.setStatus("mandatory")
_Wish_9_serial_num_Type = OctetString
_Wish_9_serial_num_Object = MibScalar
wish_9_serial_num = _Wish_9_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 2),
    _Wish_9_serial_num_Type()
)
wish_9_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_serial_num.setStatus("mandatory")


class _Wish_9_updates_Type(Integer32):
    """Custom type wish_9_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_updates_Type.__name__ = "Integer32"
_Wish_9_updates_Object = MibScalar
wish_9_updates = _Wish_9_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 3),
    _Wish_9_updates_Type()
)
wish_9_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_updates.setStatus("mandatory")
_Wish_9_sensors_ObjectIdentity = ObjectIdentity
wish_9_sensors = _Wish_9_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4)
)
_Wish_9_internal_ObjectIdentity = ObjectIdentity
wish_9_internal = _Wish_9_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 1)
)


class _Wish_9_battery_voltage_Type(Integer32):
    """Custom type wish_9_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_battery_voltage_Type.__name__ = "Integer32"
_Wish_9_battery_voltage_Object = MibScalar
wish_9_battery_voltage = _Wish_9_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 1, 1),
    _Wish_9_battery_voltage_Type()
)
wish_9_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_battery_voltage.setStatus("mandatory")


class _Wish_9_internal_tempc_Type(Integer32):
    """Custom type wish_9_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_internal_tempc_Type.__name__ = "Integer32"
_Wish_9_internal_tempc_Object = MibScalar
wish_9_internal_tempc = _Wish_9_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 1, 2),
    _Wish_9_internal_tempc_Type()
)
wish_9_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_internal_tempc.setStatus("mandatory")


class _Wish_9_internal_tempf_Type(Integer32):
    """Custom type wish_9_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_internal_tempf_Type.__name__ = "Integer32"
_Wish_9_internal_tempf_Object = MibScalar
wish_9_internal_tempf = _Wish_9_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 1, 3),
    _Wish_9_internal_tempf_Type()
)
wish_9_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_internal_tempf.setStatus("mandatory")
_Wish_9_external_ObjectIdentity = ObjectIdentity
wish_9_external = _Wish_9_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2)
)
_Wish_9_external_1_ObjectIdentity = ObjectIdentity
wish_9_external_1 = _Wish_9_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 1)
)


class _Wish_9_external_1_type_Type(Integer32):
    """Custom type wish_9_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_1_type_Type.__name__ = "Integer32"
_Wish_9_external_1_type_Object = MibScalar
wish_9_external_1_type = _Wish_9_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 1, 1),
    _Wish_9_external_1_type_Type()
)
wish_9_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_1_type.setStatus("mandatory")


class _Wish_9_external_1_val1_Type(Integer32):
    """Custom type wish_9_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_1_val1_Type.__name__ = "Integer32"
_Wish_9_external_1_val1_Object = MibScalar
wish_9_external_1_val1 = _Wish_9_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 1, 2),
    _Wish_9_external_1_val1_Type()
)
wish_9_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_1_val1.setStatus("mandatory")


class _Wish_9_external_1_val2_Type(Integer32):
    """Custom type wish_9_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_1_val2_Type.__name__ = "Integer32"
_Wish_9_external_1_val2_Object = MibScalar
wish_9_external_1_val2 = _Wish_9_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 1, 3),
    _Wish_9_external_1_val2_Type()
)
wish_9_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_1_val2.setStatus("mandatory")


class _Wish_9_external_1_val3_Type(Integer32):
    """Custom type wish_9_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_1_val3_Type.__name__ = "Integer32"
_Wish_9_external_1_val3_Object = MibScalar
wish_9_external_1_val3 = _Wish_9_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 1, 4),
    _Wish_9_external_1_val3_Type()
)
wish_9_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_1_val3.setStatus("mandatory")


class _Wish_9_external_1_val4_Type(Integer32):
    """Custom type wish_9_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_1_val4_Type.__name__ = "Integer32"
_Wish_9_external_1_val4_Object = MibScalar
wish_9_external_1_val4 = _Wish_9_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 1, 5),
    _Wish_9_external_1_val4_Type()
)
wish_9_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_1_val4.setStatus("mandatory")


class _Wish_9_external_1_val5_Type(Integer32):
    """Custom type wish_9_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_1_val5_Type.__name__ = "Integer32"
_Wish_9_external_1_val5_Object = MibScalar
wish_9_external_1_val5 = _Wish_9_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 1, 6),
    _Wish_9_external_1_val5_Type()
)
wish_9_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_1_val5.setStatus("mandatory")
_Wish_9_external_2_ObjectIdentity = ObjectIdentity
wish_9_external_2 = _Wish_9_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 2)
)


class _Wish_9_external_2_type_Type(Integer32):
    """Custom type wish_9_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_2_type_Type.__name__ = "Integer32"
_Wish_9_external_2_type_Object = MibScalar
wish_9_external_2_type = _Wish_9_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 2, 1),
    _Wish_9_external_2_type_Type()
)
wish_9_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_2_type.setStatus("mandatory")


class _Wish_9_external_2_val1_Type(Integer32):
    """Custom type wish_9_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_2_val1_Type.__name__ = "Integer32"
_Wish_9_external_2_val1_Object = MibScalar
wish_9_external_2_val1 = _Wish_9_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 2, 2),
    _Wish_9_external_2_val1_Type()
)
wish_9_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_2_val1.setStatus("mandatory")


class _Wish_9_external_2_val2_Type(Integer32):
    """Custom type wish_9_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_2_val2_Type.__name__ = "Integer32"
_Wish_9_external_2_val2_Object = MibScalar
wish_9_external_2_val2 = _Wish_9_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 2, 3),
    _Wish_9_external_2_val2_Type()
)
wish_9_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_2_val2.setStatus("mandatory")


class _Wish_9_external_2_val3_Type(Integer32):
    """Custom type wish_9_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_2_val3_Type.__name__ = "Integer32"
_Wish_9_external_2_val3_Object = MibScalar
wish_9_external_2_val3 = _Wish_9_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 2, 4),
    _Wish_9_external_2_val3_Type()
)
wish_9_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_2_val3.setStatus("mandatory")


class _Wish_9_external_2_val4_Type(Integer32):
    """Custom type wish_9_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_2_val4_Type.__name__ = "Integer32"
_Wish_9_external_2_val4_Object = MibScalar
wish_9_external_2_val4 = _Wish_9_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 2, 5),
    _Wish_9_external_2_val4_Type()
)
wish_9_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_2_val4.setStatus("mandatory")


class _Wish_9_external_2_val5_Type(Integer32):
    """Custom type wish_9_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_9_external_2_val5_Type.__name__ = "Integer32"
_Wish_9_external_2_val5_Object = MibScalar
wish_9_external_2_val5 = _Wish_9_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 2, 6),
    _Wish_9_external_2_val5_Type()
)
wish_9_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_2_val5.setStatus("mandatory")


class _Wish_9_external_switch_Type(Integer32):
    """Custom type wish_9_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_9_external_switch_Type.__name__ = "Integer32"
_Wish_9_external_switch_Object = MibScalar
wish_9_external_switch = _Wish_9_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 9, 4, 2, 3),
    _Wish_9_external_switch_Type()
)
wish_9_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_9_external_switch.setStatus("mandatory")
_Wish_10_ObjectIdentity = ObjectIdentity
wish_10 = _Wish_10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10)
)


class _Wish_10_enabled_Type(Integer32):
    """Custom type wish_10_enabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_10_enabled_Type.__name__ = "Integer32"
_Wish_10_enabled_Object = MibScalar
wish_10_enabled = _Wish_10_enabled_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 1),
    _Wish_10_enabled_Type()
)
wish_10_enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_enabled.setStatus("mandatory")
_Wish_10_serial_num_Type = OctetString
_Wish_10_serial_num_Object = MibScalar
wish_10_serial_num = _Wish_10_serial_num_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 2),
    _Wish_10_serial_num_Type()
)
wish_10_serial_num.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_serial_num.setStatus("mandatory")


class _Wish_10_updates_Type(Integer32):
    """Custom type wish_10_updates based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_updates_Type.__name__ = "Integer32"
_Wish_10_updates_Object = MibScalar
wish_10_updates = _Wish_10_updates_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 3),
    _Wish_10_updates_Type()
)
wish_10_updates.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_updates.setStatus("mandatory")
_Wish_10_sensors_ObjectIdentity = ObjectIdentity
wish_10_sensors = _Wish_10_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4)
)
_Wish_10_internal_ObjectIdentity = ObjectIdentity
wish_10_internal = _Wish_10_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 1)
)


class _Wish_10_battery_voltage_Type(Integer32):
    """Custom type wish_10_battery_voltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_battery_voltage_Type.__name__ = "Integer32"
_Wish_10_battery_voltage_Object = MibScalar
wish_10_battery_voltage = _Wish_10_battery_voltage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 1, 1),
    _Wish_10_battery_voltage_Type()
)
wish_10_battery_voltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_battery_voltage.setStatus("mandatory")


class _Wish_10_internal_tempc_Type(Integer32):
    """Custom type wish_10_internal_tempc based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_internal_tempc_Type.__name__ = "Integer32"
_Wish_10_internal_tempc_Object = MibScalar
wish_10_internal_tempc = _Wish_10_internal_tempc_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 1, 2),
    _Wish_10_internal_tempc_Type()
)
wish_10_internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_internal_tempc.setStatus("mandatory")


class _Wish_10_internal_tempf_Type(Integer32):
    """Custom type wish_10_internal_tempf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_internal_tempf_Type.__name__ = "Integer32"
_Wish_10_internal_tempf_Object = MibScalar
wish_10_internal_tempf = _Wish_10_internal_tempf_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 1, 3),
    _Wish_10_internal_tempf_Type()
)
wish_10_internal_tempf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_internal_tempf.setStatus("mandatory")
_Wish_10_external_ObjectIdentity = ObjectIdentity
wish_10_external = _Wish_10_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2)
)
_Wish_10_external_1_ObjectIdentity = ObjectIdentity
wish_10_external_1 = _Wish_10_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 1)
)


class _Wish_10_external_1_type_Type(Integer32):
    """Custom type wish_10_external_1_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_1_type_Type.__name__ = "Integer32"
_Wish_10_external_1_type_Object = MibScalar
wish_10_external_1_type = _Wish_10_external_1_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 1, 1),
    _Wish_10_external_1_type_Type()
)
wish_10_external_1_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_1_type.setStatus("mandatory")


class _Wish_10_external_1_val1_Type(Integer32):
    """Custom type wish_10_external_1_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_1_val1_Type.__name__ = "Integer32"
_Wish_10_external_1_val1_Object = MibScalar
wish_10_external_1_val1 = _Wish_10_external_1_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 1, 2),
    _Wish_10_external_1_val1_Type()
)
wish_10_external_1_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_1_val1.setStatus("mandatory")


class _Wish_10_external_1_val2_Type(Integer32):
    """Custom type wish_10_external_1_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_1_val2_Type.__name__ = "Integer32"
_Wish_10_external_1_val2_Object = MibScalar
wish_10_external_1_val2 = _Wish_10_external_1_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 1, 3),
    _Wish_10_external_1_val2_Type()
)
wish_10_external_1_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_1_val2.setStatus("mandatory")


class _Wish_10_external_1_val3_Type(Integer32):
    """Custom type wish_10_external_1_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_1_val3_Type.__name__ = "Integer32"
_Wish_10_external_1_val3_Object = MibScalar
wish_10_external_1_val3 = _Wish_10_external_1_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 1, 4),
    _Wish_10_external_1_val3_Type()
)
wish_10_external_1_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_1_val3.setStatus("mandatory")


class _Wish_10_external_1_val4_Type(Integer32):
    """Custom type wish_10_external_1_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_1_val4_Type.__name__ = "Integer32"
_Wish_10_external_1_val4_Object = MibScalar
wish_10_external_1_val4 = _Wish_10_external_1_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 1, 5),
    _Wish_10_external_1_val4_Type()
)
wish_10_external_1_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_1_val4.setStatus("mandatory")


class _Wish_10_external_1_val5_Type(Integer32):
    """Custom type wish_10_external_1_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_1_val5_Type.__name__ = "Integer32"
_Wish_10_external_1_val5_Object = MibScalar
wish_10_external_1_val5 = _Wish_10_external_1_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 1, 6),
    _Wish_10_external_1_val5_Type()
)
wish_10_external_1_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_1_val5.setStatus("mandatory")
_Wish_10_external_2_ObjectIdentity = ObjectIdentity
wish_10_external_2 = _Wish_10_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 2)
)


class _Wish_10_external_2_type_Type(Integer32):
    """Custom type wish_10_external_2_type based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_2_type_Type.__name__ = "Integer32"
_Wish_10_external_2_type_Object = MibScalar
wish_10_external_2_type = _Wish_10_external_2_type_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 2, 1),
    _Wish_10_external_2_type_Type()
)
wish_10_external_2_type.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_2_type.setStatus("mandatory")


class _Wish_10_external_2_val1_Type(Integer32):
    """Custom type wish_10_external_2_val1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_2_val1_Type.__name__ = "Integer32"
_Wish_10_external_2_val1_Object = MibScalar
wish_10_external_2_val1 = _Wish_10_external_2_val1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 2, 2),
    _Wish_10_external_2_val1_Type()
)
wish_10_external_2_val1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_2_val1.setStatus("mandatory")


class _Wish_10_external_2_val2_Type(Integer32):
    """Custom type wish_10_external_2_val2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_2_val2_Type.__name__ = "Integer32"
_Wish_10_external_2_val2_Object = MibScalar
wish_10_external_2_val2 = _Wish_10_external_2_val2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 2, 3),
    _Wish_10_external_2_val2_Type()
)
wish_10_external_2_val2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_2_val2.setStatus("mandatory")


class _Wish_10_external_2_val3_Type(Integer32):
    """Custom type wish_10_external_2_val3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_2_val3_Type.__name__ = "Integer32"
_Wish_10_external_2_val3_Object = MibScalar
wish_10_external_2_val3 = _Wish_10_external_2_val3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 2, 4),
    _Wish_10_external_2_val3_Type()
)
wish_10_external_2_val3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_2_val3.setStatus("mandatory")


class _Wish_10_external_2_val4_Type(Integer32):
    """Custom type wish_10_external_2_val4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_2_val4_Type.__name__ = "Integer32"
_Wish_10_external_2_val4_Object = MibScalar
wish_10_external_2_val4 = _Wish_10_external_2_val4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 2, 5),
    _Wish_10_external_2_val4_Type()
)
wish_10_external_2_val4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_2_val4.setStatus("mandatory")


class _Wish_10_external_2_val5_Type(Integer32):
    """Custom type wish_10_external_2_val5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Wish_10_external_2_val5_Type.__name__ = "Integer32"
_Wish_10_external_2_val5_Object = MibScalar
wish_10_external_2_val5 = _Wish_10_external_2_val5_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 2, 6),
    _Wish_10_external_2_val5_Type()
)
wish_10_external_2_val5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_2_val5.setStatus("mandatory")


class _Wish_10_external_switch_Type(Integer32):
    """Custom type wish_10_external_switch based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Wish_10_external_switch_Type.__name__ = "Integer32"
_Wish_10_external_switch_Object = MibScalar
wish_10_external_switch = _Wish_10_external_switch_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 10, 4, 2, 3),
    _Wish_10_external_switch_Type()
)
wish_10_external_switch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wish_10_external_switch.setStatus("mandatory")
_Wish_11_ObjectIdentity = ObjectIdentity
wish_11 = _Wish_11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 11)
)
_Wish_11_sensors_ObjectIdentity = ObjectIdentity
wish_11_sensors = _Wish_11_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 11, 4)
)
_Wish_11_internal_ObjectIdentity = ObjectIdentity
wish_11_internal = _Wish_11_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 11, 4, 1)
)
_Wish_11_external_ObjectIdentity = ObjectIdentity
wish_11_external = _Wish_11_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 11, 4, 2)
)
_Wish_11_external_1_ObjectIdentity = ObjectIdentity
wish_11_external_1 = _Wish_11_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 11, 4, 2, 1)
)
_Wish_11_external_2_ObjectIdentity = ObjectIdentity
wish_11_external_2 = _Wish_11_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 11, 4, 2, 2)
)
_Wish_12_ObjectIdentity = ObjectIdentity
wish_12 = _Wish_12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 12)
)
_Wish_12_sensors_ObjectIdentity = ObjectIdentity
wish_12_sensors = _Wish_12_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 12, 4)
)
_Wish_12_internal_ObjectIdentity = ObjectIdentity
wish_12_internal = _Wish_12_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 12, 4, 1)
)
_Wish_12_external_ObjectIdentity = ObjectIdentity
wish_12_external = _Wish_12_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 12, 4, 2)
)
_Wish_12_external_1_ObjectIdentity = ObjectIdentity
wish_12_external_1 = _Wish_12_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 12, 4, 2, 1)
)
_Wish_12_external_2_ObjectIdentity = ObjectIdentity
wish_12_external_2 = _Wish_12_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 12, 4, 2, 2)
)
_Wish_13_ObjectIdentity = ObjectIdentity
wish_13 = _Wish_13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 13)
)
_Wish_13_sensors_ObjectIdentity = ObjectIdentity
wish_13_sensors = _Wish_13_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 13, 4)
)
_Wish_13_internal_ObjectIdentity = ObjectIdentity
wish_13_internal = _Wish_13_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 13, 4, 1)
)
_Wish_13_external_ObjectIdentity = ObjectIdentity
wish_13_external = _Wish_13_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 13, 4, 2)
)
_Wish_13_external_1_ObjectIdentity = ObjectIdentity
wish_13_external_1 = _Wish_13_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 13, 4, 2, 1)
)
_Wish_13_external_2_ObjectIdentity = ObjectIdentity
wish_13_external_2 = _Wish_13_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 13, 4, 2, 2)
)
_Wish_14_ObjectIdentity = ObjectIdentity
wish_14 = _Wish_14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 14)
)
_Wish_14_sensors_ObjectIdentity = ObjectIdentity
wish_14_sensors = _Wish_14_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 14, 4)
)
_Wish_14_internal_ObjectIdentity = ObjectIdentity
wish_14_internal = _Wish_14_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 14, 4, 1)
)
_Wish_14_external_ObjectIdentity = ObjectIdentity
wish_14_external = _Wish_14_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 14, 4, 2)
)
_Wish_14_external_1_ObjectIdentity = ObjectIdentity
wish_14_external_1 = _Wish_14_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 14, 4, 2, 1)
)
_Wish_14_external_2_ObjectIdentity = ObjectIdentity
wish_14_external_2 = _Wish_14_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 14, 4, 2, 2)
)
_Wish_15_ObjectIdentity = ObjectIdentity
wish_15 = _Wish_15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 15)
)
_Wish_15_sensors_ObjectIdentity = ObjectIdentity
wish_15_sensors = _Wish_15_sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 15, 4)
)
_Wish_15_internal_ObjectIdentity = ObjectIdentity
wish_15_internal = _Wish_15_internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 15, 4, 1)
)
_Wish_15_external_ObjectIdentity = ObjectIdentity
wish_15_external = _Wish_15_external_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 15, 4, 2)
)
_Wish_15_external_1_ObjectIdentity = ObjectIdentity
wish_15_external_1 = _Wish_15_external_1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 15, 4, 2, 1)
)
_Wish_15_external_2_ObjectIdentity = ObjectIdentity
wish_15_external_2 = _Wish_15_external_2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 1, 4, 15, 4, 2, 2)
)
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 2)
)
_Alarmmessage_Type = OctetString
_Alarmmessage_Object = MibScalar
alarmmessage = _Alarmmessage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 2, 1),
    _Alarmmessage_Type()
)
alarmmessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmmessage.setStatus("mandatory")
_Lighttowers_ObjectIdentity = ObjectIdentity
lighttowers = _Lighttowers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3)
)
_Lighttower1_ObjectIdentity = ObjectIdentity
lighttower1 = _Lighttower1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 1)
)


class _Lighttower1_RE_Type(Integer32):
    """Custom type lighttower1_RE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower1_RE_Type.__name__ = "Integer32"
_Lighttower1_RE_Object = MibScalar
lighttower1_RE = _Lighttower1_RE_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 1, 1),
    _Lighttower1_RE_Type()
)
lighttower1_RE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower1_RE.setStatus("mandatory")


class _Lighttower1_OR_Type(Integer32):
    """Custom type lighttower1_OR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower1_OR_Type.__name__ = "Integer32"
_Lighttower1_OR_Object = MibScalar
lighttower1_OR = _Lighttower1_OR_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 1, 2),
    _Lighttower1_OR_Type()
)
lighttower1_OR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower1_OR.setStatus("mandatory")


class _Lighttower1_GR_Type(Integer32):
    """Custom type lighttower1_GR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower1_GR_Type.__name__ = "Integer32"
_Lighttower1_GR_Object = MibScalar
lighttower1_GR = _Lighttower1_GR_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 1, 3),
    _Lighttower1_GR_Type()
)
lighttower1_GR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower1_GR.setStatus("mandatory")


class _Lighttower1_WH_Type(Integer32):
    """Custom type lighttower1_WH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower1_WH_Type.__name__ = "Integer32"
_Lighttower1_WH_Object = MibScalar
lighttower1_WH = _Lighttower1_WH_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 1, 4),
    _Lighttower1_WH_Type()
)
lighttower1_WH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower1_WH.setStatus("mandatory")


class _Lighttower1_BL_Type(Integer32):
    """Custom type lighttower1_BL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower1_BL_Type.__name__ = "Integer32"
_Lighttower1_BL_Object = MibScalar
lighttower1_BL = _Lighttower1_BL_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 1, 5),
    _Lighttower1_BL_Type()
)
lighttower1_BL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower1_BL.setStatus("mandatory")


class _Lighttower1_A1_Type(Integer32):
    """Custom type lighttower1_A1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower1_A1_Type.__name__ = "Integer32"
_Lighttower1_A1_Object = MibScalar
lighttower1_A1 = _Lighttower1_A1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 1, 6),
    _Lighttower1_A1_Type()
)
lighttower1_A1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower1_A1.setStatus("mandatory")


class _Lighttower1_A2_Type(Integer32):
    """Custom type lighttower1_A2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower1_A2_Type.__name__ = "Integer32"
_Lighttower1_A2_Object = MibScalar
lighttower1_A2 = _Lighttower1_A2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 1, 7),
    _Lighttower1_A2_Type()
)
lighttower1_A2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower1_A2.setStatus("mandatory")


class _Lighttower1_RL_Type(Integer32):
    """Custom type lighttower1_RL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower1_RL_Type.__name__ = "Integer32"
_Lighttower1_RL_Object = MibScalar
lighttower1_RL = _Lighttower1_RL_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 1, 8),
    _Lighttower1_RL_Type()
)
lighttower1_RL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower1_RL.setStatus("mandatory")
_Lighttower2_ObjectIdentity = ObjectIdentity
lighttower2 = _Lighttower2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 2)
)


class _Lighttower2_RE_Type(Integer32):
    """Custom type lighttower2_RE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower2_RE_Type.__name__ = "Integer32"
_Lighttower2_RE_Object = MibScalar
lighttower2_RE = _Lighttower2_RE_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 2, 1),
    _Lighttower2_RE_Type()
)
lighttower2_RE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower2_RE.setStatus("mandatory")


class _Lighttower2_OR_Type(Integer32):
    """Custom type lighttower2_OR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower2_OR_Type.__name__ = "Integer32"
_Lighttower2_OR_Object = MibScalar
lighttower2_OR = _Lighttower2_OR_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 2, 2),
    _Lighttower2_OR_Type()
)
lighttower2_OR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower2_OR.setStatus("mandatory")


class _Lighttower2_GR_Type(Integer32):
    """Custom type lighttower2_GR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower2_GR_Type.__name__ = "Integer32"
_Lighttower2_GR_Object = MibScalar
lighttower2_GR = _Lighttower2_GR_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 2, 3),
    _Lighttower2_GR_Type()
)
lighttower2_GR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower2_GR.setStatus("mandatory")


class _Lighttower2_WH_Type(Integer32):
    """Custom type lighttower2_WH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower2_WH_Type.__name__ = "Integer32"
_Lighttower2_WH_Object = MibScalar
lighttower2_WH = _Lighttower2_WH_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 2, 4),
    _Lighttower2_WH_Type()
)
lighttower2_WH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower2_WH.setStatus("mandatory")


class _Lighttower2_BL_Type(Integer32):
    """Custom type lighttower2_BL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower2_BL_Type.__name__ = "Integer32"
_Lighttower2_BL_Object = MibScalar
lighttower2_BL = _Lighttower2_BL_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 2, 5),
    _Lighttower2_BL_Type()
)
lighttower2_BL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower2_BL.setStatus("mandatory")


class _Lighttower2_A1_Type(Integer32):
    """Custom type lighttower2_A1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower2_A1_Type.__name__ = "Integer32"
_Lighttower2_A1_Object = MibScalar
lighttower2_A1 = _Lighttower2_A1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 2, 6),
    _Lighttower2_A1_Type()
)
lighttower2_A1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower2_A1.setStatus("mandatory")


class _Lighttower2_A2_Type(Integer32):
    """Custom type lighttower2_A2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower2_A2_Type.__name__ = "Integer32"
_Lighttower2_A2_Object = MibScalar
lighttower2_A2 = _Lighttower2_A2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 2, 7),
    _Lighttower2_A2_Type()
)
lighttower2_A2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower2_A2.setStatus("mandatory")


class _Lighttower2_RL_Type(Integer32):
    """Custom type lighttower2_RL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Lighttower2_RL_Type.__name__ = "Integer32"
_Lighttower2_RL_Object = MibScalar
lighttower2_RL = _Lighttower2_RL_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 3, 2, 8),
    _Lighttower2_RL_Type()
)
lighttower2_RL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lighttower2_RL.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tempalarm1_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 1)
)
tempalarm1_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempalarm1_32E.setStatus(
        ""
    )

room_alert_32E_snmp_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 2)
)
room_alert_32E_snmp_trap.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    room_alert_32E_snmp_trap.setStatus(
        ""
    )

tempalarm2_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 3)
)
tempalarm2_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempalarm2_32E.setStatus(
        ""
    )

tempclear2_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 4)
)
tempclear2_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempclear2_32E.setStatus(
        ""
    )

tempalarm3_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 5)
)
tempalarm3_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempalarm3_32E.setStatus(
        ""
    )

tempclear3_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 6)
)
tempclear3_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempclear3_32E.setStatus(
        ""
    )

humidityalarm1_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 7)
)
humidityalarm1_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityalarm1_32E.setStatus(
        ""
    )

humidityclear1_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 8)
)
humidityclear1_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityclear1_32E.setStatus(
        ""
    )

humidityalarm2_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 9)
)
humidityalarm2_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityalarm2_32E.setStatus(
        ""
    )

humidityclear2_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 10)
)
humidityclear2_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityclear2_32E.setStatus(
        ""
    )

humidityalarm3_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 11)
)
humidityalarm3_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityalarm3_32E.setStatus(
        ""
    )

humidityclear3_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 12)
)
humidityclear3_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityclear3_32E.setStatus(
        ""
    )

switchalarm1_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 13)
)
switchalarm1_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm1_32E.setStatus(
        ""
    )

switchclear1_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 14)
)
switchclear1_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear1_32E.setStatus(
        ""
    )

switchalarm2_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 15)
)
switchalarm2_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm2_32E.setStatus(
        ""
    )

switchclear2_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 16)
)
switchclear2_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear2_32E.setStatus(
        ""
    )

switchalarm3_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 17)
)
switchalarm3_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm3_32E.setStatus(
        ""
    )

switchclear3_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 18)
)
switchclear3_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear3_32E.setStatus(
        ""
    )

switchalarm4_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 19)
)
switchalarm4_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm4_32E.setStatus(
        ""
    )

switchclear4_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 20)
)
switchclear4_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear4_32E.setStatus(
        ""
    )

switchalarm5_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 21)
)
switchalarm5_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm5_32E.setStatus(
        ""
    )

switchclear5_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 22)
)
switchclear5_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear5_32E.setStatus(
        ""
    )

switchalarm6_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 23)
)
switchalarm6_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm6_32E.setStatus(
        ""
    )

switchclear6_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 24)
)
switchclear6_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear6_32E.setStatus(
        ""
    )

switchalarm7_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 25)
)
switchalarm7_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm7_32E.setStatus(
        ""
    )

switchclear7_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 26)
)
switchclear7_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear7_32E.setStatus(
        ""
    )

switchalarm8_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 27)
)
switchalarm8_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm8_32E.setStatus(
        ""
    )

switchclear8_32E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 8, 0, 28)
)
switchclear8_32E.setObjects(
    ("ROOMALERT32E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear8_32E.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROOMALERT32E-MIB",
    **{"avtech": avtech,
       "products": products,
       "roomalert32E": roomalert32E,
       "tempalarm1-32E": tempalarm1_32E,
       "room-alert-32E-snmp-trap": room_alert_32E_snmp_trap,
       "tempalarm2-32E": tempalarm2_32E,
       "tempclear2-32E": tempclear2_32E,
       "tempalarm3-32E": tempalarm3_32E,
       "tempclear3-32E": tempclear3_32E,
       "humidityalarm1-32E": humidityalarm1_32E,
       "humidityclear1-32E": humidityclear1_32E,
       "humidityalarm2-32E": humidityalarm2_32E,
       "humidityclear2-32E": humidityclear2_32E,
       "humidityalarm3-32E": humidityalarm3_32E,
       "humidityclear3-32E": humidityclear3_32E,
       "switchalarm1-32E": switchalarm1_32E,
       "switchclear1-32E": switchclear1_32E,
       "switchalarm2-32E": switchalarm2_32E,
       "switchclear2-32E": switchclear2_32E,
       "switchalarm3-32E": switchalarm3_32E,
       "switchclear3-32E": switchclear3_32E,
       "switchalarm4-32E": switchalarm4_32E,
       "switchclear4-32E": switchclear4_32E,
       "switchalarm5-32E": switchalarm5_32E,
       "switchclear5-32E": switchclear5_32E,
       "switchalarm6-32E": switchalarm6_32E,
       "switchclear6-32E": switchclear6_32E,
       "switchalarm7-32E": switchalarm7_32E,
       "switchclear7-32E": switchclear7_32E,
       "switchalarm8-32E": switchalarm8_32E,
       "switchclear8-32E": switchclear8_32E,
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
       "digital": digital,
       "digital-sen1": digital_sen1,
       "digital-sen1-1": digital_sen1_1,
       "digital-sen1-2": digital_sen1_2,
       "digital-sen1-3": digital_sen1_3,
       "digital-sen1-4": digital_sen1_4,
       "digital-sen1-5": digital_sen1_5,
       "digital-sen2": digital_sen2,
       "digital-sen2-1": digital_sen2_1,
       "digital-sen2-2": digital_sen2_2,
       "digital-sen2-3": digital_sen2_3,
       "digital-sen2-4": digital_sen2_4,
       "digital-sen2-5": digital_sen2_5,
       "digital-sen3": digital_sen3,
       "digital-sen3-1": digital_sen3_1,
       "digital-sen3-2": digital_sen3_2,
       "digital-sen3-3": digital_sen3_3,
       "digital-sen3-4": digital_sen3_4,
       "digital-sen3-5": digital_sen3_5,
       "digital-sen4": digital_sen4,
       "digital-sen4-1": digital_sen4_1,
       "digital-sen4-2": digital_sen4_2,
       "digital-sen4-3": digital_sen4_3,
       "digital-sen4-4": digital_sen4_4,
       "digital-sen4-5": digital_sen4_5,
       "digital-sen5": digital_sen5,
       "digital-sen5-1": digital_sen5_1,
       "digital-sen5-2": digital_sen5_2,
       "digital-sen5-3": digital_sen5_3,
       "digital-sen5-4": digital_sen5_4,
       "digital-sen5-5": digital_sen5_5,
       "digital-sen6": digital_sen6,
       "digital-sen6-1": digital_sen6_1,
       "digital-sen6-2": digital_sen6_2,
       "digital-sen6-3": digital_sen6_3,
       "digital-sen6-4": digital_sen6_4,
       "digital-sen6-5": digital_sen6_5,
       "digital-sen7": digital_sen7,
       "digital-sen7-1": digital_sen7_1,
       "digital-sen7-2": digital_sen7_2,
       "digital-sen7-3": digital_sen7_3,
       "digital-sen7-4": digital_sen7_4,
       "digital-sen7-5": digital_sen7_5,
       "digital-sen8": digital_sen8,
       "digital-sen8-1": digital_sen8_1,
       "digital-sen8-2": digital_sen8_2,
       "digital-sen8-3": digital_sen8_3,
       "digital-sen8-4": digital_sen8_4,
       "digital-sen8-5": digital_sen8_5,
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
       "wireless": wireless,
       "wish-1": wish_1,
       "wish-1-enabled": wish_1_enabled,
       "wish-1-serial-num": wish_1_serial_num,
       "wish-1-updates": wish_1_updates,
       "wish-1-sensors": wish_1_sensors,
       "wish-1-internal": wish_1_internal,
       "wish-1-battery-voltage": wish_1_battery_voltage,
       "wish-1-internal-tempc": wish_1_internal_tempc,
       "wish-1-internal-tempf": wish_1_internal_tempf,
       "wish-1-external": wish_1_external,
       "wish-1-external-1": wish_1_external_1,
       "wish-1-external-1-type": wish_1_external_1_type,
       "wish-1-external-1-val1": wish_1_external_1_val1,
       "wish-1-external-1-val2": wish_1_external_1_val2,
       "wish-1-external-1-val3": wish_1_external_1_val3,
       "wish-1-external-1-val4": wish_1_external_1_val4,
       "wish-1-external-1-val5": wish_1_external_1_val5,
       "wish-1-external-2": wish_1_external_2,
       "wish-1-external-2-type": wish_1_external_2_type,
       "wish-1-external-2-val1": wish_1_external_2_val1,
       "wish-1-external-2-val2": wish_1_external_2_val2,
       "wish-1-external-2-val3": wish_1_external_2_val3,
       "wish-1-external-2-val4": wish_1_external_2_val4,
       "wish-1-external-2-val5": wish_1_external_2_val5,
       "wish-1-external-switch": wish_1_external_switch,
       "wish-2": wish_2,
       "wish-2-enabled": wish_2_enabled,
       "wish-2-serial-num": wish_2_serial_num,
       "wish-2-updates": wish_2_updates,
       "wish-2-sensors": wish_2_sensors,
       "wish-2-internal": wish_2_internal,
       "wish-2-battery-voltage": wish_2_battery_voltage,
       "wish-2-internal-tempc": wish_2_internal_tempc,
       "wish-2-internal-tempf": wish_2_internal_tempf,
       "wish-2-external": wish_2_external,
       "wish-2-external-1": wish_2_external_1,
       "wish-2-external-1-type": wish_2_external_1_type,
       "wish-2-external-1-val1": wish_2_external_1_val1,
       "wish-2-external-1-val2": wish_2_external_1_val2,
       "wish-2-external-1-val3": wish_2_external_1_val3,
       "wish-2-external-1-val4": wish_2_external_1_val4,
       "wish-2-external-1-val5": wish_2_external_1_val5,
       "wish-2-external-2": wish_2_external_2,
       "wish-2-external-2-type": wish_2_external_2_type,
       "wish-2-external-2-val1": wish_2_external_2_val1,
       "wish-2-external-2-val2": wish_2_external_2_val2,
       "wish-2-external-2-val3": wish_2_external_2_val3,
       "wish-2-external-2-val4": wish_2_external_2_val4,
       "wish-2-external-2-val5": wish_2_external_2_val5,
       "wish-2-external-switch": wish_2_external_switch,
       "wish-3": wish_3,
       "wish-3-enabled": wish_3_enabled,
       "wish-3-serial-num": wish_3_serial_num,
       "wish-3-updates": wish_3_updates,
       "wish-3-sensors": wish_3_sensors,
       "wish-3-internal": wish_3_internal,
       "wish-3-battery-voltage": wish_3_battery_voltage,
       "wish-3-internal-tempc": wish_3_internal_tempc,
       "wish-3-internal-tempf": wish_3_internal_tempf,
       "wish-3-external": wish_3_external,
       "wish-3-external-1": wish_3_external_1,
       "wish-3-external-1-type": wish_3_external_1_type,
       "wish-3-external-1-val1": wish_3_external_1_val1,
       "wish-3-external-1-val2": wish_3_external_1_val2,
       "wish-3-external-1-val3": wish_3_external_1_val3,
       "wish-3-external-1-val4": wish_3_external_1_val4,
       "wish-3-external-1-val5": wish_3_external_1_val5,
       "wish-3-external-2": wish_3_external_2,
       "wish-3-external-2-type": wish_3_external_2_type,
       "wish-3-external-2-val1": wish_3_external_2_val1,
       "wish-3-external-2-val2": wish_3_external_2_val2,
       "wish-3-external-2-val3": wish_3_external_2_val3,
       "wish-3-external-2-val4": wish_3_external_2_val4,
       "wish-3-external-2-val5": wish_3_external_2_val5,
       "wish-3-external-switch": wish_3_external_switch,
       "wish-4": wish_4,
       "wish-4-enabled": wish_4_enabled,
       "wish-4-serial-num": wish_4_serial_num,
       "wish-4-updates": wish_4_updates,
       "wish-4-sensors": wish_4_sensors,
       "wish-4-internal": wish_4_internal,
       "wish-4-battery-voltage": wish_4_battery_voltage,
       "wish-4-internal-tempc": wish_4_internal_tempc,
       "wish-4-internal-tempf": wish_4_internal_tempf,
       "wish-4-external": wish_4_external,
       "wish-4-external-1": wish_4_external_1,
       "wish-4-external-1-type": wish_4_external_1_type,
       "wish-4-external-1-val1": wish_4_external_1_val1,
       "wish-4-external-1-val2": wish_4_external_1_val2,
       "wish-4-external-1-val3": wish_4_external_1_val3,
       "wish-4-external-1-val4": wish_4_external_1_val4,
       "wish-4-external-1-val5": wish_4_external_1_val5,
       "wish-4-external-2": wish_4_external_2,
       "wish-4-external-2-type": wish_4_external_2_type,
       "wish-4-external-2-val1": wish_4_external_2_val1,
       "wish-4-external-2-val2": wish_4_external_2_val2,
       "wish-4-external-2-val3": wish_4_external_2_val3,
       "wish-4-external-2-val4": wish_4_external_2_val4,
       "wish-4-external-2-val5": wish_4_external_2_val5,
       "wish-4-external-switch": wish_4_external_switch,
       "wish-5": wish_5,
       "wish-5-enabled": wish_5_enabled,
       "wish-5-serial-num": wish_5_serial_num,
       "wish-5-updates": wish_5_updates,
       "wish-5-sensors": wish_5_sensors,
       "wish-5-internal": wish_5_internal,
       "wish-5-battery-voltage": wish_5_battery_voltage,
       "wish-5-internal-tempc": wish_5_internal_tempc,
       "wish-5-internal-tempf": wish_5_internal_tempf,
       "wish-5-external": wish_5_external,
       "wish-5-external-1": wish_5_external_1,
       "wish-5-external-1-type": wish_5_external_1_type,
       "wish-5-external-1-val1": wish_5_external_1_val1,
       "wish-5-external-1-val2": wish_5_external_1_val2,
       "wish-5-external-1-val3": wish_5_external_1_val3,
       "wish-5-external-1-val4": wish_5_external_1_val4,
       "wish-5-external-1-val5": wish_5_external_1_val5,
       "wish-5-external-2": wish_5_external_2,
       "wish-5-external-2-type": wish_5_external_2_type,
       "wish-5-external-2-val1": wish_5_external_2_val1,
       "wish-5-external-2-val2": wish_5_external_2_val2,
       "wish-5-external-2-val3": wish_5_external_2_val3,
       "wish-5-external-2-val4": wish_5_external_2_val4,
       "wish-5-external-2-val5": wish_5_external_2_val5,
       "wish-5-external-switch": wish_5_external_switch,
       "wish-6": wish_6,
       "wish-6-enabled": wish_6_enabled,
       "wish-6-serial-num": wish_6_serial_num,
       "wish-6-updates": wish_6_updates,
       "wish-6-sensors": wish_6_sensors,
       "wish-6-internal": wish_6_internal,
       "wish-6-battery-voltage": wish_6_battery_voltage,
       "wish-6-internal-tempc": wish_6_internal_tempc,
       "wish-6-internal-tempf": wish_6_internal_tempf,
       "wish-6-external": wish_6_external,
       "wish-6-external-1": wish_6_external_1,
       "wish-6-external-1-type": wish_6_external_1_type,
       "wish-6-external-1-val1": wish_6_external_1_val1,
       "wish-6-external-1-val2": wish_6_external_1_val2,
       "wish-6-external-1-val3": wish_6_external_1_val3,
       "wish-6-external-1-val4": wish_6_external_1_val4,
       "wish-6-external-1-val5": wish_6_external_1_val5,
       "wish-6-external-2": wish_6_external_2,
       "wish-6-external-2-type": wish_6_external_2_type,
       "wish-6-external-2-val1": wish_6_external_2_val1,
       "wish-6-external-2-val2": wish_6_external_2_val2,
       "wish-6-external-2-val3": wish_6_external_2_val3,
       "wish-6-external-2-val4": wish_6_external_2_val4,
       "wish-6-external-2-val5": wish_6_external_2_val5,
       "wish-6-external-switch": wish_6_external_switch,
       "wish-7": wish_7,
       "wish-7-enabled": wish_7_enabled,
       "wish-7-serial-num": wish_7_serial_num,
       "wish-7-updates": wish_7_updates,
       "wish-7-sensors": wish_7_sensors,
       "wish-7-internal": wish_7_internal,
       "wish-7-battery-voltage": wish_7_battery_voltage,
       "wish-7-internal-tempc": wish_7_internal_tempc,
       "wish-7-internal-tempf": wish_7_internal_tempf,
       "wish-7-external": wish_7_external,
       "wish-7-external-1": wish_7_external_1,
       "wish-7-external-1-type": wish_7_external_1_type,
       "wish-7-external-1-val1": wish_7_external_1_val1,
       "wish-7-external-1-val2": wish_7_external_1_val2,
       "wish-7-external-1-val3": wish_7_external_1_val3,
       "wish-7-external-1-val4": wish_7_external_1_val4,
       "wish-7-external-1-val5": wish_7_external_1_val5,
       "wish-7-external-2": wish_7_external_2,
       "wish-7-external-2-type": wish_7_external_2_type,
       "wish-7-external-2-val1": wish_7_external_2_val1,
       "wish-7-external-2-val2": wish_7_external_2_val2,
       "wish-7-external-2-val3": wish_7_external_2_val3,
       "wish-7-external-2-val4": wish_7_external_2_val4,
       "wish-7-external-2-val5": wish_7_external_2_val5,
       "wish-7-external-switch": wish_7_external_switch,
       "wish-8": wish_8,
       "wish-8-enabled": wish_8_enabled,
       "wish-8-serial-num": wish_8_serial_num,
       "wish-8-updates": wish_8_updates,
       "wish-8-sensors": wish_8_sensors,
       "wish-8-internal": wish_8_internal,
       "wish-8-battery-voltage": wish_8_battery_voltage,
       "wish-8-internal-tempc": wish_8_internal_tempc,
       "wish-8-internal-tempf": wish_8_internal_tempf,
       "wish-8-external": wish_8_external,
       "wish-8-external-1": wish_8_external_1,
       "wish-8-external-1-type": wish_8_external_1_type,
       "wish-8-external-1-val1": wish_8_external_1_val1,
       "wish-8-external-1-val2": wish_8_external_1_val2,
       "wish-8-external-1-val3": wish_8_external_1_val3,
       "wish-8-external-1-val4": wish_8_external_1_val4,
       "wish-8-external-1-val5": wish_8_external_1_val5,
       "wish-8-external-2": wish_8_external_2,
       "wish-8-external-2-type": wish_8_external_2_type,
       "wish-8-external-2-val1": wish_8_external_2_val1,
       "wish-8-external-2-val2": wish_8_external_2_val2,
       "wish-8-external-2-val3": wish_8_external_2_val3,
       "wish-8-external-2-val4": wish_8_external_2_val4,
       "wish-8-external-2-val5": wish_8_external_2_val5,
       "wish-8-external-switch": wish_8_external_switch,
       "wish-9": wish_9,
       "wish-9-enabled": wish_9_enabled,
       "wish-9-serial-num": wish_9_serial_num,
       "wish-9-updates": wish_9_updates,
       "wish-9-sensors": wish_9_sensors,
       "wish-9-internal": wish_9_internal,
       "wish-9-battery-voltage": wish_9_battery_voltage,
       "wish-9-internal-tempc": wish_9_internal_tempc,
       "wish-9-internal-tempf": wish_9_internal_tempf,
       "wish-9-external": wish_9_external,
       "wish-9-external-1": wish_9_external_1,
       "wish-9-external-1-type": wish_9_external_1_type,
       "wish-9-external-1-val1": wish_9_external_1_val1,
       "wish-9-external-1-val2": wish_9_external_1_val2,
       "wish-9-external-1-val3": wish_9_external_1_val3,
       "wish-9-external-1-val4": wish_9_external_1_val4,
       "wish-9-external-1-val5": wish_9_external_1_val5,
       "wish-9-external-2": wish_9_external_2,
       "wish-9-external-2-type": wish_9_external_2_type,
       "wish-9-external-2-val1": wish_9_external_2_val1,
       "wish-9-external-2-val2": wish_9_external_2_val2,
       "wish-9-external-2-val3": wish_9_external_2_val3,
       "wish-9-external-2-val4": wish_9_external_2_val4,
       "wish-9-external-2-val5": wish_9_external_2_val5,
       "wish-9-external-switch": wish_9_external_switch,
       "wish-10": wish_10,
       "wish-10-enabled": wish_10_enabled,
       "wish-10-serial-num": wish_10_serial_num,
       "wish-10-updates": wish_10_updates,
       "wish-10-sensors": wish_10_sensors,
       "wish-10-internal": wish_10_internal,
       "wish-10-battery-voltage": wish_10_battery_voltage,
       "wish-10-internal-tempc": wish_10_internal_tempc,
       "wish-10-internal-tempf": wish_10_internal_tempf,
       "wish-10-external": wish_10_external,
       "wish-10-external-1": wish_10_external_1,
       "wish-10-external-1-type": wish_10_external_1_type,
       "wish-10-external-1-val1": wish_10_external_1_val1,
       "wish-10-external-1-val2": wish_10_external_1_val2,
       "wish-10-external-1-val3": wish_10_external_1_val3,
       "wish-10-external-1-val4": wish_10_external_1_val4,
       "wish-10-external-1-val5": wish_10_external_1_val5,
       "wish-10-external-2": wish_10_external_2,
       "wish-10-external-2-type": wish_10_external_2_type,
       "wish-10-external-2-val1": wish_10_external_2_val1,
       "wish-10-external-2-val2": wish_10_external_2_val2,
       "wish-10-external-2-val3": wish_10_external_2_val3,
       "wish-10-external-2-val4": wish_10_external_2_val4,
       "wish-10-external-2-val5": wish_10_external_2_val5,
       "wish-10-external-switch": wish_10_external_switch,
       "wish-11": wish_11,
       "wish-11-sensors": wish_11_sensors,
       "wish-11-internal": wish_11_internal,
       "wish-11-external": wish_11_external,
       "wish-11-external-1": wish_11_external_1,
       "wish-11-external-2": wish_11_external_2,
       "wish-12": wish_12,
       "wish-12-sensors": wish_12_sensors,
       "wish-12-internal": wish_12_internal,
       "wish-12-external": wish_12_external,
       "wish-12-external-1": wish_12_external_1,
       "wish-12-external-2": wish_12_external_2,
       "wish-13": wish_13,
       "wish-13-sensors": wish_13_sensors,
       "wish-13-internal": wish_13_internal,
       "wish-13-external": wish_13_external,
       "wish-13-external-1": wish_13_external_1,
       "wish-13-external-2": wish_13_external_2,
       "wish-14": wish_14,
       "wish-14-sensors": wish_14_sensors,
       "wish-14-internal": wish_14_internal,
       "wish-14-external": wish_14_external,
       "wish-14-external-1": wish_14_external_1,
       "wish-14-external-2": wish_14_external_2,
       "wish-15": wish_15,
       "wish-15-sensors": wish_15_sensors,
       "wish-15-internal": wish_15_internal,
       "wish-15-external": wish_15_external,
       "wish-15-external-1": wish_15_external_1,
       "wish-15-external-2": wish_15_external_2,
       "traps": traps,
       "alarmmessage": alarmmessage,
       "lighttowers": lighttowers,
       "lighttower1": lighttower1,
       "lighttower1-RE": lighttower1_RE,
       "lighttower1-OR": lighttower1_OR,
       "lighttower1-GR": lighttower1_GR,
       "lighttower1-WH": lighttower1_WH,
       "lighttower1-BL": lighttower1_BL,
       "lighttower1-A1": lighttower1_A1,
       "lighttower1-A2": lighttower1_A2,
       "lighttower1-RL": lighttower1_RL,
       "lighttower2": lighttower2,
       "lighttower2-RE": lighttower2_RE,
       "lighttower2-OR": lighttower2_OR,
       "lighttower2-GR": lighttower2_GR,
       "lighttower2-WH": lighttower2_WH,
       "lighttower2-BL": lighttower2_BL,
       "lighttower2-A1": lighttower2_A1,
       "lighttower2-A2": lighttower2_A2,
       "lighttower2-RL": lighttower2_RL}
)
