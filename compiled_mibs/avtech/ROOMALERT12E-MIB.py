# SNMP MIB module (ROOMALERT12E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\avtech\ROOMALERT12E-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:12 2025
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
_Roomalert12E_ObjectIdentity = ObjectIdentity
roomalert12E = _Roomalert12E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1)
)
_Internal_sen_ObjectIdentity = ObjectIdentity
internal_sen = _Internal_sen_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 1)
)


class _Internal_sen_1_Type(Integer32):
    """Custom type internal_sen_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_sen_1_Type.__name__ = "Integer32"
_Internal_sen_1_Object = MibScalar
internal_sen_1 = _Internal_sen_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 1, 1),
    _Internal_sen_1_Type()
)
internal_sen_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_sen_1.setStatus("mandatory")


class _Internal_sen_2_Type(Integer32):
    """Custom type internal_sen_2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Internal_sen_2_Type.__name__ = "Integer32"
_Internal_sen_2_Object = MibScalar
internal_sen_2 = _Internal_sen_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 1, 2),
    _Internal_sen_2_Type()
)
internal_sen_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_sen_2.setStatus("mandatory")
_Internal_sen_3_Type = OctetString
_Internal_sen_3_Object = MibScalar
internal_sen_3 = _Internal_sen_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 1, 3),
    _Internal_sen_3_Type()
)
internal_sen_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_sen_3.setStatus("mandatory")
_Digital_sen1_ObjectIdentity = ObjectIdentity
digital_sen1 = _Digital_sen1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 2)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 2, 7),
    _Digital_sen1_7_Type()
)
digital_sen1_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_7.setStatus("mandatory")
_Digital_sen1_8_Type = OctetString
_Digital_sen1_8_Object = MibScalar
digital_sen1_8 = _Digital_sen1_8_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 2, 8),
    _Digital_sen1_8_Type()
)
digital_sen1_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_8.setStatus("mandatory")
_Digital_sen2_ObjectIdentity = ObjectIdentity
digital_sen2 = _Digital_sen2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 3, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 3, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 3, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 3, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 3, 5),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 3, 6),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 3, 7),
    _Digital_sen2_7_Type()
)
digital_sen2_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_7.setStatus("mandatory")
_Digital_sen2_8_Type = OctetString
_Digital_sen2_8_Object = MibScalar
digital_sen2_8 = _Digital_sen2_8_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 3, 8),
    _Digital_sen2_8_Type()
)
digital_sen2_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_8.setStatus("mandatory")
_Digital_sen3_ObjectIdentity = ObjectIdentity
digital_sen3 = _Digital_sen3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 4)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 4, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 4, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 4, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 4, 5),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 4, 6),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 4, 7),
    _Digital_sen3_7_Type()
)
digital_sen3_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_7.setStatus("mandatory")
_Digital_sen3_8_Type = OctetString
_Digital_sen3_8_Object = MibScalar
digital_sen3_8 = _Digital_sen3_8_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 4, 8),
    _Digital_sen3_8_Type()
)
digital_sen3_8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen3_8.setStatus("mandatory")
_Switch1_ObjectIdentity = ObjectIdentity
switch1 = _Switch1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 5)
)


class _Switch_sen1_1_Type(Integer32):
    """Custom type switch_sen1_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen1_1_Type.__name__ = "Integer32"
_Switch_sen1_1_Object = MibScalar
switch_sen1_1 = _Switch_sen1_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 5, 1),
    _Switch_sen1_1_Type()
)
switch_sen1_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen1_1.setStatus("mandatory")
_Switch_sen1_2_Type = OctetString
_Switch_sen1_2_Object = MibScalar
switch_sen1_2 = _Switch_sen1_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 5, 2),
    _Switch_sen1_2_Type()
)
switch_sen1_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen1_2.setStatus("mandatory")
_Switch2_ObjectIdentity = ObjectIdentity
switch2 = _Switch2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 6)
)


class _Switch_sen2_Type(Integer32):
    """Custom type switch_sen2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen2_Type.__name__ = "Integer32"
