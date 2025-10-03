# SNMP MIB module (CIENA-WS-BLADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ciena\CIENA-WS-BLADE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:25:03 2025
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

(cienaWsConfig,) = mibBuilder.importSymbols(
    "CIENA-WS-MIB",
    "cienaWsConfig")

(MacString,
 ModuleTypeEnum,
 StringMaxl32,
 StringMaxl64) = mibBuilder.importSymbols(
    "CIENA-WS-TYPEDEFS-MIB",
    "MacString",
    "ModuleTypeEnum",
    "StringMaxl32",
    "StringMaxl64")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

cienaWsBladeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5)
)
if mibBuilder.loadTexts:
    cienaWsBladeMIB.setRevisions(
        ("2017-02-28 00:00",
         "2016-12-12 00:00",
         "2016-06-12 00:00",
         "2016-04-06 00:00",
         "2015-07-25 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DeviceTypeBit(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("pluggable", 0),
          ("fixed", 1))
    )


# MIB Managed Objects in the order of their OIDs

_CienaWsBladeObjects_ObjectIdentity = ObjectIdentity
cienaWsBladeObjects = _CienaWsBladeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 1)
)
_CienaWsBladeConformance_ObjectIdentity = ObjectIdentity
cienaWsBladeConformance = _CienaWsBladeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 2)
)
_CienaWsBladeGroups_ObjectIdentity = ObjectIdentity
cienaWsBladeGroups = _CienaWsBladeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 2, 1)
)
_CienaWsBladeCompliances_ObjectIdentity = ObjectIdentity
cienaWsBladeCompliances = _CienaWsBladeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 2, 2)
)
_CwsBladeBladeidentificationTable_Object = MibTable
cwsBladeBladeidentificationTable = _CwsBladeBladeidentificationTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3)
)
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationTable.setStatus("current")
_CwsBladeBladeidentificationEntry_Object = MibTableRow
cwsBladeBladeidentificationEntry = _CwsBladeBladeidentificationEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3, 1)
)
cwsBladeBladeidentificationEntry.setIndexNames(
    (0, "CIENA-WS-BLADE-MIB", "cwsBladeBladeidentificationTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationEntry.setStatus("current")


class _CwsBladeBladeidentificationTableSnmpKey_Type(Integer32):
    """Custom type cwsBladeBladeidentificationTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsBladeBladeidentificationTableSnmpKey_Type.__name__ = "Integer32"
_CwsBladeBladeidentificationTableSnmpKey_Object = MibTableColumn
cwsBladeBladeidentificationTableSnmpKey = _CwsBladeBladeidentificationTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3, 1, 1),
    _CwsBladeBladeidentificationTableSnmpKey_Type()
)
cwsBladeBladeidentificationTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationTableSnmpKey.setStatus("current")
_CwsBladeBladeidentificationName_Type = StringMaxl32
_CwsBladeBladeidentificationName_Object = MibTableColumn
cwsBladeBladeidentificationName = _CwsBladeBladeidentificationName_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3, 1, 2),
    _CwsBladeBladeidentificationName_Type()
)
cwsBladeBladeidentificationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationName.setStatus("current")
_CwsBladeBladeidentificationModel_Type = StringMaxl32
_CwsBladeBladeidentificationModel_Object = MibTableColumn
cwsBladeBladeidentificationModel = _CwsBladeBladeidentificationModel_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3, 1, 3),
    _CwsBladeBladeidentificationModel_Type()
)
cwsBladeBladeidentificationModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationModel.setStatus("current")
_CwsBladeBladeidentificationDescription_Type = StringMaxl64
_CwsBladeBladeidentificationDescription_Object = MibTableColumn
cwsBladeBladeidentificationDescription = _CwsBladeBladeidentificationDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3, 1, 4),
    _CwsBladeBladeidentificationDescription_Type()
)
cwsBladeBladeidentificationDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationDescription.setStatus("current")
_CwsBladeBladeidentificationType_Type = Unsigned32
_CwsBladeBladeidentificationType_Object = MibTableColumn
cwsBladeBladeidentificationType = _CwsBladeBladeidentificationType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3, 1, 5),
    _CwsBladeBladeidentificationType_Type()
)
cwsBladeBladeidentificationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationType.setStatus("current")


class _CwsBladeBladeidentificationUserDescription_Type(OctetString):
    """Custom type cwsBladeBladeidentificationUserDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 130),
    )


