# SNMP MIB module (F3-CFM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-CFM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:49 2025
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

(AdminState,
 CmPmBinAction,
 OperationalState,
 PerfCounter64,
 SecondaryState,
 VlanPriority) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "AdminState",
    "CmPmBinAction",
    "OperationalState",
    "PerfCounter64",
    "SecondaryState",
    "VlanPriority")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmEthernetAccPortIndex,
 cmEthernetNetPortIndex,
 cmEthernetTrafficPortIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetAccPortIndex",
    "cmEthernetNetPortIndex",
    "cmEthernetTrafficPortIndex")

(Dot1agCfmMDLevel,
 Dot1agCfmMepId,
 dot1agCfmMaCompEntry,
 dot1agCfmMaIndex,
 dot1agCfmMaNetEntry,
 dot1agCfmMdIndex,
 dot1agCfmMepEntry,
 dot1agCfmMepIdentifier) = mibBuilder.importSymbols(
    "IEEE8021-CFM-MIB",
    "Dot1agCfmMDLevel",
    "Dot1agCfmMepId",
    "dot1agCfmMaCompEntry",
    "dot1agCfmMaIndex",
    "dot1agCfmMaNetEntry",
    "dot1agCfmMdIndex",
    "dot1agCfmMepEntry",
    "dot1agCfmMepIdentifier")

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

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue,
 VariablePointer) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue",
    "VariablePointer")


# MODULE-IDENTITY

f3CfmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13)
)
if mibBuilder.loadTexts:
    f3CfmMIB.setRevisions(
        ("2021-01-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CfmAisGenTriggerTypes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bAisDefRemoteCCM", 0),
          ("bAisDefErrorCCM", 1),
          ("bAisDefXconCCM", 2),
          ("bAisDefAis", 3))
    )


class CfmAisInterval(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("aisInterval1sec", 1),
          ("aisInterval1min", 2))
    )



class CfmLmmDmmInterval(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("interval10msec", 1),
          ("interval100msec", 2),
          ("interval1sec", 3),
          ("interval10sec", 4),
          ("interval1min", 5))
    )



class CfmMepDefects(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        ("bDefAIS", 0)
    )


class CfmLLFTriggerTypes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("bAis", 0),
          ("bCcmIfStatusTlv", 1),
          ("bRemoteCCM", 2),
          ("bRDI", 3))
    )


class CfmSignalFailTriggers(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rdiCcm", 0),
          ("remoteCcm", 1),
          ("erroredCcm", 2),
          ("xconCcm", 3),
          ("ais", 4))
    )


class CfmSlmEnabledTypes(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cos0", 0),
          ("cos1", 1),
          ("cos2", 2),
          ("cos3", 3),
          ("cos4", 4),
          ("cos5", 5),
          ("cos6", 6),
          ("cos7", 7))
    )


class CfmPduVersionType(TextualConvention, Integer32):
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
        *(("notApplicable", 0),
          ("y1731-2008", 1),
          ("y1731-2011", 2))
    )



# MIB Managed Objects in the order of their OIDs

_CfmExtSvc_ObjectIdentity = ObjectIdentity
cfmExtSvc = _CfmExtSvc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1)
)
_CfmExtSvcObjects_ObjectIdentity = ObjectIdentity
cfmExtSvcObjects = _CfmExtSvcObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1)
)
_CfmExtScalars_ObjectIdentity = ObjectIdentity
cfmExtScalars = _CfmExtScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1)
)
_CfmEthType_Type = Integer32
_CfmEthType_Object = MibScalar
cfmEthType = _CfmEthType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 1),
    _CfmEthType_Type()
)
cfmEthType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmEthType.setStatus("current")
_CfmMacAddress_Type = MacAddress
_CfmMacAddress_Object = MibScalar
cfmMacAddress = _CfmMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 2),
    _CfmMacAddress_Type()
)
cfmMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMacAddress.setStatus("current")
_SlmMulticastMacAddress_Type = MacAddress
_SlmMulticastMacAddress_Object = MibScalar
slmMulticastMacAddress = _SlmMulticastMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 3),
    _SlmMulticastMacAddress_Type()
)
slmMulticastMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmMulticastMacAddress.setStatus("current")


class _SlmOpcode_Type(Integer32):
    """Custom type slmOpcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlmOpcode_Type.__name__ = "Integer32"
_SlmOpcode_Object = MibScalar
slmOpcode = _SlmOpcode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 4),
    _SlmOpcode_Type()
)
slmOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slmOpcode.setStatus("current")


class _SlrOpcode_Type(Integer32):
    """Custom type slrOpcode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SlrOpcode_Type.__name__ = "Integer32"
_SlrOpcode_Object = MibScalar
slrOpcode = _SlrOpcode_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 5),
    _SlrOpcode_Type()
)
slrOpcode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slrOpcode.setStatus("current")
_CfmSignalFailTriggers_Type = CfmSignalFailTriggers
_CfmSignalFailTriggers_Object = MibScalar
cfmSignalFailTriggers = _CfmSignalFailTriggers_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 1, 6),
    _CfmSignalFailTriggers_Type()
)
cfmSignalFailTriggers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmSignalFailTriggers.setStatus("current")
_CfmMepTable_Object = MibTable
cfmMepTable = _CfmMepTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2)
)
if mibBuilder.loadTexts:
    cfmMepTable.setStatus("current")
