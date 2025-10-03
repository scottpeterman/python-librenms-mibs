# SNMP MIB module (DOCS-SUBMGT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\arris\DOCS-SUBMGT-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:18:40 2025
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

(docsIfCmtsCmStatusEntry,
 docsIfCmtsCmStatusIndex) = mibBuilder.importSymbols(
    "DOCS-IF-MIB",
    "docsIfCmtsCmStatusEntry",
    "docsIfCmtsCmStatusIndex")

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
 experimental,
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
    "experimental",
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

docsSubMgt = ModuleIdentity(
    (1, 3, 6, 1, 3, 83, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class IpV4orV6Addr(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )



# MIB Managed Objects in the order of their OIDs

_DocsSubMgtObjects_ObjectIdentity = ObjectIdentity
docsSubMgtObjects = _DocsSubMgtObjects_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 4, 1)
)
_DocsSubMgtCpeControlTable_Object = MibTable
docsSubMgtCpeControlTable = _DocsSubMgtCpeControlTable_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 1)
)
if mibBuilder.loadTexts:
    docsSubMgtCpeControlTable.setStatus("current")
_DocsSubMgtCpeControlEntry_Object = MibTableRow
docsSubMgtCpeControlEntry = _DocsSubMgtCpeControlEntry_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    docsSubMgtCpeControlEntry.setStatus("current")


class _DocsSubMgtCpeControlMaxCpeIp_Type(Integer32):
    """Custom type docsSubMgtCpeControlMaxCpeIp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtCpeControlMaxCpeIp_Type.__name__ = "Integer32"
_DocsSubMgtCpeControlMaxCpeIp_Object = MibTableColumn
docsSubMgtCpeControlMaxCpeIp = _DocsSubMgtCpeControlMaxCpeIp_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 1),
    _DocsSubMgtCpeControlMaxCpeIp_Type()
)
docsSubMgtCpeControlMaxCpeIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeControlMaxCpeIp.setStatus("current")
_DocsSubMgtCpeControlActive_Type = TruthValue
_DocsSubMgtCpeControlActive_Object = MibTableColumn
docsSubMgtCpeControlActive = _DocsSubMgtCpeControlActive_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 2),
    _DocsSubMgtCpeControlActive_Type()
)
docsSubMgtCpeControlActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeControlActive.setStatus("current")
_DocsSubMgtCpeControlLearnable_Type = TruthValue
_DocsSubMgtCpeControlLearnable_Object = MibTableColumn
docsSubMgtCpeControlLearnable = _DocsSubMgtCpeControlLearnable_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 3),
    _DocsSubMgtCpeControlLearnable_Type()
)
docsSubMgtCpeControlLearnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeControlLearnable.setStatus("current")
_DocsSubMgtCpeControlReset_Type = TruthValue
_DocsSubMgtCpeControlReset_Object = MibTableColumn
docsSubMgtCpeControlReset = _DocsSubMgtCpeControlReset_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 1, 1, 4),
    _DocsSubMgtCpeControlReset_Type()
)
docsSubMgtCpeControlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeControlReset.setStatus("current")


class _DocsSubMgtCpeMaxIpDefault_Type(Integer32):
    """Custom type docsSubMgtCpeMaxIpDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtCpeMaxIpDefault_Type.__name__ = "Integer32"
_DocsSubMgtCpeMaxIpDefault_Object = MibScalar
docsSubMgtCpeMaxIpDefault = _DocsSubMgtCpeMaxIpDefault_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 2),
    _DocsSubMgtCpeMaxIpDefault_Type()
)
docsSubMgtCpeMaxIpDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeMaxIpDefault.setStatus("current")
_DocsSubMgtCpeActiveDefault_Type = TruthValue
_DocsSubMgtCpeActiveDefault_Object = MibScalar
docsSubMgtCpeActiveDefault = _DocsSubMgtCpeActiveDefault_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 3),
    _DocsSubMgtCpeActiveDefault_Type()
)
docsSubMgtCpeActiveDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeActiveDefault.setStatus("current")
_DocsSubMgtCpeLearnableDefault_Type = TruthValue
_DocsSubMgtCpeLearnableDefault_Object = MibScalar
docsSubMgtCpeLearnableDefault = _DocsSubMgtCpeLearnableDefault_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 4),
    _DocsSubMgtCpeLearnableDefault_Type()
)
docsSubMgtCpeLearnableDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCpeLearnableDefault.setStatus("current")
_DocsSubMgtCpeIpTable_Object = MibTable
docsSubMgtCpeIpTable = _DocsSubMgtCpeIpTable_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 5)
)
if mibBuilder.loadTexts:
    docsSubMgtCpeIpTable.setStatus("current")
