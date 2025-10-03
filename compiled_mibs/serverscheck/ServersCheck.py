# SNMP MIB module (ServersCheck) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\serverscheck\ServersCheck
# Produced by pysmi-1.6.2 at Thu Oct  2 12:26:31 2025
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

_Serverscheck_ObjectIdentity = ObjectIdentity
serverscheck = _Serverscheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095)
)
_Product_ObjectIdentity = ObjectIdentity
product = _Product_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 1)
)
_Productname_Type = DisplayString
_Productname_Object = MibScalar
productname = _Productname_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 1),
    _Productname_Type()
)
productname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productname.setStatus("mandatory")
_Productversion_Type = DisplayString
_Productversion_Object = MibScalar
productversion = _Productversion_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 2),
    _Productversion_Type()
)
productversion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productversion.setStatus("mandatory")
_Productdate_Type = DisplayString
_Productdate_Object = MibScalar
productdate = _Productdate_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 3),
    _Productdate_Type()
)
productdate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productdate.setStatus("mandatory")
_Productusername_Type = DisplayString
_Productusername_Object = MibScalar
productusername = _Productusername_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 4),
    _Productusername_Type()
)
productusername.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productusername.setStatus("mandatory")
_Productuserloc_Type = DisplayString
_Productuserloc_Object = MibScalar
productuserloc = _Productuserloc_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 5),
    _Productuserloc_Type()
)
productuserloc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productuserloc.setStatus("mandatory")
_Productnetip_Type = IpAddress
_Productnetip_Object = MibScalar
productnetip = _Productnetip_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 6),
    _Productnetip_Type()
)
productnetip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productnetip.setStatus("mandatory")
_Productnetgateway_Type = IpAddress
_Productnetgateway_Object = MibScalar
productnetgateway = _Productnetgateway_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 7),
    _Productnetgateway_Type()
)
productnetgateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productnetgateway.setStatus("mandatory")
_Productnetpridns_Type = IpAddress
_Productnetpridns_Object = MibScalar
productnetpridns = _Productnetpridns_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 8),
    _Productnetpridns_Type()
)
productnetpridns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productnetpridns.setStatus("mandatory")
_Productnetsecdns_Type = IpAddress
_Productnetsecdns_Object = MibScalar
productnetsecdns = _Productnetsecdns_Object(
    (1, 3, 6, 1, 4, 1, 17095, 1, 9),
    _Productnetsecdns_Type()
)
productnetsecdns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    productnetsecdns.setStatus("mandatory")
_Setup_ObjectIdentity = ObjectIdentity
setup = _Setup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 2)
)
_Traps_Object = MibTable
traps = _Traps_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1)
)
if mibBuilder.loadTexts:
    traps.setStatus("mandatory")
_TrapEntry_Object = MibTableRow
trapEntry = _TrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1)
)
trapEntry.setIndexNames(
    (0, "ServersCheck", "trapReceiverNumber"),
)
if mibBuilder.loadTexts:
    trapEntry.setStatus("mandatory")


class _TrapReceiverNumber_Type(Integer32):
    """Custom type trapReceiverNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_TrapReceiverNumber_Type.__name__ = "Integer32"
_TrapReceiverNumber_Object = MibTableColumn
trapReceiverNumber = _TrapReceiverNumber_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 1),
    _TrapReceiverNumber_Type()
)
trapReceiverNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapReceiverNumber.setStatus("mandatory")


class _TrapEnabled_Type(Integer32):
    """Custom type trapEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_TrapEnabled_Type.__name__ = "Integer32"
