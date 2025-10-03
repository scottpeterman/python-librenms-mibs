# SNMP MIB module (LINKSYS-BRIDGE-SECURITY) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\linksys\LINKSYS-BRIDGE-SECURITY
# Produced by pysmi-1.6.2 at Thu Oct  2 12:08:48 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(rnd,) = mibBuilder.importSymbols(
    "LINKSYS-MIB",
    "rnd")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlBridgeSecurity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RlIpDhcpSnoopType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("learnedByProtocol", 1),
          ("deletedByTimeout", 2),
          ("static", 3))
    )



class RlIpSourceGuardType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )



class RlIpSourceGuardStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



class RlIpSourceGuardFailReason(TextualConvention, Integer32):
    status = "current"
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
        *(("noProblem", 1),
          ("noResource", 2),
          ("noSnoopVlan", 3),
          ("trustPort", 4))
    )



class RlIpArpInspectListNameType(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )



class ProtocolFilteringMap(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("all", 0),
          ("cdp", 1),
          ("vtp", 2),
          ("dtp", 3),
          ("udld", 4),
          ("pagp", 5),
          ("sstp", 6))
    )


# MIB Managed Objects in the order of their OIDs

_RlIpDhcpSnoop_ObjectIdentity = ObjectIdentity
rlIpDhcpSnoop = _RlIpDhcpSnoop_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1)
)
_RlIpDhcpSnoopMibVersion_Type = Integer32
_RlIpDhcpSnoopMibVersion_Object = MibScalar
rlIpDhcpSnoopMibVersion = _RlIpDhcpSnoopMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 1),
    _RlIpDhcpSnoopMibVersion_Type()
)
rlIpDhcpSnoopMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopMibVersion.setStatus("current")


class _RlIpDhcpSnoopEnable_Type(Integer32):
    """Custom type rlIpDhcpSnoopEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlIpDhcpSnoopEnable_Type.__name__ = "Integer32"
_RlIpDhcpSnoopEnable_Object = MibScalar
rlIpDhcpSnoopEnable = _RlIpDhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 2),
    _RlIpDhcpSnoopEnable_Type()
)
rlIpDhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopEnable.setStatus("current")


class _RlIpDhcpSnoopFileEnable_Type(Integer32):
    """Custom type rlIpDhcpSnoopFileEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlIpDhcpSnoopFileEnable_Type.__name__ = "Integer32"
_RlIpDhcpSnoopFileEnable_Object = MibScalar
rlIpDhcpSnoopFileEnable = _RlIpDhcpSnoopFileEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 3),
    _RlIpDhcpSnoopFileEnable_Type()
)
rlIpDhcpSnoopFileEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopFileEnable.setStatus("current")


class _RlIpDhcpSnoopClearAction_Type(Integer32):
    """Custom type rlIpDhcpSnoopClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("clearNow", 2))
    )


_RlIpDhcpSnoopClearAction_Type.__name__ = "Integer32"
_RlIpDhcpSnoopClearAction_Object = MibScalar
rlIpDhcpSnoopClearAction = _RlIpDhcpSnoopClearAction_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 4),
    _RlIpDhcpSnoopClearAction_Type()
)
rlIpDhcpSnoopClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopClearAction.setStatus("current")


class _RlIpDhcpSnoopFileUpdateTime_Type(Integer32):
    """Custom type rlIpDhcpSnoopFileUpdateTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(600, 86400),
    )


_RlIpDhcpSnoopFileUpdateTime_Type.__name__ = "Integer32"
_RlIpDhcpSnoopFileUpdateTime_Object = MibScalar
rlIpDhcpSnoopFileUpdateTime = _RlIpDhcpSnoopFileUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 5),
    _RlIpDhcpSnoopFileUpdateTime_Type()
)
rlIpDhcpSnoopFileUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopFileUpdateTime.setStatus("current")


class _RlIpDhcpSnoopVerifyMacAddress_Type(Integer32):
    """Custom type rlIpDhcpSnoopVerifyMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlIpDhcpSnoopVerifyMacAddress_Type.__name__ = "Integer32"
_RlIpDhcpSnoopVerifyMacAddress_Object = MibScalar
rlIpDhcpSnoopVerifyMacAddress = _RlIpDhcpSnoopVerifyMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 6),
    _RlIpDhcpSnoopVerifyMacAddress_Type()
)
rlIpDhcpSnoopVerifyMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopVerifyMacAddress.setStatus("current")
_RlIpDhcpSnoopCurrentEntiresNumber_Type = Integer32
_RlIpDhcpSnoopCurrentEntiresNumber_Object = MibScalar
rlIpDhcpSnoopCurrentEntiresNumber = _RlIpDhcpSnoopCurrentEntiresNumber_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 7),
    _RlIpDhcpSnoopCurrentEntiresNumber_Type()
)
rlIpDhcpSnoopCurrentEntiresNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopCurrentEntiresNumber.setStatus("current")


class _RlIpDhcpOpt82InsertionEnable_Type(Integer32):
    """Custom type rlIpDhcpOpt82InsertionEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlIpDhcpOpt82InsertionEnable_Type.__name__ = "Integer32"
_RlIpDhcpOpt82InsertionEnable_Object = MibScalar
rlIpDhcpOpt82InsertionEnable = _RlIpDhcpOpt82InsertionEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 8),
    _RlIpDhcpOpt82InsertionEnable_Type()
)
rlIpDhcpOpt82InsertionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpOpt82InsertionEnable.setStatus("current")