_DocsSubMgtCpeIpEntry_Object = MibTableRow
docsSubMgtCpeIpEntry = _DocsSubMgtCpeIpEntry_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 5, 1)
)
docsSubMgtCpeIpEntry.setIndexNames(
    (0, "DOCS-IF-MIB", "docsIfCmtsCmStatusIndex"),
    (0, "DOCS-SUBMGT-MIB", "docsSubMgtCpeIpIndex"),
)
if mibBuilder.loadTexts:
    docsSubMgtCpeIpEntry.setStatus("current")


class _DocsSubMgtCpeIpIndex_Type(Integer32):
    """Custom type docsSubMgtCpeIpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DocsSubMgtCpeIpIndex_Type.__name__ = "Integer32"
_DocsSubMgtCpeIpIndex_Object = MibTableColumn
docsSubMgtCpeIpIndex = _DocsSubMgtCpeIpIndex_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 5, 1, 1),
    _DocsSubMgtCpeIpIndex_Type()
)
docsSubMgtCpeIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSubMgtCpeIpIndex.setStatus("current")
_DocsSubMgtCpeIpAddr_Type = IpV4orV6Addr
_DocsSubMgtCpeIpAddr_Object = MibTableColumn
docsSubMgtCpeIpAddr = _DocsSubMgtCpeIpAddr_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 5, 1, 2),
    _DocsSubMgtCpeIpAddr_Type()
)
docsSubMgtCpeIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubMgtCpeIpAddr.setStatus("current")
_DocsSubMgtCpeIpLearned_Type = TruthValue
_DocsSubMgtCpeIpLearned_Object = MibTableColumn
docsSubMgtCpeIpLearned = _DocsSubMgtCpeIpLearned_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 5, 1, 3),
    _DocsSubMgtCpeIpLearned_Type()
)
docsSubMgtCpeIpLearned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubMgtCpeIpLearned.setStatus("current")
_DocsSubMgtPktFilterTable_Object = MibTable
docsSubMgtPktFilterTable = _DocsSubMgtPktFilterTable_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6)
)
if mibBuilder.loadTexts:
    docsSubMgtPktFilterTable.setStatus("current")
_DocsSubMgtPktFilterEntry_Object = MibTableRow
docsSubMgtPktFilterEntry = _DocsSubMgtPktFilterEntry_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1)
)
docsSubMgtPktFilterEntry.setIndexNames(
    (0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterGroup"),
    (0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterIndex"),
)
if mibBuilder.loadTexts:
    docsSubMgtPktFilterEntry.setStatus("current")


class _DocsSubMgtPktFilterGroup_Type(Integer32):
    """Custom type docsSubMgtPktFilterGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DocsSubMgtPktFilterGroup_Type.__name__ = "Integer32"
_DocsSubMgtPktFilterGroup_Object = MibTableColumn
docsSubMgtPktFilterGroup = _DocsSubMgtPktFilterGroup_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 1),
    _DocsSubMgtPktFilterGroup_Type()
)
docsSubMgtPktFilterGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterGroup.setStatus("current")


