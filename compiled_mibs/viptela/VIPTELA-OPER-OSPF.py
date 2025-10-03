# SNMP MIB module (VIPTELA-OPER-OSPF) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\viptela\VIPTELA-OPER-OSPF
# Produced by pysmi-1.6.2 at Thu Oct  2 12:34:05 2025
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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(viptela,) = mibBuilder.importSymbols(
    "VIPTELA-GLOBAL",
    "viptela")


# MODULE-IDENTITY

viptela_oper_ospf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 13)
)
if mibBuilder.loadTexts:
    viptela_oper_ospf.setRevisions(
        ("2016-08-10 00:00",
         "2016-08-01 00:00",
         "2016-06-09 00:00",
         "2016-04-22 00:00",
         "2016-03-15 00:00",
         "2016-01-30 00:00",
         "2015-12-28 00:00",
         "2015-12-01 00:00",
         "2015-10-31 00:00",
         "2015-09-27 00:00",
         "2015-09-01 00:00",
         "2015-07-01 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class UnsignedByte(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class ConfdString(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class Ipv4Prefix(TextualConvention, OctetString):
    status = "current"
    displayHint = "1d.1d.1d.1d/1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5



class String(TextualConvention, OctetString):
    status = "current"
    displayHint = "1t"


class OspfNeighborOptions(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("t", 0),
          ("e", 1),
          ("mc", 2),
          ("np", 3),
          ("ea", 4),
          ("dc", 5),
          ("o", 6),
          ("dn", 7))
    )


class OspfDbRlsaFlags(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("abr", 0),
          ("asbr", 1),
          ("vl", 2),
          ("type-7", 4),
          ("shortcut-abr", 5))
    )


# MIB Managed Objects in the order of their OIDs

_Ospf_ObjectIdentity = ObjectIdentity
ospf = _Ospf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41916, 13, 1)
)
_OspfNeighborTable_Object = MibTable
ospfNeighborTable = _OspfNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2)
)
if mibBuilder.loadTexts:
    ospfNeighborTable.setStatus("current")
_OspfNeighborEntry_Object = MibTableRow
ospfNeighborEntry = _OspfNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1)
)
ospfNeighborEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfNeighborVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfNeighborSource"),
    (0, "VIPTELA-OPER-OSPF", "ospfNeighborIfIndex"),
)
if mibBuilder.loadTexts:
    ospfNeighborEntry.setStatus("current")


class _OspfNeighborVpnId_Type(Unsigned32):
    """Custom type ospfNeighborVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OspfNeighborVpnId_Type.__name__ = "Unsigned32"
_OspfNeighborVpnId_Object = MibTableColumn
ospfNeighborVpnId = _OspfNeighborVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 1),
    _OspfNeighborVpnId_Type()
)
ospfNeighborVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfNeighborVpnId.setStatus("current")
_OspfNeighborSource_Type = IpAddress
_OspfNeighborSource_Object = MibTableColumn
ospfNeighborSource = _OspfNeighborSource_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 2),
    _OspfNeighborSource_Type()
)
ospfNeighborSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfNeighborSource.setStatus("current")
_OspfNeighborIfIndex_Type = Unsigned32
_OspfNeighborIfIndex_Object = MibTableColumn
ospfNeighborIfIndex = _OspfNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 3),
    _OspfNeighborIfIndex_Type()
)
ospfNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfNeighborIfIndex.setStatus("current")


class _OspfNeighborIfName_Type(String):
    """Custom type ospfNeighborIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OspfNeighborIfName_Type.__name__ = "String"
_OspfNeighborIfName_Object = MibTableColumn
ospfNeighborIfName = _OspfNeighborIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 4),
    _OspfNeighborIfName_Type()
)
ospfNeighborIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborIfName.setStatus("current")
_OspfNeighborRouterId_Type = IpAddress
_OspfNeighborRouterId_Object = MibTableColumn
ospfNeighborRouterId = _OspfNeighborRouterId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 5),
    _OspfNeighborRouterId_Type()
)
ospfNeighborRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborRouterId.setStatus("current")
_OspfNeighborIfAddress_Type = IpAddress
_OspfNeighborIfAddress_Object = MibTableColumn
ospfNeighborIfAddress = _OspfNeighborIfAddress_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 6),
    _OspfNeighborIfAddress_Type()
)
ospfNeighborIfAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborIfAddress.setStatus("current")
_OspfNeighborArea_Type = Unsigned32
_OspfNeighborArea_Object = MibTableColumn
ospfNeighborArea = _OspfNeighborArea_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 7),
    _OspfNeighborArea_Type()
)
ospfNeighborArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborArea.setStatus("current")


class _OspfNeighborAreaType_Type(Integer32):
    """Custom type ospfNeighborAreaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("regular", 0),
          ("stub", 1),
          ("nssa", 2))
    )


_OspfNeighborAreaType_Type.__name__ = "Integer32"
_OspfNeighborAreaType_Object = MibTableColumn
ospfNeighborAreaType = _OspfNeighborAreaType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 8),
    _OspfNeighborAreaType_Type()
)
ospfNeighborAreaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborAreaType.setStatus("current")


class _OspfNeighborNeighborState_Type(Integer32):
    """Custom type ospfNeighborNeighborState based on Integer32"""
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
        *(("full", 0),
          ("deleted", 1),
          ("depend-upon", 2),
          ("down", 3),
          ("attempt", 4),
          ("init", 5),
          ("two-way", 6),
          ("exstart", 7),
          ("exchange", 8),
          ("loading", 9))
    )


_OspfNeighborNeighborState_Type.__name__ = "Integer32"
_OspfNeighborNeighborState_Object = MibTableColumn
ospfNeighborNeighborState = _OspfNeighborNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 9),
    _OspfNeighborNeighborState_Type()
)
ospfNeighborNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborNeighborState.setStatus("current")


class _OspfNeighborInterfaceState_Type(Integer32):
    """Custom type ospfNeighborInterfaceState based on Integer32"""
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
        *(("if-depend-upon", 0),
          ("if-down", 1),
          ("if-loopback", 2),
          ("if-waiting", 3),
          ("if-point-to-point", 4),
          ("if-dr-other", 5),
          ("if-backup", 6),
          ("if-dr", 7))
    )


_OspfNeighborInterfaceState_Type.__name__ = "Integer32"
_OspfNeighborInterfaceState_Object = MibTableColumn
ospfNeighborInterfaceState = _OspfNeighborInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 10),
    _OspfNeighborInterfaceState_Type()
)
ospfNeighborInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborInterfaceState.setStatus("current")
_OspfNeighborPriority_Type = Unsigned32
_OspfNeighborPriority_Object = MibTableColumn
ospfNeighborPriority = _OspfNeighborPriority_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 11),
    _OspfNeighborPriority_Type()
)
ospfNeighborPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborPriority.setStatus("current")
_OspfNeighborStateChanges_Type = Unsigned32
_OspfNeighborStateChanges_Object = MibTableColumn
ospfNeighborStateChanges = _OspfNeighborStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 12),
    _OspfNeighborStateChanges_Type()
)
ospfNeighborStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborStateChanges.setStatus("current")
_OspfNeighborProgressiveChangeTime_Type = Unsigned32
_OspfNeighborProgressiveChangeTime_Object = MibTableColumn
ospfNeighborProgressiveChangeTime = _OspfNeighborProgressiveChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 13),
    _OspfNeighborProgressiveChangeTime_Type()
)
ospfNeighborProgressiveChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborProgressiveChangeTime.setStatus("current")
_OspfNeighborRegressiveChangeTime_Type = Unsigned32
_OspfNeighborRegressiveChangeTime_Object = MibTableColumn
ospfNeighborRegressiveChangeTime = _OspfNeighborRegressiveChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 14),
    _OspfNeighborRegressiveChangeTime_Type()
)
ospfNeighborRegressiveChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborRegressiveChangeTime.setStatus("current")


class _OspfNeighborRegressiveChangeReason_Type(String):
    """Custom type ospfNeighborRegressiveChangeReason based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OspfNeighborRegressiveChangeReason_Type.__name__ = "String"
_OspfNeighborRegressiveChangeReason_Object = MibTableColumn
ospfNeighborRegressiveChangeReason = _OspfNeighborRegressiveChangeReason_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 15),
    _OspfNeighborRegressiveChangeReason_Type()
)
ospfNeighborRegressiveChangeReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborRegressiveChangeReason.setStatus("current")
_OspfNeighborDesignatedRouterId_Type = IpAddress
_OspfNeighborDesignatedRouterId_Object = MibTableColumn
ospfNeighborDesignatedRouterId = _OspfNeighborDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 16),
    _OspfNeighborDesignatedRouterId_Type()
)
ospfNeighborDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborDesignatedRouterId.setStatus("current")
_OspfNeighborBackupDesignatedRouterId_Type = IpAddress
_OspfNeighborBackupDesignatedRouterId_Object = MibTableColumn
ospfNeighborBackupDesignatedRouterId = _OspfNeighborBackupDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 17),
    _OspfNeighborBackupDesignatedRouterId_Type()
)
ospfNeighborBackupDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborBackupDesignatedRouterId.setStatus("current")
_OspfNeighborDeadTimer_Type = Unsigned32
_OspfNeighborDeadTimer_Object = MibTableColumn
ospfNeighborDeadTimer = _OspfNeighborDeadTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 18),
    _OspfNeighborDeadTimer_Type()
)
ospfNeighborDeadTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborDeadTimer.setStatus("current")
_OspfNeighborDbSummaryList_Type = Unsigned32
_OspfNeighborDbSummaryList_Object = MibTableColumn
ospfNeighborDbSummaryList = _OspfNeighborDbSummaryList_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 19),
    _OspfNeighborDbSummaryList_Type()
)
ospfNeighborDbSummaryList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborDbSummaryList.setStatus("current")
_OspfNeighborLinkStateReqList_Type = Counter64
_OspfNeighborLinkStateReqList_Object = MibTableColumn
ospfNeighborLinkStateReqList = _OspfNeighborLinkStateReqList_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 20),
    _OspfNeighborLinkStateReqList_Type()
)
ospfNeighborLinkStateReqList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborLinkStateReqList.setStatus("current")
_OspfNeighborLinkStateRetransList_Type = Counter64
_OspfNeighborLinkStateRetransList_Object = MibTableColumn
ospfNeighborLinkStateRetransList = _OspfNeighborLinkStateRetransList_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 21),
    _OspfNeighborLinkStateRetransList_Type()
)
ospfNeighborLinkStateRetransList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborLinkStateRetransList.setStatus("current")
_OspfNeighborOptions_Type = OspfNeighborOptions
_OspfNeighborOptions_Object = MibTableColumn
ospfNeighborOptions = _OspfNeighborOptions_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 2, 1, 22),
    _OspfNeighborOptions_Type()
)
ospfNeighborOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfNeighborOptions.setStatus("current")
_OspfInterfaceTable_Object = MibTable
ospfInterfaceTable = _OspfInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3)
)
if mibBuilder.loadTexts:
    ospfInterfaceTable.setStatus("current")
_OspfInterfaceEntry_Object = MibTableRow
ospfInterfaceEntry = _OspfInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1)
)
ospfInterfaceEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfInterfaceVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfInterfaceIfAddr"),
    (0, "VIPTELA-OPER-OSPF", "ospfInterfaceIfIndex"),
)
if mibBuilder.loadTexts:
    ospfInterfaceEntry.setStatus("current")


class _OspfInterfaceVpnId_Type(Unsigned32):
    """Custom type ospfInterfaceVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OspfInterfaceVpnId_Type.__name__ = "Unsigned32"
_OspfInterfaceVpnId_Object = MibTableColumn
ospfInterfaceVpnId = _OspfInterfaceVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 1),
    _OspfInterfaceVpnId_Type()
)
ospfInterfaceVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfInterfaceVpnId.setStatus("current")


class _OspfInterfaceIfAddr_Type(OctetString):
    """Custom type ospfInterfaceIfAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(5, 5),
    )
    fixed_length = 5


