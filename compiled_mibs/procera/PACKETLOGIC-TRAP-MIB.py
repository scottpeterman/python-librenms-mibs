# SNMP MIB module (PACKETLOGIC-TRAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\procera\PACKETLOGIC-TRAP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:21:29 2025
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

(CounterBasedGauge64,) = mibBuilder.importSymbols(
    "HCNUM-TC",
    "CounterBasedGauge64")

(packetlogic2,) = mibBuilder.importSymbols(
    "PACKETLOGIC-MIB",
    "packetlogic2")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

pl2Trap = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8)
)
if mibBuilder.loadTexts:
    pl2Trap.setRevisions(
        ("2019-09-12 15:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Pl2Traps_ObjectIdentity = ObjectIdentity
pl2Traps = _Pl2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0)
)
_Pl2TrapVals_ObjectIdentity = ObjectIdentity
pl2TrapVals = _Pl2TrapVals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1)
)
_Pl2TrapMessage_Type = DisplayString
_Pl2TrapMessage_Object = MibScalar
pl2TrapMessage = _Pl2TrapMessage_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 1),
    _Pl2TrapMessage_Type()
)
pl2TrapMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapMessage.setStatus("current")
_Pl2TrapOid_Type = ObjectIdentifier
_Pl2TrapOid_Object = MibScalar
pl2TrapOid = _Pl2TrapOid_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 2),
    _Pl2TrapOid_Type()
)
pl2TrapOid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapOid.setStatus("current")
_Pl2TrapValue_Type = Unsigned32
_Pl2TrapValue_Object = MibScalar
pl2TrapValue = _Pl2TrapValue_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 3),
    _Pl2TrapValue_Type()
)
pl2TrapValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapValue.setStatus("current")
_Pl2TrapThreshold_Type = Unsigned32
_Pl2TrapThreshold_Object = MibScalar
pl2TrapThreshold = _Pl2TrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 4),
    _Pl2TrapThreshold_Type()
)
pl2TrapThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapThreshold.setStatus("current")
_Pl2TrapValue64_Type = Counter64
_Pl2TrapValue64_Object = MibScalar
pl2TrapValue64 = _Pl2TrapValue64_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 5),
    _Pl2TrapValue64_Type()
)
pl2TrapValue64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapValue64.setStatus("current")
_Pl2TrapThreshold64_Type = Counter64
_Pl2TrapThreshold64_Object = MibScalar
pl2TrapThreshold64 = _Pl2TrapThreshold64_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 1, 6),
    _Pl2TrapThreshold64_Type()
)
pl2TrapThreshold64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2TrapThreshold64.setStatus("current")
_Pl2ChannelTraps_ObjectIdentity = ObjectIdentity
pl2ChannelTraps = _Pl2ChannelTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 2)
)
_Pl2ChannelTrapVals_ObjectIdentity = ObjectIdentity
pl2ChannelTrapVals = _Pl2ChannelTrapVals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3)
)
_ChannelIndex_Type = Unsigned32
_ChannelIndex_Object = MibScalar
channelIndex = _ChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 1),
    _ChannelIndex_Type()
)
channelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelIndex.setStatus("current")
_ChannelDescr_Type = DisplayString
_ChannelDescr_Object = MibScalar
channelDescr = _ChannelDescr_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 2),
    _ChannelDescr_Type()
)
channelDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelDescr.setStatus("current")


class _ChannelPort_Type(Integer32):
    """Custom type channelPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("external", 0),
          ("internal", 1))
    )


_ChannelPort_Type.__name__ = "Integer32"
_ChannelPort_Object = MibScalar
channelPort = _ChannelPort_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 3),
    _ChannelPort_Type()
)
channelPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelPort.setStatus("current")


class _PrevState_Type(Integer32):
    """Custom type prevState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("hd-10", 1),
          ("fd-10", 2),
          ("hd-100", 3),
          ("fd-100", 4),
          ("fd-1000", 5),
          ("fd-10000", 6),
          ("fd-40000", 7),
          ("fd-100000", 8))
    )


_PrevState_Type.__name__ = "Integer32"
_PrevState_Object = MibScalar
prevState = _PrevState_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 4),
    _PrevState_Type()
)
prevState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    prevState.setStatus("current")