class _DocsSubMgtPktFilterIndex_Type(Integer32):
    """Custom type docsSubMgtPktFilterIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_DocsSubMgtPktFilterIndex_Type.__name__ = "Integer32"
_DocsSubMgtPktFilterIndex_Object = MibTableColumn
docsSubMgtPktFilterIndex = _DocsSubMgtPktFilterIndex_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 2),
    _DocsSubMgtPktFilterIndex_Type()
)
docsSubMgtPktFilterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterIndex.setStatus("current")


class _DocsSubMgtPktFilterSrcAddr_Type(IpV4orV6Addr):
    """Custom type docsSubMgtPktFilterSrcAddr based on IpV4orV6Addr"""
    defaultHexValue = ""


_DocsSubMgtPktFilterSrcAddr_Type.__name__ = "IpV4orV6Addr"
_DocsSubMgtPktFilterSrcAddr_Object = MibTableColumn
docsSubMgtPktFilterSrcAddr = _DocsSubMgtPktFilterSrcAddr_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 3),
    _DocsSubMgtPktFilterSrcAddr_Type()
)
docsSubMgtPktFilterSrcAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterSrcAddr.setStatus("current")


class _DocsSubMgtPktFilterSrcMask_Type(IpV4orV6Addr):
    """Custom type docsSubMgtPktFilterSrcMask based on IpV4orV6Addr"""
    defaultHexValue = ""


_DocsSubMgtPktFilterSrcMask_Type.__name__ = "IpV4orV6Addr"
_DocsSubMgtPktFilterSrcMask_Object = MibTableColumn
docsSubMgtPktFilterSrcMask = _DocsSubMgtPktFilterSrcMask_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 4),
    _DocsSubMgtPktFilterSrcMask_Type()
)
docsSubMgtPktFilterSrcMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterSrcMask.setStatus("current")


class _DocsSubMgtPktFilterDstAddr_Type(IpV4orV6Addr):
    """Custom type docsSubMgtPktFilterDstAddr based on IpV4orV6Addr"""
    defaultHexValue = ""


_DocsSubMgtPktFilterDstAddr_Type.__name__ = "IpV4orV6Addr"
_DocsSubMgtPktFilterDstAddr_Object = MibTableColumn
docsSubMgtPktFilterDstAddr = _DocsSubMgtPktFilterDstAddr_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 5),
    _DocsSubMgtPktFilterDstAddr_Type()
)
docsSubMgtPktFilterDstAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterDstAddr.setStatus("current")


class _DocsSubMgtPktFilterDstMask_Type(IpV4orV6Addr):
    """Custom type docsSubMgtPktFilterDstMask based on IpV4orV6Addr"""
    defaultHexValue = ""


_DocsSubMgtPktFilterDstMask_Type.__name__ = "IpV4orV6Addr"
_DocsSubMgtPktFilterDstMask_Object = MibTableColumn
docsSubMgtPktFilterDstMask = _DocsSubMgtPktFilterDstMask_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 6),
    _DocsSubMgtPktFilterDstMask_Type()
)
docsSubMgtPktFilterDstMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterDstMask.setStatus("current")


class _DocsSubMgtPktFilterUlp_Type(Integer32):
    """Custom type docsSubMgtPktFilterUlp based on Integer32"""
    defaultValue = 256

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_DocsSubMgtPktFilterUlp_Type.__name__ = "Integer32"
_DocsSubMgtPktFilterUlp_Object = MibTableColumn
docsSubMgtPktFilterUlp = _DocsSubMgtPktFilterUlp_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 7),
    _DocsSubMgtPktFilterUlp_Type()
)
docsSubMgtPktFilterUlp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterUlp.setStatus("current")


class _DocsSubMgtPktFilterTosValue_Type(OctetString):
    """Custom type docsSubMgtPktFilterTosValue based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DocsSubMgtPktFilterTosValue_Type.__name__ = "OctetString"
_DocsSubMgtPktFilterTosValue_Object = MibTableColumn
docsSubMgtPktFilterTosValue = _DocsSubMgtPktFilterTosValue_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 8),
    _DocsSubMgtPktFilterTosValue_Type()
)
docsSubMgtPktFilterTosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterTosValue.setStatus("current")


class _DocsSubMgtPktFilterTosMask_Type(OctetString):
    """Custom type docsSubMgtPktFilterTosMask based on OctetString"""
    defaultHexValue = "00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_DocsSubMgtPktFilterTosMask_Type.__name__ = "OctetString"
_DocsSubMgtPktFilterTosMask_Object = MibTableColumn
docsSubMgtPktFilterTosMask = _DocsSubMgtPktFilterTosMask_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 9),
    _DocsSubMgtPktFilterTosMask_Type()
)
docsSubMgtPktFilterTosMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterTosMask.setStatus("current")