class _RlIpDhcpOpt82RxOnUntrustedEnable_Type(Integer32):
    """Custom type rlIpDhcpOpt82RxOnUntrustedEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlIpDhcpOpt82RxOnUntrustedEnable_Type.__name__ = "Integer32"
_RlIpDhcpOpt82RxOnUntrustedEnable_Object = MibScalar
rlIpDhcpOpt82RxOnUntrustedEnable = _RlIpDhcpOpt82RxOnUntrustedEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 9),
    _RlIpDhcpOpt82RxOnUntrustedEnable_Type()
)
rlIpDhcpOpt82RxOnUntrustedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpOpt82RxOnUntrustedEnable.setStatus("current")
_RlIpDhcpSnoopStaticTable_Object = MibTable
rlIpDhcpSnoopStaticTable = _RlIpDhcpSnoopStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 10)
)
if mibBuilder.loadTexts:
    rlIpDhcpSnoopStaticTable.setStatus("current")
_RlIpDhcpSnoopStaticEntry_Object = MibTableRow
rlIpDhcpSnoopStaticEntry = _RlIpDhcpSnoopStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 10, 1)
)
rlIpDhcpSnoopStaticEntry.setIndexNames(
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpDhcpSnoopStaticVLANTag"),
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpDhcpSnoopStaticMACAddress"),
)
if mibBuilder.loadTexts:
    rlIpDhcpSnoopStaticEntry.setStatus("current")
_RlIpDhcpSnoopStaticVLANTag_Type = VlanId
_RlIpDhcpSnoopStaticVLANTag_Object = MibTableColumn
rlIpDhcpSnoopStaticVLANTag = _RlIpDhcpSnoopStaticVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 10, 1, 1),
    _RlIpDhcpSnoopStaticVLANTag_Type()
)
rlIpDhcpSnoopStaticVLANTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopStaticVLANTag.setStatus("current")
_RlIpDhcpSnoopStaticMACAddress_Type = MacAddress
_RlIpDhcpSnoopStaticMACAddress_Object = MibTableColumn
rlIpDhcpSnoopStaticMACAddress = _RlIpDhcpSnoopStaticMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 10, 1, 2),
    _RlIpDhcpSnoopStaticMACAddress_Type()
)
rlIpDhcpSnoopStaticMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopStaticMACAddress.setStatus("current")
_RlIpDhcpSnoopStaticIPAddress_Type = IpAddress
_RlIpDhcpSnoopStaticIPAddress_Object = MibTableColumn
rlIpDhcpSnoopStaticIPAddress = _RlIpDhcpSnoopStaticIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 10, 1, 3),
    _RlIpDhcpSnoopStaticIPAddress_Type()
)
rlIpDhcpSnoopStaticIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopStaticIPAddress.setStatus("current")
_RlIpDhcpSnoopStaticPortInterface_Type = InterfaceIndex
_RlIpDhcpSnoopStaticPortInterface_Object = MibTableColumn
rlIpDhcpSnoopStaticPortInterface = _RlIpDhcpSnoopStaticPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 10, 1, 4),
    _RlIpDhcpSnoopStaticPortInterface_Type()
)
rlIpDhcpSnoopStaticPortInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopStaticPortInterface.setStatus("current")
_RlIpDhcpSnoopStaticRowStatus_Type = RowStatus
_RlIpDhcpSnoopStaticRowStatus_Object = MibTableColumn
rlIpDhcpSnoopStaticRowStatus = _RlIpDhcpSnoopStaticRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 10, 1, 5),
    _RlIpDhcpSnoopStaticRowStatus_Type()
)
rlIpDhcpSnoopStaticRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopStaticRowStatus.setStatus("current")
_RlIpDhcpSnoopTable_Object = MibTable
rlIpDhcpSnoopTable = _RlIpDhcpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 11)
)
if mibBuilder.loadTexts:
    rlIpDhcpSnoopTable.setStatus("current")
_RlIpDhcpSnoopEntry_Object = MibTableRow
rlIpDhcpSnoopEntry = _RlIpDhcpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 11, 1)
)
rlIpDhcpSnoopEntry.setIndexNames(
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpDhcpSnoopVLANTag"),
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpDhcpSnoopMACAddress"),
)
if mibBuilder.loadTexts:
    rlIpDhcpSnoopEntry.setStatus("current")
_RlIpDhcpSnoopVLANTag_Type = VlanId
_RlIpDhcpSnoopVLANTag_Object = MibTableColumn
rlIpDhcpSnoopVLANTag = _RlIpDhcpSnoopVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 11, 1, 1),
    _RlIpDhcpSnoopVLANTag_Type()
)
rlIpDhcpSnoopVLANTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopVLANTag.setStatus("current")
_RlIpDhcpSnoopMACAddress_Type = MacAddress
_RlIpDhcpSnoopMACAddress_Object = MibTableColumn
rlIpDhcpSnoopMACAddress = _RlIpDhcpSnoopMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 11, 1, 2),
    _RlIpDhcpSnoopMACAddress_Type()
)
rlIpDhcpSnoopMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopMACAddress.setStatus("current")
_RlIpDhcpSnoopType_Type = RlIpDhcpSnoopType
_RlIpDhcpSnoopType_Object = MibTableColumn
rlIpDhcpSnoopType = _RlIpDhcpSnoopType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 11, 1, 3),
    _RlIpDhcpSnoopType_Type()
)
rlIpDhcpSnoopType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopType.setStatus("current")
_RlIpDhcpSnoopLeaseTime_Type = Unsigned32
_RlIpDhcpSnoopLeaseTime_Object = MibTableColumn
rlIpDhcpSnoopLeaseTime = _RlIpDhcpSnoopLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 11, 1, 4),
    _RlIpDhcpSnoopLeaseTime_Type()
)
rlIpDhcpSnoopLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopLeaseTime.setStatus("current")
_RlIpDhcpSnoopIPAddress_Type = IpAddress
_RlIpDhcpSnoopIPAddress_Object = MibTableColumn
rlIpDhcpSnoopIPAddress = _RlIpDhcpSnoopIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 11, 1, 5),
    _RlIpDhcpSnoopIPAddress_Type()
)
rlIpDhcpSnoopIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopIPAddress.setStatus("current")
_RlIpDhcpSnoopPortInterface_Type = InterfaceIndex
_RlIpDhcpSnoopPortInterface_Object = MibTableColumn
rlIpDhcpSnoopPortInterface = _RlIpDhcpSnoopPortInterface_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 11, 1, 6),
    _RlIpDhcpSnoopPortInterface_Type()
)
rlIpDhcpSnoopPortInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopPortInterface.setStatus("current")
_RlIpDhcpSnoopRowStatus_Type = RowStatus
_RlIpDhcpSnoopRowStatus_Object = MibTableColumn
rlIpDhcpSnoopRowStatus = _RlIpDhcpSnoopRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 11, 1, 7),
    _RlIpDhcpSnoopRowStatus_Type()
)
rlIpDhcpSnoopRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopRowStatus.setStatus("current")
_RlIpDhcpSnoopEnableVlanTable_Object = MibTable
rlIpDhcpSnoopEnableVlanTable = _RlIpDhcpSnoopEnableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 12)
)
if mibBuilder.loadTexts:
    rlIpDhcpSnoopEnableVlanTable.setStatus("current")
_RlIpDhcpSnoopEnableVlanEntry_Object = MibTableRow
rlIpDhcpSnoopEnableVlanEntry = _RlIpDhcpSnoopEnableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 12, 1)
)
rlIpDhcpSnoopEnableVlanEntry.setIndexNames(
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpDhcpSnoopEnableVlanTag"),
)
if mibBuilder.loadTexts:
    rlIpDhcpSnoopEnableVlanEntry.setStatus("current")
_RlIpDhcpSnoopEnableVlanTag_Type = VlanId
_RlIpDhcpSnoopEnableVlanTag_Object = MibTableColumn
rlIpDhcpSnoopEnableVlanTag = _RlIpDhcpSnoopEnableVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 12, 1, 1),
    _RlIpDhcpSnoopEnableVlanTag_Type()
)
rlIpDhcpSnoopEnableVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopEnableVlanTag.setStatus("current")
_RlIpDhcpSnoopEnableVlanRowStatus_Type = RowStatus
_RlIpDhcpSnoopEnableVlanRowStatus_Object = MibTableColumn
rlIpDhcpSnoopEnableVlanRowStatus = _RlIpDhcpSnoopEnableVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 12, 1, 2),
    _RlIpDhcpSnoopEnableVlanRowStatus_Type()
)
rlIpDhcpSnoopEnableVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopEnableVlanRowStatus.setStatus("current")
_RlIpDhcpSnoopTrustedPortTable_Object = MibTable
rlIpDhcpSnoopTrustedPortTable = _RlIpDhcpSnoopTrustedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 13)
)
if mibBuilder.loadTexts:
    rlIpDhcpSnoopTrustedPortTable.setStatus("current")
_RlIpDhcpSnoopTrustedPortEntry_Object = MibTableRow
rlIpDhcpSnoopTrustedPortEntry = _RlIpDhcpSnoopTrustedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 13, 1)
)
rlIpDhcpSnoopTrustedPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlIpDhcpSnoopTrustedPortEntry.setStatus("current")
_RlIpDhcpSnoopTrustedPortRowStatus_Type = RowStatus
_RlIpDhcpSnoopTrustedPortRowStatus_Object = MibTableColumn
rlIpDhcpSnoopTrustedPortRowStatus = _RlIpDhcpSnoopTrustedPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 1, 13, 1, 2),
    _RlIpDhcpSnoopTrustedPortRowStatus_Type()
)
rlIpDhcpSnoopTrustedPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpDhcpSnoopTrustedPortRowStatus.setStatus("current")
_RlIpSourceGuard_ObjectIdentity = ObjectIdentity
rlIpSourceGuard = _RlIpSourceGuard_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2)
)
_RlIpSourceGuardMibVersion_Type = Integer32
_RlIpSourceGuardMibVersion_Object = MibScalar
rlIpSourceGuardMibVersion = _RlIpSourceGuardMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 1),
    _RlIpSourceGuardMibVersion_Type()
)
rlIpSourceGuardMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpSourceGuardMibVersion.setStatus("current")


class _RlIpSourceGuardEnable_Type(Integer32):
    """Custom type rlIpSourceGuardEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlIpSourceGuardEnable_Type.__name__ = "Integer32"
