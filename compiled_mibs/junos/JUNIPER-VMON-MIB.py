# SNMP MIB module (JUNIPER-VMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junos\JUNIPER-VMON-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:05:05 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(jnxServices,
 jnxVmonMibRoot) = mibBuilder.importSymbols(
    "JUNIPER-SMI",
    "jnxServices",
    "jnxVmonMibRoot")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

jnxVmonMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1)
)
if mibBuilder.loadTexts:
    jnxVmonMIB.setRevisions(
        ("2013-12-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JnxVmonFlowType(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )



class JnxVmonTrapLevel(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              4,
              6,
              8)
        )
    )
    namedValues = NamedValues(
        *(("critical", 2),
          ("warning", 4),
          ("info", 6),
          ("clear", 8))
    )



class JnxVmonFlowDirection(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



# MIB Managed Objects in the order of their OIDs

_JnxVmonServices_ObjectIdentity = ObjectIdentity
jnxVmonServices = _JnxVmonServices_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1)
)
_JnxmdiStatsTable_Object = MibTable
jnxmdiStatsTable = _JnxmdiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1)
)
if mibBuilder.loadTexts:
    jnxmdiStatsTable.setStatus("current")
_JnxmdiStatsEntry_Object = MibTableRow
jnxmdiStatsEntry = _JnxmdiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1)
)
jnxmdiStatsEntry.setIndexNames(
    (0, "JUNIPER-VMON-MIB", "jnxmdiFPCSlotNo"),
)
if mibBuilder.loadTexts:
    jnxmdiStatsEntry.setStatus("current")


