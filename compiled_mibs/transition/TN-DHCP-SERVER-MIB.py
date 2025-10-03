# SNMP MIB module (TN-DHCP-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\transition\TN-DHCP-SERVER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:31:17 2025
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
 MacAddress,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(TNDisplayString,
 TNInterfaceIndex,
 TNRowEditorState,
 TNUnsigned16) = mibBuilder.importSymbols(
    "TN-TC",
    "TNDisplayString",
    "TNInterfaceIndex",
    "TNRowEditorState",
    "TNUnsigned16")

(tnProducts,) = mibBuilder.importSymbols(
    "TRANSITION-SMI",
    "tnProducts")


# MODULE-IDENTITY

tnDhcpServerMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146)
)
if mibBuilder.loadTexts:
    tnDhcpServerMib.setRevisions(
        ("2015-04-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TNDhcpServerBindingEnum(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("automatic", 1),
          ("manual", 2),
          ("expired", 3))
    )



class TNDhcpServerBindingStateEnum(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("allocated", 1),
          ("committed", 2),
          ("expired", 3))
    )



class TNDhcpServerClientIdentifierEnum(TextualConvention, Integer32):
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
        *(("none", 0),
          ("fqdn", 1),
          ("mac", 2))
    )



class TNDhcpServerNetbiosNodeEnum(TextualConvention, Integer32):
    status = "current"
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
        *(("nodeNone", 0),
          ("nodeB", 1),
          ("nodeP", 2),
          ("nodeM", 3),
          ("nodeH", 4))
    )



class TNDhcpServerPoolEnum(TextualConvention, Integer32):
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
        *(("none", 0),
          ("network", 1),
          ("host", 2))
    )



# MIB Managed Objects in the order of their OIDs

_TnDhcpServerMibObjects_ObjectIdentity = ObjectIdentity
tnDhcpServerMibObjects = _TnDhcpServerMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1)
)
_TnDhcpServerConfig_ObjectIdentity = ObjectIdentity
tnDhcpServerConfig = _TnDhcpServerConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2)
)
_TnDhcpServerConfigGlobals_ObjectIdentity = ObjectIdentity
tnDhcpServerConfigGlobals = _TnDhcpServerConfigGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 1)
)
_TnDhcpServerConfigGlobalsMode_Type = TruthValue
_TnDhcpServerConfigGlobalsMode_Object = MibScalar
tnDhcpServerConfigGlobalsMode = _TnDhcpServerConfigGlobalsMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 1, 1),
    _TnDhcpServerConfigGlobalsMode_Type()
)
tnDhcpServerConfigGlobalsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigGlobalsMode.setStatus("current")
_TnDhcpServerConfigVlanTable_Object = MibTable
tnDhcpServerConfigVlanTable = _TnDhcpServerConfigVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 2)
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigVlanTable.setStatus("current")
_TnDhcpServerConfigVlanEntry_Object = MibTableRow
tnDhcpServerConfigVlanEntry = _TnDhcpServerConfigVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 2, 1)
)
tnDhcpServerConfigVlanEntry.setIndexNames(
    (0, "TN-DHCP-SERVER-MIB", "tnDhcpServerConfigVlanIfIndex"),
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigVlanEntry.setStatus("current")
_TnDhcpServerConfigVlanIfIndex_Type = TNInterfaceIndex
_TnDhcpServerConfigVlanIfIndex_Object = MibTableColumn
tnDhcpServerConfigVlanIfIndex = _TnDhcpServerConfigVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 2, 1, 1),
    _TnDhcpServerConfigVlanIfIndex_Type()
)
tnDhcpServerConfigVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpServerConfigVlanIfIndex.setStatus("current")
_TnDhcpServerConfigVlanMode_Type = TruthValue
_TnDhcpServerConfigVlanMode_Object = MibTableColumn
tnDhcpServerConfigVlanMode = _TnDhcpServerConfigVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 2, 1, 2),
    _TnDhcpServerConfigVlanMode_Type()
)
tnDhcpServerConfigVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigVlanMode.setStatus("current")
_TnDhcpServerConfigExcludedTable_Object = MibTable
tnDhcpServerConfigExcludedTable = _TnDhcpServerConfigExcludedTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 3)
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedTable.setStatus("current")
_TnDhcpServerConfigExcludedEntry_Object = MibTableRow
tnDhcpServerConfigExcludedEntry = _TnDhcpServerConfigExcludedEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 3, 1)
)
tnDhcpServerConfigExcludedEntry.setIndexNames(
    (0, "TN-DHCP-SERVER-MIB", "tnDhcpServerConfigExcludedLowIpAddress"),
    (0, "TN-DHCP-SERVER-MIB", "tnDhcpServerConfigExcludedHighIpAddress"),
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedEntry.setStatus("current")
_TnDhcpServerConfigExcludedLowIpAddress_Type = IpAddress
_TnDhcpServerConfigExcludedLowIpAddress_Object = MibTableColumn
tnDhcpServerConfigExcludedLowIpAddress = _TnDhcpServerConfigExcludedLowIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 3, 1, 1),
    _TnDhcpServerConfigExcludedLowIpAddress_Type()
)
tnDhcpServerConfigExcludedLowIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedLowIpAddress.setStatus("current")
_TnDhcpServerConfigExcludedHighIpAddress_Type = IpAddress
_TnDhcpServerConfigExcludedHighIpAddress_Object = MibTableColumn
tnDhcpServerConfigExcludedHighIpAddress = _TnDhcpServerConfigExcludedHighIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 3, 1, 2),
    _TnDhcpServerConfigExcludedHighIpAddress_Type()
)
tnDhcpServerConfigExcludedHighIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedHighIpAddress.setStatus("current")
_TnDhcpServerConfigExcludedAction_Type = TNRowEditorState
_TnDhcpServerConfigExcludedAction_Object = MibTableColumn
tnDhcpServerConfigExcludedAction = _TnDhcpServerConfigExcludedAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 3, 1, 100),
    _TnDhcpServerConfigExcludedAction_Type()
)
tnDhcpServerConfigExcludedAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedAction.setStatus("current")
_TnDhcpServerConfigExcludedIpTableRowEditor_ObjectIdentity = ObjectIdentity
tnDhcpServerConfigExcludedIpTableRowEditor = _TnDhcpServerConfigExcludedIpTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 4)
)
_TnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Type = IpAddress
_TnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Object = MibScalar
tnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress = _TnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 4, 1),
    _TnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress_Type()
)
tnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress.setStatus("current")
_TnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Type = IpAddress
_TnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Object = MibScalar
tnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress = _TnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 4, 2),
    _TnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress_Type()
)
tnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress.setStatus("current")
_TnDhcpServerConfigExcludedIpTableRowEditorAction_Type = TNRowEditorState
_TnDhcpServerConfigExcludedIpTableRowEditorAction_Object = MibScalar
tnDhcpServerConfigExcludedIpTableRowEditorAction = _TnDhcpServerConfigExcludedIpTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 4, 100),
    _TnDhcpServerConfigExcludedIpTableRowEditorAction_Type()
)
tnDhcpServerConfigExcludedIpTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedIpTableRowEditorAction.setStatus("current")
_TnDhcpServerConfigPoolTable_Object = MibTable
tnDhcpServerConfigPoolTable = _TnDhcpServerConfigPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5)
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTable.setStatus("current")
_TnDhcpServerConfigPoolEntry_Object = MibTableRow
tnDhcpServerConfigPoolEntry = _TnDhcpServerConfigPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1)
)
tnDhcpServerConfigPoolEntry.setIndexNames(
    (0, "TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolPoolName"),
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolEntry.setStatus("current")


class _TnDhcpServerConfigPoolPoolName_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolPoolName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolPoolName_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolPoolName_Object = MibTableColumn
tnDhcpServerConfigPoolPoolName = _TnDhcpServerConfigPoolPoolName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 1),
    _TnDhcpServerConfigPoolPoolName_Type()
)
tnDhcpServerConfigPoolPoolName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolPoolName.setStatus("current")
_TnDhcpServerConfigPoolPoolType_Type = TNDhcpServerPoolEnum
_TnDhcpServerConfigPoolPoolType_Object = MibTableColumn
tnDhcpServerConfigPoolPoolType = _TnDhcpServerConfigPoolPoolType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 2),
    _TnDhcpServerConfigPoolPoolType_Type()
)
tnDhcpServerConfigPoolPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolPoolType.setStatus("current")
_TnDhcpServerConfigPoolIpv4Address_Type = IpAddress
_TnDhcpServerConfigPoolIpv4Address_Object = MibTableColumn
tnDhcpServerConfigPoolIpv4Address = _TnDhcpServerConfigPoolIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 3),
    _TnDhcpServerConfigPoolIpv4Address_Type()
)
tnDhcpServerConfigPoolIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolIpv4Address.setStatus("current")
_TnDhcpServerConfigPoolSubnetMask_Type = IpAddress
_TnDhcpServerConfigPoolSubnetMask_Object = MibTableColumn
tnDhcpServerConfigPoolSubnetMask = _TnDhcpServerConfigPoolSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 4),
    _TnDhcpServerConfigPoolSubnetMask_Type()
)
tnDhcpServerConfigPoolSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolSubnetMask.setStatus("current")
_TnDhcpServerConfigPoolSubnetBroadcast_Type = IpAddress
_TnDhcpServerConfigPoolSubnetBroadcast_Object = MibTableColumn
tnDhcpServerConfigPoolSubnetBroadcast = _TnDhcpServerConfigPoolSubnetBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 5),
    _TnDhcpServerConfigPoolSubnetBroadcast_Type()
)
tnDhcpServerConfigPoolSubnetBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolSubnetBroadcast.setStatus("current")
_TnDhcpServerConfigPoolLeaseDay_Type = Unsigned32
_TnDhcpServerConfigPoolLeaseDay_Object = MibTableColumn
tnDhcpServerConfigPoolLeaseDay = _TnDhcpServerConfigPoolLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 6),
    _TnDhcpServerConfigPoolLeaseDay_Type()
)
tnDhcpServerConfigPoolLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolLeaseDay.setStatus("current")
_TnDhcpServerConfigPoolLeaseHour_Type = Unsigned32
_TnDhcpServerConfigPoolLeaseHour_Object = MibTableColumn
tnDhcpServerConfigPoolLeaseHour = _TnDhcpServerConfigPoolLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 7),
    _TnDhcpServerConfigPoolLeaseHour_Type()
)
tnDhcpServerConfigPoolLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolLeaseHour.setStatus("current")
_TnDhcpServerConfigPoolLeaseMinute_Type = Unsigned32
_TnDhcpServerConfigPoolLeaseMinute_Object = MibTableColumn
tnDhcpServerConfigPoolLeaseMinute = _TnDhcpServerConfigPoolLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 8),
    _TnDhcpServerConfigPoolLeaseMinute_Type()
)
tnDhcpServerConfigPoolLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolLeaseMinute.setStatus("current")


