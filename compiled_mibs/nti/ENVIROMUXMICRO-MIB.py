# SNMP MIB module (ENVIROMUXMICRO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nti\ENVIROMUXMICRO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:08 2025
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

enviromuxMicro = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12)
)
if mibBuilder.loadTexts:
    enviromuxMicro.setRevisions(
        ("2021-03-07 14:00",
         "2015-09-27 14:00",
         "2015-02-23 14:00",
         "2014-11-25 14:00",
         "2014-11-14 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nti_ObjectIdentity = ObjectIdentity
nti = _Nti_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699)
)
_Products_ObjectIdentity = ObjectIdentity
products = _Products_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1)
)
_Hardware_ObjectIdentity = ObjectIdentity
hardware = _Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1)
)
_MasterUnit_ObjectIdentity = ObjectIdentity
masterUnit = _MasterUnit_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1)
)
_IntSensors_ObjectIdentity = ObjectIdentity
intSensors = _IntSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 1)
)
_IntSensorTable_Object = MibTable
intSensorTable = _IntSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 1, 1)
)
if mibBuilder.loadTexts:
    intSensorTable.setStatus("current")
_IntSensorEntry_Object = MibTableRow
intSensorEntry = _IntSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 1, 1, 1)
)
intSensorEntry.setIndexNames(
    (0, "ENVIROMUXMICRO-MIB", "intSensorIndex"),
)
if mibBuilder.loadTexts:
    intSensorEntry.setStatus("current")


class _IntSensorIndex_Type(Integer32):
    """Custom type intSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IntSensorIndex_Type.__name__ = "Integer32"
_IntSensorIndex_Object = MibTableColumn
intSensorIndex = _IntSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 1, 1, 1, 1),
    _IntSensorIndex_Type()
)
intSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    intSensorIndex.setStatus("current")


class _IntSensorType_Type(Integer32):
    """Custom type intSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              24)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("temperature", 1),
          ("humidity", 2),
          ("dewPoint", 24))
    )


_IntSensorType_Type.__name__ = "Integer32"
_IntSensorType_Object = MibTableColumn
intSensorType = _IntSensorType_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 1, 1, 1, 2),
    _IntSensorType_Type()
)
intSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSensorType.setStatus("current")
_IntSensorDescription_Type = DisplayString
_IntSensorDescription_Object = MibTableColumn
intSensorDescription = _IntSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 1, 1, 1, 3),
    _IntSensorDescription_Type()
)
intSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSensorDescription.setStatus("current")
_IntSensorValue_Type = Integer32
_IntSensorValue_Object = MibTableColumn
intSensorValue = _IntSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 1, 1, 1, 4),
    _IntSensorValue_Type()
)
intSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSensorValue.setStatus("current")


class _IntSensorUnit_Type(Integer32):
    """Custom type intSensorUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_IntSensorUnit_Type.__name__ = "Integer32"
_IntSensorUnit_Object = MibTableColumn
intSensorUnit = _IntSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 1, 1, 1, 5),
    _IntSensorUnit_Type()
)
intSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    intSensorUnit.setStatus("current")
_ExtSensors_ObjectIdentity = ObjectIdentity
extSensors = _ExtSensors_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2)
)
_ExtSensorTable_Object = MibTable
extSensorTable = _ExtSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    extSensorTable.setStatus("current")
_ExtSensorEntry_Object = MibTableRow
extSensorEntry = _ExtSensorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1)
)
extSensorEntry.setIndexNames(
    (0, "ENVIROMUXMICRO-MIB", "extSensorIndex"),
)
if mibBuilder.loadTexts:
    extSensorEntry.setStatus("current")


class _ExtSensorIndex_Type(Integer32):
    """Custom type extSensorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_ExtSensorIndex_Type.__name__ = "Integer32"
_ExtSensorIndex_Object = MibTableColumn
extSensorIndex = _ExtSensorIndex_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 1),
    _ExtSensorIndex_Type()
)
extSensorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    extSensorIndex.setStatus("current")


