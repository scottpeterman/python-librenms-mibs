# SNMP MIB module (ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\exalt\ETHERNET-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:43:03 2025
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

(interface,
 locEthAlarms,
 remEthAlarms) = mibBuilder.importSymbols(
    "ExaltComProducts",
    "interface",
    "locEthAlarms",
    "remEthAlarms")

(AlarmLevelT,
 EnableStatusT,
 EthernetMgmtTypeT) = mibBuilder.importSymbols(
    "ExaltComm",
    "AlarmLevelT",
    "EnableStatusT",
    "EthernetMgmtTypeT")

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


# Types definitions


# TEXTUAL-CONVENTIONS



class EthernetFunctionT(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("traffic", 0),
          ("mgmt", 1),
          ("trafficmgmt", 2))
    )



class EthernetModeT(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("full1000", 0),
          ("half1000", 1),
          ("full100", 2),
          ("half100", 3),
          ("full10", 4),
          ("half10", 5),
          ("auto", 6))
    )



class EthRateLimitTypeT(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("kbps", 0),
          ("mbps", 1))
    )



class EthRateLimitValueT(TextualConvention, Integer32):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_Ethernet_ObjectIdentity = ObjectIdentity
ethernet = _Ethernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ethernet.setStatus("current")
_EthernetNumChannels_Type = Gauge32
_EthernetNumChannels_Object = MibScalar
ethernetNumChannels = _EthernetNumChannels_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 3),
    _EthernetNumChannels_Type()
)
ethernetNumChannels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethernetNumChannels.setStatus("current")
if mibBuilder.loadTexts:
    ethernetNumChannels.setUnits("channels")
_EthernetInterfaces_Object = MibTable
ethernetInterfaces = _EthernetInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4)
)
if mibBuilder.loadTexts:
    ethernetInterfaces.setStatus("current")
_EthernetInterface_Object = MibTableRow
ethernetInterface = _EthernetInterface_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1)
)
ethernetInterface.setIndexNames(
    (0, "ETHERNET-MIB", "function"),
    (0, "ETHERNET-MIB", "mode"),
    (0, "ETHERNET-MIB", "alarm"),
    (0, "ETHERNET-MIB", "mute"),
    (0, "ETHERNET-MIB", "dhcp"),
    (0, "ETHERNET-MIB", "rateConfig"),
    (0, "ETHERNET-MIB", "rateType"),
    (0, "ETHERNET-MIB", "rateLimit"),
)
if mibBuilder.loadTexts:
    ethernetInterface.setStatus("current")
_Function_Type = EthernetFunctionT
_Function_Object = MibTableColumn
function = _Function_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 1),
    _Function_Type()
)
function.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    function.setStatus("current")
_Mode_Type = EthernetModeT
_Mode_Object = MibTableColumn
mode = _Mode_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 2),
    _Mode_Type()
)
mode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mode.setStatus("current")
_Alarm_Type = EnableStatusT
_Alarm_Object = MibTableColumn
alarm = _Alarm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 3),
    _Alarm_Type()
)
alarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alarm.setStatus("current")
_Mute_Type = EnableStatusT
_Mute_Object = MibTableColumn
mute = _Mute_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 4),
    _Mute_Type()
)
mute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mute.setStatus("current")
_RateConfig_Type = EnableStatusT
_RateConfig_Object = MibTableColumn
rateConfig = _RateConfig_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 5),
    _RateConfig_Type()
)
rateConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateConfig.setStatus("current")
_RateType_Type = EthRateLimitTypeT
_RateType_Object = MibTableColumn
rateType = _RateType_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 6),
    _RateType_Type()
)
rateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateType.setStatus("current")
_RateLimit_Type = EthRateLimitValueT
_RateLimit_Object = MibTableColumn
rateLimit = _RateLimit_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 7),
    _RateLimit_Type()
)
rateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rateLimit.setStatus("current")
_Dhcp_Type = EnableStatusT
_Dhcp_Object = MibTableColumn
dhcp = _Dhcp_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 4, 1, 8),
    _Dhcp_Type()
)
dhcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcp.setStatus("current")
_EthernetLearning_Type = EnableStatusT
_EthernetLearning_Object = MibScalar
ethernetLearning = _EthernetLearning_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 5),
    _EthernetLearning_Type()
)
ethernetLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetLearning.setStatus("current")
_EthernetMgmt_Type = EthernetMgmtTypeT
_EthernetMgmt_Object = MibScalar
ethernetMgmt = _EthernetMgmt_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 6),
    _EthernetMgmt_Type()
)
ethernetMgmt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetMgmt.setStatus("current")
_EthernetFlowControl_Type = EnableStatusT
_EthernetFlowControl_Object = MibScalar
ethernetFlowControl = _EthernetFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 7),
    _EthernetFlowControl_Type()
)
ethernetFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethernetFlowControl.setStatus("current")