class _TnDhcpServerConfigPoolDomainName_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolDomainName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolDomainName_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolDomainName_Object = MibTableColumn
tnDhcpServerConfigPoolDomainName = _TnDhcpServerConfigPoolDomainName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 9),
    _TnDhcpServerConfigPoolDomainName_Type()
)
tnDhcpServerConfigPoolDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolDomainName.setStatus("current")
_TnDhcpServerConfigPoolDefaultRouter1_Type = IpAddress
_TnDhcpServerConfigPoolDefaultRouter1_Object = MibTableColumn
tnDhcpServerConfigPoolDefaultRouter1 = _TnDhcpServerConfigPoolDefaultRouter1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 10),
    _TnDhcpServerConfigPoolDefaultRouter1_Type()
)
tnDhcpServerConfigPoolDefaultRouter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolDefaultRouter1.setStatus("current")
_TnDhcpServerConfigPoolDefaultRouter2_Type = IpAddress
_TnDhcpServerConfigPoolDefaultRouter2_Object = MibTableColumn
tnDhcpServerConfigPoolDefaultRouter2 = _TnDhcpServerConfigPoolDefaultRouter2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 11),
    _TnDhcpServerConfigPoolDefaultRouter2_Type()
)
tnDhcpServerConfigPoolDefaultRouter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolDefaultRouter2.setStatus("current")
_TnDhcpServerConfigPoolDefaultRouter3_Type = IpAddress
_TnDhcpServerConfigPoolDefaultRouter3_Object = MibTableColumn
tnDhcpServerConfigPoolDefaultRouter3 = _TnDhcpServerConfigPoolDefaultRouter3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 12),
    _TnDhcpServerConfigPoolDefaultRouter3_Type()
)
tnDhcpServerConfigPoolDefaultRouter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolDefaultRouter3.setStatus("current")
_TnDhcpServerConfigPoolDefaultRouter4_Type = IpAddress
_TnDhcpServerConfigPoolDefaultRouter4_Object = MibTableColumn
tnDhcpServerConfigPoolDefaultRouter4 = _TnDhcpServerConfigPoolDefaultRouter4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 13),
    _TnDhcpServerConfigPoolDefaultRouter4_Type()
)
tnDhcpServerConfigPoolDefaultRouter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolDefaultRouter4.setStatus("current")
_TnDhcpServerConfigPoolDnsServer1_Type = IpAddress
_TnDhcpServerConfigPoolDnsServer1_Object = MibTableColumn
tnDhcpServerConfigPoolDnsServer1 = _TnDhcpServerConfigPoolDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 14),
    _TnDhcpServerConfigPoolDnsServer1_Type()
)
tnDhcpServerConfigPoolDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolDnsServer1.setStatus("current")
_TnDhcpServerConfigPoolDnsServer2_Type = IpAddress
_TnDhcpServerConfigPoolDnsServer2_Object = MibTableColumn
tnDhcpServerConfigPoolDnsServer2 = _TnDhcpServerConfigPoolDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 15),
    _TnDhcpServerConfigPoolDnsServer2_Type()
)
tnDhcpServerConfigPoolDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolDnsServer2.setStatus("current")
_TnDhcpServerConfigPoolDnsServer3_Type = IpAddress
_TnDhcpServerConfigPoolDnsServer3_Object = MibTableColumn
tnDhcpServerConfigPoolDnsServer3 = _TnDhcpServerConfigPoolDnsServer3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 16),
    _TnDhcpServerConfigPoolDnsServer3_Type()
)
tnDhcpServerConfigPoolDnsServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolDnsServer3.setStatus("current")
_TnDhcpServerConfigPoolDnsServer4_Type = IpAddress
_TnDhcpServerConfigPoolDnsServer4_Object = MibTableColumn
tnDhcpServerConfigPoolDnsServer4 = _TnDhcpServerConfigPoolDnsServer4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 17),
    _TnDhcpServerConfigPoolDnsServer4_Type()
)
tnDhcpServerConfigPoolDnsServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolDnsServer4.setStatus("current")
_TnDhcpServerConfigPoolNtpServer1_Type = IpAddress
_TnDhcpServerConfigPoolNtpServer1_Object = MibTableColumn
tnDhcpServerConfigPoolNtpServer1 = _TnDhcpServerConfigPoolNtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 18),
    _TnDhcpServerConfigPoolNtpServer1_Type()
)
tnDhcpServerConfigPoolNtpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNtpServer1.setStatus("current")
_TnDhcpServerConfigPoolNtpServer2_Type = IpAddress
_TnDhcpServerConfigPoolNtpServer2_Object = MibTableColumn
tnDhcpServerConfigPoolNtpServer2 = _TnDhcpServerConfigPoolNtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 19),
    _TnDhcpServerConfigPoolNtpServer2_Type()
)
tnDhcpServerConfigPoolNtpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNtpServer2.setStatus("current")
_TnDhcpServerConfigPoolNtpServer3_Type = IpAddress
_TnDhcpServerConfigPoolNtpServer3_Object = MibTableColumn
tnDhcpServerConfigPoolNtpServer3 = _TnDhcpServerConfigPoolNtpServer3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 20),
    _TnDhcpServerConfigPoolNtpServer3_Type()
)
tnDhcpServerConfigPoolNtpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNtpServer3.setStatus("current")
_TnDhcpServerConfigPoolNtpServer4_Type = IpAddress
_TnDhcpServerConfigPoolNtpServer4_Object = MibTableColumn
tnDhcpServerConfigPoolNtpServer4 = _TnDhcpServerConfigPoolNtpServer4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 21),
    _TnDhcpServerConfigPoolNtpServer4_Type()
)
tnDhcpServerConfigPoolNtpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNtpServer4.setStatus("current")
_TnDhcpServerConfigPoolNetbiosNodeType_Type = TNDhcpServerNetbiosNodeEnum
_TnDhcpServerConfigPoolNetbiosNodeType_Object = MibTableColumn
tnDhcpServerConfigPoolNetbiosNodeType = _TnDhcpServerConfigPoolNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 22),
    _TnDhcpServerConfigPoolNetbiosNodeType_Type()
)
tnDhcpServerConfigPoolNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNetbiosNodeType.setStatus("current")


class _TnDhcpServerConfigPoolNetbiosScope_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolNetbiosScope based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolNetbiosScope_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolNetbiosScope_Object = MibTableColumn
tnDhcpServerConfigPoolNetbiosScope = _TnDhcpServerConfigPoolNetbiosScope_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 23),
    _TnDhcpServerConfigPoolNetbiosScope_Type()
)
tnDhcpServerConfigPoolNetbiosScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNetbiosScope.setStatus("current")
_TnDhcpServerConfigPoolNetbiosNameServer1_Type = IpAddress
_TnDhcpServerConfigPoolNetbiosNameServer1_Object = MibTableColumn
tnDhcpServerConfigPoolNetbiosNameServer1 = _TnDhcpServerConfigPoolNetbiosNameServer1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 24),
    _TnDhcpServerConfigPoolNetbiosNameServer1_Type()
)
tnDhcpServerConfigPoolNetbiosNameServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNetbiosNameServer1.setStatus("current")
_TnDhcpServerConfigPoolNetbiosNameServer2_Type = IpAddress
_TnDhcpServerConfigPoolNetbiosNameServer2_Object = MibTableColumn
tnDhcpServerConfigPoolNetbiosNameServer2 = _TnDhcpServerConfigPoolNetbiosNameServer2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 25),
    _TnDhcpServerConfigPoolNetbiosNameServer2_Type()
)
tnDhcpServerConfigPoolNetbiosNameServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNetbiosNameServer2.setStatus("current")
_TnDhcpServerConfigPoolNetbiosNameServer3_Type = IpAddress
_TnDhcpServerConfigPoolNetbiosNameServer3_Object = MibTableColumn
tnDhcpServerConfigPoolNetbiosNameServer3 = _TnDhcpServerConfigPoolNetbiosNameServer3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 26),
    _TnDhcpServerConfigPoolNetbiosNameServer3_Type()
)
tnDhcpServerConfigPoolNetbiosNameServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNetbiosNameServer3.setStatus("current")
_TnDhcpServerConfigPoolNetbiosNameServer4_Type = IpAddress
_TnDhcpServerConfigPoolNetbiosNameServer4_Object = MibTableColumn
tnDhcpServerConfigPoolNetbiosNameServer4 = _TnDhcpServerConfigPoolNetbiosNameServer4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 27),
    _TnDhcpServerConfigPoolNetbiosNameServer4_Type()
)
tnDhcpServerConfigPoolNetbiosNameServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNetbiosNameServer4.setStatus("current")


