# SNMP MIB module (SL-OPT-APS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\packetlight\SL-OPT-APS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:57 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

(slmTrapLogId,) = mibBuilder.importSymbols(
    "SL-MAIN-MIB",
    "slmTrapLogId")

(sitelight,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "sitelight")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
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

slOptApsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlOptApsConfig_ObjectIdentity = ObjectIdentity
slOptApsConfig = _SlOptApsConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1)
)
_OptApsConfigTable_Object = MibTable
optApsConfigTable = _OptApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    optApsConfigTable.setStatus("current")
_OptApsConfigEntry_Object = MibTableRow
optApsConfigEntry = _OptApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1)
)
optApsConfigEntry.setIndexNames(
    (0, "SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"),
)
if mibBuilder.loadTexts:
    optApsConfigEntry.setStatus("current")
_OptApsConfigUserWorkingIndex_Type = InterfaceIndex
_OptApsConfigUserWorkingIndex_Object = MibTableColumn
optApsConfigUserWorkingIndex = _OptApsConfigUserWorkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 1),
    _OptApsConfigUserWorkingIndex_Type()
)
optApsConfigUserWorkingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigUserWorkingIndex.setStatus("current")
_OptApsConfigNetWorkingIndex_Type = InterfaceIndex
_OptApsConfigNetWorkingIndex_Object = MibTableColumn
optApsConfigNetWorkingIndex = _OptApsConfigNetWorkingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 2),
    _OptApsConfigNetWorkingIndex_Type()
)
optApsConfigNetWorkingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigNetWorkingIndex.setStatus("current")
_OptApsConfigUserProtectingIndex_Type = InterfaceIndex
_OptApsConfigUserProtectingIndex_Object = MibTableColumn
optApsConfigUserProtectingIndex = _OptApsConfigUserProtectingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 3),
    _OptApsConfigUserProtectingIndex_Type()
)
optApsConfigUserProtectingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigUserProtectingIndex.setStatus("current")
_OptApsConfigNetProtectingIndex_Type = InterfaceIndex
_OptApsConfigNetProtectingIndex_Object = MibTableColumn
optApsConfigNetProtectingIndex = _OptApsConfigNetProtectingIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 4),
    _OptApsConfigNetProtectingIndex_Type()
)
optApsConfigNetProtectingIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigNetProtectingIndex.setStatus("current")


class _OptApsConfigScheme_Type(Integer32):
    """Custom type optApsConfigScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("equipment", 1),
          ("facility", 2))
    )


_OptApsConfigScheme_Type.__name__ = "Integer32"
_OptApsConfigScheme_Object = MibTableColumn
optApsConfigScheme = _OptApsConfigScheme_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 5),
    _OptApsConfigScheme_Type()
)
optApsConfigScheme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigScheme.setStatus("current")


class _OptApsConfigEnable_Type(Integer32):
    """Custom type optApsConfigEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optApsDisabled", 1),
          ("optApsEnabled", 2))
    )


_OptApsConfigEnable_Type.__name__ = "Integer32"
_OptApsConfigEnable_Object = MibTableColumn
optApsConfigEnable = _OptApsConfigEnable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 6),
    _OptApsConfigEnable_Type()
)
optApsConfigEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigEnable.setStatus("current")


class _OptApsConfigArchMode_Type(Integer32):
    """Custom type optApsConfigArchMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onePlusOne", 1),
          ("oneToOne", 2))
    )


_OptApsConfigArchMode_Type.__name__ = "Integer32"
_OptApsConfigArchMode_Object = MibTableColumn
optApsConfigArchMode = _OptApsConfigArchMode_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 7),
    _OptApsConfigArchMode_Type()
)
optApsConfigArchMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigArchMode.setStatus("current")


class _OptApsConfigActiveConnectionRx_Type(Integer32):
    """Custom type optApsConfigActiveConnectionRx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optApsWorkingConnection", 1),
          ("optApsProtectionConnection", 2))
    )


_OptApsConfigActiveConnectionRx_Type.__name__ = "Integer32"
_OptApsConfigActiveConnectionRx_Object = MibTableColumn
optApsConfigActiveConnectionRx = _OptApsConfigActiveConnectionRx_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 8),
    _OptApsConfigActiveConnectionRx_Type()
)
optApsConfigActiveConnectionRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optApsConfigActiveConnectionRx.setStatus("current")