_Switch_sen2_Object = MibScalar
switch_sen2 = _Switch_sen2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 6, 1),
    _Switch_sen2_Type()
)
switch_sen2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen2.setStatus("mandatory")
_Switch_sen2_2_Type = OctetString
_Switch_sen2_2_Object = MibScalar
switch_sen2_2 = _Switch_sen2_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 6, 2),
    _Switch_sen2_2_Type()
)
switch_sen2_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen2_2.setStatus("mandatory")
_Switch3_ObjectIdentity = ObjectIdentity
switch3 = _Switch3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 7)
)


class _Switch_sen3_Type(Integer32):
    """Custom type switch_sen3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen3_Type.__name__ = "Integer32"
_Switch_sen3_Object = MibScalar
switch_sen3 = _Switch_sen3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 7, 1),
    _Switch_sen3_Type()
)
switch_sen3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen3.setStatus("mandatory")
_Switch_sen3_2_Type = OctetString
_Switch_sen3_2_Object = MibScalar
switch_sen3_2 = _Switch_sen3_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 7, 2),
    _Switch_sen3_2_Type()
)
switch_sen3_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen3_2.setStatus("mandatory")
_Switch4_ObjectIdentity = ObjectIdentity
switch4 = _Switch4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 8)
)


class _Switch_sen4_Type(Integer32):
    """Custom type switch_sen4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Switch_sen4_Type.__name__ = "Integer32"
_Switch_sen4_Object = MibScalar
switch_sen4 = _Switch_sen4_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 8, 1),
    _Switch_sen4_Type()
)
switch_sen4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen4.setStatus("mandatory")
_Switch_sen4_2_Type = OctetString
_Switch_sen4_2_Object = MibScalar
switch_sen4_2 = _Switch_sen4_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 8, 2),
    _Switch_sen4_2_Type()
)
switch_sen4_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen4_2.setStatus("mandatory")
_Analog_ObjectIdentity = ObjectIdentity
analog = _Analog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 9)
)


class _Analog_1_Type(Integer32):
    """Custom type analog_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Analog_1_Type.__name__ = "Integer32"
_Analog_1_Object = MibScalar
analog_1 = _Analog_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 9, 1),
    _Analog_1_Type()
)
analog_1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog_1.setStatus("mandatory")
_Analog_2_Type = OctetString
_Analog_2_Object = MibScalar
analog_2 = _Analog_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 9, 2),
    _Analog_2_Type()
)
analog_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog_2.setStatus("mandatory")
_Analog_3_Type = OctetString
_Analog_3_Object = MibScalar
analog_3 = _Analog_3_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 9, 3),
    _Analog_3_Type()
)
analog_3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    analog_3.setStatus("mandatory")
_Relay_ObjectIdentity = ObjectIdentity
relay = _Relay_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 10)
)


class _Relay_1_Type(Integer32):
    """Custom type relay_1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Relay_1_Type.__name__ = "Integer32"
_Relay_1_Object = MibScalar
relay_1 = _Relay_1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 10, 1),
    _Relay_1_Type()
)
relay_1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    relay_1.setStatus("mandatory")
_Relay_2_Type = OctetString
_Relay_2_Object = MibScalar
relay_2 = _Relay_2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 1, 10, 2),
    _Relay_2_Type()
)
relay_2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    relay_2.setStatus("mandatory")
_LightTower_ObjectIdentity = ObjectIdentity
lightTower = _LightTower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 2)
)


class _LightTower_RE_Type(Integer32):
    """Custom type lightTower_RE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LightTower_RE_Type.__name__ = "Integer32"
_LightTower_RE_Object = MibScalar
lightTower_RE = _LightTower_RE_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 2, 1),
    _LightTower_RE_Type()
)
lightTower_RE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightTower_RE.setStatus("mandatory")


class _LightTower_OR_Type(Integer32):
    """Custom type lightTower_OR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LightTower_OR_Type.__name__ = "Integer32"
_LightTower_OR_Object = MibScalar
lightTower_OR = _LightTower_OR_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 2, 2),
    _LightTower_OR_Type()
)
lightTower_OR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightTower_OR.setStatus("mandatory")


class _LightTower_GR_Type(Integer32):
    """Custom type lightTower_GR based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LightTower_GR_Type.__name__ = "Integer32"
_LightTower_GR_Object = MibScalar
lightTower_GR = _LightTower_GR_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 2, 3),
    _LightTower_GR_Type()
)
lightTower_GR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightTower_GR.setStatus("mandatory")


class _LightTower_WH_Type(Integer32):
    """Custom type lightTower_WH based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LightTower_WH_Type.__name__ = "Integer32"