class _DocsSubMgtPktFilterAction_Type(Integer32):
    """Custom type docsSubMgtPktFilterAction based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("accept", 1),
          ("drop", 2))
    )


_DocsSubMgtPktFilterAction_Type.__name__ = "Integer32"
_DocsSubMgtPktFilterAction_Object = MibTableColumn
docsSubMgtPktFilterAction = _DocsSubMgtPktFilterAction_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 10),
    _DocsSubMgtPktFilterAction_Type()
)
docsSubMgtPktFilterAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterAction.setStatus("current")
_DocsSubMgtPktFilterMatches_Type = Counter32
_DocsSubMgtPktFilterMatches_Object = MibTableColumn
docsSubMgtPktFilterMatches = _DocsSubMgtPktFilterMatches_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 11),
    _DocsSubMgtPktFilterMatches_Type()
)
docsSubMgtPktFilterMatches.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterMatches.setStatus("current")
_DocsSubMgtPktFilterStatus_Type = RowStatus
_DocsSubMgtPktFilterStatus_Object = MibTableColumn
docsSubMgtPktFilterStatus = _DocsSubMgtPktFilterStatus_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 6, 1, 12),
    _DocsSubMgtPktFilterStatus_Type()
)
docsSubMgtPktFilterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtPktFilterStatus.setStatus("current")
_DocsSubMgtTcpUdpFilterTable_Object = MibTable
docsSubMgtTcpUdpFilterTable = _DocsSubMgtTcpUdpFilterTable_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 7)
)
if mibBuilder.loadTexts:
    docsSubMgtTcpUdpFilterTable.setStatus("current")
_DocsSubMgtTcpUdpFilterEntry_Object = MibTableRow
docsSubMgtTcpUdpFilterEntry = _DocsSubMgtTcpUdpFilterEntry_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 7, 1)
)
docsSubMgtTcpUdpFilterEntry.setIndexNames(
    (0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterGroup"),
    (0, "DOCS-SUBMGT-MIB", "docsSubMgtPktFilterIndex"),
)
if mibBuilder.loadTexts:
    docsSubMgtTcpUdpFilterEntry.setStatus("current")


class _DocsSubMgtTcpUdpSrcPort_Type(Integer32):
    """Custom type docsSubMgtTcpUdpSrcPort based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_DocsSubMgtTcpUdpSrcPort_Type.__name__ = "Integer32"
_DocsSubMgtTcpUdpSrcPort_Object = MibTableColumn
docsSubMgtTcpUdpSrcPort = _DocsSubMgtTcpUdpSrcPort_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 1),
    _DocsSubMgtTcpUdpSrcPort_Type()
)
docsSubMgtTcpUdpSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtTcpUdpSrcPort.setStatus("current")


class _DocsSubMgtTcpUdpDstPort_Type(Integer32):
    """Custom type docsSubMgtTcpUdpDstPort based on Integer32"""
    defaultValue = 65536

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65536),
    )


_DocsSubMgtTcpUdpDstPort_Type.__name__ = "Integer32"
_DocsSubMgtTcpUdpDstPort_Object = MibTableColumn
docsSubMgtTcpUdpDstPort = _DocsSubMgtTcpUdpDstPort_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 2),
    _DocsSubMgtTcpUdpDstPort_Type()
)
docsSubMgtTcpUdpDstPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtTcpUdpDstPort.setStatus("current")


class _DocsSubMgtTcpFlagValues_Type(Bits):
    """Custom type docsSubMgtTcpFlagValues based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("urgent", 0),
          ("ack", 1),
          ("push", 2),
          ("reset", 3),
          ("syn", 4),
          ("fin", 5))
    )

_DocsSubMgtTcpFlagValues_Type.__name__ = "Bits"
_DocsSubMgtTcpFlagValues_Object = MibTableColumn
docsSubMgtTcpFlagValues = _DocsSubMgtTcpFlagValues_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 3),
    _DocsSubMgtTcpFlagValues_Type()
)
docsSubMgtTcpFlagValues.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtTcpFlagValues.setStatus("current")


class _DocsSubMgtTcpFlagMask_Type(Bits):
    """Custom type docsSubMgtTcpFlagMask based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("urgent", 0),
          ("ack", 1),
          ("push", 2),
          ("reset", 3),
          ("syn", 4),
          ("fin", 5))
    )