class _OptApsConfigActiveConnectionTx_Type(Integer32):
    """Custom type optApsConfigActiveConnectionTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("optApsWorkingConnection", 1),
          ("optApsProtectionConnection", 2))
    )


_OptApsConfigActiveConnectionTx_Type.__name__ = "Integer32"
_OptApsConfigActiveConnectionTx_Object = MibTableColumn
optApsConfigActiveConnectionTx = _OptApsConfigActiveConnectionTx_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 9),
    _OptApsConfigActiveConnectionTx_Type()
)
optApsConfigActiveConnectionTx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optApsConfigActiveConnectionTx.setStatus("current")


class _OptApsConfigWaitToRestore_Type(Unsigned32):
    """Custom type optApsConfigWaitToRestore based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_OptApsConfigWaitToRestore_Type.__name__ = "Unsigned32"
_OptApsConfigWaitToRestore_Object = MibTableColumn
optApsConfigWaitToRestore = _OptApsConfigWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 10),
    _OptApsConfigWaitToRestore_Type()
)
optApsConfigWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    optApsConfigWaitToRestore.setUnits("minutes")


class _OptApsConfigDirection_Type(Integer32):
    """Custom type optApsConfigDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("uniDirectional", 1),
          ("biDirectional", 2))
    )


_OptApsConfigDirection_Type.__name__ = "Integer32"
_OptApsConfigDirection_Object = MibTableColumn
optApsConfigDirection = _OptApsConfigDirection_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 11),
    _OptApsConfigDirection_Type()
)
optApsConfigDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigDirection.setStatus("current")


class _OptApsConfigRevertive_Type(Integer32):
    """Custom type optApsConfigRevertive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonrevertive", 1),
          ("revertive", 2))
    )


_OptApsConfigRevertive_Type.__name__ = "Integer32"
_OptApsConfigRevertive_Object = MibTableColumn
optApsConfigRevertive = _OptApsConfigRevertive_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 12),
    _OptApsConfigRevertive_Type()
)
optApsConfigRevertive.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigRevertive.setStatus("current")


class _OptApsConfigChanStatus_Type(Bits):
    """Custom type optApsConfigChanStatus based on Bits"""
    namedValues = NamedValues(
        *(("lockedOut", 0),
          ("sfWorking", 1),
          ("sfProtecting", 2),
          ("switched", 3),
          ("lockedOutRemote", 4))
    )

_OptApsConfigChanStatus_Type.__name__ = "Bits"
_OptApsConfigChanStatus_Object = MibTableColumn
optApsConfigChanStatus = _OptApsConfigChanStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 13),
    _OptApsConfigChanStatus_Type()
)
optApsConfigChanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optApsConfigChanStatus.setStatus("current")
_OptApsConfigChanSignalFailures_Type = Counter32
_OptApsConfigChanSignalFailures_Object = MibTableColumn
optApsConfigChanSignalFailures = _OptApsConfigChanSignalFailures_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 14),
    _OptApsConfigChanSignalFailures_Type()
)
optApsConfigChanSignalFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optApsConfigChanSignalFailures.setStatus("current")
_OptApsConfigChanSwitchovers_Type = Counter32
_OptApsConfigChanSwitchovers_Object = MibTableColumn
optApsConfigChanSwitchovers = _OptApsConfigChanSwitchovers_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 15),
    _OptApsConfigChanSwitchovers_Type()
)
optApsConfigChanSwitchovers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optApsConfigChanSwitchovers.setStatus("current")
_OptApsConfigChanLastSwitchover_Type = TimeTicks
_OptApsConfigChanLastSwitchover_Object = MibTableColumn
optApsConfigChanLastSwitchover = _OptApsConfigChanLastSwitchover_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 16),
    _OptApsConfigChanLastSwitchover_Type()
)
optApsConfigChanLastSwitchover.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optApsConfigChanLastSwitchover.setStatus("current")


class _OptApsConfigSwitchCommand_Type(Integer32):
    """Custom type optApsConfigSwitchCommand based on Integer32"""
    defaultValue = 1

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
        *(("clear", 1),
          ("lockoutOfProtection", 2),
          ("forcedSwitchOfWorking", 3),
          ("forcedSwitchOfProtection", 4),
          ("manualSwitchOfWorking", 5),
          ("manualSwitchOfProtection", 6))
    )


_OptApsConfigSwitchCommand_Type.__name__ = "Integer32"
_OptApsConfigSwitchCommand_Object = MibTableColumn
optApsConfigSwitchCommand = _OptApsConfigSwitchCommand_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 17),
    _OptApsConfigSwitchCommand_Type()
)
optApsConfigSwitchCommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigSwitchCommand.setStatus("current")


