# SNMP MIB module (DLINKSW-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dlink\DLINKSW-ACL-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:36:39 2025
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

(dlinkIndustrialCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkIndustrialCommon")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

(VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId",
    "VlanIdOrNone")

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

dlinkSwAclMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28)
)
if mibBuilder.loadTexts:
    dlinkSwAclMIB.setRevisions(
        ("2015-11-26 00:00",
         "2015-07-10 00:00",
         "2014-01-21 00:00",
         "2013-11-13 00:00",
         "2013-08-20 00:00",
         "2013-02-08 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlinkAclRuleType(TextualConvention, Integer32):
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
        *(("permit", 1),
          ("deny", 2),
          ("deny-cpu", 3))
    )



class DlinkAclPortOperatorType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("eq", 2),
          ("gt", 3),
          ("lt", 4),
          ("neq", 5),
          ("range", 6),
          ("mask", 7))
    )



class TcpFlag(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("urgent", 0),
          ("acknowledge", 1),
          ("push", 2),
          ("reset", 3),
          ("synchronize", 4),
          ("finish", 5))
    )


# MIB Managed Objects in the order of their OIDs

_DAclMIBNotifications_ObjectIdentity = ObjectIdentity
dAclMIBNotifications = _DAclMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 0)
)
_DAclMIBObjects_ObjectIdentity = ObjectIdentity
dAclMIBObjects = _DAclMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1)
)
_DAclGeneral_ObjectIdentity = ObjectIdentity
dAclGeneral = _DAclGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 1)
)
_DAclReSeqTable_Object = MibTable
dAclReSeqTable = _DAclReSeqTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dAclReSeqTable.setStatus("current")
_DAclReSeqEntry_Object = MibTableRow
dAclReSeqEntry = _DAclReSeqEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 1, 1, 1)
)
dAclReSeqEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclReSeqAccessListName"),
)
if mibBuilder.loadTexts:
    dAclReSeqEntry.setStatus("current")


class _DAclReSeqAccessListName_Type(DisplayString):
    """Custom type dAclReSeqAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclReSeqAccessListName_Type.__name__ = "DisplayString"
_DAclReSeqAccessListName_Object = MibTableColumn
dAclReSeqAccessListName = _DAclReSeqAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 1, 1, 1, 1),
    _DAclReSeqAccessListName_Type()
)
dAclReSeqAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclReSeqAccessListName.setStatus("current")


class _DAclReSeqStartingNumber_Type(Integer32):
    """Custom type dAclReSeqStartingNumber based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DAclReSeqStartingNumber_Type.__name__ = "Integer32"
_DAclReSeqStartingNumber_Object = MibTableColumn
dAclReSeqStartingNumber = _DAclReSeqStartingNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 1, 1, 1, 2),
    _DAclReSeqStartingNumber_Type()
)
dAclReSeqStartingNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dAclReSeqStartingNumber.setStatus("current")


class _DAclReSeqIncrement_Type(Integer32):
    """Custom type dAclReSeqIncrement based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DAclReSeqIncrement_Type.__name__ = "Integer32"
_DAclReSeqIncrement_Object = MibTableColumn
dAclReSeqIncrement = _DAclReSeqIncrement_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 1, 1, 1, 3),
    _DAclReSeqIncrement_Type()
)
dAclReSeqIncrement.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dAclReSeqIncrement.setStatus("current")
_DAclMac_ObjectIdentity = ObjectIdentity
dAclMac = _DAclMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2)
)
_DAclMacAccessListNumber_Type = Unsigned32
_DAclMacAccessListNumber_Object = MibScalar
dAclMacAccessListNumber = _DAclMacAccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 1),
    _DAclMacAccessListNumber_Type()
)
dAclMacAccessListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dAclMacAccessListNumber.setStatus("current")
_DAclMacAccessListTable_Object = MibTable
dAclMacAccessListTable = _DAclMacAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 2)
)
if mibBuilder.loadTexts:
    dAclMacAccessListTable.setStatus("current")
_DAclMacAccessListEntry_Object = MibTableRow
dAclMacAccessListEntry = _DAclMacAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 2, 1)
)
dAclMacAccessListEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclMacAccessListName"),
)
if mibBuilder.loadTexts:
    dAclMacAccessListEntry.setStatus("current")


class _DAclMacAccessListName_Type(DisplayString):
    """Custom type dAclMacAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclMacAccessListName_Type.__name__ = "DisplayString"
_DAclMacAccessListName_Object = MibTableColumn
dAclMacAccessListName = _DAclMacAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 2, 1, 1),
    _DAclMacAccessListName_Type()
)
dAclMacAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclMacAccessListName.setStatus("current")
_DAclMacAccessListRowStatus_Type = RowStatus
_DAclMacAccessListRowStatus_Object = MibTableColumn
dAclMacAccessListRowStatus = _DAclMacAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 2, 1, 2),
    _DAclMacAccessListRowStatus_Type()
)
dAclMacAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessListRowStatus.setStatus("current")
_DAclMacAccessListId_Type = Integer32
_DAclMacAccessListId_Object = MibTableColumn
dAclMacAccessListId = _DAclMacAccessListId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 2, 1, 3),
    _DAclMacAccessListId_Type()
)
dAclMacAccessListId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessListId.setStatus("current")
_DAclMacAccessListCounterEnabled_Type = TruthValue
_DAclMacAccessListCounterEnabled_Object = MibTableColumn
dAclMacAccessListCounterEnabled = _DAclMacAccessListCounterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 2, 1, 4),
    _DAclMacAccessListCounterEnabled_Type()
)
dAclMacAccessListCounterEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessListCounterEnabled.setStatus("current")


class _DAclMacAccessListClearStatAction_Type(Integer32):
    """Custom type dAclMacAccessListClearStatAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DAclMacAccessListClearStatAction_Type.__name__ = "Integer32"
_DAclMacAccessListClearStatAction_Object = MibTableColumn
dAclMacAccessListClearStatAction = _DAclMacAccessListClearStatAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 2, 1, 5),
    _DAclMacAccessListClearStatAction_Type()
)
dAclMacAccessListClearStatAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessListClearStatAction.setStatus("current")


class _DAclMacAccessListRemark_Type(DisplayString):
    """Custom type dAclMacAccessListRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DAclMacAccessListRemark_Type.__name__ = "DisplayString"
_DAclMacAccessListRemark_Object = MibTableColumn
dAclMacAccessListRemark = _DAclMacAccessListRemark_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 2, 1, 6),
    _DAclMacAccessListRemark_Type()
)
dAclMacAccessListRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessListRemark.setStatus("current")
_DAclMacAccessRuleTable_Object = MibTable
dAclMacAccessRuleTable = _DAclMacAccessRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dAclMacAccessRuleTable.setStatus("current")
_DAclMacAccessRuleEntry_Object = MibTableRow
dAclMacAccessRuleEntry = _DAclMacAccessRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1)
)
dAclMacAccessRuleEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclMacAccessListName"),
    (0, "DLINKSW-ACL-MIB", "dAclMacAccessRuleSn"),
)
if mibBuilder.loadTexts:
    dAclMacAccessRuleEntry.setStatus("current")


class _DAclMacAccessRuleSn_Type(Integer32):
    """Custom type dAclMacAccessRuleSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DAclMacAccessRuleSn_Type.__name__ = "Integer32"
_DAclMacAccessRuleSn_Object = MibTableColumn
dAclMacAccessRuleSn = _DAclMacAccessRuleSn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 1),
    _DAclMacAccessRuleSn_Type()
)
dAclMacAccessRuleSn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclMacAccessRuleSn.setStatus("current")
_DAclMacAccessRuleRowStatus_Type = RowStatus
_DAclMacAccessRuleRowStatus_Object = MibTableColumn
dAclMacAccessRuleRowStatus = _DAclMacAccessRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 2),
    _DAclMacAccessRuleRowStatus_Type()
)
dAclMacAccessRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleRowStatus.setStatus("current")
_DAclMacAccessRuleAction_Type = DlinkAclRuleType
_DAclMacAccessRuleAction_Object = MibTableColumn
dAclMacAccessRuleAction = _DAclMacAccessRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 3),
    _DAclMacAccessRuleAction_Type()
)
dAclMacAccessRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleAction.setStatus("current")
_DAclMacAccessRuleSrcMacAddr_Type = MacAddress
_DAclMacAccessRuleSrcMacAddr_Object = MibTableColumn
dAclMacAccessRuleSrcMacAddr = _DAclMacAccessRuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 4),
    _DAclMacAccessRuleSrcMacAddr_Type()
)
dAclMacAccessRuleSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleSrcMacAddr.setStatus("current")
_DAclMacAccessRuleSrcMacWildcard_Type = MacAddress
_DAclMacAccessRuleSrcMacWildcard_Object = MibTableColumn
dAclMacAccessRuleSrcMacWildcard = _DAclMacAccessRuleSrcMacWildcard_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 5),
    _DAclMacAccessRuleSrcMacWildcard_Type()
)
dAclMacAccessRuleSrcMacWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleSrcMacWildcard.setStatus("current")
_DAclMacAccessRuleDstMacAddr_Type = MacAddress
_DAclMacAccessRuleDstMacAddr_Object = MibTableColumn
dAclMacAccessRuleDstMacAddr = _DAclMacAccessRuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 6),
    _DAclMacAccessRuleDstMacAddr_Type()
)
dAclMacAccessRuleDstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleDstMacAddr.setStatus("current")
_DAclMacAccessRuleDstMacWildcard_Type = MacAddress
_DAclMacAccessRuleDstMacWildcard_Object = MibTableColumn
dAclMacAccessRuleDstMacWildcard = _DAclMacAccessRuleDstMacWildcard_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 7),
    _DAclMacAccessRuleDstMacWildcard_Type()
)
dAclMacAccessRuleDstMacWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleDstMacWildcard.setStatus("current")


class _DAclMacAccessRulePacketType_Type(Integer32):
    """Custom type dAclMacAccessRulePacketType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("ethernet", 2),
          ("llc", 3))
    )


_DAclMacAccessRulePacketType_Type.__name__ = "Integer32"
_DAclMacAccessRulePacketType_Object = MibTableColumn
dAclMacAccessRulePacketType = _DAclMacAccessRulePacketType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 8),
    _DAclMacAccessRulePacketType_Type()
)
dAclMacAccessRulePacketType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRulePacketType.setStatus("current")


class _DAclMacAccessRuleEthernetType_Type(Integer32):
    """Custom type dAclMacAccessRuleEthernetType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 65535),
    )


_DAclMacAccessRuleEthernetType_Type.__name__ = "Integer32"
_DAclMacAccessRuleEthernetType_Object = MibTableColumn
dAclMacAccessRuleEthernetType = _DAclMacAccessRuleEthernetType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 9),
    _DAclMacAccessRuleEthernetType_Type()
)
dAclMacAccessRuleEthernetType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleEthernetType.setStatus("current")


class _DAclMacAccessRuleLlcDSAP_Type(Integer32):
    """Custom type dAclMacAccessRuleLlcDSAP based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclMacAccessRuleLlcDSAP_Type.__name__ = "Integer32"
_DAclMacAccessRuleLlcDSAP_Object = MibTableColumn
dAclMacAccessRuleLlcDSAP = _DAclMacAccessRuleLlcDSAP_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 10),
    _DAclMacAccessRuleLlcDSAP_Type()
)
dAclMacAccessRuleLlcDSAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleLlcDSAP.setStatus("obsolete")


class _DAclMacAccessRuleLlcSSAP_Type(Integer32):
    """Custom type dAclMacAccessRuleLlcSSAP based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclMacAccessRuleLlcSSAP_Type.__name__ = "Integer32"
_DAclMacAccessRuleLlcSSAP_Object = MibTableColumn
dAclMacAccessRuleLlcSSAP = _DAclMacAccessRuleLlcSSAP_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 11),
    _DAclMacAccessRuleLlcSSAP_Type()
)
dAclMacAccessRuleLlcSSAP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleLlcSSAP.setStatus("obsolete")


class _DAclMacAccessRuleLlcCntl_Type(Integer32):
    """Custom type dAclMacAccessRuleLlcCntl based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclMacAccessRuleLlcCntl_Type.__name__ = "Integer32"
_DAclMacAccessRuleLlcCntl_Object = MibTableColumn
dAclMacAccessRuleLlcCntl = _DAclMacAccessRuleLlcCntl_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 12),
    _DAclMacAccessRuleLlcCntl_Type()
)
dAclMacAccessRuleLlcCntl.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleLlcCntl.setStatus("obsolete")


class _DAclMacAccessRuleDot1p_Type(Integer32):
    """Custom type dAclMacAccessRuleDot1p based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DAclMacAccessRuleDot1p_Type.__name__ = "Integer32"
_DAclMacAccessRuleDot1p_Object = MibTableColumn
dAclMacAccessRuleDot1p = _DAclMacAccessRuleDot1p_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 13),
    _DAclMacAccessRuleDot1p_Type()
)
dAclMacAccessRuleDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleDot1p.setStatus("current")


class _DAclMacAccessRuleInnerDot1p_Type(Integer32):
    """Custom type dAclMacAccessRuleInnerDot1p based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DAclMacAccessRuleInnerDot1p_Type.__name__ = "Integer32"
_DAclMacAccessRuleInnerDot1p_Object = MibTableColumn
dAclMacAccessRuleInnerDot1p = _DAclMacAccessRuleInnerDot1p_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 14),
    _DAclMacAccessRuleInnerDot1p_Type()
)
dAclMacAccessRuleInnerDot1p.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleInnerDot1p.setStatus("current")


class _DAclMacAccessRuleVlanID_Type(VlanIdOrNone):
    """Custom type dAclMacAccessRuleVlanID based on VlanIdOrNone"""
    defaultValue = 0


_DAclMacAccessRuleVlanID_Type.__name__ = "VlanIdOrNone"
_DAclMacAccessRuleVlanID_Object = MibTableColumn
dAclMacAccessRuleVlanID = _DAclMacAccessRuleVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 15),
    _DAclMacAccessRuleVlanID_Type()
)
dAclMacAccessRuleVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleVlanID.setStatus("current")


class _DAclMacAccessRuleInnerVlanID_Type(VlanIdOrNone):
    """Custom type dAclMacAccessRuleInnerVlanID based on VlanIdOrNone"""
    defaultValue = 0


_DAclMacAccessRuleInnerVlanID_Type.__name__ = "VlanIdOrNone"
_DAclMacAccessRuleInnerVlanID_Object = MibTableColumn
dAclMacAccessRuleInnerVlanID = _DAclMacAccessRuleInnerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 16),
    _DAclMacAccessRuleInnerVlanID_Type()
)
dAclMacAccessRuleInnerVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleInnerVlanID.setStatus("current")
_DAclMacAccessRuleTimeName_Type = DisplayString
_DAclMacAccessRuleTimeName_Object = MibTableColumn
dAclMacAccessRuleTimeName = _DAclMacAccessRuleTimeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 17),
    _DAclMacAccessRuleTimeName_Type()
)
dAclMacAccessRuleTimeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleTimeName.setStatus("current")


class _DAclMacAccessRuleEthernetTypeMask_Type(OctetString):
    """Custom type dAclMacAccessRuleEthernetTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclMacAccessRuleEthernetTypeMask_Type.__name__ = "OctetString"
_DAclMacAccessRuleEthernetTypeMask_Object = MibTableColumn
dAclMacAccessRuleEthernetTypeMask = _DAclMacAccessRuleEthernetTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 18),
    _DAclMacAccessRuleEthernetTypeMask_Type()
)
dAclMacAccessRuleEthernetTypeMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleEthernetTypeMask.setStatus("current")


class _DAclMacAccessRuleDot1pMask_Type(OctetString):
    """Custom type dAclMacAccessRuleDot1pMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclMacAccessRuleDot1pMask_Type.__name__ = "OctetString"
_DAclMacAccessRuleDot1pMask_Object = MibTableColumn
dAclMacAccessRuleDot1pMask = _DAclMacAccessRuleDot1pMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 19),
    _DAclMacAccessRuleDot1pMask_Type()
)
dAclMacAccessRuleDot1pMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleDot1pMask.setStatus("current")


class _DAclMacAccessRuleInnerDot1pMask_Type(OctetString):
    """Custom type dAclMacAccessRuleInnerDot1pMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclMacAccessRuleInnerDot1pMask_Type.__name__ = "OctetString"
_DAclMacAccessRuleInnerDot1pMask_Object = MibTableColumn
dAclMacAccessRuleInnerDot1pMask = _DAclMacAccessRuleInnerDot1pMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 20),
    _DAclMacAccessRuleInnerDot1pMask_Type()
)
dAclMacAccessRuleInnerDot1pMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleInnerDot1pMask.setStatus("current")


class _DAclMacAccessRuleVlanIDMask_Type(OctetString):
    """Custom type dAclMacAccessRuleVlanIDMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclMacAccessRuleVlanIDMask_Type.__name__ = "OctetString"