_TrapEnabled_Object = MibTableColumn
trapEnabled = _TrapEnabled_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 2),
    _TrapEnabled_Type()
)
trapEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapEnabled.setStatus("mandatory")
_TrapReceiverIPAddress_Type = IpAddress
_TrapReceiverIPAddress_Object = MibTableColumn
trapReceiverIPAddress = _TrapReceiverIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 3),
    _TrapReceiverIPAddress_Type()
)
trapReceiverIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapReceiverIPAddress.setStatus("mandatory")
_TrapCommunity_Type = DisplayString
_TrapCommunity_Object = MibTableColumn
trapCommunity = _TrapCommunity_Object(
    (1, 3, 6, 1, 4, 1, 17095, 2, 1, 1, 4),
    _TrapCommunity_Type()
)
trapCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    trapCommunity.setStatus("mandatory")
_Control_ObjectIdentity = ObjectIdentity
control = _Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 3)
)
_Sensor1name_Type = DisplayString
_Sensor1name_Object = MibScalar
sensor1name = _Sensor1name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 1),
    _Sensor1name_Type()
)
sensor1name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1name.setStatus("mandatory")
_Sensor1Value_Type = DisplayString
_Sensor1Value_Object = MibScalar
sensor1Value = _Sensor1Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 2),
    _Sensor1Value_Type()
)
sensor1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1Value.setStatus("mandatory")
_Sensor1LastErrMsg_Type = DisplayString
_Sensor1LastErrMsg_Object = MibScalar
sensor1LastErrMsg = _Sensor1LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 3),
    _Sensor1LastErrMsg_Type()
)
sensor1LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1LastErrMsg.setStatus("mandatory")
_Sensor1LastErrTime_Type = DisplayString
_Sensor1LastErrTime_Object = MibScalar
sensor1LastErrTime = _Sensor1LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 4),
    _Sensor1LastErrTime_Type()
)
sensor1LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1LastErrTime.setStatus("mandatory")
_Sensor2name_Type = DisplayString
_Sensor2name_Object = MibScalar
sensor2name = _Sensor2name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 5),
    _Sensor2name_Type()
)
sensor2name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2name.setStatus("mandatory")
_Sensor2Value_Type = DisplayString
_Sensor2Value_Object = MibScalar
sensor2Value = _Sensor2Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 6),
    _Sensor2Value_Type()
)
sensor2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2Value.setStatus("mandatory")
_Sensor2LastErrMsg_Type = DisplayString
_Sensor2LastErrMsg_Object = MibScalar
sensor2LastErrMsg = _Sensor2LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 7),
    _Sensor2LastErrMsg_Type()
)
sensor2LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2LastErrMsg.setStatus("mandatory")
_Sensor2LastErrTime_Type = DisplayString
_Sensor2LastErrTime_Object = MibScalar
sensor2LastErrTime = _Sensor2LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 8),
    _Sensor2LastErrTime_Type()
)
sensor2LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2LastErrTime.setStatus("mandatory")
_Sensor3name_Type = DisplayString
_Sensor3name_Object = MibScalar
sensor3name = _Sensor3name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 9),
    _Sensor3name_Type()
)
sensor3name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3name.setStatus("mandatory")
_Sensor3Value_Type = DisplayString
_Sensor3Value_Object = MibScalar
sensor3Value = _Sensor3Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 10),
    _Sensor3Value_Type()
)
sensor3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3Value.setStatus("mandatory")
_Sensor3LastErrMsg_Type = DisplayString
_Sensor3LastErrMsg_Object = MibScalar
sensor3LastErrMsg = _Sensor3LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 11),
    _Sensor3LastErrMsg_Type()
)
sensor3LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3LastErrMsg.setStatus("mandatory")
_Sensor3LastErrTime_Type = DisplayString
_Sensor3LastErrTime_Object = MibScalar
sensor3LastErrTime = _Sensor3LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 12),
    _Sensor3LastErrTime_Type()
)
sensor3LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3LastErrTime.setStatus("mandatory")
_Sensor4name_Type = DisplayString
_Sensor4name_Object = MibScalar
sensor4name = _Sensor4name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 13),
    _Sensor4name_Type()
)
sensor4name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4name.setStatus("mandatory")
_Sensor4Value_Type = DisplayString
_Sensor4Value_Object = MibScalar
sensor4Value = _Sensor4Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 14),
    _Sensor4Value_Type()
)
sensor4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4Value.setStatus("mandatory")
_Sensor4LastErrMsg_Type = DisplayString
_Sensor4LastErrMsg_Object = MibScalar
sensor4LastErrMsg = _Sensor4LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 15),
    _Sensor4LastErrMsg_Type()
)
sensor4LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4LastErrMsg.setStatus("mandatory")
_Sensor4LastErrTime_Type = DisplayString
_Sensor4LastErrTime_Object = MibScalar
sensor4LastErrTime = _Sensor4LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 16),
    _Sensor4LastErrTime_Type()
)
sensor4LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4LastErrTime.setStatus("mandatory")
_Sensor5name_Type = DisplayString
_Sensor5name_Object = MibScalar
sensor5name = _Sensor5name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 17),
    _Sensor5name_Type()
)
sensor5name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5name.setStatus("mandatory")
_Sensor5Value_Type = DisplayString
_Sensor5Value_Object = MibScalar
sensor5Value = _Sensor5Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 18),
    _Sensor5Value_Type()
)
sensor5Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5Value.setStatus("mandatory")
_Sensor5LastErrMsg_Type = DisplayString
_Sensor5LastErrMsg_Object = MibScalar
sensor5LastErrMsg = _Sensor5LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 19),
    _Sensor5LastErrMsg_Type()
)
sensor5LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5LastErrMsg.setStatus("mandatory")
_Sensor5LastErrTime_Type = DisplayString
_Sensor5LastErrTime_Object = MibScalar
sensor5LastErrTime = _Sensor5LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 20),
    _Sensor5LastErrTime_Type()
)
sensor5LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5LastErrTime.setStatus("mandatory")
_Sensor6name_Type = DisplayString
_Sensor6name_Object = MibScalar
sensor6name = _Sensor6name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 21),
    _Sensor6name_Type()
)
sensor6name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6name.setStatus("mandatory")
_Sensor6Value_Type = DisplayString
_Sensor6Value_Object = MibScalar
sensor6Value = _Sensor6Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 22),
    _Sensor6Value_Type()
)
sensor6Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6Value.setStatus("mandatory")
_Sensor6LastErrMsg_Type = DisplayString
_Sensor6LastErrMsg_Object = MibScalar
sensor6LastErrMsg = _Sensor6LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 23),
    _Sensor6LastErrMsg_Type()
)
sensor6LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6LastErrMsg.setStatus("mandatory")
_Sensor6LastErrTime_Type = DisplayString
_Sensor6LastErrTime_Object = MibScalar
sensor6LastErrTime = _Sensor6LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 24),
    _Sensor6LastErrTime_Type()
)
sensor6LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6LastErrTime.setStatus("mandatory")
_Sensor7name_Type = DisplayString
_Sensor7name_Object = MibScalar
sensor7name = _Sensor7name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 25),
    _Sensor7name_Type()
)
sensor7name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7name.setStatus("mandatory")
_Sensor7Value_Type = DisplayString
_Sensor7Value_Object = MibScalar
sensor7Value = _Sensor7Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 26),
    _Sensor7Value_Type()
)
sensor7Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7Value.setStatus("mandatory")
_Sensor7LastErrMsg_Type = DisplayString
_Sensor7LastErrMsg_Object = MibScalar
sensor7LastErrMsg = _Sensor7LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 27),
    _Sensor7LastErrMsg_Type()
)
sensor7LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7LastErrMsg.setStatus("mandatory")
_Sensor7LastErrTime_Type = DisplayString
_Sensor7LastErrTime_Object = MibScalar
sensor7LastErrTime = _Sensor7LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 28),
    _Sensor7LastErrTime_Type()
)
sensor7LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7LastErrTime.setStatus("mandatory")
_Sensor8name_Type = DisplayString
_Sensor8name_Object = MibScalar
sensor8name = _Sensor8name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 29),
    _Sensor8name_Type()
)
sensor8name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8name.setStatus("mandatory")
_Sensor8Value_Type = DisplayString
_Sensor8Value_Object = MibScalar
sensor8Value = _Sensor8Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 30),
    _Sensor8Value_Type()
)
sensor8Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8Value.setStatus("mandatory")
_Sensor8LastErrMsg_Type = DisplayString
_Sensor8LastErrMsg_Object = MibScalar
sensor8LastErrMsg = _Sensor8LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 31),
    _Sensor8LastErrMsg_Type()
)
sensor8LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8LastErrMsg.setStatus("mandatory")
_Sensor8LastErrTime_Type = DisplayString
_Sensor8LastErrTime_Object = MibScalar
sensor8LastErrTime = _Sensor8LastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 3, 32),
    _Sensor8LastErrTime_Type()
)
sensor8LastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8LastErrTime.setStatus("mandatory")
_Trapalerts_ObjectIdentity = ObjectIdentity
trapalerts = _Trapalerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 4)
)
_Sensor1TrapErrMsg_Type = OctetString
_Sensor1TrapErrMsg_Object = MibScalar
sensor1TrapErrMsg = _Sensor1TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 1),
    _Sensor1TrapErrMsg_Type()
)
sensor1TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1TrapErrMsg.setStatus("mandatory")
_Sensor2TrapErrMsg_Type = OctetString
_Sensor2TrapErrMsg_Object = MibScalar
sensor2TrapErrMsg = _Sensor2TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 2),
    _Sensor2TrapErrMsg_Type()
)
sensor2TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2TrapErrMsg.setStatus("mandatory")
_Sensor3TrapErrMsg_Type = OctetString
_Sensor3TrapErrMsg_Object = MibScalar
sensor3TrapErrMsg = _Sensor3TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 3),
    _Sensor3TrapErrMsg_Type()
)
sensor3TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3TrapErrMsg.setStatus("mandatory")
_Sensor4TrapErrMsg_Type = OctetString
_Sensor4TrapErrMsg_Object = MibScalar
sensor4TrapErrMsg = _Sensor4TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 4),
    _Sensor4TrapErrMsg_Type()
)
sensor4TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4TrapErrMsg.setStatus("mandatory")
_Sensor5TrapErrMsg_Type = OctetString
_Sensor5TrapErrMsg_Object = MibScalar
sensor5TrapErrMsg = _Sensor5TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 5),
    _Sensor5TrapErrMsg_Type()
)
sensor5TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5TrapErrMsg.setStatus("mandatory")
_Sensor6TrapErrMsg_Type = OctetString
_Sensor6TrapErrMsg_Object = MibScalar
sensor6TrapErrMsg = _Sensor6TrapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 4, 6),
    _Sensor6TrapErrMsg_Type()
)
sensor6TrapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6TrapErrMsg.setStatus("mandatory")
_Iotrapalerts_ObjectIdentity = ObjectIdentity
iotrapalerts = _Iotrapalerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 5)
)
_IosensorINPUT1trapErrMsg_Type = OctetString
_IosensorINPUT1trapErrMsg_Object = MibScalar
iosensorINPUT1trapErrMsg = _IosensorINPUT1trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 1),
    _IosensorINPUT1trapErrMsg_Type()
)
iosensorINPUT1trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT1trapErrMsg.setStatus("mandatory")
_IosensorINPUT2trapErrMsg_Type = OctetString
_IosensorINPUT2trapErrMsg_Object = MibScalar
iosensorINPUT2trapErrMsg = _IosensorINPUT2trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 2),
    _IosensorINPUT2trapErrMsg_Type()
)
iosensorINPUT2trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT2trapErrMsg.setStatus("mandatory")
_IosensorINPUT3trapErrMsg_Type = OctetString
_IosensorINPUT3trapErrMsg_Object = MibScalar
iosensorINPUT3trapErrMsg = _IosensorINPUT3trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 3),
    _IosensorINPUT3trapErrMsg_Type()
)
iosensorINPUT3trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT3trapErrMsg.setStatus("mandatory")
_IosensorINPUT4trapErrMsg_Type = OctetString
_IosensorINPUT4trapErrMsg_Object = MibScalar
iosensorINPUT4trapErrMsg = _IosensorINPUT4trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 4),
    _IosensorINPUT4trapErrMsg_Type()
)
iosensorINPUT4trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT4trapErrMsg.setStatus("mandatory")
_IosensorINPUT5trapErrMsg_Type = OctetString
_IosensorINPUT5trapErrMsg_Object = MibScalar
iosensorINPUT5trapErrMsg = _IosensorINPUT5trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 5),
    _IosensorINPUT5trapErrMsg_Type()
)
iosensorINPUT5trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT5trapErrMsg.setStatus("mandatory")
_IosensorINPUT6trapErrMsg_Type = OctetString
_IosensorINPUT6trapErrMsg_Object = MibScalar
iosensorINPUT6trapErrMsg = _IosensorINPUT6trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 6),
    _IosensorINPUT6trapErrMsg_Type()
)
iosensorINPUT6trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT6trapErrMsg.setStatus("mandatory")
_IosensorINPUT7trapErrMsg_Type = OctetString
_IosensorINPUT7trapErrMsg_Object = MibScalar
iosensorINPUT7trapErrMsg = _IosensorINPUT7trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 7),
    _IosensorINPUT7trapErrMsg_Type()
)
iosensorINPUT7trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT7trapErrMsg.setStatus("mandatory")
_IosensorINPUT8trapErrMsg_Type = OctetString
_IosensorINPUT8trapErrMsg_Object = MibScalar
iosensorINPUT8trapErrMsg = _IosensorINPUT8trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 8),
    _IosensorINPUT8trapErrMsg_Type()
)
iosensorINPUT8trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT8trapErrMsg.setStatus("mandatory")
_IosensorINPUT9trapErrMsg_Type = OctetString
_IosensorINPUT9trapErrMsg_Object = MibScalar
iosensorINPUT9trapErrMsg = _IosensorINPUT9trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 9),
    _IosensorINPUT9trapErrMsg_Type()
)
iosensorINPUT9trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT9trapErrMsg.setStatus("mandatory")
_IosensorINPUT10trapErrMsg_Type = OctetString
_IosensorINPUT10trapErrMsg_Object = MibScalar
iosensorINPUT10trapErrMsg = _IosensorINPUT10trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 10),
    _IosensorINPUT10trapErrMsg_Type()
)
iosensorINPUT10trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT10trapErrMsg.setStatus("mandatory")
_IosensorINPUT11trapErrMsg_Type = OctetString
_IosensorINPUT11trapErrMsg_Object = MibScalar
iosensorINPUT11trapErrMsg = _IosensorINPUT11trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 11),
    _IosensorINPUT11trapErrMsg_Type()
)
iosensorINPUT11trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT11trapErrMsg.setStatus("mandatory")
_IosensorINPUT12trapErrMsg_Type = OctetString
_IosensorINPUT12trapErrMsg_Object = MibScalar
iosensorINPUT12trapErrMsg = _IosensorINPUT12trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 12),
    _IosensorINPUT12trapErrMsg_Type()
)
iosensorINPUT12trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT12trapErrMsg.setStatus("mandatory")
_IosensorINPUT13trapErrMsg_Type = OctetString
_IosensorINPUT13trapErrMsg_Object = MibScalar
iosensorINPUT13trapErrMsg = _IosensorINPUT13trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 13),
    _IosensorINPUT13trapErrMsg_Type()
)
iosensorINPUT13trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT13trapErrMsg.setStatus("mandatory")
_IosensorINPUT14trapErrMsg_Type = OctetString
_IosensorINPUT14trapErrMsg_Object = MibScalar
iosensorINPUT14trapErrMsg = _IosensorINPUT14trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 14),
    _IosensorINPUT14trapErrMsg_Type()
)
iosensorINPUT14trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT14trapErrMsg.setStatus("mandatory")
_IosensorINPUT15trapErrMsg_Type = OctetString
_IosensorINPUT15trapErrMsg_Object = MibScalar
iosensorINPUT15trapErrMsg = _IosensorINPUT15trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 15),
    _IosensorINPUT15trapErrMsg_Type()
)
iosensorINPUT15trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT15trapErrMsg.setStatus("mandatory")
_IosensorINPUT16trapErrMsg_Type = OctetString
_IosensorINPUT16trapErrMsg_Object = MibScalar
iosensorINPUT16trapErrMsg = _IosensorINPUT16trapErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 5, 16),
    _IosensorINPUT16trapErrMsg_Type()
)
iosensorINPUT16trapErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iosensorINPUT16trapErrMsg.setStatus("mandatory")
_Input_ObjectIdentity = ObjectIdentity
input = _Input_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 6)
)
_Input1name_Type = DisplayString
_Input1name_Object = MibScalar
input1name = _Input1name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 1),
    _Input1name_Type()
)
input1name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input1name.setStatus("mandatory")
_Input1Value_Type = DisplayString
_Input1Value_Object = MibScalar
input1Value = _Input1Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 2),
    _Input1Value_Type()
)
input1Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input1Value.setStatus("mandatory")
_Input1LastErrMsg_Type = DisplayString
_Input1LastErrMsg_Object = MibScalar
input1LastErrMsg = _Input1LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 3),
    _Input1LastErrMsg_Type()
)
input1LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input1LastErrMsg.setStatus("mandatory")
_Input2name_Type = DisplayString
_Input2name_Object = MibScalar
input2name = _Input2name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 4),
    _Input2name_Type()
)
input2name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input2name.setStatus("mandatory")
_Input2Value_Type = DisplayString
_Input2Value_Object = MibScalar
input2Value = _Input2Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 5),
    _Input2Value_Type()
)
input2Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input2Value.setStatus("mandatory")
_Input2LastErrMsg_Type = DisplayString
_Input2LastErrMsg_Object = MibScalar
input2LastErrMsg = _Input2LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 6),
    _Input2LastErrMsg_Type()
)
input2LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input2LastErrMsg.setStatus("mandatory")
_Input3name_Type = DisplayString
_Input3name_Object = MibScalar
input3name = _Input3name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 7),
    _Input3name_Type()
)
input3name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input3name.setStatus("mandatory")
_Input3Value_Type = DisplayString
_Input3Value_Object = MibScalar
input3Value = _Input3Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 8),
    _Input3Value_Type()
)
input3Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input3Value.setStatus("mandatory")
_Input3LastErrMsg_Type = DisplayString
_Input3LastErrMsg_Object = MibScalar
input3LastErrMsg = _Input3LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 9),
    _Input3LastErrMsg_Type()
)
input3LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input3LastErrMsg.setStatus("mandatory")
_Input4name_Type = DisplayString
_Input4name_Object = MibScalar
input4name = _Input4name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 10),
    _Input4name_Type()
)
input4name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input4name.setStatus("mandatory")
_Input4Value_Type = DisplayString
_Input4Value_Object = MibScalar
input4Value = _Input4Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 11),
    _Input4Value_Type()
)
input4Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input4Value.setStatus("mandatory")
_Input4LastErrMsg_Type = DisplayString
_Input4LastErrMsg_Object = MibScalar
input4LastErrMsg = _Input4LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 12),
    _Input4LastErrMsg_Type()
)
input4LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input4LastErrMsg.setStatus("mandatory")
_Input5name_Type = DisplayString
_Input5name_Object = MibScalar
input5name = _Input5name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 13),
    _Input5name_Type()
)
input5name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input5name.setStatus("mandatory")
_Input5Value_Type = DisplayString
_Input5Value_Object = MibScalar
input5Value = _Input5Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 14),
    _Input5Value_Type()
)
input5Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input5Value.setStatus("mandatory")
_Input5LastErrMsg_Type = DisplayString
_Input5LastErrMsg_Object = MibScalar
input5LastErrMsg = _Input5LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 15),
    _Input5LastErrMsg_Type()
)
input5LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input5LastErrMsg.setStatus("mandatory")
_Input6name_Type = DisplayString
_Input6name_Object = MibScalar
input6name = _Input6name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 16),
    _Input6name_Type()
)
input6name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input6name.setStatus("mandatory")
_Input6Value_Type = DisplayString
_Input6Value_Object = MibScalar
input6Value = _Input6Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 17),
    _Input6Value_Type()
)
input6Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input6Value.setStatus("mandatory")
_Input6LastErrMsg_Type = DisplayString
_Input6LastErrMsg_Object = MibScalar
input6LastErrMsg = _Input6LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 18),
    _Input6LastErrMsg_Type()
)
input6LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input6LastErrMsg.setStatus("mandatory")
_Input7name_Type = DisplayString
_Input7name_Object = MibScalar
input7name = _Input7name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 19),
    _Input7name_Type()
)
input7name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input7name.setStatus("mandatory")
_Input7Value_Type = DisplayString
_Input7Value_Object = MibScalar
input7Value = _Input7Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 20),
    _Input7Value_Type()
)
input7Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input7Value.setStatus("mandatory")
_Input7LastErrMsg_Type = DisplayString
_Input7LastErrMsg_Object = MibScalar
input7LastErrMsg = _Input7LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 21),
    _Input7LastErrMsg_Type()
)
input7LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input7LastErrMsg.setStatus("mandatory")
_Input8name_Type = DisplayString
_Input8name_Object = MibScalar
input8name = _Input8name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 22),
    _Input8name_Type()
)
input8name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input8name.setStatus("mandatory")
_Input8Value_Type = DisplayString
_Input8Value_Object = MibScalar
input8Value = _Input8Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 23),
    _Input8Value_Type()
)
input8Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input8Value.setStatus("mandatory")
_Input8LastErrMsg_Type = DisplayString
_Input8LastErrMsg_Object = MibScalar
input8LastErrMsg = _Input8LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 24),
    _Input8LastErrMsg_Type()
)
input8LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input8LastErrMsg.setStatus("mandatory")
_Input9name_Type = DisplayString
_Input9name_Object = MibScalar
input9name = _Input9name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 25),
    _Input9name_Type()
)
input9name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input9name.setStatus("mandatory")
_Input9Value_Type = DisplayString
_Input9Value_Object = MibScalar
input9Value = _Input9Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 26),
    _Input9Value_Type()
)
input9Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input9Value.setStatus("mandatory")
_Input9LastErrMsg_Type = DisplayString
_Input9LastErrMsg_Object = MibScalar
input9LastErrMsg = _Input9LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 27),
    _Input9LastErrMsg_Type()
)
input9LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input9LastErrMsg.setStatus("mandatory")
_Input10name_Type = DisplayString
_Input10name_Object = MibScalar
input10name = _Input10name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 28),
    _Input10name_Type()
)
input10name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input10name.setStatus("mandatory")
_Input10Value_Type = DisplayString
_Input10Value_Object = MibScalar
input10Value = _Input10Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 29),
    _Input10Value_Type()
)
input10Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input10Value.setStatus("mandatory")
_Input10LastErrMsg_Type = DisplayString
_Input10LastErrMsg_Object = MibScalar
input10LastErrMsg = _Input10LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 30),
    _Input10LastErrMsg_Type()
)
input10LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input10LastErrMsg.setStatus("mandatory")
_Input11name_Type = DisplayString
_Input11name_Object = MibScalar
input11name = _Input11name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 31),
    _Input11name_Type()
)
input11name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input11name.setStatus("mandatory")
_Input11Value_Type = DisplayString
_Input11Value_Object = MibScalar
input11Value = _Input11Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 32),
    _Input11Value_Type()
)
input11Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input11Value.setStatus("mandatory")
_Input11LastErrMsg_Type = DisplayString
_Input11LastErrMsg_Object = MibScalar
input11LastErrMsg = _Input11LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 33),
    _Input11LastErrMsg_Type()
)
input11LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input11LastErrMsg.setStatus("mandatory")
_Input12name_Type = DisplayString
_Input12name_Object = MibScalar
input12name = _Input12name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 34),
    _Input12name_Type()
)
input12name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input12name.setStatus("mandatory")
_Input12Value_Type = DisplayString
_Input12Value_Object = MibScalar
input12Value = _Input12Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 35),
    _Input12Value_Type()
)
input12Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input12Value.setStatus("mandatory")
_Input12LastErrMsg_Type = DisplayString
_Input12LastErrMsg_Object = MibScalar
input12LastErrMsg = _Input12LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 36),
    _Input12LastErrMsg_Type()
)
input12LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input12LastErrMsg.setStatus("mandatory")
_Input13name_Type = DisplayString
_Input13name_Object = MibScalar
input13name = _Input13name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 37),
    _Input13name_Type()
)
input13name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input13name.setStatus("mandatory")
_Input13Value_Type = DisplayString
_Input13Value_Object = MibScalar
input13Value = _Input13Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 38),
    _Input13Value_Type()
)
input13Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input13Value.setStatus("mandatory")
_Input13LastErrMsg_Type = DisplayString
_Input13LastErrMsg_Object = MibScalar
input13LastErrMsg = _Input13LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 39),
    _Input13LastErrMsg_Type()
)
input13LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input13LastErrMsg.setStatus("mandatory")
_Input14name_Type = DisplayString
_Input14name_Object = MibScalar
input14name = _Input14name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 40),
    _Input14name_Type()
)
input14name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input14name.setStatus("mandatory")
_Input14Value_Type = DisplayString
_Input14Value_Object = MibScalar
input14Value = _Input14Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 41),
    _Input14Value_Type()
)
input14Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input14Value.setStatus("mandatory")
_Input14LastErrMsg_Type = DisplayString
_Input14LastErrMsg_Object = MibScalar
input14LastErrMsg = _Input14LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 42),
    _Input14LastErrMsg_Type()
)
input14LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input14LastErrMsg.setStatus("mandatory")
_Input15name_Type = DisplayString
_Input15name_Object = MibScalar
input15name = _Input15name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 43),
    _Input15name_Type()
)
input15name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input15name.setStatus("mandatory")
_Input15Value_Type = DisplayString
_Input15Value_Object = MibScalar
input15Value = _Input15Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 44),
    _Input15Value_Type()
)
input15Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input15Value.setStatus("mandatory")
_Input15LastErrMsg_Type = DisplayString
_Input15LastErrMsg_Object = MibScalar
input15LastErrMsg = _Input15LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 45),
    _Input15LastErrMsg_Type()
)
input15LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input15LastErrMsg.setStatus("mandatory")
_Input16name_Type = DisplayString
_Input16name_Object = MibScalar
input16name = _Input16name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 46),
    _Input16name_Type()
)
input16name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input16name.setStatus("mandatory")
_Input16Value_Type = DisplayString
_Input16Value_Object = MibScalar
input16Value = _Input16Value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 47),
    _Input16Value_Type()
)
input16Value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input16Value.setStatus("mandatory")
_Input16LastErrMsg_Type = DisplayString
_Input16LastErrMsg_Object = MibScalar
input16LastErrMsg = _Input16LastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 6, 48),
    _Input16LastErrMsg_Type()
)
input16LastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    input16LastErrMsg.setStatus("mandatory")
_Output_ObjectIdentity = ObjectIdentity
output = _Output_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 7)
)
_Output1State_Type = DisplayString
_Output1State_Object = MibScalar
output1State = _Output1State_Object(
    (1, 3, 6, 1, 4, 1, 17095, 7, 1),
    _Output1State_Type()
)
output1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    output1State.setStatus("mandatory")
_Output2State_Type = DisplayString
_Output2State_Object = MibScalar
output2State = _Output2State_Object(
    (1, 3, 6, 1, 4, 1, 17095, 7, 2),
    _Output2State_Type()
)
output2State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    output2State.setStatus("mandatory")
_Output3State_Type = DisplayString
_Output3State_Object = MibScalar
output3State = _Output3State_Object(
    (1, 3, 6, 1, 4, 1, 17095, 7, 3),
    _Output3State_Type()
)
output3State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    output3State.setStatus("mandatory")
_Output4State_Type = DisplayString
_Output4State_Object = MibScalar
output4State = _Output4State_Object(
    (1, 3, 6, 1, 4, 1, 17095, 7, 4),
    _Output4State_Type()
)
output4State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    output4State.setStatus("mandatory")
_SensorTable_ObjectIdentity = ObjectIdentity
sensorTable = _SensorTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11)
)
_Sensor1_ObjectIdentity = ObjectIdentity
sensor1 = _Sensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 1)
)
_Sensor1Name_Type = DisplayString
_Sensor1Name_Object = MibScalar
sensor1Name = _Sensor1Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 1, 1),
    _Sensor1Name_Type()
)
sensor1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1Name.setStatus("mandatory")
_Sensor1value_Type = DisplayString
_Sensor1value_Object = MibScalar
sensor1value = _Sensor1value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 1, 2),
    _Sensor1value_Type()
)
sensor1value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1value.setStatus("mandatory")
_Sensor1ErrState_Type = DisplayString
_Sensor1ErrState_Object = MibScalar
sensor1ErrState = _Sensor1ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 1, 3),
    _Sensor1ErrState_Type()
)
sensor1ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1ErrState.setStatus("mandatory")
_Sensor1lastErrTime_Type = DisplayString
_Sensor1lastErrTime_Object = MibScalar
sensor1lastErrTime = _Sensor1lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 1, 4),
    _Sensor1lastErrTime_Type()
)
sensor1lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1lastErrTime.setStatus("mandatory")
_Sensor1lastErrMsg_Type = DisplayString
_Sensor1lastErrMsg_Object = MibScalar
sensor1lastErrMsg = _Sensor1lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 1, 5),
    _Sensor1lastErrMsg_Type()
)
sensor1lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor1lastErrMsg.setStatus("mandatory")
_Sensor2_ObjectIdentity = ObjectIdentity
sensor2 = _Sensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 2)
)
_Sensor2Name_Type = DisplayString
_Sensor2Name_Object = MibScalar
sensor2Name = _Sensor2Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 2, 1),
    _Sensor2Name_Type()
)
sensor2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2Name.setStatus("mandatory")
_Sensor2value_Type = DisplayString
_Sensor2value_Object = MibScalar
sensor2value = _Sensor2value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 2, 2),
    _Sensor2value_Type()
)
sensor2value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2value.setStatus("mandatory")
_Sensor2ErrState_Type = DisplayString
_Sensor2ErrState_Object = MibScalar
sensor2ErrState = _Sensor2ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 2, 3),
    _Sensor2ErrState_Type()
)
sensor2ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2ErrState.setStatus("mandatory")
_Sensor2lastErrTime_Type = DisplayString
_Sensor2lastErrTime_Object = MibScalar
sensor2lastErrTime = _Sensor2lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 2, 4),
    _Sensor2lastErrTime_Type()
)
sensor2lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2lastErrTime.setStatus("mandatory")
_Sensor2lastErrMsg_Type = DisplayString
_Sensor2lastErrMsg_Object = MibScalar
sensor2lastErrMsg = _Sensor2lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 2, 5),
    _Sensor2lastErrMsg_Type()
)
sensor2lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor2lastErrMsg.setStatus("mandatory")
_Sensor3_ObjectIdentity = ObjectIdentity
sensor3 = _Sensor3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 3)
)
_Sensor3Name_Type = DisplayString
_Sensor3Name_Object = MibScalar
sensor3Name = _Sensor3Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 3, 1),
    _Sensor3Name_Type()
)
sensor3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3Name.setStatus("mandatory")
_Sensor3value_Type = DisplayString
_Sensor3value_Object = MibScalar
sensor3value = _Sensor3value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 3, 2),
    _Sensor3value_Type()
)
sensor3value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3value.setStatus("mandatory")
_Sensor3ErrState_Type = DisplayString
_Sensor3ErrState_Object = MibScalar
sensor3ErrState = _Sensor3ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 3, 3),
    _Sensor3ErrState_Type()
)
sensor3ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3ErrState.setStatus("mandatory")
_Sensor3lastErrTime_Type = DisplayString
_Sensor3lastErrTime_Object = MibScalar
sensor3lastErrTime = _Sensor3lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 3, 4),
    _Sensor3lastErrTime_Type()
)
sensor3lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3lastErrTime.setStatus("mandatory")
_Sensor3lastErrMsg_Type = DisplayString
_Sensor3lastErrMsg_Object = MibScalar
sensor3lastErrMsg = _Sensor3lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 3, 5),
    _Sensor3lastErrMsg_Type()
)
sensor3lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor3lastErrMsg.setStatus("mandatory")
_Sensor4_ObjectIdentity = ObjectIdentity
sensor4 = _Sensor4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 4)
)
_Sensor4Name_Type = DisplayString
_Sensor4Name_Object = MibScalar
sensor4Name = _Sensor4Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 4, 1),
    _Sensor4Name_Type()
)
sensor4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4Name.setStatus("mandatory")
_Sensor4value_Type = DisplayString
_Sensor4value_Object = MibScalar
sensor4value = _Sensor4value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 4, 2),
    _Sensor4value_Type()
)
sensor4value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4value.setStatus("mandatory")
_Sensor4ErrState_Type = DisplayString
_Sensor4ErrState_Object = MibScalar
sensor4ErrState = _Sensor4ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 4, 3),
    _Sensor4ErrState_Type()
)
sensor4ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4ErrState.setStatus("mandatory")
_Sensor4lastErrTime_Type = DisplayString
_Sensor4lastErrTime_Object = MibScalar
sensor4lastErrTime = _Sensor4lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 4, 4),
    _Sensor4lastErrTime_Type()
)
sensor4lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4lastErrTime.setStatus("mandatory")
_Sensor4lastErrMsg_Type = DisplayString
_Sensor4lastErrMsg_Object = MibScalar
sensor4lastErrMsg = _Sensor4lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 4, 5),
    _Sensor4lastErrMsg_Type()
)
sensor4lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor4lastErrMsg.setStatus("mandatory")
_Sensor5_ObjectIdentity = ObjectIdentity
sensor5 = _Sensor5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 5)
)
_Sensor5Name_Type = DisplayString
_Sensor5Name_Object = MibScalar
sensor5Name = _Sensor5Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 5, 1),
    _Sensor5Name_Type()
)
sensor5Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5Name.setStatus("mandatory")
_Sensor5value_Type = DisplayString
_Sensor5value_Object = MibScalar
sensor5value = _Sensor5value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 5, 2),
    _Sensor5value_Type()
)
sensor5value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5value.setStatus("mandatory")
_Sensor5ErrState_Type = DisplayString
_Sensor5ErrState_Object = MibScalar
sensor5ErrState = _Sensor5ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 5, 3),
    _Sensor5ErrState_Type()
)
sensor5ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5ErrState.setStatus("mandatory")
_Sensor5lastErrTime_Type = DisplayString
_Sensor5lastErrTime_Object = MibScalar
sensor5lastErrTime = _Sensor5lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 5, 4),
    _Sensor5lastErrTime_Type()
)
sensor5lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5lastErrTime.setStatus("mandatory")
_Sensor5lastErrMsg_Type = DisplayString
_Sensor5lastErrMsg_Object = MibScalar
sensor5lastErrMsg = _Sensor5lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 5, 5),
    _Sensor5lastErrMsg_Type()
)
sensor5lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor5lastErrMsg.setStatus("mandatory")
_Sensor6_ObjectIdentity = ObjectIdentity
sensor6 = _Sensor6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 6)
)
_Sensor6Name_Type = DisplayString
_Sensor6Name_Object = MibScalar
sensor6Name = _Sensor6Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 6, 1),
    _Sensor6Name_Type()
)
sensor6Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6Name.setStatus("mandatory")
_Sensor6value_Type = DisplayString
_Sensor6value_Object = MibScalar
sensor6value = _Sensor6value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 6, 2),
    _Sensor6value_Type()
)
sensor6value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6value.setStatus("mandatory")
_Sensor6ErrState_Type = DisplayString
_Sensor6ErrState_Object = MibScalar
sensor6ErrState = _Sensor6ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 6, 3),
    _Sensor6ErrState_Type()
)
sensor6ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6ErrState.setStatus("mandatory")
_Sensor6lastErrTime_Type = DisplayString
_Sensor6lastErrTime_Object = MibScalar
sensor6lastErrTime = _Sensor6lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 6, 4),
    _Sensor6lastErrTime_Type()
)
sensor6lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6lastErrTime.setStatus("mandatory")
_Sensor6lastErrMsg_Type = DisplayString
_Sensor6lastErrMsg_Object = MibScalar
sensor6lastErrMsg = _Sensor6lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 6, 5),
    _Sensor6lastErrMsg_Type()
)
sensor6lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor6lastErrMsg.setStatus("mandatory")
_Sensor7_ObjectIdentity = ObjectIdentity
sensor7 = _Sensor7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 7)
)
_Sensor7Name_Type = DisplayString
_Sensor7Name_Object = MibScalar
sensor7Name = _Sensor7Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 7, 1),
    _Sensor7Name_Type()
)
sensor7Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7Name.setStatus("mandatory")
_Sensor7value_Type = DisplayString
_Sensor7value_Object = MibScalar
sensor7value = _Sensor7value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 7, 2),
    _Sensor7value_Type()
)
sensor7value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7value.setStatus("mandatory")
_Sensor7ErrState_Type = DisplayString
_Sensor7ErrState_Object = MibScalar
sensor7ErrState = _Sensor7ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 7, 3),
    _Sensor7ErrState_Type()
)
sensor7ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7ErrState.setStatus("mandatory")
_Sensor7lastErrTime_Type = DisplayString
_Sensor7lastErrTime_Object = MibScalar
sensor7lastErrTime = _Sensor7lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 7, 4),
    _Sensor7lastErrTime_Type()
)
sensor7lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7lastErrTime.setStatus("mandatory")
_Sensor7lastErrMsg_Type = DisplayString
_Sensor7lastErrMsg_Object = MibScalar
sensor7lastErrMsg = _Sensor7lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 7, 5),
    _Sensor7lastErrMsg_Type()
)
sensor7lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor7lastErrMsg.setStatus("mandatory")
_Sensor8_ObjectIdentity = ObjectIdentity
sensor8 = _Sensor8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 8)
)
_Sensor8Name_Type = DisplayString
_Sensor8Name_Object = MibScalar
sensor8Name = _Sensor8Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 8, 1),
    _Sensor8Name_Type()
)
sensor8Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8Name.setStatus("mandatory")
_Sensor8value_Type = DisplayString
_Sensor8value_Object = MibScalar
sensor8value = _Sensor8value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 8, 2),
    _Sensor8value_Type()
)
sensor8value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8value.setStatus("mandatory")
_Sensor8ErrState_Type = DisplayString
_Sensor8ErrState_Object = MibScalar
sensor8ErrState = _Sensor8ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 8, 3),
    _Sensor8ErrState_Type()
)
sensor8ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8ErrState.setStatus("mandatory")
_Sensor8lastErrTime_Type = DisplayString
_Sensor8lastErrTime_Object = MibScalar
sensor8lastErrTime = _Sensor8lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 8, 4),
    _Sensor8lastErrTime_Type()
)
sensor8lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8lastErrTime.setStatus("mandatory")
_Sensor8lastErrMsg_Type = DisplayString
_Sensor8lastErrMsg_Object = MibScalar
sensor8lastErrMsg = _Sensor8lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 8, 5),
    _Sensor8lastErrMsg_Type()
)
sensor8lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor8lastErrMsg.setStatus("mandatory")
_Sensor9_ObjectIdentity = ObjectIdentity
sensor9 = _Sensor9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 9)
)
_Sensor9Name_Type = DisplayString
_Sensor9Name_Object = MibScalar
sensor9Name = _Sensor9Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 9, 1),
    _Sensor9Name_Type()
)
sensor9Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor9Name.setStatus("mandatory")
_Sensor9value_Type = DisplayString
_Sensor9value_Object = MibScalar
sensor9value = _Sensor9value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 9, 2),
    _Sensor9value_Type()
)
sensor9value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor9value.setStatus("mandatory")
_Sensor9ErrState_Type = DisplayString
_Sensor9ErrState_Object = MibScalar
sensor9ErrState = _Sensor9ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 9, 3),
    _Sensor9ErrState_Type()
)
sensor9ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor9ErrState.setStatus("mandatory")
_Sensor9lastErrTime_Type = DisplayString
_Sensor9lastErrTime_Object = MibScalar
sensor9lastErrTime = _Sensor9lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 9, 4),
    _Sensor9lastErrTime_Type()
)
sensor9lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor9lastErrTime.setStatus("mandatory")
_Sensor9lastErrMsg_Type = DisplayString
_Sensor9lastErrMsg_Object = MibScalar
sensor9lastErrMsg = _Sensor9lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 9, 5),
    _Sensor9lastErrMsg_Type()
)
sensor9lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor9lastErrMsg.setStatus("mandatory")
_Sensor10_ObjectIdentity = ObjectIdentity
sensor10 = _Sensor10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 10)
)
_Sensor10Name_Type = DisplayString
_Sensor10Name_Object = MibScalar
sensor10Name = _Sensor10Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 10, 1),
    _Sensor10Name_Type()
)
sensor10Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor10Name.setStatus("mandatory")
_Sensor10value_Type = DisplayString
_Sensor10value_Object = MibScalar
sensor10value = _Sensor10value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 10, 2),
    _Sensor10value_Type()
)
sensor10value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor10value.setStatus("mandatory")
_Sensor10ErrState_Type = DisplayString
_Sensor10ErrState_Object = MibScalar
sensor10ErrState = _Sensor10ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 10, 3),
    _Sensor10ErrState_Type()
)
sensor10ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor10ErrState.setStatus("mandatory")
_Sensor10lastErrTime_Type = DisplayString
_Sensor10lastErrTime_Object = MibScalar
sensor10lastErrTime = _Sensor10lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 10, 4),
    _Sensor10lastErrTime_Type()
)
sensor10lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor10lastErrTime.setStatus("mandatory")
_Sensor10lastErrMsg_Type = DisplayString
_Sensor10lastErrMsg_Object = MibScalar
sensor10lastErrMsg = _Sensor10lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 10, 5),
    _Sensor10lastErrMsg_Type()
)
sensor10lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor10lastErrMsg.setStatus("mandatory")
_Sensor11_ObjectIdentity = ObjectIdentity
sensor11 = _Sensor11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 11)
)
_Sensor11Name_Type = DisplayString
_Sensor11Name_Object = MibScalar
sensor11Name = _Sensor11Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 11, 1),
    _Sensor11Name_Type()
)
sensor11Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor11Name.setStatus("mandatory")
_Sensor11value_Type = DisplayString
_Sensor11value_Object = MibScalar
sensor11value = _Sensor11value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 11, 2),
    _Sensor11value_Type()
)
sensor11value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor11value.setStatus("mandatory")
_Sensor11ErrState_Type = DisplayString
_Sensor11ErrState_Object = MibScalar
sensor11ErrState = _Sensor11ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 11, 3),
    _Sensor11ErrState_Type()
)
sensor11ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor11ErrState.setStatus("mandatory")
_Sensor11lastErrTime_Type = DisplayString
_Sensor11lastErrTime_Object = MibScalar
sensor11lastErrTime = _Sensor11lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 11, 4),
    _Sensor11lastErrTime_Type()
)
sensor11lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor11lastErrTime.setStatus("mandatory")
_Sensor11lastErrMsg_Type = DisplayString
_Sensor11lastErrMsg_Object = MibScalar
sensor11lastErrMsg = _Sensor11lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 11, 5),
    _Sensor11lastErrMsg_Type()
)
sensor11lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor11lastErrMsg.setStatus("mandatory")
_Sensor12_ObjectIdentity = ObjectIdentity
sensor12 = _Sensor12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 12)
)
_Sensor12Name_Type = DisplayString
_Sensor12Name_Object = MibScalar
sensor12Name = _Sensor12Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 12, 1),
    _Sensor12Name_Type()
)
sensor12Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor12Name.setStatus("mandatory")
_Sensor12value_Type = DisplayString
_Sensor12value_Object = MibScalar
sensor12value = _Sensor12value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 12, 2),
    _Sensor12value_Type()
)
sensor12value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor12value.setStatus("mandatory")
_Sensor12ErrState_Type = DisplayString
_Sensor12ErrState_Object = MibScalar
sensor12ErrState = _Sensor12ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 12, 3),
    _Sensor12ErrState_Type()
)
sensor12ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor12ErrState.setStatus("mandatory")
_Sensor12lastErrTime_Type = DisplayString
_Sensor12lastErrTime_Object = MibScalar
sensor12lastErrTime = _Sensor12lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 12, 4),
    _Sensor12lastErrTime_Type()
)
sensor12lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor12lastErrTime.setStatus("mandatory")
_Sensor12lastErrMsg_Type = DisplayString
_Sensor12lastErrMsg_Object = MibScalar
sensor12lastErrMsg = _Sensor12lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 12, 5),
    _Sensor12lastErrMsg_Type()
)
sensor12lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor12lastErrMsg.setStatus("mandatory")
_Sensor13_ObjectIdentity = ObjectIdentity
sensor13 = _Sensor13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 13)
)
_Sensor13Name_Type = DisplayString
_Sensor13Name_Object = MibScalar
sensor13Name = _Sensor13Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 13, 1),
    _Sensor13Name_Type()
)
sensor13Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor13Name.setStatus("mandatory")
_Sensor13value_Type = DisplayString
_Sensor13value_Object = MibScalar
sensor13value = _Sensor13value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 13, 2),
    _Sensor13value_Type()
)
sensor13value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor13value.setStatus("mandatory")
_Sensor13ErrState_Type = DisplayString
_Sensor13ErrState_Object = MibScalar
sensor13ErrState = _Sensor13ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 13, 3),
    _Sensor13ErrState_Type()
)
sensor13ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor13ErrState.setStatus("mandatory")
_Sensor13lastErrTime_Type = DisplayString
_Sensor13lastErrTime_Object = MibScalar
sensor13lastErrTime = _Sensor13lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 13, 4),
    _Sensor13lastErrTime_Type()
)
sensor13lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor13lastErrTime.setStatus("mandatory")
_Sensor13lastErrMsg_Type = DisplayString
_Sensor13lastErrMsg_Object = MibScalar
sensor13lastErrMsg = _Sensor13lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 13, 5),
    _Sensor13lastErrMsg_Type()
)
sensor13lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor13lastErrMsg.setStatus("mandatory")
_Sensor14_ObjectIdentity = ObjectIdentity
sensor14 = _Sensor14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 14)
)
_Sensor14Name_Type = DisplayString
_Sensor14Name_Object = MibScalar
sensor14Name = _Sensor14Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 14, 1),
    _Sensor14Name_Type()
)
sensor14Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor14Name.setStatus("mandatory")
_Sensor14value_Type = DisplayString
_Sensor14value_Object = MibScalar
sensor14value = _Sensor14value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 14, 2),
    _Sensor14value_Type()
)
sensor14value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor14value.setStatus("mandatory")
_Sensor14ErrState_Type = DisplayString
_Sensor14ErrState_Object = MibScalar
sensor14ErrState = _Sensor14ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 14, 3),
    _Sensor14ErrState_Type()
)
sensor14ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor14ErrState.setStatus("mandatory")
_Sensor14lastErrTime_Type = DisplayString
_Sensor14lastErrTime_Object = MibScalar
sensor14lastErrTime = _Sensor14lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 14, 4),
    _Sensor14lastErrTime_Type()
)
sensor14lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor14lastErrTime.setStatus("mandatory")
_Sensor14lastErrMsg_Type = DisplayString
_Sensor14lastErrMsg_Object = MibScalar
sensor14lastErrMsg = _Sensor14lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 14, 5),
    _Sensor14lastErrMsg_Type()
)
sensor14lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor14lastErrMsg.setStatus("mandatory")
_Sensor15_ObjectIdentity = ObjectIdentity
sensor15 = _Sensor15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 15)
)
_Sensor15Name_Type = DisplayString
_Sensor15Name_Object = MibScalar
sensor15Name = _Sensor15Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 15, 1),
    _Sensor15Name_Type()
)
sensor15Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor15Name.setStatus("mandatory")
_Sensor15value_Type = DisplayString
_Sensor15value_Object = MibScalar
sensor15value = _Sensor15value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 15, 2),
    _Sensor15value_Type()
)
sensor15value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor15value.setStatus("mandatory")
_Sensor15ErrState_Type = DisplayString
_Sensor15ErrState_Object = MibScalar
sensor15ErrState = _Sensor15ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 15, 3),
    _Sensor15ErrState_Type()
)
sensor15ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor15ErrState.setStatus("mandatory")
_Sensor15lastErrTime_Type = DisplayString
_Sensor15lastErrTime_Object = MibScalar
sensor15lastErrTime = _Sensor15lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 15, 4),
    _Sensor15lastErrTime_Type()
)
sensor15lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor15lastErrTime.setStatus("mandatory")
_Sensor15lastErrMsg_Type = DisplayString
_Sensor15lastErrMsg_Object = MibScalar
sensor15lastErrMsg = _Sensor15lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 15, 5),
    _Sensor15lastErrMsg_Type()
)
sensor15lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor15lastErrMsg.setStatus("mandatory")
_Sensor16_ObjectIdentity = ObjectIdentity
sensor16 = _Sensor16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 16)
)
_Sensor16Name_Type = DisplayString
_Sensor16Name_Object = MibScalar
sensor16Name = _Sensor16Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 16, 1),
    _Sensor16Name_Type()
)
sensor16Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor16Name.setStatus("mandatory")
_Sensor16value_Type = DisplayString
_Sensor16value_Object = MibScalar
sensor16value = _Sensor16value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 16, 2),
    _Sensor16value_Type()
)
sensor16value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor16value.setStatus("mandatory")
_Sensor16ErrState_Type = DisplayString
_Sensor16ErrState_Object = MibScalar
sensor16ErrState = _Sensor16ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 16, 3),
    _Sensor16ErrState_Type()
)
sensor16ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor16ErrState.setStatus("mandatory")
_Sensor16lastErrTime_Type = DisplayString
_Sensor16lastErrTime_Object = MibScalar
sensor16lastErrTime = _Sensor16lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 16, 4),
    _Sensor16lastErrTime_Type()
)
sensor16lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor16lastErrTime.setStatus("mandatory")
_Sensor16lastErrMsg_Type = DisplayString
_Sensor16lastErrMsg_Object = MibScalar
sensor16lastErrMsg = _Sensor16lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 16, 5),
    _Sensor16lastErrMsg_Type()
)
sensor16lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor16lastErrMsg.setStatus("mandatory")
_Sensor17_ObjectIdentity = ObjectIdentity
sensor17 = _Sensor17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 17)
)
_Sensor17Name_Type = DisplayString
_Sensor17Name_Object = MibScalar
sensor17Name = _Sensor17Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 17, 1),
    _Sensor17Name_Type()
)
sensor17Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor17Name.setStatus("mandatory")
_Sensor17value_Type = DisplayString
_Sensor17value_Object = MibScalar
sensor17value = _Sensor17value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 17, 2),
    _Sensor17value_Type()
)
sensor17value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor17value.setStatus("mandatory")
_Sensor17ErrState_Type = DisplayString
_Sensor17ErrState_Object = MibScalar
sensor17ErrState = _Sensor17ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 17, 3),
    _Sensor17ErrState_Type()
)
sensor17ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor17ErrState.setStatus("mandatory")
_Sensor17lastErrTime_Type = DisplayString
_Sensor17lastErrTime_Object = MibScalar
sensor17lastErrTime = _Sensor17lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 17, 4),
    _Sensor17lastErrTime_Type()
)
sensor17lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor17lastErrTime.setStatus("mandatory")
_Sensor17lastErrMsg_Type = DisplayString
_Sensor17lastErrMsg_Object = MibScalar
sensor17lastErrMsg = _Sensor17lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 17, 5),
    _Sensor17lastErrMsg_Type()
)
sensor17lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor17lastErrMsg.setStatus("mandatory")
_Sensor18_ObjectIdentity = ObjectIdentity
sensor18 = _Sensor18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 18)
)
_Sensor18Name_Type = DisplayString
_Sensor18Name_Object = MibScalar
sensor18Name = _Sensor18Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 18, 1),
    _Sensor18Name_Type()
)
sensor18Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor18Name.setStatus("mandatory")
_Sensor18value_Type = DisplayString
_Sensor18value_Object = MibScalar
sensor18value = _Sensor18value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 18, 2),
    _Sensor18value_Type()
)
sensor18value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor18value.setStatus("mandatory")
_Sensor18ErrState_Type = DisplayString
_Sensor18ErrState_Object = MibScalar
sensor18ErrState = _Sensor18ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 18, 3),
    _Sensor18ErrState_Type()
)
sensor18ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor18ErrState.setStatus("mandatory")
_Sensor18lastErrTime_Type = DisplayString
_Sensor18lastErrTime_Object = MibScalar
sensor18lastErrTime = _Sensor18lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 18, 4),
    _Sensor18lastErrTime_Type()
)
sensor18lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor18lastErrTime.setStatus("mandatory")
_Sensor18lastErrMsg_Type = DisplayString
_Sensor18lastErrMsg_Object = MibScalar
sensor18lastErrMsg = _Sensor18lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 18, 5),
    _Sensor18lastErrMsg_Type()
)
sensor18lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor18lastErrMsg.setStatus("mandatory")
_Sensor19_ObjectIdentity = ObjectIdentity
sensor19 = _Sensor19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 19)
)
_Sensor19Name_Type = DisplayString
_Sensor19Name_Object = MibScalar
sensor19Name = _Sensor19Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 19, 1),
    _Sensor19Name_Type()
)
sensor19Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor19Name.setStatus("mandatory")
_Sensor19value_Type = DisplayString
_Sensor19value_Object = MibScalar
sensor19value = _Sensor19value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 19, 2),
    _Sensor19value_Type()
)
sensor19value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor19value.setStatus("mandatory")
_Sensor19ErrState_Type = DisplayString
_Sensor19ErrState_Object = MibScalar
sensor19ErrState = _Sensor19ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 19, 3),
    _Sensor19ErrState_Type()
)
sensor19ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor19ErrState.setStatus("mandatory")
_Sensor19lastErrTime_Type = DisplayString
_Sensor19lastErrTime_Object = MibScalar
sensor19lastErrTime = _Sensor19lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 19, 4),
    _Sensor19lastErrTime_Type()
)
sensor19lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor19lastErrTime.setStatus("mandatory")
_Sensor19lastErrMsg_Type = DisplayString
_Sensor19lastErrMsg_Object = MibScalar
sensor19lastErrMsg = _Sensor19lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 19, 5),
    _Sensor19lastErrMsg_Type()
)
sensor19lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor19lastErrMsg.setStatus("mandatory")
_Sensor20_ObjectIdentity = ObjectIdentity
sensor20 = _Sensor20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 20)
)
_Sensor20Name_Type = DisplayString
_Sensor20Name_Object = MibScalar
sensor20Name = _Sensor20Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 20, 1),
    _Sensor20Name_Type()
)
sensor20Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor20Name.setStatus("mandatory")
_Sensor20value_Type = DisplayString
_Sensor20value_Object = MibScalar
sensor20value = _Sensor20value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 20, 2),
    _Sensor20value_Type()
)
sensor20value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor20value.setStatus("mandatory")
_Sensor20ErrState_Type = DisplayString
_Sensor20ErrState_Object = MibScalar
sensor20ErrState = _Sensor20ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 20, 3),
    _Sensor20ErrState_Type()
)
sensor20ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor20ErrState.setStatus("mandatory")
_Sensor20lastErrTime_Type = DisplayString
_Sensor20lastErrTime_Object = MibScalar
sensor20lastErrTime = _Sensor20lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 20, 4),
    _Sensor20lastErrTime_Type()
)
sensor20lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor20lastErrTime.setStatus("mandatory")
_Sensor20lastErrMsg_Type = DisplayString
_Sensor20lastErrMsg_Object = MibScalar
sensor20lastErrMsg = _Sensor20lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 20, 5),
    _Sensor20lastErrMsg_Type()
)
sensor20lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor20lastErrMsg.setStatus("mandatory")
_Sensor21_ObjectIdentity = ObjectIdentity
sensor21 = _Sensor21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 21)
)
_Sensor21Name_Type = DisplayString
_Sensor21Name_Object = MibScalar
sensor21Name = _Sensor21Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 21, 1),
    _Sensor21Name_Type()
)
sensor21Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor21Name.setStatus("mandatory")
_Sensor21value_Type = DisplayString
_Sensor21value_Object = MibScalar
sensor21value = _Sensor21value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 21, 2),
    _Sensor21value_Type()
)
sensor21value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor21value.setStatus("mandatory")
_Sensor21ErrState_Type = DisplayString
_Sensor21ErrState_Object = MibScalar
sensor21ErrState = _Sensor21ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 21, 3),
    _Sensor21ErrState_Type()
)
sensor21ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor21ErrState.setStatus("mandatory")
_Sensor21lastErrTime_Type = DisplayString
_Sensor21lastErrTime_Object = MibScalar
sensor21lastErrTime = _Sensor21lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 21, 4),
    _Sensor21lastErrTime_Type()
)
sensor21lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor21lastErrTime.setStatus("mandatory")
_Sensor21lastErrMsg_Type = DisplayString
_Sensor21lastErrMsg_Object = MibScalar
sensor21lastErrMsg = _Sensor21lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 21, 5),
    _Sensor21lastErrMsg_Type()
)
sensor21lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor21lastErrMsg.setStatus("mandatory")
_Sensor22_ObjectIdentity = ObjectIdentity
sensor22 = _Sensor22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 22)
)
_Sensor22Name_Type = DisplayString
_Sensor22Name_Object = MibScalar
sensor22Name = _Sensor22Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 22, 1),
    _Sensor22Name_Type()
)
sensor22Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor22Name.setStatus("mandatory")
_Sensor22value_Type = DisplayString
_Sensor22value_Object = MibScalar
sensor22value = _Sensor22value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 22, 2),
    _Sensor22value_Type()
)
sensor22value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor22value.setStatus("mandatory")
_Sensor22ErrState_Type = DisplayString
_Sensor22ErrState_Object = MibScalar
sensor22ErrState = _Sensor22ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 22, 3),
    _Sensor22ErrState_Type()
)
sensor22ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor22ErrState.setStatus("mandatory")
_Sensor22lastErrTime_Type = DisplayString
_Sensor22lastErrTime_Object = MibScalar
sensor22lastErrTime = _Sensor22lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 22, 4),
    _Sensor22lastErrTime_Type()
)
sensor22lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor22lastErrTime.setStatus("mandatory")
_Sensor22lastErrMsg_Type = DisplayString
_Sensor22lastErrMsg_Object = MibScalar
sensor22lastErrMsg = _Sensor22lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 22, 5),
    _Sensor22lastErrMsg_Type()
)
sensor22lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor22lastErrMsg.setStatus("mandatory")
_Sensor23_ObjectIdentity = ObjectIdentity
sensor23 = _Sensor23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 23)
)
_Sensor23Name_Type = DisplayString
_Sensor23Name_Object = MibScalar
sensor23Name = _Sensor23Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 23, 1),
    _Sensor23Name_Type()
)
sensor23Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor23Name.setStatus("mandatory")
_Sensor23value_Type = DisplayString
_Sensor23value_Object = MibScalar
sensor23value = _Sensor23value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 23, 2),
    _Sensor23value_Type()
)
sensor23value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor23value.setStatus("mandatory")
_Sensor23ErrState_Type = DisplayString
_Sensor23ErrState_Object = MibScalar
sensor23ErrState = _Sensor23ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 23, 3),
    _Sensor23ErrState_Type()
)
sensor23ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor23ErrState.setStatus("mandatory")
_Sensor23lastErrTime_Type = DisplayString
_Sensor23lastErrTime_Object = MibScalar
sensor23lastErrTime = _Sensor23lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 23, 4),
    _Sensor23lastErrTime_Type()
)
sensor23lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor23lastErrTime.setStatus("mandatory")
_Sensor23lastErrMsg_Type = DisplayString
_Sensor23lastErrMsg_Object = MibScalar
sensor23lastErrMsg = _Sensor23lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 23, 5),
    _Sensor23lastErrMsg_Type()
)
sensor23lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor23lastErrMsg.setStatus("mandatory")
_Sensor24_ObjectIdentity = ObjectIdentity
sensor24 = _Sensor24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 24)
)
_Sensor24Name_Type = DisplayString
_Sensor24Name_Object = MibScalar
sensor24Name = _Sensor24Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 24, 1),
    _Sensor24Name_Type()
)
sensor24Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor24Name.setStatus("mandatory")
_Sensor24value_Type = DisplayString
_Sensor24value_Object = MibScalar
sensor24value = _Sensor24value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 24, 2),
    _Sensor24value_Type()
)
sensor24value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor24value.setStatus("mandatory")
_Sensor24ErrState_Type = DisplayString
_Sensor24ErrState_Object = MibScalar
sensor24ErrState = _Sensor24ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 24, 3),
    _Sensor24ErrState_Type()
)
sensor24ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor24ErrState.setStatus("mandatory")
_Sensor24lastErrTime_Type = DisplayString
_Sensor24lastErrTime_Object = MibScalar
sensor24lastErrTime = _Sensor24lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 24, 4),
    _Sensor24lastErrTime_Type()
)
sensor24lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor24lastErrTime.setStatus("mandatory")
_Sensor24lastErrMsg_Type = DisplayString
_Sensor24lastErrMsg_Object = MibScalar
sensor24lastErrMsg = _Sensor24lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 24, 5),
    _Sensor24lastErrMsg_Type()
)
sensor24lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor24lastErrMsg.setStatus("mandatory")
_Sensor25_ObjectIdentity = ObjectIdentity
sensor25 = _Sensor25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 25)
)
_Sensor25Name_Type = DisplayString
_Sensor25Name_Object = MibScalar
sensor25Name = _Sensor25Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 25, 1),
    _Sensor25Name_Type()
)
sensor25Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor25Name.setStatus("mandatory")
_Sensor25value_Type = DisplayString
_Sensor25value_Object = MibScalar
sensor25value = _Sensor25value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 25, 2),
    _Sensor25value_Type()
)
sensor25value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor25value.setStatus("mandatory")
_Sensor25ErrState_Type = DisplayString
_Sensor25ErrState_Object = MibScalar
sensor25ErrState = _Sensor25ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 25, 3),
    _Sensor25ErrState_Type()
)
sensor25ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor25ErrState.setStatus("mandatory")
_Sensor25lastErrTime_Type = DisplayString
_Sensor25lastErrTime_Object = MibScalar
sensor25lastErrTime = _Sensor25lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 25, 4),
    _Sensor25lastErrTime_Type()
)
sensor25lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor25lastErrTime.setStatus("mandatory")
_Sensor25lastErrMsg_Type = DisplayString
_Sensor25lastErrMsg_Object = MibScalar
sensor25lastErrMsg = _Sensor25lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 25, 5),
    _Sensor25lastErrMsg_Type()
)
sensor25lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor25lastErrMsg.setStatus("mandatory")
_Sensor26_ObjectIdentity = ObjectIdentity
sensor26 = _Sensor26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 26)
)
_Sensor26Name_Type = DisplayString
_Sensor26Name_Object = MibScalar
sensor26Name = _Sensor26Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 26, 1),
    _Sensor26Name_Type()
)
sensor26Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor26Name.setStatus("mandatory")
_Sensor26value_Type = DisplayString
_Sensor26value_Object = MibScalar
sensor26value = _Sensor26value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 26, 2),
    _Sensor26value_Type()
)
sensor26value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor26value.setStatus("mandatory")
_Sensor26ErrState_Type = DisplayString
_Sensor26ErrState_Object = MibScalar
sensor26ErrState = _Sensor26ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 26, 3),
    _Sensor26ErrState_Type()
)
sensor26ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor26ErrState.setStatus("mandatory")
_Sensor26lastErrTime_Type = DisplayString
_Sensor26lastErrTime_Object = MibScalar
sensor26lastErrTime = _Sensor26lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 26, 4),
    _Sensor26lastErrTime_Type()
)
sensor26lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor26lastErrTime.setStatus("mandatory")
_Sensor26lastErrMsg_Type = DisplayString
_Sensor26lastErrMsg_Object = MibScalar
sensor26lastErrMsg = _Sensor26lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 26, 5),
    _Sensor26lastErrMsg_Type()
)
sensor26lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor26lastErrMsg.setStatus("mandatory")
_Sensor27_ObjectIdentity = ObjectIdentity
sensor27 = _Sensor27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 27)
)
_Sensor27Name_Type = DisplayString
_Sensor27Name_Object = MibScalar
sensor27Name = _Sensor27Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 27, 1),
    _Sensor27Name_Type()
)
sensor27Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor27Name.setStatus("mandatory")
_Sensor27value_Type = DisplayString
_Sensor27value_Object = MibScalar
sensor27value = _Sensor27value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 27, 2),
    _Sensor27value_Type()
)
sensor27value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor27value.setStatus("mandatory")
_Sensor27ErrState_Type = DisplayString
_Sensor27ErrState_Object = MibScalar
sensor27ErrState = _Sensor27ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 27, 3),
    _Sensor27ErrState_Type()
)
sensor27ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor27ErrState.setStatus("mandatory")
_Sensor27lastErrTime_Type = DisplayString
_Sensor27lastErrTime_Object = MibScalar
sensor27lastErrTime = _Sensor27lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 27, 4),
    _Sensor27lastErrTime_Type()
)
sensor27lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor27lastErrTime.setStatus("mandatory")
_Sensor27lastErrMsg_Type = DisplayString
_Sensor27lastErrMsg_Object = MibScalar
sensor27lastErrMsg = _Sensor27lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 27, 5),
    _Sensor27lastErrMsg_Type()
)
sensor27lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor27lastErrMsg.setStatus("mandatory")
_Sensor28_ObjectIdentity = ObjectIdentity
sensor28 = _Sensor28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 28)
)
_Sensor28Name_Type = DisplayString
_Sensor28Name_Object = MibScalar
sensor28Name = _Sensor28Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 28, 1),
    _Sensor28Name_Type()
)
sensor28Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor28Name.setStatus("mandatory")
_Sensor28value_Type = DisplayString
_Sensor28value_Object = MibScalar
sensor28value = _Sensor28value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 28, 2),
    _Sensor28value_Type()
)
sensor28value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor28value.setStatus("mandatory")
_Sensor28ErrState_Type = DisplayString
_Sensor28ErrState_Object = MibScalar
sensor28ErrState = _Sensor28ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 28, 3),
    _Sensor28ErrState_Type()
)
sensor28ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor28ErrState.setStatus("mandatory")
_Sensor28lastErrTime_Type = DisplayString
_Sensor28lastErrTime_Object = MibScalar
sensor28lastErrTime = _Sensor28lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 28, 4),
    _Sensor28lastErrTime_Type()
)
sensor28lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor28lastErrTime.setStatus("mandatory")
_Sensor28lastErrMsg_Type = DisplayString
_Sensor28lastErrMsg_Object = MibScalar
sensor28lastErrMsg = _Sensor28lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 28, 5),
    _Sensor28lastErrMsg_Type()
)
sensor28lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor28lastErrMsg.setStatus("mandatory")
_Sensor29_ObjectIdentity = ObjectIdentity
sensor29 = _Sensor29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 29)
)
_Sensor29Name_Type = DisplayString
_Sensor29Name_Object = MibScalar
sensor29Name = _Sensor29Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 29, 1),
    _Sensor29Name_Type()
)
sensor29Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor29Name.setStatus("mandatory")
_Sensor29value_Type = DisplayString
_Sensor29value_Object = MibScalar
sensor29value = _Sensor29value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 29, 2),
    _Sensor29value_Type()
)
sensor29value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor29value.setStatus("mandatory")
_Sensor29ErrState_Type = DisplayString
_Sensor29ErrState_Object = MibScalar
sensor29ErrState = _Sensor29ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 29, 3),
    _Sensor29ErrState_Type()
)
sensor29ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor29ErrState.setStatus("mandatory")
_Sensor29lastErrTime_Type = DisplayString
_Sensor29lastErrTime_Object = MibScalar
sensor29lastErrTime = _Sensor29lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 29, 4),
    _Sensor29lastErrTime_Type()
)
sensor29lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor29lastErrTime.setStatus("mandatory")
_Sensor29lastErrMsg_Type = DisplayString
_Sensor29lastErrMsg_Object = MibScalar
sensor29lastErrMsg = _Sensor29lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 29, 5),
    _Sensor29lastErrMsg_Type()
)
sensor29lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor29lastErrMsg.setStatus("mandatory")
_Sensor30_ObjectIdentity = ObjectIdentity
sensor30 = _Sensor30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 30)
)
_Sensor30Name_Type = DisplayString
_Sensor30Name_Object = MibScalar
sensor30Name = _Sensor30Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 30, 1),
    _Sensor30Name_Type()
)
sensor30Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor30Name.setStatus("mandatory")
_Sensor30value_Type = DisplayString
_Sensor30value_Object = MibScalar
sensor30value = _Sensor30value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 30, 2),
    _Sensor30value_Type()
)
sensor30value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor30value.setStatus("mandatory")
_Sensor30ErrState_Type = DisplayString
_Sensor30ErrState_Object = MibScalar
sensor30ErrState = _Sensor30ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 30, 3),
    _Sensor30ErrState_Type()
)
sensor30ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor30ErrState.setStatus("mandatory")
_Sensor30lastErrTime_Type = DisplayString
_Sensor30lastErrTime_Object = MibScalar
sensor30lastErrTime = _Sensor30lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 30, 4),
    _Sensor30lastErrTime_Type()
)
sensor30lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor30lastErrTime.setStatus("mandatory")
_Sensor30lastErrMsg_Type = DisplayString
_Sensor30lastErrMsg_Object = MibScalar
sensor30lastErrMsg = _Sensor30lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 30, 5),
    _Sensor30lastErrMsg_Type()
)
sensor30lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor30lastErrMsg.setStatus("mandatory")
_Sensor31_ObjectIdentity = ObjectIdentity
sensor31 = _Sensor31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 31)
)
_Sensor31Name_Type = DisplayString
_Sensor31Name_Object = MibScalar
sensor31Name = _Sensor31Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 31, 1),
    _Sensor31Name_Type()
)
sensor31Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor31Name.setStatus("mandatory")
_Sensor31value_Type = DisplayString
_Sensor31value_Object = MibScalar
sensor31value = _Sensor31value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 31, 2),
    _Sensor31value_Type()
)
sensor31value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor31value.setStatus("mandatory")
_Sensor31ErrState_Type = DisplayString
_Sensor31ErrState_Object = MibScalar
sensor31ErrState = _Sensor31ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 31, 3),
    _Sensor31ErrState_Type()
)
sensor31ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor31ErrState.setStatus("mandatory")
_Sensor31lastErrTime_Type = DisplayString
_Sensor31lastErrTime_Object = MibScalar
sensor31lastErrTime = _Sensor31lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 31, 4),
    _Sensor31lastErrTime_Type()
)
sensor31lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor31lastErrTime.setStatus("mandatory")
_Sensor31lastErrMsg_Type = DisplayString
_Sensor31lastErrMsg_Object = MibScalar
sensor31lastErrMsg = _Sensor31lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 31, 5),
    _Sensor31lastErrMsg_Type()
)
sensor31lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor31lastErrMsg.setStatus("mandatory")
_Sensor32_ObjectIdentity = ObjectIdentity
sensor32 = _Sensor32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 11, 32)
)
_Sensor32Name_Type = DisplayString
_Sensor32Name_Object = MibScalar
sensor32Name = _Sensor32Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 32, 1),
    _Sensor32Name_Type()
)
sensor32Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor32Name.setStatus("mandatory")
_Sensor32value_Type = DisplayString
_Sensor32value_Object = MibScalar
sensor32value = _Sensor32value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 32, 2),
    _Sensor32value_Type()
)
sensor32value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor32value.setStatus("mandatory")
_Sensor32ErrState_Type = DisplayString
_Sensor32ErrState_Object = MibScalar
sensor32ErrState = _Sensor32ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 32, 3),
    _Sensor32ErrState_Type()
)
sensor32ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor32ErrState.setStatus("mandatory")
_Sensor32lastErrTime_Type = DisplayString
_Sensor32lastErrTime_Object = MibScalar
sensor32lastErrTime = _Sensor32lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 32, 4),
    _Sensor32lastErrTime_Type()
)
sensor32lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor32lastErrTime.setStatus("mandatory")
_Sensor32lastErrMsg_Type = DisplayString
_Sensor32lastErrMsg_Object = MibScalar
sensor32lastErrMsg = _Sensor32lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 11, 32, 5),
    _Sensor32lastErrMsg_Type()
)
sensor32lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sensor32lastErrMsg.setStatus("mandatory")
_DaisySensorTable_ObjectIdentity = ObjectIdentity
daisySensorTable = _DaisySensorTable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13)
)
_DaisySensor1_ObjectIdentity = ObjectIdentity
daisySensor1 = _DaisySensor1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 1)
)
_DaisySensor1Name_Type = DisplayString
_DaisySensor1Name_Object = MibScalar
daisySensor1Name = _DaisySensor1Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 1, 1),
    _DaisySensor1Name_Type()
)
daisySensor1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor1Name.setStatus("mandatory")
_DaisySensor1value_Type = DisplayString
_DaisySensor1value_Object = MibScalar
daisySensor1value = _DaisySensor1value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 1, 2),
    _DaisySensor1value_Type()
)
daisySensor1value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor1value.setStatus("mandatory")
_DaisySensor1ErrState_Type = DisplayString
_DaisySensor1ErrState_Object = MibScalar
daisySensor1ErrState = _DaisySensor1ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 1, 3),
    _DaisySensor1ErrState_Type()
)
daisySensor1ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor1ErrState.setStatus("mandatory")
_DaisySensor1lastErrTime_Type = DisplayString
_DaisySensor1lastErrTime_Object = MibScalar
daisySensor1lastErrTime = _DaisySensor1lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 1, 4),
    _DaisySensor1lastErrTime_Type()
)
daisySensor1lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor1lastErrTime.setStatus("mandatory")
_DaisySensor1lastErrMsg_Type = DisplayString
_DaisySensor1lastErrMsg_Object = MibScalar
daisySensor1lastErrMsg = _DaisySensor1lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 1, 5),
    _DaisySensor1lastErrMsg_Type()
)
daisySensor1lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor1lastErrMsg.setStatus("mandatory")
_DaisySensor2_ObjectIdentity = ObjectIdentity
daisySensor2 = _DaisySensor2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 2)
)
_DaisySensor2Name_Type = DisplayString
_DaisySensor2Name_Object = MibScalar
daisySensor2Name = _DaisySensor2Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 2, 1),
    _DaisySensor2Name_Type()
)
daisySensor2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor2Name.setStatus("mandatory")
_DaisySensor2value_Type = DisplayString
_DaisySensor2value_Object = MibScalar
daisySensor2value = _DaisySensor2value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 2, 2),
    _DaisySensor2value_Type()
)
daisySensor2value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor2value.setStatus("mandatory")
_DaisySensor2ErrState_Type = DisplayString
_DaisySensor2ErrState_Object = MibScalar
daisySensor2ErrState = _DaisySensor2ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 2, 3),
    _DaisySensor2ErrState_Type()
)
daisySensor2ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor2ErrState.setStatus("mandatory")
_DaisySensor2lastErrTime_Type = DisplayString
_DaisySensor2lastErrTime_Object = MibScalar
daisySensor2lastErrTime = _DaisySensor2lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 2, 4),
    _DaisySensor2lastErrTime_Type()
)
daisySensor2lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor2lastErrTime.setStatus("mandatory")
_DaisySensor2lastErrMsg_Type = DisplayString
_DaisySensor2lastErrMsg_Object = MibScalar
daisySensor2lastErrMsg = _DaisySensor2lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 2, 5),
    _DaisySensor2lastErrMsg_Type()
)
daisySensor2lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor2lastErrMsg.setStatus("mandatory")
_DaisySensor3_ObjectIdentity = ObjectIdentity
daisySensor3 = _DaisySensor3_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 3)
)
_DaisySensor3Name_Type = DisplayString
_DaisySensor3Name_Object = MibScalar
daisySensor3Name = _DaisySensor3Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 3, 1),
    _DaisySensor3Name_Type()
)
daisySensor3Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor3Name.setStatus("mandatory")
_DaisySensor3value_Type = DisplayString
_DaisySensor3value_Object = MibScalar
daisySensor3value = _DaisySensor3value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 3, 2),
    _DaisySensor3value_Type()
)
daisySensor3value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor3value.setStatus("mandatory")
_DaisySensor3ErrState_Type = DisplayString
_DaisySensor3ErrState_Object = MibScalar
daisySensor3ErrState = _DaisySensor3ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 3, 3),
    _DaisySensor3ErrState_Type()
)
daisySensor3ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor3ErrState.setStatus("mandatory")
_DaisySensor3lastErrTime_Type = DisplayString
_DaisySensor3lastErrTime_Object = MibScalar
daisySensor3lastErrTime = _DaisySensor3lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 3, 4),
    _DaisySensor3lastErrTime_Type()
)
daisySensor3lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor3lastErrTime.setStatus("mandatory")
_DaisySensor3lastErrMsg_Type = DisplayString
_DaisySensor3lastErrMsg_Object = MibScalar
daisySensor3lastErrMsg = _DaisySensor3lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 3, 5),
    _DaisySensor3lastErrMsg_Type()
)
daisySensor3lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor3lastErrMsg.setStatus("mandatory")
_DaisySensor4_ObjectIdentity = ObjectIdentity
daisySensor4 = _DaisySensor4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 4)
)
_DaisySensor4Name_Type = DisplayString
_DaisySensor4Name_Object = MibScalar
daisySensor4Name = _DaisySensor4Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 4, 1),
    _DaisySensor4Name_Type()
)
daisySensor4Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor4Name.setStatus("mandatory")
_DaisySensor4value_Type = DisplayString
_DaisySensor4value_Object = MibScalar
daisySensor4value = _DaisySensor4value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 4, 2),
    _DaisySensor4value_Type()
)
daisySensor4value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor4value.setStatus("mandatory")
_DaisySensor4ErrState_Type = DisplayString
_DaisySensor4ErrState_Object = MibScalar
daisySensor4ErrState = _DaisySensor4ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 4, 3),
    _DaisySensor4ErrState_Type()
)
daisySensor4ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor4ErrState.setStatus("mandatory")
_DaisySensor4lastErrTime_Type = DisplayString
_DaisySensor4lastErrTime_Object = MibScalar
daisySensor4lastErrTime = _DaisySensor4lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 4, 4),
    _DaisySensor4lastErrTime_Type()
)
daisySensor4lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor4lastErrTime.setStatus("mandatory")
_DaisySensor4lastErrMsg_Type = DisplayString
_DaisySensor4lastErrMsg_Object = MibScalar
daisySensor4lastErrMsg = _DaisySensor4lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 4, 5),
    _DaisySensor4lastErrMsg_Type()
)
daisySensor4lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor4lastErrMsg.setStatus("mandatory")
_DaisySensor5_ObjectIdentity = ObjectIdentity
daisySensor5 = _DaisySensor5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 5)
)
_DaisySensor5Name_Type = DisplayString
_DaisySensor5Name_Object = MibScalar
daisySensor5Name = _DaisySensor5Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 5, 1),
    _DaisySensor5Name_Type()
)
daisySensor5Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor5Name.setStatus("mandatory")
_DaisySensor5value_Type = DisplayString
_DaisySensor5value_Object = MibScalar
daisySensor5value = _DaisySensor5value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 5, 2),
    _DaisySensor5value_Type()
)
daisySensor5value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor5value.setStatus("mandatory")
_DaisySensor5ErrState_Type = DisplayString
_DaisySensor5ErrState_Object = MibScalar
daisySensor5ErrState = _DaisySensor5ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 5, 3),
    _DaisySensor5ErrState_Type()
)
daisySensor5ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor5ErrState.setStatus("mandatory")
_DaisySensor5lastErrTime_Type = DisplayString
_DaisySensor5lastErrTime_Object = MibScalar
daisySensor5lastErrTime = _DaisySensor5lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 5, 4),
    _DaisySensor5lastErrTime_Type()
)
daisySensor5lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor5lastErrTime.setStatus("mandatory")
_DaisySensor5lastErrMsg_Type = DisplayString
_DaisySensor5lastErrMsg_Object = MibScalar
daisySensor5lastErrMsg = _DaisySensor5lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 5, 5),
    _DaisySensor5lastErrMsg_Type()
)
daisySensor5lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor5lastErrMsg.setStatus("mandatory")
_DaisySensor6_ObjectIdentity = ObjectIdentity
daisySensor6 = _DaisySensor6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 6)
)
_DaisySensor6Name_Type = DisplayString
_DaisySensor6Name_Object = MibScalar
daisySensor6Name = _DaisySensor6Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 6, 1),
    _DaisySensor6Name_Type()
)
daisySensor6Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor6Name.setStatus("mandatory")
_DaisySensor6value_Type = DisplayString
_DaisySensor6value_Object = MibScalar
daisySensor6value = _DaisySensor6value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 6, 2),
    _DaisySensor6value_Type()
)
daisySensor6value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor6value.setStatus("mandatory")
_DaisySensor6ErrState_Type = DisplayString
_DaisySensor6ErrState_Object = MibScalar
daisySensor6ErrState = _DaisySensor6ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 6, 3),
    _DaisySensor6ErrState_Type()
)
daisySensor6ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor6ErrState.setStatus("mandatory")
_DaisySensor6lastErrTime_Type = DisplayString
_DaisySensor6lastErrTime_Object = MibScalar
daisySensor6lastErrTime = _DaisySensor6lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 6, 4),
    _DaisySensor6lastErrTime_Type()
)
daisySensor6lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor6lastErrTime.setStatus("mandatory")
_DaisySensor6lastErrMsg_Type = DisplayString
_DaisySensor6lastErrMsg_Object = MibScalar
daisySensor6lastErrMsg = _DaisySensor6lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 6, 5),
    _DaisySensor6lastErrMsg_Type()
)
daisySensor6lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor6lastErrMsg.setStatus("mandatory")
_DaisySensor7_ObjectIdentity = ObjectIdentity
daisySensor7 = _DaisySensor7_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 7)
)
_DaisySensor7Name_Type = DisplayString
_DaisySensor7Name_Object = MibScalar
daisySensor7Name = _DaisySensor7Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 7, 1),
    _DaisySensor7Name_Type()
)
daisySensor7Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor7Name.setStatus("mandatory")
_DaisySensor7value_Type = DisplayString
_DaisySensor7value_Object = MibScalar
daisySensor7value = _DaisySensor7value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 7, 2),
    _DaisySensor7value_Type()
)
daisySensor7value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor7value.setStatus("mandatory")
_DaisySensor7ErrState_Type = DisplayString
_DaisySensor7ErrState_Object = MibScalar
daisySensor7ErrState = _DaisySensor7ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 7, 3),
    _DaisySensor7ErrState_Type()
)
daisySensor7ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor7ErrState.setStatus("mandatory")
_DaisySensor7lastErrTime_Type = DisplayString
_DaisySensor7lastErrTime_Object = MibScalar
daisySensor7lastErrTime = _DaisySensor7lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 7, 4),
    _DaisySensor7lastErrTime_Type()
)
daisySensor7lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor7lastErrTime.setStatus("mandatory")
_DaisySensor7lastErrMsg_Type = DisplayString
_DaisySensor7lastErrMsg_Object = MibScalar
daisySensor7lastErrMsg = _DaisySensor7lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 7, 5),
    _DaisySensor7lastErrMsg_Type()
)
daisySensor7lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor7lastErrMsg.setStatus("mandatory")
_DaisySensor8_ObjectIdentity = ObjectIdentity
daisySensor8 = _DaisySensor8_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 8)
)
_DaisySensor8Name_Type = DisplayString
_DaisySensor8Name_Object = MibScalar
daisySensor8Name = _DaisySensor8Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 8, 1),
    _DaisySensor8Name_Type()
)
daisySensor8Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor8Name.setStatus("mandatory")
_DaisySensor8value_Type = DisplayString
_DaisySensor8value_Object = MibScalar
daisySensor8value = _DaisySensor8value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 8, 2),
    _DaisySensor8value_Type()
)
daisySensor8value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor8value.setStatus("mandatory")
_DaisySensor8ErrState_Type = DisplayString
_DaisySensor8ErrState_Object = MibScalar
daisySensor8ErrState = _DaisySensor8ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 8, 3),
    _DaisySensor8ErrState_Type()
)
daisySensor8ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor8ErrState.setStatus("mandatory")
_DaisySensor8lastErrTime_Type = DisplayString
_DaisySensor8lastErrTime_Object = MibScalar
daisySensor8lastErrTime = _DaisySensor8lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 8, 4),
    _DaisySensor8lastErrTime_Type()
)
daisySensor8lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor8lastErrTime.setStatus("mandatory")
_DaisySensor8lastErrMsg_Type = DisplayString
_DaisySensor8lastErrMsg_Object = MibScalar
daisySensor8lastErrMsg = _DaisySensor8lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 8, 5),
    _DaisySensor8lastErrMsg_Type()
)
daisySensor8lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor8lastErrMsg.setStatus("mandatory")
_DaisySensor9_ObjectIdentity = ObjectIdentity
daisySensor9 = _DaisySensor9_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 9)
)
_DaisySensor9Name_Type = DisplayString
_DaisySensor9Name_Object = MibScalar
daisySensor9Name = _DaisySensor9Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 9, 1),
    _DaisySensor9Name_Type()
)
daisySensor9Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor9Name.setStatus("mandatory")
_DaisySensor9value_Type = DisplayString
_DaisySensor9value_Object = MibScalar
daisySensor9value = _DaisySensor9value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 9, 2),
    _DaisySensor9value_Type()
)
daisySensor9value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor9value.setStatus("mandatory")
_DaisySensor9ErrState_Type = DisplayString
_DaisySensor9ErrState_Object = MibScalar
daisySensor9ErrState = _DaisySensor9ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 9, 3),
    _DaisySensor9ErrState_Type()
)
daisySensor9ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor9ErrState.setStatus("mandatory")
_DaisySensor9lastErrTime_Type = DisplayString
_DaisySensor9lastErrTime_Object = MibScalar
daisySensor9lastErrTime = _DaisySensor9lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 9, 4),
    _DaisySensor9lastErrTime_Type()
)
daisySensor9lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor9lastErrTime.setStatus("mandatory")
_DaisySensor9lastErrMsg_Type = DisplayString
_DaisySensor9lastErrMsg_Object = MibScalar
daisySensor9lastErrMsg = _DaisySensor9lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 9, 5),
    _DaisySensor9lastErrMsg_Type()
)
daisySensor9lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor9lastErrMsg.setStatus("mandatory")
_DaisySensor10_ObjectIdentity = ObjectIdentity
daisySensor10 = _DaisySensor10_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 10)
)
_DaisySensor10Name_Type = DisplayString
_DaisySensor10Name_Object = MibScalar
daisySensor10Name = _DaisySensor10Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 10, 1),
    _DaisySensor10Name_Type()
)
daisySensor10Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor10Name.setStatus("mandatory")
_DaisySensor10value_Type = DisplayString
_DaisySensor10value_Object = MibScalar
daisySensor10value = _DaisySensor10value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 10, 2),
    _DaisySensor10value_Type()
)
daisySensor10value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor10value.setStatus("mandatory")
_DaisySensor10ErrState_Type = DisplayString
_DaisySensor10ErrState_Object = MibScalar
daisySensor10ErrState = _DaisySensor10ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 10, 3),
    _DaisySensor10ErrState_Type()
)
daisySensor10ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor10ErrState.setStatus("mandatory")
_DaisySensor10lastErrTime_Type = DisplayString
_DaisySensor10lastErrTime_Object = MibScalar
daisySensor10lastErrTime = _DaisySensor10lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 10, 4),
    _DaisySensor10lastErrTime_Type()
)
daisySensor10lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor10lastErrTime.setStatus("mandatory")
_DaisySensor10lastErrMsg_Type = DisplayString
_DaisySensor10lastErrMsg_Object = MibScalar
daisySensor10lastErrMsg = _DaisySensor10lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 10, 5),
    _DaisySensor10lastErrMsg_Type()
)
daisySensor10lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor10lastErrMsg.setStatus("mandatory")
_DaisySensor11_ObjectIdentity = ObjectIdentity
daisySensor11 = _DaisySensor11_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 11)
)
_DaisySensor11Name_Type = DisplayString
_DaisySensor11Name_Object = MibScalar
daisySensor11Name = _DaisySensor11Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 11, 1),
    _DaisySensor11Name_Type()
)
daisySensor11Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor11Name.setStatus("mandatory")
_DaisySensor11value_Type = DisplayString
_DaisySensor11value_Object = MibScalar
daisySensor11value = _DaisySensor11value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 11, 2),
    _DaisySensor11value_Type()
)
daisySensor11value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor11value.setStatus("mandatory")
_DaisySensor11ErrState_Type = DisplayString
_DaisySensor11ErrState_Object = MibScalar
daisySensor11ErrState = _DaisySensor11ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 11, 3),
    _DaisySensor11ErrState_Type()
)
daisySensor11ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor11ErrState.setStatus("mandatory")
_DaisySensor11lastErrTime_Type = DisplayString
_DaisySensor11lastErrTime_Object = MibScalar
daisySensor11lastErrTime = _DaisySensor11lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 11, 4),
    _DaisySensor11lastErrTime_Type()
)
daisySensor11lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor11lastErrTime.setStatus("mandatory")
_DaisySensor11lastErrMsg_Type = DisplayString
_DaisySensor11lastErrMsg_Object = MibScalar
daisySensor11lastErrMsg = _DaisySensor11lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 11, 5),
    _DaisySensor11lastErrMsg_Type()
)
daisySensor11lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor11lastErrMsg.setStatus("mandatory")
_DaisySensor12_ObjectIdentity = ObjectIdentity
daisySensor12 = _DaisySensor12_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 12)
)
_DaisySensor12Name_Type = DisplayString
_DaisySensor12Name_Object = MibScalar
daisySensor12Name = _DaisySensor12Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 12, 1),
    _DaisySensor12Name_Type()
)
daisySensor12Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor12Name.setStatus("mandatory")
_DaisySensor12value_Type = DisplayString
_DaisySensor12value_Object = MibScalar
daisySensor12value = _DaisySensor12value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 12, 2),
    _DaisySensor12value_Type()
)
daisySensor12value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor12value.setStatus("mandatory")
_DaisySensor12ErrState_Type = DisplayString
_DaisySensor12ErrState_Object = MibScalar
daisySensor12ErrState = _DaisySensor12ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 12, 3),
    _DaisySensor12ErrState_Type()
)
daisySensor12ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor12ErrState.setStatus("mandatory")
_DaisySensor12lastErrTime_Type = DisplayString
_DaisySensor12lastErrTime_Object = MibScalar
daisySensor12lastErrTime = _DaisySensor12lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 12, 4),
    _DaisySensor12lastErrTime_Type()
)
daisySensor12lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor12lastErrTime.setStatus("mandatory")
_DaisySensor12lastErrMsg_Type = DisplayString
_DaisySensor12lastErrMsg_Object = MibScalar
daisySensor12lastErrMsg = _DaisySensor12lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 12, 5),
    _DaisySensor12lastErrMsg_Type()
)
daisySensor12lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor12lastErrMsg.setStatus("mandatory")
_DaisySensor13_ObjectIdentity = ObjectIdentity
daisySensor13 = _DaisySensor13_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 13)
)
_DaisySensor13Name_Type = DisplayString
_DaisySensor13Name_Object = MibScalar
daisySensor13Name = _DaisySensor13Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 13, 1),
    _DaisySensor13Name_Type()
)
daisySensor13Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor13Name.setStatus("mandatory")
_DaisySensor13value_Type = DisplayString
_DaisySensor13value_Object = MibScalar
daisySensor13value = _DaisySensor13value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 13, 2),
    _DaisySensor13value_Type()
)
daisySensor13value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor13value.setStatus("mandatory")
_DaisySensor13ErrState_Type = DisplayString
_DaisySensor13ErrState_Object = MibScalar
daisySensor13ErrState = _DaisySensor13ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 13, 3),
    _DaisySensor13ErrState_Type()
)
daisySensor13ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor13ErrState.setStatus("mandatory")
_DaisySensor13lastErrTime_Type = DisplayString
_DaisySensor13lastErrTime_Object = MibScalar
daisySensor13lastErrTime = _DaisySensor13lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 13, 4),
    _DaisySensor13lastErrTime_Type()
)
daisySensor13lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor13lastErrTime.setStatus("mandatory")
_DaisySensor13lastErrMsg_Type = DisplayString
_DaisySensor13lastErrMsg_Object = MibScalar
daisySensor13lastErrMsg = _DaisySensor13lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 13, 5),
    _DaisySensor13lastErrMsg_Type()
)
daisySensor13lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor13lastErrMsg.setStatus("mandatory")
_DaisySensor14_ObjectIdentity = ObjectIdentity
daisySensor14 = _DaisySensor14_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 14)
)
_DaisySensor14Name_Type = DisplayString
_DaisySensor14Name_Object = MibScalar
daisySensor14Name = _DaisySensor14Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 14, 1),
    _DaisySensor14Name_Type()
)
daisySensor14Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor14Name.setStatus("mandatory")
_DaisySensor14value_Type = DisplayString
_DaisySensor14value_Object = MibScalar
daisySensor14value = _DaisySensor14value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 14, 2),
    _DaisySensor14value_Type()
)
daisySensor14value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor14value.setStatus("mandatory")
_DaisySensor14ErrState_Type = DisplayString
_DaisySensor14ErrState_Object = MibScalar
daisySensor14ErrState = _DaisySensor14ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 14, 3),
    _DaisySensor14ErrState_Type()
)
daisySensor14ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor14ErrState.setStatus("mandatory")
_DaisySensor14lastErrTime_Type = DisplayString
_DaisySensor14lastErrTime_Object = MibScalar
daisySensor14lastErrTime = _DaisySensor14lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 14, 4),
    _DaisySensor14lastErrTime_Type()
)
daisySensor14lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor14lastErrTime.setStatus("mandatory")
_DaisySensor14lastErrMsg_Type = DisplayString
_DaisySensor14lastErrMsg_Object = MibScalar
daisySensor14lastErrMsg = _DaisySensor14lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 14, 5),
    _DaisySensor14lastErrMsg_Type()
)
daisySensor14lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor14lastErrMsg.setStatus("mandatory")
_DaisySensor15_ObjectIdentity = ObjectIdentity
daisySensor15 = _DaisySensor15_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 15)
)
_DaisySensor15Name_Type = DisplayString
_DaisySensor15Name_Object = MibScalar
daisySensor15Name = _DaisySensor15Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 15, 1),
    _DaisySensor15Name_Type()
)
daisySensor15Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor15Name.setStatus("mandatory")
_DaisySensor15value_Type = DisplayString
_DaisySensor15value_Object = MibScalar
daisySensor15value = _DaisySensor15value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 15, 2),
    _DaisySensor15value_Type()
)
daisySensor15value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor15value.setStatus("mandatory")
_DaisySensor15ErrState_Type = DisplayString
_DaisySensor15ErrState_Object = MibScalar
daisySensor15ErrState = _DaisySensor15ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 15, 3),
    _DaisySensor15ErrState_Type()
)
daisySensor15ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor15ErrState.setStatus("mandatory")
_DaisySensor15lastErrTime_Type = DisplayString
_DaisySensor15lastErrTime_Object = MibScalar
daisySensor15lastErrTime = _DaisySensor15lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 15, 4),
    _DaisySensor15lastErrTime_Type()
)
daisySensor15lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor15lastErrTime.setStatus("mandatory")
_DaisySensor15lastErrMsg_Type = DisplayString
_DaisySensor15lastErrMsg_Object = MibScalar
daisySensor15lastErrMsg = _DaisySensor15lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 15, 5),
    _DaisySensor15lastErrMsg_Type()
)
daisySensor15lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor15lastErrMsg.setStatus("mandatory")
_DaisySensor16_ObjectIdentity = ObjectIdentity
daisySensor16 = _DaisySensor16_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 16)
)
_DaisySensor16Name_Type = DisplayString
_DaisySensor16Name_Object = MibScalar
daisySensor16Name = _DaisySensor16Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 16, 1),
    _DaisySensor16Name_Type()
)
daisySensor16Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor16Name.setStatus("mandatory")
_DaisySensor16value_Type = DisplayString
_DaisySensor16value_Object = MibScalar
daisySensor16value = _DaisySensor16value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 16, 2),
    _DaisySensor16value_Type()
)
daisySensor16value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor16value.setStatus("mandatory")
_DaisySensor16ErrState_Type = DisplayString
_DaisySensor16ErrState_Object = MibScalar
daisySensor16ErrState = _DaisySensor16ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 16, 3),
    _DaisySensor16ErrState_Type()
)
daisySensor16ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor16ErrState.setStatus("mandatory")
_DaisySensor16lastErrTime_Type = DisplayString
_DaisySensor16lastErrTime_Object = MibScalar
daisySensor16lastErrTime = _DaisySensor16lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 16, 4),
    _DaisySensor16lastErrTime_Type()
)
daisySensor16lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor16lastErrTime.setStatus("mandatory")
_DaisySensor16lastErrMsg_Type = DisplayString
_DaisySensor16lastErrMsg_Object = MibScalar
daisySensor16lastErrMsg = _DaisySensor16lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 16, 5),
    _DaisySensor16lastErrMsg_Type()
)
daisySensor16lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor16lastErrMsg.setStatus("mandatory")
_DaisySensor17_ObjectIdentity = ObjectIdentity
daisySensor17 = _DaisySensor17_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 17)
)
_DaisySensor17Name_Type = DisplayString
_DaisySensor17Name_Object = MibScalar
daisySensor17Name = _DaisySensor17Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 17, 1),
    _DaisySensor17Name_Type()
)
daisySensor17Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor17Name.setStatus("mandatory")
_DaisySensor17value_Type = DisplayString
_DaisySensor17value_Object = MibScalar
daisySensor17value = _DaisySensor17value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 17, 2),
    _DaisySensor17value_Type()
)
daisySensor17value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor17value.setStatus("mandatory")
_DaisySensor17ErrState_Type = DisplayString
_DaisySensor17ErrState_Object = MibScalar
daisySensor17ErrState = _DaisySensor17ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 17, 3),
    _DaisySensor17ErrState_Type()
)
daisySensor17ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor17ErrState.setStatus("mandatory")
_DaisySensor17lastErrTime_Type = DisplayString
_DaisySensor17lastErrTime_Object = MibScalar
daisySensor17lastErrTime = _DaisySensor17lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 17, 4),
    _DaisySensor17lastErrTime_Type()
)
daisySensor17lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor17lastErrTime.setStatus("mandatory")
_DaisySensor17lastErrMsg_Type = DisplayString
_DaisySensor17lastErrMsg_Object = MibScalar
daisySensor17lastErrMsg = _DaisySensor17lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 17, 5),
    _DaisySensor17lastErrMsg_Type()
)
daisySensor17lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor17lastErrMsg.setStatus("mandatory")
_DaisySensor18_ObjectIdentity = ObjectIdentity
daisySensor18 = _DaisySensor18_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 18)
)
_DaisySensor18Name_Type = DisplayString
_DaisySensor18Name_Object = MibScalar
daisySensor18Name = _DaisySensor18Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 18, 1),
    _DaisySensor18Name_Type()
)
daisySensor18Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor18Name.setStatus("mandatory")
_DaisySensor18value_Type = DisplayString
_DaisySensor18value_Object = MibScalar
daisySensor18value = _DaisySensor18value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 18, 2),
    _DaisySensor18value_Type()
)
daisySensor18value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor18value.setStatus("mandatory")
_DaisySensor18ErrState_Type = DisplayString
_DaisySensor18ErrState_Object = MibScalar
daisySensor18ErrState = _DaisySensor18ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 18, 3),
    _DaisySensor18ErrState_Type()
)
daisySensor18ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor18ErrState.setStatus("mandatory")
_DaisySensor18lastErrTime_Type = DisplayString
_DaisySensor18lastErrTime_Object = MibScalar
daisySensor18lastErrTime = _DaisySensor18lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 18, 4),
    _DaisySensor18lastErrTime_Type()
)
daisySensor18lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor18lastErrTime.setStatus("mandatory")
_DaisySensor18lastErrMsg_Type = DisplayString
_DaisySensor18lastErrMsg_Object = MibScalar
daisySensor18lastErrMsg = _DaisySensor18lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 18, 5),
    _DaisySensor18lastErrMsg_Type()
)
daisySensor18lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor18lastErrMsg.setStatus("mandatory")
_DaisySensor19_ObjectIdentity = ObjectIdentity
daisySensor19 = _DaisySensor19_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 19)
)
_DaisySensor19Name_Type = DisplayString
_DaisySensor19Name_Object = MibScalar
daisySensor19Name = _DaisySensor19Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 19, 1),
    _DaisySensor19Name_Type()
)
daisySensor19Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor19Name.setStatus("mandatory")
_DaisySensor19value_Type = DisplayString
_DaisySensor19value_Object = MibScalar
daisySensor19value = _DaisySensor19value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 19, 2),
    _DaisySensor19value_Type()
)
daisySensor19value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor19value.setStatus("mandatory")
_DaisySensor19ErrState_Type = DisplayString
_DaisySensor19ErrState_Object = MibScalar
daisySensor19ErrState = _DaisySensor19ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 19, 3),
    _DaisySensor19ErrState_Type()
)
daisySensor19ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor19ErrState.setStatus("mandatory")
_DaisySensor19lastErrTime_Type = DisplayString
_DaisySensor19lastErrTime_Object = MibScalar
daisySensor19lastErrTime = _DaisySensor19lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 19, 4),
    _DaisySensor19lastErrTime_Type()
)
daisySensor19lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor19lastErrTime.setStatus("mandatory")
_DaisySensor19lastErrMsg_Type = DisplayString
_DaisySensor19lastErrMsg_Object = MibScalar
daisySensor19lastErrMsg = _DaisySensor19lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 19, 5),
    _DaisySensor19lastErrMsg_Type()
)
daisySensor19lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor19lastErrMsg.setStatus("mandatory")
_DaisySensor20_ObjectIdentity = ObjectIdentity
daisySensor20 = _DaisySensor20_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 20)
)
_DaisySensor20Name_Type = DisplayString
_DaisySensor20Name_Object = MibScalar
daisySensor20Name = _DaisySensor20Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 20, 1),
    _DaisySensor20Name_Type()
)
daisySensor20Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor20Name.setStatus("mandatory")
_DaisySensor20value_Type = DisplayString
_DaisySensor20value_Object = MibScalar
daisySensor20value = _DaisySensor20value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 20, 2),
    _DaisySensor20value_Type()
)
daisySensor20value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor20value.setStatus("mandatory")
_DaisySensor20ErrState_Type = DisplayString
_DaisySensor20ErrState_Object = MibScalar
daisySensor20ErrState = _DaisySensor20ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 20, 3),
    _DaisySensor20ErrState_Type()
)
daisySensor20ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor20ErrState.setStatus("mandatory")
_DaisySensor20lastErrTime_Type = DisplayString
_DaisySensor20lastErrTime_Object = MibScalar
daisySensor20lastErrTime = _DaisySensor20lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 20, 4),
    _DaisySensor20lastErrTime_Type()
)
daisySensor20lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor20lastErrTime.setStatus("mandatory")
_DaisySensor20lastErrMsg_Type = DisplayString
_DaisySensor20lastErrMsg_Object = MibScalar
daisySensor20lastErrMsg = _DaisySensor20lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 20, 5),
    _DaisySensor20lastErrMsg_Type()
)
daisySensor20lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor20lastErrMsg.setStatus("mandatory")
_DaisySensor21_ObjectIdentity = ObjectIdentity
daisySensor21 = _DaisySensor21_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 21)
)
_DaisySensor21Name_Type = DisplayString
_DaisySensor21Name_Object = MibScalar
daisySensor21Name = _DaisySensor21Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 21, 1),
    _DaisySensor21Name_Type()
)
daisySensor21Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor21Name.setStatus("mandatory")
_DaisySensor21value_Type = DisplayString
_DaisySensor21value_Object = MibScalar
daisySensor21value = _DaisySensor21value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 21, 2),
    _DaisySensor21value_Type()
)
daisySensor21value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor21value.setStatus("mandatory")
_DaisySensor21ErrState_Type = DisplayString
_DaisySensor21ErrState_Object = MibScalar
daisySensor21ErrState = _DaisySensor21ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 21, 3),
    _DaisySensor21ErrState_Type()
)
daisySensor21ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor21ErrState.setStatus("mandatory")
_DaisySensor21lastErrTime_Type = DisplayString
_DaisySensor21lastErrTime_Object = MibScalar
daisySensor21lastErrTime = _DaisySensor21lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 21, 4),
    _DaisySensor21lastErrTime_Type()
)
daisySensor21lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor21lastErrTime.setStatus("mandatory")
_DaisySensor21lastErrMsg_Type = DisplayString
_DaisySensor21lastErrMsg_Object = MibScalar
daisySensor21lastErrMsg = _DaisySensor21lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 21, 5),
    _DaisySensor21lastErrMsg_Type()
)
daisySensor21lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor21lastErrMsg.setStatus("mandatory")
_DaisySensor22_ObjectIdentity = ObjectIdentity
daisySensor22 = _DaisySensor22_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 22)
)
_DaisySensor22Name_Type = DisplayString
_DaisySensor22Name_Object = MibScalar
daisySensor22Name = _DaisySensor22Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 22, 1),
    _DaisySensor22Name_Type()
)
daisySensor22Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor22Name.setStatus("mandatory")
_DaisySensor22value_Type = DisplayString
_DaisySensor22value_Object = MibScalar
daisySensor22value = _DaisySensor22value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 22, 2),
    _DaisySensor22value_Type()
)
daisySensor22value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor22value.setStatus("mandatory")
_DaisySensor22ErrState_Type = DisplayString
_DaisySensor22ErrState_Object = MibScalar
daisySensor22ErrState = _DaisySensor22ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 22, 3),
    _DaisySensor22ErrState_Type()
)
daisySensor22ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor22ErrState.setStatus("mandatory")
_DaisySensor22lastErrTime_Type = DisplayString
_DaisySensor22lastErrTime_Object = MibScalar
daisySensor22lastErrTime = _DaisySensor22lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 22, 4),
    _DaisySensor22lastErrTime_Type()
)
daisySensor22lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor22lastErrTime.setStatus("mandatory")
_DaisySensor22lastErrMsg_Type = DisplayString
_DaisySensor22lastErrMsg_Object = MibScalar
daisySensor22lastErrMsg = _DaisySensor22lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 22, 5),
    _DaisySensor22lastErrMsg_Type()
)
daisySensor22lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor22lastErrMsg.setStatus("mandatory")
_DaisySensor23_ObjectIdentity = ObjectIdentity
daisySensor23 = _DaisySensor23_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 23)
)
_DaisySensor23Name_Type = DisplayString
_DaisySensor23Name_Object = MibScalar
daisySensor23Name = _DaisySensor23Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 23, 1),
    _DaisySensor23Name_Type()
)
daisySensor23Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor23Name.setStatus("mandatory")
_DaisySensor23value_Type = DisplayString
_DaisySensor23value_Object = MibScalar
daisySensor23value = _DaisySensor23value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 23, 2),
    _DaisySensor23value_Type()
)
daisySensor23value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor23value.setStatus("mandatory")
_DaisySensor23ErrState_Type = DisplayString
_DaisySensor23ErrState_Object = MibScalar
daisySensor23ErrState = _DaisySensor23ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 23, 3),
    _DaisySensor23ErrState_Type()
)
daisySensor23ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor23ErrState.setStatus("mandatory")
_DaisySensor23lastErrTime_Type = DisplayString
_DaisySensor23lastErrTime_Object = MibScalar
daisySensor23lastErrTime = _DaisySensor23lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 23, 4),
    _DaisySensor23lastErrTime_Type()
)
daisySensor23lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor23lastErrTime.setStatus("mandatory")
_DaisySensor23lastErrMsg_Type = DisplayString
_DaisySensor23lastErrMsg_Object = MibScalar
daisySensor23lastErrMsg = _DaisySensor23lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 23, 5),
    _DaisySensor23lastErrMsg_Type()
)
daisySensor23lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor23lastErrMsg.setStatus("mandatory")
_DaisySensor24_ObjectIdentity = ObjectIdentity
daisySensor24 = _DaisySensor24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 24)
)
_DaisySensor24Name_Type = DisplayString
_DaisySensor24Name_Object = MibScalar
daisySensor24Name = _DaisySensor24Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 24, 1),
    _DaisySensor24Name_Type()
)
daisySensor24Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor24Name.setStatus("mandatory")
_DaisySensor24value_Type = DisplayString
_DaisySensor24value_Object = MibScalar
daisySensor24value = _DaisySensor24value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 24, 2),
    _DaisySensor24value_Type()
)
daisySensor24value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor24value.setStatus("mandatory")
_DaisySensor24ErrState_Type = DisplayString
_DaisySensor24ErrState_Object = MibScalar
daisySensor24ErrState = _DaisySensor24ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 24, 3),
    _DaisySensor24ErrState_Type()
)
daisySensor24ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor24ErrState.setStatus("mandatory")
_DaisySensor24lastErrTime_Type = DisplayString
_DaisySensor24lastErrTime_Object = MibScalar
daisySensor24lastErrTime = _DaisySensor24lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 24, 4),
    _DaisySensor24lastErrTime_Type()
)
daisySensor24lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor24lastErrTime.setStatus("mandatory")
_DaisySensor24lastErrMsg_Type = DisplayString
_DaisySensor24lastErrMsg_Object = MibScalar
daisySensor24lastErrMsg = _DaisySensor24lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 24, 5),
    _DaisySensor24lastErrMsg_Type()
)
daisySensor24lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor24lastErrMsg.setStatus("mandatory")
_DaisySensor25_ObjectIdentity = ObjectIdentity
daisySensor25 = _DaisySensor25_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 25)
)
_DaisySensor25Name_Type = DisplayString
_DaisySensor25Name_Object = MibScalar
daisySensor25Name = _DaisySensor25Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 25, 1),
    _DaisySensor25Name_Type()
)
daisySensor25Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor25Name.setStatus("mandatory")
_DaisySensor25value_Type = DisplayString
_DaisySensor25value_Object = MibScalar
daisySensor25value = _DaisySensor25value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 25, 2),
    _DaisySensor25value_Type()
)
daisySensor25value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor25value.setStatus("mandatory")
_DaisySensor25ErrState_Type = DisplayString
_DaisySensor25ErrState_Object = MibScalar
daisySensor25ErrState = _DaisySensor25ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 25, 3),
    _DaisySensor25ErrState_Type()
)
daisySensor25ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor25ErrState.setStatus("mandatory")
_DaisySensor25lastErrTime_Type = DisplayString
_DaisySensor25lastErrTime_Object = MibScalar
daisySensor25lastErrTime = _DaisySensor25lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 25, 4),
    _DaisySensor25lastErrTime_Type()
)
daisySensor25lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor25lastErrTime.setStatus("mandatory")
_DaisySensor25lastErrMsg_Type = DisplayString
_DaisySensor25lastErrMsg_Object = MibScalar
daisySensor25lastErrMsg = _DaisySensor25lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 25, 5),
    _DaisySensor25lastErrMsg_Type()
)
daisySensor25lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor25lastErrMsg.setStatus("mandatory")
_DaisySensor26_ObjectIdentity = ObjectIdentity
daisySensor26 = _DaisySensor26_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 26)
)
_DaisySensor26Name_Type = DisplayString
_DaisySensor26Name_Object = MibScalar
daisySensor26Name = _DaisySensor26Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 26, 1),
    _DaisySensor26Name_Type()
)
daisySensor26Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor26Name.setStatus("mandatory")
_DaisySensor26value_Type = DisplayString
_DaisySensor26value_Object = MibScalar
daisySensor26value = _DaisySensor26value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 26, 2),
    _DaisySensor26value_Type()
)
daisySensor26value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor26value.setStatus("mandatory")
_DaisySensor26ErrState_Type = DisplayString
_DaisySensor26ErrState_Object = MibScalar
daisySensor26ErrState = _DaisySensor26ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 26, 3),
    _DaisySensor26ErrState_Type()
)
daisySensor26ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor26ErrState.setStatus("mandatory")
_DaisySensor26lastErrTime_Type = DisplayString
_DaisySensor26lastErrTime_Object = MibScalar
daisySensor26lastErrTime = _DaisySensor26lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 26, 4),
    _DaisySensor26lastErrTime_Type()
)
daisySensor26lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor26lastErrTime.setStatus("mandatory")
_DaisySensor26lastErrMsg_Type = DisplayString
_DaisySensor26lastErrMsg_Object = MibScalar
daisySensor26lastErrMsg = _DaisySensor26lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 26, 5),
    _DaisySensor26lastErrMsg_Type()
)
daisySensor26lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor26lastErrMsg.setStatus("mandatory")
_DaisySensor27_ObjectIdentity = ObjectIdentity
daisySensor27 = _DaisySensor27_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 27)
)
_DaisySensor27Name_Type = DisplayString
_DaisySensor27Name_Object = MibScalar
daisySensor27Name = _DaisySensor27Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 27, 1),
    _DaisySensor27Name_Type()
)
daisySensor27Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor27Name.setStatus("mandatory")
_DaisySensor27value_Type = DisplayString
_DaisySensor27value_Object = MibScalar
daisySensor27value = _DaisySensor27value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 27, 2),
    _DaisySensor27value_Type()
)
daisySensor27value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor27value.setStatus("mandatory")
_DaisySensor27ErrState_Type = DisplayString
_DaisySensor27ErrState_Object = MibScalar
daisySensor27ErrState = _DaisySensor27ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 27, 3),
    _DaisySensor27ErrState_Type()
)
daisySensor27ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor27ErrState.setStatus("mandatory")
_DaisySensor27lastErrTime_Type = DisplayString
_DaisySensor27lastErrTime_Object = MibScalar
daisySensor27lastErrTime = _DaisySensor27lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 27, 4),
    _DaisySensor27lastErrTime_Type()
)
daisySensor27lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor27lastErrTime.setStatus("mandatory")
_DaisySensor27lastErrMsg_Type = DisplayString
_DaisySensor27lastErrMsg_Object = MibScalar
daisySensor27lastErrMsg = _DaisySensor27lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 27, 5),
    _DaisySensor27lastErrMsg_Type()
)
daisySensor27lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor27lastErrMsg.setStatus("mandatory")
_DaisySensor28_ObjectIdentity = ObjectIdentity
daisySensor28 = _DaisySensor28_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 28)
)
_DaisySensor28Name_Type = DisplayString
_DaisySensor28Name_Object = MibScalar
daisySensor28Name = _DaisySensor28Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 28, 1),
    _DaisySensor28Name_Type()
)
daisySensor28Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor28Name.setStatus("mandatory")
_DaisySensor28value_Type = DisplayString
_DaisySensor28value_Object = MibScalar
daisySensor28value = _DaisySensor28value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 28, 2),
    _DaisySensor28value_Type()
)
daisySensor28value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor28value.setStatus("mandatory")
_DaisySensor28ErrState_Type = DisplayString
_DaisySensor28ErrState_Object = MibScalar
daisySensor28ErrState = _DaisySensor28ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 28, 3),
    _DaisySensor28ErrState_Type()
)
daisySensor28ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor28ErrState.setStatus("mandatory")
_DaisySensor28lastErrTime_Type = DisplayString
_DaisySensor28lastErrTime_Object = MibScalar
daisySensor28lastErrTime = _DaisySensor28lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 28, 4),
    _DaisySensor28lastErrTime_Type()
)
daisySensor28lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor28lastErrTime.setStatus("mandatory")
_DaisySensor28lastErrMsg_Type = DisplayString
_DaisySensor28lastErrMsg_Object = MibScalar
daisySensor28lastErrMsg = _DaisySensor28lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 28, 5),
    _DaisySensor28lastErrMsg_Type()
)
daisySensor28lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor28lastErrMsg.setStatus("mandatory")
_DaisySensor29_ObjectIdentity = ObjectIdentity
daisySensor29 = _DaisySensor29_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 29)
)
_DaisySensor29Name_Type = DisplayString
_DaisySensor29Name_Object = MibScalar
daisySensor29Name = _DaisySensor29Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 29, 1),
    _DaisySensor29Name_Type()
)
daisySensor29Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor29Name.setStatus("mandatory")
_DaisySensor29value_Type = DisplayString
_DaisySensor29value_Object = MibScalar
daisySensor29value = _DaisySensor29value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 29, 2),
    _DaisySensor29value_Type()
)
daisySensor29value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor29value.setStatus("mandatory")
_DaisySensor29ErrState_Type = DisplayString
_DaisySensor29ErrState_Object = MibScalar
daisySensor29ErrState = _DaisySensor29ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 29, 3),
    _DaisySensor29ErrState_Type()
)
daisySensor29ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor29ErrState.setStatus("mandatory")
_DaisySensor29lastErrTime_Type = DisplayString
_DaisySensor29lastErrTime_Object = MibScalar
daisySensor29lastErrTime = _DaisySensor29lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 29, 4),
    _DaisySensor29lastErrTime_Type()
)
daisySensor29lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor29lastErrTime.setStatus("mandatory")
_DaisySensor29lastErrMsg_Type = DisplayString
_DaisySensor29lastErrMsg_Object = MibScalar
daisySensor29lastErrMsg = _DaisySensor29lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 29, 5),
    _DaisySensor29lastErrMsg_Type()
)
daisySensor29lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor29lastErrMsg.setStatus("mandatory")
_DaisySensor30_ObjectIdentity = ObjectIdentity
daisySensor30 = _DaisySensor30_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 30)
)
_DaisySensor30Name_Type = DisplayString
_DaisySensor30Name_Object = MibScalar
daisySensor30Name = _DaisySensor30Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 30, 1),
    _DaisySensor30Name_Type()
)
daisySensor30Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor30Name.setStatus("mandatory")
_DaisySensor30value_Type = DisplayString
_DaisySensor30value_Object = MibScalar
daisySensor30value = _DaisySensor30value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 30, 2),
    _DaisySensor30value_Type()
)
daisySensor30value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor30value.setStatus("mandatory")
_DaisySensor30ErrState_Type = DisplayString
_DaisySensor30ErrState_Object = MibScalar
daisySensor30ErrState = _DaisySensor30ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 30, 3),
    _DaisySensor30ErrState_Type()
)
daisySensor30ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor30ErrState.setStatus("mandatory")
_DaisySensor30lastErrTime_Type = DisplayString
_DaisySensor30lastErrTime_Object = MibScalar
daisySensor30lastErrTime = _DaisySensor30lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 30, 4),
    _DaisySensor30lastErrTime_Type()
)
daisySensor30lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor30lastErrTime.setStatus("mandatory")
_DaisySensor30lastErrMsg_Type = DisplayString
_DaisySensor30lastErrMsg_Object = MibScalar
daisySensor30lastErrMsg = _DaisySensor30lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 30, 5),
    _DaisySensor30lastErrMsg_Type()
)
daisySensor30lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor30lastErrMsg.setStatus("mandatory")
_DaisySensor31_ObjectIdentity = ObjectIdentity
daisySensor31 = _DaisySensor31_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 31)
)
_DaisySensor31Name_Type = DisplayString
_DaisySensor31Name_Object = MibScalar
daisySensor31Name = _DaisySensor31Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 31, 1),
    _DaisySensor31Name_Type()
)
daisySensor31Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor31Name.setStatus("mandatory")
_DaisySensor31value_Type = DisplayString
_DaisySensor31value_Object = MibScalar
daisySensor31value = _DaisySensor31value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 31, 2),
    _DaisySensor31value_Type()
)
daisySensor31value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor31value.setStatus("mandatory")
_DaisySensor31ErrState_Type = DisplayString
_DaisySensor31ErrState_Object = MibScalar
daisySensor31ErrState = _DaisySensor31ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 31, 3),
    _DaisySensor31ErrState_Type()
)
daisySensor31ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor31ErrState.setStatus("mandatory")
_DaisySensor31lastErrTime_Type = DisplayString
_DaisySensor31lastErrTime_Object = MibScalar
daisySensor31lastErrTime = _DaisySensor31lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 31, 4),
    _DaisySensor31lastErrTime_Type()
)
daisySensor31lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor31lastErrTime.setStatus("mandatory")
_DaisySensor31lastErrMsg_Type = DisplayString
_DaisySensor31lastErrMsg_Object = MibScalar
daisySensor31lastErrMsg = _DaisySensor31lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 31, 5),
    _DaisySensor31lastErrMsg_Type()
)
daisySensor31lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor31lastErrMsg.setStatus("mandatory")
_DaisySensor32_ObjectIdentity = ObjectIdentity
daisySensor32 = _DaisySensor32_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 17095, 13, 32)
)
_DaisySensor32Name_Type = DisplayString
_DaisySensor32Name_Object = MibScalar
daisySensor32Name = _DaisySensor32Name_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 32, 1),
    _DaisySensor32Name_Type()
)
daisySensor32Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor32Name.setStatus("mandatory")
_DaisySensor32value_Type = DisplayString
_DaisySensor32value_Object = MibScalar
daisySensor32value = _DaisySensor32value_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 32, 2),
    _DaisySensor32value_Type()
)
daisySensor32value.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor32value.setStatus("mandatory")
_DaisySensor32ErrState_Type = DisplayString
_DaisySensor32ErrState_Object = MibScalar
daisySensor32ErrState = _DaisySensor32ErrState_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 32, 3),
    _DaisySensor32ErrState_Type()
)
daisySensor32ErrState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor32ErrState.setStatus("mandatory")
_DaisySensor32lastErrTime_Type = DisplayString
_DaisySensor32lastErrTime_Object = MibScalar
daisySensor32lastErrTime = _DaisySensor32lastErrTime_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 32, 4),
    _DaisySensor32lastErrTime_Type()
)
daisySensor32lastErrTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor32lastErrTime.setStatus("mandatory")
_DaisySensor32lastErrMsg_Type = DisplayString
_DaisySensor32lastErrMsg_Object = MibScalar
daisySensor32lastErrMsg = _DaisySensor32lastErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 17095, 13, 32, 5),
    _DaisySensor32lastErrMsg_Type()
)
daisySensor32lastErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daisySensor32lastErrMsg.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sensorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 17095, 0, 1)
)
sensorAlert.setObjects(
      *(("ServersCheck", "sensor1TrapErrMsg"),
        ("ServersCheck", "sensor2TrapErrMsg"),
        ("ServersCheck", "sensor3TrapErrMsg"),
        ("ServersCheck", "sensor4TrapErrMsg"),
        ("ServersCheck", "sensor5TrapErrMsg"),
        ("ServersCheck", "sensor6TrapErrMsg"))
)
if mibBuilder.loadTexts:
    sensorAlert.setStatus(
        ""
    )

iosensorAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 17095, 0, 2)
)
iosensorAlert.setObjects(
      *(("ServersCheck", "iosensorINPUT1trapErrMsg"),
        ("ServersCheck", "iosensorINPUT2trapErrMsg"),
        ("ServersCheck", "iosensorINPUT3trapErrMsg"),
        ("ServersCheck", "iosensorINPUT4trapErrMsg"),
        ("ServersCheck", "iosensorINPUT5trapErrMsg"),
        ("ServersCheck", "iosensorINPUT6trapErrMsg"),
        ("ServersCheck", "iosensorINPUT7trapErrMsg"),
        ("ServersCheck", "iosensorINPUT8trapErrMsg"),
        ("ServersCheck", "iosensorINPUT9trapErrMsg"),
        ("ServersCheck", "iosensorINPUT10trapErrMsg"),
        ("ServersCheck", "iosensorINPUT11trapErrMsg"),
        ("ServersCheck", "iosensorINPUT12trapErrMsg"),
        ("ServersCheck", "iosensorINPUT13trapErrMsg"),
        ("ServersCheck", "iosensorINPUT14trapErrMsg"),
        ("ServersCheck", "iosensorINPUT15trapErrMsg"),
        ("ServersCheck", "iosensorINPUT16trapErrMsg"))
)
if mibBuilder.loadTexts:
    iosensorAlert.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ServersCheck",
    **{"serverscheck": serverscheck,
       "sensorAlert": sensorAlert,
       "iosensorAlert": iosensorAlert,
       "product": product,
       "productname": productname,
       "productversion": productversion,
       "productdate": productdate,
       "productusername": productusername,
       "productuserloc": productuserloc,
       "productnetip": productnetip,
       "productnetgateway": productnetgateway,
       "productnetpridns": productnetpridns,
       "productnetsecdns": productnetsecdns,
       "setup": setup,
       "traps": traps,
       "trapEntry": trapEntry,
       "trapReceiverNumber": trapReceiverNumber,
       "trapEnabled": trapEnabled,
       "trapReceiverIPAddress": trapReceiverIPAddress,
       "trapCommunity": trapCommunity,
       "control": control,
       "sensor1name": sensor1name,
       "sensor1Value": sensor1Value,
       "sensor1LastErrMsg": sensor1LastErrMsg,
       "sensor1LastErrTime": sensor1LastErrTime,
       "sensor2name": sensor2name,
       "sensor2Value": sensor2Value,
       "sensor2LastErrMsg": sensor2LastErrMsg,
       "sensor2LastErrTime": sensor2LastErrTime,
       "sensor3name": sensor3name,
       "sensor3Value": sensor3Value,
       "sensor3LastErrMsg": sensor3LastErrMsg,
       "sensor3LastErrTime": sensor3LastErrTime,
       "sensor4name": sensor4name,
       "sensor4Value": sensor4Value,
       "sensor4LastErrMsg": sensor4LastErrMsg,
       "sensor4LastErrTime": sensor4LastErrTime,
       "sensor5name": sensor5name,
       "sensor5Value": sensor5Value,
       "sensor5LastErrMsg": sensor5LastErrMsg,
       "sensor5LastErrTime": sensor5LastErrTime,
       "sensor6name": sensor6name,
       "sensor6Value": sensor6Value,
       "sensor6LastErrMsg": sensor6LastErrMsg,
       "sensor6LastErrTime": sensor6LastErrTime,
       "sensor7name": sensor7name,
       "sensor7Value": sensor7Value,
       "sensor7LastErrMsg": sensor7LastErrMsg,
       "sensor7LastErrTime": sensor7LastErrTime,
       "sensor8name": sensor8name,
       "sensor8Value": sensor8Value,
       "sensor8LastErrMsg": sensor8LastErrMsg,
       "sensor8LastErrTime": sensor8LastErrTime,
       "trapalerts": trapalerts,
       "sensor1TrapErrMsg": sensor1TrapErrMsg,
       "sensor2TrapErrMsg": sensor2TrapErrMsg,
       "sensor3TrapErrMsg": sensor3TrapErrMsg,
       "sensor4TrapErrMsg": sensor4TrapErrMsg,
       "sensor5TrapErrMsg": sensor5TrapErrMsg,
       "sensor6TrapErrMsg": sensor6TrapErrMsg,
       "iotrapalerts": iotrapalerts,
       "iosensorINPUT1trapErrMsg": iosensorINPUT1trapErrMsg,
       "iosensorINPUT2trapErrMsg": iosensorINPUT2trapErrMsg,
       "iosensorINPUT3trapErrMsg": iosensorINPUT3trapErrMsg,
       "iosensorINPUT4trapErrMsg": iosensorINPUT4trapErrMsg,
       "iosensorINPUT5trapErrMsg": iosensorINPUT5trapErrMsg,
       "iosensorINPUT6trapErrMsg": iosensorINPUT6trapErrMsg,
       "iosensorINPUT7trapErrMsg": iosensorINPUT7trapErrMsg,
       "iosensorINPUT8trapErrMsg": iosensorINPUT8trapErrMsg,
       "iosensorINPUT9trapErrMsg": iosensorINPUT9trapErrMsg,
       "iosensorINPUT10trapErrMsg": iosensorINPUT10trapErrMsg,
       "iosensorINPUT11trapErrMsg": iosensorINPUT11trapErrMsg,
       "iosensorINPUT12trapErrMsg": iosensorINPUT12trapErrMsg,
       "iosensorINPUT13trapErrMsg": iosensorINPUT13trapErrMsg,
       "iosensorINPUT14trapErrMsg": iosensorINPUT14trapErrMsg,
       "iosensorINPUT15trapErrMsg": iosensorINPUT15trapErrMsg,
       "iosensorINPUT16trapErrMsg": iosensorINPUT16trapErrMsg,
       "input": input,
       "input1name": input1name,
       "input1Value": input1Value,
       "input1LastErrMsg": input1LastErrMsg,
       "input2name": input2name,
       "input2Value": input2Value,
       "input2LastErrMsg": input2LastErrMsg,
       "input3name": input3name,
       "input3Value": input3Value,
       "input3LastErrMsg": input3LastErrMsg,
       "input4name": input4name,
       "input4Value": input4Value,
       "input4LastErrMsg": input4LastErrMsg,
       "input5name": input5name,
       "input5Value": input5Value,
       "input5LastErrMsg": input5LastErrMsg,
       "input6name": input6name,
       "input6Value": input6Value,
       "input6LastErrMsg": input6LastErrMsg,
       "input7name": input7name,
       "input7Value": input7Value,
       "input7LastErrMsg": input7LastErrMsg,
       "input8name": input8name,
       "input8Value": input8Value,
       "input8LastErrMsg": input8LastErrMsg,
       "input9name": input9name,
       "input9Value": input9Value,
       "input9LastErrMsg": input9LastErrMsg,
       "input10name": input10name,
       "input10Value": input10Value,
       "input10LastErrMsg": input10LastErrMsg,
       "input11name": input11name,
       "input11Value": input11Value,
       "input11LastErrMsg": input11LastErrMsg,
       "input12name": input12name,
       "input12Value": input12Value,
       "input12LastErrMsg": input12LastErrMsg,
       "input13name": input13name,
       "input13Value": input13Value,
       "input13LastErrMsg": input13LastErrMsg,
       "input14name": input14name,
       "input14Value": input14Value,
       "input14LastErrMsg": input14LastErrMsg,
       "input15name": input15name,
       "input15Value": input15Value,
       "input15LastErrMsg": input15LastErrMsg,
       "input16name": input16name,
       "input16Value": input16Value,
       "input16LastErrMsg": input16LastErrMsg,
       "output": output,
       "output1State": output1State,
       "output2State": output2State,
       "output3State": output3State,
       "output4State": output4State,
       "sensorTable": sensorTable,
       "sensor1": sensor1,
       "sensor1Name": sensor1Name,
       "sensor1value": sensor1value,
       "sensor1ErrState": sensor1ErrState,
       "sensor1lastErrTime": sensor1lastErrTime,
       "sensor1lastErrMsg": sensor1lastErrMsg,
       "sensor2": sensor2,
       "sensor2Name": sensor2Name,
       "sensor2value": sensor2value,
       "sensor2ErrState": sensor2ErrState,
       "sensor2lastErrTime": sensor2lastErrTime,
       "sensor2lastErrMsg": sensor2lastErrMsg,
       "sensor3": sensor3,
       "sensor3Name": sensor3Name,
       "sensor3value": sensor3value,
       "sensor3ErrState": sensor3ErrState,
       "sensor3lastErrTime": sensor3lastErrTime,
       "sensor3lastErrMsg": sensor3lastErrMsg,
       "sensor4": sensor4,
       "sensor4Name": sensor4Name,
       "sensor4value": sensor4value,
       "sensor4ErrState": sensor4ErrState,
       "sensor4lastErrTime": sensor4lastErrTime,
       "sensor4lastErrMsg": sensor4lastErrMsg,
       "sensor5": sensor5,
       "sensor5Name": sensor5Name,
       "sensor5value": sensor5value,
       "sensor5ErrState": sensor5ErrState,
       "sensor5lastErrTime": sensor5lastErrTime,
       "sensor5lastErrMsg": sensor5lastErrMsg,
       "sensor6": sensor6,
       "sensor6Name": sensor6Name,
       "sensor6value": sensor6value,
       "sensor6ErrState": sensor6ErrState,
       "sensor6lastErrTime": sensor6lastErrTime,
       "sensor6lastErrMsg": sensor6lastErrMsg,
       "sensor7": sensor7,
       "sensor7Name": sensor7Name,
       "sensor7value": sensor7value,
       "sensor7ErrState": sensor7ErrState,
       "sensor7lastErrTime": sensor7lastErrTime,
       "sensor7lastErrMsg": sensor7lastErrMsg,
       "sensor8": sensor8,
       "sensor8Name": sensor8Name,
       "sensor8value": sensor8value,
       "sensor8ErrState": sensor8ErrState,
       "sensor8lastErrTime": sensor8lastErrTime,
       "sensor8lastErrMsg": sensor8lastErrMsg,
       "sensor9": sensor9,
       "sensor9Name": sensor9Name,
       "sensor9value": sensor9value,
       "sensor9ErrState": sensor9ErrState,
       "sensor9lastErrTime": sensor9lastErrTime,
       "sensor9lastErrMsg": sensor9lastErrMsg,
       "sensor10": sensor10,
       "sensor10Name": sensor10Name,
       "sensor10value": sensor10value,
       "sensor10ErrState": sensor10ErrState,
       "sensor10lastErrTime": sensor10lastErrTime,
       "sensor10lastErrMsg": sensor10lastErrMsg,
       "sensor11": sensor11,
       "sensor11Name": sensor11Name,
       "sensor11value": sensor11value,
       "sensor11ErrState": sensor11ErrState,
       "sensor11lastErrTime": sensor11lastErrTime,
       "sensor11lastErrMsg": sensor11lastErrMsg,
       "sensor12": sensor12,
       "sensor12Name": sensor12Name,
       "sensor12value": sensor12value,
       "sensor12ErrState": sensor12ErrState,
       "sensor12lastErrTime": sensor12lastErrTime,
       "sensor12lastErrMsg": sensor12lastErrMsg,
       "sensor13": sensor13,
       "sensor13Name": sensor13Name,
       "sensor13value": sensor13value,
       "sensor13ErrState": sensor13ErrState,
       "sensor13lastErrTime": sensor13lastErrTime,
       "sensor13lastErrMsg": sensor13lastErrMsg,
       "sensor14": sensor14,
       "sensor14Name": sensor14Name,
       "sensor14value": sensor14value,
       "sensor14ErrState": sensor14ErrState,
       "sensor14lastErrTime": sensor14lastErrTime,
       "sensor14lastErrMsg": sensor14lastErrMsg,
       "sensor15": sensor15,
       "sensor15Name": sensor15Name,
       "sensor15value": sensor15value,
       "sensor15ErrState": sensor15ErrState,
       "sensor15lastErrTime": sensor15lastErrTime,
       "sensor15lastErrMsg": sensor15lastErrMsg,
       "sensor16": sensor16,
       "sensor16Name": sensor16Name,
       "sensor16value": sensor16value,
       "sensor16ErrState": sensor16ErrState,
       "sensor16lastErrTime": sensor16lastErrTime,
       "sensor16lastErrMsg": sensor16lastErrMsg,
       "sensor17": sensor17,
       "sensor17Name": sensor17Name,
       "sensor17value": sensor17value,
       "sensor17ErrState": sensor17ErrState,
       "sensor17lastErrTime": sensor17lastErrTime,
       "sensor17lastErrMsg": sensor17lastErrMsg,
       "sensor18": sensor18,
       "sensor18Name": sensor18Name,
       "sensor18value": sensor18value,
       "sensor18ErrState": sensor18ErrState,
       "sensor18lastErrTime": sensor18lastErrTime,
       "sensor18lastErrMsg": sensor18lastErrMsg,
       "sensor19": sensor19,
       "sensor19Name": sensor19Name,
       "sensor19value": sensor19value,
       "sensor19ErrState": sensor19ErrState,
       "sensor19lastErrTime": sensor19lastErrTime,
       "sensor19lastErrMsg": sensor19lastErrMsg,
       "sensor20": sensor20,
       "sensor20Name": sensor20Name,
       "sensor20value": sensor20value,
       "sensor20ErrState": sensor20ErrState,
       "sensor20lastErrTime": sensor20lastErrTime,
       "sensor20lastErrMsg": sensor20lastErrMsg,
       "sensor21": sensor21,
       "sensor21Name": sensor21Name,
       "sensor21value": sensor21value,
       "sensor21ErrState": sensor21ErrState,
       "sensor21lastErrTime": sensor21lastErrTime,
       "sensor21lastErrMsg": sensor21lastErrMsg,
       "sensor22": sensor22,
       "sensor22Name": sensor22Name,
       "sensor22value": sensor22value,
       "sensor22ErrState": sensor22ErrState,
       "sensor22lastErrTime": sensor22lastErrTime,
       "sensor22lastErrMsg": sensor22lastErrMsg,
       "sensor23": sensor23,
       "sensor23Name": sensor23Name,
       "sensor23value": sensor23value,
       "sensor23ErrState": sensor23ErrState,
       "sensor23lastErrTime": sensor23lastErrTime,
       "sensor23lastErrMsg": sensor23lastErrMsg,
       "sensor24": sensor24,
       "sensor24Name": sensor24Name,
       "sensor24value": sensor24value,
       "sensor24ErrState": sensor24ErrState,
       "sensor24lastErrTime": sensor24lastErrTime,
       "sensor24lastErrMsg": sensor24lastErrMsg,
       "sensor25": sensor25,
       "sensor25Name": sensor25Name,
       "sensor25value": sensor25value,
       "sensor25ErrState": sensor25ErrState,
       "sensor25lastErrTime": sensor25lastErrTime,
       "sensor25lastErrMsg": sensor25lastErrMsg,
       "sensor26": sensor26,
       "sensor26Name": sensor26Name,
       "sensor26value": sensor26value,
       "sensor26ErrState": sensor26ErrState,
       "sensor26lastErrTime": sensor26lastErrTime,
       "sensor26lastErrMsg": sensor26lastErrMsg,
       "sensor27": sensor27,
       "sensor27Name": sensor27Name,
       "sensor27value": sensor27value,
       "sensor27ErrState": sensor27ErrState,
       "sensor27lastErrTime": sensor27lastErrTime,
       "sensor27lastErrMsg": sensor27lastErrMsg,
       "sensor28": sensor28,
       "sensor28Name": sensor28Name,
       "sensor28value": sensor28value,
       "sensor28ErrState": sensor28ErrState,
       "sensor28lastErrTime": sensor28lastErrTime,
       "sensor28lastErrMsg": sensor28lastErrMsg,
       "sensor29": sensor29,
       "sensor29Name": sensor29Name,
       "sensor29value": sensor29value,
       "sensor29ErrState": sensor29ErrState,
       "sensor29lastErrTime": sensor29lastErrTime,
       "sensor29lastErrMsg": sensor29lastErrMsg,
       "sensor30": sensor30,
       "sensor30Name": sensor30Name,
       "sensor30value": sensor30value,
       "sensor30ErrState": sensor30ErrState,
       "sensor30lastErrTime": sensor30lastErrTime,
       "sensor30lastErrMsg": sensor30lastErrMsg,
       "sensor31": sensor31,
       "sensor31Name": sensor31Name,
       "sensor31value": sensor31value,
       "sensor31ErrState": sensor31ErrState,
       "sensor31lastErrTime": sensor31lastErrTime,
       "sensor31lastErrMsg": sensor31lastErrMsg,
       "sensor32": sensor32,
       "sensor32Name": sensor32Name,
       "sensor32value": sensor32value,
       "sensor32ErrState": sensor32ErrState,
       "sensor32lastErrTime": sensor32lastErrTime,
       "sensor32lastErrMsg": sensor32lastErrMsg,
       "daisySensorTable": daisySensorTable,
       "daisySensor1": daisySensor1,
       "daisySensor1Name": daisySensor1Name,
       "daisySensor1value": daisySensor1value,
       "daisySensor1ErrState": daisySensor1ErrState,
       "daisySensor1lastErrTime": daisySensor1lastErrTime,
       "daisySensor1lastErrMsg": daisySensor1lastErrMsg,
       "daisySensor2": daisySensor2,
       "daisySensor2Name": daisySensor2Name,
       "daisySensor2value": daisySensor2value,
       "daisySensor2ErrState": daisySensor2ErrState,
       "daisySensor2lastErrTime": daisySensor2lastErrTime,
       "daisySensor2lastErrMsg": daisySensor2lastErrMsg,
       "daisySensor3": daisySensor3,
       "daisySensor3Name": daisySensor3Name,
       "daisySensor3value": daisySensor3value,
       "daisySensor3ErrState": daisySensor3ErrState,
       "daisySensor3lastErrTime": daisySensor3lastErrTime,
       "daisySensor3lastErrMsg": daisySensor3lastErrMsg,
       "daisySensor4": daisySensor4,
       "daisySensor4Name": daisySensor4Name,
       "daisySensor4value": daisySensor4value,
       "daisySensor4ErrState": daisySensor4ErrState,
       "daisySensor4lastErrTime": daisySensor4lastErrTime,
       "daisySensor4lastErrMsg": daisySensor4lastErrMsg,
       "daisySensor5": daisySensor5,
       "daisySensor5Name": daisySensor5Name,
       "daisySensor5value": daisySensor5value,
       "daisySensor5ErrState": daisySensor5ErrState,
       "daisySensor5lastErrTime": daisySensor5lastErrTime,
       "daisySensor5lastErrMsg": daisySensor5lastErrMsg,
       "daisySensor6": daisySensor6,
       "daisySensor6Name": daisySensor6Name,
       "daisySensor6value": daisySensor6value,
       "daisySensor6ErrState": daisySensor6ErrState,
       "daisySensor6lastErrTime": daisySensor6lastErrTime,
       "daisySensor6lastErrMsg": daisySensor6lastErrMsg,
       "daisySensor7": daisySensor7,
       "daisySensor7Name": daisySensor7Name,
       "daisySensor7value": daisySensor7value,
       "daisySensor7ErrState": daisySensor7ErrState,
       "daisySensor7lastErrTime": daisySensor7lastErrTime,
       "daisySensor7lastErrMsg": daisySensor7lastErrMsg,
       "daisySensor8": daisySensor8,
       "daisySensor8Name": daisySensor8Name,
       "daisySensor8value": daisySensor8value,
       "daisySensor8ErrState": daisySensor8ErrState,
       "daisySensor8lastErrTime": daisySensor8lastErrTime,
       "daisySensor8lastErrMsg": daisySensor8lastErrMsg,
       "daisySensor9": daisySensor9,
       "daisySensor9Name": daisySensor9Name,
       "daisySensor9value": daisySensor9value,
       "daisySensor9ErrState": daisySensor9ErrState,
       "daisySensor9lastErrTime": daisySensor9lastErrTime,
       "daisySensor9lastErrMsg": daisySensor9lastErrMsg,
       "daisySensor10": daisySensor10,
       "daisySensor10Name": daisySensor10Name,
       "daisySensor10value": daisySensor10value,
       "daisySensor10ErrState": daisySensor10ErrState,
       "daisySensor10lastErrTime": daisySensor10lastErrTime,
       "daisySensor10lastErrMsg": daisySensor10lastErrMsg,
       "daisySensor11": daisySensor11,
       "daisySensor11Name": daisySensor11Name,
       "daisySensor11value": daisySensor11value,
       "daisySensor11ErrState": daisySensor11ErrState,
       "daisySensor11lastErrTime": daisySensor11lastErrTime,
       "daisySensor11lastErrMsg": daisySensor11lastErrMsg,
       "daisySensor12": daisySensor12,
       "daisySensor12Name": daisySensor12Name,
       "daisySensor12value": daisySensor12value,
       "daisySensor12ErrState": daisySensor12ErrState,
       "daisySensor12lastErrTime": daisySensor12lastErrTime,
       "daisySensor12lastErrMsg": daisySensor12lastErrMsg,
       "daisySensor13": daisySensor13,
       "daisySensor13Name": daisySensor13Name,
       "daisySensor13value": daisySensor13value,
       "daisySensor13ErrState": daisySensor13ErrState,
       "daisySensor13lastErrTime": daisySensor13lastErrTime,
       "daisySensor13lastErrMsg": daisySensor13lastErrMsg,
       "daisySensor14": daisySensor14,
       "daisySensor14Name": daisySensor14Name,
       "daisySensor14value": daisySensor14value,
       "daisySensor14ErrState": daisySensor14ErrState,
       "daisySensor14lastErrTime": daisySensor14lastErrTime,
       "daisySensor14lastErrMsg": daisySensor14lastErrMsg,
       "daisySensor15": daisySensor15,
       "daisySensor15Name": daisySensor15Name,
       "daisySensor15value": daisySensor15value,
       "daisySensor15ErrState": daisySensor15ErrState,
       "daisySensor15lastErrTime": daisySensor15lastErrTime,
       "daisySensor15lastErrMsg": daisySensor15lastErrMsg,
       "daisySensor16": daisySensor16,
       "daisySensor16Name": daisySensor16Name,
       "daisySensor16value": daisySensor16value,
       "daisySensor16ErrState": daisySensor16ErrState,
       "daisySensor16lastErrTime": daisySensor16lastErrTime,
       "daisySensor16lastErrMsg": daisySensor16lastErrMsg,
       "daisySensor17": daisySensor17,
       "daisySensor17Name": daisySensor17Name,
       "daisySensor17value": daisySensor17value,
       "daisySensor17ErrState": daisySensor17ErrState,
       "daisySensor17lastErrTime": daisySensor17lastErrTime,
       "daisySensor17lastErrMsg": daisySensor17lastErrMsg,
       "daisySensor18": daisySensor18,
       "daisySensor18Name": daisySensor18Name,
       "daisySensor18value": daisySensor18value,
       "daisySensor18ErrState": daisySensor18ErrState,
       "daisySensor18lastErrTime": daisySensor18lastErrTime,
       "daisySensor18lastErrMsg": daisySensor18lastErrMsg,
       "daisySensor19": daisySensor19,
       "daisySensor19Name": daisySensor19Name,
       "daisySensor19value": daisySensor19value,
       "daisySensor19ErrState": daisySensor19ErrState,
       "daisySensor19lastErrTime": daisySensor19lastErrTime,
       "daisySensor19lastErrMsg": daisySensor19lastErrMsg,
       "daisySensor20": daisySensor20,
       "daisySensor20Name": daisySensor20Name,
       "daisySensor20value": daisySensor20value,
       "daisySensor20ErrState": daisySensor20ErrState,
       "daisySensor20lastErrTime": daisySensor20lastErrTime,
       "daisySensor20lastErrMsg": daisySensor20lastErrMsg,
       "daisySensor21": daisySensor21,
       "daisySensor21Name": daisySensor21Name,
       "daisySensor21value": daisySensor21value,
       "daisySensor21ErrState": daisySensor21ErrState,
       "daisySensor21lastErrTime": daisySensor21lastErrTime,
       "daisySensor21lastErrMsg": daisySensor21lastErrMsg,
       "daisySensor22": daisySensor22,
       "daisySensor22Name": daisySensor22Name,
       "daisySensor22value": daisySensor22value,
       "daisySensor22ErrState": daisySensor22ErrState,
       "daisySensor22lastErrTime": daisySensor22lastErrTime,
       "daisySensor22lastErrMsg": daisySensor22lastErrMsg,
       "daisySensor23": daisySensor23,
       "daisySensor23Name": daisySensor23Name,
       "daisySensor23value": daisySensor23value,
       "daisySensor23ErrState": daisySensor23ErrState,
       "daisySensor23lastErrTime": daisySensor23lastErrTime,
       "daisySensor23lastErrMsg": daisySensor23lastErrMsg,
       "daisySensor24": daisySensor24,
       "daisySensor24Name": daisySensor24Name,
       "daisySensor24value": daisySensor24value,
       "daisySensor24ErrState": daisySensor24ErrState,
       "daisySensor24lastErrTime": daisySensor24lastErrTime,
       "daisySensor24lastErrMsg": daisySensor24lastErrMsg,
       "daisySensor25": daisySensor25,
       "daisySensor25Name": daisySensor25Name,
       "daisySensor25value": daisySensor25value,
       "daisySensor25ErrState": daisySensor25ErrState,
       "daisySensor25lastErrTime": daisySensor25lastErrTime,
       "daisySensor25lastErrMsg": daisySensor25lastErrMsg,
       "daisySensor26": daisySensor26,
       "daisySensor26Name": daisySensor26Name,
       "daisySensor26value": daisySensor26value,
       "daisySensor26ErrState": daisySensor26ErrState,
       "daisySensor26lastErrTime": daisySensor26lastErrTime,
       "daisySensor26lastErrMsg": daisySensor26lastErrMsg,
       "daisySensor27": daisySensor27,
       "daisySensor27Name": daisySensor27Name,
       "daisySensor27value": daisySensor27value,
       "daisySensor27ErrState": daisySensor27ErrState,
       "daisySensor27lastErrTime": daisySensor27lastErrTime,
       "daisySensor27lastErrMsg": daisySensor27lastErrMsg,
       "daisySensor28": daisySensor28,
       "daisySensor28Name": daisySensor28Name,
       "daisySensor28value": daisySensor28value,
       "daisySensor28ErrState": daisySensor28ErrState,
       "daisySensor28lastErrTime": daisySensor28lastErrTime,
       "daisySensor28lastErrMsg": daisySensor28lastErrMsg,
       "daisySensor29": daisySensor29,
       "daisySensor29Name": daisySensor29Name,
       "daisySensor29value": daisySensor29value,
       "daisySensor29ErrState": daisySensor29ErrState,
       "daisySensor29lastErrTime": daisySensor29lastErrTime,
       "daisySensor29lastErrMsg": daisySensor29lastErrMsg,
       "daisySensor30": daisySensor30,
       "daisySensor30Name": daisySensor30Name,
       "daisySensor30value": daisySensor30value,
       "daisySensor30ErrState": daisySensor30ErrState,
       "daisySensor30lastErrTime": daisySensor30lastErrTime,
       "daisySensor30lastErrMsg": daisySensor30lastErrMsg,
       "daisySensor31": daisySensor31,
       "daisySensor31Name": daisySensor31Name,
       "daisySensor31value": daisySensor31value,
       "daisySensor31ErrState": daisySensor31ErrState,
       "daisySensor31lastErrTime": daisySensor31lastErrTime,
       "daisySensor31lastErrMsg": daisySensor31lastErrMsg,
       "daisySensor32": daisySensor32,
       "daisySensor32Name": daisySensor32Name,
       "daisySensor32value": daisySensor32value,
       "daisySensor32ErrState": daisySensor32ErrState,
       "daisySensor32lastErrTime": daisySensor32lastErrTime,
       "daisySensor32lastErrMsg": daisySensor32lastErrMsg}
)