class _TnDhcpServerConfigPoolNisDomainName_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolNisDomainName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolNisDomainName_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolNisDomainName_Object = MibTableColumn
tnDhcpServerConfigPoolNisDomainName = _TnDhcpServerConfigPoolNisDomainName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 28),
    _TnDhcpServerConfigPoolNisDomainName_Type()
)
tnDhcpServerConfigPoolNisDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNisDomainName.setStatus("current")
_TnDhcpServerConfigPoolNisServer1_Type = IpAddress
_TnDhcpServerConfigPoolNisServer1_Object = MibTableColumn
tnDhcpServerConfigPoolNisServer1 = _TnDhcpServerConfigPoolNisServer1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 29),
    _TnDhcpServerConfigPoolNisServer1_Type()
)
tnDhcpServerConfigPoolNisServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNisServer1.setStatus("current")
_TnDhcpServerConfigPoolNisServer2_Type = IpAddress
_TnDhcpServerConfigPoolNisServer2_Object = MibTableColumn
tnDhcpServerConfigPoolNisServer2 = _TnDhcpServerConfigPoolNisServer2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 30),
    _TnDhcpServerConfigPoolNisServer2_Type()
)
tnDhcpServerConfigPoolNisServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNisServer2.setStatus("current")
_TnDhcpServerConfigPoolNisServer3_Type = IpAddress
_TnDhcpServerConfigPoolNisServer3_Object = MibTableColumn
tnDhcpServerConfigPoolNisServer3 = _TnDhcpServerConfigPoolNisServer3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 31),
    _TnDhcpServerConfigPoolNisServer3_Type()
)
tnDhcpServerConfigPoolNisServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNisServer3.setStatus("current")
_TnDhcpServerConfigPoolNisServer4_Type = IpAddress
_TnDhcpServerConfigPoolNisServer4_Object = MibTableColumn
tnDhcpServerConfigPoolNisServer4 = _TnDhcpServerConfigPoolNisServer4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 32),
    _TnDhcpServerConfigPoolNisServer4_Type()
)
tnDhcpServerConfigPoolNisServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolNisServer4.setStatus("current")
_TnDhcpServerConfigPoolClientIdentifierType_Type = TNDhcpServerClientIdentifierEnum
_TnDhcpServerConfigPoolClientIdentifierType_Object = MibTableColumn
tnDhcpServerConfigPoolClientIdentifierType = _TnDhcpServerConfigPoolClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 33),
    _TnDhcpServerConfigPoolClientIdentifierType_Type()
)
tnDhcpServerConfigPoolClientIdentifierType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolClientIdentifierType.setStatus("current")


class _TnDhcpServerConfigPoolClientIdentifierFqdn_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolClientIdentifierFqdn based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolClientIdentifierFqdn_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolClientIdentifierFqdn_Object = MibTableColumn
tnDhcpServerConfigPoolClientIdentifierFqdn = _TnDhcpServerConfigPoolClientIdentifierFqdn_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 34),
    _TnDhcpServerConfigPoolClientIdentifierFqdn_Type()
)
tnDhcpServerConfigPoolClientIdentifierFqdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolClientIdentifierFqdn.setStatus("current")
_TnDhcpServerConfigPoolClientIdentifierMac_Type = MacAddress
_TnDhcpServerConfigPoolClientIdentifierMac_Object = MibTableColumn
tnDhcpServerConfigPoolClientIdentifierMac = _TnDhcpServerConfigPoolClientIdentifierMac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 35),
    _TnDhcpServerConfigPoolClientIdentifierMac_Type()
)
tnDhcpServerConfigPoolClientIdentifierMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolClientIdentifierMac.setStatus("current")
_TnDhcpServerConfigPoolClientHardwareAddress_Type = MacAddress
_TnDhcpServerConfigPoolClientHardwareAddress_Object = MibTableColumn
tnDhcpServerConfigPoolClientHardwareAddress = _TnDhcpServerConfigPoolClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 36),
    _TnDhcpServerConfigPoolClientHardwareAddress_Type()
)
tnDhcpServerConfigPoolClientHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolClientHardwareAddress.setStatus("current")


class _TnDhcpServerConfigPoolClientName_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolClientName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolClientName_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolClientName_Object = MibTableColumn
tnDhcpServerConfigPoolClientName = _TnDhcpServerConfigPoolClientName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 37),
    _TnDhcpServerConfigPoolClientName_Type()
)
tnDhcpServerConfigPoolClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolClientName.setStatus("current")


class _TnDhcpServerConfigPoolVendorClassId1_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolVendorClassId1 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolVendorClassId1_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolVendorClassId1_Object = MibTableColumn
tnDhcpServerConfigPoolVendorClassId1 = _TnDhcpServerConfigPoolVendorClassId1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 38),
    _TnDhcpServerConfigPoolVendorClassId1_Type()
)
tnDhcpServerConfigPoolVendorClassId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolVendorClassId1.setStatus("current")


class _TnDhcpServerConfigPoolVendorSpecificInfo1_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolVendorSpecificInfo1 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_TnDhcpServerConfigPoolVendorSpecificInfo1_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolVendorSpecificInfo1_Object = MibTableColumn
tnDhcpServerConfigPoolVendorSpecificInfo1 = _TnDhcpServerConfigPoolVendorSpecificInfo1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 39),
    _TnDhcpServerConfigPoolVendorSpecificInfo1_Type()
)
tnDhcpServerConfigPoolVendorSpecificInfo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolVendorSpecificInfo1.setStatus("current")


class _TnDhcpServerConfigPoolVendorClassId2_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolVendorClassId2 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolVendorClassId2_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolVendorClassId2_Object = MibTableColumn
tnDhcpServerConfigPoolVendorClassId2 = _TnDhcpServerConfigPoolVendorClassId2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 40),
    _TnDhcpServerConfigPoolVendorClassId2_Type()
)
tnDhcpServerConfigPoolVendorClassId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolVendorClassId2.setStatus("current")


class _TnDhcpServerConfigPoolVendorSpecificInfo2_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolVendorSpecificInfo2 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_TnDhcpServerConfigPoolVendorSpecificInfo2_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolVendorSpecificInfo2_Object = MibTableColumn
tnDhcpServerConfigPoolVendorSpecificInfo2 = _TnDhcpServerConfigPoolVendorSpecificInfo2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 41),
    _TnDhcpServerConfigPoolVendorSpecificInfo2_Type()
)
tnDhcpServerConfigPoolVendorSpecificInfo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolVendorSpecificInfo2.setStatus("current")


class _TnDhcpServerConfigPoolVendorClassId3_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolVendorClassId3 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolVendorClassId3_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolVendorClassId3_Object = MibTableColumn
tnDhcpServerConfigPoolVendorClassId3 = _TnDhcpServerConfigPoolVendorClassId3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 42),
    _TnDhcpServerConfigPoolVendorClassId3_Type()
)
tnDhcpServerConfigPoolVendorClassId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolVendorClassId3.setStatus("current")


class _TnDhcpServerConfigPoolVendorSpecificInfo3_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolVendorSpecificInfo3 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_TnDhcpServerConfigPoolVendorSpecificInfo3_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolVendorSpecificInfo3_Object = MibTableColumn
tnDhcpServerConfigPoolVendorSpecificInfo3 = _TnDhcpServerConfigPoolVendorSpecificInfo3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 43),
    _TnDhcpServerConfigPoolVendorSpecificInfo3_Type()
)
tnDhcpServerConfigPoolVendorSpecificInfo3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolVendorSpecificInfo3.setStatus("current")


class _TnDhcpServerConfigPoolVendorClassId4_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolVendorClassId4 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolVendorClassId4_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolVendorClassId4_Object = MibTableColumn
tnDhcpServerConfigPoolVendorClassId4 = _TnDhcpServerConfigPoolVendorClassId4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 44),
    _TnDhcpServerConfigPoolVendorClassId4_Type()
)
tnDhcpServerConfigPoolVendorClassId4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolVendorClassId4.setStatus("current")


class _TnDhcpServerConfigPoolVendorSpecificInfo4_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolVendorSpecificInfo4 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_TnDhcpServerConfigPoolVendorSpecificInfo4_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolVendorSpecificInfo4_Object = MibTableColumn
tnDhcpServerConfigPoolVendorSpecificInfo4 = _TnDhcpServerConfigPoolVendorSpecificInfo4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 45),
    _TnDhcpServerConfigPoolVendorSpecificInfo4_Type()
)
tnDhcpServerConfigPoolVendorSpecificInfo4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolVendorSpecificInfo4.setStatus("current")
_TnDhcpServerConfigPoolAction_Type = TNRowEditorState
_TnDhcpServerConfigPoolAction_Object = MibTableColumn
tnDhcpServerConfigPoolAction = _TnDhcpServerConfigPoolAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 5, 1, 100),
    _TnDhcpServerConfigPoolAction_Type()
)
tnDhcpServerConfigPoolAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolAction.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditor_ObjectIdentity = ObjectIdentity
tnDhcpServerConfigPoolTableRowEditor = _TnDhcpServerConfigPoolTableRowEditor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6)
)


