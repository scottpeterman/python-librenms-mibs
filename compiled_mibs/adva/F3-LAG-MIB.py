# SNMP MIB module (F3-LAG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-LAG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:04 2025
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

(fsp150cm,) = mibBuilder.importSymbols(
    "ADVA-MIB",
    "fsp150cm")

(CmPmBinAction,) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "CmPmBinAction")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3LagMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14)
)
if mibBuilder.loadTexts:
    f3LagMIB.setRevisions(
        ("2016-04-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AggMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active-standby", 1),
          ("loadsharing", 2))
    )



class AggPortState(TextualConvention, Integer32):
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
          ("standby", 2))
    )



class LagFrameDistributionAlgorithmType(TextualConvention, Integer32):
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
        *(("activeStandby", 1),
          ("srcdstMacHash", 2),
          ("serviceAssignment", 3))
    )



class LinkAssignMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("provisionedLinkList", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F3LagObjects_ObjectIdentity = ObjectIdentity
f3LagObjects = _F3LagObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1)
)
_F3LagTable_Object = MibTable
f3LagTable = _F3LagTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1)
)
if mibBuilder.loadTexts:
    f3LagTable.setStatus("current")
_F3LagEntry_Object = MibTableRow
f3LagEntry = _F3LagEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1)
)
f3LagEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-LAG-MIB", "f3LagIndex"),
)
if mibBuilder.loadTexts:
    f3LagEntry.setStatus("current")
_F3LagIndex_Type = Integer32
_F3LagIndex_Object = MibTableColumn
f3LagIndex = _F3LagIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 1),
    _F3LagIndex_Type()
)
f3LagIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3LagIndex.setStatus("current")
_F3LagIfIndex_Type = InterfaceIndex
_F3LagIfIndex_Object = MibTableColumn
f3LagIfIndex = _F3LagIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 2),
    _F3LagIfIndex_Type()
)
f3LagIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagIfIndex.setStatus("current")


