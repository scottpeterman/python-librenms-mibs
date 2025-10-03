# SNMP MIB module (F3-ELMI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\adva\F3-ELMI-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:15:58 2025
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

(OperationalState,
 PerfCounter64) = mibBuilder.importSymbols(
    "CM-COMMON-MIB",
    "OperationalState",
    "PerfCounter64")

(neIndex,
 shelfIndex,
 slotIndex) = mibBuilder.importSymbols(
    "CM-ENTITY-MIB",
    "neIndex",
    "shelfIndex",
    "slotIndex")

(cmEthernetAccPortIndex,
 cmEthernetNetPortIndex,
 cmFlowIndex) = mibBuilder.importSymbols(
    "CM-FACILITY-MIB",
    "cmEthernetAccPortIndex",
    "cmEthernetNetPortIndex",
    "cmFlowIndex")

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


# MODULE-IDENTITY

f3ElmiMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20)
)
if mibBuilder.loadTexts:
    f3ElmiMIB.setRevisions(
        ("2012-05-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ELMIEvcStatus(TextualConvention, Integer32):
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
        *(("active", 1),
          ("inactive", 2),
          ("partiallyActive", 3))
    )



class ELMIEvcType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 1),
          ("pointToMultipoint", 2))
    )



# MIB Managed Objects in the order of their OIDs

_F3ElmiConfigObjects_ObjectIdentity = ObjectIdentity
f3ElmiConfigObjects = _F3ElmiConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1)
)
_F3AccPortElmiConfigTable_Object = MibTable
f3AccPortElmiConfigTable = _F3AccPortElmiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1)
)
if mibBuilder.loadTexts:
    f3AccPortElmiConfigTable.setStatus("current")
_F3AccPortElmiConfigEntry_Object = MibTableRow
f3AccPortElmiConfigEntry = _F3AccPortElmiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1)
)
f3AccPortElmiConfigEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-ELMI-MIB", "f3AccPortElmiConfigIndex"),
)
if mibBuilder.loadTexts:
    f3AccPortElmiConfigEntry.setStatus("current")
_F3AccPortElmiConfigIndex_Type = Integer32
_F3AccPortElmiConfigIndex_Object = MibTableColumn
f3AccPortElmiConfigIndex = _F3AccPortElmiConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 1),
    _F3AccPortElmiConfigIndex_Type()
)
f3AccPortElmiConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AccPortElmiConfigIndex.setStatus("current")
_F3AccPortElmiConfigEnabled_Type = TruthValue
_F3AccPortElmiConfigEnabled_Object = MibTableColumn
f3AccPortElmiConfigEnabled = _F3AccPortElmiConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 2),
    _F3AccPortElmiConfigEnabled_Type()
)
f3AccPortElmiConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccPortElmiConfigEnabled.setStatus("current")
_F3AccPortElmiConfigOperationalState_Type = OperationalState
_F3AccPortElmiConfigOperationalState_Object = MibTableColumn
f3AccPortElmiConfigOperationalState = _F3AccPortElmiConfigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 3),
    _F3AccPortElmiConfigOperationalState_Type()
)
f3AccPortElmiConfigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiConfigOperationalState.setStatus("current")


class _F3AccPortElmiConfigN393StatusCounter_Type(Integer32):
    """Custom type f3AccPortElmiConfigN393StatusCounter based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_F3AccPortElmiConfigN393StatusCounter_Type.__name__ = "Integer32"
_F3AccPortElmiConfigN393StatusCounter_Object = MibTableColumn
f3AccPortElmiConfigN393StatusCounter = _F3AccPortElmiConfigN393StatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 4),
    _F3AccPortElmiConfigN393StatusCounter_Type()
)
f3AccPortElmiConfigN393StatusCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccPortElmiConfigN393StatusCounter.setStatus("current")


class _F3AccPortElmiConfigT392PollVerificationTimer_Type(Integer32):
    """Custom type f3AccPortElmiConfigT392PollVerificationTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 30),
    )


_F3AccPortElmiConfigT392PollVerificationTimer_Type.__name__ = "Integer32"
_F3AccPortElmiConfigT392PollVerificationTimer_Object = MibTableColumn
f3AccPortElmiConfigT392PollVerificationTimer = _F3AccPortElmiConfigT392PollVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 5),
    _F3AccPortElmiConfigT392PollVerificationTimer_Type()
)
f3AccPortElmiConfigT392PollVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccPortElmiConfigT392PollVerificationTimer.setStatus("current")
_F3AccPortElmiConfigAsyncStatusEnabled_Type = TruthValue
_F3AccPortElmiConfigAsyncStatusEnabled_Object = MibTableColumn
f3AccPortElmiConfigAsyncStatusEnabled = _F3AccPortElmiConfigAsyncStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 6),
    _F3AccPortElmiConfigAsyncStatusEnabled_Type()
)
f3AccPortElmiConfigAsyncStatusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccPortElmiConfigAsyncStatusEnabled.setStatus("current")