_OspfInterfaceIfAddr_Type.__name__ = "OctetString"
_OspfInterfaceIfAddr_Object = MibTableColumn
ospfInterfaceIfAddr = _OspfInterfaceIfAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 2),
    _OspfInterfaceIfAddr_Type()
)
ospfInterfaceIfAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfInterfaceIfAddr.setStatus("current")
_OspfInterfaceIfIndex_Type = Unsigned32
_OspfInterfaceIfIndex_Object = MibTableColumn
ospfInterfaceIfIndex = _OspfInterfaceIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 3),
    _OspfInterfaceIfIndex_Type()
)
ospfInterfaceIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfInterfaceIfIndex.setStatus("current")


class _OspfInterfaceIfName_Type(String):
    """Custom type ospfInterfaceIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OspfInterfaceIfName_Type.__name__ = "String"
_OspfInterfaceIfName_Object = MibTableColumn
ospfInterfaceIfName = _OspfInterfaceIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 4),
    _OspfInterfaceIfName_Type()
)
ospfInterfaceIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceIfName.setStatus("current")
_OspfInterfaceMtu_Type = Unsigned32
_OspfInterfaceMtu_Object = MibTableColumn
ospfInterfaceMtu = _OspfInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 5),
    _OspfInterfaceMtu_Type()
)
ospfInterfaceMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceMtu.setStatus("current")
_OspfInterfaceBandwidth_Type = Unsigned32
_OspfInterfaceBandwidth_Object = MibTableColumn
ospfInterfaceBandwidth = _OspfInterfaceBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 6),
    _OspfInterfaceBandwidth_Type()
)
ospfInterfaceBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceBandwidth.setStatus("current")
_OspfInterfaceBroadcastAddr_Type = IpAddress
_OspfInterfaceBroadcastAddr_Object = MibTableColumn
ospfInterfaceBroadcastAddr = _OspfInterfaceBroadcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 7),
    _OspfInterfaceBroadcastAddr_Type()
)
ospfInterfaceBroadcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceBroadcastAddr.setStatus("current")
_OspfInterfaceAreaAddr_Type = Unsigned32
_OspfInterfaceAreaAddr_Object = MibTableColumn
ospfInterfaceAreaAddr = _OspfInterfaceAreaAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 8),
    _OspfInterfaceAreaAddr_Type()
)
ospfInterfaceAreaAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceAreaAddr.setStatus("current")
_OspfInterfaceMtuMismatch_Type = TruthValue
_OspfInterfaceMtuMismatch_Object = MibTableColumn
ospfInterfaceMtuMismatch = _OspfInterfaceMtuMismatch_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 9),
    _OspfInterfaceMtuMismatch_Type()
)
ospfInterfaceMtuMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceMtuMismatch.setStatus("current")
_OspfInterfaceRouterId_Type = IpAddress
_OspfInterfaceRouterId_Object = MibTableColumn
ospfInterfaceRouterId = _OspfInterfaceRouterId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 10),
    _OspfInterfaceRouterId_Type()
)
ospfInterfaceRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceRouterId.setStatus("current")


class _OspfInterfaceIfType_Type(Integer32):
    """Custom type ospfInterfaceIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("point-to-point", 1),
          ("broadcast", 2),
          ("nbma", 3),
          ("point-to-multipoint", 4),
          ("loopback", 5))
    )


_OspfInterfaceIfType_Type.__name__ = "Integer32"
_OspfInterfaceIfType_Object = MibTableColumn
ospfInterfaceIfType = _OspfInterfaceIfType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 11),
    _OspfInterfaceIfType_Type()
)
ospfInterfaceIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceIfType.setStatus("current")
_OspfInterfaceCost_Type = Unsigned32
_OspfInterfaceCost_Object = MibTableColumn
ospfInterfaceCost = _OspfInterfaceCost_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 12),
    _OspfInterfaceCost_Type()
)
ospfInterfaceCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceCost.setStatus("current")
_OspfInterfaceDelay_Type = Unsigned32
_OspfInterfaceDelay_Object = MibTableColumn
ospfInterfaceDelay = _OspfInterfaceDelay_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 13),
    _OspfInterfaceDelay_Type()
)
ospfInterfaceDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceDelay.setStatus("current")


class _OspfInterfaceOspfIfState_Type(Integer32):
    """Custom type ospfInterfaceOspfIfState based on Integer32"""
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
        *(("if-depend-upon", 0),
          ("if-down", 1),
          ("if-loopback", 2),
          ("if-waiting", 3),
          ("if-point-to-point", 4),
          ("if-dr-other", 5),
          ("if-backup", 6),
          ("if-dr", 7))
    )


_OspfInterfaceOspfIfState_Type.__name__ = "Integer32"
_OspfInterfaceOspfIfState_Object = MibTableColumn
ospfInterfaceOspfIfState = _OspfInterfaceOspfIfState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 14),
    _OspfInterfaceOspfIfState_Type()
)
ospfInterfaceOspfIfState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceOspfIfState.setStatus("current")
_OspfInterfacePriority_Type = Unsigned32
_OspfInterfacePriority_Object = MibTableColumn
ospfInterfacePriority = _OspfInterfacePriority_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 15),
    _OspfInterfacePriority_Type()
)
ospfInterfacePriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfacePriority.setStatus("current")
_OspfInterfaceDesignatedRouterId_Type = IpAddress
_OspfInterfaceDesignatedRouterId_Object = MibTableColumn
ospfInterfaceDesignatedRouterId = _OspfInterfaceDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 16),
    _OspfInterfaceDesignatedRouterId_Type()
)
ospfInterfaceDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceDesignatedRouterId.setStatus("current")
_OspfInterfaceBackupDesignatedRouterId_Type = IpAddress
_OspfInterfaceBackupDesignatedRouterId_Object = MibTableColumn
ospfInterfaceBackupDesignatedRouterId = _OspfInterfaceBackupDesignatedRouterId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 17),
    _OspfInterfaceBackupDesignatedRouterId_Type()
)
ospfInterfaceBackupDesignatedRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceBackupDesignatedRouterId.setStatus("current")
_OspfInterfaceDesignatedRouterIp_Type = IpAddress
_OspfInterfaceDesignatedRouterIp_Object = MibTableColumn
ospfInterfaceDesignatedRouterIp = _OspfInterfaceDesignatedRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 18),
    _OspfInterfaceDesignatedRouterIp_Type()
)
ospfInterfaceDesignatedRouterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceDesignatedRouterIp.setStatus("current")
_OspfInterfaceBackupDesignatedRouterIp_Type = IpAddress
_OspfInterfaceBackupDesignatedRouterIp_Object = MibTableColumn
ospfInterfaceBackupDesignatedRouterIp = _OspfInterfaceBackupDesignatedRouterIp_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 19),
    _OspfInterfaceBackupDesignatedRouterIp_Type()
)
ospfInterfaceBackupDesignatedRouterIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceBackupDesignatedRouterIp.setStatus("current")
_OspfInterfaceLsaSeqnum_Type = Unsigned32
_OspfInterfaceLsaSeqnum_Object = MibTableColumn
ospfInterfaceLsaSeqnum = _OspfInterfaceLsaSeqnum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 20),
    _OspfInterfaceLsaSeqnum_Type()
)
ospfInterfaceLsaSeqnum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceLsaSeqnum.setStatus("current")


class _OspfInterfaceMembers_Type(Integer32):
    """Custom type ospfInterfaceMembers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("all", 0),
          ("designated", 1),
          ("both", 2))
    )


_OspfInterfaceMembers_Type.__name__ = "Integer32"
_OspfInterfaceMembers_Object = MibTableColumn
ospfInterfaceMembers = _OspfInterfaceMembers_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 21),
    _OspfInterfaceMembers_Type()
)
ospfInterfaceMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceMembers.setStatus("current")
_OspfInterfaceHelloTimer_Type = Unsigned32
_OspfInterfaceHelloTimer_Object = MibTableColumn
ospfInterfaceHelloTimer = _OspfInterfaceHelloTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 22),
    _OspfInterfaceHelloTimer_Type()
)
ospfInterfaceHelloTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceHelloTimer.setStatus("current")
_OspfInterfaceDeadInterval_Type = Unsigned32
_OspfInterfaceDeadInterval_Object = MibTableColumn
ospfInterfaceDeadInterval = _OspfInterfaceDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 23),
    _OspfInterfaceDeadInterval_Type()
)
ospfInterfaceDeadInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceDeadInterval.setStatus("current")
_OspfInterfaceRetransmitTimer_Type = Unsigned32
_OspfInterfaceRetransmitTimer_Object = MibTableColumn
ospfInterfaceRetransmitTimer = _OspfInterfaceRetransmitTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 24),
    _OspfInterfaceRetransmitTimer_Type()
)
ospfInterfaceRetransmitTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceRetransmitTimer.setStatus("current")
_OspfInterfaceNeighborCount_Type = Unsigned32
_OspfInterfaceNeighborCount_Object = MibTableColumn
ospfInterfaceNeighborCount = _OspfInterfaceNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 25),
    _OspfInterfaceNeighborCount_Type()
)
ospfInterfaceNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceNeighborCount.setStatus("current")
_OspfInterfaceAdjNeighborCount_Type = Unsigned32
_OspfInterfaceAdjNeighborCount_Object = MibTableColumn
ospfInterfaceAdjNeighborCount = _OspfInterfaceAdjNeighborCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 26),
    _OspfInterfaceAdjNeighborCount_Type()
)
ospfInterfaceAdjNeighborCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceAdjNeighborCount.setStatus("current")
_OspfInterfaceHelloDueTime_Type = Unsigned32
_OspfInterfaceHelloDueTime_Object = MibTableColumn
ospfInterfaceHelloDueTime = _OspfInterfaceHelloDueTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 27),
    _OspfInterfaceHelloDueTime_Type()
)
ospfInterfaceHelloDueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceHelloDueTime.setStatus("current")
_OspfInterfaceOperState_Type = TruthValue
_OspfInterfaceOperState_Object = MibTableColumn
ospfInterfaceOperState = _OspfInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 28),
    _OspfInterfaceOperState_Type()
)
ospfInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceOperState.setStatus("current")
_OspfInterfaceMd5KeyId_Type = UnsignedByte
_OspfInterfaceMd5KeyId_Object = MibTableColumn
ospfInterfaceMd5KeyId = _OspfInterfaceMd5KeyId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 29),
    _OspfInterfaceMd5KeyId_Type()
)
ospfInterfaceMd5KeyId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceMd5KeyId.setStatus("current")


class _OspfInterfaceMd5Key_Type(String):
    """Custom type ospfInterfaceMd5Key based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OspfInterfaceMd5Key_Type.__name__ = "String"
_OspfInterfaceMd5Key_Object = MibTableColumn
ospfInterfaceMd5Key = _OspfInterfaceMd5Key_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 3, 1, 30),
    _OspfInterfaceMd5Key_Type()
)
ospfInterfaceMd5Key.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfInterfaceMd5Key.setStatus("current")
_OspfDatabaseTable_Object = MibTable
ospfDatabaseTable = _OspfDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4)
)
if mibBuilder.loadTexts:
    ospfDatabaseTable.setStatus("current")
_OspfDatabaseEntry_Object = MibTableRow
ospfDatabaseEntry = _OspfDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1)
)
ospfDatabaseEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseArea"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseLsaType"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseLinkId"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseAdvRouter"),
)
if mibBuilder.loadTexts:
    ospfDatabaseEntry.setStatus("current")