_CfmMepEntry_Object = MibTableRow
cfmMepEntry = _CfmMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    cfmMepEntry.setStatus("current")
_CfmMepAdminState_Type = AdminState
_CfmMepAdminState_Object = MibTableColumn
cfmMepAdminState = _CfmMepAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 1),
    _CfmMepAdminState_Type()
)
cfmMepAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepAdminState.setStatus("current")
_CfmMepAisGenTriggerTypes_Type = CfmAisGenTriggerTypes
_CfmMepAisGenTriggerTypes_Object = MibTableColumn
cfmMepAisGenTriggerTypes = _CfmMepAisGenTriggerTypes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 2),
    _CfmMepAisGenTriggerTypes_Type()
)
cfmMepAisGenTriggerTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepAisGenTriggerTypes.setStatus("current")
_CfmMepAisClientMdLevel_Type = Dot1agCfmMDLevel
_CfmMepAisClientMdLevel_Object = MibTableColumn
cfmMepAisClientMdLevel = _CfmMepAisClientMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 3),
    _CfmMepAisClientMdLevel_Type()
)
cfmMepAisClientMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepAisClientMdLevel.setStatus("current")
_CfmMepAisInterval_Type = CfmAisInterval
_CfmMepAisInterval_Object = MibTableColumn
cfmMepAisInterval = _CfmMepAisInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 4),
    _CfmMepAisInterval_Type()
)
cfmMepAisInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepAisInterval.setStatus("current")
_CfmMepAisGenEnabled_Type = TruthValue
_CfmMepAisGenEnabled_Object = MibTableColumn
cfmMepAisGenEnabled = _CfmMepAisGenEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 5),
    _CfmMepAisGenEnabled_Type()
)
cfmMepAisGenEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepAisGenEnabled.setStatus("current")
_CfmMepAisPriority_Type = VlanPriority
_CfmMepAisPriority_Object = MibTableColumn
cfmMepAisPriority = _CfmMepAisPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 6),
    _CfmMepAisPriority_Type()
)
cfmMepAisPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepAisPriority.setStatus("current")
_CfmMepLmTxCountAllPriosEnabled_Type = TruthValue
_CfmMepLmTxCountAllPriosEnabled_Object = MibTableColumn
cfmMepLmTxCountAllPriosEnabled = _CfmMepLmTxCountAllPriosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 7),
    _CfmMepLmTxCountAllPriosEnabled_Type()
)
cfmMepLmTxCountAllPriosEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepLmTxCountAllPriosEnabled.setStatus("current")
_CfmMepLmRxCountAllPriosEnabled_Type = TruthValue
_CfmMepLmRxCountAllPriosEnabled_Object = MibTableColumn
cfmMepLmRxCountAllPriosEnabled = _CfmMepLmRxCountAllPriosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 8),
    _CfmMepLmRxCountAllPriosEnabled_Type()
)
cfmMepLmRxCountAllPriosEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepLmRxCountAllPriosEnabled.setStatus("current")
_CfmMepLmDualEndedCountAllPriosEnabled_Type = TruthValue
_CfmMepLmDualEndedCountAllPriosEnabled_Object = MibTableColumn
cfmMepLmDualEndedCountAllPriosEnabled = _CfmMepLmDualEndedCountAllPriosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 9),
    _CfmMepLmDualEndedCountAllPriosEnabled_Type()
)
cfmMepLmDualEndedCountAllPriosEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepLmDualEndedCountAllPriosEnabled.setStatus("current")
_CfmMepLmCountInProfileEnabled_Type = TruthValue
_CfmMepLmCountInProfileEnabled_Object = MibTableColumn
cfmMepLmCountInProfileEnabled = _CfmMepLmCountInProfileEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 10),
    _CfmMepLmCountInProfileEnabled_Type()
)
cfmMepLmCountInProfileEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepLmCountInProfileEnabled.setStatus("current")
_CfmMepLmTxPriority_Type = VlanPriority
_CfmMepLmTxPriority_Object = MibTableColumn
cfmMepLmTxPriority = _CfmMepLmTxPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 11),
    _CfmMepLmTxPriority_Type()
)
cfmMepLmTxPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepLmTxPriority.setStatus("current")
_CfmMepDmPriority_Type = VlanPriority
_CfmMepDmPriority_Object = MibTableColumn
cfmMepDmPriority = _CfmMepDmPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 12),
    _CfmMepDmPriority_Type()
)
cfmMepDmPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepDmPriority.setStatus("current")
_CfmMepRxCCMs_Type = PerfCounter64
_CfmMepRxCCMs_Object = MibTableColumn
cfmMepRxCCMs = _CfmMepRxCCMs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 13),
    _CfmMepRxCCMs_Type()
)
cfmMepRxCCMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMepRxCCMs.setStatus("current")
_CfmMepErrCCMs_Type = PerfCounter64
_CfmMepErrCCMs_Object = MibTableColumn
cfmMepErrCCMs = _CfmMepErrCCMs_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 14),
    _CfmMepErrCCMs_Type()
)
cfmMepErrCCMs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMepErrCCMs.setStatus("current")
_CfmMepLLFTriggerTypes_Type = CfmLLFTriggerTypes
_CfmMepLLFTriggerTypes_Object = MibTableColumn
cfmMepLLFTriggerTypes = _CfmMepLLFTriggerTypes_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 15),
    _CfmMepLLFTriggerTypes_Type()
)
cfmMepLLFTriggerTypes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepLLFTriggerTypes.setStatus("current")
_CfmMepDefects_Type = CfmMepDefects
_CfmMepDefects_Object = MibTableColumn
cfmMepDefects = _CfmMepDefects_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 16),
    _CfmMepDefects_Type()
)
cfmMepDefects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMepDefects.setStatus("current")
_CfmMepTagEtherType_Type = Unsigned32
_CfmMepTagEtherType_Object = MibTableColumn
cfmMepTagEtherType = _CfmMepTagEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 17),
    _CfmMepTagEtherType_Type()
)
cfmMepTagEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepTagEtherType.setStatus("current")
_CfmMepStatsAction_Type = CmPmBinAction
_CfmMepStatsAction_Object = MibTableColumn
cfmMepStatsAction = _CfmMepStatsAction_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 18),
    _CfmMepStatsAction_Type()
)
cfmMepStatsAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepStatsAction.setStatus("current")
_CfmMepLbmInterval_Type = Integer32
_CfmMepLbmInterval_Object = MibTableColumn
cfmMepLbmInterval = _CfmMepLbmInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 19),
    _CfmMepLbmInterval_Type()
)
cfmMepLbmInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepLbmInterval.setStatus("current")
_CfmMepOperationalState_Type = OperationalState
_CfmMepOperationalState_Object = MibTableColumn
cfmMepOperationalState = _CfmMepOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 20),
    _CfmMepOperationalState_Type()
)
cfmMepOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMepOperationalState.setStatus("current")
_CfmMepSecondaryState_Type = SecondaryState
_CfmMepSecondaryState_Object = MibTableColumn
cfmMepSecondaryState = _CfmMepSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 21),
    _CfmMepSecondaryState_Type()
)
cfmMepSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMepSecondaryState.setStatus("current")
_CfmMepSlmEnabled_Type = CfmSlmEnabledTypes
_CfmMepSlmEnabled_Object = MibTableColumn
cfmMepSlmEnabled = _CfmMepSlmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 22),
    _CfmMepSlmEnabled_Type()
)
cfmMepSlmEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepSlmEnabled.setStatus("current")
_CfmMepAssociatedObject_Type = VariablePointer
_CfmMepAssociatedObject_Object = MibTableColumn
cfmMepAssociatedObject = _CfmMepAssociatedObject_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 23),
    _CfmMepAssociatedObject_Type()
)
cfmMepAssociatedObject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepAssociatedObject.setStatus("current")
_CfmMepPduVersion_Type = CfmPduVersionType
_CfmMepPduVersion_Object = MibTableColumn
cfmMepPduVersion = _CfmMepPduVersion_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 24),
    _CfmMepPduVersion_Type()
)
cfmMepPduVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepPduVersion.setStatus("current")
_CfmMepLlbResponderEnabled_Type = TruthValue
_CfmMepLlbResponderEnabled_Object = MibTableColumn
cfmMepLlbResponderEnabled = _CfmMepLlbResponderEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 25),
    _CfmMepLlbResponderEnabled_Type()
)
cfmMepLlbResponderEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepLlbResponderEnabled.setStatus("current")
_CfmMepLlbPortLLEnabled_Type = TruthValue
_CfmMepLlbPortLLEnabled_Object = MibTableColumn
cfmMepLlbPortLLEnabled = _CfmMepLlbPortLLEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 26),
    _CfmMepLlbPortLLEnabled_Type()
)
cfmMepLlbPortLLEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepLlbPortLLEnabled.setStatus("current")