class _F3AccPortElmiConfigMinAsyncMessageInterval_Type(Integer32):
    """Custom type f3AccPortElmiConfigMinAsyncMessageInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_F3AccPortElmiConfigMinAsyncMessageInterval_Type.__name__ = "Integer32"
_F3AccPortElmiConfigMinAsyncMessageInterval_Object = MibTableColumn
f3AccPortElmiConfigMinAsyncMessageInterval = _F3AccPortElmiConfigMinAsyncMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 1, 1, 7),
    _F3AccPortElmiConfigMinAsyncMessageInterval_Type()
)
f3AccPortElmiConfigMinAsyncMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3AccPortElmiConfigMinAsyncMessageInterval.setStatus("current")
_F3NetPortElmiConfigTable_Object = MibTable
f3NetPortElmiConfigTable = _F3NetPortElmiConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2)
)
if mibBuilder.loadTexts:
    f3NetPortElmiConfigTable.setStatus("current")
_F3NetPortElmiConfigEntry_Object = MibTableRow
f3NetPortElmiConfigEntry = _F3NetPortElmiConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1)
)
f3NetPortElmiConfigEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-ELMI-MIB", "f3NetPortElmiConfigIndex"),
)
if mibBuilder.loadTexts:
    f3NetPortElmiConfigEntry.setStatus("current")
_F3NetPortElmiConfigIndex_Type = Integer32
_F3NetPortElmiConfigIndex_Object = MibTableColumn
f3NetPortElmiConfigIndex = _F3NetPortElmiConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 1),
    _F3NetPortElmiConfigIndex_Type()
)
f3NetPortElmiConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NetPortElmiConfigIndex.setStatus("current")
_F3NetPortElmiConfigEnabled_Type = TruthValue
_F3NetPortElmiConfigEnabled_Object = MibTableColumn
f3NetPortElmiConfigEnabled = _F3NetPortElmiConfigEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 2),
    _F3NetPortElmiConfigEnabled_Type()
)
f3NetPortElmiConfigEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortElmiConfigEnabled.setStatus("current")
_F3NetPortElmiConfigOperationalState_Type = OperationalState
_F3NetPortElmiConfigOperationalState_Object = MibTableColumn
f3NetPortElmiConfigOperationalState = _F3NetPortElmiConfigOperationalState_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 3),
    _F3NetPortElmiConfigOperationalState_Type()
)
f3NetPortElmiConfigOperationalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiConfigOperationalState.setStatus("current")


class _F3NetPortElmiConfigN393StatusCounter_Type(Integer32):
    """Custom type f3NetPortElmiConfigN393StatusCounter based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_F3NetPortElmiConfigN393StatusCounter_Type.__name__ = "Integer32"
_F3NetPortElmiConfigN393StatusCounter_Object = MibTableColumn
f3NetPortElmiConfigN393StatusCounter = _F3NetPortElmiConfigN393StatusCounter_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 4),
    _F3NetPortElmiConfigN393StatusCounter_Type()
)
f3NetPortElmiConfigN393StatusCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortElmiConfigN393StatusCounter.setStatus("current")


class _F3NetPortElmiConfigT392PollVerificationTimer_Type(Integer32):
    """Custom type f3NetPortElmiConfigT392PollVerificationTimer based on Integer32"""
    defaultValue = 15

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 30),
    )


_F3NetPortElmiConfigT392PollVerificationTimer_Type.__name__ = "Integer32"
_F3NetPortElmiConfigT392PollVerificationTimer_Object = MibTableColumn
f3NetPortElmiConfigT392PollVerificationTimer = _F3NetPortElmiConfigT392PollVerificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 5),
    _F3NetPortElmiConfigT392PollVerificationTimer_Type()
)
f3NetPortElmiConfigT392PollVerificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortElmiConfigT392PollVerificationTimer.setStatus("current")
_F3NetPortElmiConfigAsyncStatusEnabled_Type = TruthValue
_F3NetPortElmiConfigAsyncStatusEnabled_Object = MibTableColumn
f3NetPortElmiConfigAsyncStatusEnabled = _F3NetPortElmiConfigAsyncStatusEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 6),
    _F3NetPortElmiConfigAsyncStatusEnabled_Type()
)
f3NetPortElmiConfigAsyncStatusEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortElmiConfigAsyncStatusEnabled.setStatus("current")