class _OspfDatabaseVpnId_Type(Unsigned32):
    """Custom type ospfDatabaseVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OspfDatabaseVpnId_Type.__name__ = "Unsigned32"
_OspfDatabaseVpnId_Object = MibTableColumn
ospfDatabaseVpnId = _OspfDatabaseVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 1),
    _OspfDatabaseVpnId_Type()
)
ospfDatabaseVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfDatabaseVpnId.setStatus("current")
_OspfDatabaseArea_Type = Unsigned32
_OspfDatabaseArea_Object = MibTableColumn
ospfDatabaseArea = _OspfDatabaseArea_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 2),
    _OspfDatabaseArea_Type()
)
ospfDatabaseArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfDatabaseArea.setStatus("current")


class _OspfDatabaseLsaType_Type(Integer32):
    """Custom type ospfDatabaseLsaType based on Integer32"""
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
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("router", 1),
          ("network", 2),
          ("summary", 3),
          ("asbr-summary", 4),
          ("external", 5),
          ("group-member", 6),
          ("nssa-external", 7),
          ("type-ext-attributes", 8),
          ("link-local-opaque", 9),
          ("area-local-opaque", 10),
          ("as-external-opaque", 11))
    )


_OspfDatabaseLsaType_Type.__name__ = "Integer32"
_OspfDatabaseLsaType_Object = MibTableColumn
ospfDatabaseLsaType = _OspfDatabaseLsaType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 3),
    _OspfDatabaseLsaType_Type()
)
ospfDatabaseLsaType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfDatabaseLsaType.setStatus("current")
_OspfDatabaseLinkId_Type = IpAddress
_OspfDatabaseLinkId_Object = MibTableColumn
ospfDatabaseLinkId = _OspfDatabaseLinkId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 4),
    _OspfDatabaseLinkId_Type()
)
ospfDatabaseLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfDatabaseLinkId.setStatus("current")
_OspfDatabaseAdvRouter_Type = IpAddress
_OspfDatabaseAdvRouter_Object = MibTableColumn
ospfDatabaseAdvRouter = _OspfDatabaseAdvRouter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 5),
    _OspfDatabaseAdvRouter_Type()
)
ospfDatabaseAdvRouter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfDatabaseAdvRouter.setStatus("current")
_OspfDatabaseChecksum_Type = Unsigned32
_OspfDatabaseChecksum_Object = MibTableColumn
ospfDatabaseChecksum = _OspfDatabaseChecksum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 6),
    _OspfDatabaseChecksum_Type()
)
ospfDatabaseChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseChecksum.setStatus("current")
_OspfDatabaseAge_Type = Unsigned32
_OspfDatabaseAge_Object = MibTableColumn
ospfDatabaseAge = _OspfDatabaseAge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 7),
    _OspfDatabaseAge_Type()
)
ospfDatabaseAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseAge.setStatus("current")
_OspfDatabaseSequence_Type = Unsigned32
_OspfDatabaseSequence_Object = MibTableColumn
ospfDatabaseSequence = _OspfDatabaseSequence_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 8),
    _OspfDatabaseSequence_Type()
)
ospfDatabaseSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseSequence.setStatus("current")
_OspfDatabaseLength_Type = Unsigned32
_OspfDatabaseLength_Object = MibTableColumn
ospfDatabaseLength = _OspfDatabaseLength_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 9),
    _OspfDatabaseLength_Type()
)
ospfDatabaseLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseLength.setStatus("current")
_OspfDatabaseOptions_Type = Unsigned32
_OspfDatabaseOptions_Object = MibTableColumn
ospfDatabaseOptions = _OspfDatabaseOptions_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 10),
    _OspfDatabaseOptions_Type()
)
ospfDatabaseOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseOptions.setStatus("current")
_OspfDatabaseOptionsFlags_Type = OspfNeighborOptions
_OspfDatabaseOptionsFlags_Object = MibTableColumn
ospfDatabaseOptionsFlags = _OspfDatabaseOptionsFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 11),
    _OspfDatabaseOptionsFlags_Type()
)
ospfDatabaseOptionsFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseOptionsFlags.setStatus("current")
_OspfDatabaseFlags_Type = Unsigned32
_OspfDatabaseFlags_Object = MibTableColumn
ospfDatabaseFlags = _OspfDatabaseFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 12),
    _OspfDatabaseFlags_Type()
)
ospfDatabaseFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseFlags.setStatus("current")
_OspfDatabaseRlsaFlags_Type = OspfDbRlsaFlags
_OspfDatabaseRlsaFlags_Object = MibTableColumn
ospfDatabaseRlsaFlags = _OspfDatabaseRlsaFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 13),
    _OspfDatabaseRlsaFlags_Type()
)
ospfDatabaseRlsaFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseRlsaFlags.setStatus("current")
_OspfDatabaseRlsaFlagsValue_Type = Unsigned32
_OspfDatabaseRlsaFlagsValue_Object = MibTableColumn
ospfDatabaseRlsaFlagsValue = _OspfDatabaseRlsaFlagsValue_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 14),
    _OspfDatabaseRlsaFlagsValue_Type()
)
ospfDatabaseRlsaFlagsValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseRlsaFlagsValue.setStatus("current")
_OspfDatabasePrefix_Type = Ipv4Prefix
_OspfDatabasePrefix_Object = MibTableColumn
ospfDatabasePrefix = _OspfDatabasePrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 15),
    _OspfDatabasePrefix_Type()
)
ospfDatabasePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabasePrefix.setStatus("current")
_OspfDatabaseTag_Type = Unsigned32
_OspfDatabaseTag_Object = MibTableColumn
ospfDatabaseTag = _OspfDatabaseTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 16),
    _OspfDatabaseTag_Type()
)
ospfDatabaseTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseTag.setStatus("current")


class _OspfDatabaseMetricType_Type(Integer32):
    """Custom type ospfDatabaseMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type1", 0),
          ("type2", 1))
    )


_OspfDatabaseMetricType_Type.__name__ = "Integer32"
_OspfDatabaseMetricType_Object = MibTableColumn
ospfDatabaseMetricType = _OspfDatabaseMetricType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 17),
    _OspfDatabaseMetricType_Type()
)
ospfDatabaseMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseMetricType.setStatus("current")
_OspfDatabaseMask_Type = IpAddress
_OspfDatabaseMask_Object = MibTableColumn
ospfDatabaseMask = _OspfDatabaseMask_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 18),
    _OspfDatabaseMask_Type()
)
ospfDatabaseMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseMask.setStatus("current")
_OspfDatabaseMetric_Type = Unsigned32
_OspfDatabaseMetric_Object = MibTableColumn
ospfDatabaseMetric = _OspfDatabaseMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 19),
    _OspfDatabaseMetric_Type()
)
ospfDatabaseMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseMetric.setStatus("current")
_OspfDatabaseForwardingAddr_Type = IpAddress
_OspfDatabaseForwardingAddr_Object = MibTableColumn
ospfDatabaseForwardingAddr = _OspfDatabaseForwardingAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 20),
    _OspfDatabaseForwardingAddr_Type()
)
ospfDatabaseForwardingAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseForwardingAddr.setStatus("current")
_OspfDatabaseLinkCount_Type = Unsigned32
_OspfDatabaseLinkCount_Object = MibTableColumn
ospfDatabaseLinkCount = _OspfDatabaseLinkCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 4, 1, 21),
    _OspfDatabaseLinkCount_Type()
)
ospfDatabaseLinkCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseLinkCount.setStatus("current")
_OspfDatabaseRouterLinkTable_Object = MibTable
ospfDatabaseRouterLinkTable = _OspfDatabaseRouterLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 5)
)
if mibBuilder.loadTexts:
    ospfDatabaseRouterLinkTable.setStatus("current")
_OspfDatabaseRouterLinkEntry_Object = MibTableRow
ospfDatabaseRouterLinkEntry = _OspfDatabaseRouterLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 5, 1)
)
ospfDatabaseRouterLinkEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseArea"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseLsaType"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseLinkId"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseAdvRouter"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseRouterLinkLinkIndex"),
)
if mibBuilder.loadTexts:
    ospfDatabaseRouterLinkEntry.setStatus("current")
_OspfDatabaseRouterLinkLinkIndex_Type = Unsigned32
_OspfDatabaseRouterLinkLinkIndex_Object = MibTableColumn
ospfDatabaseRouterLinkLinkIndex = _OspfDatabaseRouterLinkLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 5, 1, 1),
    _OspfDatabaseRouterLinkLinkIndex_Type()
)
ospfDatabaseRouterLinkLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfDatabaseRouterLinkLinkIndex.setStatus("current")
_OspfDatabaseRouterLinkRouterLinkId_Type = IpAddress
_OspfDatabaseRouterLinkRouterLinkId_Object = MibTableColumn
ospfDatabaseRouterLinkRouterLinkId = _OspfDatabaseRouterLinkRouterLinkId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 5, 1, 2),
    _OspfDatabaseRouterLinkRouterLinkId_Type()
)
ospfDatabaseRouterLinkRouterLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseRouterLinkRouterLinkId.setStatus("current")
_OspfDatabaseRouterLinkData_Type = IpAddress
_OspfDatabaseRouterLinkData_Object = MibTableColumn
ospfDatabaseRouterLinkData = _OspfDatabaseRouterLinkData_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 5, 1, 3),
    _OspfDatabaseRouterLinkData_Type()
)
ospfDatabaseRouterLinkData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseRouterLinkData.setStatus("current")
_OspfDatabaseRouterLinkTosMetric_Type = Unsigned32
_OspfDatabaseRouterLinkTosMetric_Object = MibTableColumn
ospfDatabaseRouterLinkTosMetric = _OspfDatabaseRouterLinkTosMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 5, 1, 4),
    _OspfDatabaseRouterLinkTosMetric_Type()
)
ospfDatabaseRouterLinkTosMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseRouterLinkTosMetric.setStatus("current")


class _OspfDatabaseRouterLinkRouterLinkType_Type(Integer32):
    """Custom type ospfDatabaseRouterLinkRouterLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("point-to-point", 0),
          ("transit", 1),
          ("stub", 2))
    )


_OspfDatabaseRouterLinkRouterLinkType_Type.__name__ = "Integer32"
_OspfDatabaseRouterLinkRouterLinkType_Object = MibTableColumn
ospfDatabaseRouterLinkRouterLinkType = _OspfDatabaseRouterLinkRouterLinkType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 5, 1, 5),
    _OspfDatabaseRouterLinkRouterLinkType_Type()
)
ospfDatabaseRouterLinkRouterLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseRouterLinkRouterLinkType.setStatus("current")
_OspfDatabaseNetworkLinkTable_Object = MibTable
ospfDatabaseNetworkLinkTable = _OspfDatabaseNetworkLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 6)
)
if mibBuilder.loadTexts:
    ospfDatabaseNetworkLinkTable.setStatus("current")
_OspfDatabaseNetworkLinkEntry_Object = MibTableRow
ospfDatabaseNetworkLinkEntry = _OspfDatabaseNetworkLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 6, 1)
)
ospfDatabaseNetworkLinkEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseArea"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseLsaType"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseLinkId"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseAdvRouter"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseNetworkLinkLinkIndex"),
)
if mibBuilder.loadTexts:
    ospfDatabaseNetworkLinkEntry.setStatus("current")
_OspfDatabaseNetworkLinkLinkIndex_Type = Unsigned32
_OspfDatabaseNetworkLinkLinkIndex_Object = MibTableColumn
ospfDatabaseNetworkLinkLinkIndex = _OspfDatabaseNetworkLinkLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 6, 1, 1),
    _OspfDatabaseNetworkLinkLinkIndex_Type()
)
ospfDatabaseNetworkLinkLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfDatabaseNetworkLinkLinkIndex.setStatus("current")
_OspfDatabaseNetworkLinkNetworkLinkId_Type = IpAddress
_OspfDatabaseNetworkLinkNetworkLinkId_Object = MibTableColumn
ospfDatabaseNetworkLinkNetworkLinkId = _OspfDatabaseNetworkLinkNetworkLinkId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 6, 1, 2),
    _OspfDatabaseNetworkLinkNetworkLinkId_Type()
)
ospfDatabaseNetworkLinkNetworkLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseNetworkLinkNetworkLinkId.setStatus("current")
_OspfExternalDatabaseTable_Object = MibTable
ospfExternalDatabaseTable = _OspfExternalDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7)
)
if mibBuilder.loadTexts:
    ospfExternalDatabaseTable.setStatus("current")
_OspfExternalDatabaseEntry_Object = MibTableRow
ospfExternalDatabaseEntry = _OspfExternalDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1)
)
ospfExternalDatabaseEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfExternalDatabaseVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfExternalDatabaseLinkId"),
    (0, "VIPTELA-OPER-OSPF", "ospfExternalDatabaseAdvRouter"),
)
if mibBuilder.loadTexts:
    ospfExternalDatabaseEntry.setStatus("current")


class _OspfExternalDatabaseVpnId_Type(Unsigned32):
    """Custom type ospfExternalDatabaseVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OspfExternalDatabaseVpnId_Type.__name__ = "Unsigned32"