_DocsSubMgtTcpFlagMask_Type.__name__ = "Bits"
_DocsSubMgtTcpFlagMask_Object = MibTableColumn
docsSubMgtTcpFlagMask = _DocsSubMgtTcpFlagMask_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 4),
    _DocsSubMgtTcpFlagMask_Type()
)
docsSubMgtTcpFlagMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtTcpFlagMask.setStatus("current")
_DocsSubMgtTcpUdpStatus_Type = RowStatus
_DocsSubMgtTcpUdpStatus_Object = MibTableColumn
docsSubMgtTcpUdpStatus = _DocsSubMgtTcpUdpStatus_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 7, 1, 5),
    _DocsSubMgtTcpUdpStatus_Type()
)
docsSubMgtTcpUdpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    docsSubMgtTcpUdpStatus.setStatus("current")
_DocsSubMgtCmFilterTable_Object = MibTable
docsSubMgtCmFilterTable = _DocsSubMgtCmFilterTable_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 8)
)
if mibBuilder.loadTexts:
    docsSubMgtCmFilterTable.setStatus("current")
_DocsSubMgtCmFilterEntry_Object = MibTableRow
docsSubMgtCmFilterEntry = _DocsSubMgtCmFilterEntry_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 8, 1)
)
if mibBuilder.loadTexts:
    docsSubMgtCmFilterEntry.setStatus("current")


class _DocsSubMgtSubFilterDownstream_Type(Integer32):
    """Custom type docsSubMgtSubFilterDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtSubFilterDownstream_Type.__name__ = "Integer32"
_DocsSubMgtSubFilterDownstream_Object = MibTableColumn
docsSubMgtSubFilterDownstream = _DocsSubMgtSubFilterDownstream_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 1),
    _DocsSubMgtSubFilterDownstream_Type()
)
docsSubMgtSubFilterDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtSubFilterDownstream.setStatus("current")


class _DocsSubMgtSubFilterUpstream_Type(Integer32):
    """Custom type docsSubMgtSubFilterUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtSubFilterUpstream_Type.__name__ = "Integer32"
_DocsSubMgtSubFilterUpstream_Object = MibTableColumn
docsSubMgtSubFilterUpstream = _DocsSubMgtSubFilterUpstream_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 2),
    _DocsSubMgtSubFilterUpstream_Type()
)
docsSubMgtSubFilterUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtSubFilterUpstream.setStatus("current")


class _DocsSubMgtCmFilterDownstream_Type(Integer32):
    """Custom type docsSubMgtCmFilterDownstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtCmFilterDownstream_Type.__name__ = "Integer32"
_DocsSubMgtCmFilterDownstream_Object = MibTableColumn
docsSubMgtCmFilterDownstream = _DocsSubMgtCmFilterDownstream_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 3),
    _DocsSubMgtCmFilterDownstream_Type()
)
docsSubMgtCmFilterDownstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCmFilterDownstream.setStatus("current")


class _DocsSubMgtCmFilterUpstream_Type(Integer32):
    """Custom type docsSubMgtCmFilterUpstream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtCmFilterUpstream_Type.__name__ = "Integer32"
_DocsSubMgtCmFilterUpstream_Object = MibTableColumn
docsSubMgtCmFilterUpstream = _DocsSubMgtCmFilterUpstream_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 8, 1, 4),
    _DocsSubMgtCmFilterUpstream_Type()
)
docsSubMgtCmFilterUpstream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCmFilterUpstream.setStatus("current")


class _DocsSubMgtSubFilterDownDefault_Type(Integer32):
    """Custom type docsSubMgtSubFilterDownDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtSubFilterDownDefault_Type.__name__ = "Integer32"
_DocsSubMgtSubFilterDownDefault_Object = MibScalar
docsSubMgtSubFilterDownDefault = _DocsSubMgtSubFilterDownDefault_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 9),
    _DocsSubMgtSubFilterDownDefault_Type()
)
docsSubMgtSubFilterDownDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtSubFilterDownDefault.setStatus("current")


class _DocsSubMgtSubFilterUpDefault_Type(Integer32):
    """Custom type docsSubMgtSubFilterUpDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtSubFilterUpDefault_Type.__name__ = "Integer32"
_DocsSubMgtSubFilterUpDefault_Object = MibScalar
docsSubMgtSubFilterUpDefault = _DocsSubMgtSubFilterUpDefault_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 10),
    _DocsSubMgtSubFilterUpDefault_Type()
)
docsSubMgtSubFilterUpDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtSubFilterUpDefault.setStatus("current")