class _TnDhcpServerConfigPoolTableRowEditorPoolName_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorPoolName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolTableRowEditorPoolName_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorPoolName_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorPoolName = _TnDhcpServerConfigPoolTableRowEditorPoolName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 1),
    _TnDhcpServerConfigPoolTableRowEditorPoolName_Type()
)
tnDhcpServerConfigPoolTableRowEditorPoolName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorPoolName.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorPoolType_Type = TNDhcpServerPoolEnum
_TnDhcpServerConfigPoolTableRowEditorPoolType_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorPoolType = _TnDhcpServerConfigPoolTableRowEditorPoolType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 2),
    _TnDhcpServerConfigPoolTableRowEditorPoolType_Type()
)
tnDhcpServerConfigPoolTableRowEditorPoolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorPoolType.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorIpv4Address_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorIpv4Address_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorIpv4Address = _TnDhcpServerConfigPoolTableRowEditorIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 3),
    _TnDhcpServerConfigPoolTableRowEditorIpv4Address_Type()
)
tnDhcpServerConfigPoolTableRowEditorIpv4Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorIpv4Address.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorSubnetMask_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorSubnetMask_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorSubnetMask = _TnDhcpServerConfigPoolTableRowEditorSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 4),
    _TnDhcpServerConfigPoolTableRowEditorSubnetMask_Type()
)
tnDhcpServerConfigPoolTableRowEditorSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorSubnetMask.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorSubnetBroadcast_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorSubnetBroadcast_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorSubnetBroadcast = _TnDhcpServerConfigPoolTableRowEditorSubnetBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 5),
    _TnDhcpServerConfigPoolTableRowEditorSubnetBroadcast_Type()
)
tnDhcpServerConfigPoolTableRowEditorSubnetBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorSubnetBroadcast.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorLeaseDay_Type = Unsigned32
_TnDhcpServerConfigPoolTableRowEditorLeaseDay_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorLeaseDay = _TnDhcpServerConfigPoolTableRowEditorLeaseDay_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 6),
    _TnDhcpServerConfigPoolTableRowEditorLeaseDay_Type()
)
tnDhcpServerConfigPoolTableRowEditorLeaseDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorLeaseDay.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorLeaseHour_Type = Unsigned32
_TnDhcpServerConfigPoolTableRowEditorLeaseHour_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorLeaseHour = _TnDhcpServerConfigPoolTableRowEditorLeaseHour_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 7),
    _TnDhcpServerConfigPoolTableRowEditorLeaseHour_Type()
)
tnDhcpServerConfigPoolTableRowEditorLeaseHour.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorLeaseHour.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorLeaseMinute_Type = Unsigned32
_TnDhcpServerConfigPoolTableRowEditorLeaseMinute_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorLeaseMinute = _TnDhcpServerConfigPoolTableRowEditorLeaseMinute_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 8),
    _TnDhcpServerConfigPoolTableRowEditorLeaseMinute_Type()
)
tnDhcpServerConfigPoolTableRowEditorLeaseMinute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorLeaseMinute.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorDomainName_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorDomainName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolTableRowEditorDomainName_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorDomainName_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorDomainName = _TnDhcpServerConfigPoolTableRowEditorDomainName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 9),
    _TnDhcpServerConfigPoolTableRowEditorDomainName_Type()
)
tnDhcpServerConfigPoolTableRowEditorDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorDomainName.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorDefaultRouter1_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorDefaultRouter1_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorDefaultRouter1 = _TnDhcpServerConfigPoolTableRowEditorDefaultRouter1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 10),
    _TnDhcpServerConfigPoolTableRowEditorDefaultRouter1_Type()
)
tnDhcpServerConfigPoolTableRowEditorDefaultRouter1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorDefaultRouter1.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorDefaultRouter2_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorDefaultRouter2_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorDefaultRouter2 = _TnDhcpServerConfigPoolTableRowEditorDefaultRouter2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 11),
    _TnDhcpServerConfigPoolTableRowEditorDefaultRouter2_Type()
)
tnDhcpServerConfigPoolTableRowEditorDefaultRouter2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorDefaultRouter2.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorDefaultRouter3_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorDefaultRouter3_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorDefaultRouter3 = _TnDhcpServerConfigPoolTableRowEditorDefaultRouter3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 12),
    _TnDhcpServerConfigPoolTableRowEditorDefaultRouter3_Type()
)
tnDhcpServerConfigPoolTableRowEditorDefaultRouter3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorDefaultRouter3.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorDefaultRouter4_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorDefaultRouter4_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorDefaultRouter4 = _TnDhcpServerConfigPoolTableRowEditorDefaultRouter4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 13),
    _TnDhcpServerConfigPoolTableRowEditorDefaultRouter4_Type()
)
tnDhcpServerConfigPoolTableRowEditorDefaultRouter4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorDefaultRouter4.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorDnsServer1_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorDnsServer1_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorDnsServer1 = _TnDhcpServerConfigPoolTableRowEditorDnsServer1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 14),
    _TnDhcpServerConfigPoolTableRowEditorDnsServer1_Type()
)
tnDhcpServerConfigPoolTableRowEditorDnsServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorDnsServer1.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorDnsServer2_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorDnsServer2_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorDnsServer2 = _TnDhcpServerConfigPoolTableRowEditorDnsServer2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 15),
    _TnDhcpServerConfigPoolTableRowEditorDnsServer2_Type()
)
tnDhcpServerConfigPoolTableRowEditorDnsServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorDnsServer2.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorDnsServer3_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorDnsServer3_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorDnsServer3 = _TnDhcpServerConfigPoolTableRowEditorDnsServer3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 16),
    _TnDhcpServerConfigPoolTableRowEditorDnsServer3_Type()
)
tnDhcpServerConfigPoolTableRowEditorDnsServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorDnsServer3.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorDnsServer4_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorDnsServer4_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorDnsServer4 = _TnDhcpServerConfigPoolTableRowEditorDnsServer4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 17),
    _TnDhcpServerConfigPoolTableRowEditorDnsServer4_Type()
)
tnDhcpServerConfigPoolTableRowEditorDnsServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorDnsServer4.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNtpServer1_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNtpServer1_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNtpServer1 = _TnDhcpServerConfigPoolTableRowEditorNtpServer1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 18),
    _TnDhcpServerConfigPoolTableRowEditorNtpServer1_Type()
)
tnDhcpServerConfigPoolTableRowEditorNtpServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNtpServer1.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNtpServer2_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNtpServer2_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNtpServer2 = _TnDhcpServerConfigPoolTableRowEditorNtpServer2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 19),
    _TnDhcpServerConfigPoolTableRowEditorNtpServer2_Type()
)
tnDhcpServerConfigPoolTableRowEditorNtpServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNtpServer2.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNtpServer3_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNtpServer3_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNtpServer3 = _TnDhcpServerConfigPoolTableRowEditorNtpServer3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 20),
    _TnDhcpServerConfigPoolTableRowEditorNtpServer3_Type()
)
tnDhcpServerConfigPoolTableRowEditorNtpServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNtpServer3.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNtpServer4_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNtpServer4_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNtpServer4 = _TnDhcpServerConfigPoolTableRowEditorNtpServer4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 21),
    _TnDhcpServerConfigPoolTableRowEditorNtpServer4_Type()
)
tnDhcpServerConfigPoolTableRowEditorNtpServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNtpServer4.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNetbiosNodeType_Type = TNDhcpServerNetbiosNodeEnum
_TnDhcpServerConfigPoolTableRowEditorNetbiosNodeType_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNetbiosNodeType = _TnDhcpServerConfigPoolTableRowEditorNetbiosNodeType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 22),
    _TnDhcpServerConfigPoolTableRowEditorNetbiosNodeType_Type()
)
tnDhcpServerConfigPoolTableRowEditorNetbiosNodeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNetbiosNodeType.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorNetbiosScope_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorNetbiosScope based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolTableRowEditorNetbiosScope_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorNetbiosScope_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNetbiosScope = _TnDhcpServerConfigPoolTableRowEditorNetbiosScope_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 23),
    _TnDhcpServerConfigPoolTableRowEditorNetbiosScope_Type()
)
tnDhcpServerConfigPoolTableRowEditorNetbiosScope.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNetbiosScope.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1 = _TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 24),
    _TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1_Type()
)
tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2 = _TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 25),
    _TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2_Type()
)
tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3 = _TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 26),
    _TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3_Type()
)
tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4 = _TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 27),
    _TnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4_Type()
)
tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorNisDomainName_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorNisDomainName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolTableRowEditorNisDomainName_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorNisDomainName_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNisDomainName = _TnDhcpServerConfigPoolTableRowEditorNisDomainName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 28),
    _TnDhcpServerConfigPoolTableRowEditorNisDomainName_Type()
)
tnDhcpServerConfigPoolTableRowEditorNisDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNisDomainName.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNisServer1_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNisServer1_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNisServer1 = _TnDhcpServerConfigPoolTableRowEditorNisServer1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 29),
    _TnDhcpServerConfigPoolTableRowEditorNisServer1_Type()
)
tnDhcpServerConfigPoolTableRowEditorNisServer1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNisServer1.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNisServer2_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNisServer2_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNisServer2 = _TnDhcpServerConfigPoolTableRowEditorNisServer2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 30),
    _TnDhcpServerConfigPoolTableRowEditorNisServer2_Type()
)
tnDhcpServerConfigPoolTableRowEditorNisServer2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNisServer2.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNisServer3_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNisServer3_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNisServer3 = _TnDhcpServerConfigPoolTableRowEditorNisServer3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 31),
    _TnDhcpServerConfigPoolTableRowEditorNisServer3_Type()
)
tnDhcpServerConfigPoolTableRowEditorNisServer3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNisServer3.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorNisServer4_Type = IpAddress
_TnDhcpServerConfigPoolTableRowEditorNisServer4_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorNisServer4 = _TnDhcpServerConfigPoolTableRowEditorNisServer4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 32),
    _TnDhcpServerConfigPoolTableRowEditorNisServer4_Type()
)
tnDhcpServerConfigPoolTableRowEditorNisServer4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorNisServer4.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorClientIdentifierType_Type = TNDhcpServerClientIdentifierEnum
_TnDhcpServerConfigPoolTableRowEditorClientIdentifierType_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorClientIdentifierType = _TnDhcpServerConfigPoolTableRowEditorClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 33),
    _TnDhcpServerConfigPoolTableRowEditorClientIdentifierType_Type()
)
tnDhcpServerConfigPoolTableRowEditorClientIdentifierType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorClientIdentifierType.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn = _TnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 34),
    _TnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn_Type()
)
tnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorClientIdentifierMac_Type = MacAddress
_TnDhcpServerConfigPoolTableRowEditorClientIdentifierMac_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorClientIdentifierMac = _TnDhcpServerConfigPoolTableRowEditorClientIdentifierMac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 35),
    _TnDhcpServerConfigPoolTableRowEditorClientIdentifierMac_Type()
)
tnDhcpServerConfigPoolTableRowEditorClientIdentifierMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorClientIdentifierMac.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorClientHardwareAddress_Type = MacAddress
_TnDhcpServerConfigPoolTableRowEditorClientHardwareAddress_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorClientHardwareAddress = _TnDhcpServerConfigPoolTableRowEditorClientHardwareAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 36),
    _TnDhcpServerConfigPoolTableRowEditorClientHardwareAddress_Type()
)
tnDhcpServerConfigPoolTableRowEditorClientHardwareAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorClientHardwareAddress.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorClientName_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorClientName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerConfigPoolTableRowEditorClientName_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorClientName_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorClientName = _TnDhcpServerConfigPoolTableRowEditorClientName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 37),
    _TnDhcpServerConfigPoolTableRowEditorClientName_Type()
)
tnDhcpServerConfigPoolTableRowEditorClientName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorClientName.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorVendorClassId1_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorVendorClassId1 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolTableRowEditorVendorClassId1_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorVendorClassId1_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorVendorClassId1 = _TnDhcpServerConfigPoolTableRowEditorVendorClassId1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 38),
    _TnDhcpServerConfigPoolTableRowEditorVendorClassId1_Type()
)
tnDhcpServerConfigPoolTableRowEditorVendorClassId1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorVendorClassId1.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1 = _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 39),
    _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1_Type()
)
tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorVendorClassId2_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorVendorClassId2 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolTableRowEditorVendorClassId2_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorVendorClassId2_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorVendorClassId2 = _TnDhcpServerConfigPoolTableRowEditorVendorClassId2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 40),
    _TnDhcpServerConfigPoolTableRowEditorVendorClassId2_Type()
)
tnDhcpServerConfigPoolTableRowEditorVendorClassId2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorVendorClassId2.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2 = _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 41),
    _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2_Type()
)
tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorVendorClassId3_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorVendorClassId3 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolTableRowEditorVendorClassId3_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorVendorClassId3_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorVendorClassId3 = _TnDhcpServerConfigPoolTableRowEditorVendorClassId3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 42),
    _TnDhcpServerConfigPoolTableRowEditorVendorClassId3_Type()
)
tnDhcpServerConfigPoolTableRowEditorVendorClassId3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorVendorClassId3.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3 = _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 43),
    _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3_Type()
)
tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorVendorClassId4_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorVendorClassId4 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerConfigPoolTableRowEditorVendorClassId4_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorVendorClassId4_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorVendorClassId4 = _TnDhcpServerConfigPoolTableRowEditorVendorClassId4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 44),
    _TnDhcpServerConfigPoolTableRowEditorVendorClassId4_Type()
)
tnDhcpServerConfigPoolTableRowEditorVendorClassId4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorVendorClassId4.setStatus("current")


