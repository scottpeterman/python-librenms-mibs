# SNMP MIB module (CITRIX-NetScaler-SD-WAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\citrix\CITRIX-NetScaler-SD-WAN-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:30:34 2025
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

(AutonomousType,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TestAndIncr,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TestAndIncr",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

sdWANMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class SdWANEventObjectTypeEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              1001,
              1002,
              1003,
              1004,
              1005)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("service", 2),
          ("virtualpath", 3),
          ("wanlink", 4),
          ("wanpath", 5),
          ("harddisk", 6),
          ("fan", 7),
          ("vwanappliance", 8),
          ("vwuser", 9),
          ("powersupply", 10),
          ("configupdate", 11),
          ("softwareupdate", 12),
          ("proxyarp", 13),
          ("ethernet", 14),
          ("watchdog", 15),
          ("dynamicvirtualpath", 16),
          ("lantowanpath", 17),
          ("wantolanpath", 18),
          ("appliancesettingsupdate", 19),
          ("discoveredmtu", 20),
          ("wanlinkcongestion", 21),
          ("usagecongestion", 22),
          ("gretunnel", 23),
          ("ipsectunnel", 24),
          ("vwcentersystem", 1001),
          ("vwcenteruser", 1002),
          ("vwcenterstorage", 1003),
          ("vwcenterdatabase", 1004),
          ("vwcenterconnectiontovirtualwan", 1005))
    )



class SdWANEventSeverityEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("debug", 1),
          ("info", 2),
          ("notice", 3),
          ("warning", 4),
          ("error", 5),
          ("critical", 6),
          ("alert", 7),
          ("emergency", 8))
    )



class SdWANEventStateEnum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              1001,
              1002,
              1003,
              1004,
              1005,
              1006,
              1007,
              1008)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("disabled", 2),
          ("dead", 3),
          ("bad", 4),
          ("good", 5),
          ("warning", 6),
          ("error", 7),
          ("restart", 8),
          ("reboot", 9),
          ("active", 10),
          ("standby", 11),
          ("success", 12),
          ("failure", 13),
          ("enabled", 14),
          ("pending", 15),
          ("created", 16),
          ("removed", 17),
          ("systemerror", 18),
          ("activeha", 19),
          ("standbyha", 20),
          ("activemcn", 21),
          ("standbymcn", 22),
          ("congested", 23),
          ("uncongested", 24),
          ("iplearned", 25),
          ("ipreleased", 26),
          ("ipexpired", 27),
          ("ipgwnorsp", 28),
          ("iprcvdnak", 29),
          ("ipdetecteddup", 30),
          ("ipdhcpsnorsp", 31),
          ("rollback", 32),
          ("usage0", 33),
          ("usage1", 34),
          ("usage2", 35),
          ("usage3", 36),
          ("thresholdok", 1001),
          ("thresholdexceeded", 1002),
          ("pollingthresholdok", 1003),
          ("pollingthresholdexceeded", 1004),
          ("start", 1005),
          ("stop", 1006),
          ("mismatch", 1007),
          ("statserror", 1008))
    )



# MIB Managed Objects in the order of their OIDs

_Citrix_ObjectIdentity = ObjectIdentity
citrix = _Citrix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845)
)
_SdWANStatusMIB_ObjectIdentity = ObjectIdentity
sdWANStatusMIB = _SdWANStatusMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4)
)
_SdWANObjects_ObjectIdentity = ObjectIdentity
sdWANObjects = _SdWANObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2)
)
_SdWANConfiguration_ObjectIdentity = ObjectIdentity
sdWANConfiguration = _SdWANConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 1)
)
_SdWANStatistics_ObjectIdentity = ObjectIdentity
sdWANStatistics = _SdWANStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2)
)
_SdWANStatsAppliances_ObjectIdentity = ObjectIdentity
sdWANStatsAppliances = _SdWANStatsAppliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12)
)
_SdWANStatsApplianceScalars_ObjectIdentity = ObjectIdentity
sdWANStatsApplianceScalars = _SdWANStatsApplianceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1)
)
_SdWANStatsApplianceName_Type = DisplayString
_SdWANStatsApplianceName_Object = MibScalar
sdWANStatsApplianceName = _SdWANStatsApplianceName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 1),
    _SdWANStatsApplianceName_Type()
)
sdWANStatsApplianceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceName.setStatus("current")
_SdWANStatsApplianceBytesSent_Type = Counter64
_SdWANStatsApplianceBytesSent_Object = MibScalar
sdWANStatsApplianceBytesSent = _SdWANStatsApplianceBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 2),
    _SdWANStatsApplianceBytesSent_Type()
)
sdWANStatsApplianceBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceBytesSent.setStatus("current")
_SdWANStatsAppliancePacketsSent_Type = Counter64
_SdWANStatsAppliancePacketsSent_Object = MibScalar
sdWANStatsAppliancePacketsSent = _SdWANStatsAppliancePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 3),
    _SdWANStatsAppliancePacketsSent_Type()
)
sdWANStatsAppliancePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsAppliancePacketsSent.setStatus("current")
_SdWANStatsApplianceBytesReceived_Type = Counter64
_SdWANStatsApplianceBytesReceived_Object = MibScalar
sdWANStatsApplianceBytesReceived = _SdWANStatsApplianceBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 4),
    _SdWANStatsApplianceBytesReceived_Type()
)
sdWANStatsApplianceBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceBytesReceived.setStatus("current")
_SdWANStatsAppliancePacketsReceived_Type = Counter64
_SdWANStatsAppliancePacketsReceived_Object = MibScalar
sdWANStatsAppliancePacketsReceived = _SdWANStatsAppliancePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 5),
    _SdWANStatsAppliancePacketsReceived_Type()
)
sdWANStatsAppliancePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsAppliancePacketsReceived.setStatus("current")
_SdWANStatsApplianceBytesDropped_Type = Counter64
_SdWANStatsApplianceBytesDropped_Object = MibScalar
sdWANStatsApplianceBytesDropped = _SdWANStatsApplianceBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 6),
    _SdWANStatsApplianceBytesDropped_Type()
)
sdWANStatsApplianceBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceBytesDropped.setStatus("current")
_SdWANStatsAppliancePacketsDropped_Type = Counter64
_SdWANStatsAppliancePacketsDropped_Object = MibScalar
sdWANStatsAppliancePacketsDropped = _SdWANStatsAppliancePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 7),
    _SdWANStatsAppliancePacketsDropped_Type()
)
sdWANStatsAppliancePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsAppliancePacketsDropped.setStatus("current")