class _DocsSubMgtCmFilterDownDefault_Type(Integer32):
    """Custom type docsSubMgtCmFilterDownDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtCmFilterDownDefault_Type.__name__ = "Integer32"
_DocsSubMgtCmFilterDownDefault_Object = MibScalar
docsSubMgtCmFilterDownDefault = _DocsSubMgtCmFilterDownDefault_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 11),
    _DocsSubMgtCmFilterDownDefault_Type()
)
docsSubMgtCmFilterDownDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCmFilterDownDefault.setStatus("current")


class _DocsSubMgtCmFilterUpDefault_Type(Integer32):
    """Custom type docsSubMgtCmFilterUpDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_DocsSubMgtCmFilterUpDefault_Type.__name__ = "Integer32"
_DocsSubMgtCmFilterUpDefault_Object = MibScalar
docsSubMgtCmFilterUpDefault = _DocsSubMgtCmFilterUpDefault_Object(
    (1, 3, 6, 1, 3, 83, 4, 1, 12),
    _DocsSubMgtCmFilterUpDefault_Type()
)
docsSubMgtCmFilterUpDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    docsSubMgtCmFilterUpDefault.setStatus("current")
_DocsSubMgtNotification_ObjectIdentity = ObjectIdentity
docsSubMgtNotification = _DocsSubMgtNotification_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 4, 2)
)
_DocsSubMgtConformance_ObjectIdentity = ObjectIdentity
docsSubMgtConformance = _DocsSubMgtConformance_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 4, 3)
)
_DocsSubMgtCompliances_ObjectIdentity = ObjectIdentity
docsSubMgtCompliances = _DocsSubMgtCompliances_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 4, 3, 1)
)
_DocsSubMgtGroups_ObjectIdentity = ObjectIdentity
docsSubMgtGroups = _DocsSubMgtGroups_ObjectIdentity(
    (1, 3, 6, 1, 3, 83, 4, 3, 2)
)
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("DOCS-SUBMGT-MIB",
     "docsSubMgtCpeControlEntry")
)
docsSubMgtCpeControlEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())
docsIfCmtsCmStatusEntry.registerAugmentions(
    ("DOCS-SUBMGT-MIB",
     "docsSubMgtCmFilterEntry")
)
docsSubMgtCmFilterEntry.setIndexNames(*docsIfCmtsCmStatusEntry.getIndexNames())

# Managed Objects groups

docsSubMgtGroup = ObjectGroup(
    (1, 3, 6, 1, 3, 83, 4, 3, 2, 1)
)
docsSubMgtGroup.setObjects(
      *(("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlMaxCpeIp"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlActive"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlLearnable"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCpeControlReset"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCpeMaxIpDefault"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCpeActiveDefault"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCpeLearnableDefault"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCpeIpAddr"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCpeIpLearned"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterSrcAddr"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterSrcMask"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterDstAddr"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterDstMask"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterUlp"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterTosValue"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterTosMask"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterAction"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterMatches"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtPktFilterStatus"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtTcpUdpSrcPort"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtTcpUdpDstPort"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtTcpFlagValues"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtTcpFlagMask"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtTcpUdpStatus"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterDownstream"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterUpstream"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterDownstream"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterUpstream"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterDownDefault"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtSubFilterUpDefault"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterDownDefault"),
        ("DOCS-SUBMGT-MIB", "docsSubMgtCmFilterUpDefault"))
)
if mibBuilder.loadTexts:
    docsSubMgtGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

docsSubMgtBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 3, 83, 4, 3, 1, 1)
)
docsSubMgtBasicCompliance.setObjects(
    ("DOCS-SUBMGT-MIB", "docsSubMgtGroup")
)
if mibBuilder.loadTexts:
    docsSubMgtBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DOCS-SUBMGT-MIB",
    **{"IpV4orV6Addr": IpV4orV6Addr,
       "docsSubMgt": docsSubMgt,
       "docsSubMgtObjects": docsSubMgtObjects,
       "docsSubMgtCpeControlTable": docsSubMgtCpeControlTable,
       "docsSubMgtCpeControlEntry": docsSubMgtCpeControlEntry,
       "docsSubMgtCpeControlMaxCpeIp": docsSubMgtCpeControlMaxCpeIp,
       "docsSubMgtCpeControlActive": docsSubMgtCpeControlActive,
       "docsSubMgtCpeControlLearnable": docsSubMgtCpeControlLearnable,
       "docsSubMgtCpeControlReset": docsSubMgtCpeControlReset,
       "docsSubMgtCpeMaxIpDefault": docsSubMgtCpeMaxIpDefault,
       "docsSubMgtCpeActiveDefault": docsSubMgtCpeActiveDefault,
       "docsSubMgtCpeLearnableDefault": docsSubMgtCpeLearnableDefault,
       "docsSubMgtCpeIpTable": docsSubMgtCpeIpTable,
       "docsSubMgtCpeIpEntry": docsSubMgtCpeIpEntry,
       "docsSubMgtCpeIpIndex": docsSubMgtCpeIpIndex,
       "docsSubMgtCpeIpAddr": docsSubMgtCpeIpAddr,
       "docsSubMgtCpeIpLearned": docsSubMgtCpeIpLearned,
       "docsSubMgtPktFilterTable": docsSubMgtPktFilterTable,
       "docsSubMgtPktFilterEntry": docsSubMgtPktFilterEntry,
       "docsSubMgtPktFilterGroup": docsSubMgtPktFilterGroup,
       "docsSubMgtPktFilterIndex": docsSubMgtPktFilterIndex,
       "docsSubMgtPktFilterSrcAddr": docsSubMgtPktFilterSrcAddr,
       "docsSubMgtPktFilterSrcMask": docsSubMgtPktFilterSrcMask,
       "docsSubMgtPktFilterDstAddr": docsSubMgtPktFilterDstAddr,
       "docsSubMgtPktFilterDstMask": docsSubMgtPktFilterDstMask,
       "docsSubMgtPktFilterUlp": docsSubMgtPktFilterUlp,
       "docsSubMgtPktFilterTosValue": docsSubMgtPktFilterTosValue,
       "docsSubMgtPktFilterTosMask": docsSubMgtPktFilterTosMask,
       "docsSubMgtPktFilterAction": docsSubMgtPktFilterAction,
       "docsSubMgtPktFilterMatches": docsSubMgtPktFilterMatches,
       "docsSubMgtPktFilterStatus": docsSubMgtPktFilterStatus,
       "docsSubMgtTcpUdpFilterTable": docsSubMgtTcpUdpFilterTable,
       "docsSubMgtTcpUdpFilterEntry": docsSubMgtTcpUdpFilterEntry,
       "docsSubMgtTcpUdpSrcPort": docsSubMgtTcpUdpSrcPort,
       "docsSubMgtTcpUdpDstPort": docsSubMgtTcpUdpDstPort,
       "docsSubMgtTcpFlagValues": docsSubMgtTcpFlagValues,
       "docsSubMgtTcpFlagMask": docsSubMgtTcpFlagMask,
       "docsSubMgtTcpUdpStatus": docsSubMgtTcpUdpStatus,
       "docsSubMgtCmFilterTable": docsSubMgtCmFilterTable,
       "docsSubMgtCmFilterEntry": docsSubMgtCmFilterEntry,
       "docsSubMgtSubFilterDownstream": docsSubMgtSubFilterDownstream,
       "docsSubMgtSubFilterUpstream": docsSubMgtSubFilterUpstream,
       "docsSubMgtCmFilterDownstream": docsSubMgtCmFilterDownstream,
       "docsSubMgtCmFilterUpstream": docsSubMgtCmFilterUpstream,
       "docsSubMgtSubFilterDownDefault": docsSubMgtSubFilterDownDefault,
       "docsSubMgtSubFilterUpDefault": docsSubMgtSubFilterUpDefault,
       "docsSubMgtCmFilterDownDefault": docsSubMgtCmFilterDownDefault,
       "docsSubMgtCmFilterUpDefault": docsSubMgtCmFilterUpDefault,
       "docsSubMgtNotification": docsSubMgtNotification,
       "docsSubMgtConformance": docsSubMgtConformance,
       "docsSubMgtCompliances": docsSubMgtCompliances,
       "docsSubMgtBasicCompliance": docsSubMgtBasicCompliance,
       "docsSubMgtGroups": docsSubMgtGroups,
       "docsSubMgtGroup": docsSubMgtGroup}
)