_RlIpSourceGuardEnable_Object = MibScalar
rlIpSourceGuardEnable = _RlIpSourceGuardEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 2),
    _RlIpSourceGuardEnable_Type()
)
rlIpSourceGuardEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpSourceGuardEnable.setStatus("current")


class _RlIpSourceGuardRetryToInsert_Type(Integer32):
    """Custom type rlIpSourceGuardRetryToInsert based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("retryToInsertNow", 1))
    )


_RlIpSourceGuardRetryToInsert_Type.__name__ = "Integer32"
_RlIpSourceGuardRetryToInsert_Object = MibScalar
rlIpSourceGuardRetryToInsert = _RlIpSourceGuardRetryToInsert_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 3),
    _RlIpSourceGuardRetryToInsert_Type()
)
rlIpSourceGuardRetryToInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpSourceGuardRetryToInsert.setStatus("current")


class _RlIpSourceGuardRetryTime_Type(Integer32):
    """Custom type rlIpSourceGuardRetryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_RlIpSourceGuardRetryTime_Type.__name__ = "Integer32"
_RlIpSourceGuardRetryTime_Object = MibScalar
rlIpSourceGuardRetryTime = _RlIpSourceGuardRetryTime_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 4),
    _RlIpSourceGuardRetryTime_Type()
)
rlIpSourceGuardRetryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpSourceGuardRetryTime.setStatus("current")
_RlIpSourceGuardPortTable_Object = MibTable
rlIpSourceGuardPortTable = _RlIpSourceGuardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 5)
)
if mibBuilder.loadTexts:
    rlIpSourceGuardPortTable.setStatus("current")