_DAclMacAccessRuleVlanIDMask_Object = MibTableColumn
dAclMacAccessRuleVlanIDMask = _DAclMacAccessRuleVlanIDMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 21),
    _DAclMacAccessRuleVlanIDMask_Type()
)
dAclMacAccessRuleVlanIDMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleVlanIDMask.setStatus("current")


class _DAclMacAccessRuleInnerVlanIDMask_Type(OctetString):
    """Custom type dAclMacAccessRuleInnerVlanIDMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclMacAccessRuleInnerVlanIDMask_Type.__name__ = "OctetString"
_DAclMacAccessRuleInnerVlanIDMask_Object = MibTableColumn
dAclMacAccessRuleInnerVlanIDMask = _DAclMacAccessRuleInnerVlanIDMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 22),
    _DAclMacAccessRuleInnerVlanIDMask_Type()
)
dAclMacAccessRuleInnerVlanIDMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleInnerVlanIDMask.setStatus("current")


class _DAclMacAccessRuleVlanRangeMin_Type(VlanIdOrNone):
    """Custom type dAclMacAccessRuleVlanRangeMin based on VlanIdOrNone"""
    defaultValue = 0


_DAclMacAccessRuleVlanRangeMin_Type.__name__ = "VlanIdOrNone"
_DAclMacAccessRuleVlanRangeMin_Object = MibTableColumn
dAclMacAccessRuleVlanRangeMin = _DAclMacAccessRuleVlanRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 23),
    _DAclMacAccessRuleVlanRangeMin_Type()
)
dAclMacAccessRuleVlanRangeMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleVlanRangeMin.setStatus("current")


class _DAclMacAccessRuleVlanRangeMax_Type(VlanIdOrNone):
    """Custom type dAclMacAccessRuleVlanRangeMax based on VlanIdOrNone"""
    defaultValue = 0


_DAclMacAccessRuleVlanRangeMax_Type.__name__ = "VlanIdOrNone"
_DAclMacAccessRuleVlanRangeMax_Object = MibTableColumn
dAclMacAccessRuleVlanRangeMax = _DAclMacAccessRuleVlanRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 3, 1, 24),
    _DAclMacAccessRuleVlanRangeMax_Type()
)
dAclMacAccessRuleVlanRangeMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessRuleVlanRangeMax.setStatus("current")
_DAclMacAccessGroupTable_Object = MibTable
dAclMacAccessGroupTable = _DAclMacAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 4)
)
if mibBuilder.loadTexts:
    dAclMacAccessGroupTable.setStatus("current")
_DAclMacAccessGroupEntry_Object = MibTableRow
dAclMacAccessGroupEntry = _DAclMacAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 4, 1)
)
dAclMacAccessGroupEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclMacAccessGroupIfIndex"),
    (0, "DLINKSW-ACL-MIB", "dAclMacAccessGroupApplyDirection"),
)
if mibBuilder.loadTexts:
    dAclMacAccessGroupEntry.setStatus("current")
_DAclMacAccessGroupIfIndex_Type = InterfaceIndex
_DAclMacAccessGroupIfIndex_Object = MibTableColumn
dAclMacAccessGroupIfIndex = _DAclMacAccessGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 4, 1, 1),
    _DAclMacAccessGroupIfIndex_Type()
)
dAclMacAccessGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclMacAccessGroupIfIndex.setStatus("current")


class _DAclMacAccessGroupApplyDirection_Type(Integer32):
    """Custom type dAclMacAccessGroupApplyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_DAclMacAccessGroupApplyDirection_Type.__name__ = "Integer32"
_DAclMacAccessGroupApplyDirection_Object = MibTableColumn
dAclMacAccessGroupApplyDirection = _DAclMacAccessGroupApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 4, 1, 2),
    _DAclMacAccessGroupApplyDirection_Type()
)
dAclMacAccessGroupApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclMacAccessGroupApplyDirection.setStatus("current")
_DAclMacAccessGroupRowStatus_Type = RowStatus
_DAclMacAccessGroupRowStatus_Object = MibTableColumn
dAclMacAccessGroupRowStatus = _DAclMacAccessGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 4, 1, 3),
    _DAclMacAccessGroupRowStatus_Type()
)
dAclMacAccessGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessGroupRowStatus.setStatus("current")


class _DAclMacAccessGroupAclName_Type(DisplayString):
    """Custom type dAclMacAccessGroupAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclMacAccessGroupAclName_Type.__name__ = "DisplayString"
_DAclMacAccessGroupAclName_Object = MibTableColumn
dAclMacAccessGroupAclName = _DAclMacAccessGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 4, 1, 4),
    _DAclMacAccessGroupAclName_Type()
)
dAclMacAccessGroupAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessGroupAclName.setStatus("current")
_DAclMacAccessGroupAclId_Type = Integer32
_DAclMacAccessGroupAclId_Object = MibTableColumn
dAclMacAccessGroupAclId = _DAclMacAccessGroupAclId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 2, 4, 1, 5),
    _DAclMacAccessGroupAclId_Type()
)
dAclMacAccessGroupAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclMacAccessGroupAclId.setStatus("current")
_DAclIp_ObjectIdentity = ObjectIdentity
dAclIp = _DAclIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3)
)
_DAclIpAccessListNumber_Type = Unsigned32
_DAclIpAccessListNumber_Object = MibScalar
dAclIpAccessListNumber = _DAclIpAccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 1),
    _DAclIpAccessListNumber_Type()
)
dAclIpAccessListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dAclIpAccessListNumber.setStatus("current")
_DAclIpAccessListTable_Object = MibTable
dAclIpAccessListTable = _DAclIpAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dAclIpAccessListTable.setStatus("current")
_DAclIpAccessListEntry_Object = MibTableRow
dAclIpAccessListEntry = _DAclIpAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 2, 1)
)
dAclIpAccessListEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclIpAccessListName"),
)
if mibBuilder.loadTexts:
    dAclIpAccessListEntry.setStatus("current")


class _DAclIpAccessListName_Type(DisplayString):
    """Custom type dAclIpAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclIpAccessListName_Type.__name__ = "DisplayString"
_DAclIpAccessListName_Object = MibTableColumn
dAclIpAccessListName = _DAclIpAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 2, 1, 1),
    _DAclIpAccessListName_Type()
)
dAclIpAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclIpAccessListName.setStatus("current")
_DAclIpAccessListRowStatus_Type = RowStatus
_DAclIpAccessListRowStatus_Object = MibTableColumn
dAclIpAccessListRowStatus = _DAclIpAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 2, 1, 2),
    _DAclIpAccessListRowStatus_Type()
)
dAclIpAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessListRowStatus.setStatus("current")
_DAclIpAccessExtended_Type = TruthValue
_DAclIpAccessExtended_Object = MibTableColumn
dAclIpAccessExtended = _DAclIpAccessExtended_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 2, 1, 3),
    _DAclIpAccessExtended_Type()
)
dAclIpAccessExtended.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessExtended.setStatus("current")
_DAclIpAccessListId_Type = Integer32
_DAclIpAccessListId_Object = MibTableColumn
dAclIpAccessListId = _DAclIpAccessListId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 2, 1, 4),
    _DAclIpAccessListId_Type()
)
dAclIpAccessListId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessListId.setStatus("current")
_DAclIpAccessListCounterEnabled_Type = TruthValue
_DAclIpAccessListCounterEnabled_Object = MibTableColumn
dAclIpAccessListCounterEnabled = _DAclIpAccessListCounterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 2, 1, 5),
    _DAclIpAccessListCounterEnabled_Type()
)
dAclIpAccessListCounterEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessListCounterEnabled.setStatus("current")


class _DAclIpAccessListClearStatAction_Type(Integer32):
    """Custom type dAclIpAccessListClearStatAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DAclIpAccessListClearStatAction_Type.__name__ = "Integer32"
_DAclIpAccessListClearStatAction_Object = MibTableColumn
dAclIpAccessListClearStatAction = _DAclIpAccessListClearStatAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 2, 1, 6),
    _DAclIpAccessListClearStatAction_Type()
)
dAclIpAccessListClearStatAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessListClearStatAction.setStatus("current")


class _DAclIpAccessListRemark_Type(DisplayString):
    """Custom type dAclIpAccessListRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DAclIpAccessListRemark_Type.__name__ = "DisplayString"
_DAclIpAccessListRemark_Object = MibTableColumn
dAclIpAccessListRemark = _DAclIpAccessListRemark_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 2, 1, 7),
    _DAclIpAccessListRemark_Type()
)
dAclIpAccessListRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessListRemark.setStatus("current")
_DAclIpAccessRuleTable_Object = MibTable
dAclIpAccessRuleTable = _DAclIpAccessRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dAclIpAccessRuleTable.setStatus("current")
_DAclIpAccessRuleEntry_Object = MibTableRow
dAclIpAccessRuleEntry = _DAclIpAccessRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1)
)
dAclIpAccessRuleEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclIpAccessListName"),
    (0, "DLINKSW-ACL-MIB", "dAclIpAccessRuleSn"),
)
if mibBuilder.loadTexts:
    dAclIpAccessRuleEntry.setStatus("current")


class _DAclIpAccessRuleSn_Type(Integer32):
    """Custom type dAclIpAccessRuleSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DAclIpAccessRuleSn_Type.__name__ = "Integer32"
_DAclIpAccessRuleSn_Object = MibTableColumn
dAclIpAccessRuleSn = _DAclIpAccessRuleSn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 1),
    _DAclIpAccessRuleSn_Type()
)
dAclIpAccessRuleSn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclIpAccessRuleSn.setStatus("current")
_DAclIpAccessRuleRowStatus_Type = RowStatus
_DAclIpAccessRuleRowStatus_Object = MibTableColumn
dAclIpAccessRuleRowStatus = _DAclIpAccessRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 2),
    _DAclIpAccessRuleRowStatus_Type()
)
dAclIpAccessRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleRowStatus.setStatus("current")
_DAclIpAccessRuleAction_Type = DlinkAclRuleType
_DAclIpAccessRuleAction_Object = MibTableColumn
dAclIpAccessRuleAction = _DAclIpAccessRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 3),
    _DAclIpAccessRuleAction_Type()
)
dAclIpAccessRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleAction.setStatus("current")


class _DAclIpAccessRuleProtocol_Type(Integer32):
    """Custom type dAclIpAccessRuleProtocol based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("userDefine", 1),
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4),
          ("gre", 5),
          ("esp", 6),
          ("eigrp", 7),
          ("igmp", 8),
          ("ospf", 9),
          ("pim", 10),
          ("vrrp", 11),
          ("ipinip", 12),
          ("pcp", 13))
    )


_DAclIpAccessRuleProtocol_Type.__name__ = "Integer32"
_DAclIpAccessRuleProtocol_Object = MibTableColumn
dAclIpAccessRuleProtocol = _DAclIpAccessRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 4),
    _DAclIpAccessRuleProtocol_Type()
)
dAclIpAccessRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleProtocol.setStatus("current")


class _DAclIpAccessRuleUserDefProtocol_Type(Integer32):
    """Custom type dAclIpAccessRuleUserDefProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclIpAccessRuleUserDefProtocol_Type.__name__ = "Integer32"
_DAclIpAccessRuleUserDefProtocol_Object = MibTableColumn
dAclIpAccessRuleUserDefProtocol = _DAclIpAccessRuleUserDefProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 5),
    _DAclIpAccessRuleUserDefProtocol_Type()
)
dAclIpAccessRuleUserDefProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleUserDefProtocol.setStatus("current")
_DAclIpAccessRuleSrcAddr_Type = IpAddress
_DAclIpAccessRuleSrcAddr_Object = MibTableColumn
dAclIpAccessRuleSrcAddr = _DAclIpAccessRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 6),
    _DAclIpAccessRuleSrcAddr_Type()
)
dAclIpAccessRuleSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleSrcAddr.setStatus("current")
_DAclIpAccessRuleSrcWildcard_Type = IpAddress
_DAclIpAccessRuleSrcWildcard_Object = MibTableColumn
dAclIpAccessRuleSrcWildcard = _DAclIpAccessRuleSrcWildcard_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 7),
    _DAclIpAccessRuleSrcWildcard_Type()
)
dAclIpAccessRuleSrcWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleSrcWildcard.setStatus("current")
_DAclIpAccessRuleDstAddr_Type = IpAddress
_DAclIpAccessRuleDstAddr_Object = MibTableColumn
dAclIpAccessRuleDstAddr = _DAclIpAccessRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 8),
    _DAclIpAccessRuleDstAddr_Type()
)
dAclIpAccessRuleDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleDstAddr.setStatus("current")
_DAclIpAccessRuleDstWildcard_Type = IpAddress
_DAclIpAccessRuleDstWildcard_Object = MibTableColumn
dAclIpAccessRuleDstWildcard = _DAclIpAccessRuleDstWildcard_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 9),
    _DAclIpAccessRuleDstWildcard_Type()
)
dAclIpAccessRuleDstWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleDstWildcard.setStatus("current")
_DAclIpAccessRuleSrcOperator_Type = DlinkAclPortOperatorType
_DAclIpAccessRuleSrcOperator_Object = MibTableColumn
dAclIpAccessRuleSrcOperator = _DAclIpAccessRuleSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 10),
    _DAclIpAccessRuleSrcOperator_Type()
)
dAclIpAccessRuleSrcOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleSrcOperator.setStatus("current")


class _DAclIpAccessRuleSrcPort_Type(Integer32):
    """Custom type dAclIpAccessRuleSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclIpAccessRuleSrcPort_Type.__name__ = "Integer32"
_DAclIpAccessRuleSrcPort_Object = MibTableColumn
dAclIpAccessRuleSrcPort = _DAclIpAccessRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 11),
    _DAclIpAccessRuleSrcPort_Type()
)
dAclIpAccessRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleSrcPort.setStatus("current")


class _DAclIpAccessRuleSrcPortRange_Type(Integer32):
    """Custom type dAclIpAccessRuleSrcPortRange based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclIpAccessRuleSrcPortRange_Type.__name__ = "Integer32"
_DAclIpAccessRuleSrcPortRange_Object = MibTableColumn
dAclIpAccessRuleSrcPortRange = _DAclIpAccessRuleSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 12),
    _DAclIpAccessRuleSrcPortRange_Type()
)
dAclIpAccessRuleSrcPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleSrcPortRange.setStatus("current")
_DAclIpAccessRuleDstOperator_Type = DlinkAclPortOperatorType
_DAclIpAccessRuleDstOperator_Object = MibTableColumn
dAclIpAccessRuleDstOperator = _DAclIpAccessRuleDstOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 13),
    _DAclIpAccessRuleDstOperator_Type()
)
dAclIpAccessRuleDstOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleDstOperator.setStatus("current")


class _DAclIpAccessRuleDstPort_Type(Integer32):
    """Custom type dAclIpAccessRuleDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclIpAccessRuleDstPort_Type.__name__ = "Integer32"
_DAclIpAccessRuleDstPort_Object = MibTableColumn
dAclIpAccessRuleDstPort = _DAclIpAccessRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 14),
    _DAclIpAccessRuleDstPort_Type()
)
dAclIpAccessRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleDstPort.setStatus("current")


class _DAclIpAccessRuleDstPortRange_Type(Integer32):
    """Custom type dAclIpAccessRuleDstPortRange based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclIpAccessRuleDstPortRange_Type.__name__ = "Integer32"
_DAclIpAccessRuleDstPortRange_Object = MibTableColumn
dAclIpAccessRuleDstPortRange = _DAclIpAccessRuleDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 15),
    _DAclIpAccessRuleDstPortRange_Type()
)
dAclIpAccessRuleDstPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleDstPortRange.setStatus("current")


class _DAclIpAccessRuleQosPrecedence_Type(Integer32):
    """Custom type dAclIpAccessRuleQosPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DAclIpAccessRuleQosPrecedence_Type.__name__ = "Integer32"
_DAclIpAccessRuleQosPrecedence_Object = MibTableColumn
dAclIpAccessRuleQosPrecedence = _DAclIpAccessRuleQosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 16),
    _DAclIpAccessRuleQosPrecedence_Type()
)
dAclIpAccessRuleQosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleQosPrecedence.setStatus("current")