_CwsBladeBladeidentificationUserDescription_Type.__name__ = "OctetString"
_CwsBladeBladeidentificationUserDescription_Object = MibTableColumn
cwsBladeBladeidentificationUserDescription = _CwsBladeBladeidentificationUserDescription_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3, 1, 6),
    _CwsBladeBladeidentificationUserDescription_Type()
)
cwsBladeBladeidentificationUserDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationUserDescription.setStatus("current")
_CwsBladeBladeidentificationBasemacaddress_Type = MacString
_CwsBladeBladeidentificationBasemacaddress_Object = MibTableColumn
cwsBladeBladeidentificationBasemacaddress = _CwsBladeBladeidentificationBasemacaddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3, 1, 7),
    _CwsBladeBladeidentificationBasemacaddress_Type()
)
cwsBladeBladeidentificationBasemacaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationBasemacaddress.setStatus("current")
_CwsBladeBladeidentificationPortbasemacaddress_Type = MacString
_CwsBladeBladeidentificationPortbasemacaddress_Object = MibTableColumn
cwsBladeBladeidentificationPortbasemacaddress = _CwsBladeBladeidentificationPortbasemacaddress_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 3, 1, 8),
    _CwsBladeBladeidentificationPortbasemacaddress_Type()
)
cwsBladeBladeidentificationPortbasemacaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladeidentificationPortbasemacaddress.setStatus("current")
_CwsBladeBladestateTable_Object = MibTable
cwsBladeBladestateTable = _CwsBladeBladestateTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 4)
)
if mibBuilder.loadTexts:
    cwsBladeBladestateTable.setStatus("current")
_CwsBladeBladestateEntry_Object = MibTableRow
cwsBladeBladestateEntry = _CwsBladeBladestateEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 4, 1)
)
cwsBladeBladestateEntry.setIndexNames(
    (0, "CIENA-WS-BLADE-MIB", "cwsBladeBladestateTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsBladeBladestateEntry.setStatus("current")


class _CwsBladeBladestateTableSnmpKey_Type(Integer32):
    """Custom type cwsBladeBladestateTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsBladeBladestateTableSnmpKey_Type.__name__ = "Integer32"
_CwsBladeBladestateTableSnmpKey_Object = MibTableColumn
cwsBladeBladestateTableSnmpKey = _CwsBladeBladestateTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 4, 1, 1),
    _CwsBladeBladestateTableSnmpKey_Type()
)
cwsBladeBladestateTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsBladeBladestateTableSnmpKey.setStatus("current")


class _CwsBladeBladestateAdminState_Type(Integer32):
    """Custom type cwsBladeBladestateAdminState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 0),
          ("disabled", 1),
          ("shutdown", 2))
    )


_CwsBladeBladestateAdminState_Type.__name__ = "Integer32"
_CwsBladeBladestateAdminState_Object = MibTableColumn
cwsBladeBladestateAdminState = _CwsBladeBladestateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 4, 1, 2),
    _CwsBladeBladestateAdminState_Type()
)
cwsBladeBladestateAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cwsBladeBladestateAdminState.setStatus("current")


class _CwsBladeBladestateOperationalState_Type(Integer32):
    """Custom type cwsBladeBladestateOperationalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 0),
          ("down", 1),
          ("faulted", 2),
          ("lowpowermode", 3))
    )


_CwsBladeBladestateOperationalState_Type.__name__ = "Integer32"
_CwsBladeBladestateOperationalState_Object = MibTableColumn
cwsBladeBladestateOperationalState = _CwsBladeBladestateOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 4, 1, 3),
    _CwsBladeBladestateOperationalState_Type()
)
cwsBladeBladestateOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladestateOperationalState.setStatus("current")
_CwsBladeBladestateLastRestart_Type = StringMaxl32
_CwsBladeBladestateLastRestart_Object = MibTableColumn
cwsBladeBladestateLastRestart = _CwsBladeBladestateLastRestart_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 4, 1, 4),
    _CwsBladeBladestateLastRestart_Type()
)
cwsBladeBladestateLastRestart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladestateLastRestart.setStatus("current")


class _CwsBladeBladestateLastRestartReason_Type(Integer32):
    """Custom type cwsBladeBladestateLastRestartReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("userwarm", 0),
          ("usercold", 1),
          ("systemwarm", 2),
          ("systemcold", 3),
          ("poweron", 4))
    )