class _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Type(TNDisplayString):
    """Custom type tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4 based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 66),
    )


_TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Type.__name__ = "TNDisplayString"
_TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4 = _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 45),
    _TnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4_Type()
)
tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4.setStatus("current")
_TnDhcpServerConfigPoolTableRowEditorAction_Type = TNRowEditorState
_TnDhcpServerConfigPoolTableRowEditorAction_Object = MibScalar
tnDhcpServerConfigPoolTableRowEditorAction = _TnDhcpServerConfigPoolTableRowEditorAction_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 2, 6, 100),
    _TnDhcpServerConfigPoolTableRowEditorAction_Type()
)
tnDhcpServerConfigPoolTableRowEditorAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorAction.setStatus("current")
_TnDhcpServerStatus_ObjectIdentity = ObjectIdentity
tnDhcpServerStatus = _TnDhcpServerStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3)
)
_TnDhcpServerStatusDeclinedTable_Object = MibTable
tnDhcpServerStatusDeclinedTable = _TnDhcpServerStatusDeclinedTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tnDhcpServerStatusDeclinedTable.setStatus("current")
_TnDhcpServerStatusDeclinedEntry_Object = MibTableRow
tnDhcpServerStatusDeclinedEntry = _TnDhcpServerStatusDeclinedEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 1, 1)
)
tnDhcpServerStatusDeclinedEntry.setIndexNames(
    (0, "TN-DHCP-SERVER-MIB", "tnDhcpServerStatusDeclinedEntryNo"),
)
if mibBuilder.loadTexts:
    tnDhcpServerStatusDeclinedEntry.setStatus("current")


class _TnDhcpServerStatusDeclinedEntryNo_Type(Integer32):
    """Custom type tnDhcpServerStatusDeclinedEntryNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_TnDhcpServerStatusDeclinedEntryNo_Type.__name__ = "Integer32"
_TnDhcpServerStatusDeclinedEntryNo_Object = MibTableColumn
tnDhcpServerStatusDeclinedEntryNo = _TnDhcpServerStatusDeclinedEntryNo_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 1, 1, 1),
    _TnDhcpServerStatusDeclinedEntryNo_Type()
)
tnDhcpServerStatusDeclinedEntryNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpServerStatusDeclinedEntryNo.setStatus("current")
_TnDhcpServerStatusDeclinedIpv4Address_Type = IpAddress
_TnDhcpServerStatusDeclinedIpv4Address_Object = MibTableColumn
tnDhcpServerStatusDeclinedIpv4Address = _TnDhcpServerStatusDeclinedIpv4Address_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 1, 1, 2),
    _TnDhcpServerStatusDeclinedIpv4Address_Type()
)
tnDhcpServerStatusDeclinedIpv4Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusDeclinedIpv4Address.setStatus("current")
_TnDhcpServerStatusStatistics_ObjectIdentity = ObjectIdentity
tnDhcpServerStatusStatistics = _TnDhcpServerStatusStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 2)
)
_TnDhcpServerStatusStatisticsDiscoverCnt_Type = Unsigned32
_TnDhcpServerStatusStatisticsDiscoverCnt_Object = MibScalar
tnDhcpServerStatusStatisticsDiscoverCnt = _TnDhcpServerStatusStatisticsDiscoverCnt_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 2, 1),
    _TnDhcpServerStatusStatisticsDiscoverCnt_Type()
)
tnDhcpServerStatusStatisticsDiscoverCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusStatisticsDiscoverCnt.setStatus("current")
_TnDhcpServerStatusStatisticsOfferCnt_Type = Unsigned32
_TnDhcpServerStatusStatisticsOfferCnt_Object = MibScalar
tnDhcpServerStatusStatisticsOfferCnt = _TnDhcpServerStatusStatisticsOfferCnt_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 2, 2),
    _TnDhcpServerStatusStatisticsOfferCnt_Type()
)
tnDhcpServerStatusStatisticsOfferCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusStatisticsOfferCnt.setStatus("current")
_TnDhcpServerStatusStatisticsRequestCnt_Type = Unsigned32
_TnDhcpServerStatusStatisticsRequestCnt_Object = MibScalar
tnDhcpServerStatusStatisticsRequestCnt = _TnDhcpServerStatusStatisticsRequestCnt_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 2, 3),
    _TnDhcpServerStatusStatisticsRequestCnt_Type()
)
tnDhcpServerStatusStatisticsRequestCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusStatisticsRequestCnt.setStatus("current")
_TnDhcpServerStatusStatisticsAckCnt_Type = Unsigned32
_TnDhcpServerStatusStatisticsAckCnt_Object = MibScalar
tnDhcpServerStatusStatisticsAckCnt = _TnDhcpServerStatusStatisticsAckCnt_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 2, 4),
    _TnDhcpServerStatusStatisticsAckCnt_Type()
)
tnDhcpServerStatusStatisticsAckCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusStatisticsAckCnt.setStatus("current")
_TnDhcpServerStatusStatisticsNakCnt_Type = Unsigned32
_TnDhcpServerStatusStatisticsNakCnt_Object = MibScalar
tnDhcpServerStatusStatisticsNakCnt = _TnDhcpServerStatusStatisticsNakCnt_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 2, 5),
    _TnDhcpServerStatusStatisticsNakCnt_Type()
)
tnDhcpServerStatusStatisticsNakCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusStatisticsNakCnt.setStatus("current")
_TnDhcpServerStatusStatisticsDeclineCnt_Type = Unsigned32
_TnDhcpServerStatusStatisticsDeclineCnt_Object = MibScalar
tnDhcpServerStatusStatisticsDeclineCnt = _TnDhcpServerStatusStatisticsDeclineCnt_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 2, 6),
    _TnDhcpServerStatusStatisticsDeclineCnt_Type()
)
tnDhcpServerStatusStatisticsDeclineCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusStatisticsDeclineCnt.setStatus("current")
_TnDhcpServerStatusStatisticsReleaseCnt_Type = Unsigned32
_TnDhcpServerStatusStatisticsReleaseCnt_Object = MibScalar
tnDhcpServerStatusStatisticsReleaseCnt = _TnDhcpServerStatusStatisticsReleaseCnt_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 2, 7),
    _TnDhcpServerStatusStatisticsReleaseCnt_Type()
)
tnDhcpServerStatusStatisticsReleaseCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusStatisticsReleaseCnt.setStatus("current")
_TnDhcpServerStatusStatisticsInformCnt_Type = Unsigned32
_TnDhcpServerStatusStatisticsInformCnt_Object = MibScalar
tnDhcpServerStatusStatisticsInformCnt = _TnDhcpServerStatusStatisticsInformCnt_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 2, 8),
    _TnDhcpServerStatusStatisticsInformCnt_Type()
)
tnDhcpServerStatusStatisticsInformCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusStatisticsInformCnt.setStatus("current")
_TnDhcpServerStatusBindingTable_Object = MibTable
tnDhcpServerStatusBindingTable = _TnDhcpServerStatusBindingTable_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3)
)
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingTable.setStatus("current")
_TnDhcpServerStatusBindingEntry_Object = MibTableRow
tnDhcpServerStatusBindingEntry = _TnDhcpServerStatusBindingEntry_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1)
)
tnDhcpServerStatusBindingEntry.setIndexNames(
    (0, "TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingIpAddress"),
)
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingEntry.setStatus("current")
_TnDhcpServerStatusBindingIpAddress_Type = IpAddress
_TnDhcpServerStatusBindingIpAddress_Object = MibTableColumn
tnDhcpServerStatusBindingIpAddress = _TnDhcpServerStatusBindingIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 1),
    _TnDhcpServerStatusBindingIpAddress_Type()
)
tnDhcpServerStatusBindingIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingIpAddress.setStatus("current")
_TnDhcpServerStatusBindingState_Type = TNDhcpServerBindingStateEnum
_TnDhcpServerStatusBindingState_Object = MibTableColumn
tnDhcpServerStatusBindingState = _TnDhcpServerStatusBindingState_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 2),
    _TnDhcpServerStatusBindingState_Type()
)
tnDhcpServerStatusBindingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingState.setStatus("current")
_TnDhcpServerStatusBindingType_Type = TNDhcpServerBindingEnum
_TnDhcpServerStatusBindingType_Object = MibTableColumn
tnDhcpServerStatusBindingType = _TnDhcpServerStatusBindingType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 3),
    _TnDhcpServerStatusBindingType_Type()
)
tnDhcpServerStatusBindingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingType.setStatus("current")