class _JnxmdiFPCSlotNo_Type(Unsigned32):
    """Custom type jnxmdiFPCSlotNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JnxmdiFPCSlotNo_Type.__name__ = "Unsigned32"
_JnxmdiFPCSlotNo_Object = MibTableColumn
jnxmdiFPCSlotNo = _JnxmdiFPCSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 1),
    _JnxmdiFPCSlotNo_Type()
)
jnxmdiFPCSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxmdiFPCSlotNo.setStatus("current")
_JnxmdiActiveFlowsCount_Type = Counter64
_JnxmdiActiveFlowsCount_Object = MibTableColumn
jnxmdiActiveFlowsCount = _JnxmdiActiveFlowsCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 2),
    _JnxmdiActiveFlowsCount_Type()
)
jnxmdiActiveFlowsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiActiveFlowsCount.setStatus("current")
_JnxmdiInsertedFlowsCount_Type = Counter64
_JnxmdiInsertedFlowsCount_Object = MibTableColumn
jnxmdiInsertedFlowsCount = _JnxmdiInsertedFlowsCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 3),
    _JnxmdiInsertedFlowsCount_Type()
)
jnxmdiInsertedFlowsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiInsertedFlowsCount.setStatus("current")
_JnxmdiDeletedFlowsCount_Type = Counter64
_JnxmdiDeletedFlowsCount_Object = MibTableColumn
jnxmdiDeletedFlowsCount = _JnxmdiDeletedFlowsCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 4),
    _JnxmdiDeletedFlowsCount_Type()
)
jnxmdiDeletedFlowsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiDeletedFlowsCount.setStatus("current")
_JnxmdiTotalPktsCount_Type = Counter64
_JnxmdiTotalPktsCount_Object = MibTableColumn
jnxmdiTotalPktsCount = _JnxmdiTotalPktsCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 5),
    _JnxmdiTotalPktsCount_Type()
)
jnxmdiTotalPktsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiTotalPktsCount.setStatus("current")
_JnxmdiTotalBytesCount_Type = Counter64
_JnxmdiTotalBytesCount_Object = MibTableColumn
jnxmdiTotalBytesCount = _JnxmdiTotalBytesCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 6),
    _JnxmdiTotalBytesCount_Type()
)
jnxmdiTotalBytesCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiTotalBytesCount.setStatus("current")
_JnxmdiDFTotalAlarmCount_Type = Counter64
_JnxmdiDFTotalAlarmCount_Object = MibTableColumn
jnxmdiDFTotalAlarmCount = _JnxmdiDFTotalAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 7),
    _JnxmdiDFTotalAlarmCount_Type()
)
jnxmdiDFTotalAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiDFTotalAlarmCount.setStatus("current")
_JnxmdiDFInfoAlarmCount_Type = Counter64
_JnxmdiDFInfoAlarmCount_Object = MibTableColumn
jnxmdiDFInfoAlarmCount = _JnxmdiDFInfoAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 8),
    _JnxmdiDFInfoAlarmCount_Type()
)
jnxmdiDFInfoAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiDFInfoAlarmCount.setStatus("current")
_JnxmdiDFWarningAlarmCount_Type = Counter64
_JnxmdiDFWarningAlarmCount_Object = MibTableColumn
jnxmdiDFWarningAlarmCount = _JnxmdiDFWarningAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 9),
    _JnxmdiDFWarningAlarmCount_Type()
)
jnxmdiDFWarningAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiDFWarningAlarmCount.setStatus("current")
_JnxmdiDFCriticalAlarmCount_Type = Counter64
_JnxmdiDFCriticalAlarmCount_Object = MibTableColumn
jnxmdiDFCriticalAlarmCount = _JnxmdiDFCriticalAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 10),
    _JnxmdiDFCriticalAlarmCount_Type()
)
jnxmdiDFCriticalAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiDFCriticalAlarmCount.setStatus("current")
_JnxmdiMLRTotalAlarmCount_Type = Counter64
_JnxmdiMLRTotalAlarmCount_Object = MibTableColumn
jnxmdiMLRTotalAlarmCount = _JnxmdiMLRTotalAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 11),
    _JnxmdiMLRTotalAlarmCount_Type()
)
jnxmdiMLRTotalAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiMLRTotalAlarmCount.setStatus("current")
_JnxmdiMLRInfoAlarmCount_Type = Counter64
_JnxmdiMLRInfoAlarmCount_Object = MibTableColumn
jnxmdiMLRInfoAlarmCount = _JnxmdiMLRInfoAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 12),
    _JnxmdiMLRInfoAlarmCount_Type()
)
jnxmdiMLRInfoAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiMLRInfoAlarmCount.setStatus("current")
_JnxmdiMLRWarningAlarmCount_Type = Counter64
_JnxmdiMLRWarningAlarmCount_Object = MibTableColumn
jnxmdiMLRWarningAlarmCount = _JnxmdiMLRWarningAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 13),
    _JnxmdiMLRWarningAlarmCount_Type()
)
jnxmdiMLRWarningAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiMLRWarningAlarmCount.setStatus("current")
_JnxmdiMLRCriticalAlarmCount_Type = Counter64
_JnxmdiMLRCriticalAlarmCount_Object = MibTableColumn
jnxmdiMLRCriticalAlarmCount = _JnxmdiMLRCriticalAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 14),
    _JnxmdiMLRCriticalAlarmCount_Type()
)
jnxmdiMLRCriticalAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiMLRCriticalAlarmCount.setStatus("current")
_JnxmdiMRVTotalAlarmCount_Type = Counter64
_JnxmdiMRVTotalAlarmCount_Object = MibTableColumn
jnxmdiMRVTotalAlarmCount = _JnxmdiMRVTotalAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 15),
    _JnxmdiMRVTotalAlarmCount_Type()
)
jnxmdiMRVTotalAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiMRVTotalAlarmCount.setStatus("current")
_JnxmdiMRVInfoAlarmCount_Type = Counter64
_JnxmdiMRVInfoAlarmCount_Object = MibTableColumn
jnxmdiMRVInfoAlarmCount = _JnxmdiMRVInfoAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 16),
    _JnxmdiMRVInfoAlarmCount_Type()
)
jnxmdiMRVInfoAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiMRVInfoAlarmCount.setStatus("current")
_JnxmdiMRVWarningAlarmCount_Type = Counter64
_JnxmdiMRVWarningAlarmCount_Object = MibTableColumn
jnxmdiMRVWarningAlarmCount = _JnxmdiMRVWarningAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 17),
    _JnxmdiMRVWarningAlarmCount_Type()
)
jnxmdiMRVWarningAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiMRVWarningAlarmCount.setStatus("current")
_JnxmdiMRVCriticalAlarmCount_Type = Counter64
_JnxmdiMRVCriticalAlarmCount_Object = MibTableColumn
jnxmdiMRVCriticalAlarmCount = _JnxmdiMRVCriticalAlarmCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 1, 1, 18),
    _JnxmdiMRVCriticalAlarmCount_Type()
)
jnxmdiMRVCriticalAlarmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiMRVCriticalAlarmCount.setStatus("current")
_JnxmdiErrsTable_Object = MibTable
jnxmdiErrsTable = _JnxmdiErrsTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 2)
)
if mibBuilder.loadTexts:
    jnxmdiErrsTable.setStatus("current")
_JnxmdiErrsEntry_Object = MibTableRow
jnxmdiErrsEntry = _JnxmdiErrsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 2, 1)
)
jnxmdiErrsEntry.setIndexNames(
    (0, "JUNIPER-VMON-MIB", "jnxmdiFPCSlotNo"),
)
if mibBuilder.loadTexts:
    jnxmdiErrsEntry.setStatus("current")
_JnxmdiErrsFlowInsertErr_Type = Counter64
_JnxmdiErrsFlowInsertErr_Object = MibTableColumn
jnxmdiErrsFlowInsertErr = _JnxmdiErrsFlowInsertErr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 2, 1, 1),
    _JnxmdiErrsFlowInsertErr_Type()
)
jnxmdiErrsFlowInsertErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiErrsFlowInsertErr.setStatus("current")
_JnxmdiErrsPolicerDrop_Type = Counter64
_JnxmdiErrsPolicerDrop_Object = MibTableColumn
jnxmdiErrsPolicerDrop = _JnxmdiErrsPolicerDrop_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 2, 1, 2),
    _JnxmdiErrsPolicerDrop_Type()
)
jnxmdiErrsPolicerDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiErrsPolicerDrop.setStatus("current")
_JnxmdiErrsPIDLimitExceed_Type = Counter64
_JnxmdiErrsPIDLimitExceed_Object = MibTableColumn
jnxmdiErrsPIDLimitExceed = _JnxmdiErrsPIDLimitExceed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 2, 1, 3),
    _JnxmdiErrsPIDLimitExceed_Type()
)
jnxmdiErrsPIDLimitExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiErrsPIDLimitExceed.setStatus("current")
_JnxmdiErrsUnsupportedMediaPkts_Type = Counter64
_JnxmdiErrsUnsupportedMediaPkts_Object = MibTableColumn
jnxmdiErrsUnsupportedMediaPkts = _JnxmdiErrsUnsupportedMediaPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 2, 1, 4),
    _JnxmdiErrsUnsupportedMediaPkts_Type()
)
jnxmdiErrsUnsupportedMediaPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiErrsUnsupportedMediaPkts.setStatus("current")
_JnxmdiErrsFragmentedPkts_Type = Counter64
_JnxmdiErrsFragmentedPkts_Object = MibTableColumn
jnxmdiErrsFragmentedPkts = _JnxmdiErrsFragmentedPkts_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 2, 1, 5),
    _JnxmdiErrsFragmentedPkts_Type()
)
jnxmdiErrsFragmentedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiErrsFragmentedPkts.setStatus("current")
_JnxmdiErrsMaxLabelsExceed_Type = Counter64
_JnxmdiErrsMaxLabelsExceed_Object = MibTableColumn
jnxmdiErrsMaxLabelsExceed = _JnxmdiErrsMaxLabelsExceed_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 2, 1, 6),
    _JnxmdiErrsMaxLabelsExceed_Type()
)
jnxmdiErrsMaxLabelsExceed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiErrsMaxLabelsExceed.setStatus("current")
_JnxmdiErrsOptionPkt_Type = Counter64
_JnxmdiErrsOptionPkt_Object = MibTableColumn
jnxmdiErrsOptionPkt = _JnxmdiErrsOptionPkt_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 2, 1, 7),
    _JnxmdiErrsOptionPkt_Type()
)
jnxmdiErrsOptionPkt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiErrsOptionPkt.setStatus("current")
_JnxmdiFlowTable_Object = MibTable
jnxmdiFlowTable = _JnxmdiFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3)
)
if mibBuilder.loadTexts:
    jnxmdiFlowTable.setStatus("current")
_JnxmdiFlowEntry_Object = MibTableRow
jnxmdiFlowEntry = _JnxmdiFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1)
)
jnxmdiFlowEntry.setIndexNames(
    (0, "JUNIPER-VMON-MIB", "jnxmdiFPCSlotNo"),
    (0, "JUNIPER-VMON-MIB", "jnxmdiFlowIdentifier"),
)
if mibBuilder.loadTexts:
    jnxmdiFlowEntry.setStatus("current")
_JnxmdiFlowIdentifier_Type = Unsigned32
_JnxmdiFlowIdentifier_Object = MibTableColumn
jnxmdiFlowIdentifier = _JnxmdiFlowIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 1),
    _JnxmdiFlowIdentifier_Type()
)
jnxmdiFlowIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxmdiFlowIdentifier.setStatus("current")
_JnxmdiFlowSrcAddr_Type = InetAddress
_JnxmdiFlowSrcAddr_Object = MibTableColumn
jnxmdiFlowSrcAddr = _JnxmdiFlowSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 2),
    _JnxmdiFlowSrcAddr_Type()
)
jnxmdiFlowSrcAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowSrcAddr.setStatus("current")
_JnxmdiFlowDstAddr_Type = InetAddress
_JnxmdiFlowDstAddr_Object = MibTableColumn
jnxmdiFlowDstAddr = _JnxmdiFlowDstAddr_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 3),
    _JnxmdiFlowDstAddr_Type()
)
jnxmdiFlowDstAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowDstAddr.setStatus("current")
_JnxmdiFlowAddrFamily_Type = InetAddressType
_JnxmdiFlowAddrFamily_Object = MibTableColumn
jnxmdiFlowAddrFamily = _JnxmdiFlowAddrFamily_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 4),
    _JnxmdiFlowAddrFamily_Type()
)
jnxmdiFlowAddrFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowAddrFamily.setStatus("current")
_JnxmdiFlowSrcPort_Type = InetPortNumber
_JnxmdiFlowSrcPort_Object = MibTableColumn
jnxmdiFlowSrcPort = _JnxmdiFlowSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 5),
    _JnxmdiFlowSrcPort_Type()
)
jnxmdiFlowSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowSrcPort.setStatus("current")
_JnxmdiFlowDstPort_Type = InetPortNumber
_JnxmdiFlowDstPort_Object = MibTableColumn
jnxmdiFlowDstPort = _JnxmdiFlowDstPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 6),
    _JnxmdiFlowDstPort_Type()
)
jnxmdiFlowDstPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowDstPort.setStatus("current")
_JnxmdiFlowInterfaceName_Type = DisplayString
_JnxmdiFlowInterfaceName_Object = MibTableColumn
jnxmdiFlowInterfaceName = _JnxmdiFlowInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 7),
    _JnxmdiFlowInterfaceName_Type()
)
jnxmdiFlowInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowInterfaceName.setStatus("current")
_JnxmdiFlowInterfaceSNMPIndex_Type = InterfaceIndexOrZero
_JnxmdiFlowInterfaceSNMPIndex_Object = MibTableColumn
jnxmdiFlowInterfaceSNMPIndex = _JnxmdiFlowInterfaceSNMPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 8),
    _JnxmdiFlowInterfaceSNMPIndex_Type()
)
jnxmdiFlowInterfaceSNMPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowInterfaceSNMPIndex.setStatus("current")
_JnxmdiFlowDirection_Type = JnxVmonFlowDirection
_JnxmdiFlowDirection_Object = MibTableColumn
jnxmdiFlowDirection = _JnxmdiFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 9),
    _JnxmdiFlowDirection_Type()
)
jnxmdiFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowDirection.setStatus("current")
_JnxmdiFlowType_Type = JnxVmonFlowType
_JnxmdiFlowType_Object = MibTableColumn
jnxmdiFlowType = _JnxmdiFlowType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 10),
    _JnxmdiFlowType_Type()
)
jnxmdiFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowType.setStatus("current")
_JnxmdiFlowLastDF_Type = DisplayString
_JnxmdiFlowLastDF_Object = MibTableColumn
jnxmdiFlowLastDF = _JnxmdiFlowLastDF_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 11),
    _JnxmdiFlowLastDF_Type()
)
jnxmdiFlowLastDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowLastDF.setStatus("current")


class _JnxmdiFlowLastMLR_Type(Unsigned32):
    """Custom type jnxmdiFlowLastMLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxmdiFlowLastMLR_Type.__name__ = "Unsigned32"