_RlIpSourceGuardPortEntry_Object = MibTableRow
rlIpSourceGuardPortEntry = _RlIpSourceGuardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 5, 1)
)
rlIpSourceGuardPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlIpSourceGuardPortEntry.setStatus("current")
_RlIpSourceGuardPortRowStatus_Type = RowStatus
_RlIpSourceGuardPortRowStatus_Object = MibTableColumn
rlIpSourceGuardPortRowStatus = _RlIpSourceGuardPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 5, 1, 2),
    _RlIpSourceGuardPortRowStatus_Type()
)
rlIpSourceGuardPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpSourceGuardPortRowStatus.setStatus("current")
_RlIpSourceGuardTable_Object = MibTable
rlIpSourceGuardTable = _RlIpSourceGuardTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 6)
)
if mibBuilder.loadTexts:
    rlIpSourceGuardTable.setStatus("current")
_RlIpSourceGuardEntry_Object = MibTableRow
rlIpSourceGuardEntry = _RlIpSourceGuardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 6, 1)
)
rlIpSourceGuardEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpSourceGuardIPAddress"),
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpSourceGuardVLANTag"),
)
if mibBuilder.loadTexts:
    rlIpSourceGuardEntry.setStatus("current")
_RlIpSourceGuardIPAddress_Type = IpAddress
_RlIpSourceGuardIPAddress_Object = MibTableColumn
rlIpSourceGuardIPAddress = _RlIpSourceGuardIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 6, 1, 1),
    _RlIpSourceGuardIPAddress_Type()
)
rlIpSourceGuardIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpSourceGuardIPAddress.setStatus("current")
_RlIpSourceGuardVLANTag_Type = VlanId
_RlIpSourceGuardVLANTag_Object = MibTableColumn
rlIpSourceGuardVLANTag = _RlIpSourceGuardVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 6, 1, 2),
    _RlIpSourceGuardVLANTag_Type()
)
rlIpSourceGuardVLANTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpSourceGuardVLANTag.setStatus("current")
_RlIpSourceGuardMACAddress_Type = MacAddress
_RlIpSourceGuardMACAddress_Object = MibTableColumn
rlIpSourceGuardMACAddress = _RlIpSourceGuardMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 6, 1, 3),
    _RlIpSourceGuardMACAddress_Type()
)
rlIpSourceGuardMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpSourceGuardMACAddress.setStatus("current")
_RlIpSourceGuardType_Type = RlIpSourceGuardType
_RlIpSourceGuardType_Object = MibTableColumn
rlIpSourceGuardType = _RlIpSourceGuardType_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 6, 1, 4),
    _RlIpSourceGuardType_Type()
)
rlIpSourceGuardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpSourceGuardType.setStatus("current")
_RlIpSourceGuardStatus_Type = RlIpSourceGuardStatus
_RlIpSourceGuardStatus_Object = MibTableColumn
rlIpSourceGuardStatus = _RlIpSourceGuardStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 6, 1, 5),
    _RlIpSourceGuardStatus_Type()
)
rlIpSourceGuardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpSourceGuardStatus.setStatus("current")
_RlIpSourceGuardFailReason_Type = RlIpSourceGuardFailReason
_RlIpSourceGuardFailReason_Object = MibTableColumn
rlIpSourceGuardFailReason = _RlIpSourceGuardFailReason_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 6, 1, 6),
    _RlIpSourceGuardFailReason_Type()
)
rlIpSourceGuardFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpSourceGuardFailReason.setStatus("current")
_RlIpSourceGuardPermittedRuleCounterTable_Object = MibTable
rlIpSourceGuardPermittedRuleCounterTable = _RlIpSourceGuardPermittedRuleCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 7)
)
if mibBuilder.loadTexts:
    rlIpSourceGuardPermittedRuleCounterTable.setStatus("current")