class _ExtSensorType_Type(Integer32):
    """Custom type extSensorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              24)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("temperature", 1),
          ("humidity", 2),
          ("dewPoint", 24))
    )


_ExtSensorType_Type.__name__ = "Integer32"
_ExtSensorType_Object = MibTableColumn
extSensorType = _ExtSensorType_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 2),
    _ExtSensorType_Type()
)
extSensorType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extSensorType.setStatus("current")
_ExtSensorDescription_Type = DisplayString
_ExtSensorDescription_Object = MibTableColumn
extSensorDescription = _ExtSensorDescription_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 3),
    _ExtSensorDescription_Type()
)
extSensorDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extSensorDescription.setStatus("current")
_ExtSensorValue_Type = Integer32
_ExtSensorValue_Object = MibTableColumn
extSensorValue = _ExtSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 4),
    _ExtSensorValue_Type()
)
extSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extSensorValue.setStatus("current")


class _ExtSensorUnit_Type(Integer32):
    """Custom type extSensorUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ExtSensorUnit_Type.__name__ = "Integer32"
_ExtSensorUnit_Object = MibTableColumn
extSensorUnit = _ExtSensorUnit_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 2, 1, 1, 5),
    _ExtSensorUnit_Type()
)
extSensorUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    extSensorUnit.setStatus("current")
_DigInputs_ObjectIdentity = ObjectIdentity
digInputs = _DigInputs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3)
)
_DigInputTable_Object = MibTable
digInputTable = _DigInputTable_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1)
)
if mibBuilder.loadTexts:
    digInputTable.setStatus("current")
_DigInputEntry_Object = MibTableRow
digInputEntry = _DigInputEntry_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1)
)
digInputEntry.setIndexNames(
    (0, "ENVIROMUXMICRO-MIB", "digInputIndex"),
)
if mibBuilder.loadTexts:
    digInputEntry.setStatus("current")


class _DigInputIndex_Type(Integer32):
    """Custom type digInputIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DigInputIndex_Type.__name__ = "Integer32"
_DigInputIndex_Object = MibTableColumn
digInputIndex = _DigInputIndex_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1, 1),
    _DigInputIndex_Type()
)
digInputIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    digInputIndex.setStatus("current")
_DigInputDescription_Type = DisplayString
_DigInputDescription_Object = MibTableColumn
digInputDescription = _DigInputDescription_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1, 2),
    _DigInputDescription_Type()
)
digInputDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digInputDescription.setStatus("current")


class _DigInputValue_Type(Integer32):
    """Custom type digInputValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("closed", 0),
          ("open", 1))
    )


_DigInputValue_Type.__name__ = "Integer32"
_DigInputValue_Object = MibTableColumn
digInputValue = _DigInputValue_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 3, 1, 1, 3),
    _DigInputValue_Type()
)
digInputValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    digInputValue.setStatus("current")
_IpDevices_ObjectIdentity = ObjectIdentity
ipDevices = _IpDevices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4)
)
_IpDeviceTable_Object = MibTable
ipDeviceTable = _IpDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipDeviceTable.setStatus("current")
_IpDeviceEntry_Object = MibTableRow
ipDeviceEntry = _IpDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1)
)
ipDeviceEntry.setIndexNames(
    (0, "ENVIROMUXMICRO-MIB", "ipDeviceIndex"),
)
if mibBuilder.loadTexts:
    ipDeviceEntry.setStatus("current")


class _IpDeviceIndex_Type(Integer32):
    """Custom type ipDeviceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_IpDeviceIndex_Type.__name__ = "Integer32"
_IpDeviceIndex_Object = MibTableColumn
ipDeviceIndex = _IpDeviceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1, 1),
    _IpDeviceIndex_Type()
)
ipDeviceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipDeviceIndex.setStatus("current")
_IpDeviceDescription_Type = DisplayString
_IpDeviceDescription_Object = MibTableColumn
ipDeviceDescription = _IpDeviceDescription_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1, 2),
    _IpDeviceDescription_Type()
)
ipDeviceDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDeviceDescription.setStatus("current")


class _IpDeviceValue_Type(Integer32):
    """Custom type ipDeviceValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notResponding", 0),
          ("responding", 1))
    )


_IpDeviceValue_Type.__name__ = "Integer32"
_IpDeviceValue_Object = MibTableColumn
ipDeviceValue = _IpDeviceValue_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 4, 1, 1, 3),
    _IpDeviceValue_Type()
)
ipDeviceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipDeviceValue.setStatus("current")
_EAlerts_ObjectIdentity = ObjectIdentity
eAlerts = _EAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5)
)
_AlertTable_Object = MibTable
alertTable = _AlertTable_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1)
)
if mibBuilder.loadTexts:
    alertTable.setStatus("current")
_AlertEntry_Object = MibTableRow
alertEntry = _AlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1)
)
alertEntry.setIndexNames(
    (0, "ENVIROMUXMICRO-MIB", "alertIndex"),
)
if mibBuilder.loadTexts:
    alertEntry.setStatus("current")