class _SdWANStatsApplianceState_Type(Integer32):
    """Custom type sdWANStatsApplianceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("disabled", 1),
          ("enabled", 2))
    )


_SdWANStatsApplianceState_Type.__name__ = "Integer32"
_SdWANStatsApplianceState_Object = MibScalar
sdWANStatsApplianceState = _SdWANStatsApplianceState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 8),
    _SdWANStatsApplianceState_Type()
)
sdWANStatsApplianceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceState.setStatus("current")


class _SdWANStatsApplianceHAState_Type(Integer32):
    """Custom type sdWANStatsApplianceHAState based on Integer32"""
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
        *(("undefined", 0),
          ("notConfigured", 1),
          ("active", 2),
          ("standby", 3))
    )


_SdWANStatsApplianceHAState_Type.__name__ = "Integer32"
_SdWANStatsApplianceHAState_Object = MibScalar
sdWANStatsApplianceHAState = _SdWANStatsApplianceHAState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 9),
    _SdWANStatsApplianceHAState_Type()
)
sdWANStatsApplianceHAState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceHAState.setStatus("current")
_SdWANStatsApplianceSerialNumber_Type = DisplayString
_SdWANStatsApplianceSerialNumber_Object = MibScalar
sdWANStatsApplianceSerialNumber = _SdWANStatsApplianceSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 10),
    _SdWANStatsApplianceSerialNumber_Type()
)
sdWANStatsApplianceSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceSerialNumber.setStatus("current")
_SdWANStatsApplianceOSVersion_Type = DisplayString
_SdWANStatsApplianceOSVersion_Object = MibScalar
sdWANStatsApplianceOSVersion = _SdWANStatsApplianceOSVersion_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 11),
    _SdWANStatsApplianceOSVersion_Type()
)
sdWANStatsApplianceOSVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceOSVersion.setStatus("current")
_SdWANStatsApplianceSoftwareVersion_Type = DisplayString
_SdWANStatsApplianceSoftwareVersion_Object = MibScalar
sdWANStatsApplianceSoftwareVersion = _SdWANStatsApplianceSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 12),
    _SdWANStatsApplianceSoftwareVersion_Type()
)
sdWANStatsApplianceSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceSoftwareVersion.setStatus("current")
_SdWANStatsApplianceConfigCreatedOn_Type = DisplayString
_SdWANStatsApplianceConfigCreatedOn_Object = MibScalar
sdWANStatsApplianceConfigCreatedOn = _SdWANStatsApplianceConfigCreatedOn_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 13),
    _SdWANStatsApplianceConfigCreatedOn_Type()
)
sdWANStatsApplianceConfigCreatedOn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceConfigCreatedOn.setStatus("current")
_SdWANStatsApplianceServiceUptime_Type = TimeTicks
_SdWANStatsApplianceServiceUptime_Object = MibScalar
sdWANStatsApplianceServiceUptime = _SdWANStatsApplianceServiceUptime_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 14),
    _SdWANStatsApplianceServiceUptime_Type()
)
sdWANStatsApplianceServiceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceServiceUptime.setStatus("current")
_SdWANStatsApplianceApplianceUptime_Type = TimeTicks
_SdWANStatsApplianceApplianceUptime_Object = MibScalar
sdWANStatsApplianceApplianceUptime = _SdWANStatsApplianceApplianceUptime_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 12, 1, 15),
    _SdWANStatsApplianceApplianceUptime_Type()
)
sdWANStatsApplianceApplianceUptime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsApplianceApplianceUptime.setStatus("current")
_SdWANStatsEthernetInterfaces_ObjectIdentity = ObjectIdentity
sdWANStatsEthernetInterfaces = _SdWANStatsEthernetInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13)
)
_SdWANStatsEthernetInterfaceScalars_ObjectIdentity = ObjectIdentity
sdWANStatsEthernetInterfaceScalars = _SdWANStatsEthernetInterfaceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 1)
)


class _SdWANStatsNumEthernetInterfaces_Type(Integer32):
    """Custom type sdWANStatsNumEthernetInterfaces based on Integer32"""
    defaultValue = 0


_SdWANStatsNumEthernetInterfaces_Type.__name__ = "Integer32"
_SdWANStatsNumEthernetInterfaces_Object = MibScalar
sdWANStatsNumEthernetInterfaces = _SdWANStatsNumEthernetInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 1, 1),
    _SdWANStatsNumEthernetInterfaces_Type()
)
sdWANStatsNumEthernetInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsNumEthernetInterfaces.setStatus("current")
_SdWANStatsEthernetInterfaceTable_Object = MibTable
sdWANStatsEthernetInterfaceTable = _SdWANStatsEthernetInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2)
)
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfaceTable.setStatus("current")
_SdWANStatsEthernetInterfaceEntry_Object = MibTableRow
sdWANStatsEthernetInterfaceEntry = _SdWANStatsEthernetInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1)
)
sdWANStatsEthernetInterfaceEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsEthernetInterfaceIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfaceEntry.setStatus("current")
_SdWANStatsEthernetInterfaceIndex_Type = Integer32
_SdWANStatsEthernetInterfaceIndex_Object = MibTableColumn
sdWANStatsEthernetInterfaceIndex = _SdWANStatsEthernetInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1, 1),
    _SdWANStatsEthernetInterfaceIndex_Type()
)
sdWANStatsEthernetInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfaceIndex.setStatus("current")
_SdWANStatsEthernetInterfaceIfIndex_Type = Integer32
_SdWANStatsEthernetInterfaceIfIndex_Object = MibTableColumn
sdWANStatsEthernetInterfaceIfIndex = _SdWANStatsEthernetInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1, 2),
    _SdWANStatsEthernetInterfaceIfIndex_Type()
)
sdWANStatsEthernetInterfaceIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfaceIfIndex.setStatus("current")
_SdWANStatsEthernetInterfaceName_Type = DisplayString
_SdWANStatsEthernetInterfaceName_Object = MibTableColumn
sdWANStatsEthernetInterfaceName = _SdWANStatsEthernetInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1, 3),
    _SdWANStatsEthernetInterfaceName_Type()
)
sdWANStatsEthernetInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfaceName.setStatus("current")
_SdWANStatsEthernetInterfaceBytesSent_Type = Counter64
_SdWANStatsEthernetInterfaceBytesSent_Object = MibTableColumn
sdWANStatsEthernetInterfaceBytesSent = _SdWANStatsEthernetInterfaceBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1, 4),
    _SdWANStatsEthernetInterfaceBytesSent_Type()
)
sdWANStatsEthernetInterfaceBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfaceBytesSent.setStatus("current")
_SdWANStatsEthernetInterfacePacketsSent_Type = Counter64
_SdWANStatsEthernetInterfacePacketsSent_Object = MibTableColumn
sdWANStatsEthernetInterfacePacketsSent = _SdWANStatsEthernetInterfacePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1, 5),
    _SdWANStatsEthernetInterfacePacketsSent_Type()
)
sdWANStatsEthernetInterfacePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfacePacketsSent.setStatus("current")
_SdWANStatsEthernetInterfaceBytesReceived_Type = Counter64
_SdWANStatsEthernetInterfaceBytesReceived_Object = MibTableColumn
sdWANStatsEthernetInterfaceBytesReceived = _SdWANStatsEthernetInterfaceBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1, 6),
    _SdWANStatsEthernetInterfaceBytesReceived_Type()
)
sdWANStatsEthernetInterfaceBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfaceBytesReceived.setStatus("current")
_SdWANStatsEthernetInterfacePacketsReceived_Type = Counter64
_SdWANStatsEthernetInterfacePacketsReceived_Object = MibTableColumn
sdWANStatsEthernetInterfacePacketsReceived = _SdWANStatsEthernetInterfacePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1, 7),
    _SdWANStatsEthernetInterfacePacketsReceived_Type()
)
sdWANStatsEthernetInterfacePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfacePacketsReceived.setStatus("current")
_SdWANStatsEthernetInterfaceBytesDropped_Type = Counter64
_SdWANStatsEthernetInterfaceBytesDropped_Object = MibTableColumn
sdWANStatsEthernetInterfaceBytesDropped = _SdWANStatsEthernetInterfaceBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1, 8),
    _SdWANStatsEthernetInterfaceBytesDropped_Type()
)
sdWANStatsEthernetInterfaceBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfaceBytesDropped.setStatus("current")
_SdWANStatsEthernetInterfacePacketsDropped_Type = Counter64
_SdWANStatsEthernetInterfacePacketsDropped_Object = MibTableColumn
sdWANStatsEthernetInterfacePacketsDropped = _SdWANStatsEthernetInterfacePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 13, 2, 1, 9),
    _SdWANStatsEthernetInterfacePacketsDropped_Type()
)
sdWANStatsEthernetInterfacePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsEthernetInterfacePacketsDropped.setStatus("current")
_SdWANStatsRules_ObjectIdentity = ObjectIdentity
sdWANStatsRules = _SdWANStatsRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14)
)
_SdWANStatsRuleScalars_ObjectIdentity = ObjectIdentity
sdWANStatsRuleScalars = _SdWANStatsRuleScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 1)
)


class _SdWANStatsNumRules_Type(Integer32):
    """Custom type sdWANStatsNumRules based on Integer32"""
    defaultValue = 0


_SdWANStatsNumRules_Type.__name__ = "Integer32"
_SdWANStatsNumRules_Object = MibScalar
sdWANStatsNumRules = _SdWANStatsNumRules_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 1, 1),
    _SdWANStatsNumRules_Type()
)
sdWANStatsNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsNumRules.setStatus("current")
_SdWANStatsRuleTable_Object = MibTable
sdWANStatsRuleTable = _SdWANStatsRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2)
)
if mibBuilder.loadTexts:
    sdWANStatsRuleTable.setStatus("current")
_SdWANStatsRuleEntry_Object = MibTableRow
sdWANStatsRuleEntry = _SdWANStatsRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1)
)
sdWANStatsRuleEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsRuleIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsRuleEntry.setStatus("current")
_SdWANStatsRuleIndex_Type = Integer32
_SdWANStatsRuleIndex_Object = MibTableColumn
sdWANStatsRuleIndex = _SdWANStatsRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 1),
    _SdWANStatsRuleIndex_Type()
)
sdWANStatsRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRuleIndex.setStatus("current")
_SdWANStatsRuleID_Type = Integer32
_SdWANStatsRuleID_Object = MibTableColumn
sdWANStatsRuleID = _SdWANStatsRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 2),
    _SdWANStatsRuleID_Type()
)
sdWANStatsRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRuleID.setStatus("current")
_SdWANStatsRuleApplicationName_Type = DisplayString
_SdWANStatsRuleApplicationName_Object = MibTableColumn
sdWANStatsRuleApplicationName = _SdWANStatsRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 3),
    _SdWANStatsRuleApplicationName_Type()
)
sdWANStatsRuleApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRuleApplicationName.setStatus("current")
_SdWANStatsRuleLANToWANHitCount_Type = Gauge32
_SdWANStatsRuleLANToWANHitCount_Object = MibTableColumn
sdWANStatsRuleLANToWANHitCount = _SdWANStatsRuleLANToWANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 4),
    _SdWANStatsRuleLANToWANHitCount_Type()
)
sdWANStatsRuleLANToWANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRuleLANToWANHitCount.setStatus("current")
_SdWANStatsRuleWANToLANHitCount_Type = Gauge32
_SdWANStatsRuleWANToLANHitCount_Object = MibTableColumn
sdWANStatsRuleWANToLANHitCount = _SdWANStatsRuleWANToLANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 5),
    _SdWANStatsRuleWANToLANHitCount_Type()
)
sdWANStatsRuleWANToLANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRuleWANToLANHitCount.setStatus("current")
_SdWANStatsRuleBytesSent_Type = Gauge32
_SdWANStatsRuleBytesSent_Object = MibTableColumn
sdWANStatsRuleBytesSent = _SdWANStatsRuleBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 6),
    _SdWANStatsRuleBytesSent_Type()
)
sdWANStatsRuleBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRuleBytesSent.setStatus("current")
_SdWANStatsRulePacketsSent_Type = Gauge32
_SdWANStatsRulePacketsSent_Object = MibTableColumn
sdWANStatsRulePacketsSent = _SdWANStatsRulePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 7),
    _SdWANStatsRulePacketsSent_Type()
)
sdWANStatsRulePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRulePacketsSent.setStatus("current")
_SdWANStatsRuleBytesReceived_Type = Gauge32
_SdWANStatsRuleBytesReceived_Object = MibTableColumn
sdWANStatsRuleBytesReceived = _SdWANStatsRuleBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 8),
    _SdWANStatsRuleBytesReceived_Type()
)
sdWANStatsRuleBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRuleBytesReceived.setStatus("current")
_SdWANStatsRulePacketsReceived_Type = Gauge32
_SdWANStatsRulePacketsReceived_Object = MibTableColumn
sdWANStatsRulePacketsReceived = _SdWANStatsRulePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 9),
    _SdWANStatsRulePacketsReceived_Type()
)
sdWANStatsRulePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRulePacketsReceived.setStatus("current")
_SdWANStatsRuleBytesDropped_Type = Gauge32
_SdWANStatsRuleBytesDropped_Object = MibTableColumn
sdWANStatsRuleBytesDropped = _SdWANStatsRuleBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 10),
    _SdWANStatsRuleBytesDropped_Type()
)
sdWANStatsRuleBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRuleBytesDropped.setStatus("current")
_SdWANStatsRulePacketsDropped_Type = Gauge32
_SdWANStatsRulePacketsDropped_Object = MibTableColumn
sdWANStatsRulePacketsDropped = _SdWANStatsRulePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 11),
    _SdWANStatsRulePacketsDropped_Type()
)
sdWANStatsRulePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRulePacketsDropped.setStatus("current")
_SdWANStatsRuleLastActiveNMinuteAgo_Type = TimeTicks
_SdWANStatsRuleLastActiveNMinuteAgo_Object = MibTableColumn
sdWANStatsRuleLastActiveNMinuteAgo = _SdWANStatsRuleLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 14, 2, 1, 12),
    _SdWANStatsRuleLastActiveNMinuteAgo_Type()
)
sdWANStatsRuleLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRuleLastActiveNMinuteAgo.setStatus("current")
_SdWANStatsWANLinks_ObjectIdentity = ObjectIdentity
sdWANStatsWANLinks = _SdWANStatsWANLinks_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15)
)
_SdWANStatsWANLinkScalars_ObjectIdentity = ObjectIdentity
sdWANStatsWANLinkScalars = _SdWANStatsWANLinkScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 1)
)


class _SdWANStatsNumWANLinks_Type(Integer32):
    """Custom type sdWANStatsNumWANLinks based on Integer32"""
    defaultValue = 0


_SdWANStatsNumWANLinks_Type.__name__ = "Integer32"
_SdWANStatsNumWANLinks_Object = MibScalar
sdWANStatsNumWANLinks = _SdWANStatsNumWANLinks_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 1, 1),
    _SdWANStatsNumWANLinks_Type()
)
sdWANStatsNumWANLinks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsNumWANLinks.setStatus("current")
_SdWANStatsWANLinkTable_Object = MibTable
sdWANStatsWANLinkTable = _SdWANStatsWANLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2)
)
if mibBuilder.loadTexts:
    sdWANStatsWANLinkTable.setStatus("current")
_SdWANStatsWANLinkEntry_Object = MibTableRow
sdWANStatsWANLinkEntry = _SdWANStatsWANLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1)
)
sdWANStatsWANLinkEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsWANLinkIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsWANLinkEntry.setStatus("current")
_SdWANStatsWANLinkIndex_Type = Integer32
_SdWANStatsWANLinkIndex_Object = MibTableColumn
sdWANStatsWANLinkIndex = _SdWANStatsWANLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 1),
    _SdWANStatsWANLinkIndex_Type()
)
sdWANStatsWANLinkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkIndex.setStatus("current")
_SdWANStatsWANLinkID_Type = Integer32
_SdWANStatsWANLinkID_Object = MibTableColumn
sdWANStatsWANLinkID = _SdWANStatsWANLinkID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 2),
    _SdWANStatsWANLinkID_Type()
)
sdWANStatsWANLinkID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkID.setStatus("current")
_SdWANStatsWANLinkName_Type = DisplayString
_SdWANStatsWANLinkName_Object = MibTableColumn
sdWANStatsWANLinkName = _SdWANStatsWANLinkName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 3),
    _SdWANStatsWANLinkName_Type()
)
sdWANStatsWANLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkName.setStatus("current")


class _SdWANStatsWANLinkState_Type(Integer32):
    """Custom type sdWANStatsWANLinkState based on Integer32"""
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
        *(("undefined", 0),
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_SdWANStatsWANLinkState_Type.__name__ = "Integer32"
_SdWANStatsWANLinkState_Object = MibTableColumn
sdWANStatsWANLinkState = _SdWANStatsWANLinkState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 4),
    _SdWANStatsWANLinkState_Type()
)
sdWANStatsWANLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkState.setStatus("current")
_SdWANStatsWANLinkBytesSent_Type = Counter64
_SdWANStatsWANLinkBytesSent_Object = MibTableColumn
sdWANStatsWANLinkBytesSent = _SdWANStatsWANLinkBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 5),
    _SdWANStatsWANLinkBytesSent_Type()
)
sdWANStatsWANLinkBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkBytesSent.setStatus("current")
_SdWANStatsWANLinkPacketsSent_Type = Counter64
_SdWANStatsWANLinkPacketsSent_Object = MibTableColumn
sdWANStatsWANLinkPacketsSent = _SdWANStatsWANLinkPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 6),
    _SdWANStatsWANLinkPacketsSent_Type()
)
sdWANStatsWANLinkPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkPacketsSent.setStatus("current")
_SdWANStatsWANLinkBytesReceived_Type = Counter64
_SdWANStatsWANLinkBytesReceived_Object = MibTableColumn
sdWANStatsWANLinkBytesReceived = _SdWANStatsWANLinkBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 7),
    _SdWANStatsWANLinkBytesReceived_Type()
)
sdWANStatsWANLinkBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkBytesReceived.setStatus("current")
_SdWANStatsWANLinkPacketsReceived_Type = Counter64
_SdWANStatsWANLinkPacketsReceived_Object = MibTableColumn
sdWANStatsWANLinkPacketsReceived = _SdWANStatsWANLinkPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 8),
    _SdWANStatsWANLinkPacketsReceived_Type()
)
sdWANStatsWANLinkPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkPacketsReceived.setStatus("current")
_SdWANStatsWANLinkBytesDropped_Type = Counter64
_SdWANStatsWANLinkBytesDropped_Object = MibTableColumn
sdWANStatsWANLinkBytesDropped = _SdWANStatsWANLinkBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 9),
    _SdWANStatsWANLinkBytesDropped_Type()
)
sdWANStatsWANLinkBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkBytesDropped.setStatus("current")
_SdWANStatsWANLinkPacketsDropped_Type = Counter64
_SdWANStatsWANLinkPacketsDropped_Object = MibTableColumn
sdWANStatsWANLinkPacketsDropped = _SdWANStatsWANLinkPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 15, 2, 1, 10),
    _SdWANStatsWANLinkPacketsDropped_Type()
)
sdWANStatsWANLinkPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANLinkPacketsDropped.setStatus("current")
_SdWANStatsVPaths_ObjectIdentity = ObjectIdentity
sdWANStatsVPaths = _SdWANStatsVPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16)
)
_SdWANStatsVPathScalars_ObjectIdentity = ObjectIdentity
sdWANStatsVPathScalars = _SdWANStatsVPathScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 1)
)


class _SdWANStatsNumVPaths_Type(Integer32):
    """Custom type sdWANStatsNumVPaths based on Integer32"""
    defaultValue = 0


_SdWANStatsNumVPaths_Type.__name__ = "Integer32"
_SdWANStatsNumVPaths_Object = MibScalar
sdWANStatsNumVPaths = _SdWANStatsNumVPaths_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 1, 1),
    _SdWANStatsNumVPaths_Type()
)
sdWANStatsNumVPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsNumVPaths.setStatus("current")
_SdWANStatsVPathTable_Object = MibTable
sdWANStatsVPathTable = _SdWANStatsVPathTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2)
)
if mibBuilder.loadTexts:
    sdWANStatsVPathTable.setStatus("current")
_SdWANStatsVPathEntry_Object = MibTableRow
sdWANStatsVPathEntry = _SdWANStatsVPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1)
)
sdWANStatsVPathEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsVPathIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsVPathEntry.setStatus("current")
_SdWANStatsVPathIndex_Type = Integer32
_SdWANStatsVPathIndex_Object = MibTableColumn
sdWANStatsVPathIndex = _SdWANStatsVPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 1),
    _SdWANStatsVPathIndex_Type()
)
sdWANStatsVPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathIndex.setStatus("current")
_SdWANStatsVPathID_Type = Integer32
_SdWANStatsVPathID_Object = MibTableColumn
sdWANStatsVPathID = _SdWANStatsVPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 2),
    _SdWANStatsVPathID_Type()
)
sdWANStatsVPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathID.setStatus("current")
_SdWANStatsVPathName_Type = DisplayString
_SdWANStatsVPathName_Object = MibTableColumn
sdWANStatsVPathName = _SdWANStatsVPathName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 3),
    _SdWANStatsVPathName_Type()
)
sdWANStatsVPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathName.setStatus("current")


class _SdWANStatsVPathState_Type(Integer32):
    """Custom type sdWANStatsVPathState based on Integer32"""
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
        *(("undefined", 0),
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_SdWANStatsVPathState_Type.__name__ = "Integer32"
_SdWANStatsVPathState_Object = MibTableColumn
sdWANStatsVPathState = _SdWANStatsVPathState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 4),
    _SdWANStatsVPathState_Type()
)
sdWANStatsVPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathState.setStatus("current")
_SdWANStatsVPathBytesSent_Type = Counter64
_SdWANStatsVPathBytesSent_Object = MibTableColumn
sdWANStatsVPathBytesSent = _SdWANStatsVPathBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 5),
    _SdWANStatsVPathBytesSent_Type()
)
sdWANStatsVPathBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathBytesSent.setStatus("current")
_SdWANStatsVPathPacketsSent_Type = Counter64
_SdWANStatsVPathPacketsSent_Object = MibTableColumn
sdWANStatsVPathPacketsSent = _SdWANStatsVPathPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 6),
    _SdWANStatsVPathPacketsSent_Type()
)
sdWANStatsVPathPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathPacketsSent.setStatus("current")
_SdWANStatsVPathBytesReceived_Type = Counter64
_SdWANStatsVPathBytesReceived_Object = MibTableColumn
sdWANStatsVPathBytesReceived = _SdWANStatsVPathBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 7),
    _SdWANStatsVPathBytesReceived_Type()
)
sdWANStatsVPathBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathBytesReceived.setStatus("current")
_SdWANStatsVPathPacketsReceived_Type = Counter64
_SdWANStatsVPathPacketsReceived_Object = MibTableColumn
sdWANStatsVPathPacketsReceived = _SdWANStatsVPathPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 8),
    _SdWANStatsVPathPacketsReceived_Type()
)
sdWANStatsVPathPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathPacketsReceived.setStatus("current")
_SdWANStatsVPathNumPaths_Type = Integer32
_SdWANStatsVPathNumPaths_Object = MibTableColumn
sdWANStatsVPathNumPaths = _SdWANStatsVPathNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 9),
    _SdWANStatsVPathNumPaths_Type()
)
sdWANStatsVPathNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathNumPaths.setStatus("current")
_SdWANStatsVPathNumRules_Type = Integer32
_SdWANStatsVPathNumRules_Object = MibTableColumn
sdWANStatsVPathNumRules = _SdWANStatsVPathNumRules_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 10),
    _SdWANStatsVPathNumRules_Type()
)
sdWANStatsVPathNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathNumRules.setStatus("current")
_SdWANStatsVPathSendBytesDropped_Type = Counter64
_SdWANStatsVPathSendBytesDropped_Object = MibTableColumn
sdWANStatsVPathSendBytesDropped = _SdWANStatsVPathSendBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 11),
    _SdWANStatsVPathSendBytesDropped_Type()
)
sdWANStatsVPathSendBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathSendBytesDropped.setStatus("current")
_SdWANStatsVPathSendPacketsDropped_Type = Counter64
_SdWANStatsVPathSendPacketsDropped_Object = MibTableColumn
sdWANStatsVPathSendPacketsDropped = _SdWANStatsVPathSendPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 12),
    _SdWANStatsVPathSendPacketsDropped_Type()
)
sdWANStatsVPathSendPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathSendPacketsDropped.setStatus("current")
_SdWANStatsVPathSendPacketsLost_Type = Counter64
_SdWANStatsVPathSendPacketsLost_Object = MibTableColumn
sdWANStatsVPathSendPacketsLost = _SdWANStatsVPathSendPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 13),
    _SdWANStatsVPathSendPacketsLost_Type()
)
sdWANStatsVPathSendPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathSendPacketsLost.setStatus("current")
_SdWANStatsVPathSendPacketsOOO_Type = Counter64
_SdWANStatsVPathSendPacketsOOO_Object = MibTableColumn
sdWANStatsVPathSendPacketsOOO = _SdWANStatsVPathSendPacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 14),
    _SdWANStatsVPathSendPacketsOOO_Type()
)
sdWANStatsVPathSendPacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathSendPacketsOOO.setStatus("current")
_SdWANStatsVPathSendBOWTms_Type = Gauge32
_SdWANStatsVPathSendBOWTms_Object = MibTableColumn
sdWANStatsVPathSendBOWTms = _SdWANStatsVPathSendBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 15),
    _SdWANStatsVPathSendBOWTms_Type()
)
sdWANStatsVPathSendBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathSendBOWTms.setStatus("current")
_SdWANStatsVPathSendJitterms_Type = Gauge32
_SdWANStatsVPathSendJitterms_Object = MibTableColumn
sdWANStatsVPathSendJitterms = _SdWANStatsVPathSendJitterms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 16),
    _SdWANStatsVPathSendJitterms_Type()
)
sdWANStatsVPathSendJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathSendJitterms.setStatus("current")
_SdWANStatsVPathReceiveBytesDropped_Type = Counter64
_SdWANStatsVPathReceiveBytesDropped_Object = MibTableColumn
sdWANStatsVPathReceiveBytesDropped = _SdWANStatsVPathReceiveBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 17),
    _SdWANStatsVPathReceiveBytesDropped_Type()
)
sdWANStatsVPathReceiveBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathReceiveBytesDropped.setStatus("current")
_SdWANStatsVPathReceivePacketsDropped_Type = Counter64
_SdWANStatsVPathReceivePacketsDropped_Object = MibTableColumn
sdWANStatsVPathReceivePacketsDropped = _SdWANStatsVPathReceivePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 18),
    _SdWANStatsVPathReceivePacketsDropped_Type()
)
sdWANStatsVPathReceivePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathReceivePacketsDropped.setStatus("current")
_SdWANStatsVPathReceivePacketsLost_Type = Counter64
_SdWANStatsVPathReceivePacketsLost_Object = MibTableColumn
sdWANStatsVPathReceivePacketsLost = _SdWANStatsVPathReceivePacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 19),
    _SdWANStatsVPathReceivePacketsLost_Type()
)
sdWANStatsVPathReceivePacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathReceivePacketsLost.setStatus("current")
_SdWANStatsVPathReceivePacketsOOO_Type = Counter64
_SdWANStatsVPathReceivePacketsOOO_Object = MibTableColumn
sdWANStatsVPathReceivePacketsOOO = _SdWANStatsVPathReceivePacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 20),
    _SdWANStatsVPathReceivePacketsOOO_Type()
)
sdWANStatsVPathReceivePacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathReceivePacketsOOO.setStatus("current")
_SdWANStatsVPathReceiveBOWTms_Type = Gauge32
_SdWANStatsVPathReceiveBOWTms_Object = MibTableColumn
sdWANStatsVPathReceiveBOWTms = _SdWANStatsVPathReceiveBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 21),
    _SdWANStatsVPathReceiveBOWTms_Type()
)
sdWANStatsVPathReceiveBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathReceiveBOWTms.setStatus("current")
_SdWANStatsVPathReceiveJitterms_Type = Gauge32
_SdWANStatsVPathReceiveJitterms_Object = MibTableColumn
sdWANStatsVPathReceiveJitterms = _SdWANStatsVPathReceiveJitterms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 2, 1, 22),
    _SdWANStatsVPathReceiveJitterms_Type()
)
sdWANStatsVPathReceiveJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsVPathReceiveJitterms.setStatus("current")
_SdWANStatsWANPaths_ObjectIdentity = ObjectIdentity
sdWANStatsWANPaths = _SdWANStatsWANPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3)
)
_SdWANStatsWANPathTable_Object = MibTable
sdWANStatsWANPathTable = _SdWANStatsWANPathTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1)
)
if mibBuilder.loadTexts:
    sdWANStatsWANPathTable.setStatus("current")
_SdWANStatsWANPathEntry_Object = MibTableRow
sdWANStatsWANPathEntry = _SdWANStatsWANPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1)
)
sdWANStatsWANPathEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsWANPathVPathIndex"),
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsWANPathPathIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsWANPathEntry.setStatus("current")
_SdWANStatsWANPathVPathIndex_Type = Integer32
_SdWANStatsWANPathVPathIndex_Object = MibTableColumn
sdWANStatsWANPathVPathIndex = _SdWANStatsWANPathVPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 1),
    _SdWANStatsWANPathVPathIndex_Type()
)
sdWANStatsWANPathVPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathVPathIndex.setStatus("current")
_SdWANStatsWANPathPathIndex_Type = Integer32
_SdWANStatsWANPathPathIndex_Object = MibTableColumn
sdWANStatsWANPathPathIndex = _SdWANStatsWANPathPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 2),
    _SdWANStatsWANPathPathIndex_Type()
)
sdWANStatsWANPathPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathPathIndex.setStatus("current")
_SdWANStatsWANPathVPathID_Type = Integer32
_SdWANStatsWANPathVPathID_Object = MibTableColumn
sdWANStatsWANPathVPathID = _SdWANStatsWANPathVPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 3),
    _SdWANStatsWANPathVPathID_Type()
)
sdWANStatsWANPathVPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathVPathID.setStatus("current")
_SdWANStatsWANPathPathID_Type = Integer32
_SdWANStatsWANPathPathID_Object = MibTableColumn
sdWANStatsWANPathPathID = _SdWANStatsWANPathPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 4),
    _SdWANStatsWANPathPathID_Type()
)
sdWANStatsWANPathPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathPathID.setStatus("current")
_SdWANStatsWANPathName_Type = DisplayString
_SdWANStatsWANPathName_Object = MibTableColumn
sdWANStatsWANPathName = _SdWANStatsWANPathName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 5),
    _SdWANStatsWANPathName_Type()
)
sdWANStatsWANPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathName.setStatus("current")


class _SdWANStatsWANPathState_Type(Integer32):
    """Custom type sdWANStatsWANPathState based on Integer32"""
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
        *(("undefined", 0),
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_SdWANStatsWANPathState_Type.__name__ = "Integer32"
_SdWANStatsWANPathState_Object = MibTableColumn
sdWANStatsWANPathState = _SdWANStatsWANPathState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 6),
    _SdWANStatsWANPathState_Type()
)
sdWANStatsWANPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathState.setStatus("current")
_SdWANStatsWANPathBytesSent_Type = Counter64
_SdWANStatsWANPathBytesSent_Object = MibTableColumn
sdWANStatsWANPathBytesSent = _SdWANStatsWANPathBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 7),
    _SdWANStatsWANPathBytesSent_Type()
)
sdWANStatsWANPathBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathBytesSent.setStatus("current")
_SdWANStatsWANPathPacketsSent_Type = Counter64
_SdWANStatsWANPathPacketsSent_Object = MibTableColumn
sdWANStatsWANPathPacketsSent = _SdWANStatsWANPathPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 8),
    _SdWANStatsWANPathPacketsSent_Type()
)
sdWANStatsWANPathPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathPacketsSent.setStatus("current")
_SdWANStatsWANPathBytesReceived_Type = Counter64
_SdWANStatsWANPathBytesReceived_Object = MibTableColumn
sdWANStatsWANPathBytesReceived = _SdWANStatsWANPathBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 9),
    _SdWANStatsWANPathBytesReceived_Type()
)
sdWANStatsWANPathBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathBytesReceived.setStatus("current")
_SdWANStatsWANPathPacketsReceived_Type = Counter64
_SdWANStatsWANPathPacketsReceived_Object = MibTableColumn
sdWANStatsWANPathPacketsReceived = _SdWANStatsWANPathPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 10),
    _SdWANStatsWANPathPacketsReceived_Type()
)
sdWANStatsWANPathPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathPacketsReceived.setStatus("current")
_SdWANStatsWANPathBOWTms_Type = Gauge32
_SdWANStatsWANPathBOWTms_Object = MibTableColumn
sdWANStatsWANPathBOWTms = _SdWANStatsWANPathBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 11),
    _SdWANStatsWANPathBOWTms_Type()
)
sdWANStatsWANPathBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathBOWTms.setStatus("current")
_SdWANStatsWANPathJitterms_Type = Gauge32
_SdWANStatsWANPathJitterms_Object = MibTableColumn
sdWANStatsWANPathJitterms = _SdWANStatsWANPathJitterms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 12),
    _SdWANStatsWANPathJitterms_Type()
)
sdWANStatsWANPathJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathJitterms.setStatus("current")
_SdWANStatsWANPathPacketsLost_Type = Counter64
_SdWANStatsWANPathPacketsLost_Object = MibTableColumn
sdWANStatsWANPathPacketsLost = _SdWANStatsWANPathPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 13),
    _SdWANStatsWANPathPacketsLost_Type()
)
sdWANStatsWANPathPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathPacketsLost.setStatus("current")
_SdWANStatsWANPathPacketsOOO_Type = Counter64
_SdWANStatsWANPathPacketsOOO_Object = MibTableColumn
sdWANStatsWANPathPacketsOOO = _SdWANStatsWANPathPacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 3, 1, 1, 14),
    _SdWANStatsWANPathPacketsOOO_Type()
)
sdWANStatsWANPathPacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANPathPacketsOOO.setStatus("current")
_SdWANStatsWANClasses_ObjectIdentity = ObjectIdentity
sdWANStatsWANClasses = _SdWANStatsWANClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4)
)
_SdWANStatsWANClassTable_Object = MibTable
sdWANStatsWANClassTable = _SdWANStatsWANClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1)
)
if mibBuilder.loadTexts:
    sdWANStatsWANClassTable.setStatus("current")
_SdWANStatsWANClassEntry_Object = MibTableRow
sdWANStatsWANClassEntry = _SdWANStatsWANClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1)
)
sdWANStatsWANClassEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsWANClassVPathIndex"),
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsWANClassClassIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsWANClassEntry.setStatus("current")
_SdWANStatsWANClassVPathIndex_Type = Integer32
_SdWANStatsWANClassVPathIndex_Object = MibTableColumn
sdWANStatsWANClassVPathIndex = _SdWANStatsWANClassVPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 1),
    _SdWANStatsWANClassVPathIndex_Type()
)
sdWANStatsWANClassVPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassVPathIndex.setStatus("current")
_SdWANStatsWANClassClassIndex_Type = Integer32
_SdWANStatsWANClassClassIndex_Object = MibTableColumn
sdWANStatsWANClassClassIndex = _SdWANStatsWANClassClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 2),
    _SdWANStatsWANClassClassIndex_Type()
)
sdWANStatsWANClassClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassClassIndex.setStatus("current")
_SdWANStatsWANClassVPathID_Type = Integer32
_SdWANStatsWANClassVPathID_Object = MibTableColumn
sdWANStatsWANClassVPathID = _SdWANStatsWANClassVPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 3),
    _SdWANStatsWANClassVPathID_Type()
)
sdWANStatsWANClassVPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassVPathID.setStatus("current")
_SdWANStatsWANClassClassID_Type = Integer32
_SdWANStatsWANClassClassID_Object = MibTableColumn
sdWANStatsWANClassClassID = _SdWANStatsWANClassClassID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 4),
    _SdWANStatsWANClassClassID_Type()
)
sdWANStatsWANClassClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassClassID.setStatus("current")
_SdWANStatsWANClassName_Type = DisplayString
_SdWANStatsWANClassName_Object = MibTableColumn
sdWANStatsWANClassName = _SdWANStatsWANClassName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 5),
    _SdWANStatsWANClassName_Type()
)
sdWANStatsWANClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassName.setStatus("current")


class _SdWANStatsWANClassType_Type(Integer32):
    """Custom type sdWANStatsWANClassType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("realtime", 1),
          ("interactive", 2),
          ("bulk", 3),
          ("unknown", 4))
    )