class _CfmMepLlbVidList_Type(DisplayString):
    """Custom type cfmMepLlbVidList based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_CfmMepLlbVidList_Type.__name__ = "DisplayString"
_CfmMepLlbVidList_Object = MibTableColumn
cfmMepLlbVidList = _CfmMepLlbVidList_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 27),
    _CfmMepLlbVidList_Type()
)
cfmMepLlbVidList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepLlbVidList.setStatus("current")
_CfmMepCcmInterfaceStatusTLVControl_Type = TruthValue
_CfmMepCcmInterfaceStatusTLVControl_Object = MibTableColumn
cfmMepCcmInterfaceStatusTLVControl = _CfmMepCcmInterfaceStatusTLVControl_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 2, 1, 28),
    _CfmMepCcmInterfaceStatusTLVControl_Type()
)
cfmMepCcmInterfaceStatusTLVControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMepCcmInterfaceStatusTLVControl.setStatus("current")
_CfmAccPortQosShaperTable_Object = MibTable
cfmAccPortQosShaperTable = _CfmAccPortQosShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3)
)
if mibBuilder.loadTexts:
    cfmAccPortQosShaperTable.setStatus("current")
_CfmAccPortQosShaperEntry_Object = MibTableRow
cfmAccPortQosShaperEntry = _CfmAccPortQosShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1)
)
cfmAccPortQosShaperEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-CFM-MIB", "cfmAccPortQosShaperIndex"),
)
if mibBuilder.loadTexts:
    cfmAccPortQosShaperEntry.setStatus("current")
_CfmAccPortQosShaperIndex_Type = Integer32
_CfmAccPortQosShaperIndex_Object = MibTableColumn
cfmAccPortQosShaperIndex = _CfmAccPortQosShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1, 1),
    _CfmAccPortQosShaperIndex_Type()
)
cfmAccPortQosShaperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmAccPortQosShaperIndex.setStatus("current")
_CfmAccPortQosShaperCIR_Type = Unsigned32
_CfmAccPortQosShaperCIR_Object = MibTableColumn
cfmAccPortQosShaperCIR = _CfmAccPortQosShaperCIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1, 2),
    _CfmAccPortQosShaperCIR_Type()
)
cfmAccPortQosShaperCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmAccPortQosShaperCIR.setStatus("current")
_CfmAccPortQosShaperBufSize_Type = Unsigned32
_CfmAccPortQosShaperBufSize_Object = MibTableColumn
cfmAccPortQosShaperBufSize = _CfmAccPortQosShaperBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1, 3),
    _CfmAccPortQosShaperBufSize_Type()
)
cfmAccPortQosShaperBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmAccPortQosShaperBufSize.setStatus("current")
_CfmAccPortQosShaperAdminState_Type = AdminState
_CfmAccPortQosShaperAdminState_Object = MibTableColumn
cfmAccPortQosShaperAdminState = _CfmAccPortQosShaperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 3, 1, 4),
    _CfmAccPortQosShaperAdminState_Type()
)
cfmAccPortQosShaperAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmAccPortQosShaperAdminState.setStatus("current")
_CfmNetPortQosShaperTable_Object = MibTable
cfmNetPortQosShaperTable = _CfmNetPortQosShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4)
)
if mibBuilder.loadTexts:
    cfmNetPortQosShaperTable.setStatus("current")
_CfmNetPortQosShaperEntry_Object = MibTableRow
cfmNetPortQosShaperEntry = _CfmNetPortQosShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1)
)
cfmNetPortQosShaperEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-CFM-MIB", "cfmNetPortQosShaperTypeIndex"),
)
if mibBuilder.loadTexts:
    cfmNetPortQosShaperEntry.setStatus("current")
_CfmNetPortQosShaperTypeIndex_Type = Integer32
_CfmNetPortQosShaperTypeIndex_Object = MibTableColumn
cfmNetPortQosShaperTypeIndex = _CfmNetPortQosShaperTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1, 1),
    _CfmNetPortQosShaperTypeIndex_Type()
)
cfmNetPortQosShaperTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmNetPortQosShaperTypeIndex.setStatus("current")
_CfmNetPortQosShaperCIR_Type = Unsigned32
_CfmNetPortQosShaperCIR_Object = MibTableColumn
cfmNetPortQosShaperCIR = _CfmNetPortQosShaperCIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1, 2),
    _CfmNetPortQosShaperCIR_Type()
)
cfmNetPortQosShaperCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmNetPortQosShaperCIR.setStatus("current")
_CfmNetPortQosShaperBufSize_Type = Unsigned32
_CfmNetPortQosShaperBufSize_Object = MibTableColumn
cfmNetPortQosShaperBufSize = _CfmNetPortQosShaperBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1, 3),
    _CfmNetPortQosShaperBufSize_Type()
)
cfmNetPortQosShaperBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmNetPortQosShaperBufSize.setStatus("current")
_CfmNetPortQosShaperAdminState_Type = AdminState
_CfmNetPortQosShaperAdminState_Object = MibTableColumn
cfmNetPortQosShaperAdminState = _CfmNetPortQosShaperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 4, 1, 4),
    _CfmNetPortQosShaperAdminState_Type()
)
cfmNetPortQosShaperAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmNetPortQosShaperAdminState.setStatus("current")
_CfmServerMepTable_Object = MibTable
cfmServerMepTable = _CfmServerMepTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5)
)
if mibBuilder.loadTexts:
    cfmServerMepTable.setStatus("current")
_CfmServerMepEntry_Object = MibTableRow
cfmServerMepEntry = _CfmServerMepEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1)
)
cfmServerMepEntry.setIndexNames(
    (0, "F3-CFM-MIB", "cfmServerMepIndex"),
)
if mibBuilder.loadTexts:
    cfmServerMepEntry.setStatus("current")
_CfmServerMepIndex_Type = Integer32
_CfmServerMepIndex_Object = MibTableColumn
cfmServerMepIndex = _CfmServerMepIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 1),
    _CfmServerMepIndex_Type()
)
cfmServerMepIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmServerMepIndex.setStatus("current")
_CfmServerMepAssociatedPort_Type = VariablePointer
_CfmServerMepAssociatedPort_Object = MibTableColumn
cfmServerMepAssociatedPort = _CfmServerMepAssociatedPort_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 2),
    _CfmServerMepAssociatedPort_Type()
)
cfmServerMepAssociatedPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmServerMepAssociatedPort.setStatus("current")
_CfmServerMepAisClientMdLevel_Type = Dot1agCfmMDLevel
_CfmServerMepAisClientMdLevel_Object = MibTableColumn
cfmServerMepAisClientMdLevel = _CfmServerMepAisClientMdLevel_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 3),
    _CfmServerMepAisClientMdLevel_Type()
)
cfmServerMepAisClientMdLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmServerMepAisClientMdLevel.setStatus("current")
_CfmServerMepAisInterval_Type = CfmAisInterval
_CfmServerMepAisInterval_Object = MibTableColumn
cfmServerMepAisInterval = _CfmServerMepAisInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 4),
    _CfmServerMepAisInterval_Type()
)
cfmServerMepAisInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmServerMepAisInterval.setStatus("current")
_CfmServerMepAisGenEnabled_Type = TruthValue
_CfmServerMepAisGenEnabled_Object = MibTableColumn
cfmServerMepAisGenEnabled = _CfmServerMepAisGenEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 5),
    _CfmServerMepAisGenEnabled_Type()
)
cfmServerMepAisGenEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmServerMepAisGenEnabled.setStatus("current")
_CfmServerMepAisPriority_Type = VlanPriority
_CfmServerMepAisPriority_Object = MibTableColumn
cfmServerMepAisPriority = _CfmServerMepAisPriority_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 6),
    _CfmServerMepAisPriority_Type()
)
cfmServerMepAisPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmServerMepAisPriority.setStatus("current")
_CfmServerMepStorageType_Type = StorageType
_CfmServerMepStorageType_Object = MibTableColumn
cfmServerMepStorageType = _CfmServerMepStorageType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 7),
    _CfmServerMepStorageType_Type()
)
cfmServerMepStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmServerMepStorageType.setStatus("current")
_CfmServerMepRowStatus_Type = RowStatus
_CfmServerMepRowStatus_Object = MibTableColumn
cfmServerMepRowStatus = _CfmServerMepRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 8),
    _CfmServerMepRowStatus_Type()
)
cfmServerMepRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmServerMepRowStatus.setStatus("current")
_CfmServerMepAdminState_Type = AdminState
_CfmServerMepAdminState_Object = MibTableColumn
cfmServerMepAdminState = _CfmServerMepAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 9),
    _CfmServerMepAdminState_Type()
)
cfmServerMepAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmServerMepAdminState.setStatus("current")
_CfmServerMepOperationalState_Type = OperationalState
_CfmServerMepOperationalState_Object = MibTableColumn
cfmServerMepOperationalState = _CfmServerMepOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 10),
    _CfmServerMepOperationalState_Type()
)
cfmServerMepOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmServerMepOperationalState.setStatus("current")
_CfmServerMepSecondaryState_Type = SecondaryState
_CfmServerMepSecondaryState_Object = MibTableColumn
cfmServerMepSecondaryState = _CfmServerMepSecondaryState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 5, 1, 11),
    _CfmServerMepSecondaryState_Type()
)
cfmServerMepSecondaryState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmServerMepSecondaryState.setStatus("current")
_CfmDownMEPQosShaperTable_Object = MibTable
cfmDownMEPQosShaperTable = _CfmDownMEPQosShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6)
)
if mibBuilder.loadTexts:
    cfmDownMEPQosShaperTable.setStatus("current")
_CfmDownMEPQosShaperEntry_Object = MibTableRow
cfmDownMEPQosShaperEntry = _CfmDownMEPQosShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1)
)
cfmDownMEPQosShaperEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "F3-CFM-MIB", "cfmDownMEPQosShaperType"),
    (0, "F3-CFM-MIB", "cfmDownMEPQosShaperIndex"),
)
if mibBuilder.loadTexts:
    cfmDownMEPQosShaperEntry.setStatus("current")
_CfmDownMEPQosShaperIndex_Type = Integer32
_CfmDownMEPQosShaperIndex_Object = MibTableColumn
cfmDownMEPQosShaperIndex = _CfmDownMEPQosShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 1),
    _CfmDownMEPQosShaperIndex_Type()
)
cfmDownMEPQosShaperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmDownMEPQosShaperIndex.setStatus("current")
_CfmDownMEPQosShaperType_Type = Integer32
_CfmDownMEPQosShaperType_Object = MibTableColumn
cfmDownMEPQosShaperType = _CfmDownMEPQosShaperType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 2),
    _CfmDownMEPQosShaperType_Type()
)
cfmDownMEPQosShaperType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmDownMEPQosShaperType.setStatus("current")
_CfmDownMEPQosShaperCIR_Type = Unsigned32
_CfmDownMEPQosShaperCIR_Object = MibTableColumn
cfmDownMEPQosShaperCIR = _CfmDownMEPQosShaperCIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 3),
    _CfmDownMEPQosShaperCIR_Type()
)
cfmDownMEPQosShaperCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmDownMEPQosShaperCIR.setStatus("current")
_CfmDownMEPQosShaperProfile_Type = VariablePointer
_CfmDownMEPQosShaperProfile_Object = MibTableColumn
cfmDownMEPQosShaperProfile = _CfmDownMEPQosShaperProfile_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 4),
    _CfmDownMEPQosShaperProfile_Type()
)
cfmDownMEPQosShaperProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmDownMEPQosShaperProfile.setStatus("current")
_CfmDownMEPQosShaperAdminState_Type = AdminState
_CfmDownMEPQosShaperAdminState_Object = MibTableColumn
cfmDownMEPQosShaperAdminState = _CfmDownMEPQosShaperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 6, 1, 5),
    _CfmDownMEPQosShaperAdminState_Type()
)
cfmDownMEPQosShaperAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmDownMEPQosShaperAdminState.setStatus("current")
_CfmMepExcludedMepListTable_Object = MibTable
cfmMepExcludedMepListTable = _CfmMepExcludedMepListTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 7)
)
if mibBuilder.loadTexts:
    cfmMepExcludedMepListTable.setStatus("current")
_CfmMepExcludedMepListEntry_Object = MibTableRow
cfmMepExcludedMepListEntry = _CfmMepExcludedMepListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 7, 1)
)
cfmMepExcludedMepListEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "F3-CFM-MIB", "cfmMepExcludedMepListIdentifier"),
)
if mibBuilder.loadTexts:
    cfmMepExcludedMepListEntry.setStatus("current")


class _CfmMepExcludedMepListIdentifier_Type(Unsigned32):
    """Custom type cfmMepExcludedMepListIdentifier based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8191),
    )