_JnxmdiFlowLastMLR_Object = MibTableColumn
jnxmdiFlowLastMLR = _JnxmdiFlowLastMLR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 12),
    _JnxmdiFlowLastMLR_Type()
)
jnxmdiFlowLastMLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowLastMLR.setStatus("current")
_JnxmdiFlowLastMRV_Type = DisplayString
_JnxmdiFlowLastMRV_Object = MibTableColumn
jnxmdiFlowLastMRV = _JnxmdiFlowLastMRV_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 13),
    _JnxmdiFlowLastMRV_Type()
)
jnxmdiFlowLastMRV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowLastMRV.setStatus("current")
_JnxmdiFlowAvgDF_Type = DisplayString
_JnxmdiFlowAvgDF_Object = MibTableColumn
jnxmdiFlowAvgDF = _JnxmdiFlowAvgDF_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 14),
    _JnxmdiFlowAvgDF_Type()
)
jnxmdiFlowAvgDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowAvgDF.setStatus("current")


class _JnxmdiFlowAvgMLR_Type(Unsigned32):
    """Custom type jnxmdiFlowAvgMLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxmdiFlowAvgMLR_Type.__name__ = "Unsigned32"
_JnxmdiFlowAvgMLR_Object = MibTableColumn
jnxmdiFlowAvgMLR = _JnxmdiFlowAvgMLR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 15),
    _JnxmdiFlowAvgMLR_Type()
)
jnxmdiFlowAvgMLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowAvgMLR.setStatus("current")
_JnxmdiFlowAvgMRV_Type = DisplayString
_JnxmdiFlowAvgMRV_Object = MibTableColumn
jnxmdiFlowAvgMRV = _JnxmdiFlowAvgMRV_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 16),
    _JnxmdiFlowAvgMRV_Type()
)
jnxmdiFlowAvgMRV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowAvgMRV.setStatus("current")
_JnxmdiFlowTemplateName_Type = DisplayString
_JnxmdiFlowTemplateName_Object = MibTableColumn
jnxmdiFlowTemplateName = _JnxmdiFlowTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 17),
    _JnxmdiFlowTemplateName_Type()
)
jnxmdiFlowTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowTemplateName.setStatus("current")


class _JnxmdiFlowMDIRecCount_Type(Integer32):
    """Custom type jnxmdiFlowMDIRecCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxmdiFlowMDIRecCount_Type.__name__ = "Integer32"