class _TnDhcpServerStatusBindingPoolName_Type(TNDisplayString):
    """Custom type tnDhcpServerStatusBindingPoolName based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TnDhcpServerStatusBindingPoolName_Type.__name__ = "TNDisplayString"
_TnDhcpServerStatusBindingPoolName_Object = MibTableColumn
tnDhcpServerStatusBindingPoolName = _TnDhcpServerStatusBindingPoolName_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 4),
    _TnDhcpServerStatusBindingPoolName_Type()
)
tnDhcpServerStatusBindingPoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingPoolName.setStatus("current")
_TnDhcpServerStatusBindingServerId_Type = IpAddress
_TnDhcpServerStatusBindingServerId_Object = MibTableColumn
tnDhcpServerStatusBindingServerId = _TnDhcpServerStatusBindingServerId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 5),
    _TnDhcpServerStatusBindingServerId_Type()
)
tnDhcpServerStatusBindingServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingServerId.setStatus("current")
_TnDhcpServerStatusBindingVlanId_Type = TNUnsigned16
_TnDhcpServerStatusBindingVlanId_Object = MibTableColumn
tnDhcpServerStatusBindingVlanId = _TnDhcpServerStatusBindingVlanId_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 6),
    _TnDhcpServerStatusBindingVlanId_Type()
)
tnDhcpServerStatusBindingVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingVlanId.setStatus("current")
_TnDhcpServerStatusBindingSubnetMask_Type = IpAddress
_TnDhcpServerStatusBindingSubnetMask_Object = MibTableColumn
tnDhcpServerStatusBindingSubnetMask = _TnDhcpServerStatusBindingSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 7),
    _TnDhcpServerStatusBindingSubnetMask_Type()
)
tnDhcpServerStatusBindingSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingSubnetMask.setStatus("current")
_TnDhcpServerStatusBindingClientIdentifierType_Type = TNDhcpServerClientIdentifierEnum
_TnDhcpServerStatusBindingClientIdentifierType_Object = MibTableColumn
tnDhcpServerStatusBindingClientIdentifierType = _TnDhcpServerStatusBindingClientIdentifierType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 8),
    _TnDhcpServerStatusBindingClientIdentifierType_Type()
)
tnDhcpServerStatusBindingClientIdentifierType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingClientIdentifierType.setStatus("current")


class _TnDhcpServerStatusBindingClientIdentifierFqdn_Type(TNDisplayString):
    """Custom type tnDhcpServerStatusBindingClientIdentifierFqdn based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerStatusBindingClientIdentifierFqdn_Type.__name__ = "TNDisplayString"
_TnDhcpServerStatusBindingClientIdentifierFqdn_Object = MibTableColumn
tnDhcpServerStatusBindingClientIdentifierFqdn = _TnDhcpServerStatusBindingClientIdentifierFqdn_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 9),
    _TnDhcpServerStatusBindingClientIdentifierFqdn_Type()
)
tnDhcpServerStatusBindingClientIdentifierFqdn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingClientIdentifierFqdn.setStatus("current")
_TnDhcpServerStatusBindingClientIdentifierMac_Type = MacAddress
_TnDhcpServerStatusBindingClientIdentifierMac_Object = MibTableColumn
tnDhcpServerStatusBindingClientIdentifierMac = _TnDhcpServerStatusBindingClientIdentifierMac_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 10),
    _TnDhcpServerStatusBindingClientIdentifierMac_Type()
)
tnDhcpServerStatusBindingClientIdentifierMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingClientIdentifierMac.setStatus("current")
_TnDhcpServerStatusBindingMacAddress_Type = MacAddress
_TnDhcpServerStatusBindingMacAddress_Object = MibTableColumn
tnDhcpServerStatusBindingMacAddress = _TnDhcpServerStatusBindingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 11),
    _TnDhcpServerStatusBindingMacAddress_Type()
)
tnDhcpServerStatusBindingMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingMacAddress.setStatus("current")