class _F3NetPortElmiConfigMinAsyncMessageInterval_Type(Integer32):
    """Custom type f3NetPortElmiConfigMinAsyncMessageInterval based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_F3NetPortElmiConfigMinAsyncMessageInterval_Type.__name__ = "Integer32"
_F3NetPortElmiConfigMinAsyncMessageInterval_Object = MibTableColumn
f3NetPortElmiConfigMinAsyncMessageInterval = _F3NetPortElmiConfigMinAsyncMessageInterval_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 2, 1, 7),
    _F3NetPortElmiConfigMinAsyncMessageInterval_Type()
)
f3NetPortElmiConfigMinAsyncMessageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    f3NetPortElmiConfigMinAsyncMessageInterval.setStatus("current")
_F3ElmiEvcStatusInfoTable_Object = MibTable
f3ElmiEvcStatusInfoTable = _F3ElmiEvcStatusInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3)
)
if mibBuilder.loadTexts:
    f3ElmiEvcStatusInfoTable.setStatus("current")
_F3ElmiEvcStatusInfoEntry_Object = MibTableRow
f3ElmiEvcStatusInfoEntry = _F3ElmiEvcStatusInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1)
)
f3ElmiEvcStatusInfoEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "CM-FACILITY-MIB", "cmFlowIndex"),
)
if mibBuilder.loadTexts:
    f3ElmiEvcStatusInfoEntry.setStatus("current")
_F3ElmiEvcStatusInfoEvcID_Type = Integer32
_F3ElmiEvcStatusInfoEvcID_Object = MibTableColumn
f3ElmiEvcStatusInfoEvcID = _F3ElmiEvcStatusInfoEvcID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 1),
    _F3ElmiEvcStatusInfoEvcID_Type()
)
f3ElmiEvcStatusInfoEvcID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ElmiEvcStatusInfoEvcID.setStatus("current")
_F3ElmiEvcStatusInfoEvcFlowID_Type = DisplayString
_F3ElmiEvcStatusInfoEvcFlowID_Object = MibTableColumn
f3ElmiEvcStatusInfoEvcFlowID = _F3ElmiEvcStatusInfoEvcFlowID_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 2),
    _F3ElmiEvcStatusInfoEvcFlowID_Type()
)
f3ElmiEvcStatusInfoEvcFlowID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ElmiEvcStatusInfoEvcFlowID.setStatus("current")
_F3ElmiEvcStatusInfoEvcStatus_Type = ELMIEvcStatus
_F3ElmiEvcStatusInfoEvcStatus_Object = MibTableColumn
f3ElmiEvcStatusInfoEvcStatus = _F3ElmiEvcStatusInfoEvcStatus_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 3),
    _F3ElmiEvcStatusInfoEvcStatus_Type()
)
f3ElmiEvcStatusInfoEvcStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ElmiEvcStatusInfoEvcStatus.setStatus("current")
_F3ElmiEvcStatusInfoEvcType_Type = ELMIEvcType
_F3ElmiEvcStatusInfoEvcType_Object = MibTableColumn
f3ElmiEvcStatusInfoEvcType = _F3ElmiEvcStatusInfoEvcType_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 1, 3, 1, 4),
    _F3ElmiEvcStatusInfoEvcType_Type()
)
f3ElmiEvcStatusInfoEvcType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3ElmiEvcStatusInfoEvcType.setStatus("current")
_F3ElmiStatsObjects_ObjectIdentity = ObjectIdentity
f3ElmiStatsObjects = _F3ElmiStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2)
)
_F3AccPortElmiStatsTable_Object = MibTable
f3AccPortElmiStatsTable = _F3AccPortElmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1)
)
if mibBuilder.loadTexts:
    f3AccPortElmiStatsTable.setStatus("current")
_F3AccPortElmiStatsEntry_Object = MibTableRow
f3AccPortElmiStatsEntry = _F3AccPortElmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1)
)
f3AccPortElmiStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetAccPortIndex"),
    (0, "F3-ELMI-MIB", "f3AccPortElmiConfigIndex"),
    (0, "F3-ELMI-MIB", "f3AccPortElmiStatsIndex"),
)
if mibBuilder.loadTexts:
    f3AccPortElmiStatsEntry.setStatus("current")
_F3AccPortElmiStatsIndex_Type = Integer32
_F3AccPortElmiStatsIndex_Object = MibTableColumn
f3AccPortElmiStatsIndex = _F3AccPortElmiStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 1),
    _F3AccPortElmiStatsIndex_Type()
)
f3AccPortElmiStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsIndex.setStatus("current")
_F3AccPortElmiStatsLastFullStatusSent_Type = TimeTicks
_F3AccPortElmiStatsLastFullStatusSent_Object = MibTableColumn
f3AccPortElmiStatsLastFullStatusSent = _F3AccPortElmiStatsLastFullStatusSent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 2),
    _F3AccPortElmiStatsLastFullStatusSent_Type()
)
f3AccPortElmiStatsLastFullStatusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsLastFullStatusSent.setStatus("current")
_F3AccPortElmiStatsLastStatusCheckSent_Type = TimeTicks
_F3AccPortElmiStatsLastStatusCheckSent_Object = MibTableColumn
f3AccPortElmiStatsLastStatusCheckSent = _F3AccPortElmiStatsLastStatusCheckSent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 3),
    _F3AccPortElmiStatsLastStatusCheckSent_Type()
)
f3AccPortElmiStatsLastStatusCheckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsLastStatusCheckSent.setStatus("current")
_F3AccPortElmiStatsLastFullStatusReceived_Type = TimeTicks
_F3AccPortElmiStatsLastFullStatusReceived_Object = MibTableColumn
f3AccPortElmiStatsLastFullStatusReceived = _F3AccPortElmiStatsLastFullStatusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 4),
    _F3AccPortElmiStatsLastFullStatusReceived_Type()
)
f3AccPortElmiStatsLastFullStatusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsLastFullStatusReceived.setStatus("current")
_F3AccPortElmiStatsLastStatusCheckReceived_Type = TimeTicks
_F3AccPortElmiStatsLastStatusCheckReceived_Object = MibTableColumn
f3AccPortElmiStatsLastStatusCheckReceived = _F3AccPortElmiStatsLastStatusCheckReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 5),
    _F3AccPortElmiStatsLastStatusCheckReceived_Type()
)
f3AccPortElmiStatsLastStatusCheckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsLastStatusCheckReceived.setStatus("current")
_F3AccPortElmiStatsInvalidProtocolVersionFrames_Type = PerfCounter64
_F3AccPortElmiStatsInvalidProtocolVersionFrames_Object = MibTableColumn
f3AccPortElmiStatsInvalidProtocolVersionFrames = _F3AccPortElmiStatsInvalidProtocolVersionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 6),
    _F3AccPortElmiStatsInvalidProtocolVersionFrames_Type()
)
f3AccPortElmiStatsInvalidProtocolVersionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsInvalidProtocolVersionFrames.setStatus("current")
_F3AccPortElmiStatsInvalidMessageTypeFrames_Type = PerfCounter64
_F3AccPortElmiStatsInvalidMessageTypeFrames_Object = MibTableColumn
f3AccPortElmiStatsInvalidMessageTypeFrames = _F3AccPortElmiStatsInvalidMessageTypeFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 7),
    _F3AccPortElmiStatsInvalidMessageTypeFrames_Type()
)
f3AccPortElmiStatsInvalidMessageTypeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsInvalidMessageTypeFrames.setStatus("current")
_F3AccPortElmiStatsOutOfSequenceIEFrames_Type = PerfCounter64
_F3AccPortElmiStatsOutOfSequenceIEFrames_Object = MibTableColumn
f3AccPortElmiStatsOutOfSequenceIEFrames = _F3AccPortElmiStatsOutOfSequenceIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 8),
    _F3AccPortElmiStatsOutOfSequenceIEFrames_Type()
)
f3AccPortElmiStatsOutOfSequenceIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsOutOfSequenceIEFrames.setStatus("current")
_F3AccPortElmiStatsDuplicateIEFrames_Type = PerfCounter64
_F3AccPortElmiStatsDuplicateIEFrames_Object = MibTableColumn
f3AccPortElmiStatsDuplicateIEFrames = _F3AccPortElmiStatsDuplicateIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 9),
    _F3AccPortElmiStatsDuplicateIEFrames_Type()
)
f3AccPortElmiStatsDuplicateIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsDuplicateIEFrames.setStatus("current")
_F3AccPortElmiStatsMissingMandatoryIEFrames_Type = PerfCounter64
_F3AccPortElmiStatsMissingMandatoryIEFrames_Object = MibTableColumn
f3AccPortElmiStatsMissingMandatoryIEFrames = _F3AccPortElmiStatsMissingMandatoryIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 10),
    _F3AccPortElmiStatsMissingMandatoryIEFrames_Type()
)
f3AccPortElmiStatsMissingMandatoryIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsMissingMandatoryIEFrames.setStatus("current")
_F3AccPortElmiStatsErroredMandatoryIEFrames_Type = PerfCounter64
_F3AccPortElmiStatsErroredMandatoryIEFrames_Object = MibTableColumn
f3AccPortElmiStatsErroredMandatoryIEFrames = _F3AccPortElmiStatsErroredMandatoryIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 11),
    _F3AccPortElmiStatsErroredMandatoryIEFrames_Type()
)
f3AccPortElmiStatsErroredMandatoryIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsErroredMandatoryIEFrames.setStatus("current")
_F3AccPortElmiStatsUnexpectedIEFrames_Type = PerfCounter64
_F3AccPortElmiStatsUnexpectedIEFrames_Object = MibTableColumn
f3AccPortElmiStatsUnexpectedIEFrames = _F3AccPortElmiStatsUnexpectedIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 12),
    _F3AccPortElmiStatsUnexpectedIEFrames_Type()
)
f3AccPortElmiStatsUnexpectedIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsUnexpectedIEFrames.setStatus("current")
_F3AccPortElmiStatsPVTExpirations_Type = PerfCounter64
_F3AccPortElmiStatsPVTExpirations_Object = MibTableColumn
f3AccPortElmiStatsPVTExpirations = _F3AccPortElmiStatsPVTExpirations_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 1, 1, 13),
    _F3AccPortElmiStatsPVTExpirations_Type()
)
f3AccPortElmiStatsPVTExpirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3AccPortElmiStatsPVTExpirations.setStatus("current")
_F3NetPortElmiStatsTable_Object = MibTable
f3NetPortElmiStatsTable = _F3NetPortElmiStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2)
)
if mibBuilder.loadTexts:
    f3NetPortElmiStatsTable.setStatus("current")
_F3NetPortElmiStatsEntry_Object = MibTableRow
f3NetPortElmiStatsEntry = _F3NetPortElmiStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1)
)
f3NetPortElmiStatsEntry.setIndexNames(
    (0, "CM-ENTITY-MIB", "neIndex"),
    (0, "CM-ENTITY-MIB", "shelfIndex"),
    (0, "CM-ENTITY-MIB", "slotIndex"),
    (0, "CM-FACILITY-MIB", "cmEthernetNetPortIndex"),
    (0, "F3-ELMI-MIB", "f3NetPortElmiConfigIndex"),
    (0, "F3-ELMI-MIB", "f3NetPortElmiStatsIndex"),
)
if mibBuilder.loadTexts:
    f3NetPortElmiStatsEntry.setStatus("current")
_F3NetPortElmiStatsIndex_Type = Integer32
_F3NetPortElmiStatsIndex_Object = MibTableColumn
f3NetPortElmiStatsIndex = _F3NetPortElmiStatsIndex_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 1),
    _F3NetPortElmiStatsIndex_Type()
)
f3NetPortElmiStatsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsIndex.setStatus("current")
_F3NetPortElmiStatsLastFullStatusSent_Type = TimeTicks
_F3NetPortElmiStatsLastFullStatusSent_Object = MibTableColumn
f3NetPortElmiStatsLastFullStatusSent = _F3NetPortElmiStatsLastFullStatusSent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 2),
    _F3NetPortElmiStatsLastFullStatusSent_Type()
)
f3NetPortElmiStatsLastFullStatusSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsLastFullStatusSent.setStatus("current")
_F3NetPortElmiStatsLastStatusCheckSent_Type = TimeTicks
_F3NetPortElmiStatsLastStatusCheckSent_Object = MibTableColumn
f3NetPortElmiStatsLastStatusCheckSent = _F3NetPortElmiStatsLastStatusCheckSent_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 3),
    _F3NetPortElmiStatsLastStatusCheckSent_Type()
)
f3NetPortElmiStatsLastStatusCheckSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsLastStatusCheckSent.setStatus("current")
_F3NetPortElmiStatsLastFullStatusReceived_Type = TimeTicks
_F3NetPortElmiStatsLastFullStatusReceived_Object = MibTableColumn
f3NetPortElmiStatsLastFullStatusReceived = _F3NetPortElmiStatsLastFullStatusReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 4),
    _F3NetPortElmiStatsLastFullStatusReceived_Type()
)
f3NetPortElmiStatsLastFullStatusReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsLastFullStatusReceived.setStatus("current")
_F3NetPortElmiStatsLastStatusCheckReceived_Type = TimeTicks
_F3NetPortElmiStatsLastStatusCheckReceived_Object = MibTableColumn
f3NetPortElmiStatsLastStatusCheckReceived = _F3NetPortElmiStatsLastStatusCheckReceived_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 5),
    _F3NetPortElmiStatsLastStatusCheckReceived_Type()
)
f3NetPortElmiStatsLastStatusCheckReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsLastStatusCheckReceived.setStatus("current")
_F3NetPortElmiStatsInvalidProtocolVersionFrames_Type = PerfCounter64
_F3NetPortElmiStatsInvalidProtocolVersionFrames_Object = MibTableColumn
f3NetPortElmiStatsInvalidProtocolVersionFrames = _F3NetPortElmiStatsInvalidProtocolVersionFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 6),
    _F3NetPortElmiStatsInvalidProtocolVersionFrames_Type()
)
f3NetPortElmiStatsInvalidProtocolVersionFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsInvalidProtocolVersionFrames.setStatus("current")
_F3NetPortElmiStatsInvalidMessageTypeFrames_Type = PerfCounter64
_F3NetPortElmiStatsInvalidMessageTypeFrames_Object = MibTableColumn
f3NetPortElmiStatsInvalidMessageTypeFrames = _F3NetPortElmiStatsInvalidMessageTypeFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 7),
    _F3NetPortElmiStatsInvalidMessageTypeFrames_Type()
)
f3NetPortElmiStatsInvalidMessageTypeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsInvalidMessageTypeFrames.setStatus("current")
_F3NetPortElmiStatsOutOfSequenceIEFrames_Type = PerfCounter64
_F3NetPortElmiStatsOutOfSequenceIEFrames_Object = MibTableColumn
f3NetPortElmiStatsOutOfSequenceIEFrames = _F3NetPortElmiStatsOutOfSequenceIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 8),
    _F3NetPortElmiStatsOutOfSequenceIEFrames_Type()
)
f3NetPortElmiStatsOutOfSequenceIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsOutOfSequenceIEFrames.setStatus("current")
_F3NetPortElmiStatsDuplicateIEFrames_Type = PerfCounter64
_F3NetPortElmiStatsDuplicateIEFrames_Object = MibTableColumn
f3NetPortElmiStatsDuplicateIEFrames = _F3NetPortElmiStatsDuplicateIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 9),
    _F3NetPortElmiStatsDuplicateIEFrames_Type()
)
f3NetPortElmiStatsDuplicateIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsDuplicateIEFrames.setStatus("current")
_F3NetPortElmiStatsMissingMandatoryIEFrames_Type = PerfCounter64
_F3NetPortElmiStatsMissingMandatoryIEFrames_Object = MibTableColumn
f3NetPortElmiStatsMissingMandatoryIEFrames = _F3NetPortElmiStatsMissingMandatoryIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 10),
    _F3NetPortElmiStatsMissingMandatoryIEFrames_Type()
)
f3NetPortElmiStatsMissingMandatoryIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsMissingMandatoryIEFrames.setStatus("current")
_F3NetPortElmiStatsErroredMandatoryIEFrames_Type = PerfCounter64
_F3NetPortElmiStatsErroredMandatoryIEFrames_Object = MibTableColumn
f3NetPortElmiStatsErroredMandatoryIEFrames = _F3NetPortElmiStatsErroredMandatoryIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 11),
    _F3NetPortElmiStatsErroredMandatoryIEFrames_Type()
)
f3NetPortElmiStatsErroredMandatoryIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsErroredMandatoryIEFrames.setStatus("current")
_F3NetPortElmiStatsUnexpectedIEFrames_Type = PerfCounter64
_F3NetPortElmiStatsUnexpectedIEFrames_Object = MibTableColumn
f3NetPortElmiStatsUnexpectedIEFrames = _F3NetPortElmiStatsUnexpectedIEFrames_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 12),
    _F3NetPortElmiStatsUnexpectedIEFrames_Type()
)
f3NetPortElmiStatsUnexpectedIEFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsUnexpectedIEFrames.setStatus("current")
_F3NetPortElmiStatsPVTExpirations_Type = PerfCounter64
_F3NetPortElmiStatsPVTExpirations_Object = MibTableColumn
f3NetPortElmiStatsPVTExpirations = _F3NetPortElmiStatsPVTExpirations_Object(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 2, 2, 1, 13),
    _F3NetPortElmiStatsPVTExpirations_Type()
)
f3NetPortElmiStatsPVTExpirations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    f3NetPortElmiStatsPVTExpirations.setStatus("current")
_F3ElmiConformance_ObjectIdentity = ObjectIdentity
f3ElmiConformance = _F3ElmiConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3)
)
_F3ElmiCompliances_ObjectIdentity = ObjectIdentity
f3ElmiCompliances = _F3ElmiCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 1)
)
_F3ElmiGroups_ObjectIdentity = ObjectIdentity
f3ElmiGroups = _F3ElmiGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 2)
)

# Managed Objects groups

f3ElmiConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 2, 1)
)
f3ElmiConfigGroup.setObjects(
      *(("F3-ELMI-MIB", "f3AccPortElmiConfigEnabled"),
        ("F3-ELMI-MIB", "f3AccPortElmiConfigOperationalState"),
        ("F3-ELMI-MIB", "f3AccPortElmiConfigN393StatusCounter"),
        ("F3-ELMI-MIB", "f3AccPortElmiConfigT392PollVerificationTimer"),
        ("F3-ELMI-MIB", "f3AccPortElmiConfigAsyncStatusEnabled"),
        ("F3-ELMI-MIB", "f3AccPortElmiConfigMinAsyncMessageInterval"),
        ("F3-ELMI-MIB", "f3NetPortElmiConfigEnabled"),
        ("F3-ELMI-MIB", "f3NetPortElmiConfigOperationalState"),
        ("F3-ELMI-MIB", "f3NetPortElmiConfigN393StatusCounter"),
        ("F3-ELMI-MIB", "f3NetPortElmiConfigT392PollVerificationTimer"),
        ("F3-ELMI-MIB", "f3NetPortElmiConfigAsyncStatusEnabled"),
        ("F3-ELMI-MIB", "f3NetPortElmiConfigMinAsyncMessageInterval"),
        ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcID"),
        ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcFlowID"),
        ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcStatus"),
        ("F3-ELMI-MIB", "f3ElmiEvcStatusInfoEvcType"))
)
if mibBuilder.loadTexts:
    f3ElmiConfigGroup.setStatus("current")

f3ElmiStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 2, 2)
)
f3ElmiStatsGroup.setObjects(
      *(("F3-ELMI-MIB", "f3AccPortElmiStatsLastFullStatusSent"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsLastStatusCheckSent"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsLastFullStatusReceived"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsLastStatusCheckReceived"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsInvalidProtocolVersionFrames"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsInvalidMessageTypeFrames"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsOutOfSequenceIEFrames"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsDuplicateIEFrames"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsMissingMandatoryIEFrames"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsErroredMandatoryIEFrames"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsUnexpectedIEFrames"),
        ("F3-ELMI-MIB", "f3AccPortElmiStatsPVTExpirations"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsLastFullStatusSent"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsLastStatusCheckSent"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsLastFullStatusReceived"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsLastStatusCheckReceived"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsInvalidProtocolVersionFrames"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsInvalidMessageTypeFrames"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsOutOfSequenceIEFrames"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsDuplicateIEFrames"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsMissingMandatoryIEFrames"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsErroredMandatoryIEFrames"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsUnexpectedIEFrames"),
        ("F3-ELMI-MIB", "f3NetPortElmiStatsPVTExpirations"))
)
if mibBuilder.loadTexts:
    f3ElmiStatsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

f3ElmiCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2544, 1, 12, 20, 3, 1, 1)
)
f3ElmiCompliance.setObjects(
      *(("F3-ELMI-MIB", "f3ElmiConfigGroup"),
        ("F3-ELMI-MIB", "f3ElmiStatsGroup"))
)
if mibBuilder.loadTexts:
    f3ElmiCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "F3-ELMI-MIB",
    **{"ELMIEvcStatus": ELMIEvcStatus,
       "ELMIEvcType": ELMIEvcType,
       "f3ElmiMIB": f3ElmiMIB,
       "f3ElmiConfigObjects": f3ElmiConfigObjects,
       "f3AccPortElmiConfigTable": f3AccPortElmiConfigTable,
       "f3AccPortElmiConfigEntry": f3AccPortElmiConfigEntry,
       "f3AccPortElmiConfigIndex": f3AccPortElmiConfigIndex,
       "f3AccPortElmiConfigEnabled": f3AccPortElmiConfigEnabled,
       "f3AccPortElmiConfigOperationalState": f3AccPortElmiConfigOperationalState,
       "f3AccPortElmiConfigN393StatusCounter": f3AccPortElmiConfigN393StatusCounter,
       "f3AccPortElmiConfigT392PollVerificationTimer": f3AccPortElmiConfigT392PollVerificationTimer,
       "f3AccPortElmiConfigAsyncStatusEnabled": f3AccPortElmiConfigAsyncStatusEnabled,
       "f3AccPortElmiConfigMinAsyncMessageInterval": f3AccPortElmiConfigMinAsyncMessageInterval,
       "f3NetPortElmiConfigTable": f3NetPortElmiConfigTable,
       "f3NetPortElmiConfigEntry": f3NetPortElmiConfigEntry,
       "f3NetPortElmiConfigIndex": f3NetPortElmiConfigIndex,
       "f3NetPortElmiConfigEnabled": f3NetPortElmiConfigEnabled,
       "f3NetPortElmiConfigOperationalState": f3NetPortElmiConfigOperationalState,
       "f3NetPortElmiConfigN393StatusCounter": f3NetPortElmiConfigN393StatusCounter,
       "f3NetPortElmiConfigT392PollVerificationTimer": f3NetPortElmiConfigT392PollVerificationTimer,
       "f3NetPortElmiConfigAsyncStatusEnabled": f3NetPortElmiConfigAsyncStatusEnabled,
       "f3NetPortElmiConfigMinAsyncMessageInterval": f3NetPortElmiConfigMinAsyncMessageInterval,
       "f3ElmiEvcStatusInfoTable": f3ElmiEvcStatusInfoTable,
       "f3ElmiEvcStatusInfoEntry": f3ElmiEvcStatusInfoEntry,
       "f3ElmiEvcStatusInfoEvcID": f3ElmiEvcStatusInfoEvcID,
       "f3ElmiEvcStatusInfoEvcFlowID": f3ElmiEvcStatusInfoEvcFlowID,
       "f3ElmiEvcStatusInfoEvcStatus": f3ElmiEvcStatusInfoEvcStatus,
       "f3ElmiEvcStatusInfoEvcType": f3ElmiEvcStatusInfoEvcType,
       "f3ElmiStatsObjects": f3ElmiStatsObjects,
       "f3AccPortElmiStatsTable": f3AccPortElmiStatsTable,
       "f3AccPortElmiStatsEntry": f3AccPortElmiStatsEntry,
       "f3AccPortElmiStatsIndex": f3AccPortElmiStatsIndex,
       "f3AccPortElmiStatsLastFullStatusSent": f3AccPortElmiStatsLastFullStatusSent,
       "f3AccPortElmiStatsLastStatusCheckSent": f3AccPortElmiStatsLastStatusCheckSent,
       "f3AccPortElmiStatsLastFullStatusReceived": f3AccPortElmiStatsLastFullStatusReceived,
       "f3AccPortElmiStatsLastStatusCheckReceived": f3AccPortElmiStatsLastStatusCheckReceived,
       "f3AccPortElmiStatsInvalidProtocolVersionFrames": f3AccPortElmiStatsInvalidProtocolVersionFrames,
       "f3AccPortElmiStatsInvalidMessageTypeFrames": f3AccPortElmiStatsInvalidMessageTypeFrames,
       "f3AccPortElmiStatsOutOfSequenceIEFrames": f3AccPortElmiStatsOutOfSequenceIEFrames,
       "f3AccPortElmiStatsDuplicateIEFrames": f3AccPortElmiStatsDuplicateIEFrames,
       "f3AccPortElmiStatsMissingMandatoryIEFrames": f3AccPortElmiStatsMissingMandatoryIEFrames,
       "f3AccPortElmiStatsErroredMandatoryIEFrames": f3AccPortElmiStatsErroredMandatoryIEFrames,
       "f3AccPortElmiStatsUnexpectedIEFrames": f3AccPortElmiStatsUnexpectedIEFrames,
       "f3AccPortElmiStatsPVTExpirations": f3AccPortElmiStatsPVTExpirations,
       "f3NetPortElmiStatsTable": f3NetPortElmiStatsTable,
       "f3NetPortElmiStatsEntry": f3NetPortElmiStatsEntry,
       "f3NetPortElmiStatsIndex": f3NetPortElmiStatsIndex,
       "f3NetPortElmiStatsLastFullStatusSent": f3NetPortElmiStatsLastFullStatusSent,
       "f3NetPortElmiStatsLastStatusCheckSent": f3NetPortElmiStatsLastStatusCheckSent,
       "f3NetPortElmiStatsLastFullStatusReceived": f3NetPortElmiStatsLastFullStatusReceived,
       "f3NetPortElmiStatsLastStatusCheckReceived": f3NetPortElmiStatsLastStatusCheckReceived,
       "f3NetPortElmiStatsInvalidProtocolVersionFrames": f3NetPortElmiStatsInvalidProtocolVersionFrames,
       "f3NetPortElmiStatsInvalidMessageTypeFrames": f3NetPortElmiStatsInvalidMessageTypeFrames,
       "f3NetPortElmiStatsOutOfSequenceIEFrames": f3NetPortElmiStatsOutOfSequenceIEFrames,
       "f3NetPortElmiStatsDuplicateIEFrames": f3NetPortElmiStatsDuplicateIEFrames,
       "f3NetPortElmiStatsMissingMandatoryIEFrames": f3NetPortElmiStatsMissingMandatoryIEFrames,
       "f3NetPortElmiStatsErroredMandatoryIEFrames": f3NetPortElmiStatsErroredMandatoryIEFrames,
       "f3NetPortElmiStatsUnexpectedIEFrames": f3NetPortElmiStatsUnexpectedIEFrames,
       "f3NetPortElmiStatsPVTExpirations": f3NetPortElmiStatsPVTExpirations,
       "f3ElmiConformance": f3ElmiConformance,
       "f3ElmiCompliances": f3ElmiCompliances,
       "f3ElmiCompliance": f3ElmiCompliance,
       "f3ElmiGroups": f3ElmiGroups,
       "f3ElmiConfigGroup": f3ElmiConfigGroup,
       "f3ElmiStatsGroup": f3ElmiStatsGroup}
)