_JnxmdiFlowMDIRecCount_Object = MibTableColumn
jnxmdiFlowMDIRecCount = _JnxmdiFlowMDIRecCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 18),
    _JnxmdiFlowMDIRecCount_Type()
)
jnxmdiFlowMDIRecCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowMDIRecCount.setStatus("current")


class _JnxmdiFlowPIDCount_Type(Integer32):
    """Custom type jnxmdiFlowPIDCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxmdiFlowPIDCount_Type.__name__ = "Integer32"
_JnxmdiFlowPIDCount_Object = MibTableColumn
jnxmdiFlowPIDCount = _JnxmdiFlowPIDCount_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 19),
    _JnxmdiFlowPIDCount_Type()
)
jnxmdiFlowPIDCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowPIDCount.setStatus("current")
_JnxmdiFlowMPLSLabel0_Type = Unsigned32
_JnxmdiFlowMPLSLabel0_Object = MibTableColumn
jnxmdiFlowMPLSLabel0 = _JnxmdiFlowMPLSLabel0_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 20),
    _JnxmdiFlowMPLSLabel0_Type()
)
jnxmdiFlowMPLSLabel0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowMPLSLabel0.setStatus("current")
_JnxmdiFlowMPLSLabel1_Type = Unsigned32
_JnxmdiFlowMPLSLabel1_Object = MibTableColumn
jnxmdiFlowMPLSLabel1 = _JnxmdiFlowMPLSLabel1_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 21),
    _JnxmdiFlowMPLSLabel1_Type()
)
jnxmdiFlowMPLSLabel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowMPLSLabel1.setStatus("current")
_JnxmdiFlowMPLSLabel2_Type = Unsigned32
_JnxmdiFlowMPLSLabel2_Object = MibTableColumn
jnxmdiFlowMPLSLabel2 = _JnxmdiFlowMPLSLabel2_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 3, 1, 22),
    _JnxmdiFlowMPLSLabel2_Type()
)
jnxmdiFlowMPLSLabel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowMPLSLabel2.setStatus("current")
_JnxmdiFlowMDIRecTable_Object = MibTable
jnxmdiFlowMDIRecTable = _JnxmdiFlowMDIRecTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 4)
)
if mibBuilder.loadTexts:
    jnxmdiFlowMDIRecTable.setStatus("current")
_JnxmdiFlowMDIRecEntry_Object = MibTableRow
jnxmdiFlowMDIRecEntry = _JnxmdiFlowMDIRecEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 4, 1)
)
jnxmdiFlowMDIRecEntry.setIndexNames(
    (0, "JUNIPER-VMON-MIB", "jnxmdiFPCSlotNo"),
    (0, "JUNIPER-VMON-MIB", "jnxmdiFlowIdentifier"),
    (0, "JUNIPER-VMON-MIB", "jnxmdiFlowMDIRecIndex"),
)
if mibBuilder.loadTexts:
    jnxmdiFlowMDIRecEntry.setStatus("current")


class _JnxmdiFlowMDIRecIndex_Type(Unsigned32):
    """Custom type jnxmdiFlowMDIRecIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxmdiFlowMDIRecIndex_Type.__name__ = "Unsigned32"
