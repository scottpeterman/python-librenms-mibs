# SNMP MIB module (Juniper-REDUNDANCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\junose\Juniper-REDUNDANCY-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:07:33 2025
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

(juniMibs,) = mibBuilder.importSymbols(
    "Juniper-MIBs",
    "juniMibs")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysUpTime,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysUpTime")

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


# MODULE-IDENTITY

juniRedundancyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74)
)
if mibBuilder.loadTexts:
    juniRedundancyMIB.setRevisions(
        ("2003-12-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class JuniRedundancyState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("notKnown", 1),
          ("fileSystemSyncing", 2),
          ("disabled", 3),
          ("initializing", 4),
          ("pending", 5),
          ("active", 6))
    )



class JuniRedundancyMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fileSystemSynchronization", 1),
          ("highAvailability", 2))
    )



class JuniRedundancyResetReason(TextualConvention, Integer32):
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
        *(("none", 1),
          ("notKnown", 2),
          ("userInitiated", 3))
    )



class JuniRedundancySystemActivationType(TextualConvention, Integer32):
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
        *(("reload", 1),
          ("coldSwitch", 2),
          ("warmSwitch", 3))
    )



class JuniRedundancyResetType(TextualConvention, Integer32):
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
        *(("notKnown", 1),
          ("srpReload", 2),
          ("srpSwitchover", 3),
          ("linecardReload", 4),
          ("linecardSwitchover", 5))
    )



class JuniRedundancyHistoryCommand(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keep", 1),
          ("clear", 2))
    )



# MIB Managed Objects in the order of their OIDs

_JuniRedundancyNotifications_ObjectIdentity = ObjectIdentity
juniRedundancyNotifications = _JuniRedundancyNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0)
)
_JuniRedundancyObjects_ObjectIdentity = ObjectIdentity
juniRedundancyObjects = _JuniRedundancyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1)
)
_JuniRedundancyStatus_ObjectIdentity = ObjectIdentity
juniRedundancyStatus = _JuniRedundancyStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1)
)


class _JuniRedundancyActiveSlot_Type(Integer32):
    """Custom type juniRedundancyActiveSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniRedundancyActiveSlot_Type.__name__ = "Integer32"
_JuniRedundancyActiveSlot_Object = MibScalar
juniRedundancyActiveSlot = _JuniRedundancyActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 1),
    _JuniRedundancyActiveSlot_Type()
)
juniRedundancyActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyActiveSlot.setStatus("current")
_JuniRedundancyActiveSlotState_Type = JuniRedundancyState
_JuniRedundancyActiveSlotState_Object = MibScalar
juniRedundancyActiveSlotState = _JuniRedundancyActiveSlotState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 2),
    _JuniRedundancyActiveSlotState_Type()
)
juniRedundancyActiveSlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyActiveSlotState.setStatus("current")


class _JuniRedundancyStandbySlot_Type(Integer32):
    """Custom type juniRedundancyStandbySlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniRedundancyStandbySlot_Type.__name__ = "Integer32"
_JuniRedundancyStandbySlot_Object = MibScalar
juniRedundancyStandbySlot = _JuniRedundancyStandbySlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 3),
    _JuniRedundancyStandbySlot_Type()
)
juniRedundancyStandbySlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyStandbySlot.setStatus("current")
_JuniRedundancyStandbySlotState_Type = JuniRedundancyState
_JuniRedundancyStandbySlotState_Object = MibScalar
juniRedundancyStandbySlotState = _JuniRedundancyStandbySlotState_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 4),
    _JuniRedundancyStandbySlotState_Type()
)
juniRedundancyStandbySlotState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyStandbySlotState.setStatus("current")
_JuniRedundancyLastResetReason_Type = JuniRedundancyResetReason
_JuniRedundancyLastResetReason_Object = MibScalar
juniRedundancyLastResetReason = _JuniRedundancyLastResetReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 5),
    _JuniRedundancyLastResetReason_Type()
)
juniRedundancyLastResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyLastResetReason.setStatus("current")
_JuniRedundancyLastSystemActivationTime_Type = TimeTicks
_JuniRedundancyLastSystemActivationTime_Object = MibScalar
juniRedundancyLastSystemActivationTime = _JuniRedundancyLastSystemActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 6),
    _JuniRedundancyLastSystemActivationTime_Type()
)
juniRedundancyLastSystemActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyLastSystemActivationTime.setStatus("current")
_JuniRedundancyLastSystemActivationType_Type = JuniRedundancySystemActivationType
_JuniRedundancyLastSystemActivationType_Object = MibScalar
juniRedundancyLastSystemActivationType = _JuniRedundancyLastSystemActivationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 7),
    _JuniRedundancyLastSystemActivationType_Type()
)
juniRedundancyLastSystemActivationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyLastSystemActivationType.setStatus("current")
_JuniRedundancyHaActiveTime_Type = TimeTicks
_JuniRedundancyHaActiveTime_Object = MibScalar
juniRedundancyHaActiveTime = _JuniRedundancyHaActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 1, 8),
    _JuniRedundancyHaActiveTime_Type()
)
juniRedundancyHaActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHaActiveTime.setStatus("current")
_JuniRedundancyCfg_ObjectIdentity = ObjectIdentity
juniRedundancyCfg = _JuniRedundancyCfg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2)
)