class _AlertIndex_Type(Integer32):
    """Custom type alertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AlertIndex_Type.__name__ = "Integer32"
_AlertIndex_Object = MibTableColumn
alertIndex = _AlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 1),
    _AlertIndex_Type()
)
alertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alertIndex.setStatus("current")


class _AlertEnabled_Type(Integer32):
    """Custom type alertEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_AlertEnabled_Type.__name__ = "Integer32"
_AlertEnabled_Object = MibTableColumn
alertEnabled = _AlertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 2),
    _AlertEnabled_Type()
)
alertEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertEnabled.setStatus("current")
_AlertSensor_Type = DisplayString
_AlertSensor_Object = MibTableColumn
alertSensor = _AlertSensor_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 3),
    _AlertSensor_Type()
)
alertSensor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSensor.setStatus("current")
_AlertSensorValue_Type = Integer32
_AlertSensorValue_Object = MibTableColumn
alertSensorValue = _AlertSensorValue_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 4),
    _AlertSensorValue_Type()
)
alertSensorValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertSensorValue.setStatus("current")
_AlertThreshold_Type = Integer32
_AlertThreshold_Object = MibTableColumn
alertThreshold = _AlertThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 5),
    _AlertThreshold_Type()
)
alertThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertThreshold.setStatus("current")


class _AlertThresholdType_Type(Integer32):
    """Custom type alertThresholdType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("lessThan", 0),
          ("greaterThan", 1))
    )


_AlertThresholdType_Type.__name__ = "Integer32"
_AlertThresholdType_Object = MibTableColumn
alertThresholdType = _AlertThresholdType_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 6),
    _AlertThresholdType_Type()
)
alertThresholdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertThresholdType.setStatus("current")


class _AlertStatus_Type(Integer32):
    """Custom type alertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("enteringCritical", 1),
          ("critical", 2),
          ("exitingCritical", 3),
          ("waitingAckDismiss", 4),
          ("acknowledged", 5),
          ("dismissed", 6),
          ("disconnected", 7))
    )


_AlertStatus_Type.__name__ = "Integer32"
_AlertStatus_Object = MibTableColumn
alertStatus = _AlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 5, 1, 1, 7),
    _AlertStatus_Type()
)
alertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alertStatus.setStatus("current")
_SmAlerts_ObjectIdentity = ObjectIdentity
smAlerts = _SmAlerts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6)
)
_SmAlertTable_Object = MibTable
smAlertTable = _SmAlertTable_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1)
)
if mibBuilder.loadTexts:
    smAlertTable.setStatus("current")
_SmAlertEntry_Object = MibTableRow
smAlertEntry = _SmAlertEntry_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1)
)
smAlertEntry.setIndexNames(
    (0, "ENVIROMUXMICRO-MIB", "smAlertIndex"),
)
if mibBuilder.loadTexts:
    smAlertEntry.setStatus("current")


class _SmAlertIndex_Type(Integer32):
    """Custom type smAlertIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_SmAlertIndex_Type.__name__ = "Integer32"
_SmAlertIndex_Object = MibTableColumn
smAlertIndex = _SmAlertIndex_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1, 1),
    _SmAlertIndex_Type()
)
smAlertIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smAlertIndex.setStatus("current")


class _SmAlertEnabled_Type(Integer32):
    """Custom type smAlertEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_SmAlertEnabled_Type.__name__ = "Integer32"
_SmAlertEnabled_Object = MibTableColumn
smAlertEnabled = _SmAlertEnabled_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1, 2),
    _SmAlertEnabled_Type()
)
smAlertEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smAlertEnabled.setStatus("current")