class _OptApsConfigSwitchReason_Type(Integer32):
    """Custom type optApsConfigSwitchReason based on Integer32"""
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
        *(("optApsOther", 1),
          ("optApsRevertive", 2),
          ("optApsManual", 3),
          ("optApsSignalFailure", 4),
          ("optApsForceSwitch", 5),
          ("optApsLockOut", 6))
    )


_OptApsConfigSwitchReason_Type.__name__ = "Integer32"
_OptApsConfigSwitchReason_Object = MibTableColumn
optApsConfigSwitchReason = _OptApsConfigSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 18),
    _OptApsConfigSwitchReason_Type()
)
optApsConfigSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optApsConfigSwitchReason.setStatus("current")


class _OptApsConfigResetCounters_Type(Integer32):
    """Custom type optApsConfigResetCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetCounters", 1)
    )


_OptApsConfigResetCounters_Type.__name__ = "Integer32"
_OptApsConfigResetCounters_Object = MibTableColumn
optApsConfigResetCounters = _OptApsConfigResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 19),
    _OptApsConfigResetCounters_Type()
)
optApsConfigResetCounters.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigResetCounters.setStatus("current")


class _OptApsConfigActiveRequest_Type(Integer32):
    """Custom type optApsConfigActiveRequest based on Integer32"""
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
        *(("optApsOther", 1),
          ("optApsRevertive", 2),
          ("optApsManual", 3),
          ("optApsSignalFailure", 4),
          ("optApsForceSwitch", 5),
          ("optApsLockOut", 6))
    )


_OptApsConfigActiveRequest_Type.__name__ = "Integer32"
_OptApsConfigActiveRequest_Object = MibTableColumn
optApsConfigActiveRequest = _OptApsConfigActiveRequest_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 20),
    _OptApsConfigActiveRequest_Type()
)
optApsConfigActiveRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    optApsConfigActiveRequest.setStatus("current")
_OptApsConfigStatus_Type = RowStatus
_OptApsConfigStatus_Object = MibTableColumn
optApsConfigStatus = _OptApsConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 21),
    _OptApsConfigStatus_Type()
)
optApsConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    optApsConfigStatus.setStatus("current")


class _OptApsConfigLosThreshold_Type(Integer32):
    """Custom type optApsConfigLosThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OptApsConfigLosThreshold_Type.__name__ = "Integer32"
_OptApsConfigLosThreshold_Object = MibTableColumn
optApsConfigLosThreshold = _OptApsConfigLosThreshold_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 1, 1, 22),
    _OptApsConfigLosThreshold_Type()
)
optApsConfigLosThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    optApsConfigLosThreshold.setStatus("current")
_EqptApsConfigTable_Object = MibTable
eqptApsConfigTable = _EqptApsConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    eqptApsConfigTable.setStatus("current")
_EqptApsConfigEntry_Object = MibTableRow
eqptApsConfigEntry = _EqptApsConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1)
)
eqptApsConfigEntry.setIndexNames(
    (0, "SL-OPT-APS-MIB", "eqptApsConfigDummyIndex"),
)
if mibBuilder.loadTexts:
    eqptApsConfigEntry.setStatus("current")
_EqptApsConfigDummyIndex_Type = Integer32
_EqptApsConfigDummyIndex_Object = MibTableColumn
eqptApsConfigDummyIndex = _EqptApsConfigDummyIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 1),
    _EqptApsConfigDummyIndex_Type()
)
eqptApsConfigDummyIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eqptApsConfigDummyIndex.setStatus("current")


class _EqptApsConfigRole_Type(Integer32):
    """Custom type eqptApsConfigRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eqptApsWorkingRole", 1),
          ("eqptApsProtectionRole", 2))
    )


_EqptApsConfigRole_Type.__name__ = "Integer32"
_EqptApsConfigRole_Object = MibTableColumn
eqptApsConfigRole = _EqptApsConfigRole_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 2),
    _EqptApsConfigRole_Type()
)
eqptApsConfigRole.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqptApsConfigRole.setStatus("current")
_EqptApsConfigMate_Type = IpAddress
_EqptApsConfigMate_Object = MibTableColumn
eqptApsConfigMate = _EqptApsConfigMate_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 3),
    _EqptApsConfigMate_Type()
)
eqptApsConfigMate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqptApsConfigMate.setStatus("current")


class _EqptApsConfigLinkStatus_Type(Integer32):
    """Custom type eqptApsConfigLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("eqptApsLinkUp", 1),
          ("eqptApsLinkDown", 2))
    )