class _DAclIpAccessRuleQosTos_Type(Integer32):
    """Custom type dAclIpAccessRuleQosTos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 15),
    )


_DAclIpAccessRuleQosTos_Type.__name__ = "Integer32"
_DAclIpAccessRuleQosTos_Object = MibTableColumn
dAclIpAccessRuleQosTos = _DAclIpAccessRuleQosTos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 17),
    _DAclIpAccessRuleQosTos_Type()
)
dAclIpAccessRuleQosTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleQosTos.setStatus("current")


class _DAclIpAccessRuleQosDscp_Type(Integer32):
    """Custom type dAclIpAccessRuleQosDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_DAclIpAccessRuleQosDscp_Type.__name__ = "Integer32"
_DAclIpAccessRuleQosDscp_Object = MibTableColumn
dAclIpAccessRuleQosDscp = _DAclIpAccessRuleQosDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 18),
    _DAclIpAccessRuleQosDscp_Type()
)
dAclIpAccessRuleQosDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleQosDscp.setStatus("current")


class _DAclIpAccessRuleIcmpType_Type(Integer32):
    """Custom type dAclIpAccessRuleIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclIpAccessRuleIcmpType_Type.__name__ = "Integer32"
_DAclIpAccessRuleIcmpType_Object = MibTableColumn
dAclIpAccessRuleIcmpType = _DAclIpAccessRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 19),
    _DAclIpAccessRuleIcmpType_Type()
)
dAclIpAccessRuleIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleIcmpType.setStatus("current")


class _DAclIpAccessRuleIcmpCode_Type(Integer32):
    """Custom type dAclIpAccessRuleIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclIpAccessRuleIcmpCode_Type.__name__ = "Integer32"
_DAclIpAccessRuleIcmpCode_Object = MibTableColumn
dAclIpAccessRuleIcmpCode = _DAclIpAccessRuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 20),
    _DAclIpAccessRuleIcmpCode_Type()
)
dAclIpAccessRuleIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleIcmpCode.setStatus("current")
_DAclIpAccessRuleTimeName_Type = DisplayString
_DAclIpAccessRuleTimeName_Object = MibTableColumn
dAclIpAccessRuleTimeName = _DAclIpAccessRuleTimeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 21),
    _DAclIpAccessRuleTimeName_Type()
)
dAclIpAccessRuleTimeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessRuleTimeName.setStatus("current")
_DAclIpAccRuleTcpFlag_Type = TcpFlag
_DAclIpAccRuleTcpFlag_Object = MibTableColumn
dAclIpAccRuleTcpFlag = _DAclIpAccRuleTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 22),
    _DAclIpAccRuleTcpFlag_Type()
)
dAclIpAccRuleTcpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccRuleTcpFlag.setStatus("current")
_DAclIpAccRuleFragments_Type = TruthValue
_DAclIpAccRuleFragments_Object = MibTableColumn
dAclIpAccRuleFragments = _DAclIpAccRuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 23),
    _DAclIpAccRuleFragments_Type()
)
dAclIpAccRuleFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccRuleFragments.setStatus("current")


class _DAclIpAccRuleUserDefProtocolMask_Type(OctetString):
    """Custom type dAclIpAccRuleUserDefProtocolMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclIpAccRuleUserDefProtocolMask_Type.__name__ = "OctetString"
_DAclIpAccRuleUserDefProtocolMask_Object = MibTableColumn
dAclIpAccRuleUserDefProtocolMask = _DAclIpAccRuleUserDefProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 24),
    _DAclIpAccRuleUserDefProtocolMask_Type()
)
dAclIpAccRuleUserDefProtocolMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccRuleUserDefProtocolMask.setStatus("current")


class _DAclIpAccRuleSrcPortMask_Type(OctetString):
    """Custom type dAclIpAccRuleSrcPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclIpAccRuleSrcPortMask_Type.__name__ = "OctetString"
_DAclIpAccRuleSrcPortMask_Object = MibTableColumn
dAclIpAccRuleSrcPortMask = _DAclIpAccRuleSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 25),
    _DAclIpAccRuleSrcPortMask_Type()
)
dAclIpAccRuleSrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccRuleSrcPortMask.setStatus("current")


class _DAclIpAccRuleDstPortMask_Type(OctetString):
    """Custom type dAclIpAccRuleDstPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclIpAccRuleDstPortMask_Type.__name__ = "OctetString"
_DAclIpAccRuleDstPortMask_Object = MibTableColumn
dAclIpAccRuleDstPortMask = _DAclIpAccRuleDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 26),
    _DAclIpAccRuleDstPortMask_Type()
)
dAclIpAccRuleDstPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccRuleDstPortMask.setStatus("current")


class _DAclIpAccRuleQosPrecedenceMask_Type(OctetString):
    """Custom type dAclIpAccRuleQosPrecedenceMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclIpAccRuleQosPrecedenceMask_Type.__name__ = "OctetString"
_DAclIpAccRuleQosPrecedenceMask_Object = MibTableColumn
dAclIpAccRuleQosPrecedenceMask = _DAclIpAccRuleQosPrecedenceMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 27),
    _DAclIpAccRuleQosPrecedenceMask_Type()
)
dAclIpAccRuleQosPrecedenceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccRuleQosPrecedenceMask.setStatus("current")


class _DAclIpAccRuleQosTosMask_Type(OctetString):
    """Custom type dAclIpAccRuleQosTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclIpAccRuleQosTosMask_Type.__name__ = "OctetString"
_DAclIpAccRuleQosTosMask_Object = MibTableColumn
dAclIpAccRuleQosTosMask = _DAclIpAccRuleQosTosMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 28),
    _DAclIpAccRuleQosTosMask_Type()
)
dAclIpAccRuleQosTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccRuleQosTosMask.setStatus("current")


class _DAclIpAccRuleQosDscpMask_Type(OctetString):
    """Custom type dAclIpAccRuleQosDscpMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclIpAccRuleQosDscpMask_Type.__name__ = "OctetString"
_DAclIpAccRuleQosDscpMask_Object = MibTableColumn
dAclIpAccRuleQosDscpMask = _DAclIpAccRuleQosDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 3, 1, 29),
    _DAclIpAccRuleQosDscpMask_Type()
)
dAclIpAccRuleQosDscpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccRuleQosDscpMask.setStatus("current")
_DAclIpAccessGroupTable_Object = MibTable
dAclIpAccessGroupTable = _DAclIpAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 4)
)
if mibBuilder.loadTexts:
    dAclIpAccessGroupTable.setStatus("current")
_DAclIpAccessGroupEntry_Object = MibTableRow
dAclIpAccessGroupEntry = _DAclIpAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 4, 1)
)
dAclIpAccessGroupEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclIpAccessGroupIfIndex"),
    (0, "DLINKSW-ACL-MIB", "dAclIpAccessGroupApplyDirection"),
)
if mibBuilder.loadTexts:
    dAclIpAccessGroupEntry.setStatus("current")
_DAclIpAccessGroupIfIndex_Type = InterfaceIndex
_DAclIpAccessGroupIfIndex_Object = MibTableColumn
dAclIpAccessGroupIfIndex = _DAclIpAccessGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 4, 1, 1),
    _DAclIpAccessGroupIfIndex_Type()
)
dAclIpAccessGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclIpAccessGroupIfIndex.setStatus("current")


class _DAclIpAccessGroupApplyDirection_Type(Integer32):
    """Custom type dAclIpAccessGroupApplyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_DAclIpAccessGroupApplyDirection_Type.__name__ = "Integer32"
_DAclIpAccessGroupApplyDirection_Object = MibTableColumn
dAclIpAccessGroupApplyDirection = _DAclIpAccessGroupApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 4, 1, 2),
    _DAclIpAccessGroupApplyDirection_Type()
)
dAclIpAccessGroupApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclIpAccessGroupApplyDirection.setStatus("current")
_DAclIpAccessGroupStatus_Type = RowStatus
_DAclIpAccessGroupStatus_Object = MibTableColumn
dAclIpAccessGroupStatus = _DAclIpAccessGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 4, 1, 3),
    _DAclIpAccessGroupStatus_Type()
)
dAclIpAccessGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessGroupStatus.setStatus("current")


class _DAclIpAccessGroupAclName_Type(DisplayString):
    """Custom type dAclIpAccessGroupAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclIpAccessGroupAclName_Type.__name__ = "DisplayString"
_DAclIpAccessGroupAclName_Object = MibTableColumn
dAclIpAccessGroupAclName = _DAclIpAccessGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 4, 1, 4),
    _DAclIpAccessGroupAclName_Type()
)
dAclIpAccessGroupAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessGroupAclName.setStatus("current")
_DAclIpAccessGroupAclId_Type = Integer32
_DAclIpAccessGroupAclId_Object = MibTableColumn
dAclIpAccessGroupAclId = _DAclIpAccessGroupAclId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 3, 4, 1, 5),
    _DAclIpAccessGroupAclId_Type()
)
dAclIpAccessGroupAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIpAccessGroupAclId.setStatus("current")
_DAclIPv6_ObjectIdentity = ObjectIdentity
dAclIPv6 = _DAclIPv6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4)
)
_DAclIPv6AccessListNumber_Type = Unsigned32
_DAclIPv6AccessListNumber_Object = MibScalar
dAclIPv6AccessListNumber = _DAclIPv6AccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 1),
    _DAclIPv6AccessListNumber_Type()
)
dAclIPv6AccessListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dAclIPv6AccessListNumber.setStatus("current")
_DAclIPv6AccessListTable_Object = MibTable
dAclIPv6AccessListTable = _DAclIPv6AccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 2)
)
if mibBuilder.loadTexts:
    dAclIPv6AccessListTable.setStatus("current")
_DAclIPv6AccessListEntry_Object = MibTableRow
dAclIPv6AccessListEntry = _DAclIPv6AccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 2, 1)
)
dAclIPv6AccessListEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclIPv6AccessListName"),
)
if mibBuilder.loadTexts:
    dAclIPv6AccessListEntry.setStatus("current")


class _DAclIPv6AccessListName_Type(DisplayString):
    """Custom type dAclIPv6AccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclIPv6AccessListName_Type.__name__ = "DisplayString"
_DAclIPv6AccessListName_Object = MibTableColumn
dAclIPv6AccessListName = _DAclIPv6AccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 2, 1, 1),
    _DAclIPv6AccessListName_Type()
)
dAclIPv6AccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclIPv6AccessListName.setStatus("current")
_DAclIPv6AccessListRowStatus_Type = RowStatus
_DAclIPv6AccessListRowStatus_Object = MibTableColumn
dAclIPv6AccessListRowStatus = _DAclIPv6AccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 2, 1, 2),
    _DAclIPv6AccessListRowStatus_Type()
)
dAclIPv6AccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessListRowStatus.setStatus("current")
_DAclIPv6AccessExtended_Type = TruthValue
_DAclIPv6AccessExtended_Object = MibTableColumn
dAclIPv6AccessExtended = _DAclIPv6AccessExtended_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 2, 1, 3),
    _DAclIPv6AccessExtended_Type()
)
dAclIPv6AccessExtended.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessExtended.setStatus("current")
_DAclIPv6AccessListId_Type = Integer32
_DAclIPv6AccessListId_Object = MibTableColumn
dAclIPv6AccessListId = _DAclIPv6AccessListId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 2, 1, 4),
    _DAclIPv6AccessListId_Type()
)
dAclIPv6AccessListId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessListId.setStatus("current")
_DAclIPv6AccessListCounterEnabled_Type = TruthValue
_DAclIPv6AccessListCounterEnabled_Object = MibTableColumn
dAclIPv6AccessListCounterEnabled = _DAclIPv6AccessListCounterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 2, 1, 5),
    _DAclIPv6AccessListCounterEnabled_Type()
)
dAclIPv6AccessListCounterEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessListCounterEnabled.setStatus("current")


class _DAclIPv6AccessListClearStatAction_Type(Integer32):
    """Custom type dAclIPv6AccessListClearStatAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DAclIPv6AccessListClearStatAction_Type.__name__ = "Integer32"
_DAclIPv6AccessListClearStatAction_Object = MibTableColumn
dAclIPv6AccessListClearStatAction = _DAclIPv6AccessListClearStatAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 2, 1, 6),
    _DAclIPv6AccessListClearStatAction_Type()
)
dAclIPv6AccessListClearStatAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessListClearStatAction.setStatus("current")


class _DAclIPv6AccessListRemark_Type(DisplayString):
    """Custom type dAclIPv6AccessListRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DAclIPv6AccessListRemark_Type.__name__ = "DisplayString"
_DAclIPv6AccessListRemark_Object = MibTableColumn
dAclIPv6AccessListRemark = _DAclIPv6AccessListRemark_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 2, 1, 7),
    _DAclIPv6AccessListRemark_Type()
)
dAclIPv6AccessListRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessListRemark.setStatus("current")
_DAclIPv6AccessRuleTable_Object = MibTable
dAclIPv6AccessRuleTable = _DAclIPv6AccessRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3)
)
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleTable.setStatus("current")
_DAclIPv6AccessRuleEntry_Object = MibTableRow
dAclIPv6AccessRuleEntry = _DAclIPv6AccessRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1)
)
dAclIPv6AccessRuleEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclIPv6AccessListName"),
    (0, "DLINKSW-ACL-MIB", "dAclIPv6AccessRuleSn"),
)
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleEntry.setStatus("current")


class _DAclIPv6AccessRuleSn_Type(Integer32):
    """Custom type dAclIPv6AccessRuleSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DAclIPv6AccessRuleSn_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleSn_Object = MibTableColumn
dAclIPv6AccessRuleSn = _DAclIPv6AccessRuleSn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 1),
    _DAclIPv6AccessRuleSn_Type()
)
dAclIPv6AccessRuleSn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleSn.setStatus("current")
_DAclIPv6AccessRuleRowStatus_Type = RowStatus
_DAclIPv6AccessRuleRowStatus_Object = MibTableColumn
dAclIPv6AccessRuleRowStatus = _DAclIPv6AccessRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 2),
    _DAclIPv6AccessRuleRowStatus_Type()
)
dAclIPv6AccessRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleRowStatus.setStatus("current")
_DAclIPv6AccessRuleAction_Type = DlinkAclRuleType
_DAclIPv6AccessRuleAction_Object = MibTableColumn
dAclIPv6AccessRuleAction = _DAclIPv6AccessRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 3),
    _DAclIPv6AccessRuleAction_Type()
)
dAclIPv6AccessRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleAction.setStatus("current")


class _DAclIPv6AccessRuleProtocol_Type(Integer32):
    """Custom type dAclIPv6AccessRuleProtocol based on Integer32"""
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
        *(("none", 0),
          ("userDefine", 1),
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4),
          ("esp", 5),
          ("pcp", 6),
          ("sctp", 7))
    )


_DAclIPv6AccessRuleProtocol_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleProtocol_Object = MibTableColumn
dAclIPv6AccessRuleProtocol = _DAclIPv6AccessRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 4),
    _DAclIPv6AccessRuleProtocol_Type()
)
dAclIPv6AccessRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleProtocol.setStatus("current")


class _DAclIPv6AccessRuleUserDefProtocol_Type(Integer32):
    """Custom type dAclIPv6AccessRuleUserDefProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclIPv6AccessRuleUserDefProtocol_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleUserDefProtocol_Object = MibTableColumn
dAclIPv6AccessRuleUserDefProtocol = _DAclIPv6AccessRuleUserDefProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 5),
    _DAclIPv6AccessRuleUserDefProtocol_Type()
)
dAclIPv6AccessRuleUserDefProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleUserDefProtocol.setStatus("current")
_DAclIPv6AccessRuleSrcAddr_Type = InetAddressIPv6
_DAclIPv6AccessRuleSrcAddr_Object = MibTableColumn
dAclIPv6AccessRuleSrcAddr = _DAclIPv6AccessRuleSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 6),
    _DAclIPv6AccessRuleSrcAddr_Type()
)
dAclIPv6AccessRuleSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleSrcAddr.setStatus("current")
_DAclIPv6AccessRuleSrcPrefixLen_Type = InetAddressPrefixLength
_DAclIPv6AccessRuleSrcPrefixLen_Object = MibTableColumn
dAclIPv6AccessRuleSrcPrefixLen = _DAclIPv6AccessRuleSrcPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 7),
    _DAclIPv6AccessRuleSrcPrefixLen_Type()
)
dAclIPv6AccessRuleSrcPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleSrcPrefixLen.setStatus("current")
_DAclIPv6AccessRuleDstAddr_Type = InetAddressIPv6
_DAclIPv6AccessRuleDstAddr_Object = MibTableColumn
dAclIPv6AccessRuleDstAddr = _DAclIPv6AccessRuleDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 8),
    _DAclIPv6AccessRuleDstAddr_Type()
)
dAclIPv6AccessRuleDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleDstAddr.setStatus("current")
_DAclIPv6AccessRuleDstPrefixLen_Type = InetAddressPrefixLength
_DAclIPv6AccessRuleDstPrefixLen_Object = MibTableColumn
dAclIPv6AccessRuleDstPrefixLen = _DAclIPv6AccessRuleDstPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 9),
    _DAclIPv6AccessRuleDstPrefixLen_Type()
)
dAclIPv6AccessRuleDstPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleDstPrefixLen.setStatus("current")
_DAclIPv6AccessRuleSrcOperator_Type = DlinkAclPortOperatorType
_DAclIPv6AccessRuleSrcOperator_Object = MibTableColumn
dAclIPv6AccessRuleSrcOperator = _DAclIPv6AccessRuleSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 10),
    _DAclIPv6AccessRuleSrcOperator_Type()
)
dAclIPv6AccessRuleSrcOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleSrcOperator.setStatus("current")


class _DAclIPv6AccessRuleSrcPort_Type(Integer32):
    """Custom type dAclIPv6AccessRuleSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclIPv6AccessRuleSrcPort_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleSrcPort_Object = MibTableColumn