_OspfExternalDatabaseVpnId_Object = MibTableColumn
ospfExternalDatabaseVpnId = _OspfExternalDatabaseVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 1),
    _OspfExternalDatabaseVpnId_Type()
)
ospfExternalDatabaseVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfExternalDatabaseVpnId.setStatus("current")
_OspfExternalDatabaseLinkId_Type = IpAddress
_OspfExternalDatabaseLinkId_Object = MibTableColumn
ospfExternalDatabaseLinkId = _OspfExternalDatabaseLinkId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 2),
    _OspfExternalDatabaseLinkId_Type()
)
ospfExternalDatabaseLinkId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfExternalDatabaseLinkId.setStatus("current")
_OspfExternalDatabaseAdvRouter_Type = IpAddress
_OspfExternalDatabaseAdvRouter_Object = MibTableColumn
ospfExternalDatabaseAdvRouter = _OspfExternalDatabaseAdvRouter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 3),
    _OspfExternalDatabaseAdvRouter_Type()
)
ospfExternalDatabaseAdvRouter.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfExternalDatabaseAdvRouter.setStatus("current")
_OspfExternalDatabaseChecksum_Type = Unsigned32
_OspfExternalDatabaseChecksum_Object = MibTableColumn
ospfExternalDatabaseChecksum = _OspfExternalDatabaseChecksum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 4),
    _OspfExternalDatabaseChecksum_Type()
)
ospfExternalDatabaseChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseChecksum.setStatus("current")
_OspfExternalDatabaseAge_Type = Unsigned32
_OspfExternalDatabaseAge_Object = MibTableColumn
ospfExternalDatabaseAge = _OspfExternalDatabaseAge_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 5),
    _OspfExternalDatabaseAge_Type()
)
ospfExternalDatabaseAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseAge.setStatus("current")
_OspfExternalDatabaseSequence_Type = Unsigned32
_OspfExternalDatabaseSequence_Object = MibTableColumn
ospfExternalDatabaseSequence = _OspfExternalDatabaseSequence_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 6),
    _OspfExternalDatabaseSequence_Type()
)
ospfExternalDatabaseSequence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseSequence.setStatus("current")
_OspfExternalDatabaseLength_Type = Unsigned32
_OspfExternalDatabaseLength_Object = MibTableColumn
ospfExternalDatabaseLength = _OspfExternalDatabaseLength_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 7),
    _OspfExternalDatabaseLength_Type()
)
ospfExternalDatabaseLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseLength.setStatus("current")
_OspfExternalDatabaseOptions_Type = Unsigned32
_OspfExternalDatabaseOptions_Object = MibTableColumn
ospfExternalDatabaseOptions = _OspfExternalDatabaseOptions_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 8),
    _OspfExternalDatabaseOptions_Type()
)
ospfExternalDatabaseOptions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseOptions.setStatus("current")
_OspfExternalDatabaseOptionsFlags_Type = OspfNeighborOptions
_OspfExternalDatabaseOptionsFlags_Object = MibTableColumn
ospfExternalDatabaseOptionsFlags = _OspfExternalDatabaseOptionsFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 9),
    _OspfExternalDatabaseOptionsFlags_Type()
)
ospfExternalDatabaseOptionsFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseOptionsFlags.setStatus("current")
_OspfExternalDatabaseFlags_Type = Unsigned32
_OspfExternalDatabaseFlags_Object = MibTableColumn
ospfExternalDatabaseFlags = _OspfExternalDatabaseFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 10),
    _OspfExternalDatabaseFlags_Type()
)
ospfExternalDatabaseFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseFlags.setStatus("current")
_OspfExternalDatabasePrefix_Type = Ipv4Prefix
_OspfExternalDatabasePrefix_Object = MibTableColumn
ospfExternalDatabasePrefix = _OspfExternalDatabasePrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 11),
    _OspfExternalDatabasePrefix_Type()
)
ospfExternalDatabasePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabasePrefix.setStatus("current")
_OspfExternalDatabaseTag_Type = Unsigned32
_OspfExternalDatabaseTag_Object = MibTableColumn
ospfExternalDatabaseTag = _OspfExternalDatabaseTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 12),
    _OspfExternalDatabaseTag_Type()
)
ospfExternalDatabaseTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseTag.setStatus("current")


class _OspfExternalDatabaseMetricType_Type(Integer32):
    """Custom type ospfExternalDatabaseMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("type1", 0),
          ("type2", 1))
    )


_OspfExternalDatabaseMetricType_Type.__name__ = "Integer32"
_OspfExternalDatabaseMetricType_Object = MibTableColumn
ospfExternalDatabaseMetricType = _OspfExternalDatabaseMetricType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 13),
    _OspfExternalDatabaseMetricType_Type()
)
ospfExternalDatabaseMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseMetricType.setStatus("current")
_OspfExternalDatabaseMask_Type = IpAddress
_OspfExternalDatabaseMask_Object = MibTableColumn
ospfExternalDatabaseMask = _OspfExternalDatabaseMask_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 14),
    _OspfExternalDatabaseMask_Type()
)
ospfExternalDatabaseMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseMask.setStatus("current")
_OspfExternalDatabaseMetric_Type = Unsigned32
_OspfExternalDatabaseMetric_Object = MibTableColumn
ospfExternalDatabaseMetric = _OspfExternalDatabaseMetric_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 15),
    _OspfExternalDatabaseMetric_Type()
)
ospfExternalDatabaseMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseMetric.setStatus("current")
_OspfExternalDatabaseForwardingAddr_Type = IpAddress
_OspfExternalDatabaseForwardingAddr_Object = MibTableColumn
ospfExternalDatabaseForwardingAddr = _OspfExternalDatabaseForwardingAddr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 7, 1, 16),
    _OspfExternalDatabaseForwardingAddr_Type()
)
ospfExternalDatabaseForwardingAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfExternalDatabaseForwardingAddr.setStatus("current")
_OspfRoutesTableTable_Object = MibTable
ospfRoutesTableTable = _OspfRoutesTableTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 8)
)
if mibBuilder.loadTexts:
    ospfRoutesTableTable.setStatus("current")
_OspfRoutesTableEntry_Object = MibTableRow
ospfRoutesTableEntry = _OspfRoutesTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 8, 1)
)
ospfRoutesTableEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfRoutesTableVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfRoutesTableRouteType"),
    (0, "VIPTELA-OPER-OSPF", "ospfRoutesTablePrefix"),
)
if mibBuilder.loadTexts:
    ospfRoutesTableEntry.setStatus("current")


class _OspfRoutesTableVpnId_Type(Unsigned32):
    """Custom type ospfRoutesTableVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OspfRoutesTableVpnId_Type.__name__ = "Unsigned32"
_OspfRoutesTableVpnId_Object = MibTableColumn
ospfRoutesTableVpnId = _OspfRoutesTableVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 8, 1, 1),
    _OspfRoutesTableVpnId_Type()
)
ospfRoutesTableVpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableVpnId.setStatus("current")


class _OspfRoutesTableRouteType_Type(Integer32):
    """Custom type ospfRoutesTableRouteType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("router", 0),
          ("network", 1),
          ("external", 2))
    )


_OspfRoutesTableRouteType_Type.__name__ = "Integer32"
_OspfRoutesTableRouteType_Object = MibTableColumn
ospfRoutesTableRouteType = _OspfRoutesTableRouteType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 8, 1, 2),
    _OspfRoutesTableRouteType_Type()
)
ospfRoutesTableRouteType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfRoutesTableRouteType.setStatus("current")
_OspfRoutesTablePrefix_Type = Ipv4Prefix
_OspfRoutesTablePrefix_Object = MibTableColumn
ospfRoutesTablePrefix = _OspfRoutesTablePrefix_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 8, 1, 3),
    _OspfRoutesTablePrefix_Type()
)
ospfRoutesTablePrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfRoutesTablePrefix.setStatus("current")
_OspfRoutesTableInfoTable_Object = MibTable
ospfRoutesTableInfoTable = _OspfRoutesTableInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9)
)
if mibBuilder.loadTexts:
    ospfRoutesTableInfoTable.setStatus("current")
_OspfRoutesTableInfoEntry_Object = MibTableRow
ospfRoutesTableInfoEntry = _OspfRoutesTableInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1)
)
ospfRoutesTableInfoEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfRoutesTableVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfRoutesTableRouteType"),
    (0, "VIPTELA-OPER-OSPF", "ospfRoutesTablePrefix"),
    (0, "VIPTELA-OPER-OSPF", "ospfRoutesTableInfoInfoId"),
)
if mibBuilder.loadTexts:
    ospfRoutesTableInfoEntry.setStatus("current")
_OspfRoutesTableInfoInfoId_Type = Unsigned32
_OspfRoutesTableInfoInfoId_Object = MibTableColumn
ospfRoutesTableInfoInfoId = _OspfRoutesTableInfoInfoId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 1),
    _OspfRoutesTableInfoInfoId_Type()
)
ospfRoutesTableInfoInfoId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoInfoId.setStatus("current")
_OspfRoutesTableInfoAreaId_Type = Unsigned32
_OspfRoutesTableInfoAreaId_Object = MibTableColumn
ospfRoutesTableInfoAreaId = _OspfRoutesTableInfoAreaId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 2),
    _OspfRoutesTableInfoAreaId_Type()
)
ospfRoutesTableInfoAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoAreaId.setStatus("current")
_OspfRoutesTableInfoCost_Type = Unsigned32
_OspfRoutesTableInfoCost_Object = MibTableColumn
ospfRoutesTableInfoCost = _OspfRoutesTableInfoCost_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 3),
    _OspfRoutesTableInfoCost_Type()
)
ospfRoutesTableInfoCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoCost.setStatus("current")
_OspfRoutesTableInfoFlags_Type = Unsigned32
_OspfRoutesTableInfoFlags_Object = MibTableColumn
ospfRoutesTableInfoFlags = _OspfRoutesTableInfoFlags_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 4),
    _OspfRoutesTableInfoFlags_Type()
)
ospfRoutesTableInfoFlags.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoFlags.setStatus("current")


class _OspfRoutesTableInfoPathType_Type(Integer32):
    """Custom type ospfRoutesTableInfoPathType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("intra-area", 0),
          ("inter-area", 1),
          ("external1", 2),
          ("external2", 3),
          ("nssa-external1", 4),
          ("nssa-external2", 5))
    )