_CwsBladeBladestateLastRestartReason_Type.__name__ = "Integer32"
_CwsBladeBladestateLastRestartReason_Object = MibTableColumn
cwsBladeBladestateLastRestartReason = _CwsBladeBladestateLastRestartReason_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 4, 1, 5),
    _CwsBladeBladestateLastRestartReason_Type()
)
cwsBladeBladestateLastRestartReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladestateLastRestartReason.setStatus("current")
_CwsBladeBladestateUptime_Type = StringMaxl32
_CwsBladeBladestateUptime_Object = MibTableColumn
cwsBladeBladestateUptime = _CwsBladeBladestateUptime_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 4, 1, 6),
    _CwsBladeBladestateUptime_Type()
)
cwsBladeBladestateUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladestateUptime.setStatus("current")
_CwsBladeBladecapabilitiesTable_Object = MibTable
cwsBladeBladecapabilitiesTable = _CwsBladeBladecapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 5)
)
if mibBuilder.loadTexts:
    cwsBladeBladecapabilitiesTable.setStatus("current")
_CwsBladeBladecapabilitiesEntry_Object = MibTableRow
cwsBladeBladecapabilitiesEntry = _CwsBladeBladecapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 5, 1)
)
cwsBladeBladecapabilitiesEntry.setIndexNames(
    (0, "CIENA-WS-BLADE-MIB", "cwsBladeBladecapabilitiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsBladeBladecapabilitiesEntry.setStatus("current")


class _CwsBladeBladecapabilitiesTableSnmpKey_Type(Integer32):
    """Custom type cwsBladeBladecapabilitiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsBladeBladecapabilitiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsBladeBladecapabilitiesTableSnmpKey_Object = MibTableColumn
cwsBladeBladecapabilitiesTableSnmpKey = _CwsBladeBladecapabilitiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 5, 1, 1),
    _CwsBladeBladecapabilitiesTableSnmpKey_Type()
)
cwsBladeBladecapabilitiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsBladeBladecapabilitiesTableSnmpKey.setStatus("current")
_CwsBladeBladecapabilitiesModuleType_Type = ModuleTypeEnum
_CwsBladeBladecapabilitiesModuleType_Object = MibTableColumn
cwsBladeBladecapabilitiesModuleType = _CwsBladeBladecapabilitiesModuleType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 5, 1, 2),
    _CwsBladeBladecapabilitiesModuleType_Type()
)
cwsBladeBladecapabilitiesModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladecapabilitiesModuleType.setStatus("current")
_CwsBladeBladecapabilitiesNumOfPorts_Type = Unsigned32
_CwsBladeBladecapabilitiesNumOfPorts_Object = MibTableColumn
cwsBladeBladecapabilitiesNumOfPorts = _CwsBladeBladecapabilitiesNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 5, 1, 3),
    _CwsBladeBladecapabilitiesNumOfPorts_Type()
)
cwsBladeBladecapabilitiesNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladecapabilitiesNumOfPorts.setStatus("current")
_CwsBladeBladecapabilitiesNumOfChannels_Type = Unsigned32
_CwsBladeBladecapabilitiesNumOfChannels_Object = MibTableColumn
cwsBladeBladecapabilitiesNumOfChannels = _CwsBladeBladecapabilitiesNumOfChannels_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 5, 1, 4),
    _CwsBladeBladecapabilitiesNumOfChannels_Type()
)
cwsBladeBladecapabilitiesNumOfChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeBladecapabilitiesNumOfChannels.setStatus("current")
_CwsBladeClientcapabilitiesTable_Object = MibTable
cwsBladeClientcapabilitiesTable = _CwsBladeClientcapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 6)
)
if mibBuilder.loadTexts:
    cwsBladeClientcapabilitiesTable.setStatus("current")
_CwsBladeClientcapabilitiesEntry_Object = MibTableRow
cwsBladeClientcapabilitiesEntry = _CwsBladeClientcapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 6, 1)
)
cwsBladeClientcapabilitiesEntry.setIndexNames(
    (0, "CIENA-WS-BLADE-MIB", "cwsBladeClientcapabilitiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsBladeClientcapabilitiesEntry.setStatus("current")


class _CwsBladeClientcapabilitiesTableSnmpKey_Type(Integer32):
    """Custom type cwsBladeClientcapabilitiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsBladeClientcapabilitiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsBladeClientcapabilitiesTableSnmpKey_Object = MibTableColumn
cwsBladeClientcapabilitiesTableSnmpKey = _CwsBladeClientcapabilitiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 6, 1, 1),
    _CwsBladeClientcapabilitiesTableSnmpKey_Type()
)
cwsBladeClientcapabilitiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsBladeClientcapabilitiesTableSnmpKey.setStatus("current")
_CwsBladeClientcapabilitiesNumOfPhysicalClientPorts_Type = Unsigned32
_CwsBladeClientcapabilitiesNumOfPhysicalClientPorts_Object = MibTableColumn
cwsBladeClientcapabilitiesNumOfPhysicalClientPorts = _CwsBladeClientcapabilitiesNumOfPhysicalClientPorts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 6, 1, 2),
    _CwsBladeClientcapabilitiesNumOfPhysicalClientPorts_Type()
)
cwsBladeClientcapabilitiesNumOfPhysicalClientPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeClientcapabilitiesNumOfPhysicalClientPorts.setStatus("current")
_CwsBladeClientcapabilitiesNumOfChannelPerClientPort_Type = Unsigned32
_CwsBladeClientcapabilitiesNumOfChannelPerClientPort_Object = MibTableColumn
cwsBladeClientcapabilitiesNumOfChannelPerClientPort = _CwsBladeClientcapabilitiesNumOfChannelPerClientPort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 6, 1, 3),
    _CwsBladeClientcapabilitiesNumOfChannelPerClientPort_Type()
)
cwsBladeClientcapabilitiesNumOfChannelPerClientPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeClientcapabilitiesNumOfChannelPerClientPort.setStatus("current")
_CwsBladeClientcapabilitiesCapacity_Type = StringMaxl64
_CwsBladeClientcapabilitiesCapacity_Object = MibTableColumn
cwsBladeClientcapabilitiesCapacity = _CwsBladeClientcapabilitiesCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 6, 1, 4),
    _CwsBladeClientcapabilitiesCapacity_Type()
)
cwsBladeClientcapabilitiesCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeClientcapabilitiesCapacity.setStatus("current")
_CwsBladeClientcapabilitiesDeviceType_Type = DeviceTypeBit
_CwsBladeClientcapabilitiesDeviceType_Object = MibTableColumn
cwsBladeClientcapabilitiesDeviceType = _CwsBladeClientcapabilitiesDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 6, 1, 5),
    _CwsBladeClientcapabilitiesDeviceType_Type()
)
cwsBladeClientcapabilitiesDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeClientcapabilitiesDeviceType.setStatus("current")