class _JuniRedundancyNotifsEnabled_Type(TruthValue):
    """Custom type juniRedundancyNotifsEnabled based on TruthValue"""
    defaultValue = 1


_JuniRedundancyNotifsEnabled_Type.__name__ = "TruthValue"
_JuniRedundancyNotifsEnabled_Object = MibScalar
juniRedundancyNotifsEnabled = _JuniRedundancyNotifsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2, 1),
    _JuniRedundancyNotifsEnabled_Type()
)
juniRedundancyNotifsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRedundancyNotifsEnabled.setStatus("current")


class _JuniRedundancyCfgRedundancyMode_Type(JuniRedundancyMode):
    """Custom type juniRedundancyCfgRedundancyMode based on JuniRedundancyMode"""
    defaultValue = 1


_JuniRedundancyCfgRedundancyMode_Type.__name__ = "JuniRedundancyMode"
_JuniRedundancyCfgRedundancyMode_Object = MibScalar
juniRedundancyCfgRedundancyMode = _JuniRedundancyCfgRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 2, 2),
    _JuniRedundancyCfgRedundancyMode_Type()
)
juniRedundancyCfgRedundancyMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRedundancyCfgRedundancyMode.setStatus("current")
_JuniRedundancyHistory_ObjectIdentity = ObjectIdentity
juniRedundancyHistory = _JuniRedundancyHistory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3)
)


class _JuniRedundancySystemActivationHistoryTableMaxLength_Type(Integer32):
    """Custom type juniRedundancySystemActivationHistoryTableMaxLength based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 50),
    )


_JuniRedundancySystemActivationHistoryTableMaxLength_Type.__name__ = "Integer32"
_JuniRedundancySystemActivationHistoryTableMaxLength_Object = MibScalar
juniRedundancySystemActivationHistoryTableMaxLength = _JuniRedundancySystemActivationHistoryTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 1),
    _JuniRedundancySystemActivationHistoryTableMaxLength_Type()
)
juniRedundancySystemActivationHistoryTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRedundancySystemActivationHistoryTableMaxLength.setStatus("current")


class _JuniRedundancySystemActivationHistoryCommand_Type(JuniRedundancyHistoryCommand):
    """Custom type juniRedundancySystemActivationHistoryCommand based on JuniRedundancyHistoryCommand"""
    defaultValue = 1


_JuniRedundancySystemActivationHistoryCommand_Type.__name__ = "JuniRedundancyHistoryCommand"
_JuniRedundancySystemActivationHistoryCommand_Object = MibScalar
juniRedundancySystemActivationHistoryCommand = _JuniRedundancySystemActivationHistoryCommand_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 2),
    _JuniRedundancySystemActivationHistoryCommand_Type()
)
juniRedundancySystemActivationHistoryCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    juniRedundancySystemActivationHistoryCommand.setStatus("current")
_JuniRedundancySystemActivationHistoryTable_Object = MibTable
juniRedundancySystemActivationHistoryTable = _JuniRedundancySystemActivationHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3)
)
if mibBuilder.loadTexts:
    juniRedundancySystemActivationHistoryTable.setStatus("current")
_JuniRedundancySystemActivationHistoryEntry_Object = MibTableRow
juniRedundancySystemActivationHistoryEntry = _JuniRedundancySystemActivationHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1)
)
juniRedundancySystemActivationHistoryEntry.setIndexNames(
    (0, "Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryIndex"),
)
if mibBuilder.loadTexts:
    juniRedundancySystemActivationHistoryEntry.setStatus("current")
_JuniRedundancySystemActivationHistoryIndex_Type = Integer32
_JuniRedundancySystemActivationHistoryIndex_Object = MibTableColumn
juniRedundancySystemActivationHistoryIndex = _JuniRedundancySystemActivationHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 1),
    _JuniRedundancySystemActivationHistoryIndex_Type()
)
juniRedundancySystemActivationHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    juniRedundancySystemActivationHistoryIndex.setStatus("current")
_JuniRedundancyHistoryResetType_Type = JuniRedundancyResetType
_JuniRedundancyHistoryResetType_Object = MibTableColumn
juniRedundancyHistoryResetType = _JuniRedundancyHistoryResetType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 2),
    _JuniRedundancyHistoryResetType_Type()
)
juniRedundancyHistoryResetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryResetType.setStatus("current")
_JuniRedundancyHistoryActivationType_Type = JuniRedundancySystemActivationType
_JuniRedundancyHistoryActivationType_Object = MibTableColumn
juniRedundancyHistoryActivationType = _JuniRedundancyHistoryActivationType_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 3),
    _JuniRedundancyHistoryActivationType_Type()
)
juniRedundancyHistoryActivationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryActivationType.setStatus("current")


class _JuniRedundancyHistoryPrevActiveSlot_Type(Integer32):
    """Custom type juniRedundancyHistoryPrevActiveSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniRedundancyHistoryPrevActiveSlot_Type.__name__ = "Integer32"