_EqptApsConfigLinkStatus_Type.__name__ = "Integer32"
_EqptApsConfigLinkStatus_Object = MibTableColumn
eqptApsConfigLinkStatus = _EqptApsConfigLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 1, 2, 1, 4),
    _EqptApsConfigLinkStatus_Type()
)
eqptApsConfigLinkStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eqptApsConfigLinkStatus.setStatus("current")
_SlOptApsTraps_ObjectIdentity = ObjectIdentity
slOptApsTraps = _SlOptApsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 2)
)
_SlOptApsTraps0_ObjectIdentity = ObjectIdentity
slOptApsTraps0 = _SlOptApsTraps0_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 0)
)

# Managed Objects groups


# Notification objects

optApsTrapSwitchover0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 0, 1)
)
optApsTrapSwitchover0.setObjects(
      *(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"),
        ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"),
        ("SL-MAIN-MIB", "slmTrapLogId"))
)
if mibBuilder.loadTexts:
    optApsTrapSwitchover0.setStatus(
        "current"
    )

optApsConfigTableChanged0 = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 0, 2)
)
optApsConfigTableChanged0.setObjects(
      *(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"),
        ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"),
        ("SL-MAIN-MIB", "slmTrapLogId"))
)
if mibBuilder.loadTexts:
    optApsConfigTableChanged0.setStatus(
        "current"
    )

optApsTrapSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 1)
)
optApsTrapSwitchover.setObjects(
      *(("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex"),
        ("SL-OPT-APS-MIB", "optApsConfigActiveConnectionRx"))
)
if mibBuilder.loadTexts:
    optApsTrapSwitchover.setStatus(
        "current"
    )

optApsConfigTableChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4515, 1, 11, 2, 2)
)
optApsConfigTableChanged.setObjects(
    ("SL-OPT-APS-MIB", "optApsConfigUserWorkingIndex")
)
if mibBuilder.loadTexts:
    optApsConfigTableChanged.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-OPT-APS-MIB",
    **{"slOptApsMib": slOptApsMib,
       "slOptApsConfig": slOptApsConfig,
       "optApsConfigTable": optApsConfigTable,
       "optApsConfigEntry": optApsConfigEntry,
       "optApsConfigUserWorkingIndex": optApsConfigUserWorkingIndex,
       "optApsConfigNetWorkingIndex": optApsConfigNetWorkingIndex,
       "optApsConfigUserProtectingIndex": optApsConfigUserProtectingIndex,
       "optApsConfigNetProtectingIndex": optApsConfigNetProtectingIndex,
       "optApsConfigScheme": optApsConfigScheme,
       "optApsConfigEnable": optApsConfigEnable,
       "optApsConfigArchMode": optApsConfigArchMode,
       "optApsConfigActiveConnectionRx": optApsConfigActiveConnectionRx,
       "optApsConfigActiveConnectionTx": optApsConfigActiveConnectionTx,
       "optApsConfigWaitToRestore": optApsConfigWaitToRestore,
       "optApsConfigDirection": optApsConfigDirection,
       "optApsConfigRevertive": optApsConfigRevertive,
       "optApsConfigChanStatus": optApsConfigChanStatus,
       "optApsConfigChanSignalFailures": optApsConfigChanSignalFailures,
       "optApsConfigChanSwitchovers": optApsConfigChanSwitchovers,
       "optApsConfigChanLastSwitchover": optApsConfigChanLastSwitchover,
       "optApsConfigSwitchCommand": optApsConfigSwitchCommand,
       "optApsConfigSwitchReason": optApsConfigSwitchReason,
       "optApsConfigResetCounters": optApsConfigResetCounters,
       "optApsConfigActiveRequest": optApsConfigActiveRequest,
       "optApsConfigStatus": optApsConfigStatus,
       "optApsConfigLosThreshold": optApsConfigLosThreshold,
       "eqptApsConfigTable": eqptApsConfigTable,
       "eqptApsConfigEntry": eqptApsConfigEntry,
       "eqptApsConfigDummyIndex": eqptApsConfigDummyIndex,
       "eqptApsConfigRole": eqptApsConfigRole,
       "eqptApsConfigMate": eqptApsConfigMate,
       "eqptApsConfigLinkStatus": eqptApsConfigLinkStatus,
       "slOptApsTraps": slOptApsTraps,
       "slOptApsTraps0": slOptApsTraps0,
       "optApsTrapSwitchover0": optApsTrapSwitchover0,
       "optApsConfigTableChanged0": optApsConfigTableChanged0,
       "optApsTrapSwitchover": optApsTrapSwitchover,
       "optApsConfigTableChanged": optApsConfigTableChanged}
)