_CfmMepExcludedMepListIdentifier_Type.__name__ = "Unsigned32"
_CfmMepExcludedMepListIdentifier_Object = MibTableColumn
cfmMepExcludedMepListIdentifier = _CfmMepExcludedMepListIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 7, 1, 1),
    _CfmMepExcludedMepListIdentifier_Type()
)
cfmMepExcludedMepListIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmMepExcludedMepListIdentifier.setStatus("current")
_CfmMepExcludedMepListRowStatus_Type = RowStatus
_CfmMepExcludedMepListRowStatus_Object = MibTableColumn
cfmMepExcludedMepListRowStatus = _CfmMepExcludedMepListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 7, 1, 2),
    _CfmMepExcludedMepListRowStatus_Type()
)
cfmMepExcludedMepListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMepExcludedMepListRowStatus.setStatus("current")
_CfmMepLbrTable_Object = MibTable
cfmMepLbrTable = _CfmMepLbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8)
)
if mibBuilder.loadTexts:
    cfmMepLbrTable.setStatus("current")
_CfmMepLbrEntry_Object = MibTableRow
cfmMepLbrEntry = _CfmMepLbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1)
)
cfmMepLbrEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "F3-CFM-MIB", "cfmMepLbrMacAddress"),
)
if mibBuilder.loadTexts:
    cfmMepLbrEntry.setStatus("current")