_SdWANStatsWANClassType_Type.__name__ = "Integer32"
_SdWANStatsWANClassType_Object = MibTableColumn
sdWANStatsWANClassType = _SdWANStatsWANClassType_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 6),
    _SdWANStatsWANClassType_Type()
)
sdWANStatsWANClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassType.setStatus("current")
_SdWANStatsWANClassBytesSent_Type = Counter64
_SdWANStatsWANClassBytesSent_Object = MibTableColumn
sdWANStatsWANClassBytesSent = _SdWANStatsWANClassBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 7),
    _SdWANStatsWANClassBytesSent_Type()
)
sdWANStatsWANClassBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassBytesSent.setStatus("current")
_SdWANStatsWANClassPacketsSent_Type = Counter64
_SdWANStatsWANClassPacketsSent_Object = MibTableColumn
sdWANStatsWANClassPacketsSent = _SdWANStatsWANClassPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 8),
    _SdWANStatsWANClassPacketsSent_Type()
)
sdWANStatsWANClassPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassPacketsSent.setStatus("current")
_SdWANStatsWANClassBytesPending_Type = Counter64
_SdWANStatsWANClassBytesPending_Object = MibTableColumn
sdWANStatsWANClassBytesPending = _SdWANStatsWANClassBytesPending_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 9),
    _SdWANStatsWANClassBytesPending_Type()
)
sdWANStatsWANClassBytesPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassBytesPending.setStatus("current")
_SdWANStatsWANClassPacketsPending_Type = Counter64
_SdWANStatsWANClassPacketsPending_Object = MibTableColumn
sdWANStatsWANClassPacketsPending = _SdWANStatsWANClassPacketsPending_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 10),
    _SdWANStatsWANClassPacketsPending_Type()
)
sdWANStatsWANClassPacketsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassPacketsPending.setStatus("current")
_SdWANStatsWANClassBytesDropped_Type = Counter64
_SdWANStatsWANClassBytesDropped_Object = MibTableColumn
sdWANStatsWANClassBytesDropped = _SdWANStatsWANClassBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 11),
    _SdWANStatsWANClassBytesDropped_Type()
)
sdWANStatsWANClassBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassBytesDropped.setStatus("current")
_SdWANStatsWANClassPacketsDropped_Type = Counter64
_SdWANStatsWANClassPacketsDropped_Object = MibTableColumn
sdWANStatsWANClassPacketsDropped = _SdWANStatsWANClassPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 4, 1, 1, 12),
    _SdWANStatsWANClassPacketsDropped_Type()
)
sdWANStatsWANClassPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANClassPacketsDropped.setStatus("current")
_SdWANStatsWANRules_ObjectIdentity = ObjectIdentity
sdWANStatsWANRules = _SdWANStatsWANRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5)
)
_SdWANStatsWANRuleTable_Object = MibTable
sdWANStatsWANRuleTable = _SdWANStatsWANRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1)
)
if mibBuilder.loadTexts:
    sdWANStatsWANRuleTable.setStatus("current")
_SdWANStatsWANRuleEntry_Object = MibTableRow
sdWANStatsWANRuleEntry = _SdWANStatsWANRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1)
)
sdWANStatsWANRuleEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsWANRuleVPathIndex"),
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsWANRuleRuleIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsWANRuleEntry.setStatus("current")
_SdWANStatsWANRuleVPathIndex_Type = Integer32
_SdWANStatsWANRuleVPathIndex_Object = MibTableColumn
sdWANStatsWANRuleVPathIndex = _SdWANStatsWANRuleVPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 1),
    _SdWANStatsWANRuleVPathIndex_Type()
)
sdWANStatsWANRuleVPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleVPathIndex.setStatus("current")
_SdWANStatsWANRuleRuleIndex_Type = Integer32
_SdWANStatsWANRuleRuleIndex_Object = MibTableColumn
sdWANStatsWANRuleRuleIndex = _SdWANStatsWANRuleRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 2),
    _SdWANStatsWANRuleRuleIndex_Type()
)
sdWANStatsWANRuleRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleRuleIndex.setStatus("current")
_SdWANStatsWANRuleVPathID_Type = Integer32
_SdWANStatsWANRuleVPathID_Object = MibTableColumn
sdWANStatsWANRuleVPathID = _SdWANStatsWANRuleVPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 3),
    _SdWANStatsWANRuleVPathID_Type()
)
sdWANStatsWANRuleVPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleVPathID.setStatus("current")
_SdWANStatsWANRuleRuleID_Type = Integer32
_SdWANStatsWANRuleRuleID_Object = MibTableColumn
sdWANStatsWANRuleRuleID = _SdWANStatsWANRuleRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 4),
    _SdWANStatsWANRuleRuleID_Type()
)
sdWANStatsWANRuleRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleRuleID.setStatus("current")
_SdWANStatsWANRuleGlobalRuleIndex_Type = Integer32
_SdWANStatsWANRuleGlobalRuleIndex_Object = MibTableColumn
sdWANStatsWANRuleGlobalRuleIndex = _SdWANStatsWANRuleGlobalRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 5),
    _SdWANStatsWANRuleGlobalRuleIndex_Type()
)
sdWANStatsWANRuleGlobalRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleGlobalRuleIndex.setStatus("current")
_SdWANStatsWANRuleApplicationName_Type = DisplayString
_SdWANStatsWANRuleApplicationName_Object = MibTableColumn
sdWANStatsWANRuleApplicationName = _SdWANStatsWANRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 6),
    _SdWANStatsWANRuleApplicationName_Type()
)
sdWANStatsWANRuleApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleApplicationName.setStatus("current")
_SdWANStatsWANRuleLANToWANHitCount_Type = Gauge32
_SdWANStatsWANRuleLANToWANHitCount_Object = MibTableColumn
sdWANStatsWANRuleLANToWANHitCount = _SdWANStatsWANRuleLANToWANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 7),
    _SdWANStatsWANRuleLANToWANHitCount_Type()
)
sdWANStatsWANRuleLANToWANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleLANToWANHitCount.setStatus("current")
_SdWANStatsWANRuleWANToLANHitCount_Type = Gauge32
_SdWANStatsWANRuleWANToLANHitCount_Object = MibTableColumn
sdWANStatsWANRuleWANToLANHitCount = _SdWANStatsWANRuleWANToLANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 8),
    _SdWANStatsWANRuleWANToLANHitCount_Type()
)
sdWANStatsWANRuleWANToLANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleWANToLANHitCount.setStatus("current")
_SdWANStatsWANRuleBytesSent_Type = Gauge32
_SdWANStatsWANRuleBytesSent_Object = MibTableColumn
sdWANStatsWANRuleBytesSent = _SdWANStatsWANRuleBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 9),
    _SdWANStatsWANRuleBytesSent_Type()
)
sdWANStatsWANRuleBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleBytesSent.setStatus("current")
_SdWANStatsWANRulePacketsSent_Type = Gauge32
_SdWANStatsWANRulePacketsSent_Object = MibTableColumn
sdWANStatsWANRulePacketsSent = _SdWANStatsWANRulePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 10),
    _SdWANStatsWANRulePacketsSent_Type()
)
sdWANStatsWANRulePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRulePacketsSent.setStatus("current")
_SdWANStatsWANRuleBytesReceived_Type = Gauge32
_SdWANStatsWANRuleBytesReceived_Object = MibTableColumn
sdWANStatsWANRuleBytesReceived = _SdWANStatsWANRuleBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 11),
    _SdWANStatsWANRuleBytesReceived_Type()
)
sdWANStatsWANRuleBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleBytesReceived.setStatus("current")
_SdWANStatsWANRulePacketsReceived_Type = Gauge32
_SdWANStatsWANRulePacketsReceived_Object = MibTableColumn
sdWANStatsWANRulePacketsReceived = _SdWANStatsWANRulePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 12),
    _SdWANStatsWANRulePacketsReceived_Type()
)
sdWANStatsWANRulePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRulePacketsReceived.setStatus("current")
_SdWANStatsWANRuleBytesDropped_Type = Gauge32
_SdWANStatsWANRuleBytesDropped_Object = MibTableColumn
sdWANStatsWANRuleBytesDropped = _SdWANStatsWANRuleBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 13),
    _SdWANStatsWANRuleBytesDropped_Type()
)
sdWANStatsWANRuleBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleBytesDropped.setStatus("current")
_SdWANStatsWANRulePacketsDropped_Type = Gauge32
_SdWANStatsWANRulePacketsDropped_Object = MibTableColumn
sdWANStatsWANRulePacketsDropped = _SdWANStatsWANRulePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 14),
    _SdWANStatsWANRulePacketsDropped_Type()
)
sdWANStatsWANRulePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRulePacketsDropped.setStatus("current")
_SdWANStatsWANRuleLastActiveNMinuteAgo_Type = TimeTicks
_SdWANStatsWANRuleLastActiveNMinuteAgo_Object = MibTableColumn
sdWANStatsWANRuleLastActiveNMinuteAgo = _SdWANStatsWANRuleLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 16, 5, 1, 1, 15),
    _SdWANStatsWANRuleLastActiveNMinuteAgo_Type()
)
sdWANStatsWANRuleLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsWANRuleLastActiveNMinuteAgo.setStatus("current")
_SdWANStatsInternet_ObjectIdentity = ObjectIdentity
sdWANStatsInternet = _SdWANStatsInternet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17)
)
_SdWANStatsInternetScalars_ObjectIdentity = ObjectIdentity
sdWANStatsInternetScalars = _SdWANStatsInternetScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 1)
)


class _SdWANStatsInternetBytesSent_Type(Counter64):
    """Custom type sdWANStatsInternetBytesSent based on Counter64"""
    defaultValue = 0


_SdWANStatsInternetBytesSent_Type.__name__ = "Counter64"
_SdWANStatsInternetBytesSent_Object = MibScalar
sdWANStatsInternetBytesSent = _SdWANStatsInternetBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 1, 1),
    _SdWANStatsInternetBytesSent_Type()
)
sdWANStatsInternetBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetBytesSent.setStatus("current")


class _SdWANStatsInternetPacketsSent_Type(Counter64):
    """Custom type sdWANStatsInternetPacketsSent based on Counter64"""
    defaultValue = 0


_SdWANStatsInternetPacketsSent_Type.__name__ = "Counter64"
_SdWANStatsInternetPacketsSent_Object = MibScalar
sdWANStatsInternetPacketsSent = _SdWANStatsInternetPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 1, 2),
    _SdWANStatsInternetPacketsSent_Type()
)
sdWANStatsInternetPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetPacketsSent.setStatus("current")


class _SdWANStatsInternetBytesReceived_Type(Counter64):
    """Custom type sdWANStatsInternetBytesReceived based on Counter64"""
    defaultValue = 0


_SdWANStatsInternetBytesReceived_Type.__name__ = "Counter64"
_SdWANStatsInternetBytesReceived_Object = MibScalar
sdWANStatsInternetBytesReceived = _SdWANStatsInternetBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 1, 3),
    _SdWANStatsInternetBytesReceived_Type()
)
sdWANStatsInternetBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetBytesReceived.setStatus("current")


class _SdWANStatsInternetPacketsReceived_Type(Counter64):
    """Custom type sdWANStatsInternetPacketsReceived based on Counter64"""
    defaultValue = 0


_SdWANStatsInternetPacketsReceived_Type.__name__ = "Counter64"
_SdWANStatsInternetPacketsReceived_Object = MibScalar
sdWANStatsInternetPacketsReceived = _SdWANStatsInternetPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 1, 4),
    _SdWANStatsInternetPacketsReceived_Type()
)
sdWANStatsInternetPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetPacketsReceived.setStatus("current")


class _SdWANStatsInternetBytesDropped_Type(Counter64):
    """Custom type sdWANStatsInternetBytesDropped based on Counter64"""
    defaultValue = 0


_SdWANStatsInternetBytesDropped_Type.__name__ = "Counter64"
_SdWANStatsInternetBytesDropped_Object = MibScalar
sdWANStatsInternetBytesDropped = _SdWANStatsInternetBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 1, 5),
    _SdWANStatsInternetBytesDropped_Type()
)
sdWANStatsInternetBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetBytesDropped.setStatus("current")


class _SdWANStatsInternetPacketsDropped_Type(Counter64):
    """Custom type sdWANStatsInternetPacketsDropped based on Counter64"""
    defaultValue = 0


_SdWANStatsInternetPacketsDropped_Type.__name__ = "Counter64"
_SdWANStatsInternetPacketsDropped_Object = MibScalar
sdWANStatsInternetPacketsDropped = _SdWANStatsInternetPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 1, 6),
    _SdWANStatsInternetPacketsDropped_Type()
)
sdWANStatsInternetPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetPacketsDropped.setStatus("current")


class _SdWANStatsInternetNumRules_Type(Integer32):
    """Custom type sdWANStatsInternetNumRules based on Integer32"""
    defaultValue = 0


_SdWANStatsInternetNumRules_Type.__name__ = "Integer32"
_SdWANStatsInternetNumRules_Object = MibScalar
sdWANStatsInternetNumRules = _SdWANStatsInternetNumRules_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 1, 7),
    _SdWANStatsInternetNumRules_Type()
)
sdWANStatsInternetNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetNumRules.setStatus("current")
_SdWANStatsInternetRuleTable_Object = MibTable
sdWANStatsInternetRuleTable = _SdWANStatsInternetRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2)
)
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleTable.setStatus("current")
_SdWANStatsInternetRuleEntry_Object = MibTableRow
sdWANStatsInternetRuleEntry = _SdWANStatsInternetRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1)
)
sdWANStatsInternetRuleEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsInternetRuleIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleEntry.setStatus("current")
_SdWANStatsInternetRuleIndex_Type = Integer32
_SdWANStatsInternetRuleIndex_Object = MibTableColumn
sdWANStatsInternetRuleIndex = _SdWANStatsInternetRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 1),
    _SdWANStatsInternetRuleIndex_Type()
)
sdWANStatsInternetRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleIndex.setStatus("current")
_SdWANStatsInternetRuleID_Type = Integer32
_SdWANStatsInternetRuleID_Object = MibTableColumn
sdWANStatsInternetRuleID = _SdWANStatsInternetRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 2),
    _SdWANStatsInternetRuleID_Type()
)
sdWANStatsInternetRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleID.setStatus("current")
_SdWANStatsInternetRuleGlobalRuleIndex_Type = Integer32
_SdWANStatsInternetRuleGlobalRuleIndex_Object = MibTableColumn
sdWANStatsInternetRuleGlobalRuleIndex = _SdWANStatsInternetRuleGlobalRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 3),
    _SdWANStatsInternetRuleGlobalRuleIndex_Type()
)
sdWANStatsInternetRuleGlobalRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleGlobalRuleIndex.setStatus("current")
_SdWANStatsInternetRuleApplicationName_Type = DisplayString
_SdWANStatsInternetRuleApplicationName_Object = MibTableColumn
sdWANStatsInternetRuleApplicationName = _SdWANStatsInternetRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 4),
    _SdWANStatsInternetRuleApplicationName_Type()
)
sdWANStatsInternetRuleApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleApplicationName.setStatus("current")
_SdWANStatsInternetRuleLANToWANHitCount_Type = Gauge32
_SdWANStatsInternetRuleLANToWANHitCount_Object = MibTableColumn
sdWANStatsInternetRuleLANToWANHitCount = _SdWANStatsInternetRuleLANToWANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 5),
    _SdWANStatsInternetRuleLANToWANHitCount_Type()
)
sdWANStatsInternetRuleLANToWANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleLANToWANHitCount.setStatus("current")
_SdWANStatsInternetRuleWANToLANHitCount_Type = Gauge32
_SdWANStatsInternetRuleWANToLANHitCount_Object = MibTableColumn
sdWANStatsInternetRuleWANToLANHitCount = _SdWANStatsInternetRuleWANToLANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 6),
    _SdWANStatsInternetRuleWANToLANHitCount_Type()
)
sdWANStatsInternetRuleWANToLANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleWANToLANHitCount.setStatus("current")
_SdWANStatsInternetRuleBytesSent_Type = Gauge32
_SdWANStatsInternetRuleBytesSent_Object = MibTableColumn
sdWANStatsInternetRuleBytesSent = _SdWANStatsInternetRuleBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 7),
    _SdWANStatsInternetRuleBytesSent_Type()
)
sdWANStatsInternetRuleBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleBytesSent.setStatus("current")
_SdWANStatsInternetRulePacketsSent_Type = Gauge32
_SdWANStatsInternetRulePacketsSent_Object = MibTableColumn
sdWANStatsInternetRulePacketsSent = _SdWANStatsInternetRulePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 8),
    _SdWANStatsInternetRulePacketsSent_Type()
)
sdWANStatsInternetRulePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRulePacketsSent.setStatus("current")
_SdWANStatsInternetRuleBytesReceived_Type = Gauge32
_SdWANStatsInternetRuleBytesReceived_Object = MibTableColumn
sdWANStatsInternetRuleBytesReceived = _SdWANStatsInternetRuleBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 9),
    _SdWANStatsInternetRuleBytesReceived_Type()
)
sdWANStatsInternetRuleBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleBytesReceived.setStatus("current")
_SdWANStatsInternetRulePacketsReceived_Type = Gauge32
_SdWANStatsInternetRulePacketsReceived_Object = MibTableColumn
sdWANStatsInternetRulePacketsReceived = _SdWANStatsInternetRulePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 10),
    _SdWANStatsInternetRulePacketsReceived_Type()
)
sdWANStatsInternetRulePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRulePacketsReceived.setStatus("current")
_SdWANStatsInternetRuleBytesDropped_Type = Gauge32
_SdWANStatsInternetRuleBytesDropped_Object = MibTableColumn
sdWANStatsInternetRuleBytesDropped = _SdWANStatsInternetRuleBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 11),
    _SdWANStatsInternetRuleBytesDropped_Type()
)
sdWANStatsInternetRuleBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleBytesDropped.setStatus("current")
_SdWANStatsInternetRulePacketsDropped_Type = Gauge32
_SdWANStatsInternetRulePacketsDropped_Object = MibTableColumn
sdWANStatsInternetRulePacketsDropped = _SdWANStatsInternetRulePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 12),
    _SdWANStatsInternetRulePacketsDropped_Type()
)
sdWANStatsInternetRulePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRulePacketsDropped.setStatus("current")
_SdWANStatsInternetRuleLastActiveNMinuteAgo_Type = TimeTicks
_SdWANStatsInternetRuleLastActiveNMinuteAgo_Object = MibTableColumn
sdWANStatsInternetRuleLastActiveNMinuteAgo = _SdWANStatsInternetRuleLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 17, 2, 1, 13),
    _SdWANStatsInternetRuleLastActiveNMinuteAgo_Type()
)
sdWANStatsInternetRuleLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsInternetRuleLastActiveNMinuteAgo.setStatus("current")
_SdWANStatsIntranet_ObjectIdentity = ObjectIdentity
sdWANStatsIntranet = _SdWANStatsIntranet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18)
)
_SdWANStatsIntranetScalars_ObjectIdentity = ObjectIdentity
sdWANStatsIntranetScalars = _SdWANStatsIntranetScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 1)
)


class _SdWANStatsIntranetNumIntranetServices_Type(Integer32):
    """Custom type sdWANStatsIntranetNumIntranetServices based on Integer32"""
    defaultValue = 0


_SdWANStatsIntranetNumIntranetServices_Type.__name__ = "Integer32"
_SdWANStatsIntranetNumIntranetServices_Object = MibScalar
sdWANStatsIntranetNumIntranetServices = _SdWANStatsIntranetNumIntranetServices_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 1, 8),
    _SdWANStatsIntranetNumIntranetServices_Type()
)
sdWANStatsIntranetNumIntranetServices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetNumIntranetServices.setStatus("current")
_SdWANStatsIntranetsTable_Object = MibTable
sdWANStatsIntranetsTable = _SdWANStatsIntranetsTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3)
)
if mibBuilder.loadTexts:
    sdWANStatsIntranetsTable.setStatus("current")