_OspfRoutesTableInfoPathType_Type.__name__ = "Integer32"
_OspfRoutesTableInfoPathType_Object = MibTableColumn
ospfRoutesTableInfoPathType = _OspfRoutesTableInfoPathType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 5),
    _OspfRoutesTableInfoPathType_Type()
)
ospfRoutesTableInfoPathType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoPathType.setStatus("current")


class _OspfRoutesTableInfoDestType_Type(Integer32):
    """Custom type ospfRoutesTableInfoDestType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("router", 0),
          ("network", 1),
          ("discard", 2))
    )


_OspfRoutesTableInfoDestType_Type.__name__ = "Integer32"
_OspfRoutesTableInfoDestType_Object = MibTableColumn
ospfRoutesTableInfoDestType = _OspfRoutesTableInfoDestType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 6),
    _OspfRoutesTableInfoDestType_Type()
)
ospfRoutesTableInfoDestType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoDestType.setStatus("current")
_OspfRoutesTableInfoTag_Type = Unsigned32
_OspfRoutesTableInfoTag_Object = MibTableColumn
ospfRoutesTableInfoTag = _OspfRoutesTableInfoTag_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 7),
    _OspfRoutesTableInfoTag_Type()
)
ospfRoutesTableInfoTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoTag.setStatus("current")
_OspfRoutesTableInfoType2Cost_Type = Unsigned32
_OspfRoutesTableInfoType2Cost_Object = MibTableColumn
ospfRoutesTableInfoType2Cost = _OspfRoutesTableInfoType2Cost_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 8),
    _OspfRoutesTableInfoType2Cost_Type()
)
ospfRoutesTableInfoType2Cost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoType2Cost.setStatus("current")
_OspfRoutesTableInfoNextHop_Type = IpAddress
_OspfRoutesTableInfoNextHop_Object = MibTableColumn
ospfRoutesTableInfoNextHop = _OspfRoutesTableInfoNextHop_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 9),
    _OspfRoutesTableInfoNextHop_Type()
)
ospfRoutesTableInfoNextHop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoNextHop.setStatus("current")


class _OspfRoutesTableInfoIfName_Type(String):
    """Custom type ospfRoutesTableInfoIfName based on String"""
    subtypeSpec = String.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_OspfRoutesTableInfoIfName_Type.__name__ = "String"
_OspfRoutesTableInfoIfName_Object = MibTableColumn
ospfRoutesTableInfoIfName = _OspfRoutesTableInfoIfName_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 9, 1, 10),
    _OspfRoutesTableInfoIfName_Type()
)
ospfRoutesTableInfoIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRoutesTableInfoIfName.setStatus("current")
_OspfDatabaseSummaryTable_Object = MibTable
ospfDatabaseSummaryTable = _OspfDatabaseSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10)
)
if mibBuilder.loadTexts:
    ospfDatabaseSummaryTable.setStatus("current")
_OspfDatabaseSummaryEntry_Object = MibTableRow
ospfDatabaseSummaryEntry = _OspfDatabaseSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10, 1)
)
ospfDatabaseSummaryEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseSummaryVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfDatabaseSummaryAreaId"),
)
if mibBuilder.loadTexts:
    ospfDatabaseSummaryEntry.setStatus("current")


class _OspfDatabaseSummaryVpnId_Type(Unsigned32):
    """Custom type ospfDatabaseSummaryVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OspfDatabaseSummaryVpnId_Type.__name__ = "Unsigned32"
_OspfDatabaseSummaryVpnId_Object = MibTableColumn
ospfDatabaseSummaryVpnId = _OspfDatabaseSummaryVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10, 1, 1),
    _OspfDatabaseSummaryVpnId_Type()
)
ospfDatabaseSummaryVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfDatabaseSummaryVpnId.setStatus("current")
_OspfDatabaseSummaryAreaId_Type = Unsigned32
_OspfDatabaseSummaryAreaId_Object = MibTableColumn
ospfDatabaseSummaryAreaId = _OspfDatabaseSummaryAreaId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10, 1, 2),
    _OspfDatabaseSummaryAreaId_Type()
)
ospfDatabaseSummaryAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfDatabaseSummaryAreaId.setStatus("current")
_OspfDatabaseSummaryRouterLsa_Type = Unsigned32
_OspfDatabaseSummaryRouterLsa_Object = MibTableColumn
ospfDatabaseSummaryRouterLsa = _OspfDatabaseSummaryRouterLsa_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10, 1, 3),
    _OspfDatabaseSummaryRouterLsa_Type()
)
ospfDatabaseSummaryRouterLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseSummaryRouterLsa.setStatus("current")
_OspfDatabaseSummaryNetworkLsa_Type = Unsigned32
_OspfDatabaseSummaryNetworkLsa_Object = MibTableColumn
ospfDatabaseSummaryNetworkLsa = _OspfDatabaseSummaryNetworkLsa_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10, 1, 4),
    _OspfDatabaseSummaryNetworkLsa_Type()
)
ospfDatabaseSummaryNetworkLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseSummaryNetworkLsa.setStatus("current")
_OspfDatabaseSummarySummaryLsa_Type = Unsigned32
_OspfDatabaseSummarySummaryLsa_Object = MibTableColumn
ospfDatabaseSummarySummaryLsa = _OspfDatabaseSummarySummaryLsa_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10, 1, 5),
    _OspfDatabaseSummarySummaryLsa_Type()
)
ospfDatabaseSummarySummaryLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseSummarySummaryLsa.setStatus("current")
_OspfDatabaseSummaryAsExternalLsa_Type = Unsigned32
_OspfDatabaseSummaryAsExternalLsa_Object = MibTableColumn
ospfDatabaseSummaryAsExternalLsa = _OspfDatabaseSummaryAsExternalLsa_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10, 1, 6),
    _OspfDatabaseSummaryAsExternalLsa_Type()
)
ospfDatabaseSummaryAsExternalLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseSummaryAsExternalLsa.setStatus("current")
_OspfDatabaseSummaryNssaLsa_Type = Unsigned32
_OspfDatabaseSummaryNssaLsa_Object = MibTableColumn
ospfDatabaseSummaryNssaLsa = _OspfDatabaseSummaryNssaLsa_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10, 1, 7),
    _OspfDatabaseSummaryNssaLsa_Type()
)
ospfDatabaseSummaryNssaLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseSummaryNssaLsa.setStatus("current")
_OspfDatabaseSummaryTotalLsa_Type = Unsigned32
_OspfDatabaseSummaryTotalLsa_Object = MibTableColumn
ospfDatabaseSummaryTotalLsa = _OspfDatabaseSummaryTotalLsa_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 10, 1, 8),
    _OspfDatabaseSummaryTotalLsa_Type()
)
ospfDatabaseSummaryTotalLsa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfDatabaseSummaryTotalLsa.setStatus("current")
_OspfProcessTable_Object = MibTable
ospfProcessTable = _OspfProcessTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11)
)
if mibBuilder.loadTexts:
    ospfProcessTable.setStatus("current")
_OspfProcessEntry_Object = MibTableRow
ospfProcessEntry = _OspfProcessEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1)
)
ospfProcessEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfProcessVpnId"),
)
if mibBuilder.loadTexts:
    ospfProcessEntry.setStatus("current")