_CfmMepLbrMacAddress_Type = MacAddress
_CfmMepLbrMacAddress_Object = MibTableColumn
cfmMepLbrMacAddress = _CfmMepLbrMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1, 1),
    _CfmMepLbrMacAddress_Type()
)
cfmMepLbrMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMepLbrMacAddress.setStatus("current")
_CfmMepLbrMepId_Type = Integer32
_CfmMepLbrMepId_Object = MibTableColumn
cfmMepLbrMepId = _CfmMepLbrMepId_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1, 2),
    _CfmMepLbrMepId_Type()
)
cfmMepLbrMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMepLbrMepId.setStatus("current")
_CfmMepLbrInOrder_Type = PerfCounter64
_CfmMepLbrInOrder_Object = MibTableColumn
cfmMepLbrInOrder = _CfmMepLbrInOrder_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1, 3),
    _CfmMepLbrInOrder_Type()
)
cfmMepLbrInOrder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMepLbrInOrder.setStatus("current")
_CfmMepLbrOutOfOder_Type = PerfCounter64
_CfmMepLbrOutOfOder_Object = MibTableColumn
cfmMepLbrOutOfOder = _CfmMepLbrOutOfOder_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 8, 1, 4),
    _CfmMepLbrOutOfOder_Type()
)
cfmMepLbrOutOfOder.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMepLbrOutOfOder.setStatus("current")
_CfmMaCompTable_Object = MibTable
cfmMaCompTable = _CfmMaCompTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 9)
)
if mibBuilder.loadTexts:
    cfmMaCompTable.setStatus("current")
_CfmMaCompEntry_Object = MibTableRow
cfmMaCompEntry = _CfmMaCompEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 9, 1)
)
if mibBuilder.loadTexts:
    cfmMaCompEntry.setStatus("current")
_CfmMaCompIndex_Type = Unsigned32
_CfmMaCompIndex_Object = MibTableColumn
cfmMaCompIndex = _CfmMaCompIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 9, 1, 1),
    _CfmMaCompIndex_Type()
)
cfmMaCompIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfmMaCompIndex.setStatus("current")
_CfmMaCompEntity_Type = VariablePointer
_CfmMaCompEntity_Object = MibTableColumn
cfmMaCompEntity = _CfmMaCompEntity_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 9, 1, 2),
    _CfmMaCompEntity_Type()
)
cfmMaCompEntity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmMaCompEntity.setStatus("current")
_CfmMaNetTable_Object = MibTable
cfmMaNetTable = _CfmMaNetTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 10)
)
if mibBuilder.loadTexts:
    cfmMaNetTable.setStatus("current")
_CfmMaNetEntry_Object = MibTableRow
cfmMaNetEntry = _CfmMaNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    cfmMaNetEntry.setStatus("current")
_CfmMaNetRemoteMepAutoDiscovery_Type = TruthValue
_CfmMaNetRemoteMepAutoDiscovery_Object = MibTableColumn
cfmMaNetRemoteMepAutoDiscovery = _CfmMaNetRemoteMepAutoDiscovery_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 10, 1, 1),
    _CfmMaNetRemoteMepAutoDiscovery_Type()
)
cfmMaNetRemoteMepAutoDiscovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMaNetRemoteMepAutoDiscovery.setStatus("current")
_CfmMaNetMepNumbers_Type = Unsigned32
_CfmMaNetMepNumbers_Object = MibTableColumn
cfmMaNetMepNumbers = _CfmMaNetMepNumbers_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 10, 1, 2),
    _CfmMaNetMepNumbers_Type()
)
cfmMaNetMepNumbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmMaNetMepNumbers.setStatus("current")
_CfmTrafficPortQosShaperTable_Object = MibTable
cfmTrafficPortQosShaperTable = _CfmTrafficPortQosShaperTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11)
)
if mibBuilder.loadTexts:
    cfmTrafficPortQosShaperTable.setStatus("current")
_CfmTrafficPortQosShaperEntry_Object = MibTableRow
cfmTrafficPortQosShaperEntry = _CfmTrafficPortQosShaperEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1)
)
cfmTrafficPortQosShaperEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetTrafficPortIndex"),
    (0, "F3-CFM-MIB", "cfmTrafficPortQosShaperIndex"),
)
if mibBuilder.loadTexts:
    cfmTrafficPortQosShaperEntry.setStatus("current")
_CfmTrafficPortQosShaperIndex_Type = Integer32
_CfmTrafficPortQosShaperIndex_Object = MibTableColumn
cfmTrafficPortQosShaperIndex = _CfmTrafficPortQosShaperIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1, 1),
    _CfmTrafficPortQosShaperIndex_Type()
)
cfmTrafficPortQosShaperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmTrafficPortQosShaperIndex.setStatus("current")
_CfmTrafficPortQosShaperCIR_Type = Unsigned32
_CfmTrafficPortQosShaperCIR_Object = MibTableColumn
cfmTrafficPortQosShaperCIR = _CfmTrafficPortQosShaperCIR_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1, 2),
    _CfmTrafficPortQosShaperCIR_Type()
)
cfmTrafficPortQosShaperCIR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmTrafficPortQosShaperCIR.setStatus("current")
_CfmTrafficPortQosShaperBufSize_Type = Unsigned32
_CfmTrafficPortQosShaperBufSize_Object = MibTableColumn
cfmTrafficPortQosShaperBufSize = _CfmTrafficPortQosShaperBufSize_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1, 3),
    _CfmTrafficPortQosShaperBufSize_Type()
)
cfmTrafficPortQosShaperBufSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmTrafficPortQosShaperBufSize.setStatus("current")
_CfmTrafficPortQosShaperAdminState_Type = AdminState
_CfmTrafficPortQosShaperAdminState_Object = MibTableColumn
cfmTrafficPortQosShaperAdminState = _CfmTrafficPortQosShaperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 11, 1, 4),
    _CfmTrafficPortQosShaperAdminState_Type()
)
cfmTrafficPortQosShaperAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfmTrafficPortQosShaperAdminState.setStatus("current")
_CfmMepLlbMacAddressTable_Object = MibTable
cfmMepLlbMacAddressTable = _CfmMepLlbMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 12)
)
if mibBuilder.loadTexts:
    cfmMepLlbMacAddressTable.setStatus("current")