class _CwsBladeClientcapabilitiesDeviceSupport_Type(Bits):
    """Custom type cwsBladeClientcapabilitiesDeviceSupport based on Bits"""
    namedValues = NamedValues(
        *(("qsfpplus", 0),
          ("qsfp28", 1))
    )

_CwsBladeClientcapabilitiesDeviceSupport_Type.__name__ = "Bits"
_CwsBladeClientcapabilitiesDeviceSupport_Object = MibTableColumn
cwsBladeClientcapabilitiesDeviceSupport = _CwsBladeClientcapabilitiesDeviceSupport_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 6, 1, 6),
    _CwsBladeClientcapabilitiesDeviceSupport_Type()
)
cwsBladeClientcapabilitiesDeviceSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeClientcapabilitiesDeviceSupport.setStatus("current")


class _CwsBladeClientcapabilitiesProtocolSupport_Type(Bits):
    """Custom type cwsBladeClientcapabilitiesProtocolSupport based on Bits"""
    namedValues = NamedValues(
        ("ethernet", 0)
    )

_CwsBladeClientcapabilitiesProtocolSupport_Type.__name__ = "Bits"
_CwsBladeClientcapabilitiesProtocolSupport_Object = MibTableColumn
cwsBladeClientcapabilitiesProtocolSupport = _CwsBladeClientcapabilitiesProtocolSupport_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 6, 1, 7),
    _CwsBladeClientcapabilitiesProtocolSupport_Type()
)
cwsBladeClientcapabilitiesProtocolSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeClientcapabilitiesProtocolSupport.setStatus("current")
_CwsBladeLinecapabilitiesTable_Object = MibTable
cwsBladeLinecapabilitiesTable = _CwsBladeLinecapabilitiesTable_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 7)
)
if mibBuilder.loadTexts:
    cwsBladeLinecapabilitiesTable.setStatus("current")
