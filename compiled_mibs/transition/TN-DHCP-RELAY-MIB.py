# SNMP MIB module (TN-DHCP-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DHCP-RELAY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:16 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnDhcpRelayMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148)
)
if mibBuilder.loadTexts:
    tnDhcpRelayMib.setRevisions(
        ("2015-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TNDhcpRelayInformationPolicyType(TextualConvention, Integer32):
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
        *(("replace", 0),
          ("keep", 1),
          ("drop", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnDhcpRelayMibObjects_ObjectIdentity = ObjectIdentity
tnDhcpRelayMibObjects = _TnDhcpRelayMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1)
)
_TnDhcpRelayConfig_ObjectIdentity = ObjectIdentity
tnDhcpRelayConfig = _TnDhcpRelayConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 2)
)
_TnDhcpRelayConfigGlobals_ObjectIdentity = ObjectIdentity
tnDhcpRelayConfigGlobals = _TnDhcpRelayConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 2, 1)
)
_TnDhcpRelayConfigGlobalsMode_Type = TruthValue
_TnDhcpRelayConfigGlobalsMode_Object = MibScalar
tnDhcpRelayConfigGlobalsMode = _TnDhcpRelayConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 2, 1, 1),
    _TnDhcpRelayConfigGlobalsMode_Type()
)
tnDhcpRelayConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayConfigGlobalsMode.setStatus("current")
_TnDhcpRelayConfigGlobalsServerIpAddress_Type = IpAddress
_TnDhcpRelayConfigGlobalsServerIpAddress_Object = MibScalar
tnDhcpRelayConfigGlobalsServerIpAddress = _TnDhcpRelayConfigGlobalsServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 2, 1, 2),
    _TnDhcpRelayConfigGlobalsServerIpAddress_Type()
)
tnDhcpRelayConfigGlobalsServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayConfigGlobalsServerIpAddress.setStatus("current")
_TnDhcpRelayConfigGlobalsInformationMode_Type = TruthValue
_TnDhcpRelayConfigGlobalsInformationMode_Object = MibScalar
tnDhcpRelayConfigGlobalsInformationMode = _TnDhcpRelayConfigGlobalsInformationMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 2, 1, 3),
    _TnDhcpRelayConfigGlobalsInformationMode_Type()
)
tnDhcpRelayConfigGlobalsInformationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayConfigGlobalsInformationMode.setStatus("current")
_TnDhcpRelayConfigGlobalsInformationPolicy_Type = TNDhcpRelayInformationPolicyType
_TnDhcpRelayConfigGlobalsInformationPolicy_Object = MibScalar
tnDhcpRelayConfigGlobalsInformationPolicy = _TnDhcpRelayConfigGlobalsInformationPolicy_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 2, 1, 4),
    _TnDhcpRelayConfigGlobalsInformationPolicy_Type()
)
tnDhcpRelayConfigGlobalsInformationPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayConfigGlobalsInformationPolicy.setStatus("current")
_TnDhcpRelayStatus_ObjectIdentity = ObjectIdentity
tnDhcpRelayStatus = _TnDhcpRelayStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3)
)
_TnDhcpRelayStatusStatistics_ObjectIdentity = ObjectIdentity
tnDhcpRelayStatusStatistics = _TnDhcpRelayStatusStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1)
)
_TnDhcpRelayStatusStatisticsServerPacketsRelayed_Type = Unsigned32
_TnDhcpRelayStatusStatisticsServerPacketsRelayed_Object = MibScalar
tnDhcpRelayStatusStatisticsServerPacketsRelayed = _TnDhcpRelayStatusStatisticsServerPacketsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 1),
    _TnDhcpRelayStatusStatisticsServerPacketsRelayed_Type()
)
tnDhcpRelayStatusStatisticsServerPacketsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsServerPacketsRelayed.setStatus("current")
_TnDhcpRelayStatusStatisticsServerPacketErrors_Type = Unsigned32
_TnDhcpRelayStatusStatisticsServerPacketErrors_Object = MibScalar
tnDhcpRelayStatusStatisticsServerPacketErrors = _TnDhcpRelayStatusStatisticsServerPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 2),
    _TnDhcpRelayStatusStatisticsServerPacketErrors_Type()
)
tnDhcpRelayStatusStatisticsServerPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsServerPacketErrors.setStatus("current")
_TnDhcpRelayStatusStatisticsClientPacketsRelayed_Type = Unsigned32
_TnDhcpRelayStatusStatisticsClientPacketsRelayed_Object = MibScalar
tnDhcpRelayStatusStatisticsClientPacketsRelayed = _TnDhcpRelayStatusStatisticsClientPacketsRelayed_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 3),
    _TnDhcpRelayStatusStatisticsClientPacketsRelayed_Type()
)
tnDhcpRelayStatusStatisticsClientPacketsRelayed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsClientPacketsRelayed.setStatus("current")
_TnDhcpRelayStatusStatisticsClientPacketErrors_Type = Unsigned32
_TnDhcpRelayStatusStatisticsClientPacketErrors_Object = MibScalar
tnDhcpRelayStatusStatisticsClientPacketErrors = _TnDhcpRelayStatusStatisticsClientPacketErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 4),
    _TnDhcpRelayStatusStatisticsClientPacketErrors_Type()
)
tnDhcpRelayStatusStatisticsClientPacketErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsClientPacketErrors.setStatus("current")
_TnDhcpRelayStatusStatisticsAgentOptionErrors_Type = Unsigned32
_TnDhcpRelayStatusStatisticsAgentOptionErrors_Object = MibScalar
tnDhcpRelayStatusStatisticsAgentOptionErrors = _TnDhcpRelayStatusStatisticsAgentOptionErrors_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 5),
    _TnDhcpRelayStatusStatisticsAgentOptionErrors_Type()
)
tnDhcpRelayStatusStatisticsAgentOptionErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsAgentOptionErrors.setStatus("current")
_TnDhcpRelayStatusStatisticsMissingAgentOption_Type = Unsigned32
_TnDhcpRelayStatusStatisticsMissingAgentOption_Object = MibScalar
tnDhcpRelayStatusStatisticsMissingAgentOption = _TnDhcpRelayStatusStatisticsMissingAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 6),
    _TnDhcpRelayStatusStatisticsMissingAgentOption_Type()
)
tnDhcpRelayStatusStatisticsMissingAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsMissingAgentOption.setStatus("current")
_TnDhcpRelayStatusStatisticsBadCircuitId_Type = Unsigned32
_TnDhcpRelayStatusStatisticsBadCircuitId_Object = MibScalar
tnDhcpRelayStatusStatisticsBadCircuitId = _TnDhcpRelayStatusStatisticsBadCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 7),
    _TnDhcpRelayStatusStatisticsBadCircuitId_Type()
)
tnDhcpRelayStatusStatisticsBadCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsBadCircuitId.setStatus("current")
_TnDhcpRelayStatusStatisticsMissingCircuitId_Type = Unsigned32
_TnDhcpRelayStatusStatisticsMissingCircuitId_Object = MibScalar
tnDhcpRelayStatusStatisticsMissingCircuitId = _TnDhcpRelayStatusStatisticsMissingCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 8),
    _TnDhcpRelayStatusStatisticsMissingCircuitId_Type()
)
tnDhcpRelayStatusStatisticsMissingCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsMissingCircuitId.setStatus("current")
_TnDhcpRelayStatusStatisticsBadRemoteId_Type = Unsigned32
_TnDhcpRelayStatusStatisticsBadRemoteId_Object = MibScalar
tnDhcpRelayStatusStatisticsBadRemoteId = _TnDhcpRelayStatusStatisticsBadRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 9),
    _TnDhcpRelayStatusStatisticsBadRemoteId_Type()
)
tnDhcpRelayStatusStatisticsBadRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsBadRemoteId.setStatus("current")
_TnDhcpRelayStatusStatisticsMissingRemoteId_Type = Unsigned32
_TnDhcpRelayStatusStatisticsMissingRemoteId_Object = MibScalar
tnDhcpRelayStatusStatisticsMissingRemoteId = _TnDhcpRelayStatusStatisticsMissingRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 10),
    _TnDhcpRelayStatusStatisticsMissingRemoteId_Type()
)
tnDhcpRelayStatusStatisticsMissingRemoteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsMissingRemoteId.setStatus("current")
_TnDhcpRelayStatusStatisticsReceiveServerPackets_Type = Unsigned32
_TnDhcpRelayStatusStatisticsReceiveServerPackets_Object = MibScalar
tnDhcpRelayStatusStatisticsReceiveServerPackets = _TnDhcpRelayStatusStatisticsReceiveServerPackets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 11),
    _TnDhcpRelayStatusStatisticsReceiveServerPackets_Type()
)
tnDhcpRelayStatusStatisticsReceiveServerPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsReceiveServerPackets.setStatus("current")
_TnDhcpRelayStatusStatisticsReceiveClientPackets_Type = Unsigned32
_TnDhcpRelayStatusStatisticsReceiveClientPackets_Object = MibScalar
tnDhcpRelayStatusStatisticsReceiveClientPackets = _TnDhcpRelayStatusStatisticsReceiveClientPackets_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 12),
    _TnDhcpRelayStatusStatisticsReceiveClientPackets_Type()
)
tnDhcpRelayStatusStatisticsReceiveClientPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsReceiveClientPackets.setStatus("current")
_TnDhcpRelayStatusStatisticsReceiveClientAgentOption_Type = Unsigned32
_TnDhcpRelayStatusStatisticsReceiveClientAgentOption_Object = MibScalar
tnDhcpRelayStatusStatisticsReceiveClientAgentOption = _TnDhcpRelayStatusStatisticsReceiveClientAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 13),
    _TnDhcpRelayStatusStatisticsReceiveClientAgentOption_Type()
)
tnDhcpRelayStatusStatisticsReceiveClientAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsReceiveClientAgentOption.setStatus("current")
_TnDhcpRelayStatusStatisticsReplaceAgentOption_Type = Unsigned32
_TnDhcpRelayStatusStatisticsReplaceAgentOption_Object = MibScalar
tnDhcpRelayStatusStatisticsReplaceAgentOption = _TnDhcpRelayStatusStatisticsReplaceAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 14),
    _TnDhcpRelayStatusStatisticsReplaceAgentOption_Type()
)
tnDhcpRelayStatusStatisticsReplaceAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsReplaceAgentOption.setStatus("current")
_TnDhcpRelayStatusStatisticsKeepAgentOption_Type = Unsigned32
_TnDhcpRelayStatusStatisticsKeepAgentOption_Object = MibScalar
tnDhcpRelayStatusStatisticsKeepAgentOption = _TnDhcpRelayStatusStatisticsKeepAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 15),
    _TnDhcpRelayStatusStatisticsKeepAgentOption_Type()
)
tnDhcpRelayStatusStatisticsKeepAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsKeepAgentOption.setStatus("current")
_TnDhcpRelayStatusStatisticsDropAgentOption_Type = Unsigned32
_TnDhcpRelayStatusStatisticsDropAgentOption_Object = MibScalar
tnDhcpRelayStatusStatisticsDropAgentOption = _TnDhcpRelayStatusStatisticsDropAgentOption_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 3, 1, 16),
    _TnDhcpRelayStatusStatisticsDropAgentOption_Type()
)
tnDhcpRelayStatusStatisticsDropAgentOption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsDropAgentOption.setStatus("current")
_TnDhcpRelayControl_ObjectIdentity = ObjectIdentity
tnDhcpRelayControl = _TnDhcpRelayControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 4)
)
_TnDhcpRelayControlClearStatistics_Type = TruthValue
_TnDhcpRelayControlClearStatistics_Object = MibScalar
tnDhcpRelayControlClearStatistics = _TnDhcpRelayControlClearStatistics_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 1, 4, 1),
    _TnDhcpRelayControlClearStatistics_Type()
)
tnDhcpRelayControlClearStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpRelayControlClearStatistics.setStatus("current")
_TnDhcpRelayMibConformance_ObjectIdentity = ObjectIdentity
tnDhcpRelayMibConformance = _TnDhcpRelayMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 2)
)
_TnDhcpRelayMibCompliances_ObjectIdentity = ObjectIdentity
tnDhcpRelayMibCompliances = _TnDhcpRelayMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 2, 1)
)
_TnDhcpRelayMibGroups_ObjectIdentity = ObjectIdentity
tnDhcpRelayMibGroups = _TnDhcpRelayMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 2, 2)
)