_SdWANStatsIntranetsEntry_Object = MibTableRow
sdWANStatsIntranetsEntry = _SdWANStatsIntranetsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1)
)
sdWANStatsIntranetsEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsIntranetsIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsIntranetsEntry.setStatus("current")
_SdWANStatsIntranetsIndex_Type = Integer32
_SdWANStatsIntranetsIndex_Object = MibTableColumn
sdWANStatsIntranetsIndex = _SdWANStatsIntranetsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 1),
    _SdWANStatsIntranetsIndex_Type()
)
sdWANStatsIntranetsIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsIndex.setStatus("current")
_SdWANStatsIntranetsID_Type = Integer32
_SdWANStatsIntranetsID_Object = MibTableColumn
sdWANStatsIntranetsID = _SdWANStatsIntranetsID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 2),
    _SdWANStatsIntranetsID_Type()
)
sdWANStatsIntranetsID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsID.setStatus("current")
_SdWANStatsIntranetsName_Type = DisplayString
_SdWANStatsIntranetsName_Object = MibTableColumn
sdWANStatsIntranetsName = _SdWANStatsIntranetsName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 3),
    _SdWANStatsIntranetsName_Type()
)
sdWANStatsIntranetsName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsName.setStatus("current")
_SdWANStatsIntranetsBytesSent_Type = Counter64
_SdWANStatsIntranetsBytesSent_Object = MibTableColumn
sdWANStatsIntranetsBytesSent = _SdWANStatsIntranetsBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 4),
    _SdWANStatsIntranetsBytesSent_Type()
)
sdWANStatsIntranetsBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsBytesSent.setStatus("current")
_SdWANStatsIntranetsPacketsSent_Type = Counter64
_SdWANStatsIntranetsPacketsSent_Object = MibTableColumn
sdWANStatsIntranetsPacketsSent = _SdWANStatsIntranetsPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 5),
    _SdWANStatsIntranetsPacketsSent_Type()
)
sdWANStatsIntranetsPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsPacketsSent.setStatus("current")
_SdWANStatsIntranetsBytesReceived_Type = Counter64
_SdWANStatsIntranetsBytesReceived_Object = MibTableColumn
sdWANStatsIntranetsBytesReceived = _SdWANStatsIntranetsBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 6),
    _SdWANStatsIntranetsBytesReceived_Type()
)
sdWANStatsIntranetsBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsBytesReceived.setStatus("current")
_SdWANStatsIntranetsPacketsReceived_Type = Counter64
_SdWANStatsIntranetsPacketsReceived_Object = MibTableColumn
sdWANStatsIntranetsPacketsReceived = _SdWANStatsIntranetsPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 7),
    _SdWANStatsIntranetsPacketsReceived_Type()
)
sdWANStatsIntranetsPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsPacketsReceived.setStatus("current")
_SdWANStatsIntranetsBytesDropped_Type = Counter64
_SdWANStatsIntranetsBytesDropped_Object = MibTableColumn
sdWANStatsIntranetsBytesDropped = _SdWANStatsIntranetsBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 8),
    _SdWANStatsIntranetsBytesDropped_Type()
)
sdWANStatsIntranetsBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsBytesDropped.setStatus("current")
_SdWANStatsIntranetsPacketsDropped_Type = Counter64
_SdWANStatsIntranetsPacketsDropped_Object = MibTableColumn
sdWANStatsIntranetsPacketsDropped = _SdWANStatsIntranetsPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 9),
    _SdWANStatsIntranetsPacketsDropped_Type()
)
sdWANStatsIntranetsPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsPacketsDropped.setStatus("current")
_SdWANStatsIntranetsNumRules_Type = Integer32
_SdWANStatsIntranetsNumRules_Object = MibTableColumn
sdWANStatsIntranetsNumRules = _SdWANStatsIntranetsNumRules_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 10),
    _SdWANStatsIntranetsNumRules_Type()
)
sdWANStatsIntranetsNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsNumRules.setStatus("current")
_SdWANStatsIntranetsRoutingDomainName_Type = DisplayString
_SdWANStatsIntranetsRoutingDomainName_Object = MibTableColumn
sdWANStatsIntranetsRoutingDomainName = _SdWANStatsIntranetsRoutingDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 3, 1, 11),
    _SdWANStatsIntranetsRoutingDomainName_Type()
)
sdWANStatsIntranetsRoutingDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetsRoutingDomainName.setStatus("current")
_SdWANStatsIntranetRulesTable_Object = MibTable
sdWANStatsIntranetRulesTable = _SdWANStatsIntranetRulesTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4)
)
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesTable.setStatus("current")
_SdWANStatsIntranetRulesEntry_Object = MibTableRow
sdWANStatsIntranetRulesEntry = _SdWANStatsIntranetRulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1)
)
sdWANStatsIntranetRulesEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsIntranetRulesIntranetIndex"),
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsIntranetRulesRuleIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesEntry.setStatus("current")
_SdWANStatsIntranetRulesIntranetIndex_Type = Integer32
_SdWANStatsIntranetRulesIntranetIndex_Object = MibTableColumn
sdWANStatsIntranetRulesIntranetIndex = _SdWANStatsIntranetRulesIntranetIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 1),
    _SdWANStatsIntranetRulesIntranetIndex_Type()
)
sdWANStatsIntranetRulesIntranetIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesIntranetIndex.setStatus("current")
_SdWANStatsIntranetRulesRuleIndex_Type = Integer32
_SdWANStatsIntranetRulesRuleIndex_Object = MibTableColumn
sdWANStatsIntranetRulesRuleIndex = _SdWANStatsIntranetRulesRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 2),
    _SdWANStatsIntranetRulesRuleIndex_Type()
)
sdWANStatsIntranetRulesRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesRuleIndex.setStatus("current")
_SdWANStatsIntranetRulesID_Type = Integer32
_SdWANStatsIntranetRulesID_Object = MibTableColumn
sdWANStatsIntranetRulesID = _SdWANStatsIntranetRulesID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 3),
    _SdWANStatsIntranetRulesID_Type()
)
sdWANStatsIntranetRulesID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesID.setStatus("current")
_SdWANStatsIntranetRulesGlobalRuleIndex_Type = Integer32
_SdWANStatsIntranetRulesGlobalRuleIndex_Object = MibTableColumn
sdWANStatsIntranetRulesGlobalRuleIndex = _SdWANStatsIntranetRulesGlobalRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 4),
    _SdWANStatsIntranetRulesGlobalRuleIndex_Type()
)
sdWANStatsIntranetRulesGlobalRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesGlobalRuleIndex.setStatus("current")
_SdWANStatsIntranetRulesIntranetName_Type = DisplayString
_SdWANStatsIntranetRulesIntranetName_Object = MibTableColumn
sdWANStatsIntranetRulesIntranetName = _SdWANStatsIntranetRulesIntranetName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 5),
    _SdWANStatsIntranetRulesIntranetName_Type()
)
sdWANStatsIntranetRulesIntranetName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesIntranetName.setStatus("current")
_SdWANStatsIntranetRulesApplicationName_Type = DisplayString
_SdWANStatsIntranetRulesApplicationName_Object = MibTableColumn
sdWANStatsIntranetRulesApplicationName = _SdWANStatsIntranetRulesApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 6),
    _SdWANStatsIntranetRulesApplicationName_Type()
)
sdWANStatsIntranetRulesApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesApplicationName.setStatus("current")
_SdWANStatsIntranetRulesLANToWANHitCount_Type = Gauge32
_SdWANStatsIntranetRulesLANToWANHitCount_Object = MibTableColumn
sdWANStatsIntranetRulesLANToWANHitCount = _SdWANStatsIntranetRulesLANToWANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 7),
    _SdWANStatsIntranetRulesLANToWANHitCount_Type()
)
sdWANStatsIntranetRulesLANToWANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesLANToWANHitCount.setStatus("current")
_SdWANStatsIntranetRulesWANToLANHitCount_Type = Gauge32
_SdWANStatsIntranetRulesWANToLANHitCount_Object = MibTableColumn
sdWANStatsIntranetRulesWANToLANHitCount = _SdWANStatsIntranetRulesWANToLANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 8),
    _SdWANStatsIntranetRulesWANToLANHitCount_Type()
)
sdWANStatsIntranetRulesWANToLANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesWANToLANHitCount.setStatus("current")
_SdWANStatsIntranetRulesBytesSent_Type = Gauge32
_SdWANStatsIntranetRulesBytesSent_Object = MibTableColumn
sdWANStatsIntranetRulesBytesSent = _SdWANStatsIntranetRulesBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 9),
    _SdWANStatsIntranetRulesBytesSent_Type()
)
sdWANStatsIntranetRulesBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesBytesSent.setStatus("current")
_SdWANStatsIntranetRulesPacketsSent_Type = Gauge32
_SdWANStatsIntranetRulesPacketsSent_Object = MibTableColumn
sdWANStatsIntranetRulesPacketsSent = _SdWANStatsIntranetRulesPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 10),
    _SdWANStatsIntranetRulesPacketsSent_Type()
)
sdWANStatsIntranetRulesPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesPacketsSent.setStatus("current")
_SdWANStatsIntranetRulesBytesReceived_Type = Gauge32
_SdWANStatsIntranetRulesBytesReceived_Object = MibTableColumn
sdWANStatsIntranetRulesBytesReceived = _SdWANStatsIntranetRulesBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 11),
    _SdWANStatsIntranetRulesBytesReceived_Type()
)
sdWANStatsIntranetRulesBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesBytesReceived.setStatus("current")
_SdWANStatsIntranetRulesPacketsReceived_Type = Gauge32
_SdWANStatsIntranetRulesPacketsReceived_Object = MibTableColumn
sdWANStatsIntranetRulesPacketsReceived = _SdWANStatsIntranetRulesPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 12),
    _SdWANStatsIntranetRulesPacketsReceived_Type()
)
sdWANStatsIntranetRulesPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesPacketsReceived.setStatus("current")
_SdWANStatsIntranetRulesBytesDropped_Type = Gauge32
_SdWANStatsIntranetRulesBytesDropped_Object = MibTableColumn
sdWANStatsIntranetRulesBytesDropped = _SdWANStatsIntranetRulesBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 13),
    _SdWANStatsIntranetRulesBytesDropped_Type()
)
sdWANStatsIntranetRulesBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesBytesDropped.setStatus("current")
_SdWANStatsIntranetRulesPacketsDropped_Type = Gauge32
_SdWANStatsIntranetRulesPacketsDropped_Object = MibTableColumn
sdWANStatsIntranetRulesPacketsDropped = _SdWANStatsIntranetRulesPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 14),
    _SdWANStatsIntranetRulesPacketsDropped_Type()
)
sdWANStatsIntranetRulesPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesPacketsDropped.setStatus("current")
_SdWANStatsIntranetRulesLastActiveNMinuteAgo_Type = TimeTicks
_SdWANStatsIntranetRulesLastActiveNMinuteAgo_Object = MibTableColumn
sdWANStatsIntranetRulesLastActiveNMinuteAgo = _SdWANStatsIntranetRulesLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 18, 4, 1, 15),
    _SdWANStatsIntranetRulesLastActiveNMinuteAgo_Type()
)
sdWANStatsIntranetRulesLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsIntranetRulesLastActiveNMinuteAgo.setStatus("current")
_SdWANStatsPassthrough_ObjectIdentity = ObjectIdentity
sdWANStatsPassthrough = _SdWANStatsPassthrough_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 19)
)
_SdWANStatsPassthroughScalars_ObjectIdentity = ObjectIdentity
sdWANStatsPassthroughScalars = _SdWANStatsPassthroughScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 19, 1)
)


class _SdWANStatsPassthroughBytesSent_Type(Counter64):
    """Custom type sdWANStatsPassthroughBytesSent based on Counter64"""
    defaultValue = 0


_SdWANStatsPassthroughBytesSent_Type.__name__ = "Counter64"
_SdWANStatsPassthroughBytesSent_Object = MibScalar
sdWANStatsPassthroughBytesSent = _SdWANStatsPassthroughBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 19, 1, 1),
    _SdWANStatsPassthroughBytesSent_Type()
)
sdWANStatsPassthroughBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsPassthroughBytesSent.setStatus("current")


class _SdWANStatsPassthroughPacketsSent_Type(Counter64):
    """Custom type sdWANStatsPassthroughPacketsSent based on Counter64"""
    defaultValue = 0


_SdWANStatsPassthroughPacketsSent_Type.__name__ = "Counter64"
_SdWANStatsPassthroughPacketsSent_Object = MibScalar
sdWANStatsPassthroughPacketsSent = _SdWANStatsPassthroughPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 19, 1, 2),
    _SdWANStatsPassthroughPacketsSent_Type()
)
sdWANStatsPassthroughPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsPassthroughPacketsSent.setStatus("current")


class _SdWANStatsPassthroughBytesReceived_Type(Counter64):
    """Custom type sdWANStatsPassthroughBytesReceived based on Counter64"""
    defaultValue = 0


_SdWANStatsPassthroughBytesReceived_Type.__name__ = "Counter64"
_SdWANStatsPassthroughBytesReceived_Object = MibScalar
sdWANStatsPassthroughBytesReceived = _SdWANStatsPassthroughBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 19, 1, 3),
    _SdWANStatsPassthroughBytesReceived_Type()
)
sdWANStatsPassthroughBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsPassthroughBytesReceived.setStatus("current")


class _SdWANStatsPassthroughPacketsReceived_Type(Counter64):
    """Custom type sdWANStatsPassthroughPacketsReceived based on Counter64"""
    defaultValue = 0


_SdWANStatsPassthroughPacketsReceived_Type.__name__ = "Counter64"
_SdWANStatsPassthroughPacketsReceived_Object = MibScalar
sdWANStatsPassthroughPacketsReceived = _SdWANStatsPassthroughPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 19, 1, 4),
    _SdWANStatsPassthroughPacketsReceived_Type()
)
sdWANStatsPassthroughPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsPassthroughPacketsReceived.setStatus("current")


class _SdWANStatsPassthroughBytesDropped_Type(Counter64):
    """Custom type sdWANStatsPassthroughBytesDropped based on Counter64"""
    defaultValue = 0


_SdWANStatsPassthroughBytesDropped_Type.__name__ = "Counter64"
_SdWANStatsPassthroughBytesDropped_Object = MibScalar
sdWANStatsPassthroughBytesDropped = _SdWANStatsPassthroughBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 19, 1, 5),
    _SdWANStatsPassthroughBytesDropped_Type()
)
sdWANStatsPassthroughBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsPassthroughBytesDropped.setStatus("current")


class _SdWANStatsPassthroughPacketsDropped_Type(Counter64):
    """Custom type sdWANStatsPassthroughPacketsDropped based on Counter64"""
    defaultValue = 0


_SdWANStatsPassthroughPacketsDropped_Type.__name__ = "Counter64"
_SdWANStatsPassthroughPacketsDropped_Object = MibScalar
sdWANStatsPassthroughPacketsDropped = _SdWANStatsPassthroughPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 19, 1, 6),
    _SdWANStatsPassthroughPacketsDropped_Type()
)
sdWANStatsPassthroughPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsPassthroughPacketsDropped.setStatus("current")
_SdWANStatsRoutesV2_ObjectIdentity = ObjectIdentity
sdWANStatsRoutesV2 = _SdWANStatsRoutesV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20)
)
_SdWANStatsRouteScalars_ObjectIdentity = ObjectIdentity
sdWANStatsRouteScalars = _SdWANStatsRouteScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 1)
)


class _SdWANStatsNumRoutesV2_Type(Gauge32):
    """Custom type sdWANStatsNumRoutesV2 based on Gauge32"""
    defaultValue = 0


_SdWANStatsNumRoutesV2_Type.__name__ = "Gauge32"
_SdWANStatsNumRoutesV2_Object = MibScalar
sdWANStatsNumRoutesV2 = _SdWANStatsNumRoutesV2_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 1, 1),
    _SdWANStatsNumRoutesV2_Type()
)
sdWANStatsNumRoutesV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsNumRoutesV2.setStatus("current")
_SdWANStatsRouteTableV2_Object = MibTable
sdWANStatsRouteTableV2 = _SdWANStatsRouteTableV2_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2)
)
if mibBuilder.loadTexts:
    sdWANStatsRouteTableV2.setStatus("current")
_SdWANStatsRouteEntryV2_Object = MibTableRow
sdWANStatsRouteEntryV2 = _SdWANStatsRouteEntryV2_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1)
)
sdWANStatsRouteEntryV2.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsRouteIndexV2"),
)
if mibBuilder.loadTexts:
    sdWANStatsRouteEntryV2.setStatus("current")
_SdWANStatsRouteIndexV2_Type = Integer32
_SdWANStatsRouteIndexV2_Object = MibTableColumn
sdWANStatsRouteIndexV2 = _SdWANStatsRouteIndexV2_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 1),
    _SdWANStatsRouteIndexV2_Type()
)
sdWANStatsRouteIndexV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteIndexV2.setStatus("current")
_SdWANStatsRouteNetworkAddr_Type = IpAddress
_SdWANStatsRouteNetworkAddr_Object = MibTableColumn
sdWANStatsRouteNetworkAddr = _SdWANStatsRouteNetworkAddr_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 2),
    _SdWANStatsRouteNetworkAddr_Type()
)
sdWANStatsRouteNetworkAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteNetworkAddr.setStatus("current")
_SdWANStatsRouteNetworkPrefix_Type = Integer32
_SdWANStatsRouteNetworkPrefix_Object = MibTableColumn
sdWANStatsRouteNetworkPrefix = _SdWANStatsRouteNetworkPrefix_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 3),
    _SdWANStatsRouteNetworkPrefix_Type()
)
sdWANStatsRouteNetworkPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteNetworkPrefix.setStatus("current")
_SdWANStatsRouteGateway_Type = IpAddress
_SdWANStatsRouteGateway_Object = MibTableColumn
sdWANStatsRouteGateway = _SdWANStatsRouteGateway_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 4),
    _SdWANStatsRouteGateway_Type()
)
sdWANStatsRouteGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteGateway.setStatus("current")


class _SdWANStatsRouteServiceType_Type(Integer32):
    """Custom type sdWANStatsRouteServiceType based on Integer32"""
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
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("discard", 0),
          ("passthrough", 1),
          ("internet", 2),
          ("multicast", 3),
          ("intranet", 4),
          ("virtualpath", 5),
          ("langretunnel", 6),
          ("lanipsectunnel", 7),
          ("local", 8),
          ("iphost", 9))
    )


_SdWANStatsRouteServiceType_Type.__name__ = "Integer32"
_SdWANStatsRouteServiceType_Object = MibTableColumn
sdWANStatsRouteServiceType = _SdWANStatsRouteServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 5),
    _SdWANStatsRouteServiceType_Type()
)
sdWANStatsRouteServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteServiceType.setStatus("current")
_SdWANStatsRouteServiceID_Type = Integer32
_SdWANStatsRouteServiceID_Object = MibTableColumn
sdWANStatsRouteServiceID = _SdWANStatsRouteServiceID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 6),
    _SdWANStatsRouteServiceID_Type()
)
sdWANStatsRouteServiceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteServiceID.setStatus("current")
_SdWANStatsRouteServiceName_Type = DisplayString
_SdWANStatsRouteServiceName_Object = MibTableColumn
sdWANStatsRouteServiceName = _SdWANStatsRouteServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 7),
    _SdWANStatsRouteServiceName_Type()
)
sdWANStatsRouteServiceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteServiceName.setStatus("current")


class _SdWANStatsRouteReachable_Type(Integer32):
    """Custom type sdWANStatsRouteReachable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1),
          ("na", 2))
    )


_SdWANStatsRouteReachable_Type.__name__ = "Integer32"
_SdWANStatsRouteReachable_Object = MibTableColumn
sdWANStatsRouteReachable = _SdWANStatsRouteReachable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 8),
    _SdWANStatsRouteReachable_Type()
)
sdWANStatsRouteReachable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteReachable.setStatus("current")
_SdWANStatsRouteSiteName_Type = DisplayString
_SdWANStatsRouteSiteName_Object = MibTableColumn
sdWANStatsRouteSiteName = _SdWANStatsRouteSiteName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 9),
    _SdWANStatsRouteSiteName_Type()
)
sdWANStatsRouteSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteSiteName.setStatus("current")


class _SdWANStatsRouteType_Type(Integer32):
    """Custom type sdWANStatsRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1),
          ("dynamicVPath", 2))
    )


_SdWANStatsRouteType_Type.__name__ = "Integer32"
_SdWANStatsRouteType_Object = MibTableColumn
sdWANStatsRouteType = _SdWANStatsRouteType_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 10),
    _SdWANStatsRouteType_Type()
)
sdWANStatsRouteType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteType.setStatus("current")


