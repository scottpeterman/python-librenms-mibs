# SNMP MIB module (ROOMALERT4E-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\avtech\ROOMALERT4E-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:16 2025
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
_Roomalert4E_ObjectIdentity = ObjectIdentity
roomalert4E = _Roomalert4E_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6)
)
_Sensors_ObjectIdentity = ObjectIdentity
sensors = _Sensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1)
)
_Internal_ObjectIdentity = ObjectIdentity
internal = _Internal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1)
)
_Temperature_ObjectIdentity = ObjectIdentity
temperature = _Temperature_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 1, 2),
    _Internal_tempc_Type()
)
internal_tempc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_tempc.setStatus("mandatory")
_Label_ObjectIdentity = ObjectIdentity
label = _Label_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 2)
)
_Internal_label_Type = OctetString
_Internal_label_Object = MibScalar
internal_label = _Internal_label_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 1, 2, 1),
    _Internal_label_Type()
)
internal_label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internal_label.setStatus("mandatory")
_Digital_ObjectIdentity = ObjectIdentity
digital = _Digital_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2)
)
_Digital_sen1_ObjectIdentity = ObjectIdentity
digital_sen1 = _Digital_sen1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 7),
    _Digital_sen1_7_Type()
)
digital_sen1_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_7.setStatus("mandatory")
_Digital_sen1_label_Type = OctetString
_Digital_sen1_label_Object = MibScalar
digital_sen1_label = _Digital_sen1_label_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 1, 8),
    _Digital_sen1_label_Type()
)
digital_sen1_label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen1_label.setStatus("mandatory")
_Digital_sen2_ObjectIdentity = ObjectIdentity
digital_sen2 = _Digital_sen2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 5),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 6),
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 7),
    _Digital_sen2_7_Type()
)
digital_sen2_7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_7.setStatus("mandatory")
_Digital_sen2_label_Type = OctetString
_Digital_sen2_label_Object = MibScalar
digital_sen2_label = _Digital_sen2_label_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 2, 2, 8),
    _Digital_sen2_label_Type()
)
digital_sen2_label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digital_sen2_label.setStatus("mandatory")
_Switch_ObjectIdentity = ObjectIdentity
switch = _Switch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3)
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
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3, 1),
    _Switch_sen1_Type()
)
switch_sen1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_sen1.setStatus("mandatory")
_Switch_label_Type = OctetString
_Switch_label_Object = MibScalar
switch_label = _Switch_label_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 1, 3, 2),
    _Switch_label_Type()
)
switch_label.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switch_label.setStatus("mandatory")
_Signaltower_ObjectIdentity = ObjectIdentity
signaltower = _Signaltower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 2)
)


class _Red_led_Type(Integer32):
    """Custom type red_led based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Red_led_Type.__name__ = "Integer32"
_Red_led_Object = MibScalar
red_led = _Red_led_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 1),
    _Red_led_Type()
)
red_led.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    red_led.setStatus("mandatory")


class _Amber_led_Type(Integer32):
    """Custom type amber_led based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Amber_led_Type.__name__ = "Integer32"
_Amber_led_Object = MibScalar
amber_led = _Amber_led_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 2),
    _Amber_led_Type()
)
amber_led.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amber_led.setStatus("mandatory")


class _Green_led_Type(Integer32):
    """Custom type green_led based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Green_led_Type.__name__ = "Integer32"
_Green_led_Object = MibScalar
green_led = _Green_led_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 3),
    _Green_led_Type()
)
green_led.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    green_led.setStatus("mandatory")


class _Blue_led_Type(Integer32):
    """Custom type blue_led based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Blue_led_Type.__name__ = "Integer32"
_Blue_led_Object = MibScalar
blue_led = _Blue_led_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 4),
    _Blue_led_Type()
)
blue_led.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    blue_led.setStatus("mandatory")


class _White_led_Type(Integer32):
    """Custom type white_led based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_White_led_Type.__name__ = "Integer32"
_White_led_Object = MibScalar
white_led = _White_led_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 5),
    _White_led_Type()
)
white_led.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    white_led.setStatus("mandatory")


class _Alarm1_Type(Integer32):
    """Custom type alarm1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm1_Type.__name__ = "Integer32"
_Alarm1_Object = MibScalar
alarm1 = _Alarm1_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 6),
    _Alarm1_Type()
)
alarm1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm1.setStatus("mandatory")


class _Alarm2_Type(Integer32):
    """Custom type alarm2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_Alarm2_Type.__name__ = "Integer32"
_Alarm2_Object = MibScalar
alarm2 = _Alarm2_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 2, 7),
    _Alarm2_Type()
)
alarm2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm2.setStatus("mandatory")
_Traps_ObjectIdentity = ObjectIdentity
traps = _Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 3)
)
_Alarmmessage_Type = OctetString
_Alarmmessage_Object = MibScalar
alarmmessage = _Alarmmessage_Object(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 3, 1),
    _Alarmmessage_Type()
)
alarmmessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alarmmessage.setStatus("mandatory")

# Managed Objects groups


# Notification objects

room_alert_4e_snmp_trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 20916, 1, 6, 0, 2)
)
room_alert_4e_snmp_trap.setObjects(
    ("ROOMALERT4E-MIB", "alarmmessage")
)
if mibBuilder.loadTexts:
    room_alert_4e_snmp_trap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ROOMALERT4E-MIB",
    **{"avtech": avtech,
       "products": products,
       "roomalert4E": roomalert4E,
       "room-alert-4e-snmp-trap": room_alert_4e_snmp_trap,
       "sensors": sensors,
       "internal": internal,
       "temperature": temperature,
       "internal-tempf": internal_tempf,
       "internal-tempc": internal_tempc,
       "label": label,
       "internal-label": internal_label,
       "digital": digital,
       "digital-sen1": digital_sen1,
       "digital-sen1-1": digital_sen1_1,
       "digital-sen1-2": digital_sen1_2,
       "digital-sen1-3": digital_sen1_3,
       "digital-sen1-4": digital_sen1_4,
       "digital-sen1-5": digital_sen1_5,
       "digital-sen1-6": digital_sen1_6,
       "digital-sen1-7": digital_sen1_7,
       "digital-sen1-label": digital_sen1_label,
       "digital-sen2": digital_sen2,
       "digital-sen2-1": digital_sen2_1,
       "digital-sen2-2": digital_sen2_2,
       "digital-sen2-3": digital_sen2_3,
       "digital-sen2-4": digital_sen2_4,
       "digital-sen2-5": digital_sen2_5,
       "digital-sen2-6": digital_sen2_6,
       "digital-sen2-7": digital_sen2_7,
       "digital-sen2-label": digital_sen2_label,
       "switch": switch,
       "switch-sen1": switch_sen1,
       "switch-label": switch_label,
       "signaltower": signaltower,
       "red-led": red_led,
       "amber-led": amber_led,
       "green-led": green_led,
       "blue-led": blue_led,
       "white-led": white_led,
       "alarm1": alarm1,
       "alarm2": alarm2,
       "traps": traps,
       "alarmmessage": alarmmessage}
)