class _F3LagName_Type(DisplayString):
    """Custom type f3LagName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_F3LagName_Type.__name__ = "DisplayString"
_F3LagName_Object = MibTableColumn
f3LagName = _F3LagName_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 3),
    _F3LagName_Type()
)
f3LagName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagName.setStatus("current")
_F3LagProtocols_Type = TruthValue
_F3LagProtocols_Object = MibTableColumn
f3LagProtocols = _F3LagProtocols_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 4),
    _F3LagProtocols_Type()
)
f3LagProtocols.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagProtocols.setStatus("current")
_F3LagLacpControl_Type = TruthValue
_F3LagLacpControl_Object = MibTableColumn
f3LagLacpControl = _F3LagLacpControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 5),
    _F3LagLacpControl_Type()
)
f3LagLacpControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagLacpControl.setStatus("current")
_F3LagMode_Type = AggMode
_F3LagMode_Object = MibTableColumn
f3LagMode = _F3LagMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 6),
    _F3LagMode_Type()
)
f3LagMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagMode.setStatus("current")
_F3LagCcmDefectsDetectionEnabled_Type = TruthValue
_F3LagCcmDefectsDetectionEnabled_Object = MibTableColumn
f3LagCcmDefectsDetectionEnabled = _F3LagCcmDefectsDetectionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 7),
    _F3LagCcmDefectsDetectionEnabled_Type()
)
f3LagCcmDefectsDetectionEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagCcmDefectsDetectionEnabled.setStatus("current")
_F3LagStatsAction_Type = CmPmBinAction
_F3LagStatsAction_Object = MibTableColumn
f3LagStatsAction = _F3LagStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 8),
    _F3LagStatsAction_Type()
)
f3LagStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagStatsAction.setStatus("current")
_F3LagStorageType_Type = StorageType
_F3LagStorageType_Object = MibTableColumn
f3LagStorageType = _F3LagStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 9),
    _F3LagStorageType_Type()
)
f3LagStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3LagStorageType.setStatus("current")
_F3LagRowStatus_Type = RowStatus
_F3LagRowStatus_Object = MibTableColumn
f3LagRowStatus = _F3LagRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 10),
    _F3LagRowStatus_Type()
)
f3LagRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3LagRowStatus.setStatus("current")
_F3LagIgnorePartnerColMaxDelay_Type = TruthValue
_F3LagIgnorePartnerColMaxDelay_Object = MibTableColumn
f3LagIgnorePartnerColMaxDelay = _F3LagIgnorePartnerColMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 11),
    _F3LagIgnorePartnerColMaxDelay_Type()
)
f3LagIgnorePartnerColMaxDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3LagIgnorePartnerColMaxDelay.setStatus("current")
_F3LagFrameDistAlgorithm_Type = LagFrameDistributionAlgorithmType
_F3LagFrameDistAlgorithm_Object = MibTableColumn
f3LagFrameDistAlgorithm = _F3LagFrameDistAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 12),
    _F3LagFrameDistAlgorithm_Type()
)
f3LagFrameDistAlgorithm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagFrameDistAlgorithm.setStatus("current")
_F3LagDiscardWrongConversation_Type = TruthValue
_F3LagDiscardWrongConversation_Object = MibTableColumn
f3LagDiscardWrongConversation = _F3LagDiscardWrongConversation_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 1, 1, 13),
    _F3LagDiscardWrongConversation_Type()
)
f3LagDiscardWrongConversation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagDiscardWrongConversation.setStatus("current")
_F3LagStatsTable_Object = MibTable
f3LagStatsTable = _F3LagStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2)
)
if mibBuilder.loadTexts:
    f3LagStatsTable.setStatus("current")
_F3LagStatsEntry_Object = MibTableRow
f3LagStatsEntry = _F3LagStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1)
)
f3LagStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-LAG-MIB", "f3LagIndex"),
    (0, "F3-LAG-MIB", "f3LagStatsIndex"),
)
if mibBuilder.loadTexts:
    f3LagStatsEntry.setStatus("current")
_F3LagStatsIndex_Type = Integer32
_F3LagStatsIndex_Object = MibTableColumn
f3LagStatsIndex = _F3LagStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 1),
    _F3LagStatsIndex_Type()
)
f3LagStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3LagStatsIndex.setStatus("current")
_F3LagStatsOctetsTxOK_Type = Counter32
_F3LagStatsOctetsTxOK_Object = MibTableColumn
f3LagStatsOctetsTxOK = _F3LagStatsOctetsTxOK_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 2),
    _F3LagStatsOctetsTxOK_Type()
)
f3LagStatsOctetsTxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsOctetsTxOK.setStatus("current")
_F3LagStatsOctetsRxOK_Type = Counter32
_F3LagStatsOctetsRxOK_Object = MibTableColumn
f3LagStatsOctetsRxOK = _F3LagStatsOctetsRxOK_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 3),
    _F3LagStatsOctetsRxOK_Type()
)
f3LagStatsOctetsRxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsOctetsRxOK.setStatus("current")
_F3LagStatsFramesTxOK_Type = Counter32
_F3LagStatsFramesTxOK_Object = MibTableColumn
f3LagStatsFramesTxOK = _F3LagStatsFramesTxOK_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 4),
    _F3LagStatsFramesTxOK_Type()
)
f3LagStatsFramesTxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsFramesTxOK.setStatus("current")
_F3LagStatsFramesRxOK_Type = Counter32
_F3LagStatsFramesRxOK_Object = MibTableColumn
f3LagStatsFramesRxOK = _F3LagStatsFramesRxOK_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 5),
    _F3LagStatsFramesRxOK_Type()
)
f3LagStatsFramesRxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsFramesRxOK.setStatus("current")
_F3LagStatsMulticastFramesTxOK_Type = Counter32
_F3LagStatsMulticastFramesTxOK_Object = MibTableColumn
f3LagStatsMulticastFramesTxOK = _F3LagStatsMulticastFramesTxOK_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 6),
    _F3LagStatsMulticastFramesTxOK_Type()
)
f3LagStatsMulticastFramesTxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsMulticastFramesTxOK.setStatus("current")
_F3LagStatsMulticastFramesRxOK_Type = Counter32
_F3LagStatsMulticastFramesRxOK_Object = MibTableColumn
f3LagStatsMulticastFramesRxOK = _F3LagStatsMulticastFramesRxOK_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 7),
    _F3LagStatsMulticastFramesRxOK_Type()
)
f3LagStatsMulticastFramesRxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsMulticastFramesRxOK.setStatus("current")
_F3LagStatsBroadcastFramesTxOK_Type = Counter32
_F3LagStatsBroadcastFramesTxOK_Object = MibTableColumn
f3LagStatsBroadcastFramesTxOK = _F3LagStatsBroadcastFramesTxOK_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 8),
    _F3LagStatsBroadcastFramesTxOK_Type()
)
f3LagStatsBroadcastFramesTxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsBroadcastFramesTxOK.setStatus("current")
_F3LagStatsBroadcastFramesRxOK_Type = Counter32
_F3LagStatsBroadcastFramesRxOK_Object = MibTableColumn
f3LagStatsBroadcastFramesRxOK = _F3LagStatsBroadcastFramesRxOK_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 9),
    _F3LagStatsBroadcastFramesRxOK_Type()
)
f3LagStatsBroadcastFramesRxOK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsBroadcastFramesRxOK.setStatus("current")
_F3LagStatsFramesWithTxErrors_Type = Counter32
_F3LagStatsFramesWithTxErrors_Object = MibTableColumn
f3LagStatsFramesWithTxErrors = _F3LagStatsFramesWithTxErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 10),
    _F3LagStatsFramesWithTxErrors_Type()
)
f3LagStatsFramesWithTxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsFramesWithTxErrors.setStatus("current")
_F3LagStatsFramesWithRxErrors_Type = Counter32
_F3LagStatsFramesWithRxErrors_Object = MibTableColumn
f3LagStatsFramesWithRxErrors = _F3LagStatsFramesWithRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 11),
    _F3LagStatsFramesWithRxErrors_Type()
)
f3LagStatsFramesWithRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsFramesWithRxErrors.setStatus("current")
_F3LagStatsUnknownProtocolFrames_Type = Counter32
_F3LagStatsUnknownProtocolFrames_Object = MibTableColumn
f3LagStatsUnknownProtocolFrames = _F3LagStatsUnknownProtocolFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 2, 1, 12),
    _F3LagStatsUnknownProtocolFrames_Type()
)
f3LagStatsUnknownProtocolFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagStatsUnknownProtocolFrames.setStatus("current")
_F3LagPortTable_Object = MibTable
f3LagPortTable = _F3LagPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3)
)
if mibBuilder.loadTexts:
    f3LagPortTable.setStatus("current")
_F3LagPortEntry_Object = MibTableRow
f3LagPortEntry = _F3LagPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1)
)
f3LagPortEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-LAG-MIB", "f3LagIndex"),
    (0, "F3-LAG-MIB", "f3LagPortIndex"),
)
if mibBuilder.loadTexts:
    f3LagPortEntry.setStatus("current")
_F3LagPortIndex_Type = Integer32
_F3LagPortIndex_Object = MibTableColumn
f3LagPortIndex = _F3LagPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 1),
    _F3LagPortIndex_Type()
)
f3LagPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3LagPortIndex.setStatus("current")
_F3LagPortMember_Type = VariablePointer
_F3LagPortMember_Object = MibTableColumn
f3LagPortMember = _F3LagPortMember_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 2),
    _F3LagPortMember_Type()
)
f3LagPortMember.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3LagPortMember.setStatus("current")
_F3LagPortLacpForceOutOfSync_Type = TruthValue
_F3LagPortLacpForceOutOfSync_Object = MibTableColumn
f3LagPortLacpForceOutOfSync = _F3LagPortLacpForceOutOfSync_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 3),
    _F3LagPortLacpForceOutOfSync_Type()
)
f3LagPortLacpForceOutOfSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagPortLacpForceOutOfSync.setStatus("current")
_F3LagPortState_Type = AggPortState
_F3LagPortState_Object = MibTableColumn
f3LagPortState = _F3LagPortState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 4),
    _F3LagPortState_Type()
)
f3LagPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagPortState.setStatus("current")
_F3LagPortStatsAction_Type = CmPmBinAction
_F3LagPortStatsAction_Object = MibTableColumn
f3LagPortStatsAction = _F3LagPortStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 5),
    _F3LagPortStatsAction_Type()
)
f3LagPortStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagPortStatsAction.setStatus("current")
_F3LagPortStorageType_Type = StorageType
_F3LagPortStorageType_Object = MibTableColumn
f3LagPortStorageType = _F3LagPortStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 6),
    _F3LagPortStorageType_Type()
)
f3LagPortStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3LagPortStorageType.setStatus("current")
_F3LagPortRowStatus_Type = RowStatus
_F3LagPortRowStatus_Object = MibTableColumn
f3LagPortRowStatus = _F3LagPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 3, 1, 7),
    _F3LagPortRowStatus_Type()
)
f3LagPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3LagPortRowStatus.setStatus("current")
_F3LagServiceMapTable_Object = MibTable
f3LagServiceMapTable = _F3LagServiceMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4)
)
if mibBuilder.loadTexts:
    f3LagServiceMapTable.setStatus("current")
_F3LagServiceMapEntry_Object = MibTableRow
f3LagServiceMapEntry = _F3LagServiceMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1)
)
f3LagServiceMapEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "F3-LAG-MIB", "f3LagIndex"),
    (0, "F3-LAG-MIB", "f3LagServiceMapIndex"),
)
if mibBuilder.loadTexts:
    f3LagServiceMapEntry.setStatus("current")
_F3LagServiceMapIndex_Type = Integer32
_F3LagServiceMapIndex_Object = MibTableColumn
f3LagServiceMapIndex = _F3LagServiceMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 1),
    _F3LagServiceMapIndex_Type()
)
f3LagServiceMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3LagServiceMapIndex.setStatus("current")
_F3LagServiceMapServiceObj_Type = VariablePointer
_F3LagServiceMapServiceObj_Object = MibTableColumn
f3LagServiceMapServiceObj = _F3LagServiceMapServiceObj_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 2),
    _F3LagServiceMapServiceObj_Type()
)
f3LagServiceMapServiceObj.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3LagServiceMapServiceObj.setStatus("current")
_F3LagServiceMapLinkAssignMode_Type = LinkAssignMode
_F3LagServiceMapLinkAssignMode_Object = MibTableColumn
f3LagServiceMapLinkAssignMode = _F3LagServiceMapLinkAssignMode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 3),
    _F3LagServiceMapLinkAssignMode_Type()
)
f3LagServiceMapLinkAssignMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagServiceMapLinkAssignMode.setStatus("current")
_F3LagServiceMapStorageType_Type = StorageType
_F3LagServiceMapStorageType_Object = MibTableColumn
f3LagServiceMapStorageType = _F3LagServiceMapStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 4),
    _F3LagServiceMapStorageType_Type()
)
f3LagServiceMapStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3LagServiceMapStorageType.setStatus("current")
_F3LagServiceMapRowStatus_Type = RowStatus
_F3LagServiceMapRowStatus_Object = MibTableColumn
f3LagServiceMapRowStatus = _F3LagServiceMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 5),
    _F3LagServiceMapRowStatus_Type()
)
f3LagServiceMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    f3LagServiceMapRowStatus.setStatus("current")
_F3LagServiceMapMemberLinkList_Type = DisplayString
_F3LagServiceMapMemberLinkList_Object = MibTableColumn
f3LagServiceMapMemberLinkList = _F3LagServiceMapMemberLinkList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 6),
    _F3LagServiceMapMemberLinkList_Type()
)
f3LagServiceMapMemberLinkList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3LagServiceMapMemberLinkList.setStatus("current")
_F3LagServiceMapCurrentMemberLink_Type = Integer32
_F3LagServiceMapCurrentMemberLink_Object = MibTableColumn
f3LagServiceMapCurrentMemberLink = _F3LagServiceMapCurrentMemberLink_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 1, 4, 1, 7),
    _F3LagServiceMapCurrentMemberLink_Type()
)
f3LagServiceMapCurrentMemberLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3LagServiceMapCurrentMemberLink.setStatus("current")
_F3LagConformance_ObjectIdentity = ObjectIdentity
f3LagConformance = _F3LagConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2)
)
_F3LagCompliances_ObjectIdentity = ObjectIdentity
f3LagCompliances = _F3LagCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2, 1)
)
_F3LagGroups_ObjectIdentity = ObjectIdentity
f3LagGroups = _F3LagGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2, 2)
)

# Managed Objects groups

f3LagObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2, 2, 1)
)
f3LagObjectGroup.setObjects(
      *(("F3-LAG-MIB", "f3LagIndex"),
        ("F3-LAG-MIB", "f3LagIfIndex"),
        ("F3-LAG-MIB", "f3LagName"),
        ("F3-LAG-MIB", "f3LagProtocols"),
        ("F3-LAG-MIB", "f3LagLacpControl"),
        ("F3-LAG-MIB", "f3LagMode"),
        ("F3-LAG-MIB", "f3LagCcmDefectsDetectionEnabled"),
        ("F3-LAG-MIB", "f3LagStatsAction"),
        ("F3-LAG-MIB", "f3LagStorageType"),
        ("F3-LAG-MIB", "f3LagRowStatus"),
        ("F3-LAG-MIB", "f3LagIgnorePartnerColMaxDelay"),
        ("F3-LAG-MIB", "f3LagFrameDistAlgorithm"),
        ("F3-LAG-MIB", "f3LagDiscardWrongConversation"),
        ("F3-LAG-MIB", "f3LagStatsIndex"),
        ("F3-LAG-MIB", "f3LagStatsOctetsTxOK"),
        ("F3-LAG-MIB", "f3LagStatsOctetsRxOK"),
        ("F3-LAG-MIB", "f3LagStatsFramesTxOK"),
        ("F3-LAG-MIB", "f3LagStatsFramesRxOK"),
        ("F3-LAG-MIB", "f3LagStatsMulticastFramesTxOK"),
        ("F3-LAG-MIB", "f3LagStatsMulticastFramesRxOK"),
        ("F3-LAG-MIB", "f3LagStatsBroadcastFramesTxOK"),
        ("F3-LAG-MIB", "f3LagStatsBroadcastFramesRxOK"),
        ("F3-LAG-MIB", "f3LagStatsFramesWithTxErrors"),
        ("F3-LAG-MIB", "f3LagStatsFramesWithRxErrors"),
        ("F3-LAG-MIB", "f3LagStatsUnknownProtocolFrames"),
        ("F3-LAG-MIB", "f3LagPortIndex"),
        ("F3-LAG-MIB", "f3LagPortMember"),
        ("F3-LAG-MIB", "f3LagPortLacpForceOutOfSync"),
        ("F3-LAG-MIB", "f3LagPortState"),
        ("F3-LAG-MIB", "f3LagPortStatsAction"),
        ("F3-LAG-MIB", "f3LagPortStorageType"),
        ("F3-LAG-MIB", "f3LagPortRowStatus"),
        ("F3-LAG-MIB", "f3LagServiceMapIndex"),
        ("F3-LAG-MIB", "f3LagServiceMapServiceObj"),
        ("F3-LAG-MIB", "f3LagServiceMapLinkAssignMode"),
        ("F3-LAG-MIB", "f3LagServiceMapStorageType"),
        ("F3-LAG-MIB", "f3LagServiceMapRowStatus"),
        ("F3-LAG-MIB", "f3LagServiceMapMemberLinkList"),
        ("F3-LAG-MIB", "f3LagServiceMapCurrentMemberLink"))
)
if mibBuilder.loadTexts:
    f3LagObjectGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3LagCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 14, 2, 1, 1)
)
f3LagCompliance.setObjects(
    ("F3-LAG-MIB", "f3LagObjectGroup")
)
if mibBuilder.loadTexts:
    f3LagCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-LAG-MIB",
    **{"AggMode": AggMode,
       "AggPortState": AggPortState,
       "LagFrameDistributionAlgorithmType": LagFrameDistributionAlgorithmType,
       "LinkAssignMode": LinkAssignMode,
       "f3LagMIB": f3LagMIB,
       "f3LagObjects": f3LagObjects,
       "f3LagTable": f3LagTable,
       "f3LagEntry": f3LagEntry,
       "f3LagIndex": f3LagIndex,
       "f3LagIfIndex": f3LagIfIndex,
       "f3LagName": f3LagName,
       "f3LagProtocols": f3LagProtocols,
       "f3LagLacpControl": f3LagLacpControl,
       "f3LagMode": f3LagMode,
       "f3LagCcmDefectsDetectionEnabled": f3LagCcmDefectsDetectionEnabled,
       "f3LagStatsAction": f3LagStatsAction,
       "f3LagStorageType": f3LagStorageType,
       "f3LagRowStatus": f3LagRowStatus,
       "f3LagIgnorePartnerColMaxDelay": f3LagIgnorePartnerColMaxDelay,
       "f3LagFrameDistAlgorithm": f3LagFrameDistAlgorithm,
       "f3LagDiscardWrongConversation": f3LagDiscardWrongConversation,
       "f3LagStatsTable": f3LagStatsTable,
       "f3LagStatsEntry": f3LagStatsEntry,
       "f3LagStatsIndex": f3LagStatsIndex,
       "f3LagStatsOctetsTxOK": f3LagStatsOctetsTxOK,
       "f3LagStatsOctetsRxOK": f3LagStatsOctetsRxOK,
       "f3LagStatsFramesTxOK": f3LagStatsFramesTxOK,
       "f3LagStatsFramesRxOK": f3LagStatsFramesRxOK,
       "f3LagStatsMulticastFramesTxOK": f3LagStatsMulticastFramesTxOK,
       "f3LagStatsMulticastFramesRxOK": f3LagStatsMulticastFramesRxOK,
       "f3LagStatsBroadcastFramesTxOK": f3LagStatsBroadcastFramesTxOK,
       "f3LagStatsBroadcastFramesRxOK": f3LagStatsBroadcastFramesRxOK,
       "f3LagStatsFramesWithTxErrors": f3LagStatsFramesWithTxErrors,
       "f3LagStatsFramesWithRxErrors": f3LagStatsFramesWithRxErrors,
       "f3LagStatsUnknownProtocolFrames": f3LagStatsUnknownProtocolFrames,
       "f3LagPortTable": f3LagPortTable,
       "f3LagPortEntry": f3LagPortEntry,
       "f3LagPortIndex": f3LagPortIndex,
       "f3LagPortMember": f3LagPortMember,
       "f3LagPortLacpForceOutOfSync": f3LagPortLacpForceOutOfSync,
       "f3LagPortState": f3LagPortState,
       "f3LagPortStatsAction": f3LagPortStatsAction,
       "f3LagPortStorageType": f3LagPortStorageType,
       "f3LagPortRowStatus": f3LagPortRowStatus,
       "f3LagServiceMapTable": f3LagServiceMapTable,
       "f3LagServiceMapEntry": f3LagServiceMapEntry,
       "f3LagServiceMapIndex": f3LagServiceMapIndex,
       "f3LagServiceMapServiceObj": f3LagServiceMapServiceObj,
       "f3LagServiceMapLinkAssignMode": f3LagServiceMapLinkAssignMode,
       "f3LagServiceMapStorageType": f3LagServiceMapStorageType,
       "f3LagServiceMapRowStatus": f3LagServiceMapRowStatus,
       "f3LagServiceMapMemberLinkList": f3LagServiceMapMemberLinkList,
       "f3LagServiceMapCurrentMemberLink": f3LagServiceMapCurrentMemberLink,
       "f3LagConformance": f3LagConformance,
       "f3LagCompliances": f3LagCompliances,
       "f3LagCompliance": f3LagCompliance,
       "f3LagGroups": f3LagGroups,
       "f3LagObjectGroup": f3LagObjectGroup}
)