_RlIpSourceGuardPermittedRuleCounterEntry_Object = MibTableRow
rlIpSourceGuardPermittedRuleCounterEntry = _RlIpSourceGuardPermittedRuleCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 7, 1)
)
rlIpSourceGuardPermittedRuleCounterEntry.setIndexNames(
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpSourceGuardPermittedRuleCounterVLANTag"),
)
if mibBuilder.loadTexts:
    rlIpSourceGuardPermittedRuleCounterEntry.setStatus("current")
_RlIpSourceGuardPermittedRuleCounterVLANTag_Type = VlanId
_RlIpSourceGuardPermittedRuleCounterVLANTag_Object = MibTableColumn
rlIpSourceGuardPermittedRuleCounterVLANTag = _RlIpSourceGuardPermittedRuleCounterVLANTag_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 7, 1, 1),
    _RlIpSourceGuardPermittedRuleCounterVLANTag_Type()
)
rlIpSourceGuardPermittedRuleCounterVLANTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpSourceGuardPermittedRuleCounterVLANTag.setStatus("current")
_RlIpSourceGuardPermittedRuleCounterNumOfStaticRules_Type = Counter32
_RlIpSourceGuardPermittedRuleCounterNumOfStaticRules_Object = MibTableColumn
rlIpSourceGuardPermittedRuleCounterNumOfStaticRules = _RlIpSourceGuardPermittedRuleCounterNumOfStaticRules_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 7, 1, 2),
    _RlIpSourceGuardPermittedRuleCounterNumOfStaticRules_Type()
)
rlIpSourceGuardPermittedRuleCounterNumOfStaticRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpSourceGuardPermittedRuleCounterNumOfStaticRules.setStatus("current")
_RlIpSourceGuardPermittedRuleCounterNumOfDhcpRules_Type = Counter32
_RlIpSourceGuardPermittedRuleCounterNumOfDhcpRules_Object = MibTableColumn
rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules = _RlIpSourceGuardPermittedRuleCounterNumOfDhcpRules_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 2, 7, 1, 3),
    _RlIpSourceGuardPermittedRuleCounterNumOfDhcpRules_Type()
)
rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules.setStatus("current")
_RlIpArpInspect_ObjectIdentity = ObjectIdentity
rlIpArpInspect = _RlIpArpInspect_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3)
)
_RlIpArpInspectMibVersion_Type = Integer32
_RlIpArpInspectMibVersion_Object = MibScalar
rlIpArpInspectMibVersion = _RlIpArpInspectMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 1),
    _RlIpArpInspectMibVersion_Type()
)
rlIpArpInspectMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpArpInspectMibVersion.setStatus("current")


class _RlIpArpInspectEnable_Type(Integer32):
    """Custom type rlIpArpInspectEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlIpArpInspectEnable_Type.__name__ = "Integer32"
_RlIpArpInspectEnable_Object = MibScalar
rlIpArpInspectEnable = _RlIpArpInspectEnable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 2),
    _RlIpArpInspectEnable_Type()
)
rlIpArpInspectEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectEnable.setStatus("current")
_RlIpArpInspectLogInterval_Type = Unsigned32
_RlIpArpInspectLogInterval_Object = MibScalar
rlIpArpInspectLogInterval = _RlIpArpInspectLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 3),
    _RlIpArpInspectLogInterval_Type()
)
rlIpArpInspectLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectLogInterval.setStatus("current")


class _RlIpArpInspectValidation_Type(Integer32):
    """Custom type rlIpArpInspectValidation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_RlIpArpInspectValidation_Type.__name__ = "Integer32"
_RlIpArpInspectValidation_Object = MibScalar
rlIpArpInspectValidation = _RlIpArpInspectValidation_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 4),
    _RlIpArpInspectValidation_Type()
)
rlIpArpInspectValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectValidation.setStatus("current")
_RlIpArpInspectListTable_Object = MibTable
rlIpArpInspectListTable = _RlIpArpInspectListTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 5)
)
if mibBuilder.loadTexts:
    rlIpArpInspectListTable.setStatus("current")
_RlIpArpInspectListEntry_Object = MibTableRow
rlIpArpInspectListEntry = _RlIpArpInspectListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 5, 1)
)
rlIpArpInspectListEntry.setIndexNames(
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpArpInspectListName"),
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpArpInspectListIPAddress"),
)
if mibBuilder.loadTexts:
    rlIpArpInspectListEntry.setStatus("current")
_RlIpArpInspectListName_Type = RlIpArpInspectListNameType
_RlIpArpInspectListName_Object = MibTableColumn
rlIpArpInspectListName = _RlIpArpInspectListName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 5, 1, 1),
    _RlIpArpInspectListName_Type()
)
rlIpArpInspectListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpArpInspectListName.setStatus("current")
_RlIpArpInspectListIPAddress_Type = IpAddress
_RlIpArpInspectListIPAddress_Object = MibTableColumn
rlIpArpInspectListIPAddress = _RlIpArpInspectListIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 5, 1, 2),
    _RlIpArpInspectListIPAddress_Type()
)
rlIpArpInspectListIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpArpInspectListIPAddress.setStatus("current")
_RlIpArpInspectListMACAddress_Type = MacAddress
_RlIpArpInspectListMACAddress_Object = MibTableColumn
rlIpArpInspectListMACAddress = _RlIpArpInspectListMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 5, 1, 3),
    _RlIpArpInspectListMACAddress_Type()
)
rlIpArpInspectListMACAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectListMACAddress.setStatus("current")
_RlIpArpInspectListRowStatus_Type = RowStatus
_RlIpArpInspectListRowStatus_Object = MibTableColumn
rlIpArpInspectListRowStatus = _RlIpArpInspectListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 5, 1, 4),
    _RlIpArpInspectListRowStatus_Type()
)
rlIpArpInspectListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectListRowStatus.setStatus("current")
_RlIpArpInspectEnableVlanTable_Object = MibTable
rlIpArpInspectEnableVlanTable = _RlIpArpInspectEnableVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 6)
)
if mibBuilder.loadTexts:
    rlIpArpInspectEnableVlanTable.setStatus("current")