_LightTower_WH_Object = MibScalar
lightTower_WH = _LightTower_WH_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 2, 4),
    _LightTower_WH_Type()
)
lightTower_WH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightTower_WH.setStatus("mandatory")


class _LightTower_BL_Type(Integer32):
    """Custom type lightTower_BL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LightTower_BL_Type.__name__ = "Integer32"
_LightTower_BL_Object = MibScalar
lightTower_BL = _LightTower_BL_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 2, 5),
    _LightTower_BL_Type()
)
lightTower_BL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightTower_BL.setStatus("mandatory")


class _LightTower_A1_Type(Integer32):
    """Custom type lightTower_A1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LightTower_A1_Type.__name__ = "Integer32"
_LightTower_A1_Object = MibScalar
lightTower_A1 = _LightTower_A1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 2, 6),
    _LightTower_A1_Type()
)
lightTower_A1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightTower_A1.setStatus("mandatory")


class _LightTower_A2_Type(Integer32):
    """Custom type lightTower_A2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LightTower_A2_Type.__name__ = "Integer32"
_LightTower_A2_Object = MibScalar
lightTower_A2 = _LightTower_A2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 2, 7),
    _LightTower_A2_Type()
)
lightTower_A2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightTower_A2.setStatus("mandatory")


class _LightTower_RL_Type(Integer32):
    """Custom type lightTower_RL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_LightTower_RL_Type.__name__ = "Integer32"
_LightTower_RL_Object = MibScalar
lightTower_RL = _LightTower_RL_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 2, 8),
    _LightTower_RL_Type()
)
lightTower_RL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lightTower_RL.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 3)
)
_Alarmmessage_Type = OctetString
_Alarmmessage_Object = MibScalar
alarmmessage = _Alarmmessage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 3, 1),
    _Alarmmessage_Type()
)
alarmmessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmmessage.setStatus("mandatory")

# Managed Objects groups


# Notification objects

tempalarm1_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 1)
)
tempalarm1_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempalarm1_12E.setStatus(
        ""
    )

room_alert_12E_snmp_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 2)
)
room_alert_12E_snmp_trap.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    room_alert_12E_snmp_trap.setStatus(
        ""
    )

tempalarm2_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 3)
)
tempalarm2_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempalarm2_12E.setStatus(
        ""
    )

tempclear2_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 4)
)
tempclear2_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempclear2_12E.setStatus(
        ""
    )

tempalarm3_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 5)
)
tempalarm3_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempalarm3_12E.setStatus(
        ""
    )

tempclear3_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 6)
)
tempclear3_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    tempclear3_12E.setStatus(
        ""
    )

humidityalarm1_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 7)
)
humidityalarm1_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityalarm1_12E.setStatus(
        ""
    )

humidityclear1_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 8)
)
humidityclear1_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityclear1_12E.setStatus(
        ""
    )

humidityalarm2_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 9)
)
humidityalarm2_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityalarm2_12E.setStatus(
        ""
    )

humidityclear2_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 10)
)
humidityclear2_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityclear2_12E.setStatus(
        ""
    )

humidityalarm3_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 11)
)
humidityalarm3_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityalarm3_12E.setStatus(
        ""
    )

humidityclear3_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 12)
)
humidityclear3_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    humidityclear3_12E.setStatus(
        ""
    )

switchalarm1_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 13)
)
switchalarm1_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm1_12E.setStatus(
        ""
    )

switchclear1_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 14)
)
switchclear1_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear1_12E.setStatus(
        ""
    )

switchalarm2_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 15)
)
switchalarm2_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm2_12E.setStatus(
        ""
    )

switchclear2_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 16)
)
switchclear2_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear2_12E.setStatus(
        ""
    )

switchalarm3_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 17)
)
switchalarm3_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm3_12E.setStatus(
        ""
    )

switchclear3_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 18)
)
switchclear3_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear3_12E.setStatus(
        ""
    )

switchalarm4_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 19)
)
switchalarm4_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchalarm4_12E.setStatus(
        ""
    )