class _SdWANStatsRouteNeighborDirect_Type(Integer32):
    """Custom type sdWANStatsRouteNeighborDirect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("na", 0),
          ("directNeighbor", 1),
          ("indirectNeighbor", 2))
    )


_SdWANStatsRouteNeighborDirect_Type.__name__ = "Integer32"
_SdWANStatsRouteNeighborDirect_Object = MibTableColumn
sdWANStatsRouteNeighborDirect = _SdWANStatsRouteNeighborDirect_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 11),
    _SdWANStatsRouteNeighborDirect_Type()
)
sdWANStatsRouteNeighborDirect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteNeighborDirect.setStatus("current")
_SdWANStatsRouteCost_Type = Integer32
_SdWANStatsRouteCost_Object = MibTableColumn
sdWANStatsRouteCost = _SdWANStatsRouteCost_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 12),
    _SdWANStatsRouteCost_Type()
)
sdWANStatsRouteCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteCost.setStatus("current")
_SdWANStatsRouteHitCountV2_Type = Counter64
_SdWANStatsRouteHitCountV2_Object = MibTableColumn
sdWANStatsRouteHitCountV2 = _SdWANStatsRouteHitCountV2_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 13),
    _SdWANStatsRouteHitCountV2_Type()
)
sdWANStatsRouteHitCountV2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteHitCountV2.setStatus("current")
_SdWANStatsRouteEligible_Type = DisplayString
_SdWANStatsRouteEligible_Object = MibTableColumn
sdWANStatsRouteEligible = _SdWANStatsRouteEligible_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 14),
    _SdWANStatsRouteEligible_Type()
)
sdWANStatsRouteEligible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteEligible.setStatus("current")
_SdWANStatsRouteEligibilityType_Type = DisplayString
_SdWANStatsRouteEligibilityType_Object = MibTableColumn
sdWANStatsRouteEligibilityType = _SdWANStatsRouteEligibilityType_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 15),
    _SdWANStatsRouteEligibilityType_Type()
)
sdWANStatsRouteEligibilityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteEligibilityType.setStatus("current")
_SdWANStatsRouteEligibilityValue_Type = DisplayString
_SdWANStatsRouteEligibilityValue_Object = MibTableColumn
sdWANStatsRouteEligibilityValue = _SdWANStatsRouteEligibilityValue_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 16),
    _SdWANStatsRouteEligibilityValue_Type()
)
sdWANStatsRouteEligibilityValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteEligibilityValue.setStatus("current")


class _SdWANStatsRouteProtocol_Type(Integer32):
    """Custom type sdWANStatsRouteProtocol based on Integer32"""
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
        *(("NA", 0),
          ("BGP", 1),
          ("OSPF", 2),
          ("VW", 3))
    )


_SdWANStatsRouteProtocol_Type.__name__ = "Integer32"
_SdWANStatsRouteProtocol_Object = MibTableColumn
sdWANStatsRouteProtocol = _SdWANStatsRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 17),
    _SdWANStatsRouteProtocol_Type()
)
sdWANStatsRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteProtocol.setStatus("current")
_SdWANStatsRouteRoutingDomainName_Type = DisplayString
_SdWANStatsRouteRoutingDomainName_Object = MibTableColumn
sdWANStatsRouteRoutingDomainName = _SdWANStatsRouteRoutingDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 20, 2, 1, 18),
    _SdWANStatsRouteRoutingDomainName_Type()
)
sdWANStatsRouteRoutingDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsRouteRoutingDomainName.setStatus("current")
_SdWANStatsDynamicVPaths_ObjectIdentity = ObjectIdentity
sdWANStatsDynamicVPaths = _SdWANStatsDynamicVPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21)
)
_SdWANStatsDynamicVPathScalars_ObjectIdentity = ObjectIdentity
sdWANStatsDynamicVPathScalars = _SdWANStatsDynamicVPathScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 1)
)


class _SdWANStatsNumDynamicVPaths_Type(Gauge32):
    """Custom type sdWANStatsNumDynamicVPaths based on Gauge32"""
    defaultValue = 0


_SdWANStatsNumDynamicVPaths_Type.__name__ = "Gauge32"
_SdWANStatsNumDynamicVPaths_Object = MibScalar
sdWANStatsNumDynamicVPaths = _SdWANStatsNumDynamicVPaths_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 1, 1),
    _SdWANStatsNumDynamicVPaths_Type()
)
sdWANStatsNumDynamicVPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsNumDynamicVPaths.setStatus("current")
_SdWANStatsDynamicVPathTable_Object = MibTable
sdWANStatsDynamicVPathTable = _SdWANStatsDynamicVPathTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2)
)
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathTable.setStatus("current")
_SdWANStatsDynamicVPathEntry_Object = MibTableRow
sdWANStatsDynamicVPathEntry = _SdWANStatsDynamicVPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1)
)
sdWANStatsDynamicVPathEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsDynamicVPathIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathEntry.setStatus("current")
_SdWANStatsDynamicVPathIndex_Type = Integer32
_SdWANStatsDynamicVPathIndex_Object = MibTableColumn
sdWANStatsDynamicVPathIndex = _SdWANStatsDynamicVPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 1),
    _SdWANStatsDynamicVPathIndex_Type()
)
sdWANStatsDynamicVPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathIndex.setStatus("current")
_SdWANStatsDynamicVPathID_Type = Integer32
_SdWANStatsDynamicVPathID_Object = MibTableColumn
sdWANStatsDynamicVPathID = _SdWANStatsDynamicVPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 2),
    _SdWANStatsDynamicVPathID_Type()
)
sdWANStatsDynamicVPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathID.setStatus("current")
_SdWANStatsDynamicVPathName_Type = DisplayString
_SdWANStatsDynamicVPathName_Object = MibTableColumn
sdWANStatsDynamicVPathName = _SdWANStatsDynamicVPathName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 3),
    _SdWANStatsDynamicVPathName_Type()
)
sdWANStatsDynamicVPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathName.setStatus("current")


class _SdWANStatsDynamicVPathState_Type(Integer32):
    """Custom type sdWANStatsDynamicVPathState based on Integer32"""
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
        *(("undefined", 0),
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_SdWANStatsDynamicVPathState_Type.__name__ = "Integer32"
_SdWANStatsDynamicVPathState_Object = MibTableColumn
sdWANStatsDynamicVPathState = _SdWANStatsDynamicVPathState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 4),
    _SdWANStatsDynamicVPathState_Type()
)
sdWANStatsDynamicVPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathState.setStatus("current")
_SdWANStatsDynamicVPathTimeSinceCreation_Type = Counter64
_SdWANStatsDynamicVPathTimeSinceCreation_Object = MibTableColumn
sdWANStatsDynamicVPathTimeSinceCreation = _SdWANStatsDynamicVPathTimeSinceCreation_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 5),
    _SdWANStatsDynamicVPathTimeSinceCreation_Type()
)
sdWANStatsDynamicVPathTimeSinceCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathTimeSinceCreation.setStatus("current")
_SdWANStatsDynamicVPathBytesSent_Type = Counter64
_SdWANStatsDynamicVPathBytesSent_Object = MibTableColumn
sdWANStatsDynamicVPathBytesSent = _SdWANStatsDynamicVPathBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 6),
    _SdWANStatsDynamicVPathBytesSent_Type()
)
sdWANStatsDynamicVPathBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathBytesSent.setStatus("current")
_SdWANStatsDynamicVPathPacketsSent_Type = Counter64
_SdWANStatsDynamicVPathPacketsSent_Object = MibTableColumn
sdWANStatsDynamicVPathPacketsSent = _SdWANStatsDynamicVPathPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 7),
    _SdWANStatsDynamicVPathPacketsSent_Type()
)
sdWANStatsDynamicVPathPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathPacketsSent.setStatus("current")
_SdWANStatsDynamicVPathSendBytesDropped_Type = Counter64
_SdWANStatsDynamicVPathSendBytesDropped_Object = MibTableColumn
sdWANStatsDynamicVPathSendBytesDropped = _SdWANStatsDynamicVPathSendBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 8),
    _SdWANStatsDynamicVPathSendBytesDropped_Type()
)
sdWANStatsDynamicVPathSendBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathSendBytesDropped.setStatus("current")
_SdWANStatsDynamicVPathSendPacketsDropped_Type = Counter64
_SdWANStatsDynamicVPathSendPacketsDropped_Object = MibTableColumn
sdWANStatsDynamicVPathSendPacketsDropped = _SdWANStatsDynamicVPathSendPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 9),
    _SdWANStatsDynamicVPathSendPacketsDropped_Type()
)
sdWANStatsDynamicVPathSendPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathSendPacketsDropped.setStatus("current")
_SdWANStatsDynamicVPathSendPacketsLost_Type = Counter64
_SdWANStatsDynamicVPathSendPacketsLost_Object = MibTableColumn
sdWANStatsDynamicVPathSendPacketsLost = _SdWANStatsDynamicVPathSendPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 10),
    _SdWANStatsDynamicVPathSendPacketsLost_Type()
)
sdWANStatsDynamicVPathSendPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathSendPacketsLost.setStatus("current")
_SdWANStatsDynamicVPathSendPacketsOOO_Type = Counter64
_SdWANStatsDynamicVPathSendPacketsOOO_Object = MibTableColumn
sdWANStatsDynamicVPathSendPacketsOOO = _SdWANStatsDynamicVPathSendPacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 11),
    _SdWANStatsDynamicVPathSendPacketsOOO_Type()
)
sdWANStatsDynamicVPathSendPacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathSendPacketsOOO.setStatus("current")
_SdWANStatsDynamicVPathSendBOWTms_Type = Gauge32
_SdWANStatsDynamicVPathSendBOWTms_Object = MibTableColumn
sdWANStatsDynamicVPathSendBOWTms = _SdWANStatsDynamicVPathSendBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 12),
    _SdWANStatsDynamicVPathSendBOWTms_Type()
)
sdWANStatsDynamicVPathSendBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathSendBOWTms.setStatus("current")
_SdWANStatsDynamicVPathSendJitterms_Type = Gauge32
_SdWANStatsDynamicVPathSendJitterms_Object = MibTableColumn
sdWANStatsDynamicVPathSendJitterms = _SdWANStatsDynamicVPathSendJitterms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 13),
    _SdWANStatsDynamicVPathSendJitterms_Type()
)
sdWANStatsDynamicVPathSendJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathSendJitterms.setStatus("current")
_SdWANStatsDynamicVPathBytesReceived_Type = Counter64
_SdWANStatsDynamicVPathBytesReceived_Object = MibTableColumn
sdWANStatsDynamicVPathBytesReceived = _SdWANStatsDynamicVPathBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 14),
    _SdWANStatsDynamicVPathBytesReceived_Type()
)
sdWANStatsDynamicVPathBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathBytesReceived.setStatus("current")
_SdWANStatsDynamicVPathPacketsReceived_Type = Counter64
_SdWANStatsDynamicVPathPacketsReceived_Object = MibTableColumn
sdWANStatsDynamicVPathPacketsReceived = _SdWANStatsDynamicVPathPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 15),
    _SdWANStatsDynamicVPathPacketsReceived_Type()
)
sdWANStatsDynamicVPathPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathPacketsReceived.setStatus("current")
_SdWANStatsDynamicVPathReceiveBytesDropped_Type = Counter64
_SdWANStatsDynamicVPathReceiveBytesDropped_Object = MibTableColumn
sdWANStatsDynamicVPathReceiveBytesDropped = _SdWANStatsDynamicVPathReceiveBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 16),
    _SdWANStatsDynamicVPathReceiveBytesDropped_Type()
)
sdWANStatsDynamicVPathReceiveBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathReceiveBytesDropped.setStatus("current")
_SdWANStatsDynamicVPathReceivePacketsDropped_Type = Counter64
_SdWANStatsDynamicVPathReceivePacketsDropped_Object = MibTableColumn
sdWANStatsDynamicVPathReceivePacketsDropped = _SdWANStatsDynamicVPathReceivePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 17),
    _SdWANStatsDynamicVPathReceivePacketsDropped_Type()
)
sdWANStatsDynamicVPathReceivePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathReceivePacketsDropped.setStatus("current")
_SdWANStatsDynamicVPathReceivePacketsLost_Type = Counter64
_SdWANStatsDynamicVPathReceivePacketsLost_Object = MibTableColumn
sdWANStatsDynamicVPathReceivePacketsLost = _SdWANStatsDynamicVPathReceivePacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 18),
    _SdWANStatsDynamicVPathReceivePacketsLost_Type()
)
sdWANStatsDynamicVPathReceivePacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathReceivePacketsLost.setStatus("current")
_SdWANStatsDynamicVPathReceivePacketsOOO_Type = Counter64
_SdWANStatsDynamicVPathReceivePacketsOOO_Object = MibTableColumn
sdWANStatsDynamicVPathReceivePacketsOOO = _SdWANStatsDynamicVPathReceivePacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 19),
    _SdWANStatsDynamicVPathReceivePacketsOOO_Type()
)
sdWANStatsDynamicVPathReceivePacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathReceivePacketsOOO.setStatus("current")
_SdWANStatsDynamicVPathReceiveBOWTms_Type = Gauge32
_SdWANStatsDynamicVPathReceiveBOWTms_Object = MibTableColumn
sdWANStatsDynamicVPathReceiveBOWTms = _SdWANStatsDynamicVPathReceiveBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 20),
    _SdWANStatsDynamicVPathReceiveBOWTms_Type()
)
sdWANStatsDynamicVPathReceiveBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathReceiveBOWTms.setStatus("current")
_SdWANStatsDynamicVPathReceiveJitterms_Type = Gauge32
_SdWANStatsDynamicVPathReceiveJitterms_Object = MibTableColumn
sdWANStatsDynamicVPathReceiveJitterms = _SdWANStatsDynamicVPathReceiveJitterms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 21),
    _SdWANStatsDynamicVPathReceiveJitterms_Type()
)
sdWANStatsDynamicVPathReceiveJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathReceiveJitterms.setStatus("current")
_SdWANStatsDynamicVPathNumPaths_Type = Integer32
_SdWANStatsDynamicVPathNumPaths_Object = MibTableColumn
sdWANStatsDynamicVPathNumPaths = _SdWANStatsDynamicVPathNumPaths_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 22),
    _SdWANStatsDynamicVPathNumPaths_Type()
)
sdWANStatsDynamicVPathNumPaths.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathNumPaths.setStatus("current")
_SdWANStatsDynamicVPathNumRules_Type = Integer32
_SdWANStatsDynamicVPathNumRules_Object = MibTableColumn
sdWANStatsDynamicVPathNumRules = _SdWANStatsDynamicVPathNumRules_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 2, 1, 23),
    _SdWANStatsDynamicVPathNumRules_Type()
)
sdWANStatsDynamicVPathNumRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicVPathNumRules.setStatus("current")
_SdWANStatsDynamicWANPaths_ObjectIdentity = ObjectIdentity
sdWANStatsDynamicWANPaths = _SdWANStatsDynamicWANPaths_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3)
)
_SdWANStatsDynamicWANPathTable_Object = MibTable
sdWANStatsDynamicWANPathTable = _SdWANStatsDynamicWANPathTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1)
)
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathTable.setStatus("current")
_SdWANStatsDynamicWANPathEntry_Object = MibTableRow
sdWANStatsDynamicWANPathEntry = _SdWANStatsDynamicWANPathEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1)
)
sdWANStatsDynamicWANPathEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsDynamicWANPathVPathIndex"),
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsDynamicWANPathPathIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathEntry.setStatus("current")
_SdWANStatsDynamicWANPathVPathIndex_Type = Integer32
_SdWANStatsDynamicWANPathVPathIndex_Object = MibTableColumn
sdWANStatsDynamicWANPathVPathIndex = _SdWANStatsDynamicWANPathVPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 1),
    _SdWANStatsDynamicWANPathVPathIndex_Type()
)
sdWANStatsDynamicWANPathVPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathVPathIndex.setStatus("current")
_SdWANStatsDynamicWANPathPathIndex_Type = Integer32
_SdWANStatsDynamicWANPathPathIndex_Object = MibTableColumn
sdWANStatsDynamicWANPathPathIndex = _SdWANStatsDynamicWANPathPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 2),
    _SdWANStatsDynamicWANPathPathIndex_Type()
)
sdWANStatsDynamicWANPathPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathPathIndex.setStatus("current")
_SdWANStatsDynamicWANPathVPathID_Type = Integer32
_SdWANStatsDynamicWANPathVPathID_Object = MibTableColumn
sdWANStatsDynamicWANPathVPathID = _SdWANStatsDynamicWANPathVPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 3),
    _SdWANStatsDynamicWANPathVPathID_Type()
)
sdWANStatsDynamicWANPathVPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathVPathID.setStatus("current")
_SdWANStatsDynamicWANPathPathID_Type = Integer32
_SdWANStatsDynamicWANPathPathID_Object = MibTableColumn
sdWANStatsDynamicWANPathPathID = _SdWANStatsDynamicWANPathPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 4),
    _SdWANStatsDynamicWANPathPathID_Type()
)
sdWANStatsDynamicWANPathPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathPathID.setStatus("current")
_SdWANStatsDynamicWANPathName_Type = DisplayString
_SdWANStatsDynamicWANPathName_Object = MibTableColumn
sdWANStatsDynamicWANPathName = _SdWANStatsDynamicWANPathName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 5),
    _SdWANStatsDynamicWANPathName_Type()
)
sdWANStatsDynamicWANPathName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathName.setStatus("current")


class _SdWANStatsDynamicWANPathState_Type(Integer32):
    """Custom type sdWANStatsDynamicWANPathState based on Integer32"""
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
        *(("undefined", 0),
          ("disabled", 1),
          ("dead", 2),
          ("bad", 3),
          ("good", 4))
    )


_SdWANStatsDynamicWANPathState_Type.__name__ = "Integer32"
_SdWANStatsDynamicWANPathState_Object = MibTableColumn
sdWANStatsDynamicWANPathState = _SdWANStatsDynamicWANPathState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 6),
    _SdWANStatsDynamicWANPathState_Type()
)
sdWANStatsDynamicWANPathState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathState.setStatus("current")
_SdWANStatsDynamicWANPathBytesSent_Type = Counter64
_SdWANStatsDynamicWANPathBytesSent_Object = MibTableColumn
sdWANStatsDynamicWANPathBytesSent = _SdWANStatsDynamicWANPathBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 7),
    _SdWANStatsDynamicWANPathBytesSent_Type()
)
sdWANStatsDynamicWANPathBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathBytesSent.setStatus("current")
_SdWANStatsDynamicWANPathPacketsSent_Type = Counter64
_SdWANStatsDynamicWANPathPacketsSent_Object = MibTableColumn
sdWANStatsDynamicWANPathPacketsSent = _SdWANStatsDynamicWANPathPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 8),
    _SdWANStatsDynamicWANPathPacketsSent_Type()
)
sdWANStatsDynamicWANPathPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathPacketsSent.setStatus("current")
_SdWANStatsDynamicWANPathBytesReceived_Type = Counter64
_SdWANStatsDynamicWANPathBytesReceived_Object = MibTableColumn
sdWANStatsDynamicWANPathBytesReceived = _SdWANStatsDynamicWANPathBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 9),
    _SdWANStatsDynamicWANPathBytesReceived_Type()
)
sdWANStatsDynamicWANPathBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathBytesReceived.setStatus("current")
_SdWANStatsDynamicWANPathPacketsReceived_Type = Counter64
_SdWANStatsDynamicWANPathPacketsReceived_Object = MibTableColumn
sdWANStatsDynamicWANPathPacketsReceived = _SdWANStatsDynamicWANPathPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 10),
    _SdWANStatsDynamicWANPathPacketsReceived_Type()
)
sdWANStatsDynamicWANPathPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathPacketsReceived.setStatus("current")
_SdWANStatsDynamicWANPathBytesDropped_Type = Counter64
_SdWANStatsDynamicWANPathBytesDropped_Object = MibTableColumn
sdWANStatsDynamicWANPathBytesDropped = _SdWANStatsDynamicWANPathBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 11),
    _SdWANStatsDynamicWANPathBytesDropped_Type()
)
sdWANStatsDynamicWANPathBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathBytesDropped.setStatus("current")
_SdWANStatsDynamicWANPathPacketsDropped_Type = Counter64
_SdWANStatsDynamicWANPathPacketsDropped_Object = MibTableColumn
sdWANStatsDynamicWANPathPacketsDropped = _SdWANStatsDynamicWANPathPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 12),
    _SdWANStatsDynamicWANPathPacketsDropped_Type()
)
sdWANStatsDynamicWANPathPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathPacketsDropped.setStatus("current")
_SdWANStatsDynamicWANPathBOWTms_Type = Gauge32
_SdWANStatsDynamicWANPathBOWTms_Object = MibTableColumn
sdWANStatsDynamicWANPathBOWTms = _SdWANStatsDynamicWANPathBOWTms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 13),
    _SdWANStatsDynamicWANPathBOWTms_Type()
)
sdWANStatsDynamicWANPathBOWTms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathBOWTms.setStatus("current")
_SdWANStatsDynamicWANPathJitterms_Type = Gauge32
_SdWANStatsDynamicWANPathJitterms_Object = MibTableColumn
sdWANStatsDynamicWANPathJitterms = _SdWANStatsDynamicWANPathJitterms_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 14),
    _SdWANStatsDynamicWANPathJitterms_Type()
)
sdWANStatsDynamicWANPathJitterms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathJitterms.setStatus("current")
_SdWANStatsDynamicWANPathPacketsLost_Type = Counter64
_SdWANStatsDynamicWANPathPacketsLost_Object = MibTableColumn
sdWANStatsDynamicWANPathPacketsLost = _SdWANStatsDynamicWANPathPacketsLost_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 15),
    _SdWANStatsDynamicWANPathPacketsLost_Type()
)
sdWANStatsDynamicWANPathPacketsLost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathPacketsLost.setStatus("current")
_SdWANStatsDynamicWANPathPacketsOOO_Type = Counter64
_SdWANStatsDynamicWANPathPacketsOOO_Object = MibTableColumn
sdWANStatsDynamicWANPathPacketsOOO = _SdWANStatsDynamicWANPathPacketsOOO_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 3, 1, 1, 16),
    _SdWANStatsDynamicWANPathPacketsOOO_Type()
)
sdWANStatsDynamicWANPathPacketsOOO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANPathPacketsOOO.setStatus("current")
_SdWANStatsDynamicWANClasses_ObjectIdentity = ObjectIdentity
sdWANStatsDynamicWANClasses = _SdWANStatsDynamicWANClasses_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4)
)
_SdWANStatsDynamicWANClassTable_Object = MibTable
sdWANStatsDynamicWANClassTable = _SdWANStatsDynamicWANClassTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1)
)
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassTable.setStatus("current")
_SdWANStatsDynamicWANClassEntry_Object = MibTableRow
sdWANStatsDynamicWANClassEntry = _SdWANStatsDynamicWANClassEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1)
)
sdWANStatsDynamicWANClassEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsDynamicWANClassVPathIndex"),
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsDynamicWANClassClassIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassEntry.setStatus("current")
_SdWANStatsDynamicWANClassVPathIndex_Type = Integer32
_SdWANStatsDynamicWANClassVPathIndex_Object = MibTableColumn
sdWANStatsDynamicWANClassVPathIndex = _SdWANStatsDynamicWANClassVPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 1),
    _SdWANStatsDynamicWANClassVPathIndex_Type()
)
sdWANStatsDynamicWANClassVPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassVPathIndex.setStatus("current")
_SdWANStatsDynamicWANClassClassIndex_Type = Integer32
_SdWANStatsDynamicWANClassClassIndex_Object = MibTableColumn
sdWANStatsDynamicWANClassClassIndex = _SdWANStatsDynamicWANClassClassIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 2),
    _SdWANStatsDynamicWANClassClassIndex_Type()
)
sdWANStatsDynamicWANClassClassIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassClassIndex.setStatus("current")
_SdWANStatsDynamicWANClassVPathID_Type = Integer32
_SdWANStatsDynamicWANClassVPathID_Object = MibTableColumn
sdWANStatsDynamicWANClassVPathID = _SdWANStatsDynamicWANClassVPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 3),
    _SdWANStatsDynamicWANClassVPathID_Type()
)
sdWANStatsDynamicWANClassVPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassVPathID.setStatus("current")
_SdWANStatsDynamicWANClassClassID_Type = Integer32
_SdWANStatsDynamicWANClassClassID_Object = MibTableColumn
sdWANStatsDynamicWANClassClassID = _SdWANStatsDynamicWANClassClassID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 4),
    _SdWANStatsDynamicWANClassClassID_Type()
)
sdWANStatsDynamicWANClassClassID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassClassID.setStatus("current")
_SdWANStatsDynamicWANClassName_Type = DisplayString
_SdWANStatsDynamicWANClassName_Object = MibTableColumn
sdWANStatsDynamicWANClassName = _SdWANStatsDynamicWANClassName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 5),
    _SdWANStatsDynamicWANClassName_Type()
)
sdWANStatsDynamicWANClassName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassName.setStatus("current")


class _SdWANStatsDynamicWANClassType_Type(Integer32):
    """Custom type sdWANStatsDynamicWANClassType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("realtime", 1),
          ("interactive", 2),
          ("bulk", 3),
          ("unknown", 4))
    )