# Managed Objects groups

tnDhcpRelayConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 2, 2, 1)
)
tnDhcpRelayConfigGlobalsInfoGroup.setObjects(
      *(("TN-DHCP-RELAY-MIB", "tnDhcpRelayConfigGlobalsMode"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayConfigGlobalsServerIpAddress"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayConfigGlobalsInformationMode"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayConfigGlobalsInformationPolicy"))
)
if mibBuilder.loadTexts:
    tnDhcpRelayConfigGlobalsInfoGroup.setStatus("current")

tnDhcpRelayStatusStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 2, 2, 2)
)
tnDhcpRelayStatusStatisticsInfoGroup.setObjects(
      *(("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsServerPacketsRelayed"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsServerPacketErrors"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsClientPacketsRelayed"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsClientPacketErrors"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsAgentOptionErrors"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsMissingAgentOption"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsBadCircuitId"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsMissingCircuitId"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsBadRemoteId"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsMissingRemoteId"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsReceiveServerPackets"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsReceiveClientPackets"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsReceiveClientAgentOption"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsReplaceAgentOption"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsKeepAgentOption"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsDropAgentOption"))
)
if mibBuilder.loadTexts:
    tnDhcpRelayStatusStatisticsInfoGroup.setStatus("current")

tnDhcpRelayControlInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 2, 2, 3)
)
tnDhcpRelayControlInfoGroup.setObjects(
    ("TN-DHCP-RELAY-MIB", "tnDhcpRelayControlClearStatistics")
)
if mibBuilder.loadTexts:
    tnDhcpRelayControlInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnDhcpRelayMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 148, 2, 1, 1)
)
tnDhcpRelayMibCompliance.setObjects(
      *(("TN-DHCP-RELAY-MIB", "tnDhcpRelayConfigGlobalsInfoGroup"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayStatusStatisticsInfoGroup"),
        ("TN-DHCP-RELAY-MIB", "tnDhcpRelayControlInfoGroup"))
)
if mibBuilder.loadTexts:
    tnDhcpRelayMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DHCP-RELAY-MIB",
    **{"TNDhcpRelayInformationPolicyType": TNDhcpRelayInformationPolicyType,
       "tnDhcpRelayMib": tnDhcpRelayMib,
       "tnDhcpRelayMibObjects": tnDhcpRelayMibObjects,
       "tnDhcpRelayConfig": tnDhcpRelayConfig,
       "tnDhcpRelayConfigGlobals": tnDhcpRelayConfigGlobals,
       "tnDhcpRelayConfigGlobalsMode": tnDhcpRelayConfigGlobalsMode,
       "tnDhcpRelayConfigGlobalsServerIpAddress": tnDhcpRelayConfigGlobalsServerIpAddress,
       "tnDhcpRelayConfigGlobalsInformationMode": tnDhcpRelayConfigGlobalsInformationMode,
       "tnDhcpRelayConfigGlobalsInformationPolicy": tnDhcpRelayConfigGlobalsInformationPolicy,
       "tnDhcpRelayStatus": tnDhcpRelayStatus,
       "tnDhcpRelayStatusStatistics": tnDhcpRelayStatusStatistics,
       "tnDhcpRelayStatusStatisticsServerPacketsRelayed": tnDhcpRelayStatusStatisticsServerPacketsRelayed,
       "tnDhcpRelayStatusStatisticsServerPacketErrors": tnDhcpRelayStatusStatisticsServerPacketErrors,
       "tnDhcpRelayStatusStatisticsClientPacketsRelayed": tnDhcpRelayStatusStatisticsClientPacketsRelayed,
       "tnDhcpRelayStatusStatisticsClientPacketErrors": tnDhcpRelayStatusStatisticsClientPacketErrors,
       "tnDhcpRelayStatusStatisticsAgentOptionErrors": tnDhcpRelayStatusStatisticsAgentOptionErrors,
       "tnDhcpRelayStatusStatisticsMissingAgentOption": tnDhcpRelayStatusStatisticsMissingAgentOption,
       "tnDhcpRelayStatusStatisticsBadCircuitId": tnDhcpRelayStatusStatisticsBadCircuitId,
       "tnDhcpRelayStatusStatisticsMissingCircuitId": tnDhcpRelayStatusStatisticsMissingCircuitId,
       "tnDhcpRelayStatusStatisticsBadRemoteId": tnDhcpRelayStatusStatisticsBadRemoteId,
       "tnDhcpRelayStatusStatisticsMissingRemoteId": tnDhcpRelayStatusStatisticsMissingRemoteId,
       "tnDhcpRelayStatusStatisticsReceiveServerPackets": tnDhcpRelayStatusStatisticsReceiveServerPackets,
       "tnDhcpRelayStatusStatisticsReceiveClientPackets": tnDhcpRelayStatusStatisticsReceiveClientPackets,
       "tnDhcpRelayStatusStatisticsReceiveClientAgentOption": tnDhcpRelayStatusStatisticsReceiveClientAgentOption,
       "tnDhcpRelayStatusStatisticsReplaceAgentOption": tnDhcpRelayStatusStatisticsReplaceAgentOption,
       "tnDhcpRelayStatusStatisticsKeepAgentOption": tnDhcpRelayStatusStatisticsKeepAgentOption,
       "tnDhcpRelayStatusStatisticsDropAgentOption": tnDhcpRelayStatusStatisticsDropAgentOption,
       "tnDhcpRelayControl": tnDhcpRelayControl,
       "tnDhcpRelayControlClearStatistics": tnDhcpRelayControlClearStatistics,
       "tnDhcpRelayMibConformance": tnDhcpRelayMibConformance,
       "tnDhcpRelayMibCompliances": tnDhcpRelayMibCompliances,
       "tnDhcpRelayMibCompliance": tnDhcpRelayMibCompliance,
       "tnDhcpRelayMibGroups": tnDhcpRelayMibGroups,
       "tnDhcpRelayConfigGlobalsInfoGroup": tnDhcpRelayConfigGlobalsInfoGroup,
       "tnDhcpRelayStatusStatisticsInfoGroup": tnDhcpRelayStatusStatisticsInfoGroup,
       "tnDhcpRelayControlInfoGroup": tnDhcpRelayControlInfoGroup}
)