switchclear4_12E = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 10, 0, 20)
)
switchclear4_12E.setObjects(
    ("ROOMALERT12E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    switchclear4_12E.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROOMALERT12E-MIB",
    **{"avtech": avtech,
       "products": products,
       "roomalert12E": roomalert12E,
       "tempalarm1-12E": tempalarm1_12E,
       "room-alert-12E-snmp-trap": room_alert_12E_snmp_trap,
       "tempalarm2-12E": tempalarm2_12E,
       "tempclear2-12E": tempclear2_12E,
       "tempalarm3-12E": tempalarm3_12E,
       "tempclear3-12E": tempclear3_12E,
       "humidityalarm1-12E": humidityalarm1_12E,
       "humidityclear1-12E": humidityclear1_12E,
       "humidityalarm2-12E": humidityalarm2_12E,
       "humidityclear2-12E": humidityclear2_12E,
       "humidityalarm3-12E": humidityalarm3_12E,
       "humidityclear3-12E": humidityclear3_12E,
       "switchalarm1-12E": switchalarm1_12E,
       "switchclear1-12E": switchclear1_12E,
       "switchalarm2-12E": switchalarm2_12E,
       "switchclear2-12E": switchclear2_12E,
       "switchalarm3-12E": switchalarm3_12E,
       "switchclear3-12E": switchclear3_12E,
       "switchalarm4-12E": switchalarm4_12E,
       "switchclear4-12E": switchclear4_12E,
       "sensors": sensors,
       "internal-sen": internal_sen,
       "internal-sen-1": internal_sen_1,
       "internal-sen-2": internal_sen_2,
       "internal-sen-3": internal_sen_3,
       "digital-sen1": digital_sen1,
       "digital-sen1-1": digital_sen1_1,
       "digital-sen1-2": digital_sen1_2,
       "digital-sen1-3": digital_sen1_3,
       "digital-sen1-4": digital_sen1_4,
       "digital-sen1-5": digital_sen1_5,
       "digital-sen1-6": digital_sen1_6,
       "digital-sen1-7": digital_sen1_7,
       "digital-sen1-8": digital_sen1_8,
       "digital-sen2": digital_sen2,
       "digital-sen2-1": digital_sen2_1,
       "digital-sen2-2": digital_sen2_2,
       "digital-sen2-3": digital_sen2_3,
       "digital-sen2-4": digital_sen2_4,
       "digital-sen2-5": digital_sen2_5,
       "digital-sen2-6": digital_sen2_6,
       "digital-sen2-7": digital_sen2_7,
       "digital-sen2-8": digital_sen2_8,
       "digital-sen3": digital_sen3,
       "digital-sen3-1": digital_sen3_1,
       "digital-sen3-2": digital_sen3_2,
       "digital-sen3-3": digital_sen3_3,
       "digital-sen3-4": digital_sen3_4,
       "digital-sen3-5": digital_sen3_5,
       "digital-sen3-6": digital_sen3_6,
       "digital-sen3-7": digital_sen3_7,
       "digital-sen3-8": digital_sen3_8,
       "switch1": switch1,
       "switch-sen1-1": switch_sen1_1,
       "switch-sen1-2": switch_sen1_2,
       "switch2": switch2,
       "switch-sen2": switch_sen2,
       "switch-sen2-2": switch_sen2_2,
       "switch3": switch3,
       "switch-sen3": switch_sen3,
       "switch-sen3-2": switch_sen3_2,
       "switch4": switch4,
       "switch-sen4": switch_sen4,
       "switch-sen4-2": switch_sen4_2,
       "analog": analog,
       "analog-1": analog_1,
       "analog-2": analog_2,
       "analog-3": analog_3,
       "relay": relay,
       "relay-1": relay_1,
       "relay-2": relay_2,
       "lightTower": lightTower,
       "lightTower-RE": lightTower_RE,
       "lightTower-OR": lightTower_OR,
       "lightTower-GR": lightTower_GR,
       "lightTower-WH": lightTower_WH,
       "lightTower-BL": lightTower_BL,
       "lightTower-A1": lightTower_A1,
       "lightTower-A2": lightTower_A2,
       "lightTower-RL": lightTower_RL,
       "traps": traps,
       "alarmmessage": alarmmessage}
)