_SdWANStatsDynamicWANClassType_Type.__name__ = "Integer32"
_SdWANStatsDynamicWANClassType_Object = MibTableColumn
sdWANStatsDynamicWANClassType = _SdWANStatsDynamicWANClassType_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 6),
    _SdWANStatsDynamicWANClassType_Type()
)
sdWANStatsDynamicWANClassType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassType.setStatus("current")
_SdWANStatsDynamicWANClassBytesSent_Type = Counter64
_SdWANStatsDynamicWANClassBytesSent_Object = MibTableColumn
sdWANStatsDynamicWANClassBytesSent = _SdWANStatsDynamicWANClassBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 7),
    _SdWANStatsDynamicWANClassBytesSent_Type()
)
sdWANStatsDynamicWANClassBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassBytesSent.setStatus("current")
_SdWANStatsDynamicWANClassPacketsSent_Type = Counter64
_SdWANStatsDynamicWANClassPacketsSent_Object = MibTableColumn
sdWANStatsDynamicWANClassPacketsSent = _SdWANStatsDynamicWANClassPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 8),
    _SdWANStatsDynamicWANClassPacketsSent_Type()
)
sdWANStatsDynamicWANClassPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassPacketsSent.setStatus("current")
_SdWANStatsDynamicWANClassBytesPending_Type = Counter64
_SdWANStatsDynamicWANClassBytesPending_Object = MibTableColumn
sdWANStatsDynamicWANClassBytesPending = _SdWANStatsDynamicWANClassBytesPending_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 9),
    _SdWANStatsDynamicWANClassBytesPending_Type()
)
sdWANStatsDynamicWANClassBytesPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassBytesPending.setStatus("current")
_SdWANStatsDynamicWANClassPacketsPending_Type = Counter64
_SdWANStatsDynamicWANClassPacketsPending_Object = MibTableColumn
sdWANStatsDynamicWANClassPacketsPending = _SdWANStatsDynamicWANClassPacketsPending_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 10),
    _SdWANStatsDynamicWANClassPacketsPending_Type()
)
sdWANStatsDynamicWANClassPacketsPending.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassPacketsPending.setStatus("current")
_SdWANStatsDynamicWANClassBytesDropped_Type = Counter64
_SdWANStatsDynamicWANClassBytesDropped_Object = MibTableColumn
sdWANStatsDynamicWANClassBytesDropped = _SdWANStatsDynamicWANClassBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 11),
    _SdWANStatsDynamicWANClassBytesDropped_Type()
)
sdWANStatsDynamicWANClassBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassBytesDropped.setStatus("current")
_SdWANStatsDynamicWANClassPacketsDropped_Type = Counter64
_SdWANStatsDynamicWANClassPacketsDropped_Object = MibTableColumn
sdWANStatsDynamicWANClassPacketsDropped = _SdWANStatsDynamicWANClassPacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 4, 1, 1, 12),
    _SdWANStatsDynamicWANClassPacketsDropped_Type()
)
sdWANStatsDynamicWANClassPacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANClassPacketsDropped.setStatus("current")
_SdWANStatsDynamicWANRules_ObjectIdentity = ObjectIdentity
sdWANStatsDynamicWANRules = _SdWANStatsDynamicWANRules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5)
)
_SdWANStatsDynamicWANRuleTable_Object = MibTable
sdWANStatsDynamicWANRuleTable = _SdWANStatsDynamicWANRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1)
)
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleTable.setStatus("current")
_SdWANStatsDynamicWANRuleEntry_Object = MibTableRow
sdWANStatsDynamicWANRuleEntry = _SdWANStatsDynamicWANRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1)
)
sdWANStatsDynamicWANRuleEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsDynamicWANRuleVPathIndex"),
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsDynamicWANRuleRuleIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleEntry.setStatus("current")
_SdWANStatsDynamicWANRuleVPathIndex_Type = Integer32
_SdWANStatsDynamicWANRuleVPathIndex_Object = MibTableColumn
sdWANStatsDynamicWANRuleVPathIndex = _SdWANStatsDynamicWANRuleVPathIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 1),
    _SdWANStatsDynamicWANRuleVPathIndex_Type()
)
sdWANStatsDynamicWANRuleVPathIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleVPathIndex.setStatus("current")
_SdWANStatsDynamicWANRuleRuleIndex_Type = Integer32
_SdWANStatsDynamicWANRuleRuleIndex_Object = MibTableColumn
sdWANStatsDynamicWANRuleRuleIndex = _SdWANStatsDynamicWANRuleRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 2),
    _SdWANStatsDynamicWANRuleRuleIndex_Type()
)
sdWANStatsDynamicWANRuleRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleRuleIndex.setStatus("current")
_SdWANStatsDynamicWANRuleVPathID_Type = Integer32
_SdWANStatsDynamicWANRuleVPathID_Object = MibTableColumn
sdWANStatsDynamicWANRuleVPathID = _SdWANStatsDynamicWANRuleVPathID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 3),
    _SdWANStatsDynamicWANRuleVPathID_Type()
)
sdWANStatsDynamicWANRuleVPathID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleVPathID.setStatus("current")
_SdWANStatsDynamicWANRuleRuleID_Type = Integer32
_SdWANStatsDynamicWANRuleRuleID_Object = MibTableColumn
sdWANStatsDynamicWANRuleRuleID = _SdWANStatsDynamicWANRuleRuleID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 4),
    _SdWANStatsDynamicWANRuleRuleID_Type()
)
sdWANStatsDynamicWANRuleRuleID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleRuleID.setStatus("current")
_SdWANStatsDynamicWANRuleGlobalRuleIndex_Type = Integer32
_SdWANStatsDynamicWANRuleGlobalRuleIndex_Object = MibTableColumn
sdWANStatsDynamicWANRuleGlobalRuleIndex = _SdWANStatsDynamicWANRuleGlobalRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 5),
    _SdWANStatsDynamicWANRuleGlobalRuleIndex_Type()
)
sdWANStatsDynamicWANRuleGlobalRuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleGlobalRuleIndex.setStatus("current")
_SdWANStatsDynamicWANRuleApplicationName_Type = DisplayString
_SdWANStatsDynamicWANRuleApplicationName_Object = MibTableColumn
sdWANStatsDynamicWANRuleApplicationName = _SdWANStatsDynamicWANRuleApplicationName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 6),
    _SdWANStatsDynamicWANRuleApplicationName_Type()
)
sdWANStatsDynamicWANRuleApplicationName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleApplicationName.setStatus("current")
_SdWANStatsDynamicWANRuleLANToWANHitCount_Type = Gauge32
_SdWANStatsDynamicWANRuleLANToWANHitCount_Object = MibTableColumn
sdWANStatsDynamicWANRuleLANToWANHitCount = _SdWANStatsDynamicWANRuleLANToWANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 7),
    _SdWANStatsDynamicWANRuleLANToWANHitCount_Type()
)
sdWANStatsDynamicWANRuleLANToWANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleLANToWANHitCount.setStatus("current")
_SdWANStatsDynamicWANRuleWANToLANHitCount_Type = Gauge32
_SdWANStatsDynamicWANRuleWANToLANHitCount_Object = MibTableColumn
sdWANStatsDynamicWANRuleWANToLANHitCount = _SdWANStatsDynamicWANRuleWANToLANHitCount_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 8),
    _SdWANStatsDynamicWANRuleWANToLANHitCount_Type()
)
sdWANStatsDynamicWANRuleWANToLANHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleWANToLANHitCount.setStatus("current")
_SdWANStatsDynamicWANRuleBytesSent_Type = Gauge32
_SdWANStatsDynamicWANRuleBytesSent_Object = MibTableColumn
sdWANStatsDynamicWANRuleBytesSent = _SdWANStatsDynamicWANRuleBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 9),
    _SdWANStatsDynamicWANRuleBytesSent_Type()
)
sdWANStatsDynamicWANRuleBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleBytesSent.setStatus("current")
_SdWANStatsDynamicWANRulePacketsSent_Type = Gauge32
_SdWANStatsDynamicWANRulePacketsSent_Object = MibTableColumn
sdWANStatsDynamicWANRulePacketsSent = _SdWANStatsDynamicWANRulePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 10),
    _SdWANStatsDynamicWANRulePacketsSent_Type()
)
sdWANStatsDynamicWANRulePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRulePacketsSent.setStatus("current")
_SdWANStatsDynamicWANRuleBytesReceived_Type = Gauge32
_SdWANStatsDynamicWANRuleBytesReceived_Object = MibTableColumn
sdWANStatsDynamicWANRuleBytesReceived = _SdWANStatsDynamicWANRuleBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 11),
    _SdWANStatsDynamicWANRuleBytesReceived_Type()
)
sdWANStatsDynamicWANRuleBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleBytesReceived.setStatus("current")
_SdWANStatsDynamicWANRulePacketsReceived_Type = Gauge32
_SdWANStatsDynamicWANRulePacketsReceived_Object = MibTableColumn
sdWANStatsDynamicWANRulePacketsReceived = _SdWANStatsDynamicWANRulePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 12),
    _SdWANStatsDynamicWANRulePacketsReceived_Type()
)
sdWANStatsDynamicWANRulePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRulePacketsReceived.setStatus("current")
_SdWANStatsDynamicWANRuleBytesDropped_Type = Gauge32
_SdWANStatsDynamicWANRuleBytesDropped_Object = MibTableColumn
sdWANStatsDynamicWANRuleBytesDropped = _SdWANStatsDynamicWANRuleBytesDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 13),
    _SdWANStatsDynamicWANRuleBytesDropped_Type()
)
sdWANStatsDynamicWANRuleBytesDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleBytesDropped.setStatus("current")
_SdWANStatsDynamicWANRulePacketsDropped_Type = Gauge32
_SdWANStatsDynamicWANRulePacketsDropped_Object = MibTableColumn
sdWANStatsDynamicWANRulePacketsDropped = _SdWANStatsDynamicWANRulePacketsDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 14),
    _SdWANStatsDynamicWANRulePacketsDropped_Type()
)
sdWANStatsDynamicWANRulePacketsDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRulePacketsDropped.setStatus("current")
_SdWANStatsDynamicWANRuleLastActiveNMinuteAgo_Type = TimeTicks
_SdWANStatsDynamicWANRuleLastActiveNMinuteAgo_Object = MibTableColumn
sdWANStatsDynamicWANRuleLastActiveNMinuteAgo = _SdWANStatsDynamicWANRuleLastActiveNMinuteAgo_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 21, 5, 1, 1, 15),
    _SdWANStatsDynamicWANRuleLastActiveNMinuteAgo_Type()
)
sdWANStatsDynamicWANRuleLastActiveNMinuteAgo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsDynamicWANRuleLastActiveNMinuteAgo.setStatus("current")
_SdWANStatsArp_ObjectIdentity = ObjectIdentity
sdWANStatsArp = _SdWANStatsArp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22)
)
_SdWANStatsArpScalars_ObjectIdentity = ObjectIdentity
sdWANStatsArpScalars = _SdWANStatsArpScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 1)
)


class _SdWANStatsNumArpEntries_Type(Integer32):
    """Custom type sdWANStatsNumArpEntries based on Integer32"""
    defaultValue = 0


_SdWANStatsNumArpEntries_Type.__name__ = "Integer32"
_SdWANStatsNumArpEntries_Object = MibScalar
sdWANStatsNumArpEntries = _SdWANStatsNumArpEntries_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 1, 1),
    _SdWANStatsNumArpEntries_Type()
)
sdWANStatsNumArpEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsNumArpEntries.setStatus("current")
_SdWANStatsArpTable_Object = MibTable
sdWANStatsArpTable = _SdWANStatsArpTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2)
)
if mibBuilder.loadTexts:
    sdWANStatsArpTable.setStatus("current")
_SdWANStatsArpEntry_Object = MibTableRow
sdWANStatsArpEntry = _SdWANStatsArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2, 1)
)
sdWANStatsArpEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsArpID"),
)
if mibBuilder.loadTexts:
    sdWANStatsArpEntry.setStatus("current")
_SdWANStatsArpID_Type = Integer32
_SdWANStatsArpID_Object = MibTableColumn
sdWANStatsArpID = _SdWANStatsArpID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2, 1, 1),
    _SdWANStatsArpID_Type()
)
sdWANStatsArpID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsArpID.setStatus("current")
_SdWANStatsArpIfIndex_Type = DisplayString
_SdWANStatsArpIfIndex_Object = MibTableColumn
sdWANStatsArpIfIndex = _SdWANStatsArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2, 1, 2),
    _SdWANStatsArpIfIndex_Type()
)
sdWANStatsArpIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsArpIfIndex.setStatus("current")
_SdWANStatsArpVlanTag_Type = Counter64
_SdWANStatsArpVlanTag_Object = MibTableColumn
sdWANStatsArpVlanTag = _SdWANStatsArpVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2, 1, 3),
    _SdWANStatsArpVlanTag_Type()
)
sdWANStatsArpVlanTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsArpVlanTag.setStatus("current")
_SdWANStatsArpIpAddr_Type = IpAddress
_SdWANStatsArpIpAddr_Object = MibTableColumn
sdWANStatsArpIpAddr = _SdWANStatsArpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2, 1, 4),
    _SdWANStatsArpIpAddr_Type()
)
sdWANStatsArpIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsArpIpAddr.setStatus("current")
_SdWANStatsArpPhysAddr_Type = PhysAddress
_SdWANStatsArpPhysAddr_Object = MibTableColumn
sdWANStatsArpPhysAddr = _SdWANStatsArpPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2, 1, 5),
    _SdWANStatsArpPhysAddr_Type()
)
sdWANStatsArpPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsArpPhysAddr.setStatus("current")
_SdWANStatsArpState_Type = DisplayString
_SdWANStatsArpState_Object = MibTableColumn
sdWANStatsArpState = _SdWANStatsArpState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2, 1, 6),
    _SdWANStatsArpState_Type()
)
sdWANStatsArpState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsArpState.setStatus("current")
_SdWANStatsArpType_Type = DisplayString
_SdWANStatsArpType_Object = MibTableColumn
sdWANStatsArpType = _SdWANStatsArpType_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2, 1, 7),
    _SdWANStatsArpType_Type()
)
sdWANStatsArpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsArpType.setStatus("current")
_SdWANStatsArpReplyAgeMs_Type = Counter64
_SdWANStatsArpReplyAgeMs_Object = MibTableColumn
sdWANStatsArpReplyAgeMs = _SdWANStatsArpReplyAgeMs_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 22, 2, 1, 8),
    _SdWANStatsArpReplyAgeMs_Type()
)
sdWANStatsArpReplyAgeMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsArpReplyAgeMs.setStatus("current")
_SdWANStatsLanGRETunnels_ObjectIdentity = ObjectIdentity
sdWANStatsLanGRETunnels = _SdWANStatsLanGRETunnels_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23)
)
_SdWANStatsLanGRETunnelScalars_ObjectIdentity = ObjectIdentity
sdWANStatsLanGRETunnelScalars = _SdWANStatsLanGRETunnelScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 1)
)


class _SdWANStatsNumLanGRETunnels_Type(Integer32):
    """Custom type sdWANStatsNumLanGRETunnels based on Integer32"""
    defaultValue = 0


_SdWANStatsNumLanGRETunnels_Type.__name__ = "Integer32"
_SdWANStatsNumLanGRETunnels_Object = MibScalar
sdWANStatsNumLanGRETunnels = _SdWANStatsNumLanGRETunnels_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 1, 1),
    _SdWANStatsNumLanGRETunnels_Type()
)
sdWANStatsNumLanGRETunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsNumLanGRETunnels.setStatus("current")
_SdWANStatsLanGRETunnelTable_Object = MibTable
sdWANStatsLanGRETunnelTable = _SdWANStatsLanGRETunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2)
)
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelTable.setStatus("current")
_SdWANStatsLanGRETunnelEntry_Object = MibTableRow
sdWANStatsLanGRETunnelEntry = _SdWANStatsLanGRETunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1)
)
sdWANStatsLanGRETunnelEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANStatsLanGRETunnelIndex"),
)
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelEntry.setStatus("current")
_SdWANStatsLanGRETunnelIndex_Type = Integer32
_SdWANStatsLanGRETunnelIndex_Object = MibTableColumn
sdWANStatsLanGRETunnelIndex = _SdWANStatsLanGRETunnelIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 1),
    _SdWANStatsLanGRETunnelIndex_Type()
)
sdWANStatsLanGRETunnelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelIndex.setStatus("current")
_SdWANStatsLanGRETunnelName_Type = DisplayString
_SdWANStatsLanGRETunnelName_Object = MibTableColumn
sdWANStatsLanGRETunnelName = _SdWANStatsLanGRETunnelName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 2),
    _SdWANStatsLanGRETunnelName_Type()
)
sdWANStatsLanGRETunnelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelName.setStatus("current")
_SdWANStatsLanGRETunnelState_Type = DisplayString
_SdWANStatsLanGRETunnelState_Object = MibTableColumn
sdWANStatsLanGRETunnelState = _SdWANStatsLanGRETunnelState_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 3),
    _SdWANStatsLanGRETunnelState_Type()
)
sdWANStatsLanGRETunnelState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelState.setStatus("current")
_SdWANStatsLanGRETunnelKeepaliveRequestSent_Type = Counter64
_SdWANStatsLanGRETunnelKeepaliveRequestSent_Object = MibTableColumn
sdWANStatsLanGRETunnelKeepaliveRequestSent = _SdWANStatsLanGRETunnelKeepaliveRequestSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 4),
    _SdWANStatsLanGRETunnelKeepaliveRequestSent_Type()
)
sdWANStatsLanGRETunnelKeepaliveRequestSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelKeepaliveRequestSent.setStatus("current")
_SdWANStatsLanGRETunnelKeepaliveReplyReceived_Type = Counter64
_SdWANStatsLanGRETunnelKeepaliveReplyReceived_Object = MibTableColumn
sdWANStatsLanGRETunnelKeepaliveReplyReceived = _SdWANStatsLanGRETunnelKeepaliveReplyReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 5),
    _SdWANStatsLanGRETunnelKeepaliveReplyReceived_Type()
)
sdWANStatsLanGRETunnelKeepaliveReplyReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelKeepaliveReplyReceived.setStatus("current")
_SdWANStatsLanGRETunnelKeepaliveReplySent_Type = Counter64
_SdWANStatsLanGRETunnelKeepaliveReplySent_Object = MibTableColumn
sdWANStatsLanGRETunnelKeepaliveReplySent = _SdWANStatsLanGRETunnelKeepaliveReplySent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 6),
    _SdWANStatsLanGRETunnelKeepaliveReplySent_Type()
)
sdWANStatsLanGRETunnelKeepaliveReplySent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelKeepaliveReplySent.setStatus("current")
_SdWANStatsLanGRETunnelPacketsSent_Type = Counter64
_SdWANStatsLanGRETunnelPacketsSent_Object = MibTableColumn
sdWANStatsLanGRETunnelPacketsSent = _SdWANStatsLanGRETunnelPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 7),
    _SdWANStatsLanGRETunnelPacketsSent_Type()
)
sdWANStatsLanGRETunnelPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelPacketsSent.setStatus("current")
_SdWANStatsLanGRETunnelBytesSent_Type = Counter64
_SdWANStatsLanGRETunnelBytesSent_Object = MibTableColumn
sdWANStatsLanGRETunnelBytesSent = _SdWANStatsLanGRETunnelBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 8),
    _SdWANStatsLanGRETunnelBytesSent_Type()
)
sdWANStatsLanGRETunnelBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelBytesSent.setStatus("current")
_SdWANStatsLanGRETunnelPacketsSentDropped_Type = Counter64
_SdWANStatsLanGRETunnelPacketsSentDropped_Object = MibTableColumn
sdWANStatsLanGRETunnelPacketsSentDropped = _SdWANStatsLanGRETunnelPacketsSentDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 9),
    _SdWANStatsLanGRETunnelPacketsSentDropped_Type()
)
sdWANStatsLanGRETunnelPacketsSentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelPacketsSentDropped.setStatus("current")
_SdWANStatsLanGRETunnelBytesSentDropped_Type = Counter64
_SdWANStatsLanGRETunnelBytesSentDropped_Object = MibTableColumn
sdWANStatsLanGRETunnelBytesSentDropped = _SdWANStatsLanGRETunnelBytesSentDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 10),
    _SdWANStatsLanGRETunnelBytesSentDropped_Type()
)
sdWANStatsLanGRETunnelBytesSentDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelBytesSentDropped.setStatus("current")
_SdWANStatsLanGRETunnelPacketsSentFragmented_Type = Counter64
_SdWANStatsLanGRETunnelPacketsSentFragmented_Object = MibTableColumn
sdWANStatsLanGRETunnelPacketsSentFragmented = _SdWANStatsLanGRETunnelPacketsSentFragmented_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 11),
    _SdWANStatsLanGRETunnelPacketsSentFragmented_Type()
)
sdWANStatsLanGRETunnelPacketsSentFragmented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelPacketsSentFragmented.setStatus("current")
_SdWANStatsLanGRETunnelPacketsReceived_Type = Counter64
_SdWANStatsLanGRETunnelPacketsReceived_Object = MibTableColumn
sdWANStatsLanGRETunnelPacketsReceived = _SdWANStatsLanGRETunnelPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 12),
    _SdWANStatsLanGRETunnelPacketsReceived_Type()
)
sdWANStatsLanGRETunnelPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelPacketsReceived.setStatus("current")
_SdWANStatsLanGRETunnelBytesReceived_Type = Counter64
_SdWANStatsLanGRETunnelBytesReceived_Object = MibTableColumn
sdWANStatsLanGRETunnelBytesReceived = _SdWANStatsLanGRETunnelBytesReceived_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 13),
    _SdWANStatsLanGRETunnelBytesReceived_Type()
)
sdWANStatsLanGRETunnelBytesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelBytesReceived.setStatus("current")
_SdWANStatsLanGRETunnelPacketsReceivedDropped_Type = Counter64
_SdWANStatsLanGRETunnelPacketsReceivedDropped_Object = MibTableColumn
sdWANStatsLanGRETunnelPacketsReceivedDropped = _SdWANStatsLanGRETunnelPacketsReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 14),
    _SdWANStatsLanGRETunnelPacketsReceivedDropped_Type()
)
sdWANStatsLanGRETunnelPacketsReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelPacketsReceivedDropped.setStatus("current")
_SdWANStatsLanGRETunnelBytesReceivedDropped_Type = Counter64
_SdWANStatsLanGRETunnelBytesReceivedDropped_Object = MibTableColumn
sdWANStatsLanGRETunnelBytesReceivedDropped = _SdWANStatsLanGRETunnelBytesReceivedDropped_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 15),
    _SdWANStatsLanGRETunnelBytesReceivedDropped_Type()
)
sdWANStatsLanGRETunnelBytesReceivedDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelBytesReceivedDropped.setStatus("current")
_SdWANStatsLanGRETunnelRoutingDomainName_Type = DisplayString
_SdWANStatsLanGRETunnelRoutingDomainName_Object = MibTableColumn
sdWANStatsLanGRETunnelRoutingDomainName = _SdWANStatsLanGRETunnelRoutingDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 2, 23, 2, 1, 16),
    _SdWANStatsLanGRETunnelRoutingDomainName_Type()
)
sdWANStatsLanGRETunnelRoutingDomainName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANStatsLanGRETunnelRoutingDomainName.setStatus("current")
_SdWANEvents_ObjectIdentity = ObjectIdentity
sdWANEvents = _SdWANEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3)
)
_SdWANEventScalars_ObjectIdentity = ObjectIdentity
sdWANEventScalars = _SdWANEventScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 1)
)