class _OspfProcessVpnId_Type(Unsigned32):
    """Custom type ospfProcessVpnId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65530),
    )


_OspfProcessVpnId_Type.__name__ = "Unsigned32"
_OspfProcessVpnId_Object = MibTableColumn
ospfProcessVpnId = _OspfProcessVpnId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 1),
    _OspfProcessVpnId_Type()
)
ospfProcessVpnId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfProcessVpnId.setStatus("current")
_OspfProcessRouterId_Type = IpAddress
_OspfProcessRouterId_Object = MibTableColumn
ospfProcessRouterId = _OspfProcessRouterId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 2),
    _OspfProcessRouterId_Type()
)
ospfProcessRouterId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessRouterId.setStatus("current")
_OspfProcessDeferredShutdown_Type = TruthValue
_OspfProcessDeferredShutdown_Object = MibTableColumn
ospfProcessDeferredShutdown = _OspfProcessDeferredShutdown_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 3),
    _OspfProcessDeferredShutdown_Type()
)
ospfProcessDeferredShutdown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessDeferredShutdown.setStatus("current")
_OspfProcessRfc1583Compatible_Type = TruthValue
_OspfProcessRfc1583Compatible_Object = MibTableColumn
ospfProcessRfc1583Compatible = _OspfProcessRfc1583Compatible_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 4),
    _OspfProcessRfc1583Compatible_Type()
)
ospfProcessRfc1583Compatible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessRfc1583Compatible.setStatus("current")
_OspfProcessStubRouterAdv_Type = TruthValue
_OspfProcessStubRouterAdv_Object = MibTableColumn
ospfProcessStubRouterAdv = _OspfProcessStubRouterAdv_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 5),
    _OspfProcessStubRouterAdv_Type()
)
ospfProcessStubRouterAdv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessStubRouterAdv.setStatus("current")
_OspfProcessStubRouterStart_Type = Unsigned32
_OspfProcessStubRouterStart_Object = MibTableColumn
ospfProcessStubRouterStart = _OspfProcessStubRouterStart_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 6),
    _OspfProcessStubRouterStart_Type()
)
ospfProcessStubRouterStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessStubRouterStart.setStatus("current")
_OspfProcessStubRouterShut_Type = Unsigned32
_OspfProcessStubRouterShut_Object = MibTableColumn
ospfProcessStubRouterShut = _OspfProcessStubRouterShut_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 7),
    _OspfProcessStubRouterShut_Type()
)
ospfProcessStubRouterShut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessStubRouterShut.setStatus("current")
_OspfProcessSpfDelay_Type = Unsigned32
_OspfProcessSpfDelay_Object = MibTableColumn
ospfProcessSpfDelay = _OspfProcessSpfDelay_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 8),
    _OspfProcessSpfDelay_Type()
)
ospfProcessSpfDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessSpfDelay.setStatus("current")
_OspfProcessSpfHoldtime_Type = Unsigned32
_OspfProcessSpfHoldtime_Object = MibTableColumn
ospfProcessSpfHoldtime = _OspfProcessSpfHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 9),
    _OspfProcessSpfHoldtime_Type()
)
ospfProcessSpfHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessSpfHoldtime.setStatus("current")
_OspfProcessSpfMaxHoldtime_Type = Unsigned32
_OspfProcessSpfMaxHoldtime_Object = MibTableColumn
ospfProcessSpfMaxHoldtime = _OspfProcessSpfMaxHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 10),
    _OspfProcessSpfMaxHoldtime_Type()
)
ospfProcessSpfMaxHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessSpfMaxHoldtime.setStatus("current")
_OspfProcessSpfHoldMultiplier_Type = Unsigned32
_OspfProcessSpfHoldMultiplier_Object = MibTableColumn
ospfProcessSpfHoldMultiplier = _OspfProcessSpfHoldMultiplier_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 11),
    _OspfProcessSpfHoldMultiplier_Type()
)
ospfProcessSpfHoldMultiplier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessSpfHoldMultiplier.setStatus("current")
_OspfProcessSpfLastExecTime_Type = Unsigned32
_OspfProcessSpfLastExecTime_Object = MibTableColumn
ospfProcessSpfLastExecTime = _OspfProcessSpfLastExecTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 12),
    _OspfProcessSpfLastExecTime_Type()
)
ospfProcessSpfLastExecTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessSpfLastExecTime.setStatus("current")
_OspfProcessSpfNextDueTime_Type = Unsigned32
_OspfProcessSpfNextDueTime_Object = MibTableColumn
ospfProcessSpfNextDueTime = _OspfProcessSpfNextDueTime_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 13),
    _OspfProcessSpfNextDueTime_Type()
)
ospfProcessSpfNextDueTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessSpfNextDueTime.setStatus("current")
_OspfProcessLsaRefreshInterval_Type = Unsigned32
_OspfProcessLsaRefreshInterval_Object = MibTableColumn
ospfProcessLsaRefreshInterval = _OspfProcessLsaRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 14),
    _OspfProcessLsaRefreshInterval_Type()
)
ospfProcessLsaRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessLsaRefreshInterval.setStatus("current")
_OspfProcessAsbrRouter_Type = TruthValue
_OspfProcessAsbrRouter_Object = MibTableColumn
ospfProcessAsbrRouter = _OspfProcessAsbrRouter_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 15),
    _OspfProcessAsbrRouter_Type()
)
ospfProcessAsbrRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAsbrRouter.setStatus("current")
_OspfProcessExternalLsaCount_Type = Unsigned32
_OspfProcessExternalLsaCount_Object = MibTableColumn
ospfProcessExternalLsaCount = _OspfProcessExternalLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 16),
    _OspfProcessExternalLsaCount_Type()
)
ospfProcessExternalLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessExternalLsaCount.setStatus("current")
_OspfProcessExternalLsaChecksum_Type = Unsigned32
_OspfProcessExternalLsaChecksum_Object = MibTableColumn
ospfProcessExternalLsaChecksum = _OspfProcessExternalLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 17),
    _OspfProcessExternalLsaChecksum_Type()
)
ospfProcessExternalLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessExternalLsaChecksum.setStatus("current")
_OspfProcessNumberAreas_Type = Unsigned32
_OspfProcessNumberAreas_Object = MibTableColumn
ospfProcessNumberAreas = _OspfProcessNumberAreas_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 18),
    _OspfProcessNumberAreas_Type()
)
ospfProcessNumberAreas.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessNumberAreas.setStatus("current")
_OspfProcessLogAdjChanges_Type = TruthValue
_OspfProcessLogAdjChanges_Object = MibTableColumn
ospfProcessLogAdjChanges = _OspfProcessLogAdjChanges_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 19),
    _OspfProcessLogAdjChanges_Type()
)
ospfProcessLogAdjChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessLogAdjChanges.setStatus("current")
_OspfProcessIgnoreDownBit_Type = TruthValue
_OspfProcessIgnoreDownBit_Object = MibTableColumn
ospfProcessIgnoreDownBit = _OspfProcessIgnoreDownBit_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 20),
    _OspfProcessIgnoreDownBit_Type()
)
ospfProcessIgnoreDownBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessIgnoreDownBit.setStatus("current")
_OspfProcessHelloReceived_Type = Unsigned32
_OspfProcessHelloReceived_Object = MibTableColumn
ospfProcessHelloReceived = _OspfProcessHelloReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 21),
    _OspfProcessHelloReceived_Type()
)
ospfProcessHelloReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessHelloReceived.setStatus("current")
_OspfProcessHelloSent_Type = Unsigned32
_OspfProcessHelloSent_Object = MibTableColumn
ospfProcessHelloSent = _OspfProcessHelloSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 22),
    _OspfProcessHelloSent_Type()
)
ospfProcessHelloSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessHelloSent.setStatus("current")
_OspfProcessDbdReceived_Type = Unsigned32
_OspfProcessDbdReceived_Object = MibTableColumn
ospfProcessDbdReceived = _OspfProcessDbdReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 23),
    _OspfProcessDbdReceived_Type()
)
ospfProcessDbdReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessDbdReceived.setStatus("current")
_OspfProcessDbdSent_Type = Unsigned32
_OspfProcessDbdSent_Object = MibTableColumn
ospfProcessDbdSent = _OspfProcessDbdSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 24),
    _OspfProcessDbdSent_Type()
)
ospfProcessDbdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessDbdSent.setStatus("current")
_OspfProcessLsReqReceived_Type = Unsigned32
_OspfProcessLsReqReceived_Object = MibTableColumn
ospfProcessLsReqReceived = _OspfProcessLsReqReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 25),
    _OspfProcessLsReqReceived_Type()
)
ospfProcessLsReqReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessLsReqReceived.setStatus("current")
_OspfProcessLsReqSent_Type = Unsigned32
_OspfProcessLsReqSent_Object = MibTableColumn
ospfProcessLsReqSent = _OspfProcessLsReqSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 26),
    _OspfProcessLsReqSent_Type()
)
ospfProcessLsReqSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessLsReqSent.setStatus("current")
_OspfProcessLsUpdReceived_Type = Unsigned32
_OspfProcessLsUpdReceived_Object = MibTableColumn
ospfProcessLsUpdReceived = _OspfProcessLsUpdReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 27),
    _OspfProcessLsUpdReceived_Type()
)
ospfProcessLsUpdReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessLsUpdReceived.setStatus("current")
_OspfProcessLsUpdSent_Type = Unsigned32
_OspfProcessLsUpdSent_Object = MibTableColumn
ospfProcessLsUpdSent = _OspfProcessLsUpdSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 28),
    _OspfProcessLsUpdSent_Type()
)
ospfProcessLsUpdSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessLsUpdSent.setStatus("current")
_OspfProcessLsAckReceived_Type = Unsigned32
_OspfProcessLsAckReceived_Object = MibTableColumn
ospfProcessLsAckReceived = _OspfProcessLsAckReceived_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 29),
    _OspfProcessLsAckReceived_Type()
)
ospfProcessLsAckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessLsAckReceived.setStatus("current")
_OspfProcessLsAckSent_Type = Unsigned32
_OspfProcessLsAckSent_Object = MibTableColumn
ospfProcessLsAckSent = _OspfProcessLsAckSent_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 11, 1, 30),
    _OspfProcessLsAckSent_Type()
)
ospfProcessLsAckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessLsAckSent.setStatus("current")
_OspfProcessAreaTable_Object = MibTable
ospfProcessAreaTable = _OspfProcessAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12)
)
if mibBuilder.loadTexts:
    ospfProcessAreaTable.setStatus("current")
_OspfProcessAreaEntry_Object = MibTableRow
ospfProcessAreaEntry = _OspfProcessAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1)
)
ospfProcessAreaEntry.setIndexNames(
    (0, "VIPTELA-OPER-OSPF", "ospfProcessVpnId"),
    (0, "VIPTELA-OPER-OSPF", "ospfProcessAreaAreaId"),
)
if mibBuilder.loadTexts:
    ospfProcessAreaEntry.setStatus("current")
_OspfProcessAreaAreaId_Type = Unsigned32
_OspfProcessAreaAreaId_Object = MibTableColumn
ospfProcessAreaAreaId = _OspfProcessAreaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 1),
    _OspfProcessAreaAreaId_Type()
)
ospfProcessAreaAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfProcessAreaAreaId.setStatus("current")
_OspfProcessAreaBackboneArea_Type = TruthValue
_OspfProcessAreaBackboneArea_Object = MibTableColumn
ospfProcessAreaBackboneArea = _OspfProcessAreaBackboneArea_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 2),
    _OspfProcessAreaBackboneArea_Type()
)
ospfProcessAreaBackboneArea.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaBackboneArea.setStatus("current")


class _OspfProcessAreaRoutingType_Type(Integer32):
    """Custom type ospfProcessAreaRoutingType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("stub", 1),
          ("nssa", 2))
    )


_OspfProcessAreaRoutingType_Type.__name__ = "Integer32"
_OspfProcessAreaRoutingType_Object = MibTableColumn
ospfProcessAreaRoutingType = _OspfProcessAreaRoutingType_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 3),
    _OspfProcessAreaRoutingType_Type()
)
ospfProcessAreaRoutingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaRoutingType.setStatus("current")
_OspfProcessAreaNoSumm_Type = TruthValue
_OspfProcessAreaNoSumm_Object = MibTableColumn
ospfProcessAreaNoSumm = _OspfProcessAreaNoSumm_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 4),
    _OspfProcessAreaNoSumm_Type()
)
ospfProcessAreaNoSumm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaNoSumm.setStatus("current")
_OspfProcessAreaShortcutConfigured_Type = TruthValue
_OspfProcessAreaShortcutConfigured_Object = MibTableColumn
ospfProcessAreaShortcutConfigured = _OspfProcessAreaShortcutConfigured_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 5),
    _OspfProcessAreaShortcutConfigured_Type()
)
ospfProcessAreaShortcutConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaShortcutConfigured.setStatus("current")


class _OspfProcessAreaShortcutMode_Type(Integer32):
    """Custom type ospfProcessAreaShortcutMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("enable", 1),
          ("disable", 2))
    )


_OspfProcessAreaShortcutMode_Type.__name__ = "Integer32"
_OspfProcessAreaShortcutMode_Object = MibTableColumn
ospfProcessAreaShortcutMode = _OspfProcessAreaShortcutMode_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 6),
    _OspfProcessAreaShortcutMode_Type()
)
ospfProcessAreaShortcutMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaShortcutMode.setStatus("current")
_OspfProcessAreaShortcutCapability_Type = TruthValue
_OspfProcessAreaShortcutCapability_Object = MibTableColumn
ospfProcessAreaShortcutCapability = _OspfProcessAreaShortcutCapability_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 7),
    _OspfProcessAreaShortcutCapability_Type()
)
ospfProcessAreaShortcutCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaShortcutCapability.setStatus("current")
_OspfProcessAreaNumInterfaces_Type = Unsigned32
_OspfProcessAreaNumInterfaces_Object = MibTableColumn
ospfProcessAreaNumInterfaces = _OspfProcessAreaNumInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 8),
    _OspfProcessAreaNumInterfaces_Type()
)
ospfProcessAreaNumInterfaces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaNumInterfaces.setStatus("current")
_OspfProcessAreaAbr_Type = TruthValue
_OspfProcessAreaAbr_Object = MibTableColumn
ospfProcessAreaAbr = _OspfProcessAreaAbr_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 9),
    _OspfProcessAreaAbr_Type()
)
ospfProcessAreaAbr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaAbr.setStatus("current")
_OspfProcessAreaNssaTranslate_Type = TruthValue
_OspfProcessAreaNssaTranslate_Object = MibTableColumn
ospfProcessAreaNssaTranslate = _OspfProcessAreaNssaTranslate_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 10),
    _OspfProcessAreaNssaTranslate_Type()
)
ospfProcessAreaNssaTranslate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaNssaTranslate.setStatus("current")


class _OspfProcessAreaTranslateRole_Type(Integer32):
    """Custom type ospfProcessAreaTranslateRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("candidate", 0),
          ("never", 1),
          ("always", 2))
    )


_OspfProcessAreaTranslateRole_Type.__name__ = "Integer32"
_OspfProcessAreaTranslateRole_Object = MibTableColumn
ospfProcessAreaTranslateRole = _OspfProcessAreaTranslateRole_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 11),
    _OspfProcessAreaTranslateRole_Type()
)
ospfProcessAreaTranslateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaTranslateRole.setStatus("current")
_OspfProcessAreaStubRoute_Type = TruthValue
_OspfProcessAreaStubRoute_Object = MibTableColumn
ospfProcessAreaStubRoute = _OspfProcessAreaStubRoute_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 12),
    _OspfProcessAreaStubRoute_Type()
)
ospfProcessAreaStubRoute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaStubRoute.setStatus("current")
_OspfProcessAreaStubRouteAdmin_Type = TruthValue
_OspfProcessAreaStubRouteAdmin_Object = MibTableColumn
ospfProcessAreaStubRouteAdmin = _OspfProcessAreaStubRouteAdmin_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 13),
    _OspfProcessAreaStubRouteAdmin_Type()
)
ospfProcessAreaStubRouteAdmin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaStubRouteAdmin.setStatus("current")
_OspfProcessAreaStubRouteTimer_Type = Unsigned32
_OspfProcessAreaStubRouteTimer_Object = MibTableColumn
ospfProcessAreaStubRouteTimer = _OspfProcessAreaStubRouteTimer_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 14),
    _OspfProcessAreaStubRouteTimer_Type()
)
ospfProcessAreaStubRouteTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaStubRouteTimer.setStatus("current")
_OspfProcessAreaNumFullAdjRouters_Type = Unsigned32
_OspfProcessAreaNumFullAdjRouters_Object = MibTableColumn
ospfProcessAreaNumFullAdjRouters = _OspfProcessAreaNumFullAdjRouters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 15),
    _OspfProcessAreaNumFullAdjRouters_Type()
)
ospfProcessAreaNumFullAdjRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaNumFullAdjRouters.setStatus("current")