dAclIPv6AccessRuleSrcPort = _DAclIPv6AccessRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 11),
    _DAclIPv6AccessRuleSrcPort_Type()
)
dAclIPv6AccessRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleSrcPort.setStatus("current")


class _DAclIPv6AccessRuleSrcPortRange_Type(Integer32):
    """Custom type dAclIPv6AccessRuleSrcPortRange based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclIPv6AccessRuleSrcPortRange_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleSrcPortRange_Object = MibTableColumn
dAclIPv6AccessRuleSrcPortRange = _DAclIPv6AccessRuleSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 12),
    _DAclIPv6AccessRuleSrcPortRange_Type()
)
dAclIPv6AccessRuleSrcPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleSrcPortRange.setStatus("current")
_DAclIPv6AccessRuleDstOperator_Type = DlinkAclPortOperatorType
_DAclIPv6AccessRuleDstOperator_Object = MibTableColumn
dAclIPv6AccessRuleDstOperator = _DAclIPv6AccessRuleDstOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 13),
    _DAclIPv6AccessRuleDstOperator_Type()
)
dAclIPv6AccessRuleDstOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleDstOperator.setStatus("current")


class _DAclIPv6AccessRuleDstPort_Type(Integer32):
    """Custom type dAclIPv6AccessRuleDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclIPv6AccessRuleDstPort_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleDstPort_Object = MibTableColumn
dAclIPv6AccessRuleDstPort = _DAclIPv6AccessRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 14),
    _DAclIPv6AccessRuleDstPort_Type()
)
dAclIPv6AccessRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleDstPort.setStatus("current")


class _DAclIPv6AccessRuleDstPortRange_Type(Integer32):
    """Custom type dAclIPv6AccessRuleDstPortRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclIPv6AccessRuleDstPortRange_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleDstPortRange_Object = MibTableColumn
dAclIPv6AccessRuleDstPortRange = _DAclIPv6AccessRuleDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 15),
    _DAclIPv6AccessRuleDstPortRange_Type()
)
dAclIPv6AccessRuleDstPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleDstPortRange.setStatus("current")


class _DAclIPv6AccessRuleDscp_Type(Integer32):
    """Custom type dAclIPv6AccessRuleDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_DAclIPv6AccessRuleDscp_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleDscp_Object = MibTableColumn
dAclIPv6AccessRuleDscp = _DAclIPv6AccessRuleDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 16),
    _DAclIPv6AccessRuleDscp_Type()
)
dAclIPv6AccessRuleDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleDscp.setStatus("current")


class _DAclIPv6AccessRuleIcmpType_Type(Integer32):
    """Custom type dAclIPv6AccessRuleIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclIPv6AccessRuleIcmpType_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleIcmpType_Object = MibTableColumn
dAclIPv6AccessRuleIcmpType = _DAclIPv6AccessRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 17),
    _DAclIPv6AccessRuleIcmpType_Type()
)
dAclIPv6AccessRuleIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleIcmpType.setStatus("current")


class _DAclIPv6AccessRuleIcmpCode_Type(Integer32):
    """Custom type dAclIPv6AccessRuleIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclIPv6AccessRuleIcmpCode_Type.__name__ = "Integer32"
_DAclIPv6AccessRuleIcmpCode_Object = MibTableColumn
dAclIPv6AccessRuleIcmpCode = _DAclIPv6AccessRuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 18),
    _DAclIPv6AccessRuleIcmpCode_Type()
)
dAclIPv6AccessRuleIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleIcmpCode.setStatus("current")
_DAclIPv6AccessRuleTimeName_Type = DisplayString
_DAclIPv6AccessRuleTimeName_Object = MibTableColumn
dAclIPv6AccessRuleTimeName = _DAclIPv6AccessRuleTimeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 19),
    _DAclIPv6AccessRuleTimeName_Type()
)
dAclIPv6AccessRuleTimeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessRuleTimeName.setStatus("current")
_DAclIPv6AccRuleTcpFlag_Type = TcpFlag
_DAclIPv6AccRuleTcpFlag_Object = MibTableColumn
dAclIPv6AccRuleTcpFlag = _DAclIPv6AccRuleTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 20),
    _DAclIPv6AccRuleTcpFlag_Type()
)
dAclIPv6AccRuleTcpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleTcpFlag.setStatus("current")
_DAclIPv6AccRuleFragments_Type = TruthValue
_DAclIPv6AccRuleFragments_Object = MibTableColumn
dAclIPv6AccRuleFragments = _DAclIPv6AccRuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 21),
    _DAclIPv6AccRuleFragments_Type()
)
dAclIPv6AccRuleFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleFragments.setStatus("current")


class _DAclIPv6AccRuleFlowLabel_Type(Integer32):
    """Custom type dAclIPv6AccRuleFlowLabel based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 1048575),
    )


_DAclIPv6AccRuleFlowLabel_Type.__name__ = "Integer32"
_DAclIPv6AccRuleFlowLabel_Object = MibTableColumn
dAclIPv6AccRuleFlowLabel = _DAclIPv6AccRuleFlowLabel_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 22),
    _DAclIPv6AccRuleFlowLabel_Type()
)
dAclIPv6AccRuleFlowLabel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleFlowLabel.setStatus("current")


class _DAclIPv6AccRuleTrafficClass_Type(Integer32):
    """Custom type dAclIPv6AccRuleTrafficClass based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclIPv6AccRuleTrafficClass_Type.__name__ = "Integer32"
_DAclIPv6AccRuleTrafficClass_Object = MibTableColumn
dAclIPv6AccRuleTrafficClass = _DAclIPv6AccRuleTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 23),
    _DAclIPv6AccRuleTrafficClass_Type()
)
dAclIPv6AccRuleTrafficClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleTrafficClass.setStatus("current")


class _DAclIPv6AccRuleUserDefProtocolMask_Type(OctetString):
    """Custom type dAclIPv6AccRuleUserDefProtocolMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclIPv6AccRuleUserDefProtocolMask_Type.__name__ = "OctetString"
_DAclIPv6AccRuleUserDefProtocolMask_Object = MibTableColumn
dAclIPv6AccRuleUserDefProtocolMask = _DAclIPv6AccRuleUserDefProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 24),
    _DAclIPv6AccRuleUserDefProtocolMask_Type()
)
dAclIPv6AccRuleUserDefProtocolMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleUserDefProtocolMask.setStatus("current")


class _DAclIPv6AccRuleSrcPortMask_Type(OctetString):
    """Custom type dAclIPv6AccRuleSrcPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclIPv6AccRuleSrcPortMask_Type.__name__ = "OctetString"
_DAclIPv6AccRuleSrcPortMask_Object = MibTableColumn
dAclIPv6AccRuleSrcPortMask = _DAclIPv6AccRuleSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 25),
    _DAclIPv6AccRuleSrcPortMask_Type()
)
dAclIPv6AccRuleSrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleSrcPortMask.setStatus("current")


class _DAclIPv6AccRuleDstPortMask_Type(OctetString):
    """Custom type dAclIPv6AccRuleDstPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclIPv6AccRuleDstPortMask_Type.__name__ = "OctetString"
_DAclIPv6AccRuleDstPortMask_Object = MibTableColumn
dAclIPv6AccRuleDstPortMask = _DAclIPv6AccRuleDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 26),
    _DAclIPv6AccRuleDstPortMask_Type()
)
dAclIPv6AccRuleDstPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleDstPortMask.setStatus("current")


class _DAclIPv6AccRuleDscpMask_Type(OctetString):
    """Custom type dAclIPv6AccRuleDscpMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclIPv6AccRuleDscpMask_Type.__name__ = "OctetString"
_DAclIPv6AccRuleDscpMask_Object = MibTableColumn
dAclIPv6AccRuleDscpMask = _DAclIPv6AccRuleDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 27),
    _DAclIPv6AccRuleDscpMask_Type()
)
dAclIPv6AccRuleDscpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleDscpMask.setStatus("current")


class _DAclIPv6AccRuleFlowLabelMask_Type(OctetString):
    """Custom type dAclIPv6AccRuleFlowLabelMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_DAclIPv6AccRuleFlowLabelMask_Type.__name__ = "OctetString"
_DAclIPv6AccRuleFlowLabelMask_Object = MibTableColumn
dAclIPv6AccRuleFlowLabelMask = _DAclIPv6AccRuleFlowLabelMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 28),
    _DAclIPv6AccRuleFlowLabelMask_Type()
)
dAclIPv6AccRuleFlowLabelMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleFlowLabelMask.setStatus("current")


class _DAclIPv6AccRuleTrafficClassMask_Type(OctetString):
    """Custom type dAclIPv6AccRuleTrafficClassMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclIPv6AccRuleTrafficClassMask_Type.__name__ = "OctetString"
_DAclIPv6AccRuleTrafficClassMask_Object = MibTableColumn
dAclIPv6AccRuleTrafficClassMask = _DAclIPv6AccRuleTrafficClassMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 3, 1, 29),
    _DAclIPv6AccRuleTrafficClassMask_Type()
)
dAclIPv6AccRuleTrafficClassMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccRuleTrafficClassMask.setStatus("current")
_DAclIPv6AccessGroupTable_Object = MibTable
dAclIPv6AccessGroupTable = _DAclIPv6AccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 4)
)
if mibBuilder.loadTexts:
    dAclIPv6AccessGroupTable.setStatus("current")
_DAclIPv6AccessGroupEntry_Object = MibTableRow
dAclIPv6AccessGroupEntry = _DAclIPv6AccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 4, 1)
)
dAclIPv6AccessGroupEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclIPv6AccessGroupIfIndex"),
    (0, "DLINKSW-ACL-MIB", "dAclIpv6AccessGroupApplyDirection"),
)
if mibBuilder.loadTexts:
    dAclIPv6AccessGroupEntry.setStatus("current")
_DAclIPv6AccessGroupIfIndex_Type = InterfaceIndex
_DAclIPv6AccessGroupIfIndex_Object = MibTableColumn
dAclIPv6AccessGroupIfIndex = _DAclIPv6AccessGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 4, 1, 1),
    _DAclIPv6AccessGroupIfIndex_Type()
)
dAclIPv6AccessGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclIPv6AccessGroupIfIndex.setStatus("current")


class _DAclIpv6AccessGroupApplyDirection_Type(Integer32):
    """Custom type dAclIpv6AccessGroupApplyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_DAclIpv6AccessGroupApplyDirection_Type.__name__ = "Integer32"
_DAclIpv6AccessGroupApplyDirection_Object = MibTableColumn
dAclIpv6AccessGroupApplyDirection = _DAclIpv6AccessGroupApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 4, 1, 2),
    _DAclIpv6AccessGroupApplyDirection_Type()
)
dAclIpv6AccessGroupApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclIpv6AccessGroupApplyDirection.setStatus("current")
_DAclIPv6AccessGroupStatus_Type = RowStatus
_DAclIPv6AccessGroupStatus_Object = MibTableColumn
dAclIPv6AccessGroupStatus = _DAclIPv6AccessGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 4, 1, 3),
    _DAclIPv6AccessGroupStatus_Type()
)
dAclIPv6AccessGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessGroupStatus.setStatus("current")


class _DAclIPv6AccessGroupAclName_Type(DisplayString):
    """Custom type dAclIPv6AccessGroupAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclIPv6AccessGroupAclName_Type.__name__ = "DisplayString"
_DAclIPv6AccessGroupAclName_Object = MibTableColumn
dAclIPv6AccessGroupAclName = _DAclIPv6AccessGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 4, 1, 4),
    _DAclIPv6AccessGroupAclName_Type()
)
dAclIPv6AccessGroupAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessGroupAclName.setStatus("current")
_DAclIPv6AccessGroupAclId_Type = Integer32
_DAclIPv6AccessGroupAclId_Object = MibTableColumn
dAclIPv6AccessGroupAclId = _DAclIPv6AccessGroupAclId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 4, 4, 1, 5),
    _DAclIPv6AccessGroupAclId_Type()
)
dAclIPv6AccessGroupAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclIPv6AccessGroupAclId.setStatus("current")
_DAclExpert_ObjectIdentity = ObjectIdentity
dAclExpert = _DAclExpert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5)
)
_DAclExpertAccessListNumber_Type = Unsigned32
_DAclExpertAccessListNumber_Object = MibScalar
dAclExpertAccessListNumber = _DAclExpertAccessListNumber_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 1),
    _DAclExpertAccessListNumber_Type()
)
dAclExpertAccessListNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dAclExpertAccessListNumber.setStatus("current")
_DAclExpertAccessListTable_Object = MibTable
dAclExpertAccessListTable = _DAclExpertAccessListTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 2)
)
if mibBuilder.loadTexts:
    dAclExpertAccessListTable.setStatus("current")
_DAclExpertAccessListEntry_Object = MibTableRow
dAclExpertAccessListEntry = _DAclExpertAccessListEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 2, 1)
)
dAclExpertAccessListEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclExpertAccessListName"),
)
if mibBuilder.loadTexts:
    dAclExpertAccessListEntry.setStatus("current")


class _DAclExpertAccessListName_Type(DisplayString):
    """Custom type dAclExpertAccessListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclExpertAccessListName_Type.__name__ = "DisplayString"
_DAclExpertAccessListName_Object = MibTableColumn
dAclExpertAccessListName = _DAclExpertAccessListName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 2, 1, 1),
    _DAclExpertAccessListName_Type()
)
dAclExpertAccessListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclExpertAccessListName.setStatus("current")
_DAclExpertAccessListRowStatus_Type = RowStatus
_DAclExpertAccessListRowStatus_Object = MibTableColumn
dAclExpertAccessListRowStatus = _DAclExpertAccessListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 2, 1, 2),
    _DAclExpertAccessListRowStatus_Type()
)
dAclExpertAccessListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccessListRowStatus.setStatus("current")
_DAclExpertAccessListId_Type = Integer32
_DAclExpertAccessListId_Object = MibTableColumn
dAclExpertAccessListId = _DAclExpertAccessListId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 2, 1, 3),
    _DAclExpertAccessListId_Type()
)
dAclExpertAccessListId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccessListId.setStatus("current")
_DAclExpertAccessListCounterEnabled_Type = TruthValue
_DAclExpertAccessListCounterEnabled_Object = MibTableColumn
dAclExpertAccessListCounterEnabled = _DAclExpertAccessListCounterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 2, 1, 4),
    _DAclExpertAccessListCounterEnabled_Type()
)
dAclExpertAccessListCounterEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccessListCounterEnabled.setStatus("current")


class _DAclExpertAccessListClearStatAction_Type(Integer32):
    """Custom type dAclExpertAccessListClearStatAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DAclExpertAccessListClearStatAction_Type.__name__ = "Integer32"
_DAclExpertAccessListClearStatAction_Object = MibTableColumn
dAclExpertAccessListClearStatAction = _DAclExpertAccessListClearStatAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 2, 1, 5),
    _DAclExpertAccessListClearStatAction_Type()
)
dAclExpertAccessListClearStatAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccessListClearStatAction.setStatus("current")


