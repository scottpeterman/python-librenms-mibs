# SNMP MIB module (CISCO-TCPOFFLOAD-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\cisco\CISCO-TCPOFFLOAD-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:27:38 2025
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

(cipCardDtrBrdIndex,
 cipCardEntryIndex,
 cipCardSubChannelIndex) = mibBuilder.importSymbols(
    "CISCO-CHANNEL-MIB",
    "cipCardDtrBrdIndex",
    "cipCardEntryIndex",
    "cipCardSubChannelIndex")

(ciscoMgmt,) = mibBuilder.importSymbols(
    "CISCO-SMI",
    "ciscoMgmt")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ciscoTcpOffloadMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31)
)
if mibBuilder.loadTexts:
    ciscoTcpOffloadMIB.setRevisions(
        ("1998-01-06 00:00",
         "1995-04-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TcpOffloadObjects_ObjectIdentity = ObjectIdentity
tcpOffloadObjects = _TcpOffloadObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1)
)
_CipCardOffloadConfig_ObjectIdentity = ObjectIdentity
cipCardOffloadConfig = _CipCardOffloadConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1)
)
_CipCardOffloadConfigTable_Object = MibTable
cipCardOffloadConfigTable = _CipCardOffloadConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cipCardOffloadConfigTable.setStatus("current")
_CipCardOffloadConfigEntry_Object = MibTableRow
cipCardOffloadConfigEntry = _CipCardOffloadConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1)
)
cipCardOffloadConfigEntry.setIndexNames(
    (0, "CISCO-CHANNEL-MIB", "cipCardEntryIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardDtrBrdIndex"),
    (0, "CISCO-CHANNEL-MIB", "cipCardSubChannelIndex"),
)
if mibBuilder.loadTexts:
    cipCardOffloadConfigEntry.setStatus("current")


class _CipCardOffloadConfigPath_Type(OctetString):
    """Custom type cipCardOffloadConfigPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CipCardOffloadConfigPath_Type.__name__ = "OctetString"
_CipCardOffloadConfigPath_Object = MibTableColumn
cipCardOffloadConfigPath = _CipCardOffloadConfigPath_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 1),
    _CipCardOffloadConfigPath_Type()
)
cipCardOffloadConfigPath.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigPath.setStatus("current")


class _CipCardOffloadConfigDevice_Type(OctetString):
    """Custom type cipCardOffloadConfigDevice based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_CipCardOffloadConfigDevice_Type.__name__ = "OctetString"
_CipCardOffloadConfigDevice_Object = MibTableColumn
cipCardOffloadConfigDevice = _CipCardOffloadConfigDevice_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 2),
    _CipCardOffloadConfigDevice_Type()
)
cipCardOffloadConfigDevice.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigDevice.setStatus("current")
_CipCardOffloadConfigIpAddr_Type = IpAddress
_CipCardOffloadConfigIpAddr_Object = MibTableColumn
cipCardOffloadConfigIpAddr = _CipCardOffloadConfigIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 3),
    _CipCardOffloadConfigIpAddr_Type()
)
cipCardOffloadConfigIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigIpAddr.setStatus("current")


class _CipCardOffloadConfigHostName_Type(DisplayString):
    """Custom type cipCardOffloadConfigHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigHostName_Type.__name__ = "DisplayString"
_CipCardOffloadConfigHostName_Object = MibTableColumn
cipCardOffloadConfigHostName = _CipCardOffloadConfigHostName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 4),
    _CipCardOffloadConfigHostName_Type()
)
cipCardOffloadConfigHostName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigHostName.setStatus("current")


class _CipCardOffloadConfigRouterName_Type(DisplayString):
    """Custom type cipCardOffloadConfigRouterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigRouterName_Type.__name__ = "DisplayString"
_CipCardOffloadConfigRouterName_Object = MibTableColumn
cipCardOffloadConfigRouterName = _CipCardOffloadConfigRouterName_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 5),
    _CipCardOffloadConfigRouterName_Type()
)
cipCardOffloadConfigRouterName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigRouterName.setStatus("current")


class _CipCardOffloadConfigLinkHostAppl_Type(DisplayString):
    """Custom type cipCardOffloadConfigLinkHostAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigLinkHostAppl_Type.__name__ = "DisplayString"
_CipCardOffloadConfigLinkHostAppl_Object = MibTableColumn
cipCardOffloadConfigLinkHostAppl = _CipCardOffloadConfigLinkHostAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 6),
    _CipCardOffloadConfigLinkHostAppl_Type()
)
cipCardOffloadConfigLinkHostAppl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigLinkHostAppl.setStatus("current")


class _CipCardOffloadConfigLinkRouterAppl_Type(DisplayString):
    """Custom type cipCardOffloadConfigLinkRouterAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigLinkRouterAppl_Type.__name__ = "DisplayString"
_CipCardOffloadConfigLinkRouterAppl_Object = MibTableColumn
cipCardOffloadConfigLinkRouterAppl = _CipCardOffloadConfigLinkRouterAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 7),
    _CipCardOffloadConfigLinkRouterAppl_Type()
)
cipCardOffloadConfigLinkRouterAppl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigLinkRouterAppl.setStatus("current")