_RlIpArpInspectEnableVlanEntry_Object = MibTableRow
rlIpArpInspectEnableVlanEntry = _RlIpArpInspectEnableVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 6, 1)
)
rlIpArpInspectEnableVlanEntry.setIndexNames(
    (0, "LINKSYS-BRIDGE-SECURITY", "rlIpArpInspectEnableVlanTag"),
)
if mibBuilder.loadTexts:
    rlIpArpInspectEnableVlanEntry.setStatus("current")
_RlIpArpInspectEnableVlanTag_Type = VlanId
_RlIpArpInspectEnableVlanTag_Object = MibTableColumn
rlIpArpInspectEnableVlanTag = _RlIpArpInspectEnableVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 6, 1, 1),
    _RlIpArpInspectEnableVlanTag_Type()
)
rlIpArpInspectEnableVlanTag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlIpArpInspectEnableVlanTag.setStatus("current")
_RlIpArpInspectAssignedListName_Type = RlIpArpInspectListNameType
_RlIpArpInspectAssignedListName_Object = MibTableColumn
rlIpArpInspectAssignedListName = _RlIpArpInspectAssignedListName_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 6, 1, 2),
    _RlIpArpInspectAssignedListName_Type()
)
rlIpArpInspectAssignedListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectAssignedListName.setStatus("current")
_RlIpArpInspectEnableVlanRowStatus_Type = RowStatus
_RlIpArpInspectEnableVlanRowStatus_Object = MibTableColumn
rlIpArpInspectEnableVlanRowStatus = _RlIpArpInspectEnableVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 6, 1, 3),
    _RlIpArpInspectEnableVlanRowStatus_Type()
)
rlIpArpInspectEnableVlanRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectEnableVlanRowStatus.setStatus("current")
_RlIpArpInspectVlanNumOfArpForwarded_Type = Counter32
_RlIpArpInspectVlanNumOfArpForwarded_Object = MibTableColumn
rlIpArpInspectVlanNumOfArpForwarded = _RlIpArpInspectVlanNumOfArpForwarded_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 6, 1, 4),
    _RlIpArpInspectVlanNumOfArpForwarded_Type()
)
rlIpArpInspectVlanNumOfArpForwarded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpArpInspectVlanNumOfArpForwarded.setStatus("current")
_RlIpArpInspectVlanNumOfArpDropped_Type = Counter32
_RlIpArpInspectVlanNumOfArpDropped_Object = MibTableColumn
rlIpArpInspectVlanNumOfArpDropped = _RlIpArpInspectVlanNumOfArpDropped_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 6, 1, 5),
    _RlIpArpInspectVlanNumOfArpDropped_Type()
)
rlIpArpInspectVlanNumOfArpDropped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpArpInspectVlanNumOfArpDropped.setStatus("current")
_RlIpArpInspectVlanNumOfArpMismatched_Type = Counter32
_RlIpArpInspectVlanNumOfArpMismatched_Object = MibTableColumn
rlIpArpInspectVlanNumOfArpMismatched = _RlIpArpInspectVlanNumOfArpMismatched_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 6, 1, 6),
    _RlIpArpInspectVlanNumOfArpMismatched_Type()
)
rlIpArpInspectVlanNumOfArpMismatched.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlIpArpInspectVlanNumOfArpMismatched.setStatus("current")


class _RlIpArpInspectVlanClearCountersAction_Type(TruthValue):
    """Custom type rlIpArpInspectVlanClearCountersAction based on TruthValue"""
    defaultValue = 2


_RlIpArpInspectVlanClearCountersAction_Type.__name__ = "TruthValue"
_RlIpArpInspectVlanClearCountersAction_Object = MibTableColumn
rlIpArpInspectVlanClearCountersAction = _RlIpArpInspectVlanClearCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 6, 1, 7),
    _RlIpArpInspectVlanClearCountersAction_Type()
)
rlIpArpInspectVlanClearCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectVlanClearCountersAction.setStatus("current")
_RlIpArpInspectTrustedPortTable_Object = MibTable
rlIpArpInspectTrustedPortTable = _RlIpArpInspectTrustedPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 7)
)
if mibBuilder.loadTexts:
    rlIpArpInspectTrustedPortTable.setStatus("current")
_RlIpArpInspectTrustedPortEntry_Object = MibTableRow
rlIpArpInspectTrustedPortEntry = _RlIpArpInspectTrustedPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 7, 1)
)
rlIpArpInspectTrustedPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlIpArpInspectTrustedPortEntry.setStatus("current")
_RlIpArpInspectTrustedPortRowStatus_Type = RowStatus
_RlIpArpInspectTrustedPortRowStatus_Object = MibTableColumn
rlIpArpInspectTrustedPortRowStatus = _RlIpArpInspectTrustedPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 7, 1, 2),
    _RlIpArpInspectTrustedPortRowStatus_Type()
)
rlIpArpInspectTrustedPortRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectTrustedPortRowStatus.setStatus("current")