_CwsBladeLinecapabilitiesEntry_Object = MibTableRow
cwsBladeLinecapabilitiesEntry = _CwsBladeLinecapabilitiesEntry_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 7, 1)
)
cwsBladeLinecapabilitiesEntry.setIndexNames(
    (0, "CIENA-WS-BLADE-MIB", "cwsBladeLinecapabilitiesTableSnmpKey"),
)
if mibBuilder.loadTexts:
    cwsBladeLinecapabilitiesEntry.setStatus("current")


class _CwsBladeLinecapabilitiesTableSnmpKey_Type(Integer32):
    """Custom type cwsBladeLinecapabilitiesTableSnmpKey based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_CwsBladeLinecapabilitiesTableSnmpKey_Type.__name__ = "Integer32"
_CwsBladeLinecapabilitiesTableSnmpKey_Object = MibTableColumn
cwsBladeLinecapabilitiesTableSnmpKey = _CwsBladeLinecapabilitiesTableSnmpKey_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 7, 1, 1),
    _CwsBladeLinecapabilitiesTableSnmpKey_Type()
)
cwsBladeLinecapabilitiesTableSnmpKey.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cwsBladeLinecapabilitiesTableSnmpKey.setStatus("current")
_CwsBladeLinecapabilitiesNumOfPhysicalLinePorts_Type = Unsigned32
_CwsBladeLinecapabilitiesNumOfPhysicalLinePorts_Object = MibTableColumn
cwsBladeLinecapabilitiesNumOfPhysicalLinePorts = _CwsBladeLinecapabilitiesNumOfPhysicalLinePorts_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 7, 1, 2),
    _CwsBladeLinecapabilitiesNumOfPhysicalLinePorts_Type()
)
cwsBladeLinecapabilitiesNumOfPhysicalLinePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeLinecapabilitiesNumOfPhysicalLinePorts.setStatus("current")
_CwsBladeLinecapabilitiesNumOfChannelPerLinePort_Type = Unsigned32
_CwsBladeLinecapabilitiesNumOfChannelPerLinePort_Object = MibTableColumn
cwsBladeLinecapabilitiesNumOfChannelPerLinePort = _CwsBladeLinecapabilitiesNumOfChannelPerLinePort_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 7, 1, 3),
    _CwsBladeLinecapabilitiesNumOfChannelPerLinePort_Type()
)
cwsBladeLinecapabilitiesNumOfChannelPerLinePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeLinecapabilitiesNumOfChannelPerLinePort.setStatus("current")
_CwsBladeLinecapabilitiesCapacity_Type = StringMaxl64
_CwsBladeLinecapabilitiesCapacity_Object = MibTableColumn
cwsBladeLinecapabilitiesCapacity = _CwsBladeLinecapabilitiesCapacity_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 7, 1, 4),
    _CwsBladeLinecapabilitiesCapacity_Type()
)
cwsBladeLinecapabilitiesCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeLinecapabilitiesCapacity.setStatus("current")
_CwsBladeLinecapabilitiesDeviceType_Type = DeviceTypeBit
_CwsBladeLinecapabilitiesDeviceType_Object = MibTableColumn
cwsBladeLinecapabilitiesDeviceType = _CwsBladeLinecapabilitiesDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 7, 1, 5),
    _CwsBladeLinecapabilitiesDeviceType_Type()
)
cwsBladeLinecapabilitiesDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeLinecapabilitiesDeviceType.setStatus("current")


class _CwsBladeLinecapabilitiesDeviceSupport_Type(Bits):
    """Custom type cwsBladeLinecapabilitiesDeviceSupport based on Bits"""
    namedValues = NamedValues(
        ("cienawl3extreme", 0)
    )

_CwsBladeLinecapabilitiesDeviceSupport_Type.__name__ = "Bits"
_CwsBladeLinecapabilitiesDeviceSupport_Object = MibTableColumn
cwsBladeLinecapabilitiesDeviceSupport = _CwsBladeLinecapabilitiesDeviceSupport_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 7, 1, 6),
    _CwsBladeLinecapabilitiesDeviceSupport_Type()
)
cwsBladeLinecapabilitiesDeviceSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeLinecapabilitiesDeviceSupport.setStatus("current")


class _CwsBladeLinecapabilitiesProtocolSupport_Type(Bits):
    """Custom type cwsBladeLinecapabilitiesProtocolSupport based on Bits"""
    namedValues = NamedValues(
        *(("nolineprotocol", 0),
          ("modulation200g16qam", 1),
          ("modulation100gqpsk", 2),
          ("modulation150g8qam", 3))
    )

_CwsBladeLinecapabilitiesProtocolSupport_Type.__name__ = "Bits"
_CwsBladeLinecapabilitiesProtocolSupport_Object = MibTableColumn
cwsBladeLinecapabilitiesProtocolSupport = _CwsBladeLinecapabilitiesProtocolSupport_Object(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 7, 1, 7),
    _CwsBladeLinecapabilitiesProtocolSupport_Type()
)
cwsBladeLinecapabilitiesProtocolSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cwsBladeLinecapabilitiesProtocolSupport.setStatus("current")

# Managed Objects groups

cienaWsBladeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 2, 1, 1)
)
cienaWsBladeGroup.setObjects(
      *(("CIENA-WS-BLADE-MIB", "cwsBladeBladeidentificationName"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladeidentificationModel"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladeidentificationDescription"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladeidentificationType"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladeidentificationUserDescription"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladeidentificationBasemacaddress"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladeidentificationPortbasemacaddress"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladestateAdminState"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladestateOperationalState"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladestateLastRestart"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladestateLastRestartReason"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladestateUptime"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladecapabilitiesModuleType"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladecapabilitiesNumOfPorts"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeBladecapabilitiesNumOfChannels"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeClientcapabilitiesNumOfPhysicalClientPorts"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeClientcapabilitiesNumOfChannelPerClientPort"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeClientcapabilitiesCapacity"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeClientcapabilitiesDeviceType"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeClientcapabilitiesDeviceSupport"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeClientcapabilitiesProtocolSupport"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeLinecapabilitiesNumOfPhysicalLinePorts"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeLinecapabilitiesNumOfChannelPerLinePort"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeLinecapabilitiesCapacity"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeLinecapabilitiesDeviceType"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeLinecapabilitiesDeviceSupport"),
        ("CIENA-WS-BLADE-MIB", "cwsBladeLinecapabilitiesProtocolSupport"))
)
if mibBuilder.loadTexts:
    cienaWsBladeGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cienaWsBladeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 1271, 3, 4, 5, 2, 2, 1)
)
cienaWsBladeCompliance.setObjects(
    ("CIENA-WS-BLADE-MIB", "cienaWsBladeGroup")
)
if mibBuilder.loadTexts:
    cienaWsBladeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CIENA-WS-BLADE-MIB",
    **{"DeviceTypeBit": DeviceTypeBit,
       "cienaWsBladeMIB": cienaWsBladeMIB,
       "cienaWsBladeObjects": cienaWsBladeObjects,
       "cienaWsBladeConformance": cienaWsBladeConformance,
       "cienaWsBladeGroups": cienaWsBladeGroups,
       "cienaWsBladeGroup": cienaWsBladeGroup,
       "cienaWsBladeCompliances": cienaWsBladeCompliances,
       "cienaWsBladeCompliance": cienaWsBladeCompliance,
       "cwsBladeBladeidentificationTable": cwsBladeBladeidentificationTable,
       "cwsBladeBladeidentificationEntry": cwsBladeBladeidentificationEntry,
       "cwsBladeBladeidentificationTableSnmpKey": cwsBladeBladeidentificationTableSnmpKey,
       "cwsBladeBladeidentificationName": cwsBladeBladeidentificationName,
       "cwsBladeBladeidentificationModel": cwsBladeBladeidentificationModel,
       "cwsBladeBladeidentificationDescription": cwsBladeBladeidentificationDescription,
       "cwsBladeBladeidentificationType": cwsBladeBladeidentificationType,
       "cwsBladeBladeidentificationUserDescription": cwsBladeBladeidentificationUserDescription,
       "cwsBladeBladeidentificationBasemacaddress": cwsBladeBladeidentificationBasemacaddress,
       "cwsBladeBladeidentificationPortbasemacaddress": cwsBladeBladeidentificationPortbasemacaddress,
       "cwsBladeBladestateTable": cwsBladeBladestateTable,
       "cwsBladeBladestateEntry": cwsBladeBladestateEntry,
       "cwsBladeBladestateTableSnmpKey": cwsBladeBladestateTableSnmpKey,
       "cwsBladeBladestateAdminState": cwsBladeBladestateAdminState,
       "cwsBladeBladestateOperationalState": cwsBladeBladestateOperationalState,
       "cwsBladeBladestateLastRestart": cwsBladeBladestateLastRestart,
       "cwsBladeBladestateLastRestartReason": cwsBladeBladestateLastRestartReason,
       "cwsBladeBladestateUptime": cwsBladeBladestateUptime,
       "cwsBladeBladecapabilitiesTable": cwsBladeBladecapabilitiesTable,
       "cwsBladeBladecapabilitiesEntry": cwsBladeBladecapabilitiesEntry,
       "cwsBladeBladecapabilitiesTableSnmpKey": cwsBladeBladecapabilitiesTableSnmpKey,
       "cwsBladeBladecapabilitiesModuleType": cwsBladeBladecapabilitiesModuleType,
       "cwsBladeBladecapabilitiesNumOfPorts": cwsBladeBladecapabilitiesNumOfPorts,
       "cwsBladeBladecapabilitiesNumOfChannels": cwsBladeBladecapabilitiesNumOfChannels,
       "cwsBladeClientcapabilitiesTable": cwsBladeClientcapabilitiesTable,
       "cwsBladeClientcapabilitiesEntry": cwsBladeClientcapabilitiesEntry,
       "cwsBladeClientcapabilitiesTableSnmpKey": cwsBladeClientcapabilitiesTableSnmpKey,
       "cwsBladeClientcapabilitiesNumOfPhysicalClientPorts": cwsBladeClientcapabilitiesNumOfPhysicalClientPorts,
       "cwsBladeClientcapabilitiesNumOfChannelPerClientPort": cwsBladeClientcapabilitiesNumOfChannelPerClientPort,
       "cwsBladeClientcapabilitiesCapacity": cwsBladeClientcapabilitiesCapacity,
       "cwsBladeClientcapabilitiesDeviceType": cwsBladeClientcapabilitiesDeviceType,
       "cwsBladeClientcapabilitiesDeviceSupport": cwsBladeClientcapabilitiesDeviceSupport,
       "cwsBladeClientcapabilitiesProtocolSupport": cwsBladeClientcapabilitiesProtocolSupport,
       "cwsBladeLinecapabilitiesTable": cwsBladeLinecapabilitiesTable,
       "cwsBladeLinecapabilitiesEntry": cwsBladeLinecapabilitiesEntry,
       "cwsBladeLinecapabilitiesTableSnmpKey": cwsBladeLinecapabilitiesTableSnmpKey,
       "cwsBladeLinecapabilitiesNumOfPhysicalLinePorts": cwsBladeLinecapabilitiesNumOfPhysicalLinePorts,
       "cwsBladeLinecapabilitiesNumOfChannelPerLinePort": cwsBladeLinecapabilitiesNumOfChannelPerLinePort,
       "cwsBladeLinecapabilitiesCapacity": cwsBladeLinecapabilitiesCapacity,
       "cwsBladeLinecapabilitiesDeviceType": cwsBladeLinecapabilitiesDeviceType,
       "cwsBladeLinecapabilitiesDeviceSupport": cwsBladeLinecapabilitiesDeviceSupport,
       "cwsBladeLinecapabilitiesProtocolSupport": cwsBladeLinecapabilitiesProtocolSupport}
)