class _SdWANNumEvents_Type(Gauge32):
    """Custom type sdWANNumEvents based on Gauge32"""
    defaultValue = 0


_SdWANNumEvents_Type.__name__ = "Gauge32"
_SdWANNumEvents_Object = MibScalar
sdWANNumEvents = _SdWANNumEvents_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 1, 1),
    _SdWANNumEvents_Type()
)
sdWANNumEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANNumEvents.setStatus("current")
_SdWANEventTable_Object = MibTable
sdWANEventTable = _SdWANEventTable_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2)
)
if mibBuilder.loadTexts:
    sdWANEventTable.setStatus("current")
_SdWANEventEntry_Object = MibTableRow
sdWANEventEntry = _SdWANEventEntry_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1)
)
sdWANEventEntry.setIndexNames(
    (0, "CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventIndex"),
)
if mibBuilder.loadTexts:
    sdWANEventEntry.setStatus("current")
_SdWANEventIndex_Type = Integer32
_SdWANEventIndex_Object = MibTableColumn
sdWANEventIndex = _SdWANEventIndex_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1, 1),
    _SdWANEventIndex_Type()
)
sdWANEventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANEventIndex.setStatus("current")
_SdWANEventID_Type = Integer32
_SdWANEventID_Object = MibTableColumn
sdWANEventID = _SdWANEventID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1, 2),
    _SdWANEventID_Type()
)
sdWANEventID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANEventID.setStatus("current")
_SdWANEventObjectID_Type = Integer32
_SdWANEventObjectID_Object = MibTableColumn
sdWANEventObjectID = _SdWANEventObjectID_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1, 3),
    _SdWANEventObjectID_Type()
)
sdWANEventObjectID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANEventObjectID.setStatus("current")
_SdWANEventObjectName_Type = DisplayString
_SdWANEventObjectName_Object = MibTableColumn
sdWANEventObjectName = _SdWANEventObjectName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1, 4),
    _SdWANEventObjectName_Type()
)
sdWANEventObjectName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANEventObjectName.setStatus("current")
_SdWANEventObjectType_Type = SdWANEventObjectTypeEnum
_SdWANEventObjectType_Object = MibTableColumn
sdWANEventObjectType = _SdWANEventObjectType_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1, 5),
    _SdWANEventObjectType_Type()
)
sdWANEventObjectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANEventObjectType.setStatus("current")
_SdWANEventTime_Type = DisplayString
_SdWANEventTime_Object = MibTableColumn
sdWANEventTime = _SdWANEventTime_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1, 6),
    _SdWANEventTime_Type()
)
sdWANEventTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANEventTime.setStatus("current")
_SdWANEventType_Type = SdWANEventStateEnum
_SdWANEventType_Object = MibTableColumn
sdWANEventType = _SdWANEventType_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1, 7),
    _SdWANEventType_Type()
)
sdWANEventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANEventType.setStatus("current")
_SdWANEventSeverity_Type = SdWANEventSeverityEnum
_SdWANEventSeverity_Object = MibTableColumn
sdWANEventSeverity = _SdWANEventSeverity_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1, 8),
    _SdWANEventSeverity_Type()
)
sdWANEventSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANEventSeverity.setStatus("current")
_SdWANEventDescription_Type = DisplayString
_SdWANEventDescription_Object = MibTableColumn
sdWANEventDescription = _SdWANEventDescription_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 2, 1, 9),
    _SdWANEventDescription_Type()
)
sdWANEventDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANEventDescription.setStatus("current")
_SdWANNetworkEventScalars_ObjectIdentity = ObjectIdentity
sdWANNetworkEventScalars = _SdWANNetworkEventScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 3)
)
_SdWANNetworkEventSiteName_Type = DisplayString
_SdWANNetworkEventSiteName_Object = MibScalar
sdWANNetworkEventSiteName = _SdWANNetworkEventSiteName_Object(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 2, 3, 3, 1),
    _SdWANNetworkEventSiteName_Type()
)
sdWANNetworkEventSiteName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdWANNetworkEventSiteName.setStatus("current")
_SdWANNotifs_ObjectIdentity = ObjectIdentity
sdWANNotifs = _SdWANNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 3)
)

# Managed Objects groups


# Notification objects

sdWANEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 3, 1)
)
sdWANEventNotification.setObjects(
      *(("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventIndex"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventID"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventObjectID"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventObjectName"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventObjectType"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventTime"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventType"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventSeverity"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventDescription"))
)
if mibBuilder.loadTexts:
    sdWANEventNotification.setStatus(
        "current"
    )

sdWANNetworkEventNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 3845, 31, 4, 3, 2)
)
sdWANNetworkEventNotification.setObjects(
      *(("CITRIX-NetScaler-SD-WAN-MIB", "sdWANNetworkEventSiteName"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventID"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventObjectID"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventObjectName"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventObjectType"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventTime"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventType"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventSeverity"),
        ("CITRIX-NetScaler-SD-WAN-MIB", "sdWANEventDescription"))
)
if mibBuilder.loadTexts:
    sdWANNetworkEventNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CITRIX-NetScaler-SD-WAN-MIB",
    **{"SdWANEventObjectTypeEnum": SdWANEventObjectTypeEnum,
       "SdWANEventSeverityEnum": SdWANEventSeverityEnum,
       "SdWANEventStateEnum": SdWANEventStateEnum,
       "citrix": citrix,
       "sdWANMIB": sdWANMIB,
       "sdWANStatusMIB": sdWANStatusMIB,
       "sdWANObjects": sdWANObjects,
       "sdWANConfiguration": sdWANConfiguration,
       "sdWANStatistics": sdWANStatistics,
       "sdWANStatsAppliances": sdWANStatsAppliances,
       "sdWANStatsApplianceScalars": sdWANStatsApplianceScalars,
       "sdWANStatsApplianceName": sdWANStatsApplianceName,
       "sdWANStatsApplianceBytesSent": sdWANStatsApplianceBytesSent,
       "sdWANStatsAppliancePacketsSent": sdWANStatsAppliancePacketsSent,
       "sdWANStatsApplianceBytesReceived": sdWANStatsApplianceBytesReceived,
       "sdWANStatsAppliancePacketsReceived": sdWANStatsAppliancePacketsReceived,
       "sdWANStatsApplianceBytesDropped": sdWANStatsApplianceBytesDropped,
       "sdWANStatsAppliancePacketsDropped": sdWANStatsAppliancePacketsDropped,
       "sdWANStatsApplianceState": sdWANStatsApplianceState,
       "sdWANStatsApplianceHAState": sdWANStatsApplianceHAState,
       "sdWANStatsApplianceSerialNumber": sdWANStatsApplianceSerialNumber,
       "sdWANStatsApplianceOSVersion": sdWANStatsApplianceOSVersion,
       "sdWANStatsApplianceSoftwareVersion": sdWANStatsApplianceSoftwareVersion,
       "sdWANStatsApplianceConfigCreatedOn": sdWANStatsApplianceConfigCreatedOn,
       "sdWANStatsApplianceServiceUptime": sdWANStatsApplianceServiceUptime,
       "sdWANStatsApplianceApplianceUptime": sdWANStatsApplianceApplianceUptime,
       "sdWANStatsEthernetInterfaces": sdWANStatsEthernetInterfaces,
       "sdWANStatsEthernetInterfaceScalars": sdWANStatsEthernetInterfaceScalars,
       "sdWANStatsNumEthernetInterfaces": sdWANStatsNumEthernetInterfaces,
       "sdWANStatsEthernetInterfaceTable": sdWANStatsEthernetInterfaceTable,
       "sdWANStatsEthernetInterfaceEntry": sdWANStatsEthernetInterfaceEntry,
       "sdWANStatsEthernetInterfaceIndex": sdWANStatsEthernetInterfaceIndex,
       "sdWANStatsEthernetInterfaceIfIndex": sdWANStatsEthernetInterfaceIfIndex,
       "sdWANStatsEthernetInterfaceName": sdWANStatsEthernetInterfaceName,
       "sdWANStatsEthernetInterfaceBytesSent": sdWANStatsEthernetInterfaceBytesSent,
       "sdWANStatsEthernetInterfacePacketsSent": sdWANStatsEthernetInterfacePacketsSent,
       "sdWANStatsEthernetInterfaceBytesReceived": sdWANStatsEthernetInterfaceBytesReceived,
       "sdWANStatsEthernetInterfacePacketsReceived": sdWANStatsEthernetInterfacePacketsReceived,
       "sdWANStatsEthernetInterfaceBytesDropped": sdWANStatsEthernetInterfaceBytesDropped,
       "sdWANStatsEthernetInterfacePacketsDropped": sdWANStatsEthernetInterfacePacketsDropped,
       "sdWANStatsRules": sdWANStatsRules,
       "sdWANStatsRuleScalars": sdWANStatsRuleScalars,
       "sdWANStatsNumRules": sdWANStatsNumRules,
       "sdWANStatsRuleTable": sdWANStatsRuleTable,
       "sdWANStatsRuleEntry": sdWANStatsRuleEntry,
       "sdWANStatsRuleIndex": sdWANStatsRuleIndex,
       "sdWANStatsRuleID": sdWANStatsRuleID,
       "sdWANStatsRuleApplicationName": sdWANStatsRuleApplicationName,
       "sdWANStatsRuleLANToWANHitCount": sdWANStatsRuleLANToWANHitCount,
       "sdWANStatsRuleWANToLANHitCount": sdWANStatsRuleWANToLANHitCount,
       "sdWANStatsRuleBytesSent": sdWANStatsRuleBytesSent,
       "sdWANStatsRulePacketsSent": sdWANStatsRulePacketsSent,
       "sdWANStatsRuleBytesReceived": sdWANStatsRuleBytesReceived,
       "sdWANStatsRulePacketsReceived": sdWANStatsRulePacketsReceived,
       "sdWANStatsRuleBytesDropped": sdWANStatsRuleBytesDropped,
       "sdWANStatsRulePacketsDropped": sdWANStatsRulePacketsDropped,
       "sdWANStatsRuleLastActiveNMinuteAgo": sdWANStatsRuleLastActiveNMinuteAgo,
       "sdWANStatsWANLinks": sdWANStatsWANLinks,
       "sdWANStatsWANLinkScalars": sdWANStatsWANLinkScalars,
       "sdWANStatsNumWANLinks": sdWANStatsNumWANLinks,
       "sdWANStatsWANLinkTable": sdWANStatsWANLinkTable,
       "sdWANStatsWANLinkEntry": sdWANStatsWANLinkEntry,
       "sdWANStatsWANLinkIndex": sdWANStatsWANLinkIndex,
       "sdWANStatsWANLinkID": sdWANStatsWANLinkID,
       "sdWANStatsWANLinkName": sdWANStatsWANLinkName,
       "sdWANStatsWANLinkState": sdWANStatsWANLinkState,
       "sdWANStatsWANLinkBytesSent": sdWANStatsWANLinkBytesSent,
       "sdWANStatsWANLinkPacketsSent": sdWANStatsWANLinkPacketsSent,
       "sdWANStatsWANLinkBytesReceived": sdWANStatsWANLinkBytesReceived,
       "sdWANStatsWANLinkPacketsReceived": sdWANStatsWANLinkPacketsReceived,
       "sdWANStatsWANLinkBytesDropped": sdWANStatsWANLinkBytesDropped,
       "sdWANStatsWANLinkPacketsDropped": sdWANStatsWANLinkPacketsDropped,
       "sdWANStatsVPaths": sdWANStatsVPaths,
       "sdWANStatsVPathScalars": sdWANStatsVPathScalars,
       "sdWANStatsNumVPaths": sdWANStatsNumVPaths,
       "sdWANStatsVPathTable": sdWANStatsVPathTable,
       "sdWANStatsVPathEntry": sdWANStatsVPathEntry,
       "sdWANStatsVPathIndex": sdWANStatsVPathIndex,
       "sdWANStatsVPathID": sdWANStatsVPathID,
       "sdWANStatsVPathName": sdWANStatsVPathName,
       "sdWANStatsVPathState": sdWANStatsVPathState,
       "sdWANStatsVPathBytesSent": sdWANStatsVPathBytesSent,
       "sdWANStatsVPathPacketsSent": sdWANStatsVPathPacketsSent,
       "sdWANStatsVPathBytesReceived": sdWANStatsVPathBytesReceived,
       "sdWANStatsVPathPacketsReceived": sdWANStatsVPathPacketsReceived,
       "sdWANStatsVPathNumPaths": sdWANStatsVPathNumPaths,
       "sdWANStatsVPathNumRules": sdWANStatsVPathNumRules,
       "sdWANStatsVPathSendBytesDropped": sdWANStatsVPathSendBytesDropped,
       "sdWANStatsVPathSendPacketsDropped": sdWANStatsVPathSendPacketsDropped,
       "sdWANStatsVPathSendPacketsLost": sdWANStatsVPathSendPacketsLost,
       "sdWANStatsVPathSendPacketsOOO": sdWANStatsVPathSendPacketsOOO,
       "sdWANStatsVPathSendBOWTms": sdWANStatsVPathSendBOWTms,
       "sdWANStatsVPathSendJitterms": sdWANStatsVPathSendJitterms,
       "sdWANStatsVPathReceiveBytesDropped": sdWANStatsVPathReceiveBytesDropped,
       "sdWANStatsVPathReceivePacketsDropped": sdWANStatsVPathReceivePacketsDropped,
       "sdWANStatsVPathReceivePacketsLost": sdWANStatsVPathReceivePacketsLost,
       "sdWANStatsVPathReceivePacketsOOO": sdWANStatsVPathReceivePacketsOOO,
       "sdWANStatsVPathReceiveBOWTms": sdWANStatsVPathReceiveBOWTms,
       "sdWANStatsVPathReceiveJitterms": sdWANStatsVPathReceiveJitterms,
       "sdWANStatsWANPaths": sdWANStatsWANPaths,
       "sdWANStatsWANPathTable": sdWANStatsWANPathTable,
       "sdWANStatsWANPathEntry": sdWANStatsWANPathEntry,
       "sdWANStatsWANPathVPathIndex": sdWANStatsWANPathVPathIndex,
       "sdWANStatsWANPathPathIndex": sdWANStatsWANPathPathIndex,
       "sdWANStatsWANPathVPathID": sdWANStatsWANPathVPathID,
       "sdWANStatsWANPathPathID": sdWANStatsWANPathPathID,
       "sdWANStatsWANPathName": sdWANStatsWANPathName,
       "sdWANStatsWANPathState": sdWANStatsWANPathState,
       "sdWANStatsWANPathBytesSent": sdWANStatsWANPathBytesSent,
       "sdWANStatsWANPathPacketsSent": sdWANStatsWANPathPacketsSent,
       "sdWANStatsWANPathBytesReceived": sdWANStatsWANPathBytesReceived,
       "sdWANStatsWANPathPacketsReceived": sdWANStatsWANPathPacketsReceived,
       "sdWANStatsWANPathBOWTms": sdWANStatsWANPathBOWTms,
       "sdWANStatsWANPathJitterms": sdWANStatsWANPathJitterms,
       "sdWANStatsWANPathPacketsLost": sdWANStatsWANPathPacketsLost,
       "sdWANStatsWANPathPacketsOOO": sdWANStatsWANPathPacketsOOO,
       "sdWANStatsWANClasses": sdWANStatsWANClasses,
       "sdWANStatsWANClassTable": sdWANStatsWANClassTable,
       "sdWANStatsWANClassEntry": sdWANStatsWANClassEntry,
       "sdWANStatsWANClassVPathIndex": sdWANStatsWANClassVPathIndex,
       "sdWANStatsWANClassClassIndex": sdWANStatsWANClassClassIndex,
       "sdWANStatsWANClassVPathID": sdWANStatsWANClassVPathID,
       "sdWANStatsWANClassClassID": sdWANStatsWANClassClassID,
       "sdWANStatsWANClassName": sdWANStatsWANClassName,
       "sdWANStatsWANClassType": sdWANStatsWANClassType,
       "sdWANStatsWANClassBytesSent": sdWANStatsWANClassBytesSent,
       "sdWANStatsWANClassPacketsSent": sdWANStatsWANClassPacketsSent,
       "sdWANStatsWANClassBytesPending": sdWANStatsWANClassBytesPending,
       "sdWANStatsWANClassPacketsPending": sdWANStatsWANClassPacketsPending,
       "sdWANStatsWANClassBytesDropped": sdWANStatsWANClassBytesDropped,
       "sdWANStatsWANClassPacketsDropped": sdWANStatsWANClassPacketsDropped,
       "sdWANStatsWANRules": sdWANStatsWANRules,
       "sdWANStatsWANRuleTable": sdWANStatsWANRuleTable,
       "sdWANStatsWANRuleEntry": sdWANStatsWANRuleEntry,
       "sdWANStatsWANRuleVPathIndex": sdWANStatsWANRuleVPathIndex,
       "sdWANStatsWANRuleRuleIndex": sdWANStatsWANRuleRuleIndex,
       "sdWANStatsWANRuleVPathID": sdWANStatsWANRuleVPathID,
       "sdWANStatsWANRuleRuleID": sdWANStatsWANRuleRuleID,
       "sdWANStatsWANRuleGlobalRuleIndex": sdWANStatsWANRuleGlobalRuleIndex,
       "sdWANStatsWANRuleApplicationName": sdWANStatsWANRuleApplicationName,
       "sdWANStatsWANRuleLANToWANHitCount": sdWANStatsWANRuleLANToWANHitCount,
       "sdWANStatsWANRuleWANToLANHitCount": sdWANStatsWANRuleWANToLANHitCount,
       "sdWANStatsWANRuleBytesSent": sdWANStatsWANRuleBytesSent,
       "sdWANStatsWANRulePacketsSent": sdWANStatsWANRulePacketsSent,
       "sdWANStatsWANRuleBytesReceived": sdWANStatsWANRuleBytesReceived,
       "sdWANStatsWANRulePacketsReceived": sdWANStatsWANRulePacketsReceived,
       "sdWANStatsWANRuleBytesDropped": sdWANStatsWANRuleBytesDropped,
       "sdWANStatsWANRulePacketsDropped": sdWANStatsWANRulePacketsDropped,
       "sdWANStatsWANRuleLastActiveNMinuteAgo": sdWANStatsWANRuleLastActiveNMinuteAgo,
       "sdWANStatsInternet": sdWANStatsInternet,
       "sdWANStatsInternetScalars": sdWANStatsInternetScalars,
       "sdWANStatsInternetBytesSent": sdWANStatsInternetBytesSent,
       "sdWANStatsInternetPacketsSent": sdWANStatsInternetPacketsSent,
       "sdWANStatsInternetBytesReceived": sdWANStatsInternetBytesReceived,
       "sdWANStatsInternetPacketsReceived": sdWANStatsInternetPacketsReceived,
       "sdWANStatsInternetBytesDropped": sdWANStatsInternetBytesDropped,
       "sdWANStatsInternetPacketsDropped": sdWANStatsInternetPacketsDropped,
       "sdWANStatsInternetNumRules": sdWANStatsInternetNumRules,
       "sdWANStatsInternetRuleTable": sdWANStatsInternetRuleTable,
       "sdWANStatsInternetRuleEntry": sdWANStatsInternetRuleEntry,
       "sdWANStatsInternetRuleIndex": sdWANStatsInternetRuleIndex,
       "sdWANStatsInternetRuleID": sdWANStatsInternetRuleID,
       "sdWANStatsInternetRuleGlobalRuleIndex": sdWANStatsInternetRuleGlobalRuleIndex,
       "sdWANStatsInternetRuleApplicationName": sdWANStatsInternetRuleApplicationName,
       "sdWANStatsInternetRuleLANToWANHitCount": sdWANStatsInternetRuleLANToWANHitCount,
       "sdWANStatsInternetRuleWANToLANHitCount": sdWANStatsInternetRuleWANToLANHitCount,
       "sdWANStatsInternetRuleBytesSent": sdWANStatsInternetRuleBytesSent,
       "sdWANStatsInternetRulePacketsSent": sdWANStatsInternetRulePacketsSent,
       "sdWANStatsInternetRuleBytesReceived": sdWANStatsInternetRuleBytesReceived,
       "sdWANStatsInternetRulePacketsReceived": sdWANStatsInternetRulePacketsReceived,
       "sdWANStatsInternetRuleBytesDropped": sdWANStatsInternetRuleBytesDropped,
       "sdWANStatsInternetRulePacketsDropped": sdWANStatsInternetRulePacketsDropped,
       "sdWANStatsInternetRuleLastActiveNMinuteAgo": sdWANStatsInternetRuleLastActiveNMinuteAgo,
       "sdWANStatsIntranet": sdWANStatsIntranet,
       "sdWANStatsIntranetScalars": sdWANStatsIntranetScalars,
       "sdWANStatsIntranetNumIntranetServices": sdWANStatsIntranetNumIntranetServices,
       "sdWANStatsIntranetsTable": sdWANStatsIntranetsTable,
       "sdWANStatsIntranetsEntry": sdWANStatsIntranetsEntry,
       "sdWANStatsIntranetsIndex": sdWANStatsIntranetsIndex,
       "sdWANStatsIntranetsID": sdWANStatsIntranetsID,
       "sdWANStatsIntranetsName": sdWANStatsIntranetsName,
       "sdWANStatsIntranetsBytesSent": sdWANStatsIntranetsBytesSent,
       "sdWANStatsIntranetsPacketsSent": sdWANStatsIntranetsPacketsSent,
       "sdWANStatsIntranetsBytesReceived": sdWANStatsIntranetsBytesReceived,
       "sdWANStatsIntranetsPacketsReceived": sdWANStatsIntranetsPacketsReceived,
       "sdWANStatsIntranetsBytesDropped": sdWANStatsIntranetsBytesDropped,
       "sdWANStatsIntranetsPacketsDropped": sdWANStatsIntranetsPacketsDropped,
       "sdWANStatsIntranetsNumRules": sdWANStatsIntranetsNumRules,
       "sdWANStatsIntranetsRoutingDomainName": sdWANStatsIntranetsRoutingDomainName,
       "sdWANStatsIntranetRulesTable": sdWANStatsIntranetRulesTable,
       "sdWANStatsIntranetRulesEntry": sdWANStatsIntranetRulesEntry,
       "sdWANStatsIntranetRulesIntranetIndex": sdWANStatsIntranetRulesIntranetIndex,
       "sdWANStatsIntranetRulesRuleIndex": sdWANStatsIntranetRulesRuleIndex,
       "sdWANStatsIntranetRulesID": sdWANStatsIntranetRulesID,
       "sdWANStatsIntranetRulesGlobalRuleIndex": sdWANStatsIntranetRulesGlobalRuleIndex,
       "sdWANStatsIntranetRulesIntranetName": sdWANStatsIntranetRulesIntranetName,
       "sdWANStatsIntranetRulesApplicationName": sdWANStatsIntranetRulesApplicationName,
       "sdWANStatsIntranetRulesLANToWANHitCount": sdWANStatsIntranetRulesLANToWANHitCount,
       "sdWANStatsIntranetRulesWANToLANHitCount": sdWANStatsIntranetRulesWANToLANHitCount,
       "sdWANStatsIntranetRulesBytesSent": sdWANStatsIntranetRulesBytesSent,
       "sdWANStatsIntranetRulesPacketsSent": sdWANStatsIntranetRulesPacketsSent,
       "sdWANStatsIntranetRulesBytesReceived": sdWANStatsIntranetRulesBytesReceived,
       "sdWANStatsIntranetRulesPacketsReceived": sdWANStatsIntranetRulesPacketsReceived,
       "sdWANStatsIntranetRulesBytesDropped": sdWANStatsIntranetRulesBytesDropped,
       "sdWANStatsIntranetRulesPacketsDropped": sdWANStatsIntranetRulesPacketsDropped,
       "sdWANStatsIntranetRulesLastActiveNMinuteAgo": sdWANStatsIntranetRulesLastActiveNMinuteAgo,
       "sdWANStatsPassthrough": sdWANStatsPassthrough,
       "sdWANStatsPassthroughScalars": sdWANStatsPassthroughScalars,
       "sdWANStatsPassthroughBytesSent": sdWANStatsPassthroughBytesSent,
       "sdWANStatsPassthroughPacketsSent": sdWANStatsPassthroughPacketsSent,
       "sdWANStatsPassthroughBytesReceived": sdWANStatsPassthroughBytesReceived,
       "sdWANStatsPassthroughPacketsReceived": sdWANStatsPassthroughPacketsReceived,
       "sdWANStatsPassthroughBytesDropped": sdWANStatsPassthroughBytesDropped,
       "sdWANStatsPassthroughPacketsDropped": sdWANStatsPassthroughPacketsDropped,
       "sdWANStatsRoutesV2": sdWANStatsRoutesV2,
       "sdWANStatsRouteScalars": sdWANStatsRouteScalars,
       "sdWANStatsNumRoutesV2": sdWANStatsNumRoutesV2,
       "sdWANStatsRouteTableV2": sdWANStatsRouteTableV2,
       "sdWANStatsRouteEntryV2": sdWANStatsRouteEntryV2,
       "sdWANStatsRouteIndexV2": sdWANStatsRouteIndexV2,
       "sdWANStatsRouteNetworkAddr": sdWANStatsRouteNetworkAddr,
       "sdWANStatsRouteNetworkPrefix": sdWANStatsRouteNetworkPrefix,
       "sdWANStatsRouteGateway": sdWANStatsRouteGateway,
       "sdWANStatsRouteServiceType": sdWANStatsRouteServiceType,
       "sdWANStatsRouteServiceID": sdWANStatsRouteServiceID,
       "sdWANStatsRouteServiceName": sdWANStatsRouteServiceName,
       "sdWANStatsRouteReachable": sdWANStatsRouteReachable,
       "sdWANStatsRouteSiteName": sdWANStatsRouteSiteName,
       "sdWANStatsRouteType": sdWANStatsRouteType,
       "sdWANStatsRouteNeighborDirect": sdWANStatsRouteNeighborDirect,
       "sdWANStatsRouteCost": sdWANStatsRouteCost,
       "sdWANStatsRouteHitCountV2": sdWANStatsRouteHitCountV2,
       "sdWANStatsRouteEligible": sdWANStatsRouteEligible,
       "sdWANStatsRouteEligibilityType": sdWANStatsRouteEligibilityType,
       "sdWANStatsRouteEligibilityValue": sdWANStatsRouteEligibilityValue,
       "sdWANStatsRouteProtocol": sdWANStatsRouteProtocol,
       "sdWANStatsRouteRoutingDomainName": sdWANStatsRouteRoutingDomainName,
       "sdWANStatsDynamicVPaths": sdWANStatsDynamicVPaths,
       "sdWANStatsDynamicVPathScalars": sdWANStatsDynamicVPathScalars,
       "sdWANStatsNumDynamicVPaths": sdWANStatsNumDynamicVPaths,
       "sdWANStatsDynamicVPathTable": sdWANStatsDynamicVPathTable,
       "sdWANStatsDynamicVPathEntry": sdWANStatsDynamicVPathEntry,
       "sdWANStatsDynamicVPathIndex": sdWANStatsDynamicVPathIndex,
       "sdWANStatsDynamicVPathID": sdWANStatsDynamicVPathID,
       "sdWANStatsDynamicVPathName": sdWANStatsDynamicVPathName,
       "sdWANStatsDynamicVPathState": sdWANStatsDynamicVPathState,
       "sdWANStatsDynamicVPathTimeSinceCreation": sdWANStatsDynamicVPathTimeSinceCreation,
       "sdWANStatsDynamicVPathBytesSent": sdWANStatsDynamicVPathBytesSent,
       "sdWANStatsDynamicVPathPacketsSent": sdWANStatsDynamicVPathPacketsSent,
       "sdWANStatsDynamicVPathSendBytesDropped": sdWANStatsDynamicVPathSendBytesDropped,
       "sdWANStatsDynamicVPathSendPacketsDropped": sdWANStatsDynamicVPathSendPacketsDropped,
       "sdWANStatsDynamicVPathSendPacketsLost": sdWANStatsDynamicVPathSendPacketsLost,
       "sdWANStatsDynamicVPathSendPacketsOOO": sdWANStatsDynamicVPathSendPacketsOOO,
       "sdWANStatsDynamicVPathSendBOWTms": sdWANStatsDynamicVPathSendBOWTms,
       "sdWANStatsDynamicVPathSendJitterms": sdWANStatsDynamicVPathSendJitterms,
       "sdWANStatsDynamicVPathBytesReceived": sdWANStatsDynamicVPathBytesReceived,
       "sdWANStatsDynamicVPathPacketsReceived": sdWANStatsDynamicVPathPacketsReceived,
       "sdWANStatsDynamicVPathReceiveBytesDropped": sdWANStatsDynamicVPathReceiveBytesDropped,
       "sdWANStatsDynamicVPathReceivePacketsDropped": sdWANStatsDynamicVPathReceivePacketsDropped,
       "sdWANStatsDynamicVPathReceivePacketsLost": sdWANStatsDynamicVPathReceivePacketsLost,
       "sdWANStatsDynamicVPathReceivePacketsOOO": sdWANStatsDynamicVPathReceivePacketsOOO,
       "sdWANStatsDynamicVPathReceiveBOWTms": sdWANStatsDynamicVPathReceiveBOWTms,
       "sdWANStatsDynamicVPathReceiveJitterms": sdWANStatsDynamicVPathReceiveJitterms,
       "sdWANStatsDynamicVPathNumPaths": sdWANStatsDynamicVPathNumPaths,
       "sdWANStatsDynamicVPathNumRules": sdWANStatsDynamicVPathNumRules,
       "sdWANStatsDynamicWANPaths": sdWANStatsDynamicWANPaths,
       "sdWANStatsDynamicWANPathTable": sdWANStatsDynamicWANPathTable,
       "sdWANStatsDynamicWANPathEntry": sdWANStatsDynamicWANPathEntry,
       "sdWANStatsDynamicWANPathVPathIndex": sdWANStatsDynamicWANPathVPathIndex,
       "sdWANStatsDynamicWANPathPathIndex": sdWANStatsDynamicWANPathPathIndex,
       "sdWANStatsDynamicWANPathVPathID": sdWANStatsDynamicWANPathVPathID,
       "sdWANStatsDynamicWANPathPathID": sdWANStatsDynamicWANPathPathID,
       "sdWANStatsDynamicWANPathName": sdWANStatsDynamicWANPathName,
       "sdWANStatsDynamicWANPathState": sdWANStatsDynamicWANPathState,
       "sdWANStatsDynamicWANPathBytesSent": sdWANStatsDynamicWANPathBytesSent,
       "sdWANStatsDynamicWANPathPacketsSent": sdWANStatsDynamicWANPathPacketsSent,
       "sdWANStatsDynamicWANPathBytesReceived": sdWANStatsDynamicWANPathBytesReceived,
       "sdWANStatsDynamicWANPathPacketsReceived": sdWANStatsDynamicWANPathPacketsReceived,
       "sdWANStatsDynamicWANPathBytesDropped": sdWANStatsDynamicWANPathBytesDropped,
       "sdWANStatsDynamicWANPathPacketsDropped": sdWANStatsDynamicWANPathPacketsDropped,
       "sdWANStatsDynamicWANPathBOWTms": sdWANStatsDynamicWANPathBOWTms,
       "sdWANStatsDynamicWANPathJitterms": sdWANStatsDynamicWANPathJitterms,
       "sdWANStatsDynamicWANPathPacketsLost": sdWANStatsDynamicWANPathPacketsLost,
       "sdWANStatsDynamicWANPathPacketsOOO": sdWANStatsDynamicWANPathPacketsOOO,
       "sdWANStatsDynamicWANClasses": sdWANStatsDynamicWANClasses,
       "sdWANStatsDynamicWANClassTable": sdWANStatsDynamicWANClassTable,
       "sdWANStatsDynamicWANClassEntry": sdWANStatsDynamicWANClassEntry,
       "sdWANStatsDynamicWANClassVPathIndex": sdWANStatsDynamicWANClassVPathIndex,
       "sdWANStatsDynamicWANClassClassIndex": sdWANStatsDynamicWANClassClassIndex,
       "sdWANStatsDynamicWANClassVPathID": sdWANStatsDynamicWANClassVPathID,
       "sdWANStatsDynamicWANClassClassID": sdWANStatsDynamicWANClassClassID,
       "sdWANStatsDynamicWANClassName": sdWANStatsDynamicWANClassName,
       "sdWANStatsDynamicWANClassType": sdWANStatsDynamicWANClassType,
       "sdWANStatsDynamicWANClassBytesSent": sdWANStatsDynamicWANClassBytesSent,
       "sdWANStatsDynamicWANClassPacketsSent": sdWANStatsDynamicWANClassPacketsSent,
       "sdWANStatsDynamicWANClassBytesPending": sdWANStatsDynamicWANClassBytesPending,
       "sdWANStatsDynamicWANClassPacketsPending": sdWANStatsDynamicWANClassPacketsPending,
       "sdWANStatsDynamicWANClassBytesDropped": sdWANStatsDynamicWANClassBytesDropped,
       "sdWANStatsDynamicWANClassPacketsDropped": sdWANStatsDynamicWANClassPacketsDropped,
       "sdWANStatsDynamicWANRules": sdWANStatsDynamicWANRules,
       "sdWANStatsDynamicWANRuleTable": sdWANStatsDynamicWANRuleTable,
       "sdWANStatsDynamicWANRuleEntry": sdWANStatsDynamicWANRuleEntry,
       "sdWANStatsDynamicWANRuleVPathIndex": sdWANStatsDynamicWANRuleVPathIndex,
       "sdWANStatsDynamicWANRuleRuleIndex": sdWANStatsDynamicWANRuleRuleIndex,
       "sdWANStatsDynamicWANRuleVPathID": sdWANStatsDynamicWANRuleVPathID,
       "sdWANStatsDynamicWANRuleRuleID": sdWANStatsDynamicWANRuleRuleID,
       "sdWANStatsDynamicWANRuleGlobalRuleIndex": sdWANStatsDynamicWANRuleGlobalRuleIndex,
       "sdWANStatsDynamicWANRuleApplicationName": sdWANStatsDynamicWANRuleApplicationName,
       "sdWANStatsDynamicWANRuleLANToWANHitCount": sdWANStatsDynamicWANRuleLANToWANHitCount,
       "sdWANStatsDynamicWANRuleWANToLANHitCount": sdWANStatsDynamicWANRuleWANToLANHitCount,
       "sdWANStatsDynamicWANRuleBytesSent": sdWANStatsDynamicWANRuleBytesSent,
       "sdWANStatsDynamicWANRulePacketsSent": sdWANStatsDynamicWANRulePacketsSent,
       "sdWANStatsDynamicWANRuleBytesReceived": sdWANStatsDynamicWANRuleBytesReceived,
       "sdWANStatsDynamicWANRulePacketsReceived": sdWANStatsDynamicWANRulePacketsReceived,
       "sdWANStatsDynamicWANRuleBytesDropped": sdWANStatsDynamicWANRuleBytesDropped,
       "sdWANStatsDynamicWANRulePacketsDropped": sdWANStatsDynamicWANRulePacketsDropped,
       "sdWANStatsDynamicWANRuleLastActiveNMinuteAgo": sdWANStatsDynamicWANRuleLastActiveNMinuteAgo,
       "sdWANStatsArp": sdWANStatsArp,
       "sdWANStatsArpScalars": sdWANStatsArpScalars,
       "sdWANStatsNumArpEntries": sdWANStatsNumArpEntries,
       "sdWANStatsArpTable": sdWANStatsArpTable,
       "sdWANStatsArpEntry": sdWANStatsArpEntry,
       "sdWANStatsArpID": sdWANStatsArpID,
       "sdWANStatsArpIfIndex": sdWANStatsArpIfIndex,
       "sdWANStatsArpVlanTag": sdWANStatsArpVlanTag,
       "sdWANStatsArpIpAddr": sdWANStatsArpIpAddr,
       "sdWANStatsArpPhysAddr": sdWANStatsArpPhysAddr,
       "sdWANStatsArpState": sdWANStatsArpState,
       "sdWANStatsArpType": sdWANStatsArpType,
       "sdWANStatsArpReplyAgeMs": sdWANStatsArpReplyAgeMs,
       "sdWANStatsLanGRETunnels": sdWANStatsLanGRETunnels,
       "sdWANStatsLanGRETunnelScalars": sdWANStatsLanGRETunnelScalars,
       "sdWANStatsNumLanGRETunnels": sdWANStatsNumLanGRETunnels,
       "sdWANStatsLanGRETunnelTable": sdWANStatsLanGRETunnelTable,
       "sdWANStatsLanGRETunnelEntry": sdWANStatsLanGRETunnelEntry,
       "sdWANStatsLanGRETunnelIndex": sdWANStatsLanGRETunnelIndex,
       "sdWANStatsLanGRETunnelName": sdWANStatsLanGRETunnelName,
       "sdWANStatsLanGRETunnelState": sdWANStatsLanGRETunnelState,
       "sdWANStatsLanGRETunnelKeepaliveRequestSent": sdWANStatsLanGRETunnelKeepaliveRequestSent,
       "sdWANStatsLanGRETunnelKeepaliveReplyReceived": sdWANStatsLanGRETunnelKeepaliveReplyReceived,
       "sdWANStatsLanGRETunnelKeepaliveReplySent": sdWANStatsLanGRETunnelKeepaliveReplySent,
       "sdWANStatsLanGRETunnelPacketsSent": sdWANStatsLanGRETunnelPacketsSent,
       "sdWANStatsLanGRETunnelBytesSent": sdWANStatsLanGRETunnelBytesSent,
       "sdWANStatsLanGRETunnelPacketsSentDropped": sdWANStatsLanGRETunnelPacketsSentDropped,
       "sdWANStatsLanGRETunnelBytesSentDropped": sdWANStatsLanGRETunnelBytesSentDropped,
       "sdWANStatsLanGRETunnelPacketsSentFragmented": sdWANStatsLanGRETunnelPacketsSentFragmented,
       "sdWANStatsLanGRETunnelPacketsReceived": sdWANStatsLanGRETunnelPacketsReceived,
       "sdWANStatsLanGRETunnelBytesReceived": sdWANStatsLanGRETunnelBytesReceived,
       "sdWANStatsLanGRETunnelPacketsReceivedDropped": sdWANStatsLanGRETunnelPacketsReceivedDropped,
       "sdWANStatsLanGRETunnelBytesReceivedDropped": sdWANStatsLanGRETunnelBytesReceivedDropped,
       "sdWANStatsLanGRETunnelRoutingDomainName": sdWANStatsLanGRETunnelRoutingDomainName,
       "sdWANEvents": sdWANEvents,
       "sdWANEventScalars": sdWANEventScalars,
       "sdWANNumEvents": sdWANNumEvents,
       "sdWANEventTable": sdWANEventTable,
       "sdWANEventEntry": sdWANEventEntry,
       "sdWANEventIndex": sdWANEventIndex,
       "sdWANEventID": sdWANEventID,
       "sdWANEventObjectID": sdWANEventObjectID,
       "sdWANEventObjectName": sdWANEventObjectName,
       "sdWANEventObjectType": sdWANEventObjectType,
       "sdWANEventTime": sdWANEventTime,
       "sdWANEventType": sdWANEventType,
       "sdWANEventSeverity": sdWANEventSeverity,
       "sdWANEventDescription": sdWANEventDescription,
       "sdWANNetworkEventScalars": sdWANNetworkEventScalars,
       "sdWANNetworkEventSiteName": sdWANNetworkEventSiteName,
       "sdWANNotifs": sdWANNotifs,
       "sdWANEventNotification": sdWANEventNotification,
       "sdWANNetworkEventNotification": sdWANNetworkEventNotification}
)