class _TnDhcpServerStatusBindingLease_Type(TNDisplayString):
    """Custom type tnDhcpServerStatusBindingLease based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerStatusBindingLease_Type.__name__ = "TNDisplayString"
_TnDhcpServerStatusBindingLease_Object = MibTableColumn
tnDhcpServerStatusBindingLease = _TnDhcpServerStatusBindingLease_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 12),
    _TnDhcpServerStatusBindingLease_Type()
)
tnDhcpServerStatusBindingLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingLease.setStatus("current")


class _TnDhcpServerStatusBindingTimeToExpire_Type(TNDisplayString):
    """Custom type tnDhcpServerStatusBindingTimeToExpire based on TNDisplayString"""
    subtypeSpec = TNDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_TnDhcpServerStatusBindingTimeToExpire_Type.__name__ = "TNDisplayString"
_TnDhcpServerStatusBindingTimeToExpire_Object = MibTableColumn
tnDhcpServerStatusBindingTimeToExpire = _TnDhcpServerStatusBindingTimeToExpire_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 3, 3, 1, 13),
    _TnDhcpServerStatusBindingTimeToExpire_Type()
)
tnDhcpServerStatusBindingTimeToExpire.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingTimeToExpire.setStatus("current")
_TnDhcpServerControl_ObjectIdentity = ObjectIdentity
tnDhcpServerControl = _TnDhcpServerControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 4)
)
_TnDhcpServerControlStatistics_ObjectIdentity = ObjectIdentity
tnDhcpServerControlStatistics = _TnDhcpServerControlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 4, 1)
)
_TnDhcpServerControlStatisticsClear_Type = TruthValue
_TnDhcpServerControlStatisticsClear_Object = MibScalar
tnDhcpServerControlStatisticsClear = _TnDhcpServerControlStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 4, 1, 1),
    _TnDhcpServerControlStatisticsClear_Type()
)
tnDhcpServerControlStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerControlStatisticsClear.setStatus("current")
_TnDhcpServerControlBinding_ObjectIdentity = ObjectIdentity
tnDhcpServerControlBinding = _TnDhcpServerControlBinding_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 4, 2)
)
_TnDhcpServerControlBindingClearByIp_Type = IpAddress
_TnDhcpServerControlBindingClearByIp_Object = MibScalar
tnDhcpServerControlBindingClearByIp = _TnDhcpServerControlBindingClearByIp_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 4, 2, 1),
    _TnDhcpServerControlBindingClearByIp_Type()
)
tnDhcpServerControlBindingClearByIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerControlBindingClearByIp.setStatus("current")
_TnDhcpServerControlBindingClearByType_Type = TNDhcpServerBindingEnum
_TnDhcpServerControlBindingClearByType_Object = MibScalar
tnDhcpServerControlBindingClearByType = _TnDhcpServerControlBindingClearByType_Object(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 1, 4, 2, 2),
    _TnDhcpServerControlBindingClearByType_Type()
)
tnDhcpServerControlBindingClearByType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDhcpServerControlBindingClearByType.setStatus("current")
_TnDhcpServerMibConformance_ObjectIdentity = ObjectIdentity
tnDhcpServerMibConformance = _TnDhcpServerMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2)
)
_TnDhcpServerMibCompliances_ObjectIdentity = ObjectIdentity
tnDhcpServerMibCompliances = _TnDhcpServerMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 1)
)
_TnDhcpServerMibGroups_ObjectIdentity = ObjectIdentity
tnDhcpServerMibGroups = _TnDhcpServerMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2)
)

# Managed Objects groups

tnDhcpServerConfigGlobalsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 1)
)
tnDhcpServerConfigGlobalsInfoGroup.setObjects(
    ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigGlobalsMode")
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigGlobalsInfoGroup.setStatus("current")

tnDhcpServerConfigVlanTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 2)
)
tnDhcpServerConfigVlanTableInfoGroup.setObjects(
    ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigVlanMode")
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigVlanTableInfoGroup.setStatus("current")

tnDhcpServerConfigExcludedTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 3)
)
tnDhcpServerConfigExcludedTableInfoGroup.setObjects(
    ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigExcludedAction")
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedTableInfoGroup.setStatus("current")

tnDhcpServerConfigExcludedIpTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 4)
)
tnDhcpServerConfigExcludedIpTableRowEditorInfoGroup.setObjects(
      *(("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigExcludedIpTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigExcludedIpTableRowEditorInfoGroup.setStatus("current")

tnDhcpServerConfigPoolTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 5)
)
tnDhcpServerConfigPoolTableInfoGroup.setObjects(
      *(("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolPoolType"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolIpv4Address"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolSubnetMask"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolSubnetBroadcast"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolLeaseDay"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolLeaseHour"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolLeaseMinute"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolDomainName"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolDefaultRouter1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolDefaultRouter2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolDefaultRouter3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolDefaultRouter4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolDnsServer1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolDnsServer2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolDnsServer3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolDnsServer4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNtpServer1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNtpServer2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNtpServer3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNtpServer4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNetbiosNodeType"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNetbiosScope"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNetbiosNameServer1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNetbiosNameServer2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNetbiosNameServer3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNetbiosNameServer4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNisDomainName"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNisServer1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNisServer2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNisServer3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolNisServer4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolClientIdentifierType"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolClientIdentifierFqdn"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolClientIdentifierMac"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolClientHardwareAddress"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolClientName"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolVendorClassId1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolVendorSpecificInfo1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolVendorClassId2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolVendorSpecificInfo2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolVendorClassId3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolVendorSpecificInfo3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolVendorClassId4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolVendorSpecificInfo4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolAction"))
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableInfoGroup.setStatus("current")

tnDhcpServerConfigPoolTableRowEditorInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 6)
)
tnDhcpServerConfigPoolTableRowEditorInfoGroup.setObjects(
      *(("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorPoolName"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorPoolType"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorIpv4Address"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorSubnetMask"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorSubnetBroadcast"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorLeaseDay"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorLeaseHour"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorLeaseMinute"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorDomainName"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorDefaultRouter1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorDefaultRouter2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorDefaultRouter3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorDefaultRouter4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorDnsServer1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorDnsServer2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorDnsServer3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorDnsServer4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNtpServer1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNtpServer2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNtpServer3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNtpServer4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNetbiosNodeType"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNetbiosScope"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNisDomainName"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNisServer1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNisServer2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNisServer3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorNisServer4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorClientIdentifierType"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorClientIdentifierMac"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorClientHardwareAddress"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorClientName"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorVendorClassId1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorVendorClassId2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorVendorClassId3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorVendorClassId4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorAction"))
)
if mibBuilder.loadTexts:
    tnDhcpServerConfigPoolTableRowEditorInfoGroup.setStatus("current")

tnDhcpServerStatusDeclinedTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 7)
)
tnDhcpServerStatusDeclinedTableInfoGroup.setObjects(
    ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusDeclinedIpv4Address")
)
if mibBuilder.loadTexts:
    tnDhcpServerStatusDeclinedTableInfoGroup.setStatus("current")

tnDhcpServerStatusStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 8)
)
tnDhcpServerStatusStatisticsInfoGroup.setObjects(
      *(("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusStatisticsDiscoverCnt"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusStatisticsOfferCnt"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusStatisticsRequestCnt"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusStatisticsAckCnt"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusStatisticsNakCnt"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusStatisticsDeclineCnt"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusStatisticsReleaseCnt"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusStatisticsInformCnt"))
)
if mibBuilder.loadTexts:
    tnDhcpServerStatusStatisticsInfoGroup.setStatus("current")

tnDhcpServerStatusBindingTableInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 9)
)
tnDhcpServerStatusBindingTableInfoGroup.setObjects(
      *(("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingState"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingType"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingPoolName"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingServerId"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingVlanId"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingSubnetMask"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingClientIdentifierType"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingClientIdentifierFqdn"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingClientIdentifierMac"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingMacAddress"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingLease"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingTimeToExpire"))
)
if mibBuilder.loadTexts:
    tnDhcpServerStatusBindingTableInfoGroup.setStatus("current")

tnDhcpServerControlStatisticsInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 10)
)
tnDhcpServerControlStatisticsInfoGroup.setObjects(
    ("TN-DHCP-SERVER-MIB", "tnDhcpServerControlStatisticsClear")
)
if mibBuilder.loadTexts:
    tnDhcpServerControlStatisticsInfoGroup.setStatus("current")

tnDhcpServerControlBindingInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 2, 11)
)
tnDhcpServerControlBindingInfoGroup.setObjects(
      *(("TN-DHCP-SERVER-MIB", "tnDhcpServerControlBindingClearByIp"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerControlBindingClearByType"))
)
if mibBuilder.loadTexts:
    tnDhcpServerControlBindingInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnDhcpServerMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 868, 2, 5, 146, 2, 1, 1)
)
tnDhcpServerMibCompliance.setObjects(
      *(("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigGlobalsInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigVlanTableInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigExcludedTableInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigExcludedIpTableRowEditorInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerConfigPoolTableRowEditorInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusDeclinedTableInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusStatisticsInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerStatusBindingTableInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerControlStatisticsInfoGroup"),
        ("TN-DHCP-SERVER-MIB", "tnDhcpServerControlBindingInfoGroup"))
)
if mibBuilder.loadTexts:
    tnDhcpServerMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-DHCP-SERVER-MIB",
    **{"TNDhcpServerBindingEnum": TNDhcpServerBindingEnum,
       "TNDhcpServerBindingStateEnum": TNDhcpServerBindingStateEnum,
       "TNDhcpServerClientIdentifierEnum": TNDhcpServerClientIdentifierEnum,
       "TNDhcpServerNetbiosNodeEnum": TNDhcpServerNetbiosNodeEnum,
       "TNDhcpServerPoolEnum": TNDhcpServerPoolEnum,
       "tnDhcpServerMib": tnDhcpServerMib,
       "tnDhcpServerMibObjects": tnDhcpServerMibObjects,
       "tnDhcpServerConfig": tnDhcpServerConfig,
       "tnDhcpServerConfigGlobals": tnDhcpServerConfigGlobals,
       "tnDhcpServerConfigGlobalsMode": tnDhcpServerConfigGlobalsMode,
       "tnDhcpServerConfigVlanTable": tnDhcpServerConfigVlanTable,
       "tnDhcpServerConfigVlanEntry": tnDhcpServerConfigVlanEntry,
       "tnDhcpServerConfigVlanIfIndex": tnDhcpServerConfigVlanIfIndex,
       "tnDhcpServerConfigVlanMode": tnDhcpServerConfigVlanMode,
       "tnDhcpServerConfigExcludedTable": tnDhcpServerConfigExcludedTable,
       "tnDhcpServerConfigExcludedEntry": tnDhcpServerConfigExcludedEntry,
       "tnDhcpServerConfigExcludedLowIpAddress": tnDhcpServerConfigExcludedLowIpAddress,
       "tnDhcpServerConfigExcludedHighIpAddress": tnDhcpServerConfigExcludedHighIpAddress,
       "tnDhcpServerConfigExcludedAction": tnDhcpServerConfigExcludedAction,
       "tnDhcpServerConfigExcludedIpTableRowEditor": tnDhcpServerConfigExcludedIpTableRowEditor,
       "tnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress": tnDhcpServerConfigExcludedIpTableRowEditorLowIpAddress,
       "tnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress": tnDhcpServerConfigExcludedIpTableRowEditorHighIpAddress,
       "tnDhcpServerConfigExcludedIpTableRowEditorAction": tnDhcpServerConfigExcludedIpTableRowEditorAction,
       "tnDhcpServerConfigPoolTable": tnDhcpServerConfigPoolTable,
       "tnDhcpServerConfigPoolEntry": tnDhcpServerConfigPoolEntry,
       "tnDhcpServerConfigPoolPoolName": tnDhcpServerConfigPoolPoolName,
       "tnDhcpServerConfigPoolPoolType": tnDhcpServerConfigPoolPoolType,
       "tnDhcpServerConfigPoolIpv4Address": tnDhcpServerConfigPoolIpv4Address,
       "tnDhcpServerConfigPoolSubnetMask": tnDhcpServerConfigPoolSubnetMask,
       "tnDhcpServerConfigPoolSubnetBroadcast": tnDhcpServerConfigPoolSubnetBroadcast,
       "tnDhcpServerConfigPoolLeaseDay": tnDhcpServerConfigPoolLeaseDay,
       "tnDhcpServerConfigPoolLeaseHour": tnDhcpServerConfigPoolLeaseHour,
       "tnDhcpServerConfigPoolLeaseMinute": tnDhcpServerConfigPoolLeaseMinute,
       "tnDhcpServerConfigPoolDomainName": tnDhcpServerConfigPoolDomainName,
       "tnDhcpServerConfigPoolDefaultRouter1": tnDhcpServerConfigPoolDefaultRouter1,
       "tnDhcpServerConfigPoolDefaultRouter2": tnDhcpServerConfigPoolDefaultRouter2,
       "tnDhcpServerConfigPoolDefaultRouter3": tnDhcpServerConfigPoolDefaultRouter3,
       "tnDhcpServerConfigPoolDefaultRouter4": tnDhcpServerConfigPoolDefaultRouter4,
       "tnDhcpServerConfigPoolDnsServer1": tnDhcpServerConfigPoolDnsServer1,
       "tnDhcpServerConfigPoolDnsServer2": tnDhcpServerConfigPoolDnsServer2,
       "tnDhcpServerConfigPoolDnsServer3": tnDhcpServerConfigPoolDnsServer3,
       "tnDhcpServerConfigPoolDnsServer4": tnDhcpServerConfigPoolDnsServer4,
       "tnDhcpServerConfigPoolNtpServer1": tnDhcpServerConfigPoolNtpServer1,
       "tnDhcpServerConfigPoolNtpServer2": tnDhcpServerConfigPoolNtpServer2,
       "tnDhcpServerConfigPoolNtpServer3": tnDhcpServerConfigPoolNtpServer3,
       "tnDhcpServerConfigPoolNtpServer4": tnDhcpServerConfigPoolNtpServer4,
       "tnDhcpServerConfigPoolNetbiosNodeType": tnDhcpServerConfigPoolNetbiosNodeType,
       "tnDhcpServerConfigPoolNetbiosScope": tnDhcpServerConfigPoolNetbiosScope,
       "tnDhcpServerConfigPoolNetbiosNameServer1": tnDhcpServerConfigPoolNetbiosNameServer1,
       "tnDhcpServerConfigPoolNetbiosNameServer2": tnDhcpServerConfigPoolNetbiosNameServer2,
       "tnDhcpServerConfigPoolNetbiosNameServer3": tnDhcpServerConfigPoolNetbiosNameServer3,
       "tnDhcpServerConfigPoolNetbiosNameServer4": tnDhcpServerConfigPoolNetbiosNameServer4,
       "tnDhcpServerConfigPoolNisDomainName": tnDhcpServerConfigPoolNisDomainName,
       "tnDhcpServerConfigPoolNisServer1": tnDhcpServerConfigPoolNisServer1,
       "tnDhcpServerConfigPoolNisServer2": tnDhcpServerConfigPoolNisServer2,
       "tnDhcpServerConfigPoolNisServer3": tnDhcpServerConfigPoolNisServer3,
       "tnDhcpServerConfigPoolNisServer4": tnDhcpServerConfigPoolNisServer4,
       "tnDhcpServerConfigPoolClientIdentifierType": tnDhcpServerConfigPoolClientIdentifierType,
       "tnDhcpServerConfigPoolClientIdentifierFqdn": tnDhcpServerConfigPoolClientIdentifierFqdn,
       "tnDhcpServerConfigPoolClientIdentifierMac": tnDhcpServerConfigPoolClientIdentifierMac,
       "tnDhcpServerConfigPoolClientHardwareAddress": tnDhcpServerConfigPoolClientHardwareAddress,
       "tnDhcpServerConfigPoolClientName": tnDhcpServerConfigPoolClientName,
       "tnDhcpServerConfigPoolVendorClassId1": tnDhcpServerConfigPoolVendorClassId1,
       "tnDhcpServerConfigPoolVendorSpecificInfo1": tnDhcpServerConfigPoolVendorSpecificInfo1,
       "tnDhcpServerConfigPoolVendorClassId2": tnDhcpServerConfigPoolVendorClassId2,
       "tnDhcpServerConfigPoolVendorSpecificInfo2": tnDhcpServerConfigPoolVendorSpecificInfo2,
       "tnDhcpServerConfigPoolVendorClassId3": tnDhcpServerConfigPoolVendorClassId3,
       "tnDhcpServerConfigPoolVendorSpecificInfo3": tnDhcpServerConfigPoolVendorSpecificInfo3,
       "tnDhcpServerConfigPoolVendorClassId4": tnDhcpServerConfigPoolVendorClassId4,
       "tnDhcpServerConfigPoolVendorSpecificInfo4": tnDhcpServerConfigPoolVendorSpecificInfo4,
       "tnDhcpServerConfigPoolAction": tnDhcpServerConfigPoolAction,
       "tnDhcpServerConfigPoolTableRowEditor": tnDhcpServerConfigPoolTableRowEditor,
       "tnDhcpServerConfigPoolTableRowEditorPoolName": tnDhcpServerConfigPoolTableRowEditorPoolName,
       "tnDhcpServerConfigPoolTableRowEditorPoolType": tnDhcpServerConfigPoolTableRowEditorPoolType,
       "tnDhcpServerConfigPoolTableRowEditorIpv4Address": tnDhcpServerConfigPoolTableRowEditorIpv4Address,
       "tnDhcpServerConfigPoolTableRowEditorSubnetMask": tnDhcpServerConfigPoolTableRowEditorSubnetMask,
       "tnDhcpServerConfigPoolTableRowEditorSubnetBroadcast": tnDhcpServerConfigPoolTableRowEditorSubnetBroadcast,
       "tnDhcpServerConfigPoolTableRowEditorLeaseDay": tnDhcpServerConfigPoolTableRowEditorLeaseDay,
       "tnDhcpServerConfigPoolTableRowEditorLeaseHour": tnDhcpServerConfigPoolTableRowEditorLeaseHour,
       "tnDhcpServerConfigPoolTableRowEditorLeaseMinute": tnDhcpServerConfigPoolTableRowEditorLeaseMinute,
       "tnDhcpServerConfigPoolTableRowEditorDomainName": tnDhcpServerConfigPoolTableRowEditorDomainName,
       "tnDhcpServerConfigPoolTableRowEditorDefaultRouter1": tnDhcpServerConfigPoolTableRowEditorDefaultRouter1,
       "tnDhcpServerConfigPoolTableRowEditorDefaultRouter2": tnDhcpServerConfigPoolTableRowEditorDefaultRouter2,
       "tnDhcpServerConfigPoolTableRowEditorDefaultRouter3": tnDhcpServerConfigPoolTableRowEditorDefaultRouter3,
       "tnDhcpServerConfigPoolTableRowEditorDefaultRouter4": tnDhcpServerConfigPoolTableRowEditorDefaultRouter4,
       "tnDhcpServerConfigPoolTableRowEditorDnsServer1": tnDhcpServerConfigPoolTableRowEditorDnsServer1,
       "tnDhcpServerConfigPoolTableRowEditorDnsServer2": tnDhcpServerConfigPoolTableRowEditorDnsServer2,
       "tnDhcpServerConfigPoolTableRowEditorDnsServer3": tnDhcpServerConfigPoolTableRowEditorDnsServer3,
       "tnDhcpServerConfigPoolTableRowEditorDnsServer4": tnDhcpServerConfigPoolTableRowEditorDnsServer4,
       "tnDhcpServerConfigPoolTableRowEditorNtpServer1": tnDhcpServerConfigPoolTableRowEditorNtpServer1,
       "tnDhcpServerConfigPoolTableRowEditorNtpServer2": tnDhcpServerConfigPoolTableRowEditorNtpServer2,
       "tnDhcpServerConfigPoolTableRowEditorNtpServer3": tnDhcpServerConfigPoolTableRowEditorNtpServer3,
       "tnDhcpServerConfigPoolTableRowEditorNtpServer4": tnDhcpServerConfigPoolTableRowEditorNtpServer4,
       "tnDhcpServerConfigPoolTableRowEditorNetbiosNodeType": tnDhcpServerConfigPoolTableRowEditorNetbiosNodeType,
       "tnDhcpServerConfigPoolTableRowEditorNetbiosScope": tnDhcpServerConfigPoolTableRowEditorNetbiosScope,
       "tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1": tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer1,
       "tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2": tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer2,
       "tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3": tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer3,
       "tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4": tnDhcpServerConfigPoolTableRowEditorNetbiosNameServer4,
       "tnDhcpServerConfigPoolTableRowEditorNisDomainName": tnDhcpServerConfigPoolTableRowEditorNisDomainName,
       "tnDhcpServerConfigPoolTableRowEditorNisServer1": tnDhcpServerConfigPoolTableRowEditorNisServer1,
       "tnDhcpServerConfigPoolTableRowEditorNisServer2": tnDhcpServerConfigPoolTableRowEditorNisServer2,
       "tnDhcpServerConfigPoolTableRowEditorNisServer3": tnDhcpServerConfigPoolTableRowEditorNisServer3,
       "tnDhcpServerConfigPoolTableRowEditorNisServer4": tnDhcpServerConfigPoolTableRowEditorNisServer4,
       "tnDhcpServerConfigPoolTableRowEditorClientIdentifierType": tnDhcpServerConfigPoolTableRowEditorClientIdentifierType,
       "tnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn": tnDhcpServerConfigPoolTableRowEditorClientIdentifierFqdn,
       "tnDhcpServerConfigPoolTableRowEditorClientIdentifierMac": tnDhcpServerConfigPoolTableRowEditorClientIdentifierMac,
       "tnDhcpServerConfigPoolTableRowEditorClientHardwareAddress": tnDhcpServerConfigPoolTableRowEditorClientHardwareAddress,
       "tnDhcpServerConfigPoolTableRowEditorClientName": tnDhcpServerConfigPoolTableRowEditorClientName,
       "tnDhcpServerConfigPoolTableRowEditorVendorClassId1": tnDhcpServerConfigPoolTableRowEditorVendorClassId1,
       "tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1": tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo1,
       "tnDhcpServerConfigPoolTableRowEditorVendorClassId2": tnDhcpServerConfigPoolTableRowEditorVendorClassId2,
       "tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2": tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo2,
       "tnDhcpServerConfigPoolTableRowEditorVendorClassId3": tnDhcpServerConfigPoolTableRowEditorVendorClassId3,
       "tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3": tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo3,
       "tnDhcpServerConfigPoolTableRowEditorVendorClassId4": tnDhcpServerConfigPoolTableRowEditorVendorClassId4,
       "tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4": tnDhcpServerConfigPoolTableRowEditorVendorSpecificInfo4,
       "tnDhcpServerConfigPoolTableRowEditorAction": tnDhcpServerConfigPoolTableRowEditorAction,
       "tnDhcpServerStatus": tnDhcpServerStatus,
       "tnDhcpServerStatusDeclinedTable": tnDhcpServerStatusDeclinedTable,
       "tnDhcpServerStatusDeclinedEntry": tnDhcpServerStatusDeclinedEntry,
       "tnDhcpServerStatusDeclinedEntryNo": tnDhcpServerStatusDeclinedEntryNo,
       "tnDhcpServerStatusDeclinedIpv4Address": tnDhcpServerStatusDeclinedIpv4Address,
       "tnDhcpServerStatusStatistics": tnDhcpServerStatusStatistics,
       "tnDhcpServerStatusStatisticsDiscoverCnt": tnDhcpServerStatusStatisticsDiscoverCnt,
       "tnDhcpServerStatusStatisticsOfferCnt": tnDhcpServerStatusStatisticsOfferCnt,
       "tnDhcpServerStatusStatisticsRequestCnt": tnDhcpServerStatusStatisticsRequestCnt,
       "tnDhcpServerStatusStatisticsAckCnt": tnDhcpServerStatusStatisticsAckCnt,
       "tnDhcpServerStatusStatisticsNakCnt": tnDhcpServerStatusStatisticsNakCnt,
       "tnDhcpServerStatusStatisticsDeclineCnt": tnDhcpServerStatusStatisticsDeclineCnt,
       "tnDhcpServerStatusStatisticsReleaseCnt": tnDhcpServerStatusStatisticsReleaseCnt,
       "tnDhcpServerStatusStatisticsInformCnt": tnDhcpServerStatusStatisticsInformCnt,
       "tnDhcpServerStatusBindingTable": tnDhcpServerStatusBindingTable,
       "tnDhcpServerStatusBindingEntry": tnDhcpServerStatusBindingEntry,
       "tnDhcpServerStatusBindingIpAddress": tnDhcpServerStatusBindingIpAddress,
       "tnDhcpServerStatusBindingState": tnDhcpServerStatusBindingState,
       "tnDhcpServerStatusBindingType": tnDhcpServerStatusBindingType,
       "tnDhcpServerStatusBindingPoolName": tnDhcpServerStatusBindingPoolName,
       "tnDhcpServerStatusBindingServerId": tnDhcpServerStatusBindingServerId,
       "tnDhcpServerStatusBindingVlanId": tnDhcpServerStatusBindingVlanId,
       "tnDhcpServerStatusBindingSubnetMask": tnDhcpServerStatusBindingSubnetMask,
       "tnDhcpServerStatusBindingClientIdentifierType": tnDhcpServerStatusBindingClientIdentifierType,
       "tnDhcpServerStatusBindingClientIdentifierFqdn": tnDhcpServerStatusBindingClientIdentifierFqdn,
       "tnDhcpServerStatusBindingClientIdentifierMac": tnDhcpServerStatusBindingClientIdentifierMac,
       "tnDhcpServerStatusBindingMacAddress": tnDhcpServerStatusBindingMacAddress,
       "tnDhcpServerStatusBindingLease": tnDhcpServerStatusBindingLease,
       "tnDhcpServerStatusBindingTimeToExpire": tnDhcpServerStatusBindingTimeToExpire,
       "tnDhcpServerControl": tnDhcpServerControl,
       "tnDhcpServerControlStatistics": tnDhcpServerControlStatistics,
       "tnDhcpServerControlStatisticsClear": tnDhcpServerControlStatisticsClear,
       "tnDhcpServerControlBinding": tnDhcpServerControlBinding,
       "tnDhcpServerControlBindingClearByIp": tnDhcpServerControlBindingClearByIp,
       "tnDhcpServerControlBindingClearByType": tnDhcpServerControlBindingClearByType,
       "tnDhcpServerMibConformance": tnDhcpServerMibConformance,
       "tnDhcpServerMibCompliances": tnDhcpServerMibCompliances,
       "tnDhcpServerMibCompliance": tnDhcpServerMibCompliance,
       "tnDhcpServerMibGroups": tnDhcpServerMibGroups,
       "tnDhcpServerConfigGlobalsInfoGroup": tnDhcpServerConfigGlobalsInfoGroup,
       "tnDhcpServerConfigVlanTableInfoGroup": tnDhcpServerConfigVlanTableInfoGroup,
       "tnDhcpServerConfigExcludedTableInfoGroup": tnDhcpServerConfigExcludedTableInfoGroup,
       "tnDhcpServerConfigExcludedIpTableRowEditorInfoGroup": tnDhcpServerConfigExcludedIpTableRowEditorInfoGroup,
       "tnDhcpServerConfigPoolTableInfoGroup": tnDhcpServerConfigPoolTableInfoGroup,
       "tnDhcpServerConfigPoolTableRowEditorInfoGroup": tnDhcpServerConfigPoolTableRowEditorInfoGroup,
       "tnDhcpServerStatusDeclinedTableInfoGroup": tnDhcpServerStatusDeclinedTableInfoGroup,
       "tnDhcpServerStatusStatisticsInfoGroup": tnDhcpServerStatusStatisticsInfoGroup,
       "tnDhcpServerStatusBindingTableInfoGroup": tnDhcpServerStatusBindingTableInfoGroup,
       "tnDhcpServerControlStatisticsInfoGroup": tnDhcpServerControlStatisticsInfoGroup,
       "tnDhcpServerControlBindingInfoGroup": tnDhcpServerControlBindingInfoGroup}
)