_JuniRedundancyHistoryPrevActiveSlot_Object = MibTableColumn
juniRedundancyHistoryPrevActiveSlot = _JuniRedundancyHistoryPrevActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 4),
    _JuniRedundancyHistoryPrevActiveSlot_Type()
)
juniRedundancyHistoryPrevActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryPrevActiveSlot.setStatus("current")
_JuniRedundancyHistoryPrevActiveRelease_Type = DisplayString
_JuniRedundancyHistoryPrevActiveRelease_Object = MibTableColumn
juniRedundancyHistoryPrevActiveRelease = _JuniRedundancyHistoryPrevActiveRelease_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 5),
    _JuniRedundancyHistoryPrevActiveRelease_Type()
)
juniRedundancyHistoryPrevActiveRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryPrevActiveRelease.setStatus("current")


class _JuniRedundancyHistoryCurrActiveSlot_Type(Integer32):
    """Custom type juniRedundancyHistoryCurrActiveSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_JuniRedundancyHistoryCurrActiveSlot_Type.__name__ = "Integer32"
_JuniRedundancyHistoryCurrActiveSlot_Object = MibTableColumn
juniRedundancyHistoryCurrActiveSlot = _JuniRedundancyHistoryCurrActiveSlot_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 6),
    _JuniRedundancyHistoryCurrActiveSlot_Type()
)
juniRedundancyHistoryCurrActiveSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryCurrActiveSlot.setStatus("current")
_JuniRedundancyHistoryCurrActiveRelease_Type = DisplayString
_JuniRedundancyHistoryCurrActiveRelease_Object = MibTableColumn
juniRedundancyHistoryCurrActiveRelease = _JuniRedundancyHistoryCurrActiveRelease_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 7),
    _JuniRedundancyHistoryCurrActiveRelease_Type()
)
juniRedundancyHistoryCurrActiveRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryCurrActiveRelease.setStatus("current")
_JuniRedundancyHistoryResetReason_Type = JuniRedundancyResetReason
_JuniRedundancyHistoryResetReason_Object = MibTableColumn
juniRedundancyHistoryResetReason = _JuniRedundancyHistoryResetReason_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 8),
    _JuniRedundancyHistoryResetReason_Type()
)
juniRedundancyHistoryResetReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryResetReason.setStatus("current")
_JuniRedundancyHistoryActivationTime_Type = DateAndTime
_JuniRedundancyHistoryActivationTime_Object = MibTableColumn
juniRedundancyHistoryActivationTime = _JuniRedundancyHistoryActivationTime_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 3, 1, 9),
    _JuniRedundancyHistoryActivationTime_Type()
)
juniRedundancyHistoryActivationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryActivationTime.setStatus("current")
_JuniRedundancyHistoryReloads_Type = Integer32
_JuniRedundancyHistoryReloads_Object = MibScalar
juniRedundancyHistoryReloads = _JuniRedundancyHistoryReloads_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 4),
    _JuniRedundancyHistoryReloads_Type()
)
juniRedundancyHistoryReloads.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryReloads.setStatus("current")
_JuniRedundancyHistoryColdSwitchovers_Type = Integer32
_JuniRedundancyHistoryColdSwitchovers_Object = MibScalar
juniRedundancyHistoryColdSwitchovers = _JuniRedundancyHistoryColdSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 5),
    _JuniRedundancyHistoryColdSwitchovers_Type()
)
juniRedundancyHistoryColdSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryColdSwitchovers.setStatus("current")
_JuniRedundancyHistoryWarmSwitchovers_Type = Integer32
_JuniRedundancyHistoryWarmSwitchovers_Object = MibScalar
juniRedundancyHistoryWarmSwitchovers = _JuniRedundancyHistoryWarmSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 1, 3, 6),
    _JuniRedundancyHistoryWarmSwitchovers_Type()
)
juniRedundancyHistoryWarmSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    juniRedundancyHistoryWarmSwitchovers.setStatus("current")
_JuniRedundancyMIBConformance_ObjectIdentity = ObjectIdentity
juniRedundancyMIBConformance = _JuniRedundancyMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2)
)
_JuniRedundancyMIBCompliances_ObjectIdentity = ObjectIdentity
juniRedundancyMIBCompliances = _JuniRedundancyMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 1)
)
_JuniRedundancyMIBGroups_ObjectIdentity = ObjectIdentity
juniRedundancyMIBGroups = _JuniRedundancyMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2)
)

# Managed Objects groups

juniRedundancyStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 1)
)
juniRedundancyStatusGroup.setObjects(
      *(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlotState"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyStandbySlot"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyStandbySlotState"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastSystemActivationTime"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastSystemActivationType"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHaActiveTime"))
)
if mibBuilder.loadTexts:
    juniRedundancyStatusGroup.setStatus("current")

juniRedundancyCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 2)
)
juniRedundancyCfgGroup.setObjects(
      *(("Juniper-REDUNDANCY-MIB", "juniRedundancyNotifsEnabled"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgRedundancyMode"))
)
if mibBuilder.loadTexts:
    juniRedundancyCfgGroup.setStatus("current")

juniRedundancyHistoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 3)
)
juniRedundancyHistoryGroup.setObjects(
      *(("Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryTableMaxLength"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancySystemActivationHistoryCommand"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryResetType"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryActivationType"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryPrevActiveSlot"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryPrevActiveRelease"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryCurrActiveSlot"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryCurrActiveRelease"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryResetReason"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryActivationTime"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryReloads"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryColdSwitchovers"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryWarmSwitchovers"))
)
if mibBuilder.loadTexts:
    juniRedundancyHistoryGroup.setStatus("current")


# Notification objects

juniRedundancyColdSwitchoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 1)
)
juniRedundancyColdSwitchoverNotification.setObjects(
      *(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"))
)
if mibBuilder.loadTexts:
    juniRedundancyColdSwitchoverNotification.setStatus(
        "current"
    )

juniRedundancyWarmSwitchoverNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 2)
)
juniRedundancyWarmSwitchoverNotification.setObjects(
      *(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyLastResetReason"))
)
if mibBuilder.loadTexts:
    juniRedundancyWarmSwitchoverNotification.setStatus(
        "current"
    )

juniRedundancyStateEnabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 3)
)
juniRedundancyStateEnabledNotification.setObjects(
    ("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot")
)
if mibBuilder.loadTexts:
    juniRedundancyStateEnabledNotification.setStatus(
        "current"
    )

juniRedundancyStateDisabledNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 4)
)
juniRedundancyStateDisabledNotification.setObjects(
    ("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot")
)
if mibBuilder.loadTexts:
    juniRedundancyStateDisabledNotification.setStatus(
        "current"
    )

juniRedundancyStatePendingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 5)
)
juniRedundancyStatePendingNotification.setObjects(
    ("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot")
)
if mibBuilder.loadTexts:
    juniRedundancyStatePendingNotification.setStatus(
        "current"
    )

juniRedundancyModeNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 0, 6)
)
juniRedundancyModeNotification.setObjects(
      *(("Juniper-REDUNDANCY-MIB", "juniRedundancyActiveSlot"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgRedundancyMode"))
)
if mibBuilder.loadTexts:
    juniRedundancyModeNotification.setStatus(
        "current"
    )


# Notifications groups

juniRedundancyNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 2, 4)
)
juniRedundancyNotificationGroup.setObjects(
      *(("Juniper-REDUNDANCY-MIB", "juniRedundancyColdSwitchoverNotification"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyWarmSwitchoverNotification"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyStateEnabledNotification"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyStateDisabledNotification"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyStatePendingNotification"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyModeNotification"))
)
if mibBuilder.loadTexts:
    juniRedundancyNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

juniRedundancyMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4874, 2, 2, 74, 2, 1, 1)
)
juniRedundancyMIBCompliance.setObjects(
      *(("Juniper-REDUNDANCY-MIB", "juniRedundancyStatusGroup"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyCfgGroup"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyHistoryGroup"),
        ("Juniper-REDUNDANCY-MIB", "juniRedundancyNotificationGroup"))
)
if mibBuilder.loadTexts:
    juniRedundancyMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Juniper-REDUNDANCY-MIB",
    **{"JuniRedundancyState": JuniRedundancyState,
       "JuniRedundancyMode": JuniRedundancyMode,
       "JuniRedundancyResetReason": JuniRedundancyResetReason,
       "JuniRedundancySystemActivationType": JuniRedundancySystemActivationType,
       "JuniRedundancyResetType": JuniRedundancyResetType,
       "JuniRedundancyHistoryCommand": JuniRedundancyHistoryCommand,
       "juniRedundancyMIB": juniRedundancyMIB,
       "juniRedundancyNotifications": juniRedundancyNotifications,
       "juniRedundancyColdSwitchoverNotification": juniRedundancyColdSwitchoverNotification,
       "juniRedundancyWarmSwitchoverNotification": juniRedundancyWarmSwitchoverNotification,
       "juniRedundancyStateEnabledNotification": juniRedundancyStateEnabledNotification,
       "juniRedundancyStateDisabledNotification": juniRedundancyStateDisabledNotification,
       "juniRedundancyStatePendingNotification": juniRedundancyStatePendingNotification,
       "juniRedundancyModeNotification": juniRedundancyModeNotification,
       "juniRedundancyObjects": juniRedundancyObjects,
       "juniRedundancyStatus": juniRedundancyStatus,
       "juniRedundancyActiveSlot": juniRedundancyActiveSlot,
       "juniRedundancyActiveSlotState": juniRedundancyActiveSlotState,
       "juniRedundancyStandbySlot": juniRedundancyStandbySlot,
       "juniRedundancyStandbySlotState": juniRedundancyStandbySlotState,
       "juniRedundancyLastResetReason": juniRedundancyLastResetReason,
       "juniRedundancyLastSystemActivationTime": juniRedundancyLastSystemActivationTime,
       "juniRedundancyLastSystemActivationType": juniRedundancyLastSystemActivationType,
       "juniRedundancyHaActiveTime": juniRedundancyHaActiveTime,
       "juniRedundancyCfg": juniRedundancyCfg,
       "juniRedundancyNotifsEnabled": juniRedundancyNotifsEnabled,
       "juniRedundancyCfgRedundancyMode": juniRedundancyCfgRedundancyMode,
       "juniRedundancyHistory": juniRedundancyHistory,
       "juniRedundancySystemActivationHistoryTableMaxLength": juniRedundancySystemActivationHistoryTableMaxLength,
       "juniRedundancySystemActivationHistoryCommand": juniRedundancySystemActivationHistoryCommand,
       "juniRedundancySystemActivationHistoryTable": juniRedundancySystemActivationHistoryTable,
       "juniRedundancySystemActivationHistoryEntry": juniRedundancySystemActivationHistoryEntry,
       "juniRedundancySystemActivationHistoryIndex": juniRedundancySystemActivationHistoryIndex,
       "juniRedundancyHistoryResetType": juniRedundancyHistoryResetType,
       "juniRedundancyHistoryActivationType": juniRedundancyHistoryActivationType,
       "juniRedundancyHistoryPrevActiveSlot": juniRedundancyHistoryPrevActiveSlot,
       "juniRedundancyHistoryPrevActiveRelease": juniRedundancyHistoryPrevActiveRelease,
       "juniRedundancyHistoryCurrActiveSlot": juniRedundancyHistoryCurrActiveSlot,
       "juniRedundancyHistoryCurrActiveRelease": juniRedundancyHistoryCurrActiveRelease,
       "juniRedundancyHistoryResetReason": juniRedundancyHistoryResetReason,
       "juniRedundancyHistoryActivationTime": juniRedundancyHistoryActivationTime,
       "juniRedundancyHistoryReloads": juniRedundancyHistoryReloads,
       "juniRedundancyHistoryColdSwitchovers": juniRedundancyHistoryColdSwitchovers,
       "juniRedundancyHistoryWarmSwitchovers": juniRedundancyHistoryWarmSwitchovers,
       "juniRedundancyMIBConformance": juniRedundancyMIBConformance,
       "juniRedundancyMIBCompliances": juniRedundancyMIBCompliances,
       "juniRedundancyMIBCompliance": juniRedundancyMIBCompliance,
       "juniRedundancyMIBGroups": juniRedundancyMIBGroups,
       "juniRedundancyStatusGroup": juniRedundancyStatusGroup,
       "juniRedundancyCfgGroup": juniRedundancyCfgGroup,
       "juniRedundancyHistoryGroup": juniRedundancyHistoryGroup,
       "juniRedundancyNotificationGroup": juniRedundancyNotificationGroup}
)