class _SmAlertStatus_Type(Integer32):
    """Custom type smAlertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("enteringCritical", 1),
          ("critical", 2),
          ("exitingCritical", 3),
          ("waitingAckDismiss", 4),
          ("acknowledged", 5),
          ("dismissed", 6),
          ("disconnected", 7))
    )


_SmAlertStatus_Type.__name__ = "Integer32"
_SmAlertStatus_Object = MibTableColumn
smAlertStatus = _SmAlertStatus_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 6, 1, 1, 3),
    _SmAlertStatus_Type()
)
smAlertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smAlertStatus.setStatus("current")
_HostSystem_ObjectIdentity = ObjectIdentity
hostSystem = _HostSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 100)
)
_UnitName_Type = DisplayString
_UnitName_Object = MibScalar
unitName = _UnitName_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 100, 1),
    _UnitName_Type()
)
unitName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    unitName.setStatus("current")
_DeviceModel_Type = DisplayString
_DeviceModel_Object = MibScalar
deviceModel = _DeviceModel_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 100, 2),
    _DeviceModel_Type()
)
deviceModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    deviceModel.setStatus("current")
_SerialNumber_Type = DisplayString
_SerialNumber_Object = MibScalar
serialNumber = _SerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 100, 3),
    _SerialNumber_Type()
)
serialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialNumber.setStatus("current")
_FirmwareRevision_Type = DisplayString
_FirmwareRevision_Object = MibScalar
firmwareRevision = _FirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 100, 4),
    _FirmwareRevision_Type()
)
firmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    firmwareRevision.setStatus("current")
_SenderEmailAddress_Type = DisplayString
_SenderEmailAddress_Object = MibScalar
senderEmailAddress = _SenderEmailAddress_Object(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 1, 100, 5),
    _SenderEmailAddress_Type()
)
senderEmailAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    senderEmailAddress.setStatus("current")
_EnviromuxMicroTraps_ObjectIdentity = ObjectIdentity
enviromuxMicroTraps = _EnviromuxMicroTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100)
)
_IntSensorsTraps_ObjectIdentity = ObjectIdentity
intSensorsTraps = _IntSensorsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 1)
)
_ExtSensorsTraps_ObjectIdentity = ObjectIdentity
extSensorsTraps = _ExtSensorsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2)
)
_DigitalInputsTraps_ObjectIdentity = ObjectIdentity
digitalInputsTraps = _DigitalInputsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 3)
)
_IpDevicesTraps_ObjectIdentity = ObjectIdentity
ipDevicesTraps = _IpDevicesTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4)
)
_OtherProduct_ObjectIdentity = ObjectIdentity
otherProduct = _OtherProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 200)
)
_Software_ObjectIdentity = ObjectIdentity
software = _Software_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3699, 1, 2)
)

# Managed Objects groups


# Notification objects

intSensor1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 1, 1)
)
intSensor1Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "intSensorValue"),
        ("ENVIROMUXMICRO-MIB", "intSensorUnit"))
)
if mibBuilder.loadTexts:
    intSensor1Trap.setStatus(
        "current"
    )

intSensor2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 1, 2)
)
intSensor2Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "intSensorValue"),
        ("ENVIROMUXMICRO-MIB", "intSensorUnit"))
)
if mibBuilder.loadTexts:
    intSensor2Trap.setStatus(
        "current"
    )

intSensor3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 1, 3)
)
intSensor3Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "intSensorValue"),
        ("ENVIROMUXMICRO-MIB", "intSensorUnit"))
)
if mibBuilder.loadTexts:
    intSensor3Trap.setStatus(
        "current"
    )

extSensor1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 1)
)
extSensor1Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "extSensorValue"),
        ("ENVIROMUXMICRO-MIB", "extSensorUnit"))
)
if mibBuilder.loadTexts:
    extSensor1Trap.setStatus(
        "current"
    )

extSensor2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 2)
)
extSensor2Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "extSensorValue"),
        ("ENVIROMUXMICRO-MIB", "extSensorUnit"))
)
if mibBuilder.loadTexts:
    extSensor2Trap.setStatus(
        "current"
    )

extSensor3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 3)
)
extSensor3Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "extSensorValue"),
        ("ENVIROMUXMICRO-MIB", "extSensorUnit"))
)
if mibBuilder.loadTexts:
    extSensor3Trap.setStatus(
        "current"
    )

extSensor4Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 4)
)
extSensor4Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "extSensorValue"),
        ("ENVIROMUXMICRO-MIB", "extSensorUnit"))
)
if mibBuilder.loadTexts:
    extSensor4Trap.setStatus(
        "current"
    )

extSensor5Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 5)
)
extSensor5Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "extSensorValue"),
        ("ENVIROMUXMICRO-MIB", "extSensorUnit"))
)
if mibBuilder.loadTexts:
    extSensor5Trap.setStatus(
        "current"
    )

extSensor6Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 2, 6)
)
extSensor6Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "extSensorValue"),
        ("ENVIROMUXMICRO-MIB", "extSensorUnit"))
)
if mibBuilder.loadTexts:
    extSensor6Trap.setStatus(
        "current"
    )

digInput1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 3, 1)
)
digInput1Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "digInputValue"))
)
if mibBuilder.loadTexts:
    digInput1Trap.setStatus(
        "current"
    )

digInpu21Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 3, 2)
)
digInpu21Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "digInputValue"))
)
if mibBuilder.loadTexts:
    digInpu21Trap.setStatus(
        "current"
    )

ipDevice1Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 1)
)
ipDevice1Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "ipDeviceValue"))
)
if mibBuilder.loadTexts:
    ipDevice1Trap.setStatus(
        "current"
    )

ipDevice2Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 2)
)
ipDevice2Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "ipDeviceValue"))
)
if mibBuilder.loadTexts:
    ipDevice2Trap.setStatus(
        "current"
    )

ipDevice3Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 3)
)
ipDevice3Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "ipDeviceValue"))
)
if mibBuilder.loadTexts:
    ipDevice3Trap.setStatus(
        "current"
    )

ipDevice4Trap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3699, 1, 1, 12, 100, 4, 4)
)
ipDevice4Trap.setObjects(
      *(("ENVIROMUXMICRO-MIB", "alertStatus"),
        ("ENVIROMUXMICRO-MIB", "ipDeviceValue"))
)
if mibBuilder.loadTexts:
    ipDevice4Trap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENVIROMUXMICRO-MIB",
    **{"nti": nti,
       "products": products,
       "hardware": hardware,
       "enviromuxMicro": enviromuxMicro,
       "masterUnit": masterUnit,
       "intSensors": intSensors,
       "intSensorTable": intSensorTable,
       "intSensorEntry": intSensorEntry,
       "intSensorIndex": intSensorIndex,
       "intSensorType": intSensorType,
       "intSensorDescription": intSensorDescription,
       "intSensorValue": intSensorValue,
       "intSensorUnit": intSensorUnit,
       "extSensors": extSensors,
       "extSensorTable": extSensorTable,
       "extSensorEntry": extSensorEntry,
       "extSensorIndex": extSensorIndex,
       "extSensorType": extSensorType,
       "extSensorDescription": extSensorDescription,
       "extSensorValue": extSensorValue,
       "extSensorUnit": extSensorUnit,
       "digInputs": digInputs,
       "digInputTable": digInputTable,
       "digInputEntry": digInputEntry,
       "digInputIndex": digInputIndex,
       "digInputDescription": digInputDescription,
       "digInputValue": digInputValue,
       "ipDevices": ipDevices,
       "ipDeviceTable": ipDeviceTable,
       "ipDeviceEntry": ipDeviceEntry,
       "ipDeviceIndex": ipDeviceIndex,
       "ipDeviceDescription": ipDeviceDescription,
       "ipDeviceValue": ipDeviceValue,
       "eAlerts": eAlerts,
       "alertTable": alertTable,
       "alertEntry": alertEntry,
       "alertIndex": alertIndex,
       "alertEnabled": alertEnabled,
       "alertSensor": alertSensor,
       "alertSensorValue": alertSensorValue,
       "alertThreshold": alertThreshold,
       "alertThresholdType": alertThresholdType,
       "alertStatus": alertStatus,
       "smAlerts": smAlerts,
       "smAlertTable": smAlertTable,
       "smAlertEntry": smAlertEntry,
       "smAlertIndex": smAlertIndex,
       "smAlertEnabled": smAlertEnabled,
       "smAlertStatus": smAlertStatus,
       "hostSystem": hostSystem,
       "unitName": unitName,
       "deviceModel": deviceModel,
       "serialNumber": serialNumber,
       "firmwareRevision": firmwareRevision,
       "senderEmailAddress": senderEmailAddress,
       "enviromuxMicroTraps": enviromuxMicroTraps,
       "intSensorsTraps": intSensorsTraps,
       "intSensor1Trap": intSensor1Trap,
       "intSensor2Trap": intSensor2Trap,
       "intSensor3Trap": intSensor3Trap,
       "extSensorsTraps": extSensorsTraps,
       "extSensor1Trap": extSensor1Trap,
       "extSensor2Trap": extSensor2Trap,
       "extSensor3Trap": extSensor3Trap,
       "extSensor4Trap": extSensor4Trap,
       "extSensor5Trap": extSensor5Trap,
       "extSensor6Trap": extSensor6Trap,
       "digitalInputsTraps": digitalInputsTraps,
       "digInput1Trap": digInput1Trap,
       "digInpu21Trap": digInpu21Trap,
       "ipDevicesTraps": ipDevicesTraps,
       "ipDevice1Trap": ipDevice1Trap,
       "ipDevice2Trap": ipDevice2Trap,
       "ipDevice3Trap": ipDevice3Trap,
       "ipDevice4Trap": ipDevice4Trap,
       "otherProduct": otherProduct,
       "software": software}
)