class _DAclExpertAccessListRemark_Type(DisplayString):
    """Custom type dAclExpertAccessListRemark based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DAclExpertAccessListRemark_Type.__name__ = "DisplayString"
_DAclExpertAccessListRemark_Object = MibTableColumn
dAclExpertAccessListRemark = _DAclExpertAccessListRemark_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 2, 1, 6),
    _DAclExpertAccessListRemark_Type()
)
dAclExpertAccessListRemark.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccessListRemark.setStatus("current")
_DAclExpertAccessRuleTable_Object = MibTable
dAclExpertAccessRuleTable = _DAclExpertAccessRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3)
)
if mibBuilder.loadTexts:
    dAclExpertAccessRuleTable.setStatus("current")
_DAclExpertAccessRuleEntry_Object = MibTableRow
dAclExpertAccessRuleEntry = _DAclExpertAccessRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1)
)
dAclExpertAccessRuleEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclExpertAccessListName"),
    (0, "DLINKSW-ACL-MIB", "dAclExpertAccRuleSn"),
)
if mibBuilder.loadTexts:
    dAclExpertAccessRuleEntry.setStatus("current")


class _DAclExpertAccRuleSn_Type(Integer32):
    """Custom type dAclExpertAccRuleSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DAclExpertAccRuleSn_Type.__name__ = "Integer32"
_DAclExpertAccRuleSn_Object = MibTableColumn
dAclExpertAccRuleSn = _DAclExpertAccRuleSn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 1),
    _DAclExpertAccRuleSn_Type()
)
dAclExpertAccRuleSn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclExpertAccRuleSn.setStatus("current")
_DAclExpertAccRuleRowStatus_Type = RowStatus
_DAclExpertAccRuleRowStatus_Object = MibTableColumn
dAclExpertAccRuleRowStatus = _DAclExpertAccRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 2),
    _DAclExpertAccRuleRowStatus_Type()
)
dAclExpertAccRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleRowStatus.setStatus("current")
_DAclExpertAccRuleAction_Type = DlinkAclRuleType
_DAclExpertAccRuleAction_Object = MibTableColumn
dAclExpertAccRuleAction = _DAclExpertAccRuleAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 3),
    _DAclExpertAccRuleAction_Type()
)
dAclExpertAccRuleAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleAction.setStatus("current")


class _DAclExpertAccRuleProtocol_Type(Integer32):
    """Custom type dAclExpertAccRuleProtocol based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("userDefine", 1),
          ("tcp", 2),
          ("udp", 3),
          ("icmp", 4),
          ("gre", 5),
          ("esp", 6),
          ("eigrp", 7),
          ("igmp", 8),
          ("ospf", 9),
          ("pim", 10),
          ("vrrp", 11),
          ("ipinip", 12),
          ("pcp", 13))
    )


_DAclExpertAccRuleProtocol_Type.__name__ = "Integer32"
_DAclExpertAccRuleProtocol_Object = MibTableColumn
dAclExpertAccRuleProtocol = _DAclExpertAccRuleProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 4),
    _DAclExpertAccRuleProtocol_Type()
)
dAclExpertAccRuleProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleProtocol.setStatus("current")


class _DAclExpertAccRuleUserDefProtocol_Type(Integer32):
    """Custom type dAclExpertAccRuleUserDefProtocol based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclExpertAccRuleUserDefProtocol_Type.__name__ = "Integer32"
_DAclExpertAccRuleUserDefProtocol_Object = MibTableColumn
dAclExpertAccRuleUserDefProtocol = _DAclExpertAccRuleUserDefProtocol_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 5),
    _DAclExpertAccRuleUserDefProtocol_Type()
)
dAclExpertAccRuleUserDefProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleUserDefProtocol.setStatus("current")
_DAclExpertAccRuleSrcIpAddr_Type = IpAddress
_DAclExpertAccRuleSrcIpAddr_Object = MibTableColumn
dAclExpertAccRuleSrcIpAddr = _DAclExpertAccRuleSrcIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 6),
    _DAclExpertAccRuleSrcIpAddr_Type()
)
dAclExpertAccRuleSrcIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleSrcIpAddr.setStatus("current")
_DAclExpertAccRuleSrcIpWildcard_Type = IpAddress
_DAclExpertAccRuleSrcIpWildcard_Object = MibTableColumn
dAclExpertAccRuleSrcIpWildcard = _DAclExpertAccRuleSrcIpWildcard_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 7),
    _DAclExpertAccRuleSrcIpWildcard_Type()
)
dAclExpertAccRuleSrcIpWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleSrcIpWildcard.setStatus("current")
_DAclExpertAccRuleSrcMacAddr_Type = MacAddress
_DAclExpertAccRuleSrcMacAddr_Object = MibTableColumn
dAclExpertAccRuleSrcMacAddr = _DAclExpertAccRuleSrcMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 8),
    _DAclExpertAccRuleSrcMacAddr_Type()
)
dAclExpertAccRuleSrcMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleSrcMacAddr.setStatus("current")
_DAclExpertAccRuleSrcMacWildcard_Type = MacAddress
_DAclExpertAccRuleSrcMacWildcard_Object = MibTableColumn
dAclExpertAccRuleSrcMacWildcard = _DAclExpertAccRuleSrcMacWildcard_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 9),
    _DAclExpertAccRuleSrcMacWildcard_Type()
)
dAclExpertAccRuleSrcMacWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleSrcMacWildcard.setStatus("current")
_DAclExpertAccRuleSrcOperator_Type = DlinkAclPortOperatorType
_DAclExpertAccRuleSrcOperator_Object = MibTableColumn
dAclExpertAccRuleSrcOperator = _DAclExpertAccRuleSrcOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 10),
    _DAclExpertAccRuleSrcOperator_Type()
)
dAclExpertAccRuleSrcOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleSrcOperator.setStatus("current")


class _DAclExpertAccRuleSrcPort_Type(Integer32):
    """Custom type dAclExpertAccRuleSrcPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclExpertAccRuleSrcPort_Type.__name__ = "Integer32"
_DAclExpertAccRuleSrcPort_Object = MibTableColumn
dAclExpertAccRuleSrcPort = _DAclExpertAccRuleSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 11),
    _DAclExpertAccRuleSrcPort_Type()
)
dAclExpertAccRuleSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleSrcPort.setStatus("current")


class _DAclExpertAccRuleSrcPortRange_Type(Integer32):
    """Custom type dAclExpertAccRuleSrcPortRange based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclExpertAccRuleSrcPortRange_Type.__name__ = "Integer32"
_DAclExpertAccRuleSrcPortRange_Object = MibTableColumn
dAclExpertAccRuleSrcPortRange = _DAclExpertAccRuleSrcPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 12),
    _DAclExpertAccRuleSrcPortRange_Type()
)
dAclExpertAccRuleSrcPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleSrcPortRange.setStatus("current")
_DAclExpertAccRuleDstIpAddr_Type = IpAddress
_DAclExpertAccRuleDstIpAddr_Object = MibTableColumn
dAclExpertAccRuleDstIpAddr = _DAclExpertAccRuleDstIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 13),
    _DAclExpertAccRuleDstIpAddr_Type()
)
dAclExpertAccRuleDstIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleDstIpAddr.setStatus("current")
_DAclExpertAccRuleDstIpWildcard_Type = IpAddress
_DAclExpertAccRuleDstIpWildcard_Object = MibTableColumn
dAclExpertAccRuleDstIpWildcard = _DAclExpertAccRuleDstIpWildcard_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 14),
    _DAclExpertAccRuleDstIpWildcard_Type()
)
dAclExpertAccRuleDstIpWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleDstIpWildcard.setStatus("current")
_DAclExpertAccRuleDstMacAddr_Type = MacAddress
_DAclExpertAccRuleDstMacAddr_Object = MibTableColumn
dAclExpertAccRuleDstMacAddr = _DAclExpertAccRuleDstMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 15),
    _DAclExpertAccRuleDstMacAddr_Type()
)
dAclExpertAccRuleDstMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleDstMacAddr.setStatus("current")
_DAclExpertAccRuleDstMacWildcard_Type = MacAddress
_DAclExpertAccRuleDstMacWildcard_Object = MibTableColumn
dAclExpertAccRuleDstMacWildcard = _DAclExpertAccRuleDstMacWildcard_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 16),
    _DAclExpertAccRuleDstMacWildcard_Type()
)
dAclExpertAccRuleDstMacWildcard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleDstMacWildcard.setStatus("current")
_DAclExpertAccRuleDstOperator_Type = DlinkAclPortOperatorType
_DAclExpertAccRuleDstOperator_Object = MibTableColumn
dAclExpertAccRuleDstOperator = _DAclExpertAccRuleDstOperator_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 17),
    _DAclExpertAccRuleDstOperator_Type()
)
dAclExpertAccRuleDstOperator.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleDstOperator.setStatus("current")


class _DAclExpertAccRuleDstPort_Type(Integer32):
    """Custom type dAclExpertAccRuleDstPort based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclExpertAccRuleDstPort_Type.__name__ = "Integer32"
_DAclExpertAccRuleDstPort_Object = MibTableColumn
dAclExpertAccRuleDstPort = _DAclExpertAccRuleDstPort_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 18),
    _DAclExpertAccRuleDstPort_Type()
)
dAclExpertAccRuleDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleDstPort.setStatus("current")


class _DAclExpertAccRuleDstPortRange_Type(Integer32):
    """Custom type dAclExpertAccRuleDstPortRange based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_DAclExpertAccRuleDstPortRange_Type.__name__ = "Integer32"
_DAclExpertAccRuleDstPortRange_Object = MibTableColumn
dAclExpertAccRuleDstPortRange = _DAclExpertAccRuleDstPortRange_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 19),
    _DAclExpertAccRuleDstPortRange_Type()
)
dAclExpertAccRuleDstPortRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleDstPortRange.setStatus("current")


class _DAclExpertAccRuleVlanID_Type(VlanIdOrNone):
    """Custom type dAclExpertAccRuleVlanID based on VlanIdOrNone"""
    defaultValue = 0


_DAclExpertAccRuleVlanID_Type.__name__ = "VlanIdOrNone"
_DAclExpertAccRuleVlanID_Object = MibTableColumn
dAclExpertAccRuleVlanID = _DAclExpertAccRuleVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 20),
    _DAclExpertAccRuleVlanID_Type()
)
dAclExpertAccRuleVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleVlanID.setStatus("current")


class _DAclExpertAccRuleInnerVlanID_Type(VlanIdOrNone):
    """Custom type dAclExpertAccRuleInnerVlanID based on VlanIdOrNone"""
    defaultValue = 0


_DAclExpertAccRuleInnerVlanID_Type.__name__ = "VlanIdOrNone"
_DAclExpertAccRuleInnerVlanID_Object = MibTableColumn
dAclExpertAccRuleInnerVlanID = _DAclExpertAccRuleInnerVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 21),
    _DAclExpertAccRuleInnerVlanID_Type()
)
dAclExpertAccRuleInnerVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleInnerVlanID.setStatus("current")


class _DAclExpertAccRuleQosPrecedence_Type(Integer32):
    """Custom type dAclExpertAccRuleQosPrecedence based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DAclExpertAccRuleQosPrecedence_Type.__name__ = "Integer32"
_DAclExpertAccRuleQosPrecedence_Object = MibTableColumn
dAclExpertAccRuleQosPrecedence = _DAclExpertAccRuleQosPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 22),
    _DAclExpertAccRuleQosPrecedence_Type()
)
dAclExpertAccRuleQosPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleQosPrecedence.setStatus("current")


class _DAclExpertAccRuleQosTos_Type(Integer32):
    """Custom type dAclExpertAccRuleQosTos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 15),
    )


_DAclExpertAccRuleQosTos_Type.__name__ = "Integer32"
_DAclExpertAccRuleQosTos_Object = MibTableColumn
dAclExpertAccRuleQosTos = _DAclExpertAccRuleQosTos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 23),
    _DAclExpertAccRuleQosTos_Type()
)
dAclExpertAccRuleQosTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleQosTos.setStatus("current")


class _DAclExpertAccRuleQosDscp_Type(Integer32):
    """Custom type dAclExpertAccRuleQosDscp based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 63),
    )


_DAclExpertAccRuleQosDscp_Type.__name__ = "Integer32"
_DAclExpertAccRuleQosDscp_Object = MibTableColumn
dAclExpertAccRuleQosDscp = _DAclExpertAccRuleQosDscp_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 24),
    _DAclExpertAccRuleQosDscp_Type()
)
dAclExpertAccRuleQosDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleQosDscp.setStatus("current")


class _DAclExpertAccRuleIcmpType_Type(Integer32):
    """Custom type dAclExpertAccRuleIcmpType based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclExpertAccRuleIcmpType_Type.__name__ = "Integer32"
_DAclExpertAccRuleIcmpType_Object = MibTableColumn
dAclExpertAccRuleIcmpType = _DAclExpertAccRuleIcmpType_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 25),
    _DAclExpertAccRuleIcmpType_Type()
)
dAclExpertAccRuleIcmpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleIcmpType.setStatus("current")


class _DAclExpertAccRuleIcmpCode_Type(Integer32):
    """Custom type dAclExpertAccRuleIcmpCode based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 255),
    )


_DAclExpertAccRuleIcmpCode_Type.__name__ = "Integer32"
_DAclExpertAccRuleIcmpCode_Object = MibTableColumn
dAclExpertAccRuleIcmpCode = _DAclExpertAccRuleIcmpCode_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 26),
    _DAclExpertAccRuleIcmpCode_Type()
)
dAclExpertAccRuleIcmpCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleIcmpCode.setStatus("current")
_DAclExpertAccRuleTimeName_Type = DisplayString
_DAclExpertAccRuleTimeName_Object = MibTableColumn
dAclExpertAccRuleTimeName = _DAclExpertAccRuleTimeName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 27),
    _DAclExpertAccRuleTimeName_Type()
)
dAclExpertAccRuleTimeName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleTimeName.setStatus("current")
_DAclExpertAccRuleTcpFlag_Type = TcpFlag
_DAclExpertAccRuleTcpFlag_Object = MibTableColumn
dAclExpertAccRuleTcpFlag = _DAclExpertAccRuleTcpFlag_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 28),
    _DAclExpertAccRuleTcpFlag_Type()
)
dAclExpertAccRuleTcpFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleTcpFlag.setStatus("current")
_DAclExpertAccRuleFragments_Type = TruthValue
_DAclExpertAccRuleFragments_Object = MibTableColumn
dAclExpertAccRuleFragments = _DAclExpertAccRuleFragments_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 29),
    _DAclExpertAccRuleFragments_Type()
)
dAclExpertAccRuleFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleFragments.setStatus("current")


class _DAclExpertAccRuleOuterCos_Type(Integer32):
    """Custom type dAclExpertAccRuleOuterCos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DAclExpertAccRuleOuterCos_Type.__name__ = "Integer32"
_DAclExpertAccRuleOuterCos_Object = MibTableColumn
dAclExpertAccRuleOuterCos = _DAclExpertAccRuleOuterCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 30),
    _DAclExpertAccRuleOuterCos_Type()
)
dAclExpertAccRuleOuterCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleOuterCos.setStatus("current")


class _DAclExpertAccRuleInnerCos_Type(Integer32):
    """Custom type dAclExpertAccRuleInnerCos based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 7),
    )


_DAclExpertAccRuleInnerCos_Type.__name__ = "Integer32"
_DAclExpertAccRuleInnerCos_Object = MibTableColumn
dAclExpertAccRuleInnerCos = _DAclExpertAccRuleInnerCos_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 31),
    _DAclExpertAccRuleInnerCos_Type()
)
dAclExpertAccRuleInnerCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleInnerCos.setStatus("current")


class _DAclExpertAccRuleUserDefProtocolMask_Type(OctetString):
    """Custom type dAclExpertAccRuleUserDefProtocolMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclExpertAccRuleUserDefProtocolMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleUserDefProtocolMask_Object = MibTableColumn
dAclExpertAccRuleUserDefProtocolMask = _DAclExpertAccRuleUserDefProtocolMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 32),
    _DAclExpertAccRuleUserDefProtocolMask_Type()
)
dAclExpertAccRuleUserDefProtocolMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleUserDefProtocolMask.setStatus("current")


class _DAclExpertAccRuleSrcPortMask_Type(OctetString):
    """Custom type dAclExpertAccRuleSrcPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclExpertAccRuleSrcPortMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleSrcPortMask_Object = MibTableColumn
dAclExpertAccRuleSrcPortMask = _DAclExpertAccRuleSrcPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 33),
    _DAclExpertAccRuleSrcPortMask_Type()
)
dAclExpertAccRuleSrcPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleSrcPortMask.setStatus("current")


class _DAclExpertAccRuleDstPortMask_Type(OctetString):
    """Custom type dAclExpertAccRuleDstPortMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclExpertAccRuleDstPortMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleDstPortMask_Object = MibTableColumn