class _NewState_Type(Integer32):
    """Custom type newState based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 0),
          ("hd-10", 1),
          ("fd-10", 2),
          ("hd-100", 3),
          ("fd-100", 4),
          ("fd-1000", 5),
          ("fd-10000", 6),
          ("fd-40000", 7),
          ("fd-100000", 8))
    )


_NewState_Type.__name__ = "Integer32"
_NewState_Object = MibScalar
newState = _NewState_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 3, 5),
    _NewState_Type()
)
newState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    newState.setStatus("current")
_Pl2StorageTrapVals_ObjectIdentity = ObjectIdentity
pl2StorageTrapVals = _Pl2StorageTrapVals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 4)
)
_Pl2ContentLogicTraps_ObjectIdentity = ObjectIdentity
pl2ContentLogicTraps = _Pl2ContentLogicTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5)
)
_Pl2ContentLogicHourlyUpdateTraps_ObjectIdentity = ObjectIdentity
pl2ContentLogicHourlyUpdateTraps = _Pl2ContentLogicHourlyUpdateTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 1)
)
_Pl2ContentLogicCategoriesLoadingTraps_ObjectIdentity = ObjectIdentity
pl2ContentLogicCategoriesLoadingTraps = _Pl2ContentLogicCategoriesLoadingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 2)
)
_Pl2ContentLogicDatabaseUpdateTraps_ObjectIdentity = ObjectIdentity
pl2ContentLogicDatabaseUpdateTraps = _Pl2ContentLogicDatabaseUpdateTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 3)
)
_Pl2ContentLogicDatabaseLoadingTraps_ObjectIdentity = ObjectIdentity
pl2ContentLogicDatabaseLoadingTraps = _Pl2ContentLogicDatabaseLoadingTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 4)
)
_Pl2ContentLogicTrapVals_ObjectIdentity = ObjectIdentity
pl2ContentLogicTrapVals = _Pl2ContentLogicTrapVals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 6)
)
_Pl2ContentLogicDatabase_Type = DisplayString
_Pl2ContentLogicDatabase_Object = MibScalar
pl2ContentLogicDatabase = _Pl2ContentLogicDatabase_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 6, 1),
    _Pl2ContentLogicDatabase_Type()
)
pl2ContentLogicDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2ContentLogicDatabase.setStatus("current")
_Pl2ContentLogicReason_Type = DisplayString
_Pl2ContentLogicReason_Object = MibScalar
pl2ContentLogicReason = _Pl2ContentLogicReason_Object(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 6, 2),
    _Pl2ContentLogicReason_Type()
)
pl2ContentLogicReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pl2ContentLogicReason.setStatus("current")

# Managed Objects groups


# Notification objects

pl2TrapGenericMsg = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 1)
)
pl2TrapGenericMsg.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage")
)
if mibBuilder.loadTexts:
    pl2TrapGenericMsg.setStatus(
        "current"
    )

pl2TrapGeneric = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 2)
)
if mibBuilder.loadTexts:
    pl2TrapGeneric.setStatus(
        "current"
    )

pl2TrapSystemStatsAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 3)
)
pl2TrapSystemStatsAlert.setObjects(
      *(("PACKETLOGIC-TRAP-MIB", "pl2TrapThreshold"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapValue"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapOid"))
)
if mibBuilder.loadTexts:
    pl2TrapSystemStatsAlert.setStatus(
        "current"
    )

pl2TrapSystemStatsAlert64 = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 4)
)
pl2TrapSystemStatsAlert64.setObjects(
      *(("PACKETLOGIC-TRAP-MIB", "pl2TrapThreshold64"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapValue64"),
        ("PACKETLOGIC-TRAP-MIB", "pl2TrapOid"))
)
if mibBuilder.loadTexts:
    pl2TrapSystemStatsAlert64.setStatus(
        "current"
    )

pl2TrapSystemStatsAlertClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 0, 5)
)
pl2TrapSystemStatsAlertClear.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2TrapOid")
)
if mibBuilder.loadTexts:
    pl2TrapSystemStatsAlertClear.setStatus(
        "current"
    )

pl2ChannelStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 2, 1)
)
pl2ChannelStateChanged.setObjects(
      *(("PACKETLOGIC-TRAP-MIB", "channelIndex"),
        ("PACKETLOGIC-TRAP-MIB", "channelDescr"),
        ("PACKETLOGIC-TRAP-MIB", "channelPort"),
        ("PACKETLOGIC-TRAP-MIB", "newState"),
        ("PACKETLOGIC-TRAP-MIB", "prevState"))
)
if mibBuilder.loadTexts:
    pl2ChannelStateChanged.setStatus(
        "current"
    )

pl2StorageGenericTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 1)
)
pl2StorageGenericTrap.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage")
)
if mibBuilder.loadTexts:
    pl2StorageGenericTrap.setStatus(
        "current"
    )

pl2StorageBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 2)
)
pl2StorageBattery.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage")
)
if mibBuilder.loadTexts:
    pl2StorageBattery.setStatus(
        "current"
    )

pl2StoragePowerSupply = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 3)
)
pl2StoragePowerSupply.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage")
)
if mibBuilder.loadTexts:
    pl2StoragePowerSupply.setStatus(
        "current"
    )

pl2StoragePhysicalDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 4)
)
pl2StoragePhysicalDisk.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage")
)
if mibBuilder.loadTexts:
    pl2StoragePhysicalDisk.setStatus(
        "current"
    )

pl2StorageVirtualDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 4, 5)
)
pl2StorageVirtualDisk.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2TrapMessage")
)
if mibBuilder.loadTexts:
    pl2StorageVirtualDisk.setStatus(
        "current"
    )

pl2ContentLogicHourlyUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 1, 1)
)
if mibBuilder.loadTexts:
    pl2ContentLogicHourlyUpdateStarted.setStatus(
        "current"
    )

pl2ContentLogicHourlyUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 1, 2)
)
if mibBuilder.loadTexts:
    pl2ContentLogicHourlyUpdateCompleted.setStatus(
        "current"
    )

pl2ContentLogicHourlyUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 1, 3)
)
pl2ContentLogicHourlyUpdateFailed.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicReason")
)
if mibBuilder.loadTexts:
    pl2ContentLogicHourlyUpdateFailed.setStatus(
        "current"
    )

pl2ContentLogicCategoriesLoadingStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 2, 1)
)
pl2ContentLogicCategoriesLoadingStarted.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase")
)
if mibBuilder.loadTexts:
    pl2ContentLogicCategoriesLoadingStarted.setStatus(
        "current"
    )

pl2ContentLogicCategoriesLoadingCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 2, 2)
)
pl2ContentLogicCategoriesLoadingCompleted.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase")
)
if mibBuilder.loadTexts:
    pl2ContentLogicCategoriesLoadingCompleted.setStatus(
        "current"
    )

pl2ContentLogicCategoriesLoadingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 2, 3)
)
pl2ContentLogicCategoriesLoadingFailed.setObjects(
      *(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"),
        ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicReason"))
)
if mibBuilder.loadTexts:
    pl2ContentLogicCategoriesLoadingFailed.setStatus(
        "current"
    )

pl2ContentLogicDatabaseUpdateStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 3, 1)
)
pl2ContentLogicDatabaseUpdateStarted.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase")
)
if mibBuilder.loadTexts:
    pl2ContentLogicDatabaseUpdateStarted.setStatus(
        "current"
    )

pl2ContentLogicDatabaseUpdateCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 3, 2)
)
pl2ContentLogicDatabaseUpdateCompleted.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase")
)
if mibBuilder.loadTexts:
    pl2ContentLogicDatabaseUpdateCompleted.setStatus(
        "current"
    )

pl2ContentLogicDatabaseUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 3, 3)
)
pl2ContentLogicDatabaseUpdateFailed.setObjects(
      *(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"),
        ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicReason"))
)
if mibBuilder.loadTexts:
    pl2ContentLogicDatabaseUpdateFailed.setStatus(
        "current"
    )

pl2ContentLogicDatabaseLoadingStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 4, 1)
)
pl2ContentLogicDatabaseLoadingStarted.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase")
)
if mibBuilder.loadTexts:
    pl2ContentLogicDatabaseLoadingStarted.setStatus(
        "current"
    )

pl2ContentLogicDatabaseLoadingCompleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 4, 2)
)
pl2ContentLogicDatabaseLoadingCompleted.setObjects(
    ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase")
)
if mibBuilder.loadTexts:
    pl2ContentLogicDatabaseLoadingCompleted.setStatus(
        "current"
    )

pl2ContentLogicDatabaseLoadingFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 15397, 2, 8, 5, 4, 3)
)
pl2ContentLogicDatabaseLoadingFailed.setObjects(
      *(("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicDatabase"),
        ("PACKETLOGIC-TRAP-MIB", "pl2ContentLogicReason"))
)
if mibBuilder.loadTexts:
    pl2ContentLogicDatabaseLoadingFailed.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PACKETLOGIC-TRAP-MIB",
    **{"pl2Trap": pl2Trap,
       "pl2Traps": pl2Traps,
       "pl2TrapGenericMsg": pl2TrapGenericMsg,
       "pl2TrapGeneric": pl2TrapGeneric,
       "pl2TrapSystemStatsAlert": pl2TrapSystemStatsAlert,
       "pl2TrapSystemStatsAlert64": pl2TrapSystemStatsAlert64,
       "pl2TrapSystemStatsAlertClear": pl2TrapSystemStatsAlertClear,
       "pl2TrapVals": pl2TrapVals,
       "pl2TrapMessage": pl2TrapMessage,
       "pl2TrapOid": pl2TrapOid,
       "pl2TrapValue": pl2TrapValue,
       "pl2TrapThreshold": pl2TrapThreshold,
       "pl2TrapValue64": pl2TrapValue64,
       "pl2TrapThreshold64": pl2TrapThreshold64,
       "pl2ChannelTraps": pl2ChannelTraps,
       "pl2ChannelStateChanged": pl2ChannelStateChanged,
       "pl2ChannelTrapVals": pl2ChannelTrapVals,
       "channelIndex": channelIndex,
       "channelDescr": channelDescr,
       "channelPort": channelPort,
       "prevState": prevState,
       "newState": newState,
       "pl2StorageTrapVals": pl2StorageTrapVals,
       "pl2StorageGenericTrap": pl2StorageGenericTrap,
       "pl2StorageBattery": pl2StorageBattery,
       "pl2StoragePowerSupply": pl2StoragePowerSupply,
       "pl2StoragePhysicalDisk": pl2StoragePhysicalDisk,
       "pl2StorageVirtualDisk": pl2StorageVirtualDisk,
       "pl2ContentLogicTraps": pl2ContentLogicTraps,
       "pl2ContentLogicHourlyUpdateTraps": pl2ContentLogicHourlyUpdateTraps,
       "pl2ContentLogicHourlyUpdateStarted": pl2ContentLogicHourlyUpdateStarted,
       "pl2ContentLogicHourlyUpdateCompleted": pl2ContentLogicHourlyUpdateCompleted,
       "pl2ContentLogicHourlyUpdateFailed": pl2ContentLogicHourlyUpdateFailed,
       "pl2ContentLogicCategoriesLoadingTraps": pl2ContentLogicCategoriesLoadingTraps,
       "pl2ContentLogicCategoriesLoadingStarted": pl2ContentLogicCategoriesLoadingStarted,
       "pl2ContentLogicCategoriesLoadingCompleted": pl2ContentLogicCategoriesLoadingCompleted,
       "pl2ContentLogicCategoriesLoadingFailed": pl2ContentLogicCategoriesLoadingFailed,
       "pl2ContentLogicDatabaseUpdateTraps": pl2ContentLogicDatabaseUpdateTraps,
       "pl2ContentLogicDatabaseUpdateStarted": pl2ContentLogicDatabaseUpdateStarted,
       "pl2ContentLogicDatabaseUpdateCompleted": pl2ContentLogicDatabaseUpdateCompleted,
       "pl2ContentLogicDatabaseUpdateFailed": pl2ContentLogicDatabaseUpdateFailed,
       "pl2ContentLogicDatabaseLoadingTraps": pl2ContentLogicDatabaseLoadingTraps,
       "pl2ContentLogicDatabaseLoadingStarted": pl2ContentLogicDatabaseLoadingStarted,
       "pl2ContentLogicDatabaseLoadingCompleted": pl2ContentLogicDatabaseLoadingCompleted,
       "pl2ContentLogicDatabaseLoadingFailed": pl2ContentLogicDatabaseLoadingFailed,
       "pl2ContentLogicTrapVals": pl2ContentLogicTrapVals,
       "pl2ContentLogicDatabase": pl2ContentLogicDatabase,
       "pl2ContentLogicReason": pl2ContentLogicReason}
)