_JnxmdiFlowMDIRecIndex_Object = MibTableColumn
jnxmdiFlowMDIRecIndex = _JnxmdiFlowMDIRecIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 4, 1, 1),
    _JnxmdiFlowMDIRecIndex_Type()
)
jnxmdiFlowMDIRecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxmdiFlowMDIRecIndex.setStatus("current")
_JnxmdiFlowMDIRecDF_Type = DisplayString
_JnxmdiFlowMDIRecDF_Object = MibTableColumn
jnxmdiFlowMDIRecDF = _JnxmdiFlowMDIRecDF_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 4, 1, 2),
    _JnxmdiFlowMDIRecDF_Type()
)
jnxmdiFlowMDIRecDF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowMDIRecDF.setStatus("current")


class _JnxmdiFlowMDIRecMLR_Type(Unsigned32):
    """Custom type jnxmdiFlowMDIRecMLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxmdiFlowMDIRecMLR_Type.__name__ = "Unsigned32"
_JnxmdiFlowMDIRecMLR_Object = MibTableColumn
jnxmdiFlowMDIRecMLR = _JnxmdiFlowMDIRecMLR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 4, 1, 3),
    _JnxmdiFlowMDIRecMLR_Type()
)
jnxmdiFlowMDIRecMLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowMDIRecMLR.setStatus("current")
_JnxmdiFlowMDIRecMRV_Type = DisplayString
_JnxmdiFlowMDIRecMRV_Object = MibTableColumn
jnxmdiFlowMDIRecMRV = _JnxmdiFlowMDIRecMRV_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 4, 1, 4),
    _JnxmdiFlowMDIRecMRV_Type()
)
jnxmdiFlowMDIRecMRV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowMDIRecMRV.setStatus("current")
_JnxmdiFlowPIDTable_Object = MibTable
jnxmdiFlowPIDTable = _JnxmdiFlowPIDTable_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 5)
)
if mibBuilder.loadTexts:
    jnxmdiFlowPIDTable.setStatus("current")
_JnxmdiFlowPIDEntry_Object = MibTableRow
jnxmdiFlowPIDEntry = _JnxmdiFlowPIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 5, 1)
)
jnxmdiFlowPIDEntry.setIndexNames(
    (0, "JUNIPER-VMON-MIB", "jnxmdiFPCSlotNo"),
    (0, "JUNIPER-VMON-MIB", "jnxmdiFlowIdentifier"),
    (0, "JUNIPER-VMON-MIB", "jnxmdiFlowMDIRecIndex"),
    (0, "JUNIPER-VMON-MIB", "jnxmdiFlowPIDValue"),
)
if mibBuilder.loadTexts:
    jnxmdiFlowPIDEntry.setStatus("current")


class _JnxmdiFlowPIDValue_Type(Unsigned32):
    """Custom type jnxmdiFlowPIDValue based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxmdiFlowPIDValue_Type.__name__ = "Unsigned32"
_JnxmdiFlowPIDValue_Object = MibTableColumn
jnxmdiFlowPIDValue = _JnxmdiFlowPIDValue_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 5, 1, 1),
    _JnxmdiFlowPIDValue_Type()
)
jnxmdiFlowPIDValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    jnxmdiFlowPIDValue.setStatus("current")


class _JnxmdiFlowPIDMLR_Type(Unsigned32):
    """Custom type jnxmdiFlowPIDMLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_JnxmdiFlowPIDMLR_Type.__name__ = "Unsigned32"
_JnxmdiFlowPIDMLR_Object = MibTableColumn
jnxmdiFlowPIDMLR = _JnxmdiFlowPIDMLR_Object(
    (1, 3, 6, 1, 4, 1, 2636, 2, 1, 5, 1, 2),
    _JnxmdiFlowPIDMLR_Type()
)
jnxmdiFlowPIDMLR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxmdiFlowPIDMLR.setStatus("current")
_JnxVmonNotifications_ObjectIdentity = ObjectIdentity
jnxVmonNotifications = _JnxVmonNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 0)
)
_JnxVmonObjects_ObjectIdentity = ObjectIdentity
jnxVmonObjects = _JnxVmonObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1)
)
_JnxVmonFlowIdentifier_Type = Unsigned32
_JnxVmonFlowIdentifier_Object = MibScalar
jnxVmonFlowIdentifier = _JnxVmonFlowIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 1),
    _JnxVmonFlowIdentifier_Type()
)
jnxVmonFlowIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonFlowIdentifier.setStatus("current")
_JnxVmonSourceIP_Type = InetAddress
_JnxVmonSourceIP_Object = MibScalar
jnxVmonSourceIP = _JnxVmonSourceIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 2),
    _JnxVmonSourceIP_Type()
)
jnxVmonSourceIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonSourceIP.setStatus("current")
_JnxVmonDestinationIP_Type = InetAddress
_JnxVmonDestinationIP_Object = MibScalar
jnxVmonDestinationIP = _JnxVmonDestinationIP_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 3),
    _JnxVmonDestinationIP_Type()
)
jnxVmonDestinationIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonDestinationIP.setStatus("current")
_JnxVmonIPFamily_Type = InetAddressType
_JnxVmonIPFamily_Object = MibScalar
jnxVmonIPFamily = _JnxVmonIPFamily_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 4),
    _JnxVmonIPFamily_Type()
)
jnxVmonIPFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonIPFamily.setStatus("current")
_JnxVmonSourcePort_Type = InetPortNumber
_JnxVmonSourcePort_Object = MibScalar
jnxVmonSourcePort = _JnxVmonSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 5),
    _JnxVmonSourcePort_Type()
)
jnxVmonSourcePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonSourcePort.setStatus("current")
_JnxVmonDestinationPort_Type = InetPortNumber
_JnxVmonDestinationPort_Object = MibScalar
jnxVmonDestinationPort = _JnxVmonDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 6),
    _JnxVmonDestinationPort_Type()
)
jnxVmonDestinationPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonDestinationPort.setStatus("current")
_JnxVmonFlowType_Type = JnxVmonFlowType
_JnxVmonFlowType_Object = MibScalar
jnxVmonFlowType = _JnxVmonFlowType_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 7),
    _JnxVmonFlowType_Type()
)
jnxVmonFlowType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonFlowType.setStatus("current")
_JnxVmonTrapLevel_Type = JnxVmonTrapLevel
_JnxVmonTrapLevel_Object = MibScalar
jnxVmonTrapLevel = _JnxVmonTrapLevel_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 8),
    _JnxVmonTrapLevel_Type()
)
jnxVmonTrapLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonTrapLevel.setStatus("current")


class _JnxVmonFPCSlot_Type(Integer32):
    """Custom type jnxVmonFPCSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_JnxVmonFPCSlot_Type.__name__ = "Integer32"