dAclExpertAccRuleDstPortMask = _DAclExpertAccRuleDstPortMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 34),
    _DAclExpertAccRuleDstPortMask_Type()
)
dAclExpertAccRuleDstPortMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleDstPortMask.setStatus("current")


class _DAclExpertAccRuleVlanIDMask_Type(OctetString):
    """Custom type dAclExpertAccRuleVlanIDMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclExpertAccRuleVlanIDMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleVlanIDMask_Object = MibTableColumn
dAclExpertAccRuleVlanIDMask = _DAclExpertAccRuleVlanIDMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 35),
    _DAclExpertAccRuleVlanIDMask_Type()
)
dAclExpertAccRuleVlanIDMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleVlanIDMask.setStatus("current")


class _DAclExpertAccRuleInnerVlanIDMask_Type(OctetString):
    """Custom type dAclExpertAccRuleInnerVlanIDMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_DAclExpertAccRuleInnerVlanIDMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleInnerVlanIDMask_Object = MibTableColumn
dAclExpertAccRuleInnerVlanIDMask = _DAclExpertAccRuleInnerVlanIDMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 36),
    _DAclExpertAccRuleInnerVlanIDMask_Type()
)
dAclExpertAccRuleInnerVlanIDMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleInnerVlanIDMask.setStatus("current")


class _DAclExpertAccRuleQosPrecedenceMask_Type(OctetString):
    """Custom type dAclExpertAccRuleQosPrecedenceMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclExpertAccRuleQosPrecedenceMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleQosPrecedenceMask_Object = MibTableColumn
dAclExpertAccRuleQosPrecedenceMask = _DAclExpertAccRuleQosPrecedenceMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 37),
    _DAclExpertAccRuleQosPrecedenceMask_Type()
)
dAclExpertAccRuleQosPrecedenceMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleQosPrecedenceMask.setStatus("current")


class _DAclExpertAccRuleQosTosMask_Type(OctetString):
    """Custom type dAclExpertAccRuleQosTosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclExpertAccRuleQosTosMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleQosTosMask_Object = MibTableColumn
dAclExpertAccRuleQosTosMask = _DAclExpertAccRuleQosTosMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 38),
    _DAclExpertAccRuleQosTosMask_Type()
)
dAclExpertAccRuleQosTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleQosTosMask.setStatus("current")


class _DAclExpertAccRuleQosDscpMask_Type(OctetString):
    """Custom type dAclExpertAccRuleQosDscpMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclExpertAccRuleQosDscpMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleQosDscpMask_Object = MibTableColumn
dAclExpertAccRuleQosDscpMask = _DAclExpertAccRuleQosDscpMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 39),
    _DAclExpertAccRuleQosDscpMask_Type()
)
dAclExpertAccRuleQosDscpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleQosDscpMask.setStatus("current")


class _DAclExpertAccRuleOuterCosMask_Type(OctetString):
    """Custom type dAclExpertAccRuleOuterCosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclExpertAccRuleOuterCosMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleOuterCosMask_Object = MibTableColumn
dAclExpertAccRuleOuterCosMask = _DAclExpertAccRuleOuterCosMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 40),
    _DAclExpertAccRuleOuterCosMask_Type()
)
dAclExpertAccRuleOuterCosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleOuterCosMask.setStatus("current")


class _DAclExpertAccRuleInnerCosMask_Type(OctetString):
    """Custom type dAclExpertAccRuleInnerCosMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DAclExpertAccRuleInnerCosMask_Type.__name__ = "OctetString"
_DAclExpertAccRuleInnerCosMask_Object = MibTableColumn
dAclExpertAccRuleInnerCosMask = _DAclExpertAccRuleInnerCosMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 41),
    _DAclExpertAccRuleInnerCosMask_Type()
)
dAclExpertAccRuleInnerCosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleInnerCosMask.setStatus("current")


class _DAclExpertAccRuleVlanRangeMin_Type(VlanIdOrNone):
    """Custom type dAclExpertAccRuleVlanRangeMin based on VlanIdOrNone"""
    defaultValue = 0


_DAclExpertAccRuleVlanRangeMin_Type.__name__ = "VlanIdOrNone"
_DAclExpertAccRuleVlanRangeMin_Object = MibTableColumn
dAclExpertAccRuleVlanRangeMin = _DAclExpertAccRuleVlanRangeMin_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 42),
    _DAclExpertAccRuleVlanRangeMin_Type()
)
dAclExpertAccRuleVlanRangeMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleVlanRangeMin.setStatus("current")


class _DAclExpertAccRuleVlanRangeMax_Type(VlanIdOrNone):
    """Custom type dAclExpertAccRuleVlanRangeMax based on VlanIdOrNone"""
    defaultValue = 0


_DAclExpertAccRuleVlanRangeMax_Type.__name__ = "VlanIdOrNone"
_DAclExpertAccRuleVlanRangeMax_Object = MibTableColumn
dAclExpertAccRuleVlanRangeMax = _DAclExpertAccRuleVlanRangeMax_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 3, 1, 43),
    _DAclExpertAccRuleVlanRangeMax_Type()
)
dAclExpertAccRuleVlanRangeMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccRuleVlanRangeMax.setStatus("current")
_DAclExpertAccessGroupTable_Object = MibTable
dAclExpertAccessGroupTable = _DAclExpertAccessGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 4)
)
if mibBuilder.loadTexts:
    dAclExpertAccessGroupTable.setStatus("current")
_DAclExpertAccessGroupEntry_Object = MibTableRow
dAclExpertAccessGroupEntry = _DAclExpertAccessGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 4, 1)
)
dAclExpertAccessGroupEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclExpertAccessGroupIfIndex"),
    (0, "DLINKSW-ACL-MIB", "dAclExpertAccessGroupApplyDirection"),
)
if mibBuilder.loadTexts:
    dAclExpertAccessGroupEntry.setStatus("current")
_DAclExpertAccessGroupIfIndex_Type = InterfaceIndex
_DAclExpertAccessGroupIfIndex_Object = MibTableColumn
dAclExpertAccessGroupIfIndex = _DAclExpertAccessGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 4, 1, 1),
    _DAclExpertAccessGroupIfIndex_Type()
)
dAclExpertAccessGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclExpertAccessGroupIfIndex.setStatus("current")


class _DAclExpertAccessGroupApplyDirection_Type(Integer32):
    """Custom type dAclExpertAccessGroupApplyDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inbound", 1),
          ("outbound", 2))
    )


_DAclExpertAccessGroupApplyDirection_Type.__name__ = "Integer32"
_DAclExpertAccessGroupApplyDirection_Object = MibTableColumn
dAclExpertAccessGroupApplyDirection = _DAclExpertAccessGroupApplyDirection_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 4, 1, 2),
    _DAclExpertAccessGroupApplyDirection_Type()
)
dAclExpertAccessGroupApplyDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclExpertAccessGroupApplyDirection.setStatus("current")
_DAclExpertAccessGroupRowStatus_Type = RowStatus
_DAclExpertAccessGroupRowStatus_Object = MibTableColumn
dAclExpertAccessGroupRowStatus = _DAclExpertAccessGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 4, 1, 3),
    _DAclExpertAccessGroupRowStatus_Type()
)
dAclExpertAccessGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccessGroupRowStatus.setStatus("current")


class _DAclExpertAccessGroupAclName_Type(DisplayString):
    """Custom type dAclExpertAccessGroupAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclExpertAccessGroupAclName_Type.__name__ = "DisplayString"
_DAclExpertAccessGroupAclName_Object = MibTableColumn
dAclExpertAccessGroupAclName = _DAclExpertAccessGroupAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 4, 1, 4),
    _DAclExpertAccessGroupAclName_Type()
)
dAclExpertAccessGroupAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccessGroupAclName.setStatus("current")
_DAclExpertAccessGroupAclId_Type = Integer32
_DAclExpertAccessGroupAclId_Object = MibTableColumn
dAclExpertAccessGroupAclId = _DAclExpertAccessGroupAclId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 5, 4, 1, 5),
    _DAclExpertAccessGroupAclId_Type()
)
dAclExpertAccessGroupAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclExpertAccessGroupAclId.setStatus("current")
_DAclVlan_ObjectIdentity = ObjectIdentity
dAclVlan = _DAclVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6)
)
_DAclVlanSubMapTable_Object = MibTable
dAclVlanSubMapTable = _DAclVlanSubMapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 1)
)
if mibBuilder.loadTexts:
    dAclVlanSubMapTable.setStatus("current")
_DAclVlanSubMapEntry_Object = MibTableRow
dAclVlanSubMapEntry = _DAclVlanSubMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 1, 1)
)
dAclVlanSubMapEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclVlanAccMapName"),
    (0, "DLINKSW-ACL-MIB", "dAclVlanAccSubMapSeq"),
)
if mibBuilder.loadTexts:
    dAclVlanSubMapEntry.setStatus("current")


class _DAclVlanAccMapName_Type(DisplayString):
    """Custom type dAclVlanAccMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclVlanAccMapName_Type.__name__ = "DisplayString"
_DAclVlanAccMapName_Object = MibTableColumn
dAclVlanAccMapName = _DAclVlanAccMapName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 1, 1, 1),
    _DAclVlanAccMapName_Type()
)
dAclVlanAccMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclVlanAccMapName.setStatus("current")


class _DAclVlanAccSubMapSeq_Type(Integer32):
    """Custom type dAclVlanAccSubMapSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 65535),
    )


_DAclVlanAccSubMapSeq_Type.__name__ = "Integer32"
_DAclVlanAccSubMapSeq_Object = MibTableColumn
dAclVlanAccSubMapSeq = _DAclVlanAccSubMapSeq_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 1, 1, 2),
    _DAclVlanAccSubMapSeq_Type()
)
dAclVlanAccSubMapSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclVlanAccSubMapSeq.setStatus("current")
_DAclVlanAccSubMapRowStatus_Type = RowStatus
_DAclVlanAccSubMapRowStatus_Object = MibTableColumn
dAclVlanAccSubMapRowStatus = _DAclVlanAccSubMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 1, 1, 3),
    _DAclVlanAccSubMapRowStatus_Type()
)
dAclVlanAccSubMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclVlanAccSubMapRowStatus.setStatus("current")


class _DAclVlanAccSubMapMatchAclName_Type(DisplayString):
    """Custom type dAclVlanAccSubMapMatchAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclVlanAccSubMapMatchAclName_Type.__name__ = "DisplayString"
_DAclVlanAccSubMapMatchAclName_Object = MibTableColumn
dAclVlanAccSubMapMatchAclName = _DAclVlanAccSubMapMatchAclName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 1, 1, 4),
    _DAclVlanAccSubMapMatchAclName_Type()
)
dAclVlanAccSubMapMatchAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclVlanAccSubMapMatchAclName.setStatus("current")


class _DAclVlanAccessSubMapAction_Type(Integer32):
    """Custom type dAclVlanAccessSubMapAction based on Integer32"""
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
        *(("none", 1),
          ("forward", 2),
          ("drop", 3),
          ("redirect", 4))
    )


_DAclVlanAccessSubMapAction_Type.__name__ = "Integer32"
_DAclVlanAccessSubMapAction_Object = MibTableColumn
dAclVlanAccessSubMapAction = _DAclVlanAccessSubMapAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 1, 1, 5),
    _DAclVlanAccessSubMapAction_Type()
)
dAclVlanAccessSubMapAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclVlanAccessSubMapAction.setStatus("current")
_DAclVlanAccSubMapRedirectIfIndex_Type = InterfaceIndexOrZero
_DAclVlanAccSubMapRedirectIfIndex_Object = MibTableColumn
dAclVlanAccSubMapRedirectIfIndex = _DAclVlanAccSubMapRedirectIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 1, 1, 6),
    _DAclVlanAccSubMapRedirectIfIndex_Type()
)
dAclVlanAccSubMapRedirectIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclVlanAccSubMapRedirectIfIndex.setStatus("current")
_DAclVlanAccSubMapMatchAclId_Type = Integer32
_DAclVlanAccSubMapMatchAclId_Object = MibTableColumn
dAclVlanAccSubMapMatchAclId = _DAclVlanAccSubMapMatchAclId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 1, 1, 7),
    _DAclVlanAccSubMapMatchAclId_Type()
)
dAclVlanAccSubMapMatchAclId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclVlanAccSubMapMatchAclId.setStatus("current")
_DAclVlanFilterTable_Object = MibTable
dAclVlanFilterTable = _DAclVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 2)
)
if mibBuilder.loadTexts:
    dAclVlanFilterTable.setStatus("current")
_DAclVlanFilterEntry_Object = MibTableRow
dAclVlanFilterEntry = _DAclVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 2, 1)
)
dAclVlanFilterEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclVlanFilterVlanId"),
)
if mibBuilder.loadTexts:
    dAclVlanFilterEntry.setStatus("current")
_DAclVlanFilterVlanId_Type = VlanId
_DAclVlanFilterVlanId_Object = MibTableColumn
dAclVlanFilterVlanId = _DAclVlanFilterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 2, 1, 1),
    _DAclVlanFilterVlanId_Type()
)
dAclVlanFilterVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclVlanFilterVlanId.setStatus("current")
_DAclVlanFilterRowStatus_Type = RowStatus
_DAclVlanFilterRowStatus_Object = MibTableColumn
dAclVlanFilterRowStatus = _DAclVlanFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 2, 1, 2),
    _DAclVlanFilterRowStatus_Type()
)
dAclVlanFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclVlanFilterRowStatus.setStatus("current")


class _DAclVlanFilterVlanAccMapName_Type(DisplayString):
    """Custom type dAclVlanFilterVlanAccMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclVlanFilterVlanAccMapName_Type.__name__ = "DisplayString"
_DAclVlanFilterVlanAccMapName_Object = MibTableColumn
dAclVlanFilterVlanAccMapName = _DAclVlanFilterVlanAccMapName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 2, 1, 3),
    _DAclVlanFilterVlanAccMapName_Type()
)
dAclVlanFilterVlanAccMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclVlanFilterVlanAccMapName.setStatus("current")
_DAclVlanAccessMapTable_Object = MibTable
dAclVlanAccessMapTable = _DAclVlanAccessMapTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 3)
)
if mibBuilder.loadTexts:
    dAclVlanAccessMapTable.setStatus("current")
_DAclVlanAccessMapEntry_Object = MibTableRow
dAclVlanAccessMapEntry = _DAclVlanAccessMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 3, 1)
)
dAclVlanAccessMapEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclVlanAccMapName"),
)
if mibBuilder.loadTexts:
    dAclVlanAccessMapEntry.setStatus("current")
_DAclVlanAccessMapCounterEnabled_Type = TruthValue
_DAclVlanAccessMapCounterEnabled_Object = MibTableColumn
dAclVlanAccessMapCounterEnabled = _DAclVlanAccessMapCounterEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 3, 1, 1),
    _DAclVlanAccessMapCounterEnabled_Type()
)
dAclVlanAccessMapCounterEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dAclVlanAccessMapCounterEnabled.setStatus("current")


class _DAclVlanAccessMapClearStatAction_Type(Integer32):
    """Custom type dAclVlanAccessMapClearStatAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DAclVlanAccessMapClearStatAction_Type.__name__ = "Integer32"
_DAclVlanAccessMapClearStatAction_Object = MibTableColumn
dAclVlanAccessMapClearStatAction = _DAclVlanAccessMapClearStatAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 6, 3, 1, 2),
    _DAclVlanAccessMapClearStatAction_Type()
)
dAclVlanAccessMapClearStatAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dAclVlanAccessMapClearStatAction.setStatus("current")
_DAclCounter_ObjectIdentity = ObjectIdentity
dAclCounter = _DAclCounter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7)
)
_DAclAccessGroupCounterTable_Object = MibTable
dAclAccessGroupCounterTable = _DAclAccessGroupCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 1)
)
if mibBuilder.loadTexts:
    dAclAccessGroupCounterTable.setStatus("current")
_DAclAccessGroupCounterEntry_Object = MibTableRow
dAclAccessGroupCounterEntry = _DAclAccessGroupCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 1, 1)
)
dAclAccessGroupCounterEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclAccessGroupCounterAccListId"),
    (0, "DLINKSW-ACL-MIB", "dAclAccessGroupCounterAccRuleSn"),
)
if mibBuilder.loadTexts:
    dAclAccessGroupCounterEntry.setStatus("current")