class _CommitEthernetSettings_Type(DisplayString):
    """Custom type commitEthernetSettings based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 200),
    )


_CommitEthernetSettings_Type.__name__ = "DisplayString"
_CommitEthernetSettings_Object = MibScalar
commitEthernetSettings = _CommitEthernetSettings_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 3, 2, 1, 1000),
    _CommitEthernetSettings_Type()
)
commitEthernetSettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    commitEthernetSettings.setStatus("current")
_LocETHAlarms_Object = MibTable
locETHAlarms = _LocETHAlarms_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    locETHAlarms.setStatus("current")
_LocEthAlarmsEntry_Object = MibTableRow
locEthAlarmsEntry = _LocEthAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2, 1, 1)
)
locEthAlarmsEntry.setIndexNames(
    (0, "ETHERNET-MIB", "locEthAlarm"),
)
if mibBuilder.loadTexts:
    locEthAlarmsEntry.setStatus("current")
_LocEthAlarm_Type = AlarmLevelT
_LocEthAlarm_Object = MibTableColumn
locEthAlarm = _LocEthAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 3, 2, 1, 1, 1),
    _LocEthAlarm_Type()
)
locEthAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    locEthAlarm.setStatus("current")
_RemETHAlarms_Object = MibTable
remETHAlarms = _RemETHAlarms_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2, 1)
)
if mibBuilder.loadTexts:
    remETHAlarms.setStatus("current")
_RemEthAlarmsEntry_Object = MibTableRow
remEthAlarmsEntry = _RemEthAlarmsEntry_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2, 1, 1)
)
remEthAlarmsEntry.setIndexNames(
    (0, "ETHERNET-MIB", "remEthAlarm"),
)
if mibBuilder.loadTexts:
    remEthAlarmsEntry.setStatus("current")
_RemEthAlarm_Type = AlarmLevelT
_RemEthAlarm_Object = MibTableColumn
remEthAlarm = _RemEthAlarm_Object(
    (1, 3, 6, 1, 4, 1, 25651, 1, 2, 4, 2, 4, 2, 1, 1, 1),
    _RemEthAlarm_Type()
)
remEthAlarm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    remEthAlarm.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ETHERNET-MIB",
    **{"EthernetFunctionT": EthernetFunctionT,
       "EthernetModeT": EthernetModeT,
       "EthRateLimitTypeT": EthRateLimitTypeT,
       "EthRateLimitValueT": EthRateLimitValueT,
       "ethernet": ethernet,
       "ethernetNumChannels": ethernetNumChannels,
       "ethernetInterfaces": ethernetInterfaces,
       "ethernetInterface": ethernetInterface,
       "function": function,
       "mode": mode,
       "alarm": alarm,
       "mute": mute,
       "rateConfig": rateConfig,
       "rateType": rateType,
       "rateLimit": rateLimit,
       "dhcp": dhcp,
       "ethernetLearning": ethernetLearning,
       "ethernetMgmt": ethernetMgmt,
       "ethernetFlowControl": ethernetFlowControl,
       "commitEthernetSettings": commitEthernetSettings,
       "locETHAlarms": locETHAlarms,
       "locEthAlarmsEntry": locEthAlarmsEntry,
       "locEthAlarm": locEthAlarm,
       "remETHAlarms": remETHAlarms,
       "remEthAlarmsEntry": remEthAlarmsEntry,
       "remEthAlarm": remEthAlarm}
)