class _OspfProcessAreaAuthentication_Type(Integer32):
    """Custom type ospfProcessAreaAuthentication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("simple", 1),
          ("message-digest", 2))
    )


_OspfProcessAreaAuthentication_Type.__name__ = "Integer32"
_OspfProcessAreaAuthentication_Object = MibTableColumn
ospfProcessAreaAuthentication = _OspfProcessAreaAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 16),
    _OspfProcessAreaAuthentication_Type()
)
ospfProcessAreaAuthentication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaAuthentication.setStatus("current")
_OspfProcessAreaNumVirtualAdjRouters_Type = Unsigned32
_OspfProcessAreaNumVirtualAdjRouters_Object = MibTableColumn
ospfProcessAreaNumVirtualAdjRouters = _OspfProcessAreaNumVirtualAdjRouters_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 17),
    _OspfProcessAreaNumVirtualAdjRouters_Type()
)
ospfProcessAreaNumVirtualAdjRouters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaNumVirtualAdjRouters.setStatus("current")
_OspfProcessAreaSpfExecCount_Type = Unsigned32
_OspfProcessAreaSpfExecCount_Object = MibTableColumn
ospfProcessAreaSpfExecCount = _OspfProcessAreaSpfExecCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 18),
    _OspfProcessAreaSpfExecCount_Type()
)
ospfProcessAreaSpfExecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaSpfExecCount.setStatus("current")
_OspfProcessAreaLsaCount_Type = Unsigned32
_OspfProcessAreaLsaCount_Object = MibTableColumn
ospfProcessAreaLsaCount = _OspfProcessAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 19),
    _OspfProcessAreaLsaCount_Type()
)
ospfProcessAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaLsaCount.setStatus("current")
_OspfProcessAreaRouterLsaCount_Type = Unsigned32
_OspfProcessAreaRouterLsaCount_Object = MibTableColumn
ospfProcessAreaRouterLsaCount = _OspfProcessAreaRouterLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 20),
    _OspfProcessAreaRouterLsaCount_Type()
)
ospfProcessAreaRouterLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaRouterLsaCount.setStatus("current")
_OspfProcessAreaRouterLsaChecksum_Type = Unsigned32
_OspfProcessAreaRouterLsaChecksum_Object = MibTableColumn
ospfProcessAreaRouterLsaChecksum = _OspfProcessAreaRouterLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 21),
    _OspfProcessAreaRouterLsaChecksum_Type()
)
ospfProcessAreaRouterLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaRouterLsaChecksum.setStatus("current")
_OspfProcessAreaNetworkLsaCount_Type = Unsigned32
_OspfProcessAreaNetworkLsaCount_Object = MibTableColumn
ospfProcessAreaNetworkLsaCount = _OspfProcessAreaNetworkLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 22),
    _OspfProcessAreaNetworkLsaCount_Type()
)
ospfProcessAreaNetworkLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaNetworkLsaCount.setStatus("current")
_OspfProcessAreaNetworkLsaChecksum_Type = Unsigned32
_OspfProcessAreaNetworkLsaChecksum_Object = MibTableColumn
ospfProcessAreaNetworkLsaChecksum = _OspfProcessAreaNetworkLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 23),
    _OspfProcessAreaNetworkLsaChecksum_Type()
)
ospfProcessAreaNetworkLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaNetworkLsaChecksum.setStatus("current")
_OspfProcessAreaSummaryLsaCount_Type = Unsigned32
_OspfProcessAreaSummaryLsaCount_Object = MibTableColumn
ospfProcessAreaSummaryLsaCount = _OspfProcessAreaSummaryLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 24),
    _OspfProcessAreaSummaryLsaCount_Type()
)
ospfProcessAreaSummaryLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaSummaryLsaCount.setStatus("current")
_OspfProcessAreaSummaryLsaChecksum_Type = Unsigned32
_OspfProcessAreaSummaryLsaChecksum_Object = MibTableColumn
ospfProcessAreaSummaryLsaChecksum = _OspfProcessAreaSummaryLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 25),
    _OspfProcessAreaSummaryLsaChecksum_Type()
)
ospfProcessAreaSummaryLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaSummaryLsaChecksum.setStatus("current")
_OspfProcessAreaAsbrLsaCount_Type = Unsigned32
_OspfProcessAreaAsbrLsaCount_Object = MibTableColumn
ospfProcessAreaAsbrLsaCount = _OspfProcessAreaAsbrLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 26),
    _OspfProcessAreaAsbrLsaCount_Type()
)
ospfProcessAreaAsbrLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaAsbrLsaCount.setStatus("current")
_OspfProcessAreaAsbrLsaChecksum_Type = Unsigned32
_OspfProcessAreaAsbrLsaChecksum_Object = MibTableColumn
ospfProcessAreaAsbrLsaChecksum = _OspfProcessAreaAsbrLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 27),
    _OspfProcessAreaAsbrLsaChecksum_Type()
)
ospfProcessAreaAsbrLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaAsbrLsaChecksum.setStatus("current")
_OspfProcessAreaNssaLsaCount_Type = Unsigned32
_OspfProcessAreaNssaLsaCount_Object = MibTableColumn
ospfProcessAreaNssaLsaCount = _OspfProcessAreaNssaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 28),
    _OspfProcessAreaNssaLsaCount_Type()
)
ospfProcessAreaNssaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaNssaLsaCount.setStatus("current")
_OspfProcessAreaNssaLsaChecksum_Type = Unsigned32
_OspfProcessAreaNssaLsaChecksum_Object = MibTableColumn
ospfProcessAreaNssaLsaChecksum = _OspfProcessAreaNssaLsaChecksum_Object(
    (1, 3, 6, 1, 4, 1, 41916, 13, 12, 1, 29),
    _OspfProcessAreaNssaLsaChecksum_Type()
)
ospfProcessAreaNssaLsaChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfProcessAreaNssaLsaChecksum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VIPTELA-OPER-OSPF",
    **{"UnsignedByte": UnsignedByte,
       "ConfdString": ConfdString,
       "Ipv4Prefix": Ipv4Prefix,
       "String": String,
       "OspfNeighborOptions": OspfNeighborOptions,
       "OspfDbRlsaFlags": OspfDbRlsaFlags,
       "viptela-oper-ospf": viptela_oper_ospf,
       "ospf": ospf,
       "ospfNeighborTable": ospfNeighborTable,
       "ospfNeighborEntry": ospfNeighborEntry,
       "ospfNeighborVpnId": ospfNeighborVpnId,
       "ospfNeighborSource": ospfNeighborSource,
       "ospfNeighborIfIndex": ospfNeighborIfIndex,
       "ospfNeighborIfName": ospfNeighborIfName,
       "ospfNeighborRouterId": ospfNeighborRouterId,
       "ospfNeighborIfAddress": ospfNeighborIfAddress,
       "ospfNeighborArea": ospfNeighborArea,
       "ospfNeighborAreaType": ospfNeighborAreaType,
       "ospfNeighborNeighborState": ospfNeighborNeighborState,
       "ospfNeighborInterfaceState": ospfNeighborInterfaceState,
       "ospfNeighborPriority": ospfNeighborPriority,
       "ospfNeighborStateChanges": ospfNeighborStateChanges,
       "ospfNeighborProgressiveChangeTime": ospfNeighborProgressiveChangeTime,
       "ospfNeighborRegressiveChangeTime": ospfNeighborRegressiveChangeTime,
       "ospfNeighborRegressiveChangeReason": ospfNeighborRegressiveChangeReason,
       "ospfNeighborDesignatedRouterId": ospfNeighborDesignatedRouterId,
       "ospfNeighborBackupDesignatedRouterId": ospfNeighborBackupDesignatedRouterId,
       "ospfNeighborDeadTimer": ospfNeighborDeadTimer,
       "ospfNeighborDbSummaryList": ospfNeighborDbSummaryList,
       "ospfNeighborLinkStateReqList": ospfNeighborLinkStateReqList,
       "ospfNeighborLinkStateRetransList": ospfNeighborLinkStateRetransList,
       "ospfNeighborOptions": ospfNeighborOptions,
       "ospfInterfaceTable": ospfInterfaceTable,
       "ospfInterfaceEntry": ospfInterfaceEntry,
       "ospfInterfaceVpnId": ospfInterfaceVpnId,
       "ospfInterfaceIfAddr": ospfInterfaceIfAddr,
       "ospfInterfaceIfIndex": ospfInterfaceIfIndex,
       "ospfInterfaceIfName": ospfInterfaceIfName,
       "ospfInterfaceMtu": ospfInterfaceMtu,
       "ospfInterfaceBandwidth": ospfInterfaceBandwidth,
       "ospfInterfaceBroadcastAddr": ospfInterfaceBroadcastAddr,
       "ospfInterfaceAreaAddr": ospfInterfaceAreaAddr,
       "ospfInterfaceMtuMismatch": ospfInterfaceMtuMismatch,
       "ospfInterfaceRouterId": ospfInterfaceRouterId,
       "ospfInterfaceIfType": ospfInterfaceIfType,
       "ospfInterfaceCost": ospfInterfaceCost,
       "ospfInterfaceDelay": ospfInterfaceDelay,
       "ospfInterfaceOspfIfState": ospfInterfaceOspfIfState,
       "ospfInterfacePriority": ospfInterfacePriority,
       "ospfInterfaceDesignatedRouterId": ospfInterfaceDesignatedRouterId,
       "ospfInterfaceBackupDesignatedRouterId": ospfInterfaceBackupDesignatedRouterId,
       "ospfInterfaceDesignatedRouterIp": ospfInterfaceDesignatedRouterIp,
       "ospfInterfaceBackupDesignatedRouterIp": ospfInterfaceBackupDesignatedRouterIp,
       "ospfInterfaceLsaSeqnum": ospfInterfaceLsaSeqnum,
       "ospfInterfaceMembers": ospfInterfaceMembers,
       "ospfInterfaceHelloTimer": ospfInterfaceHelloTimer,
       "ospfInterfaceDeadInterval": ospfInterfaceDeadInterval,
       "ospfInterfaceRetransmitTimer": ospfInterfaceRetransmitTimer,
       "ospfInterfaceNeighborCount": ospfInterfaceNeighborCount,
       "ospfInterfaceAdjNeighborCount": ospfInterfaceAdjNeighborCount,
       "ospfInterfaceHelloDueTime": ospfInterfaceHelloDueTime,
       "ospfInterfaceOperState": ospfInterfaceOperState,
       "ospfInterfaceMd5KeyId": ospfInterfaceMd5KeyId,
       "ospfInterfaceMd5Key": ospfInterfaceMd5Key,
       "ospfDatabaseTable": ospfDatabaseTable,
       "ospfDatabaseEntry": ospfDatabaseEntry,
       "ospfDatabaseVpnId": ospfDatabaseVpnId,
       "ospfDatabaseArea": ospfDatabaseArea,
       "ospfDatabaseLsaType": ospfDatabaseLsaType,
       "ospfDatabaseLinkId": ospfDatabaseLinkId,
       "ospfDatabaseAdvRouter": ospfDatabaseAdvRouter,
       "ospfDatabaseChecksum": ospfDatabaseChecksum,
       "ospfDatabaseAge": ospfDatabaseAge,
       "ospfDatabaseSequence": ospfDatabaseSequence,
       "ospfDatabaseLength": ospfDatabaseLength,
       "ospfDatabaseOptions": ospfDatabaseOptions,
       "ospfDatabaseOptionsFlags": ospfDatabaseOptionsFlags,
       "ospfDatabaseFlags": ospfDatabaseFlags,
       "ospfDatabaseRlsaFlags": ospfDatabaseRlsaFlags,
       "ospfDatabaseRlsaFlagsValue": ospfDatabaseRlsaFlagsValue,
       "ospfDatabasePrefix": ospfDatabasePrefix,
       "ospfDatabaseTag": ospfDatabaseTag,
       "ospfDatabaseMetricType": ospfDatabaseMetricType,
       "ospfDatabaseMask": ospfDatabaseMask,
       "ospfDatabaseMetric": ospfDatabaseMetric,
       "ospfDatabaseForwardingAddr": ospfDatabaseForwardingAddr,
       "ospfDatabaseLinkCount": ospfDatabaseLinkCount,
       "ospfDatabaseRouterLinkTable": ospfDatabaseRouterLinkTable,
       "ospfDatabaseRouterLinkEntry": ospfDatabaseRouterLinkEntry,
       "ospfDatabaseRouterLinkLinkIndex": ospfDatabaseRouterLinkLinkIndex,
       "ospfDatabaseRouterLinkRouterLinkId": ospfDatabaseRouterLinkRouterLinkId,
       "ospfDatabaseRouterLinkData": ospfDatabaseRouterLinkData,
       "ospfDatabaseRouterLinkTosMetric": ospfDatabaseRouterLinkTosMetric,
       "ospfDatabaseRouterLinkRouterLinkType": ospfDatabaseRouterLinkRouterLinkType,
       "ospfDatabaseNetworkLinkTable": ospfDatabaseNetworkLinkTable,
       "ospfDatabaseNetworkLinkEntry": ospfDatabaseNetworkLinkEntry,
       "ospfDatabaseNetworkLinkLinkIndex": ospfDatabaseNetworkLinkLinkIndex,
       "ospfDatabaseNetworkLinkNetworkLinkId": ospfDatabaseNetworkLinkNetworkLinkId,
       "ospfExternalDatabaseTable": ospfExternalDatabaseTable,
       "ospfExternalDatabaseEntry": ospfExternalDatabaseEntry,
       "ospfExternalDatabaseVpnId": ospfExternalDatabaseVpnId,
       "ospfExternalDatabaseLinkId": ospfExternalDatabaseLinkId,
       "ospfExternalDatabaseAdvRouter": ospfExternalDatabaseAdvRouter,
       "ospfExternalDatabaseChecksum": ospfExternalDatabaseChecksum,
       "ospfExternalDatabaseAge": ospfExternalDatabaseAge,
       "ospfExternalDatabaseSequence": ospfExternalDatabaseSequence,
       "ospfExternalDatabaseLength": ospfExternalDatabaseLength,
       "ospfExternalDatabaseOptions": ospfExternalDatabaseOptions,
       "ospfExternalDatabaseOptionsFlags": ospfExternalDatabaseOptionsFlags,
       "ospfExternalDatabaseFlags": ospfExternalDatabaseFlags,
       "ospfExternalDatabasePrefix": ospfExternalDatabasePrefix,
       "ospfExternalDatabaseTag": ospfExternalDatabaseTag,
       "ospfExternalDatabaseMetricType": ospfExternalDatabaseMetricType,
       "ospfExternalDatabaseMask": ospfExternalDatabaseMask,
       "ospfExternalDatabaseMetric": ospfExternalDatabaseMetric,
       "ospfExternalDatabaseForwardingAddr": ospfExternalDatabaseForwardingAddr,
       "ospfRoutesTableTable": ospfRoutesTableTable,
       "ospfRoutesTableEntry": ospfRoutesTableEntry,
       "ospfRoutesTableVpnId": ospfRoutesTableVpnId,
       "ospfRoutesTableRouteType": ospfRoutesTableRouteType,
       "ospfRoutesTablePrefix": ospfRoutesTablePrefix,
       "ospfRoutesTableInfoTable": ospfRoutesTableInfoTable,
       "ospfRoutesTableInfoEntry": ospfRoutesTableInfoEntry,
       "ospfRoutesTableInfoInfoId": ospfRoutesTableInfoInfoId,
       "ospfRoutesTableInfoAreaId": ospfRoutesTableInfoAreaId,
       "ospfRoutesTableInfoCost": ospfRoutesTableInfoCost,
       "ospfRoutesTableInfoFlags": ospfRoutesTableInfoFlags,
       "ospfRoutesTableInfoPathType": ospfRoutesTableInfoPathType,
       "ospfRoutesTableInfoDestType": ospfRoutesTableInfoDestType,
       "ospfRoutesTableInfoTag": ospfRoutesTableInfoTag,
       "ospfRoutesTableInfoType2Cost": ospfRoutesTableInfoType2Cost,
       "ospfRoutesTableInfoNextHop": ospfRoutesTableInfoNextHop,
       "ospfRoutesTableInfoIfName": ospfRoutesTableInfoIfName,
       "ospfDatabaseSummaryTable": ospfDatabaseSummaryTable,
       "ospfDatabaseSummaryEntry": ospfDatabaseSummaryEntry,
       "ospfDatabaseSummaryVpnId": ospfDatabaseSummaryVpnId,
       "ospfDatabaseSummaryAreaId": ospfDatabaseSummaryAreaId,
       "ospfDatabaseSummaryRouterLsa": ospfDatabaseSummaryRouterLsa,
       "ospfDatabaseSummaryNetworkLsa": ospfDatabaseSummaryNetworkLsa,
       "ospfDatabaseSummarySummaryLsa": ospfDatabaseSummarySummaryLsa,
       "ospfDatabaseSummaryAsExternalLsa": ospfDatabaseSummaryAsExternalLsa,
       "ospfDatabaseSummaryNssaLsa": ospfDatabaseSummaryNssaLsa,
       "ospfDatabaseSummaryTotalLsa": ospfDatabaseSummaryTotalLsa,
       "ospfProcessTable": ospfProcessTable,
       "ospfProcessEntry": ospfProcessEntry,
       "ospfProcessVpnId": ospfProcessVpnId,
       "ospfProcessRouterId": ospfProcessRouterId,
       "ospfProcessDeferredShutdown": ospfProcessDeferredShutdown,
       "ospfProcessRfc1583Compatible": ospfProcessRfc1583Compatible,
       "ospfProcessStubRouterAdv": ospfProcessStubRouterAdv,
       "ospfProcessStubRouterStart": ospfProcessStubRouterStart,
       "ospfProcessStubRouterShut": ospfProcessStubRouterShut,
       "ospfProcessSpfDelay": ospfProcessSpfDelay,
       "ospfProcessSpfHoldtime": ospfProcessSpfHoldtime,
       "ospfProcessSpfMaxHoldtime": ospfProcessSpfMaxHoldtime,
       "ospfProcessSpfHoldMultiplier": ospfProcessSpfHoldMultiplier,
       "ospfProcessSpfLastExecTime": ospfProcessSpfLastExecTime,
       "ospfProcessSpfNextDueTime": ospfProcessSpfNextDueTime,
       "ospfProcessLsaRefreshInterval": ospfProcessLsaRefreshInterval,
       "ospfProcessAsbrRouter": ospfProcessAsbrRouter,
       "ospfProcessExternalLsaCount": ospfProcessExternalLsaCount,
       "ospfProcessExternalLsaChecksum": ospfProcessExternalLsaChecksum,
       "ospfProcessNumberAreas": ospfProcessNumberAreas,
       "ospfProcessLogAdjChanges": ospfProcessLogAdjChanges,
       "ospfProcessIgnoreDownBit": ospfProcessIgnoreDownBit,
       "ospfProcessHelloReceived": ospfProcessHelloReceived,
       "ospfProcessHelloSent": ospfProcessHelloSent,
       "ospfProcessDbdReceived": ospfProcessDbdReceived,
       "ospfProcessDbdSent": ospfProcessDbdSent,
       "ospfProcessLsReqReceived": ospfProcessLsReqReceived,
       "ospfProcessLsReqSent": ospfProcessLsReqSent,
       "ospfProcessLsUpdReceived": ospfProcessLsUpdReceived,
       "ospfProcessLsUpdSent": ospfProcessLsUpdSent,
       "ospfProcessLsAckReceived": ospfProcessLsAckReceived,
       "ospfProcessLsAckSent": ospfProcessLsAckSent,
       "ospfProcessAreaTable": ospfProcessAreaTable,
       "ospfProcessAreaEntry": ospfProcessAreaEntry,
       "ospfProcessAreaAreaId": ospfProcessAreaAreaId,
       "ospfProcessAreaBackboneArea": ospfProcessAreaBackboneArea,
       "ospfProcessAreaRoutingType": ospfProcessAreaRoutingType,
       "ospfProcessAreaNoSumm": ospfProcessAreaNoSumm,
       "ospfProcessAreaShortcutConfigured": ospfProcessAreaShortcutConfigured,
       "ospfProcessAreaShortcutMode": ospfProcessAreaShortcutMode,
       "ospfProcessAreaShortcutCapability": ospfProcessAreaShortcutCapability,
       "ospfProcessAreaNumInterfaces": ospfProcessAreaNumInterfaces,
       "ospfProcessAreaAbr": ospfProcessAreaAbr,
       "ospfProcessAreaNssaTranslate": ospfProcessAreaNssaTranslate,
       "ospfProcessAreaTranslateRole": ospfProcessAreaTranslateRole,
       "ospfProcessAreaStubRoute": ospfProcessAreaStubRoute,
       "ospfProcessAreaStubRouteAdmin": ospfProcessAreaStubRouteAdmin,
       "ospfProcessAreaStubRouteTimer": ospfProcessAreaStubRouteTimer,
       "ospfProcessAreaNumFullAdjRouters": ospfProcessAreaNumFullAdjRouters,
       "ospfProcessAreaAuthentication": ospfProcessAreaAuthentication,
       "ospfProcessAreaNumVirtualAdjRouters": ospfProcessAreaNumVirtualAdjRouters,
       "ospfProcessAreaSpfExecCount": ospfProcessAreaSpfExecCount,
       "ospfProcessAreaLsaCount": ospfProcessAreaLsaCount,
       "ospfProcessAreaRouterLsaCount": ospfProcessAreaRouterLsaCount,
       "ospfProcessAreaRouterLsaChecksum": ospfProcessAreaRouterLsaChecksum,
       "ospfProcessAreaNetworkLsaCount": ospfProcessAreaNetworkLsaCount,
       "ospfProcessAreaNetworkLsaChecksum": ospfProcessAreaNetworkLsaChecksum,
       "ospfProcessAreaSummaryLsaCount": ospfProcessAreaSummaryLsaCount,
       "ospfProcessAreaSummaryLsaChecksum": ospfProcessAreaSummaryLsaChecksum,
       "ospfProcessAreaAsbrLsaCount": ospfProcessAreaAsbrLsaCount,
       "ospfProcessAreaAsbrLsaChecksum": ospfProcessAreaAsbrLsaChecksum,
       "ospfProcessAreaNssaLsaCount": ospfProcessAreaNssaLsaCount,
       "ospfProcessAreaNssaLsaChecksum": ospfProcessAreaNssaLsaChecksum}
)