_DAclAccessGroupCounterAccListId_Type = Integer32
_DAclAccessGroupCounterAccListId_Object = MibTableColumn
dAclAccessGroupCounterAccListId = _DAclAccessGroupCounterAccListId_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 1, 1, 1),
    _DAclAccessGroupCounterAccListId_Type()
)
dAclAccessGroupCounterAccListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclAccessGroupCounterAccListId.setStatus("current")


class _DAclAccessGroupCounterAccRuleSn_Type(Integer32):
    """Custom type dAclAccessGroupCounterAccRuleSn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DAclAccessGroupCounterAccRuleSn_Type.__name__ = "Integer32"
_DAclAccessGroupCounterAccRuleSn_Object = MibTableColumn
dAclAccessGroupCounterAccRuleSn = _DAclAccessGroupCounterAccRuleSn_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 1, 1, 2),
    _DAclAccessGroupCounterAccRuleSn_Type()
)
dAclAccessGroupCounterAccRuleSn.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclAccessGroupCounterAccRuleSn.setStatus("current")
_DAclAccessGroupCounterIngressStat_Type = Counter64
_DAclAccessGroupCounterIngressStat_Object = MibTableColumn
dAclAccessGroupCounterIngressStat = _DAclAccessGroupCounterIngressStat_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 1, 1, 3),
    _DAclAccessGroupCounterIngressStat_Type()
)
dAclAccessGroupCounterIngressStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dAclAccessGroupCounterIngressStat.setStatus("current")
_DAclAccessGroupCounterEgressStat_Type = Counter64
_DAclAccessGroupCounterEgressStat_Object = MibTableColumn
dAclAccessGroupCounterEgressStat = _DAclAccessGroupCounterEgressStat_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 1, 1, 4),
    _DAclAccessGroupCounterEgressStat_Type()
)
dAclAccessGroupCounterEgressStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dAclAccessGroupCounterEgressStat.setStatus("current")
_DAclVlanFilterCounterTable_Object = MibTable
dAclVlanFilterCounterTable = _DAclVlanFilterCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 2)
)
if mibBuilder.loadTexts:
    dAclVlanFilterCounterTable.setStatus("current")
_DAclVlanFilterCounterEntry_Object = MibTableRow
dAclVlanFilterCounterEntry = _DAclVlanFilterCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 2, 1)
)
dAclVlanFilterCounterEntry.setIndexNames(
    (0, "DLINKSW-ACL-MIB", "dAclVlanFilterCounterAccMapName"),
    (0, "DLINKSW-ACL-MIB", "dAclVlanFilterCounterSubMapSeq"),
)
if mibBuilder.loadTexts:
    dAclVlanFilterCounterEntry.setStatus("current")


class _DAclVlanFilterCounterAccMapName_Type(DisplayString):
    """Custom type dAclVlanFilterCounterAccMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_DAclVlanFilterCounterAccMapName_Type.__name__ = "DisplayString"
_DAclVlanFilterCounterAccMapName_Object = MibTableColumn
dAclVlanFilterCounterAccMapName = _DAclVlanFilterCounterAccMapName_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 2, 1, 1),
    _DAclVlanFilterCounterAccMapName_Type()
)
dAclVlanFilterCounterAccMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclVlanFilterCounterAccMapName.setStatus("current")