_JnxVmonFPCSlot_Object = MibScalar
jnxVmonFPCSlot = _JnxVmonFPCSlot_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 9),
    _JnxVmonFPCSlot_Type()
)
jnxVmonFPCSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonFPCSlot.setStatus("current")
_JnxVmonInterfaceName_Type = DisplayString
_JnxVmonInterfaceName_Object = MibScalar
jnxVmonInterfaceName = _JnxVmonInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 10),
    _JnxVmonInterfaceName_Type()
)
jnxVmonInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonInterfaceName.setStatus("current")
_JnxVmonInterfaceSNMPIndex_Type = InterfaceIndexOrZero
_JnxVmonInterfaceSNMPIndex_Object = MibScalar
jnxVmonInterfaceSNMPIndex = _JnxVmonInterfaceSNMPIndex_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 11),
    _JnxVmonInterfaceSNMPIndex_Type()
)
jnxVmonInterfaceSNMPIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonInterfaceSNMPIndex.setStatus("current")
_JnxVmonTemplateName_Type = DisplayString
_JnxVmonTemplateName_Object = MibScalar
jnxVmonTemplateName = _JnxVmonTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 12),
    _JnxVmonTemplateName_Type()
)
jnxVmonTemplateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonTemplateName.setStatus("current")
_JnxVmonFlowDirection_Type = JnxVmonFlowDirection
_JnxVmonFlowDirection_Object = MibScalar
jnxVmonFlowDirection = _JnxVmonFlowDirection_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 13),
    _JnxVmonFlowDirection_Type()
)
jnxVmonFlowDirection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonFlowDirection.setStatus("current")
_JnxVmonExpectedVal_Type = DisplayString
_JnxVmonExpectedVal_Object = MibScalar
jnxVmonExpectedVal = _JnxVmonExpectedVal_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 14),
    _JnxVmonExpectedVal_Type()
)
jnxVmonExpectedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonExpectedVal.setStatus("current")
_JnxVmonComputedVal_Type = DisplayString
_JnxVmonComputedVal_Object = MibScalar
jnxVmonComputedVal = _JnxVmonComputedVal_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 15),
    _JnxVmonComputedVal_Type()
)
jnxVmonComputedVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonComputedVal.setStatus("current")


class _JnxVmonMDIRecIdx_Type(Unsigned32):
    """Custom type jnxVmonMDIRecIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_JnxVmonMDIRecIdx_Type.__name__ = "Unsigned32"
_JnxVmonMDIRecIdx_Object = MibScalar
jnxVmonMDIRecIdx = _JnxVmonMDIRecIdx_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 16),
    _JnxVmonMDIRecIdx_Type()
)
jnxVmonMDIRecIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonMDIRecIdx.setStatus("current")


class _JnxVmonAlarmMode_Type(Unsigned32):
    """Custom type jnxVmonAlarmMode based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_JnxVmonAlarmMode_Type.__name__ = "Unsigned32"
_JnxVmonAlarmMode_Object = MibScalar
jnxVmonAlarmMode = _JnxVmonAlarmMode_Object(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 1, 17),
    _JnxVmonAlarmMode_Type()
)
jnxVmonAlarmMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    jnxVmonAlarmMode.setStatus("current")

# Managed Objects groups


# Notification objects

jnxVmonMDIDFAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 0, 1)
)
jnxVmonMDIDFAlarm.setObjects(
      *(("JUNIPER-VMON-MIB", "jnxVmonFlowIdentifier"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourceIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonIPFamily"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourcePort"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationPort"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowType"),
        ("JUNIPER-VMON-MIB", "jnxVmonTrapLevel"),
        ("JUNIPER-VMON-MIB", "jnxVmonFPCSlot"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceName"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceSNMPIndex"),
        ("JUNIPER-VMON-MIB", "jnxVmonTemplateName"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowDirection"),
        ("JUNIPER-VMON-MIB", "jnxVmonExpectedVal"),
        ("JUNIPER-VMON-MIB", "jnxVmonComputedVal"),
        ("JUNIPER-VMON-MIB", "jnxVmonMDIRecIdx"),
        ("JUNIPER-VMON-MIB", "jnxVmonAlarmMode"))
)
if mibBuilder.loadTexts:
    jnxVmonMDIDFAlarm.setStatus(
        "current"
    )

jnxVmonMDIMLRAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 0, 2)
)
jnxVmonMDIMLRAlarm.setObjects(
      *(("JUNIPER-VMON-MIB", "jnxVmonFlowIdentifier"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourceIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonIPFamily"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourcePort"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationPort"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowType"),
        ("JUNIPER-VMON-MIB", "jnxVmonTrapLevel"),
        ("JUNIPER-VMON-MIB", "jnxVmonFPCSlot"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceName"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceSNMPIndex"),
        ("JUNIPER-VMON-MIB", "jnxVmonTemplateName"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowDirection"),
        ("JUNIPER-VMON-MIB", "jnxVmonExpectedVal"),
        ("JUNIPER-VMON-MIB", "jnxVmonComputedVal"),
        ("JUNIPER-VMON-MIB", "jnxVmonMDIRecIdx"),
        ("JUNIPER-VMON-MIB", "jnxVmonAlarmMode"))
)
if mibBuilder.loadTexts:
    jnxVmonMDIMLRAlarm.setStatus(
        "current"
    )

jnxVmonMDIMRVAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 0, 3)
)
jnxVmonMDIMRVAlarm.setObjects(
      *(("JUNIPER-VMON-MIB", "jnxVmonFlowIdentifier"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourceIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonIPFamily"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourcePort"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationPort"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowType"),
        ("JUNIPER-VMON-MIB", "jnxVmonTrapLevel"),
        ("JUNIPER-VMON-MIB", "jnxVmonFPCSlot"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceName"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceSNMPIndex"),
        ("JUNIPER-VMON-MIB", "jnxVmonTemplateName"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowDirection"),
        ("JUNIPER-VMON-MIB", "jnxVmonExpectedVal"),
        ("JUNIPER-VMON-MIB", "jnxVmonComputedVal"),
        ("JUNIPER-VMON-MIB", "jnxVmonMDIRecIdx"),
        ("JUNIPER-VMON-MIB", "jnxVmonAlarmMode"))
)
if mibBuilder.loadTexts:
    jnxVmonMDIMRVAlarm.setStatus(
        "current"
    )

jnxVmonMDIFlowInsertAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 0, 4)
)
jnxVmonMDIFlowInsertAlarm.setObjects(
      *(("JUNIPER-VMON-MIB", "jnxVmonFlowIdentifier"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourceIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonIPFamily"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourcePort"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationPort"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowType"),
        ("JUNIPER-VMON-MIB", "jnxVmonFPCSlot"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceName"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceSNMPIndex"),
        ("JUNIPER-VMON-MIB", "jnxVmonTemplateName"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowDirection"))
)
if mibBuilder.loadTexts:
    jnxVmonMDIFlowInsertAlarm.setStatus(
        "current"
    )

jnxVmonMDIFlowDeleteAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 2636, 3, 79, 1, 0, 5)
)
jnxVmonMDIFlowDeleteAlarm.setObjects(
      *(("JUNIPER-VMON-MIB", "jnxVmonFlowIdentifier"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourceIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationIP"),
        ("JUNIPER-VMON-MIB", "jnxVmonIPFamily"),
        ("JUNIPER-VMON-MIB", "jnxVmonSourcePort"),
        ("JUNIPER-VMON-MIB", "jnxVmonDestinationPort"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowType"),
        ("JUNIPER-VMON-MIB", "jnxVmonFPCSlot"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceName"),
        ("JUNIPER-VMON-MIB", "jnxVmonInterfaceSNMPIndex"),
        ("JUNIPER-VMON-MIB", "jnxVmonTemplateName"),
        ("JUNIPER-VMON-MIB", "jnxVmonFlowDirection"))
)
if mibBuilder.loadTexts:
    jnxVmonMDIFlowDeleteAlarm.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "JUNIPER-VMON-MIB",
    **{"JnxVmonFlowType": JnxVmonFlowType,
       "JnxVmonTrapLevel": JnxVmonTrapLevel,
       "JnxVmonFlowDirection": JnxVmonFlowDirection,
       "jnxVmonServices": jnxVmonServices,
       "jnxmdiStatsTable": jnxmdiStatsTable,
       "jnxmdiStatsEntry": jnxmdiStatsEntry,
       "jnxmdiFPCSlotNo": jnxmdiFPCSlotNo,
       "jnxmdiActiveFlowsCount": jnxmdiActiveFlowsCount,
       "jnxmdiInsertedFlowsCount": jnxmdiInsertedFlowsCount,
       "jnxmdiDeletedFlowsCount": jnxmdiDeletedFlowsCount,
       "jnxmdiTotalPktsCount": jnxmdiTotalPktsCount,
       "jnxmdiTotalBytesCount": jnxmdiTotalBytesCount,
       "jnxmdiDFTotalAlarmCount": jnxmdiDFTotalAlarmCount,
       "jnxmdiDFInfoAlarmCount": jnxmdiDFInfoAlarmCount,
       "jnxmdiDFWarningAlarmCount": jnxmdiDFWarningAlarmCount,
       "jnxmdiDFCriticalAlarmCount": jnxmdiDFCriticalAlarmCount,
       "jnxmdiMLRTotalAlarmCount": jnxmdiMLRTotalAlarmCount,
       "jnxmdiMLRInfoAlarmCount": jnxmdiMLRInfoAlarmCount,
       "jnxmdiMLRWarningAlarmCount": jnxmdiMLRWarningAlarmCount,
       "jnxmdiMLRCriticalAlarmCount": jnxmdiMLRCriticalAlarmCount,
       "jnxmdiMRVTotalAlarmCount": jnxmdiMRVTotalAlarmCount,
       "jnxmdiMRVInfoAlarmCount": jnxmdiMRVInfoAlarmCount,
       "jnxmdiMRVWarningAlarmCount": jnxmdiMRVWarningAlarmCount,
       "jnxmdiMRVCriticalAlarmCount": jnxmdiMRVCriticalAlarmCount,
       "jnxmdiErrsTable": jnxmdiErrsTable,
       "jnxmdiErrsEntry": jnxmdiErrsEntry,
       "jnxmdiErrsFlowInsertErr": jnxmdiErrsFlowInsertErr,
       "jnxmdiErrsPolicerDrop": jnxmdiErrsPolicerDrop,
       "jnxmdiErrsPIDLimitExceed": jnxmdiErrsPIDLimitExceed,
       "jnxmdiErrsUnsupportedMediaPkts": jnxmdiErrsUnsupportedMediaPkts,
       "jnxmdiErrsFragmentedPkts": jnxmdiErrsFragmentedPkts,
       "jnxmdiErrsMaxLabelsExceed": jnxmdiErrsMaxLabelsExceed,
       "jnxmdiErrsOptionPkt": jnxmdiErrsOptionPkt,
       "jnxmdiFlowTable": jnxmdiFlowTable,
       "jnxmdiFlowEntry": jnxmdiFlowEntry,
       "jnxmdiFlowIdentifier": jnxmdiFlowIdentifier,
       "jnxmdiFlowSrcAddr": jnxmdiFlowSrcAddr,
       "jnxmdiFlowDstAddr": jnxmdiFlowDstAddr,
       "jnxmdiFlowAddrFamily": jnxmdiFlowAddrFamily,
       "jnxmdiFlowSrcPort": jnxmdiFlowSrcPort,
       "jnxmdiFlowDstPort": jnxmdiFlowDstPort,
       "jnxmdiFlowInterfaceName": jnxmdiFlowInterfaceName,
       "jnxmdiFlowInterfaceSNMPIndex": jnxmdiFlowInterfaceSNMPIndex,
       "jnxmdiFlowDirection": jnxmdiFlowDirection,
       "jnxmdiFlowType": jnxmdiFlowType,
       "jnxmdiFlowLastDF": jnxmdiFlowLastDF,
       "jnxmdiFlowLastMLR": jnxmdiFlowLastMLR,
       "jnxmdiFlowLastMRV": jnxmdiFlowLastMRV,
       "jnxmdiFlowAvgDF": jnxmdiFlowAvgDF,
       "jnxmdiFlowAvgMLR": jnxmdiFlowAvgMLR,
       "jnxmdiFlowAvgMRV": jnxmdiFlowAvgMRV,
       "jnxmdiFlowTemplateName": jnxmdiFlowTemplateName,
       "jnxmdiFlowMDIRecCount": jnxmdiFlowMDIRecCount,
       "jnxmdiFlowPIDCount": jnxmdiFlowPIDCount,
       "jnxmdiFlowMPLSLabel0": jnxmdiFlowMPLSLabel0,
       "jnxmdiFlowMPLSLabel1": jnxmdiFlowMPLSLabel1,
       "jnxmdiFlowMPLSLabel2": jnxmdiFlowMPLSLabel2,
       "jnxmdiFlowMDIRecTable": jnxmdiFlowMDIRecTable,
       "jnxmdiFlowMDIRecEntry": jnxmdiFlowMDIRecEntry,
       "jnxmdiFlowMDIRecIndex": jnxmdiFlowMDIRecIndex,
       "jnxmdiFlowMDIRecDF": jnxmdiFlowMDIRecDF,
       "jnxmdiFlowMDIRecMLR": jnxmdiFlowMDIRecMLR,
       "jnxmdiFlowMDIRecMRV": jnxmdiFlowMDIRecMRV,
       "jnxmdiFlowPIDTable": jnxmdiFlowPIDTable,
       "jnxmdiFlowPIDEntry": jnxmdiFlowPIDEntry,
       "jnxmdiFlowPIDValue": jnxmdiFlowPIDValue,
       "jnxmdiFlowPIDMLR": jnxmdiFlowPIDMLR,
       "jnxVmonMIB": jnxVmonMIB,
       "jnxVmonNotifications": jnxVmonNotifications,
       "jnxVmonMDIDFAlarm": jnxVmonMDIDFAlarm,
       "jnxVmonMDIMLRAlarm": jnxVmonMDIMLRAlarm,
       "jnxVmonMDIMRVAlarm": jnxVmonMDIMRVAlarm,
       "jnxVmonMDIFlowInsertAlarm": jnxVmonMDIFlowInsertAlarm,
       "jnxVmonMDIFlowDeleteAlarm": jnxVmonMDIFlowDeleteAlarm,
       "jnxVmonObjects": jnxVmonObjects,
       "jnxVmonFlowIdentifier": jnxVmonFlowIdentifier,
       "jnxVmonSourceIP": jnxVmonSourceIP,
       "jnxVmonDestinationIP": jnxVmonDestinationIP,
       "jnxVmonIPFamily": jnxVmonIPFamily,
       "jnxVmonSourcePort": jnxVmonSourcePort,
       "jnxVmonDestinationPort": jnxVmonDestinationPort,
       "jnxVmonFlowType": jnxVmonFlowType,
       "jnxVmonTrapLevel": jnxVmonTrapLevel,
       "jnxVmonFPCSlot": jnxVmonFPCSlot,
       "jnxVmonInterfaceName": jnxVmonInterfaceName,
       "jnxVmonInterfaceSNMPIndex": jnxVmonInterfaceSNMPIndex,
       "jnxVmonTemplateName": jnxVmonTemplateName,
       "jnxVmonFlowDirection": jnxVmonFlowDirection,
       "jnxVmonExpectedVal": jnxVmonExpectedVal,
       "jnxVmonComputedVal": jnxVmonComputedVal,
       "jnxVmonMDIRecIdx": jnxVmonMDIRecIdx,
       "jnxVmonAlarmMode": jnxVmonAlarmMode}
)