_CfmLlbMacAddressEntry_Object = MibTableRow
cfmLlbMacAddressEntry = _CfmLlbMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 12, 1)
)
cfmLlbMacAddressEntry.setIndexNames(
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMdIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMaIndex"),
    (0, "IEEE8021-CFM-MIB", "dot1agCfmMepIdentifier"),
    (0, "F3-CFM-MIB", "cfmLlbMacAddress"),
)
if mibBuilder.loadTexts:
    cfmLlbMacAddressEntry.setStatus("current")
_CfmLlbMacAddress_Type = MacAddress
_CfmLlbMacAddress_Object = MibTableColumn
cfmLlbMacAddress = _CfmLlbMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 12, 1, 1),
    _CfmLlbMacAddress_Type()
)
cfmLlbMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cfmLlbMacAddress.setStatus("current")
_CfmLlbMacAddressRowStatus_Type = RowStatus
_CfmLlbMacAddressRowStatus_Object = MibTableColumn
cfmLlbMacAddressRowStatus = _CfmLlbMacAddressRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 1, 12, 1, 2),
    _CfmLlbMacAddressRowStatus_Type()
)
cfmLlbMacAddressRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cfmLlbMacAddressRowStatus.setStatus("current")
_CfmExtSvcConformance_ObjectIdentity = ObjectIdentity
cfmExtSvcConformance = _CfmExtSvcConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2)
)
_CfmExtSvcCompliances_ObjectIdentity = ObjectIdentity
cfmExtSvcCompliances = _CfmExtSvcCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 1)
)
_CfmExtSvcGroups_ObjectIdentity = ObjectIdentity
cfmExtSvcGroups = _CfmExtSvcGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2)
)
dot1agCfmMepEntry.registerAugmentions(
    ("F3-CFM-MIB",
     "cfmMepEntry")
)
cfmMepEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
dot1agCfmMaCompEntry.registerAugmentions(
    ("F3-CFM-MIB",
     "cfmMaCompEntry")
)
cfmMaCompEntry.setIndexNames(*dot1agCfmMaCompEntry.getIndexNames())
dot1agCfmMaNetEntry.registerAugmentions(
    ("F3-CFM-MIB",
     "cfmMaNetEntry")
)
cfmMaNetEntry.setIndexNames(*dot1agCfmMaNetEntry.getIndexNames())

# Managed Objects groups

cfmExtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 1)
)
cfmExtGroup.setObjects(
      *(("F3-CFM-MIB", "cfmEthType"),
        ("F3-CFM-MIB", "cfmMacAddress"),
        ("F3-CFM-MIB", "slmMulticastMacAddress"),
        ("F3-CFM-MIB", "slmOpcode"),
        ("F3-CFM-MIB", "slrOpcode"),
        ("F3-CFM-MIB", "cfmMepAdminState"),
        ("F3-CFM-MIB", "cfmMepAisGenTriggerTypes"),
        ("F3-CFM-MIB", "cfmMepAisClientMdLevel"),
        ("F3-CFM-MIB", "cfmMepAisInterval"),
        ("F3-CFM-MIB", "cfmMepAisGenEnabled"),
        ("F3-CFM-MIB", "cfmMepAisPriority"),
        ("F3-CFM-MIB", "cfmMepLmTxCountAllPriosEnabled"),
        ("F3-CFM-MIB", "cfmMepLmRxCountAllPriosEnabled"),
        ("F3-CFM-MIB", "cfmMepLmDualEndedCountAllPriosEnabled"),
        ("F3-CFM-MIB", "cfmMepLmCountInProfileEnabled"),
        ("F3-CFM-MIB", "cfmMepLmTxPriority"),
        ("F3-CFM-MIB", "cfmMepDmPriority"),
        ("F3-CFM-MIB", "cfmMepRxCCMs"),
        ("F3-CFM-MIB", "cfmMepErrCCMs"),
        ("F3-CFM-MIB", "cfmMepLLFTriggerTypes"),
        ("F3-CFM-MIB", "cfmMepDefects"),
        ("F3-CFM-MIB", "cfmMepTagEtherType"),
        ("F3-CFM-MIB", "cfmMepStatsAction"),
        ("F3-CFM-MIB", "cfmMepLbmInterval"),
        ("F3-CFM-MIB", "cfmAccPortQosShaperIndex"),
        ("F3-CFM-MIB", "cfmAccPortQosShaperCIR"),
        ("F3-CFM-MIB", "cfmAccPortQosShaperBufSize"),
        ("F3-CFM-MIB", "cfmAccPortQosShaperAdminState"),
        ("F3-CFM-MIB", "cfmNetPortQosShaperTypeIndex"),
        ("F3-CFM-MIB", "cfmNetPortQosShaperCIR"),
        ("F3-CFM-MIB", "cfmNetPortQosShaperBufSize"),
        ("F3-CFM-MIB", "cfmNetPortQosShaperAdminState"),
        ("F3-CFM-MIB", "cfmServerMepIndex"),
        ("F3-CFM-MIB", "cfmServerMepAssociatedPort"),
        ("F3-CFM-MIB", "cfmServerMepAisClientMdLevel"),
        ("F3-CFM-MIB", "cfmServerMepAisInterval"),
        ("F3-CFM-MIB", "cfmServerMepAisGenEnabled"),
        ("F3-CFM-MIB", "cfmServerMepAisPriority"),
        ("F3-CFM-MIB", "cfmServerMepStorageType"),
        ("F3-CFM-MIB", "cfmServerMepRowStatus"),
        ("F3-CFM-MIB", "cfmDownMEPQosShaperIndex"),
        ("F3-CFM-MIB", "cfmDownMEPQosShaperType"),
        ("F3-CFM-MIB", "cfmDownMEPQosShaperCIR"),
        ("F3-CFM-MIB", "cfmDownMEPQosShaperProfile"),
        ("F3-CFM-MIB", "cfmDownMEPQosShaperAdminState"))
)
if mibBuilder.loadTexts:
    cfmExtGroup.setStatus("deprecated")

cfmGenGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 2)
)
cfmGenGroup.setObjects(
      *(("F3-CFM-MIB", "cfmEthType"),
        ("F3-CFM-MIB", "cfmMacAddress"),
        ("F3-CFM-MIB", "slmMulticastMacAddress"),
        ("F3-CFM-MIB", "slmOpcode"),
        ("F3-CFM-MIB", "slrOpcode"),
        ("F3-CFM-MIB", "cfmSignalFailTriggers"))
)
if mibBuilder.loadTexts:
    cfmGenGroup.setStatus("current")

cfmMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 3)
)
cfmMepGroup.setObjects(
      *(("F3-CFM-MIB", "cfmMepAdminState"),
        ("F3-CFM-MIB", "cfmMepAisGenTriggerTypes"),
        ("F3-CFM-MIB", "cfmMepAisClientMdLevel"),
        ("F3-CFM-MIB", "cfmMepAisInterval"),
        ("F3-CFM-MIB", "cfmMepAisGenEnabled"),
        ("F3-CFM-MIB", "cfmMepAisPriority"),
        ("F3-CFM-MIB", "cfmMepLmTxCountAllPriosEnabled"),
        ("F3-CFM-MIB", "cfmMepLmRxCountAllPriosEnabled"),
        ("F3-CFM-MIB", "cfmMepLmDualEndedCountAllPriosEnabled"),
        ("F3-CFM-MIB", "cfmMepLmCountInProfileEnabled"),
        ("F3-CFM-MIB", "cfmMepLmTxPriority"),
        ("F3-CFM-MIB", "cfmMepDmPriority"),
        ("F3-CFM-MIB", "cfmMepRxCCMs"),
        ("F3-CFM-MIB", "cfmMepErrCCMs"),
        ("F3-CFM-MIB", "cfmMepLLFTriggerTypes"),
        ("F3-CFM-MIB", "cfmMepDefects"),
        ("F3-CFM-MIB", "cfmMepTagEtherType"),
        ("F3-CFM-MIB", "cfmMepStatsAction"),
        ("F3-CFM-MIB", "cfmMepOperationalState"),
        ("F3-CFM-MIB", "cfmMepSecondaryState"),
        ("F3-CFM-MIB", "cfmMepSlmEnabled"),
        ("F3-CFM-MIB", "cfmMepExcludedMepListIdentifier"),
        ("F3-CFM-MIB", "cfmMepExcludedMepListRowStatus"),
        ("F3-CFM-MIB", "cfmMepLbrMacAddress"),
        ("F3-CFM-MIB", "cfmMepLbrMepId"),
        ("F3-CFM-MIB", "cfmMepLbrInOrder"),
        ("F3-CFM-MIB", "cfmMepLbrOutOfOder"),
        ("F3-CFM-MIB", "cfmMepAssociatedObject"),
        ("F3-CFM-MIB", "cfmMepPduVersion"),
        ("F3-CFM-MIB", "cfmMepLlbResponderEnabled"),
        ("F3-CFM-MIB", "cfmMepLlbPortLLEnabled"),
        ("F3-CFM-MIB", "cfmMepLlbVidList"),
        ("F3-CFM-MIB", "cfmLlbMacAddress"),
        ("F3-CFM-MIB", "cfmMepCcmInterfaceStatusTLVControl"))
)
if mibBuilder.loadTexts:
    cfmMepGroup.setStatus("current")

cfmPortShaperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 4)
)
cfmPortShaperGroup.setObjects(
      *(("F3-CFM-MIB", "cfmAccPortQosShaperIndex"),
        ("F3-CFM-MIB", "cfmAccPortQosShaperCIR"),
        ("F3-CFM-MIB", "cfmAccPortQosShaperBufSize"),
        ("F3-CFM-MIB", "cfmAccPortQosShaperAdminState"),
        ("F3-CFM-MIB", "cfmNetPortQosShaperTypeIndex"),
        ("F3-CFM-MIB", "cfmNetPortQosShaperCIR"),
        ("F3-CFM-MIB", "cfmNetPortQosShaperBufSize"),
        ("F3-CFM-MIB", "cfmNetPortQosShaperAdminState"))
)
if mibBuilder.loadTexts:
    cfmPortShaperGroup.setStatus("current")

cfmServerMepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 5)
)
cfmServerMepGroup.setObjects(
      *(("F3-CFM-MIB", "cfmServerMepIndex"),
        ("F3-CFM-MIB", "cfmServerMepAssociatedPort"),
        ("F3-CFM-MIB", "cfmServerMepAisClientMdLevel"),
        ("F3-CFM-MIB", "cfmServerMepAisInterval"),
        ("F3-CFM-MIB", "cfmServerMepAisGenEnabled"),
        ("F3-CFM-MIB", "cfmServerMepAisPriority"),
        ("F3-CFM-MIB", "cfmServerMepStorageType"),
        ("F3-CFM-MIB", "cfmServerMepRowStatus"),
        ("F3-CFM-MIB", "cfmServerMepAdminState"),
        ("F3-CFM-MIB", "cfmServerMepOperationalState"),
        ("F3-CFM-MIB", "cfmServerMepSecondaryState"))
)
if mibBuilder.loadTexts:
    cfmServerMepGroup.setStatus("current")

cfmMaCompGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 2, 6)
)
cfmMaCompGroup.setObjects(
      *(("F3-CFM-MIB", "cfmMaCompIndex"),
        ("F3-CFM-MIB", "cfmMaCompEntity"))
)
if mibBuilder.loadTexts:
    cfmMaCompGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

cfmExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 13, 1, 2, 1, 1)
)
cfmExtCompliance.setObjects(
      *(("F3-CFM-MIB", "cfmExtGroup"),
        ("F3-CFM-MIB", "cfmGenGroup"),
        ("F3-CFM-MIB", "cfmMepGroup"),
        ("F3-CFM-MIB", "cfmPortShaperGroup"),
        ("F3-CFM-MIB", "cfmServerMepGroup"))
)
if mibBuilder.loadTexts:
    cfmExtCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-CFM-MIB",
    **{"CfmAisGenTriggerTypes": CfmAisGenTriggerTypes,
       "CfmAisInterval": CfmAisInterval,
       "CfmLmmDmmInterval": CfmLmmDmmInterval,
       "CfmMepDefects": CfmMepDefects,
       "CfmLLFTriggerTypes": CfmLLFTriggerTypes,
       "CfmSignalFailTriggers": CfmSignalFailTriggers,
       "CfmSlmEnabledTypes": CfmSlmEnabledTypes,
       "CfmPduVersionType": CfmPduVersionType,
       "f3CfmMIB": f3CfmMIB,
       "cfmExtSvc": cfmExtSvc,
       "cfmExtSvcObjects": cfmExtSvcObjects,
       "cfmExtScalars": cfmExtScalars,
       "cfmEthType": cfmEthType,
       "cfmMacAddress": cfmMacAddress,
       "slmMulticastMacAddress": slmMulticastMacAddress,
       "slmOpcode": slmOpcode,
       "slrOpcode": slrOpcode,
       "cfmSignalFailTriggers": cfmSignalFailTriggers,
       "cfmMepTable": cfmMepTable,
       "cfmMepEntry": cfmMepEntry,
       "cfmMepAdminState": cfmMepAdminState,
       "cfmMepAisGenTriggerTypes": cfmMepAisGenTriggerTypes,
       "cfmMepAisClientMdLevel": cfmMepAisClientMdLevel,
       "cfmMepAisInterval": cfmMepAisInterval,
       "cfmMepAisGenEnabled": cfmMepAisGenEnabled,
       "cfmMepAisPriority": cfmMepAisPriority,
       "cfmMepLmTxCountAllPriosEnabled": cfmMepLmTxCountAllPriosEnabled,
       "cfmMepLmRxCountAllPriosEnabled": cfmMepLmRxCountAllPriosEnabled,
       "cfmMepLmDualEndedCountAllPriosEnabled": cfmMepLmDualEndedCountAllPriosEnabled,
       "cfmMepLmCountInProfileEnabled": cfmMepLmCountInProfileEnabled,
       "cfmMepLmTxPriority": cfmMepLmTxPriority,
       "cfmMepDmPriority": cfmMepDmPriority,
       "cfmMepRxCCMs": cfmMepRxCCMs,
       "cfmMepErrCCMs": cfmMepErrCCMs,
       "cfmMepLLFTriggerTypes": cfmMepLLFTriggerTypes,
       "cfmMepDefects": cfmMepDefects,
       "cfmMepTagEtherType": cfmMepTagEtherType,
       "cfmMepStatsAction": cfmMepStatsAction,
       "cfmMepLbmInterval": cfmMepLbmInterval,
       "cfmMepOperationalState": cfmMepOperationalState,
       "cfmMepSecondaryState": cfmMepSecondaryState,
       "cfmMepSlmEnabled": cfmMepSlmEnabled,
       "cfmMepAssociatedObject": cfmMepAssociatedObject,
       "cfmMepPduVersion": cfmMepPduVersion,
       "cfmMepLlbResponderEnabled": cfmMepLlbResponderEnabled,
       "cfmMepLlbPortLLEnabled": cfmMepLlbPortLLEnabled,
       "cfmMepLlbVidList": cfmMepLlbVidList,
       "cfmMepCcmInterfaceStatusTLVControl": cfmMepCcmInterfaceStatusTLVControl,
       "cfmAccPortQosShaperTable": cfmAccPortQosShaperTable,
       "cfmAccPortQosShaperEntry": cfmAccPortQosShaperEntry,
       "cfmAccPortQosShaperIndex": cfmAccPortQosShaperIndex,
       "cfmAccPortQosShaperCIR": cfmAccPortQosShaperCIR,
       "cfmAccPortQosShaperBufSize": cfmAccPortQosShaperBufSize,
       "cfmAccPortQosShaperAdminState": cfmAccPortQosShaperAdminState,
       "cfmNetPortQosShaperTable": cfmNetPortQosShaperTable,
       "cfmNetPortQosShaperEntry": cfmNetPortQosShaperEntry,
       "cfmNetPortQosShaperTypeIndex": cfmNetPortQosShaperTypeIndex,
       "cfmNetPortQosShaperCIR": cfmNetPortQosShaperCIR,
       "cfmNetPortQosShaperBufSize": cfmNetPortQosShaperBufSize,
       "cfmNetPortQosShaperAdminState": cfmNetPortQosShaperAdminState,
       "cfmServerMepTable": cfmServerMepTable,
       "cfmServerMepEntry": cfmServerMepEntry,
       "cfmServerMepIndex": cfmServerMepIndex,
       "cfmServerMepAssociatedPort": cfmServerMepAssociatedPort,
       "cfmServerMepAisClientMdLevel": cfmServerMepAisClientMdLevel,
       "cfmServerMepAisInterval": cfmServerMepAisInterval,
       "cfmServerMepAisGenEnabled": cfmServerMepAisGenEnabled,
       "cfmServerMepAisPriority": cfmServerMepAisPriority,
       "cfmServerMepStorageType": cfmServerMepStorageType,
       "cfmServerMepRowStatus": cfmServerMepRowStatus,
       "cfmServerMepAdminState": cfmServerMepAdminState,
       "cfmServerMepOperationalState": cfmServerMepOperationalState,
       "cfmServerMepSecondaryState": cfmServerMepSecondaryState,
       "cfmDownMEPQosShaperTable": cfmDownMEPQosShaperTable,
       "cfmDownMEPQosShaperEntry": cfmDownMEPQosShaperEntry,
       "cfmDownMEPQosShaperIndex": cfmDownMEPQosShaperIndex,
       "cfmDownMEPQosShaperType": cfmDownMEPQosShaperType,
       "cfmDownMEPQosShaperCIR": cfmDownMEPQosShaperCIR,
       "cfmDownMEPQosShaperProfile": cfmDownMEPQosShaperProfile,
       "cfmDownMEPQosShaperAdminState": cfmDownMEPQosShaperAdminState,
       "cfmMepExcludedMepListTable": cfmMepExcludedMepListTable,
       "cfmMepExcludedMepListEntry": cfmMepExcludedMepListEntry,
       "cfmMepExcludedMepListIdentifier": cfmMepExcludedMepListIdentifier,
       "cfmMepExcludedMepListRowStatus": cfmMepExcludedMepListRowStatus,
       "cfmMepLbrTable": cfmMepLbrTable,
       "cfmMepLbrEntry": cfmMepLbrEntry,
       "cfmMepLbrMacAddress": cfmMepLbrMacAddress,
       "cfmMepLbrMepId": cfmMepLbrMepId,
       "cfmMepLbrInOrder": cfmMepLbrInOrder,
       "cfmMepLbrOutOfOder": cfmMepLbrOutOfOder,
       "cfmMaCompTable": cfmMaCompTable,
       "cfmMaCompEntry": cfmMaCompEntry,
       "cfmMaCompIndex": cfmMaCompIndex,
       "cfmMaCompEntity": cfmMaCompEntity,
       "cfmMaNetTable": cfmMaNetTable,
       "cfmMaNetEntry": cfmMaNetEntry,
       "cfmMaNetRemoteMepAutoDiscovery": cfmMaNetRemoteMepAutoDiscovery,
       "cfmMaNetMepNumbers": cfmMaNetMepNumbers,
       "cfmTrafficPortQosShaperTable": cfmTrafficPortQosShaperTable,
       "cfmTrafficPortQosShaperEntry": cfmTrafficPortQosShaperEntry,
       "cfmTrafficPortQosShaperIndex": cfmTrafficPortQosShaperIndex,
       "cfmTrafficPortQosShaperCIR": cfmTrafficPortQosShaperCIR,
       "cfmTrafficPortQosShaperBufSize": cfmTrafficPortQosShaperBufSize,
       "cfmTrafficPortQosShaperAdminState": cfmTrafficPortQosShaperAdminState,
       "cfmMepLlbMacAddressTable": cfmMepLlbMacAddressTable,
       "cfmLlbMacAddressEntry": cfmLlbMacAddressEntry,
       "cfmLlbMacAddress": cfmLlbMacAddress,
       "cfmLlbMacAddressRowStatus": cfmLlbMacAddressRowStatus,
       "cfmExtSvcConformance": cfmExtSvcConformance,
       "cfmExtSvcCompliances": cfmExtSvcCompliances,
       "cfmExtCompliance": cfmExtCompliance,
       "cfmExtSvcGroups": cfmExtSvcGroups,
       "cfmExtGroup": cfmExtGroup,
       "cfmGenGroup": cfmGenGroup,
       "cfmMepGroup": cfmMepGroup,
       "cfmPortShaperGroup": cfmPortShaperGroup,
       "cfmServerMepGroup": cfmServerMepGroup,
       "cfmMaCompGroup": cfmMaCompGroup}
)