class _DAclVlanFilterCounterSubMapSeq_Type(Integer32):
    """Custom type dAclVlanFilterCounterSubMapSeq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DAclVlanFilterCounterSubMapSeq_Type.__name__ = "Integer32"
_DAclVlanFilterCounterSubMapSeq_Object = MibTableColumn
dAclVlanFilterCounterSubMapSeq = _DAclVlanFilterCounterSubMapSeq_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 2, 1, 2),
    _DAclVlanFilterCounterSubMapSeq_Type()
)
dAclVlanFilterCounterSubMapSeq.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dAclVlanFilterCounterSubMapSeq.setStatus("current")
_DAclVlanFilterCounterStatistics_Type = Counter64
_DAclVlanFilterCounterStatistics_Object = MibTableColumn
dAclVlanFilterCounterStatistics = _DAclVlanFilterCounterStatistics_Object(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 1, 7, 2, 1, 3),
    _DAclVlanFilterCounterStatistics_Type()
)
dAclVlanFilterCounterStatistics.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dAclVlanFilterCounterStatistics.setStatus("current")
_DAclMIBConformance_ObjectIdentity = ObjectIdentity
dAclMIBConformance = _DAclMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2)
)
_DAclCompliances_ObjectIdentity = ObjectIdentity
dAclCompliances = _DAclCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 1)
)
_DAclGroups_ObjectIdentity = ObjectIdentity
dAclGroups = _DAclGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 2)
)

# Managed Objects groups

dAclGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 2, 1)
)
dAclGenGroup.setObjects(
      *(("DLINKSW-ACL-MIB", "dAclReSeqStartingNumber"),
        ("DLINKSW-ACL-MIB", "dAclReSeqIncrement"))
)
if mibBuilder.loadTexts:
    dAclGenGroup.setStatus("current")

dAclMacGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 2, 2)
)
dAclMacGroup.setObjects(
      *(("DLINKSW-ACL-MIB", "dAclMacAccessListNumber"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessListRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessListId"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessListCounterEnabled"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessListClearStatAction"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessListRemark"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleAction"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleSrcMacAddr"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleSrcMacWildcard"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleDstMacAddr"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleDstMacWildcard"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRulePacketType"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleEthernetType"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleLlcDSAP"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleLlcSSAP"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleLlcCntl"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleDot1p"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleInnerDot1p"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleVlanID"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleInnerVlanID"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessRuleTimeName"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessGroupRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessGroupAclName"),
        ("DLINKSW-ACL-MIB", "dAclMacAccessGroupAclId"))
)
if mibBuilder.loadTexts:
    dAclMacGroup.setStatus("current")

dAclIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 2, 3)
)
dAclIpGroup.setObjects(
      *(("DLINKSW-ACL-MIB", "dAclIpAccessListNumber"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessListRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessExtended"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessListId"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessListCounterEnabled"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessListClearStatAction"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessListRemark"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleAction"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleProtocol"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleUserDefProtocol"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleSrcAddr"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleSrcWildcard"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleDstAddr"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleDstWildcard"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleSrcOperator"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleSrcPort"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleSrcPortRange"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleDstOperator"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleDstPort"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleDstPortRange"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleQosPrecedence"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleQosTos"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleQosDscp"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleIcmpType"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleIcmpCode"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessRuleTimeName"),
        ("DLINKSW-ACL-MIB", "dAclIpAccRuleTcpFlag"),
        ("DLINKSW-ACL-MIB", "dAclIpAccRuleFragments"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessGroupStatus"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessGroupAclName"),
        ("DLINKSW-ACL-MIB", "dAclIpAccessGroupAclId"))
)
if mibBuilder.loadTexts:
    dAclIpGroup.setStatus("current")

dAclIPv6Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 2, 4)
)
dAclIPv6Group.setObjects(
      *(("DLINKSW-ACL-MIB", "dAclIPv6AccessListNumber"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessListRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessExtended"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessListId"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessListCounterEnabled"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessListClearStatAction"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessListRemark"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleAction"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleProtocol"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleUserDefProtocol"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleSrcAddr"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleSrcPrefixLen"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleDstAddr"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleDstPrefixLen"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleSrcOperator"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleSrcPort"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleSrcPortRange"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleDstOperator"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleDstPort"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleDstPortRange"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleDscp"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleIcmpType"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleIcmpCode"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessRuleTimeName"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessGroupStatus"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessGroupAclName"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccessGroupAclId"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccRuleTcpFlag"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccRuleFragments"),
        ("DLINKSW-ACL-MIB", "dAclIPv6AccRuleFlowLabel"))
)
if mibBuilder.loadTexts:
    dAclIPv6Group.setStatus("current")

dAclExpertGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 2, 5)
)
dAclExpertGroup.setObjects(
      *(("DLINKSW-ACL-MIB", "dAclExpertAccessListNumber"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccessListRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccessListId"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccessListCounterEnabled"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccessListClearStatAction"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccessListRemark"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleAction"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleProtocol"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleUserDefProtocol"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleSrcIpAddr"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleSrcIpWildcard"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleSrcMacAddr"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleSrcMacWildcard"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleSrcOperator"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleSrcPort"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleSrcPortRange"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleDstIpAddr"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleDstIpWildcard"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleDstMacAddr"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleDstMacWildcard"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleDstOperator"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleDstPort"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleDstPortRange"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleVlanID"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleInnerVlanID"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleQosPrecedence"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleQosTos"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleQosDscp"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleIcmpType"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleIcmpCode"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleTimeName"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccessGroupRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccessGroupAclName"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccessGroupAclId"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleTcpFlag"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleFragments"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleOuterCos"),
        ("DLINKSW-ACL-MIB", "dAclExpertAccRuleInnerCos"))
)
if mibBuilder.loadTexts:
    dAclExpertGroup.setStatus("current")

dAclVlanFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 2, 6)
)
dAclVlanFilterGroup.setObjects(
      *(("DLINKSW-ACL-MIB", "dAclVlanAccSubMapRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclVlanAccSubMapMatchAclName"),
        ("DLINKSW-ACL-MIB", "dAclVlanAccessSubMapAction"),
        ("DLINKSW-ACL-MIB", "dAclVlanAccSubMapRedirectIfIndex"),
        ("DLINKSW-ACL-MIB", "dAclVlanFilterRowStatus"),
        ("DLINKSW-ACL-MIB", "dAclVlanFilterVlanAccMapName"),
        ("DLINKSW-ACL-MIB", "dAclVlanAccSubMapMatchAclId"),
        ("DLINKSW-ACL-MIB", "dAclVlanAccessMapCounterEnabled"),
        ("DLINKSW-ACL-MIB", "dAclVlanAccessMapClearStatAction"))
)
if mibBuilder.loadTexts:
    dAclVlanFilterGroup.setStatus("current")

dAclCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 2, 7)
)
dAclCounterGroup.setObjects(
      *(("DLINKSW-ACL-MIB", "dAclAccessGroupCounterIngressStat"),
        ("DLINKSW-ACL-MIB", "dAclAccessGroupCounterEgressStat"),
        ("DLINKSW-ACL-MIB", "dAclVlanFilterCounterStatistics"))
)
if mibBuilder.loadTexts:
    dAclCounterGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dAclCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 14, 28, 2, 1, 1)
)
dAclCompliance.setObjects(
      *(("DLINKSW-ACL-MIB", "dAclGenGroup"),
        ("DLINKSW-ACL-MIB", "dAclMacGroup"),
        ("DLINKSW-ACL-MIB", "dAclIpGroup"),
        ("DLINKSW-ACL-MIB", "dAclIPv6Group"),
        ("DLINKSW-ACL-MIB", "dAclExpertGroup"),
        ("DLINKSW-ACL-MIB", "dAclVlanFilterGroup"))
)
if mibBuilder.loadTexts:
    dAclCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKSW-ACL-MIB",
    **{"DlinkAclRuleType": DlinkAclRuleType,
       "DlinkAclPortOperatorType": DlinkAclPortOperatorType,
       "TcpFlag": TcpFlag,
       "dlinkSwAclMIB": dlinkSwAclMIB,
       "dAclMIBNotifications": dAclMIBNotifications,
       "dAclMIBObjects": dAclMIBObjects,
       "dAclGeneral": dAclGeneral,
       "dAclReSeqTable": dAclReSeqTable,
       "dAclReSeqEntry": dAclReSeqEntry,
       "dAclReSeqAccessListName": dAclReSeqAccessListName,
       "dAclReSeqStartingNumber": dAclReSeqStartingNumber,
       "dAclReSeqIncrement": dAclReSeqIncrement,
       "dAclMac": dAclMac,
       "dAclMacAccessListNumber": dAclMacAccessListNumber,
       "dAclMacAccessListTable": dAclMacAccessListTable,
       "dAclMacAccessListEntry": dAclMacAccessListEntry,
       "dAclMacAccessListName": dAclMacAccessListName,
       "dAclMacAccessListRowStatus": dAclMacAccessListRowStatus,
       "dAclMacAccessListId": dAclMacAccessListId,
       "dAclMacAccessListCounterEnabled": dAclMacAccessListCounterEnabled,
       "dAclMacAccessListClearStatAction": dAclMacAccessListClearStatAction,
       "dAclMacAccessListRemark": dAclMacAccessListRemark,
       "dAclMacAccessRuleTable": dAclMacAccessRuleTable,
       "dAclMacAccessRuleEntry": dAclMacAccessRuleEntry,
       "dAclMacAccessRuleSn": dAclMacAccessRuleSn,
       "dAclMacAccessRuleRowStatus": dAclMacAccessRuleRowStatus,
       "dAclMacAccessRuleAction": dAclMacAccessRuleAction,
       "dAclMacAccessRuleSrcMacAddr": dAclMacAccessRuleSrcMacAddr,
       "dAclMacAccessRuleSrcMacWildcard": dAclMacAccessRuleSrcMacWildcard,
       "dAclMacAccessRuleDstMacAddr": dAclMacAccessRuleDstMacAddr,
       "dAclMacAccessRuleDstMacWildcard": dAclMacAccessRuleDstMacWildcard,
       "dAclMacAccessRulePacketType": dAclMacAccessRulePacketType,
       "dAclMacAccessRuleEthernetType": dAclMacAccessRuleEthernetType,
       "dAclMacAccessRuleLlcDSAP": dAclMacAccessRuleLlcDSAP,
       "dAclMacAccessRuleLlcSSAP": dAclMacAccessRuleLlcSSAP,
       "dAclMacAccessRuleLlcCntl": dAclMacAccessRuleLlcCntl,
       "dAclMacAccessRuleDot1p": dAclMacAccessRuleDot1p,
       "dAclMacAccessRuleInnerDot1p": dAclMacAccessRuleInnerDot1p,
       "dAclMacAccessRuleVlanID": dAclMacAccessRuleVlanID,
       "dAclMacAccessRuleInnerVlanID": dAclMacAccessRuleInnerVlanID,
       "dAclMacAccessRuleTimeName": dAclMacAccessRuleTimeName,
       "dAclMacAccessRuleEthernetTypeMask": dAclMacAccessRuleEthernetTypeMask,
       "dAclMacAccessRuleDot1pMask": dAclMacAccessRuleDot1pMask,
       "dAclMacAccessRuleInnerDot1pMask": dAclMacAccessRuleInnerDot1pMask,
       "dAclMacAccessRuleVlanIDMask": dAclMacAccessRuleVlanIDMask,
       "dAclMacAccessRuleInnerVlanIDMask": dAclMacAccessRuleInnerVlanIDMask,
       "dAclMacAccessRuleVlanRangeMin": dAclMacAccessRuleVlanRangeMin,
       "dAclMacAccessRuleVlanRangeMax": dAclMacAccessRuleVlanRangeMax,
       "dAclMacAccessGroupTable": dAclMacAccessGroupTable,
       "dAclMacAccessGroupEntry": dAclMacAccessGroupEntry,
       "dAclMacAccessGroupIfIndex": dAclMacAccessGroupIfIndex,
       "dAclMacAccessGroupApplyDirection": dAclMacAccessGroupApplyDirection,
       "dAclMacAccessGroupRowStatus": dAclMacAccessGroupRowStatus,
       "dAclMacAccessGroupAclName": dAclMacAccessGroupAclName,
       "dAclMacAccessGroupAclId": dAclMacAccessGroupAclId,
       "dAclIp": dAclIp,
       "dAclIpAccessListNumber": dAclIpAccessListNumber,
       "dAclIpAccessListTable": dAclIpAccessListTable,
       "dAclIpAccessListEntry": dAclIpAccessListEntry,
       "dAclIpAccessListName": dAclIpAccessListName,
       "dAclIpAccessListRowStatus": dAclIpAccessListRowStatus,
       "dAclIpAccessExtended": dAclIpAccessExtended,
       "dAclIpAccessListId": dAclIpAccessListId,
       "dAclIpAccessListCounterEnabled": dAclIpAccessListCounterEnabled,
       "dAclIpAccessListClearStatAction": dAclIpAccessListClearStatAction,
       "dAclIpAccessListRemark": dAclIpAccessListRemark,
       "dAclIpAccessRuleTable": dAclIpAccessRuleTable,
       "dAclIpAccessRuleEntry": dAclIpAccessRuleEntry,
       "dAclIpAccessRuleSn": dAclIpAccessRuleSn,
       "dAclIpAccessRuleRowStatus": dAclIpAccessRuleRowStatus,
       "dAclIpAccessRuleAction": dAclIpAccessRuleAction,
       "dAclIpAccessRuleProtocol": dAclIpAccessRuleProtocol,
       "dAclIpAccessRuleUserDefProtocol": dAclIpAccessRuleUserDefProtocol,
       "dAclIpAccessRuleSrcAddr": dAclIpAccessRuleSrcAddr,
       "dAclIpAccessRuleSrcWildcard": dAclIpAccessRuleSrcWildcard,
       "dAclIpAccessRuleDstAddr": dAclIpAccessRuleDstAddr,
       "dAclIpAccessRuleDstWildcard": dAclIpAccessRuleDstWildcard,
       "dAclIpAccessRuleSrcOperator": dAclIpAccessRuleSrcOperator,
       "dAclIpAccessRuleSrcPort": dAclIpAccessRuleSrcPort,
       "dAclIpAccessRuleSrcPortRange": dAclIpAccessRuleSrcPortRange,
       "dAclIpAccessRuleDstOperator": dAclIpAccessRuleDstOperator,
       "dAclIpAccessRuleDstPort": dAclIpAccessRuleDstPort,
       "dAclIpAccessRuleDstPortRange": dAclIpAccessRuleDstPortRange,
       "dAclIpAccessRuleQosPrecedence": dAclIpAccessRuleQosPrecedence,
       "dAclIpAccessRuleQosTos": dAclIpAccessRuleQosTos,
       "dAclIpAccessRuleQosDscp": dAclIpAccessRuleQosDscp,
       "dAclIpAccessRuleIcmpType": dAclIpAccessRuleIcmpType,
       "dAclIpAccessRuleIcmpCode": dAclIpAccessRuleIcmpCode,
       "dAclIpAccessRuleTimeName": dAclIpAccessRuleTimeName,
       "dAclIpAccRuleTcpFlag": dAclIpAccRuleTcpFlag,
       "dAclIpAccRuleFragments": dAclIpAccRuleFragments,
       "dAclIpAccRuleUserDefProtocolMask": dAclIpAccRuleUserDefProtocolMask,
       "dAclIpAccRuleSrcPortMask": dAclIpAccRuleSrcPortMask,
       "dAclIpAccRuleDstPortMask": dAclIpAccRuleDstPortMask,
       "dAclIpAccRuleQosPrecedenceMask": dAclIpAccRuleQosPrecedenceMask,
       "dAclIpAccRuleQosTosMask": dAclIpAccRuleQosTosMask,
       "dAclIpAccRuleQosDscpMask": dAclIpAccRuleQosDscpMask,
       "dAclIpAccessGroupTable": dAclIpAccessGroupTable,
       "dAclIpAccessGroupEntry": dAclIpAccessGroupEntry,
       "dAclIpAccessGroupIfIndex": dAclIpAccessGroupIfIndex,
       "dAclIpAccessGroupApplyDirection": dAclIpAccessGroupApplyDirection,
       "dAclIpAccessGroupStatus": dAclIpAccessGroupStatus,
       "dAclIpAccessGroupAclName": dAclIpAccessGroupAclName,
       "dAclIpAccessGroupAclId": dAclIpAccessGroupAclId,
       "dAclIPv6": dAclIPv6,
       "dAclIPv6AccessListNumber": dAclIPv6AccessListNumber,
       "dAclIPv6AccessListTable": dAclIPv6AccessListTable,
       "dAclIPv6AccessListEntry": dAclIPv6AccessListEntry,
       "dAclIPv6AccessListName": dAclIPv6AccessListName,
       "dAclIPv6AccessListRowStatus": dAclIPv6AccessListRowStatus,
       "dAclIPv6AccessExtended": dAclIPv6AccessExtended,
       "dAclIPv6AccessListId": dAclIPv6AccessListId,
       "dAclIPv6AccessListCounterEnabled": dAclIPv6AccessListCounterEnabled,
       "dAclIPv6AccessListClearStatAction": dAclIPv6AccessListClearStatAction,
       "dAclIPv6AccessListRemark": dAclIPv6AccessListRemark,
       "dAclIPv6AccessRuleTable": dAclIPv6AccessRuleTable,
       "dAclIPv6AccessRuleEntry": dAclIPv6AccessRuleEntry,
       "dAclIPv6AccessRuleSn": dAclIPv6AccessRuleSn,
       "dAclIPv6AccessRuleRowStatus": dAclIPv6AccessRuleRowStatus,
       "dAclIPv6AccessRuleAction": dAclIPv6AccessRuleAction,
       "dAclIPv6AccessRuleProtocol": dAclIPv6AccessRuleProtocol,
       "dAclIPv6AccessRuleUserDefProtocol": dAclIPv6AccessRuleUserDefProtocol,
       "dAclIPv6AccessRuleSrcAddr": dAclIPv6AccessRuleSrcAddr,
       "dAclIPv6AccessRuleSrcPrefixLen": dAclIPv6AccessRuleSrcPrefixLen,
       "dAclIPv6AccessRuleDstAddr": dAclIPv6AccessRuleDstAddr,
       "dAclIPv6AccessRuleDstPrefixLen": dAclIPv6AccessRuleDstPrefixLen,
       "dAclIPv6AccessRuleSrcOperator": dAclIPv6AccessRuleSrcOperator,
       "dAclIPv6AccessRuleSrcPort": dAclIPv6AccessRuleSrcPort,
       "dAclIPv6AccessRuleSrcPortRange": dAclIPv6AccessRuleSrcPortRange,
       "dAclIPv6AccessRuleDstOperator": dAclIPv6AccessRuleDstOperator,
       "dAclIPv6AccessRuleDstPort": dAclIPv6AccessRuleDstPort,
       "dAclIPv6AccessRuleDstPortRange": dAclIPv6AccessRuleDstPortRange,
       "dAclIPv6AccessRuleDscp": dAclIPv6AccessRuleDscp,
       "dAclIPv6AccessRuleIcmpType": dAclIPv6AccessRuleIcmpType,
       "dAclIPv6AccessRuleIcmpCode": dAclIPv6AccessRuleIcmpCode,
       "dAclIPv6AccessRuleTimeName": dAclIPv6AccessRuleTimeName,
       "dAclIPv6AccRuleTcpFlag": dAclIPv6AccRuleTcpFlag,
       "dAclIPv6AccRuleFragments": dAclIPv6AccRuleFragments,
       "dAclIPv6AccRuleFlowLabel": dAclIPv6AccRuleFlowLabel,
       "dAclIPv6AccRuleTrafficClass": dAclIPv6AccRuleTrafficClass,
       "dAclIPv6AccRuleUserDefProtocolMask": dAclIPv6AccRuleUserDefProtocolMask,
       "dAclIPv6AccRuleSrcPortMask": dAclIPv6AccRuleSrcPortMask,
       "dAclIPv6AccRuleDstPortMask": dAclIPv6AccRuleDstPortMask,
       "dAclIPv6AccRuleDscpMask": dAclIPv6AccRuleDscpMask,
       "dAclIPv6AccRuleFlowLabelMask": dAclIPv6AccRuleFlowLabelMask,
       "dAclIPv6AccRuleTrafficClassMask": dAclIPv6AccRuleTrafficClassMask,
       "dAclIPv6AccessGroupTable": dAclIPv6AccessGroupTable,
       "dAclIPv6AccessGroupEntry": dAclIPv6AccessGroupEntry,
       "dAclIPv6AccessGroupIfIndex": dAclIPv6AccessGroupIfIndex,
       "dAclIpv6AccessGroupApplyDirection": dAclIpv6AccessGroupApplyDirection,
       "dAclIPv6AccessGroupStatus": dAclIPv6AccessGroupStatus,
       "dAclIPv6AccessGroupAclName": dAclIPv6AccessGroupAclName,
       "dAclIPv6AccessGroupAclId": dAclIPv6AccessGroupAclId,
       "dAclExpert": dAclExpert,
       "dAclExpertAccessListNumber": dAclExpertAccessListNumber,
       "dAclExpertAccessListTable": dAclExpertAccessListTable,
       "dAclExpertAccessListEntry": dAclExpertAccessListEntry,
       "dAclExpertAccessListName": dAclExpertAccessListName,
       "dAclExpertAccessListRowStatus": dAclExpertAccessListRowStatus,
       "dAclExpertAccessListId": dAclExpertAccessListId,
       "dAclExpertAccessListCounterEnabled": dAclExpertAccessListCounterEnabled,
       "dAclExpertAccessListClearStatAction": dAclExpertAccessListClearStatAction,
       "dAclExpertAccessListRemark": dAclExpertAccessListRemark,
       "dAclExpertAccessRuleTable": dAclExpertAccessRuleTable,
       "dAclExpertAccessRuleEntry": dAclExpertAccessRuleEntry,
       "dAclExpertAccRuleSn": dAclExpertAccRuleSn,
       "dAclExpertAccRuleRowStatus": dAclExpertAccRuleRowStatus,
       "dAclExpertAccRuleAction": dAclExpertAccRuleAction,
       "dAclExpertAccRuleProtocol": dAclExpertAccRuleProtocol,
       "dAclExpertAccRuleUserDefProtocol": dAclExpertAccRuleUserDefProtocol,
       "dAclExpertAccRuleSrcIpAddr": dAclExpertAccRuleSrcIpAddr,
       "dAclExpertAccRuleSrcIpWildcard": dAclExpertAccRuleSrcIpWildcard,
       "dAclExpertAccRuleSrcMacAddr": dAclExpertAccRuleSrcMacAddr,
       "dAclExpertAccRuleSrcMacWildcard": dAclExpertAccRuleSrcMacWildcard,
       "dAclExpertAccRuleSrcOperator": dAclExpertAccRuleSrcOperator,
       "dAclExpertAccRuleSrcPort": dAclExpertAccRuleSrcPort,
       "dAclExpertAccRuleSrcPortRange": dAclExpertAccRuleSrcPortRange,
       "dAclExpertAccRuleDstIpAddr": dAclExpertAccRuleDstIpAddr,
       "dAclExpertAccRuleDstIpWildcard": dAclExpertAccRuleDstIpWildcard,
       "dAclExpertAccRuleDstMacAddr": dAclExpertAccRuleDstMacAddr,
       "dAclExpertAccRuleDstMacWildcard": dAclExpertAccRuleDstMacWildcard,
       "dAclExpertAccRuleDstOperator": dAclExpertAccRuleDstOperator,
       "dAclExpertAccRuleDstPort": dAclExpertAccRuleDstPort,
       "dAclExpertAccRuleDstPortRange": dAclExpertAccRuleDstPortRange,
       "dAclExpertAccRuleVlanID": dAclExpertAccRuleVlanID,
       "dAclExpertAccRuleInnerVlanID": dAclExpertAccRuleInnerVlanID,
       "dAclExpertAccRuleQosPrecedence": dAclExpertAccRuleQosPrecedence,
       "dAclExpertAccRuleQosTos": dAclExpertAccRuleQosTos,
       "dAclExpertAccRuleQosDscp": dAclExpertAccRuleQosDscp,
       "dAclExpertAccRuleIcmpType": dAclExpertAccRuleIcmpType,
       "dAclExpertAccRuleIcmpCode": dAclExpertAccRuleIcmpCode,
       "dAclExpertAccRuleTimeName": dAclExpertAccRuleTimeName,
       "dAclExpertAccRuleTcpFlag": dAclExpertAccRuleTcpFlag,
       "dAclExpertAccRuleFragments": dAclExpertAccRuleFragments,
       "dAclExpertAccRuleOuterCos": dAclExpertAccRuleOuterCos,
       "dAclExpertAccRuleInnerCos": dAclExpertAccRuleInnerCos,
       "dAclExpertAccRuleUserDefProtocolMask": dAclExpertAccRuleUserDefProtocolMask,
       "dAclExpertAccRuleSrcPortMask": dAclExpertAccRuleSrcPortMask,
       "dAclExpertAccRuleDstPortMask": dAclExpertAccRuleDstPortMask,
       "dAclExpertAccRuleVlanIDMask": dAclExpertAccRuleVlanIDMask,
       "dAclExpertAccRuleInnerVlanIDMask": dAclExpertAccRuleInnerVlanIDMask,
       "dAclExpertAccRuleQosPrecedenceMask": dAclExpertAccRuleQosPrecedenceMask,
       "dAclExpertAccRuleQosTosMask": dAclExpertAccRuleQosTosMask,
       "dAclExpertAccRuleQosDscpMask": dAclExpertAccRuleQosDscpMask,
       "dAclExpertAccRuleOuterCosMask": dAclExpertAccRuleOuterCosMask,
       "dAclExpertAccRuleInnerCosMask": dAclExpertAccRuleInnerCosMask,
       "dAclExpertAccRuleVlanRangeMin": dAclExpertAccRuleVlanRangeMin,
       "dAclExpertAccRuleVlanRangeMax": dAclExpertAccRuleVlanRangeMax,
       "dAclExpertAccessGroupTable": dAclExpertAccessGroupTable,
       "dAclExpertAccessGroupEntry": dAclExpertAccessGroupEntry,
       "dAclExpertAccessGroupIfIndex": dAclExpertAccessGroupIfIndex,
       "dAclExpertAccessGroupApplyDirection": dAclExpertAccessGroupApplyDirection,
       "dAclExpertAccessGroupRowStatus": dAclExpertAccessGroupRowStatus,
       "dAclExpertAccessGroupAclName": dAclExpertAccessGroupAclName,
       "dAclExpertAccessGroupAclId": dAclExpertAccessGroupAclId,
       "dAclVlan": dAclVlan,
       "dAclVlanSubMapTable": dAclVlanSubMapTable,
       "dAclVlanSubMapEntry": dAclVlanSubMapEntry,
       "dAclVlanAccMapName": dAclVlanAccMapName,
       "dAclVlanAccSubMapSeq": dAclVlanAccSubMapSeq,
       "dAclVlanAccSubMapRowStatus": dAclVlanAccSubMapRowStatus,
       "dAclVlanAccSubMapMatchAclName": dAclVlanAccSubMapMatchAclName,
       "dAclVlanAccessSubMapAction": dAclVlanAccessSubMapAction,
       "dAclVlanAccSubMapRedirectIfIndex": dAclVlanAccSubMapRedirectIfIndex,
       "dAclVlanAccSubMapMatchAclId": dAclVlanAccSubMapMatchAclId,
       "dAclVlanFilterTable": dAclVlanFilterTable,
       "dAclVlanFilterEntry": dAclVlanFilterEntry,
       "dAclVlanFilterVlanId": dAclVlanFilterVlanId,
       "dAclVlanFilterRowStatus": dAclVlanFilterRowStatus,
       "dAclVlanFilterVlanAccMapName": dAclVlanFilterVlanAccMapName,
       "dAclVlanAccessMapTable": dAclVlanAccessMapTable,
       "dAclVlanAccessMapEntry": dAclVlanAccessMapEntry,
       "dAclVlanAccessMapCounterEnabled": dAclVlanAccessMapCounterEnabled,
       "dAclVlanAccessMapClearStatAction": dAclVlanAccessMapClearStatAction,
       "dAclCounter": dAclCounter,
       "dAclAccessGroupCounterTable": dAclAccessGroupCounterTable,
       "dAclAccessGroupCounterEntry": dAclAccessGroupCounterEntry,
       "dAclAccessGroupCounterAccListId": dAclAccessGroupCounterAccListId,
       "dAclAccessGroupCounterAccRuleSn": dAclAccessGroupCounterAccRuleSn,
       "dAclAccessGroupCounterIngressStat": dAclAccessGroupCounterIngressStat,
       "dAclAccessGroupCounterEgressStat": dAclAccessGroupCounterEgressStat,
       "dAclVlanFilterCounterTable": dAclVlanFilterCounterTable,
       "dAclVlanFilterCounterEntry": dAclVlanFilterCounterEntry,
       "dAclVlanFilterCounterAccMapName": dAclVlanFilterCounterAccMapName,
       "dAclVlanFilterCounterSubMapSeq": dAclVlanFilterCounterSubMapSeq,
       "dAclVlanFilterCounterStatistics": dAclVlanFilterCounterStatistics,
       "dAclMIBConformance": dAclMIBConformance,
       "dAclCompliances": dAclCompliances,
       "dAclCompliance": dAclCompliance,
       "dAclGroups": dAclGroups,
       "dAclGenGroup": dAclGenGroup,
       "dAclMacGroup": dAclMacGroup,
       "dAclIpGroup": dAclIpGroup,
       "dAclIPv6Group": dAclIPv6Group,
       "dAclExpertGroup": dAclExpertGroup,
       "dAclVlanFilterGroup": dAclVlanFilterGroup,
       "dAclCounterGroup": dAclCounterGroup}
)