class _RlIpArpInspectClearCountersAction_Type(TruthValue):
    """Custom type rlIpArpInspectClearCountersAction based on TruthValue"""
    defaultValue = 2


_RlIpArpInspectClearCountersAction_Type.__name__ = "TruthValue"
_RlIpArpInspectClearCountersAction_Object = MibScalar
rlIpArpInspectClearCountersAction = _RlIpArpInspectClearCountersAction_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 3, 8),
    _RlIpArpInspectClearCountersAction_Type()
)
rlIpArpInspectClearCountersAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlIpArpInspectClearCountersAction.setStatus("current")
_RlProtocolFiltering_ObjectIdentity = ObjectIdentity
rlProtocolFiltering = _RlProtocolFiltering_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 4)
)
_RlProtocolFilteringTable_Object = MibTable
rlProtocolFilteringTable = _RlProtocolFilteringTable_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 4, 1)
)
if mibBuilder.loadTexts:
    rlProtocolFilteringTable.setStatus("current")
_RlProtocolFilteringEntry_Object = MibTableRow
rlProtocolFilteringEntry = _RlProtocolFilteringEntry_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 4, 1, 1)
)
rlProtocolFilteringEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    rlProtocolFilteringEntry.setStatus("current")
_RlProtocolFilteringList_Type = ProtocolFilteringMap
_RlProtocolFilteringList_Object = MibTableColumn
rlProtocolFilteringList = _RlProtocolFilteringList_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 4, 1, 1, 1),
    _RlProtocolFilteringList_Type()
)
rlProtocolFilteringList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtocolFilteringList.setStatus("current")
_RlProtocolFilteringRowStatus_Type = RowStatus
_RlProtocolFilteringRowStatus_Object = MibTableColumn
rlProtocolFilteringRowStatus = _RlProtocolFilteringRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3955, 1000, 201, 112, 4, 1, 1, 2),
    _RlProtocolFilteringRowStatus_Type()
)
rlProtocolFilteringRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlProtocolFilteringRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LINKSYS-BRIDGE-SECURITY",
    **{"RlIpDhcpSnoopType": RlIpDhcpSnoopType,
       "RlIpSourceGuardType": RlIpSourceGuardType,
       "RlIpSourceGuardStatus": RlIpSourceGuardStatus,
       "RlIpSourceGuardFailReason": RlIpSourceGuardFailReason,
       "RlIpArpInspectListNameType": RlIpArpInspectListNameType,
       "ProtocolFilteringMap": ProtocolFilteringMap,
       "rlBridgeSecurity": rlBridgeSecurity,
       "rlIpDhcpSnoop": rlIpDhcpSnoop,
       "rlIpDhcpSnoopMibVersion": rlIpDhcpSnoopMibVersion,
       "rlIpDhcpSnoopEnable": rlIpDhcpSnoopEnable,
       "rlIpDhcpSnoopFileEnable": rlIpDhcpSnoopFileEnable,
       "rlIpDhcpSnoopClearAction": rlIpDhcpSnoopClearAction,
       "rlIpDhcpSnoopFileUpdateTime": rlIpDhcpSnoopFileUpdateTime,
       "rlIpDhcpSnoopVerifyMacAddress": rlIpDhcpSnoopVerifyMacAddress,
       "rlIpDhcpSnoopCurrentEntiresNumber": rlIpDhcpSnoopCurrentEntiresNumber,
       "rlIpDhcpOpt82InsertionEnable": rlIpDhcpOpt82InsertionEnable,
       "rlIpDhcpOpt82RxOnUntrustedEnable": rlIpDhcpOpt82RxOnUntrustedEnable,
       "rlIpDhcpSnoopStaticTable": rlIpDhcpSnoopStaticTable,
       "rlIpDhcpSnoopStaticEntry": rlIpDhcpSnoopStaticEntry,
       "rlIpDhcpSnoopStaticVLANTag": rlIpDhcpSnoopStaticVLANTag,
       "rlIpDhcpSnoopStaticMACAddress": rlIpDhcpSnoopStaticMACAddress,
       "rlIpDhcpSnoopStaticIPAddress": rlIpDhcpSnoopStaticIPAddress,
       "rlIpDhcpSnoopStaticPortInterface": rlIpDhcpSnoopStaticPortInterface,
       "rlIpDhcpSnoopStaticRowStatus": rlIpDhcpSnoopStaticRowStatus,
       "rlIpDhcpSnoopTable": rlIpDhcpSnoopTable,
       "rlIpDhcpSnoopEntry": rlIpDhcpSnoopEntry,
       "rlIpDhcpSnoopVLANTag": rlIpDhcpSnoopVLANTag,
       "rlIpDhcpSnoopMACAddress": rlIpDhcpSnoopMACAddress,
       "rlIpDhcpSnoopType": rlIpDhcpSnoopType,
       "rlIpDhcpSnoopLeaseTime": rlIpDhcpSnoopLeaseTime,
       "rlIpDhcpSnoopIPAddress": rlIpDhcpSnoopIPAddress,
       "rlIpDhcpSnoopPortInterface": rlIpDhcpSnoopPortInterface,
       "rlIpDhcpSnoopRowStatus": rlIpDhcpSnoopRowStatus,
       "rlIpDhcpSnoopEnableVlanTable": rlIpDhcpSnoopEnableVlanTable,
       "rlIpDhcpSnoopEnableVlanEntry": rlIpDhcpSnoopEnableVlanEntry,
       "rlIpDhcpSnoopEnableVlanTag": rlIpDhcpSnoopEnableVlanTag,
       "rlIpDhcpSnoopEnableVlanRowStatus": rlIpDhcpSnoopEnableVlanRowStatus,
       "rlIpDhcpSnoopTrustedPortTable": rlIpDhcpSnoopTrustedPortTable,
       "rlIpDhcpSnoopTrustedPortEntry": rlIpDhcpSnoopTrustedPortEntry,
       "rlIpDhcpSnoopTrustedPortRowStatus": rlIpDhcpSnoopTrustedPortRowStatus,
       "rlIpSourceGuard": rlIpSourceGuard,
       "rlIpSourceGuardMibVersion": rlIpSourceGuardMibVersion,
       "rlIpSourceGuardEnable": rlIpSourceGuardEnable,
       "rlIpSourceGuardRetryToInsert": rlIpSourceGuardRetryToInsert,
       "rlIpSourceGuardRetryTime": rlIpSourceGuardRetryTime,
       "rlIpSourceGuardPortTable": rlIpSourceGuardPortTable,
       "rlIpSourceGuardPortEntry": rlIpSourceGuardPortEntry,
       "rlIpSourceGuardPortRowStatus": rlIpSourceGuardPortRowStatus,
       "rlIpSourceGuardTable": rlIpSourceGuardTable,
       "rlIpSourceGuardEntry": rlIpSourceGuardEntry,
       "rlIpSourceGuardIPAddress": rlIpSourceGuardIPAddress,
       "rlIpSourceGuardVLANTag": rlIpSourceGuardVLANTag,
       "rlIpSourceGuardMACAddress": rlIpSourceGuardMACAddress,
       "rlIpSourceGuardType": rlIpSourceGuardType,
       "rlIpSourceGuardStatus": rlIpSourceGuardStatus,
       "rlIpSourceGuardFailReason": rlIpSourceGuardFailReason,
       "rlIpSourceGuardPermittedRuleCounterTable": rlIpSourceGuardPermittedRuleCounterTable,
       "rlIpSourceGuardPermittedRuleCounterEntry": rlIpSourceGuardPermittedRuleCounterEntry,
       "rlIpSourceGuardPermittedRuleCounterVLANTag": rlIpSourceGuardPermittedRuleCounterVLANTag,
       "rlIpSourceGuardPermittedRuleCounterNumOfStaticRules": rlIpSourceGuardPermittedRuleCounterNumOfStaticRules,
       "rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules": rlIpSourceGuardPermittedRuleCounterNumOfDhcpRules,
       "rlIpArpInspect": rlIpArpInspect,
       "rlIpArpInspectMibVersion": rlIpArpInspectMibVersion,
       "rlIpArpInspectEnable": rlIpArpInspectEnable,
       "rlIpArpInspectLogInterval": rlIpArpInspectLogInterval,
       "rlIpArpInspectValidation": rlIpArpInspectValidation,
       "rlIpArpInspectListTable": rlIpArpInspectListTable,
       "rlIpArpInspectListEntry": rlIpArpInspectListEntry,
       "rlIpArpInspectListName": rlIpArpInspectListName,
       "rlIpArpInspectListIPAddress": rlIpArpInspectListIPAddress,
       "rlIpArpInspectListMACAddress": rlIpArpInspectListMACAddress,
       "rlIpArpInspectListRowStatus": rlIpArpInspectListRowStatus,
       "rlIpArpInspectEnableVlanTable": rlIpArpInspectEnableVlanTable,
       "rlIpArpInspectEnableVlanEntry": rlIpArpInspectEnableVlanEntry,
       "rlIpArpInspectEnableVlanTag": rlIpArpInspectEnableVlanTag,
       "rlIpArpInspectAssignedListName": rlIpArpInspectAssignedListName,
       "rlIpArpInspectEnableVlanRowStatus": rlIpArpInspectEnableVlanRowStatus,
       "rlIpArpInspectVlanNumOfArpForwarded": rlIpArpInspectVlanNumOfArpForwarded,
       "rlIpArpInspectVlanNumOfArpDropped": rlIpArpInspectVlanNumOfArpDropped,
       "rlIpArpInspectVlanNumOfArpMismatched": rlIpArpInspectVlanNumOfArpMismatched,
       "rlIpArpInspectVlanClearCountersAction": rlIpArpInspectVlanClearCountersAction,
       "rlIpArpInspectTrustedPortTable": rlIpArpInspectTrustedPortTable,
       "rlIpArpInspectTrustedPortEntry": rlIpArpInspectTrustedPortEntry,
       "rlIpArpInspectTrustedPortRowStatus": rlIpArpInspectTrustedPortRowStatus,
       "rlIpArpInspectClearCountersAction": rlIpArpInspectClearCountersAction,
       "rlProtocolFiltering": rlProtocolFiltering,
       "rlProtocolFilteringTable": rlProtocolFilteringTable,
       "rlProtocolFilteringEntry": rlProtocolFilteringEntry,
       "rlProtocolFilteringList": rlProtocolFilteringList,
       "rlProtocolFilteringRowStatus": rlProtocolFilteringRowStatus}
)