class _CipCardOffloadConfigAPIHostAppl_Type(DisplayString):
    """Custom type cipCardOffloadConfigAPIHostAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigAPIHostAppl_Type.__name__ = "DisplayString"
_CipCardOffloadConfigAPIHostAppl_Object = MibTableColumn
cipCardOffloadConfigAPIHostAppl = _CipCardOffloadConfigAPIHostAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 8),
    _CipCardOffloadConfigAPIHostAppl_Type()
)
cipCardOffloadConfigAPIHostAppl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigAPIHostAppl.setStatus("current")


class _CipCardOffloadConfigAPIRouterAppl_Type(DisplayString):
    """Custom type cipCardOffloadConfigAPIRouterAppl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 10),
    )


_CipCardOffloadConfigAPIRouterAppl_Type.__name__ = "DisplayString"
_CipCardOffloadConfigAPIRouterAppl_Object = MibTableColumn
cipCardOffloadConfigAPIRouterAppl = _CipCardOffloadConfigAPIRouterAppl_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 9),
    _CipCardOffloadConfigAPIRouterAppl_Type()
)
cipCardOffloadConfigAPIRouterAppl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigAPIRouterAppl.setStatus("current")
_CipCardOffloadConfigBroadcastEnable_Type = TruthValue
_CipCardOffloadConfigBroadcastEnable_Object = MibTableColumn
cipCardOffloadConfigBroadcastEnable = _CipCardOffloadConfigBroadcastEnable_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 10),
    _CipCardOffloadConfigBroadcastEnable_Type()
)
cipCardOffloadConfigBroadcastEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigBroadcastEnable.setStatus("current")
_CipCardOffloadConfigRowStatus_Type = RowStatus
_CipCardOffloadConfigRowStatus_Object = MibTableColumn
cipCardOffloadConfigRowStatus = _CipCardOffloadConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 1, 1, 1, 1, 11),
    _CipCardOffloadConfigRowStatus_Type()
)
cipCardOffloadConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cipCardOffloadConfigRowStatus.setStatus("current")
_CiscoTcpOffloadMibConformance_ObjectIdentity = ObjectIdentity
ciscoTcpOffloadMibConformance = _CiscoTcpOffloadMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2)
)
_CiscoTcpOffloadMibCompliances_ObjectIdentity = ObjectIdentity
ciscoTcpOffloadMibCompliances = _CiscoTcpOffloadMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2, 1)
)
_CiscoTcpOffloadMibGroups_ObjectIdentity = ObjectIdentity
ciscoTcpOffloadMibGroups = _CiscoTcpOffloadMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2, 2)
)

# Managed Objects groups

ciscoTcpOffloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2, 2, 1)
)
ciscoTcpOffloadGroup.setObjects(
      *(("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigPath"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigDevice"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigIpAddr"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigHostName"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigRouterName"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigLinkHostAppl"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigLinkRouterAppl"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigAPIHostAppl"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigAPIRouterAppl"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigBroadcastEnable"),
        ("CISCO-TCPOFFLOAD-MIB", "cipCardOffloadConfigRowStatus"))
)
if mibBuilder.loadTexts:
    ciscoTcpOffloadGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ciscoTcpOffloadMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9, 9, 31, 2, 1, 1)
)
ciscoTcpOffloadMibCompliance.setObjects(
    ("CISCO-TCPOFFLOAD-MIB", "ciscoTcpOffloadGroup")
)
if mibBuilder.loadTexts:
    ciscoTcpOffloadMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCO-TCPOFFLOAD-MIB",
    **{"ciscoTcpOffloadMIB": ciscoTcpOffloadMIB,
       "tcpOffloadObjects": tcpOffloadObjects,
       "cipCardOffloadConfig": cipCardOffloadConfig,
       "cipCardOffloadConfigTable": cipCardOffloadConfigTable,
       "cipCardOffloadConfigEntry": cipCardOffloadConfigEntry,
       "cipCardOffloadConfigPath": cipCardOffloadConfigPath,
       "cipCardOffloadConfigDevice": cipCardOffloadConfigDevice,
       "cipCardOffloadConfigIpAddr": cipCardOffloadConfigIpAddr,
       "cipCardOffloadConfigHostName": cipCardOffloadConfigHostName,
       "cipCardOffloadConfigRouterName": cipCardOffloadConfigRouterName,
       "cipCardOffloadConfigLinkHostAppl": cipCardOffloadConfigLinkHostAppl,
       "cipCardOffloadConfigLinkRouterAppl": cipCardOffloadConfigLinkRouterAppl,
       "cipCardOffloadConfigAPIHostAppl": cipCardOffloadConfigAPIHostAppl,
       "cipCardOffloadConfigAPIRouterAppl": cipCardOffloadConfigAPIRouterAppl,
       "cipCardOffloadConfigBroadcastEnable": cipCardOffloadConfigBroadcastEnable,
       "cipCardOffloadConfigRowStatus": cipCardOffloadConfigRowStatus,
       "ciscoTcpOffloadMibConformance": ciscoTcpOffloadMibConformance,
       "ciscoTcpOffloadMibCompliances": ciscoTcpOffloadMibCompliances,
       "ciscoTcpOffloadMibCompliance": ciscoTcpOffloadMibCompliance,
       "ciscoTcpOffloadMibGroups": ciscoTcpOffloadMibGroups,
       "ciscoTcpOffloadGroup": ciscoTcpOffloadGroup}
)
