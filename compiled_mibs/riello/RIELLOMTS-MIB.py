# SNMP MIB module (RIELLOMTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\riello\RIELLOMTS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:25 2025
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

(rielloMIB,) = mibBuilder.importSymbols(
    "RIELLO-MIB",
    "rielloMIB")

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
 NotificationType,
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
    "NotificationType",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MtsMIB_ObjectIdentity = ObjectIdentity
mtsMIB = _MtsMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5491, 12)
)
_MtsIdent_ObjectIdentity = ObjectIdentity
mtsIdent = _MtsIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1)
)
_MtsIdentManufacturer_Type = DisplayString
_MtsIdentManufacturer_Object = MibScalar
mtsIdentManufacturer = _MtsIdentManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 1),
    _MtsIdentManufacturer_Type()
)
mtsIdentManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentManufacturer.setStatus("mandatory")
_MtsIdentModel_Type = DisplayString
_MtsIdentModel_Object = MibScalar
mtsIdentModel = _MtsIdentModel_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 2),
    _MtsIdentModel_Type()
)
mtsIdentModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentModel.setStatus("mandatory")
_MtsIdentSoftwareVersion_Type = DisplayString
_MtsIdentSoftwareVersion_Object = MibScalar
mtsIdentSoftwareVersion = _MtsIdentSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 3),
    _MtsIdentSoftwareVersion_Type()
)
mtsIdentSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentSoftwareVersion.setStatus("mandatory")
_MtsIdentIOConfiguration_Type = Integer32
_MtsIdentIOConfiguration_Object = MibScalar
mtsIdentIOConfiguration = _MtsIdentIOConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 4),
    _MtsIdentIOConfiguration_Type()
)
mtsIdentIOConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentIOConfiguration.setStatus("mandatory")
_MtsIdentType_Type = Integer32
_MtsIdentType_Object = MibScalar
mtsIdentType = _MtsIdentType_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 5),
    _MtsIdentType_Type()
)
mtsIdentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentType.setStatus("mandatory")
_MtsIdentInputSockets_Type = Integer32
_MtsIdentInputSockets_Object = MibScalar
mtsIdentInputSockets = _MtsIdentInputSockets_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 6),
    _MtsIdentInputSockets_Type()
)
mtsIdentInputSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentInputSockets.setStatus("mandatory")
_MtsIdentOutputSockets_Type = Integer32
_MtsIdentOutputSockets_Object = MibScalar
mtsIdentOutputSockets = _MtsIdentOutputSockets_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 7),
    _MtsIdentOutputSockets_Type()
)
mtsIdentOutputSockets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentOutputSockets.setStatus("mandatory")
_MtsIdentNominalCurrent_Type = Integer32
_MtsIdentNominalCurrent_Object = MibScalar
mtsIdentNominalCurrent = _MtsIdentNominalCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 8),
    _MtsIdentNominalCurrent_Type()
)
mtsIdentNominalCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentNominalCurrent.setStatus("mandatory")
_MtsIdentNominalVoltage_Type = Integer32
_MtsIdentNominalVoltage_Object = MibScalar
mtsIdentNominalVoltage = _MtsIdentNominalVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 9),
    _MtsIdentNominalVoltage_Type()
)
mtsIdentNominalVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentNominalVoltage.setStatus("mandatory")
_MtsIdentNominalFrequency_Type = Integer32
_MtsIdentNominalFrequency_Object = MibScalar
mtsIdentNominalFrequency = _MtsIdentNominalFrequency_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 1, 10),
    _MtsIdentNominalFrequency_Type()
)
mtsIdentNominalFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsIdentNominalFrequency.setStatus("mandatory")
_MtsStatus_ObjectIdentity = ObjectIdentity
mtsStatus = _MtsStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2)
)
_MtsS1Frequency_Type = Integer32
_MtsS1Frequency_Object = MibScalar
mtsS1Frequency = _MtsS1Frequency_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 1),
    _MtsS1Frequency_Type()
)
mtsS1Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1Frequency.setStatus("mandatory")
_MtsS1VoltageL1_Type = Integer32
_MtsS1VoltageL1_Object = MibScalar
mtsS1VoltageL1 = _MtsS1VoltageL1_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 2),
    _MtsS1VoltageL1_Type()
)
mtsS1VoltageL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1VoltageL1.setStatus("mandatory")
_MtsS1VoltageL2_Type = Integer32
_MtsS1VoltageL2_Object = MibScalar
mtsS1VoltageL2 = _MtsS1VoltageL2_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 3),
    _MtsS1VoltageL2_Type()
)
mtsS1VoltageL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1VoltageL2.setStatus("mandatory")
_MtsS1VoltageL3_Type = Integer32
_MtsS1VoltageL3_Object = MibScalar
mtsS1VoltageL3 = _MtsS1VoltageL3_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 4),
    _MtsS1VoltageL3_Type()
)
mtsS1VoltageL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1VoltageL3.setStatus("mandatory")
_MtsS2Frequency_Type = Integer32
_MtsS2Frequency_Object = MibScalar
mtsS2Frequency = _MtsS2Frequency_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 5),
    _MtsS2Frequency_Type()
)
mtsS2Frequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2Frequency.setStatus("mandatory")
_MtsS2VoltageL1_Type = Integer32
_MtsS2VoltageL1_Object = MibScalar
mtsS2VoltageL1 = _MtsS2VoltageL1_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 6),
    _MtsS2VoltageL1_Type()
)
mtsS2VoltageL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2VoltageL1.setStatus("mandatory")
_MtsS2VoltageL2_Type = Integer32
_MtsS2VoltageL2_Object = MibScalar
mtsS2VoltageL2 = _MtsS2VoltageL2_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 7),
    _MtsS2VoltageL2_Type()
)
mtsS2VoltageL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2VoltageL2.setStatus("mandatory")
_MtsS2VoltageL3_Type = Integer32
_MtsS2VoltageL3_Object = MibScalar
mtsS2VoltageL3 = _MtsS2VoltageL3_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 8),
    _MtsS2VoltageL3_Type()
)
mtsS2VoltageL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2VoltageL3.setStatus("mandatory")
_MtsPhaseDifference_Type = Integer32
_MtsPhaseDifference_Object = MibScalar
mtsPhaseDifference = _MtsPhaseDifference_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 9),
    _MtsPhaseDifference_Type()
)
mtsPhaseDifference.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsPhaseDifference.setStatus("mandatory")
_MtsLoadL1_Type = Integer32
_MtsLoadL1_Object = MibScalar
mtsLoadL1 = _MtsLoadL1_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 10),
    _MtsLoadL1_Type()
)
mtsLoadL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsLoadL1.setStatus("mandatory")
_MtsLoadL2_Type = Integer32
_MtsLoadL2_Object = MibScalar
mtsLoadL2 = _MtsLoadL2_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 11),
    _MtsLoadL2_Type()
)
mtsLoadL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsLoadL2.setStatus("mandatory")
_MtsLoadL3_Type = Integer32
_MtsLoadL3_Object = MibScalar
mtsLoadL3 = _MtsLoadL3_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 12),
    _MtsLoadL3_Type()
)
mtsLoadL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsLoadL3.setStatus("mandatory")
_MtsOutputCurrentL1_Type = Integer32
_MtsOutputCurrentL1_Object = MibScalar
mtsOutputCurrentL1 = _MtsOutputCurrentL1_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 13),
    _MtsOutputCurrentL1_Type()
)
mtsOutputCurrentL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsOutputCurrentL1.setStatus("mandatory")
_MtsOutputCurrentL2_Type = Integer32
_MtsOutputCurrentL2_Object = MibScalar
mtsOutputCurrentL2 = _MtsOutputCurrentL2_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 14),
    _MtsOutputCurrentL2_Type()
)
mtsOutputCurrentL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsOutputCurrentL2.setStatus("mandatory")
_MtsOutputCurrentL3_Type = Integer32
_MtsOutputCurrentL3_Object = MibScalar
mtsOutputCurrentL3 = _MtsOutputCurrentL3_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 15),
    _MtsOutputCurrentL3_Type()
)
mtsOutputCurrentL3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsOutputCurrentL3.setStatus("mandatory")
_MtsTemperature_Type = Integer32
_MtsTemperature_Object = MibScalar
mtsTemperature = _MtsTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 16),
    _MtsTemperature_Type()
)
mtsTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsTemperature.setStatus("mandatory")
_MtsSoundOff_Type = Integer32
_MtsSoundOff_Object = MibScalar
mtsSoundOff = _MtsSoundOff_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 17),
    _MtsSoundOff_Type()
)
mtsSoundOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsSoundOff.setStatus("mandatory")
_MtsTestInProgress_Type = Integer32
_MtsTestInProgress_Object = MibScalar
mtsTestInProgress = _MtsTestInProgress_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 18),
    _MtsTestInProgress_Type()
)
mtsTestInProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsTestInProgress.setStatus("mandatory")
_MtsAuxPower2fail_Type = Integer32
_MtsAuxPower2fail_Object = MibScalar
mtsAuxPower2fail = _MtsAuxPower2fail_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 19),
    _MtsAuxPower2fail_Type()
)
mtsAuxPower2fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsAuxPower2fail.setStatus("mandatory")
_MtsAuxPower1fail_Type = Integer32
_MtsAuxPower1fail_Object = MibScalar
mtsAuxPower1fail = _MtsAuxPower1fail_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 20),
    _MtsAuxPower1fail_Type()
)
mtsAuxPower1fail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsAuxPower1fail.setStatus("mandatory")
_MtsSynchrobad_Type = Integer32
_MtsSynchrobad_Object = MibScalar
mtsSynchrobad = _MtsSynchrobad_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 21),
    _MtsSynchrobad_Type()
)
mtsSynchrobad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsSynchrobad.setStatus("mandatory")
_MtsPreferredSource_Type = Integer32
_MtsPreferredSource_Object = MibScalar
mtsPreferredSource = _MtsPreferredSource_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 22),
    _MtsPreferredSource_Type()
)
mtsPreferredSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsPreferredSource.setStatus("mandatory")
_MtsTransferhinibit_Type = Integer32
_MtsTransferhinibit_Object = MibScalar
mtsTransferhinibit = _MtsTransferhinibit_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 23),
    _MtsTransferhinibit_Type()
)
mtsTransferhinibit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsTransferhinibit.setStatus("mandatory")
_MtsNonSynchInibit_Type = Integer32
_MtsNonSynchInibit_Object = MibScalar
mtsNonSynchInibit = _MtsNonSynchInibit_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 24),
    _MtsNonSynchInibit_Type()
)
mtsNonSynchInibit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsNonSynchInibit.setStatus("mandatory")
_MtsSourceS2bad_Type = Integer32
_MtsSourceS2bad_Object = MibScalar
mtsSourceS2bad = _MtsSourceS2bad_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 25),
    _MtsSourceS2bad_Type()
)
mtsSourceS2bad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsSourceS2bad.setStatus("mandatory")
_MtsSourceS1bad_Type = Integer32
_MtsSourceS1bad_Object = MibScalar
mtsSourceS1bad = _MtsSourceS1bad_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 26),
    _MtsSourceS1bad_Type()
)
mtsSourceS1bad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsSourceS1bad.setStatus("mandatory")
_MtsOnSourceS2_Type = Integer32
_MtsOnSourceS2_Object = MibScalar
mtsOnSourceS2 = _MtsOnSourceS2_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 27),
    _MtsOnSourceS2_Type()
)
mtsOnSourceS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsOnSourceS2.setStatus("mandatory")
_MtsOnSourceS1_Type = Integer32
_MtsOnSourceS1_Object = MibScalar
mtsOnSourceS1 = _MtsOnSourceS1_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 28),
    _MtsOnSourceS1_Type()
)
mtsOnSourceS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsOnSourceS1.setStatus("mandatory")
_MtsLocked_Type = Integer32
_MtsLocked_Object = MibScalar
mtsLocked = _MtsLocked_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 29),
    _MtsLocked_Type()
)
mtsLocked.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsLocked.setStatus("mandatory")
_MtsOutputSwitchOff_Type = Integer32
_MtsOutputSwitchOff_Object = MibScalar
mtsOutputSwitchOff = _MtsOutputSwitchOff_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 30),
    _MtsOutputSwitchOff_Type()
)
mtsOutputSwitchOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsOutputSwitchOff.setStatus("mandatory")
_MtsS2Blackout_Type = Integer32
_MtsS2Blackout_Object = MibScalar
mtsS2Blackout = _MtsS2Blackout_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 31),
    _MtsS2Blackout_Type()
)
mtsS2Blackout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2Blackout.setStatus("mandatory")
_MtsS2PhaseseqNotok_Type = Integer32
_MtsS2PhaseseqNotok_Object = MibScalar
mtsS2PhaseseqNotok = _MtsS2PhaseseqNotok_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 32),
    _MtsS2PhaseseqNotok_Type()
)
mtsS2PhaseseqNotok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2PhaseseqNotok.setStatus("mandatory")
_MtsS2VoltOutoftolerance_Type = Integer32
_MtsS2VoltOutoftolerance_Object = MibScalar
mtsS2VoltOutoftolerance = _MtsS2VoltOutoftolerance_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 33),
    _MtsS2VoltOutoftolerance_Type()
)
mtsS2VoltOutoftolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2VoltOutoftolerance.setStatus("mandatory")
_MtsS1SCRAlternateLoss_Type = Integer32
_MtsS1SCRAlternateLoss_Object = MibScalar
mtsS1SCRAlternateLoss = _MtsS1SCRAlternateLoss_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 34),
    _MtsS1SCRAlternateLoss_Type()
)
mtsS1SCRAlternateLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1SCRAlternateLoss.setStatus("mandatory")
_MtsS1InputSWOff_Type = Integer32
_MtsS1InputSWOff_Object = MibScalar
mtsS1InputSWOff = _MtsS1InputSWOff_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 35),
    _MtsS1InputSWOff_Type()
)
mtsS1InputSWOff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1InputSWOff.setStatus("mandatory")
_MtsS1Frequencybad_Type = Integer32
_MtsS1Frequencybad_Object = MibScalar
mtsS1Frequencybad = _MtsS1Frequencybad_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 36),
    _MtsS1Frequencybad_Type()
)
mtsS1Frequencybad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1Frequencybad.setStatus("mandatory")
_MtsS1Balancebad_Type = Integer32
_MtsS1Balancebad_Object = MibScalar
mtsS1Balancebad = _MtsS1Balancebad_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 37),
    _MtsS1Balancebad_Type()
)
mtsS1Balancebad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1Balancebad.setStatus("mandatory")
_MtsS1Blackout_Type = Integer32
_MtsS1Blackout_Object = MibScalar
mtsS1Blackout = _MtsS1Blackout_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 38),
    _MtsS1Blackout_Type()
)
mtsS1Blackout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1Blackout.setStatus("mandatory")
_MtsS1PhaseseqNotok_Type = Integer32
_MtsS1PhaseseqNotok_Object = MibScalar
mtsS1PhaseseqNotok = _MtsS1PhaseseqNotok_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 39),
    _MtsS1PhaseseqNotok_Type()
)
mtsS1PhaseseqNotok.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1PhaseseqNotok.setStatus("mandatory")
_MtsS1VoltOutoftolerance_Type = Integer32
_MtsS1VoltOutoftolerance_Object = MibScalar
mtsS1VoltOutoftolerance = _MtsS1VoltOutoftolerance_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 40),
    _MtsS1VoltOutoftolerance_Type()
)
mtsS1VoltOutoftolerance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1VoltOutoftolerance.setStatus("mandatory")
_MtsUserlogin_Type = Integer32
_MtsUserlogin_Object = MibScalar
mtsUserlogin = _MtsUserlogin_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 41),
    _MtsUserlogin_Type()
)
mtsUserlogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsUserlogin.setStatus("mandatory")
_MtsAlarmTemperature_Type = Integer32
_MtsAlarmTemperature_Object = MibScalar
mtsAlarmTemperature = _MtsAlarmTemperature_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 42),
    _MtsAlarmTemperature_Type()
)
mtsAlarmTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsAlarmTemperature.setStatus("mandatory")
_MtsAlarmOverload_Type = Integer32
_MtsAlarmOverload_Object = MibScalar
mtsAlarmOverload = _MtsAlarmOverload_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 43),
    _MtsAlarmOverload_Type()
)
mtsAlarmOverload.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsAlarmOverload.setStatus("mandatory")
_MtsGeneralFailure_Type = Integer32
_MtsGeneralFailure_Object = MibScalar
mtsGeneralFailure = _MtsGeneralFailure_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 44),
    _MtsGeneralFailure_Type()
)
mtsGeneralFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsGeneralFailure.setStatus("mandatory")
_MtsS2InputMCCBtrip_Type = Integer32
_MtsS2InputMCCBtrip_Object = MibScalar
mtsS2InputMCCBtrip = _MtsS2InputMCCBtrip_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 45),
    _MtsS2InputMCCBtrip_Type()
)
mtsS2InputMCCBtrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2InputMCCBtrip.setStatus("mandatory")
_MtsS1InputMCCBtrip_Type = Integer32
_MtsS1InputMCCBtrip_Object = MibScalar
mtsS1InputMCCBtrip = _MtsS1InputMCCBtrip_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 46),
    _MtsS1InputMCCBtrip_Type()
)
mtsS1InputMCCBtrip.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS1InputMCCBtrip.setStatus("mandatory")
_MtsServicelogin_Type = Integer32
_MtsServicelogin_Object = MibScalar
mtsServicelogin = _MtsServicelogin_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 47),
    _MtsServicelogin_Type()
)
mtsServicelogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsServicelogin.setStatus("mandatory")
_MtsOutputSCRalternanceloss_Type = Integer32
_MtsOutputSCRalternanceloss_Object = MibScalar
mtsOutputSCRalternanceloss = _MtsOutputSCRalternanceloss_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 48),
    _MtsOutputSCRalternanceloss_Type()
)
mtsOutputSCRalternanceloss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsOutputSCRalternanceloss.setStatus("mandatory")
_MtsManBypassS2_Type = Integer32
_MtsManBypassS2_Object = MibScalar
mtsManBypassS2 = _MtsManBypassS2_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 49),
    _MtsManBypassS2_Type()
)
mtsManBypassS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsManBypassS2.setStatus("mandatory")
_MtsManBypassS1_Type = Integer32
_MtsManBypassS1_Object = MibScalar
mtsManBypassS1 = _MtsManBypassS1_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 50),
    _MtsManBypassS1_Type()
)
mtsManBypassS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsManBypassS1.setStatus("mandatory")
_MtsManTransferS2_Type = Integer32
_MtsManTransferS2_Object = MibScalar
mtsManTransferS2 = _MtsManTransferS2_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 51),
    _MtsManTransferS2_Type()
)
mtsManTransferS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsManTransferS2.setStatus("mandatory")
_MtsManTransferS1_Type = Integer32
_MtsManTransferS1_Object = MibScalar
mtsManTransferS1 = _MtsManTransferS1_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 52),
    _MtsManTransferS1_Type()
)
mtsManTransferS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsManTransferS1.setStatus("mandatory")
_MtsS2SCRalternanceloss_Type = Integer32
_MtsS2SCRalternanceloss_Object = MibScalar
mtsS2SCRalternanceloss = _MtsS2SCRalternanceloss_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 53),
    _MtsS2SCRalternanceloss_Type()
)
mtsS2SCRalternanceloss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2SCRalternanceloss.setStatus("mandatory")
_MtsS2InputSWoff_Type = Integer32
_MtsS2InputSWoff_Object = MibScalar
mtsS2InputSWoff = _MtsS2InputSWoff_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 54),
    _MtsS2InputSWoff_Type()
)
mtsS2InputSWoff.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2InputSWoff.setStatus("mandatory")
_MtsS2Frequencybad_Type = Integer32
_MtsS2Frequencybad_Object = MibScalar
mtsS2Frequencybad = _MtsS2Frequencybad_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 55),
    _MtsS2Frequencybad_Type()
)
mtsS2Frequencybad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2Frequencybad.setStatus("mandatory")
_MtsS2Balancebad_Type = Integer32
_MtsS2Balancebad_Object = MibScalar
mtsS2Balancebad = _MtsS2Balancebad_Object(
    (1, 3, 6, 1, 4, 1, 5491, 12, 2, 56),
    _MtsS2Balancebad_Type()
)
mtsS2Balancebad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mtsS2Balancebad.setStatus("mandatory")
_MtsTraps_ObjectIdentity = ObjectIdentity
mtsTraps = _MtsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5491, 12, 4)
)

# Managed Objects groups


# Notification objects

mtsNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 12, 4, 0, 1)
)
if mibBuilder.loadTexts:
    mtsNormal.setStatus(
        ""
    )

mtsAnomaly = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 12, 4, 0, 2)
)
if mibBuilder.loadTexts:
    mtsAnomaly.setStatus(
        ""
    )

mtsFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 12, 4, 0, 3)
)
if mibBuilder.loadTexts:
    mtsFault.setStatus(
        ""
    )

mtsLock = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 12, 4, 0, 4)
)
if mibBuilder.loadTexts:
    mtsLock.setStatus(
        ""
    )

mtsManualBypassEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 5491, 12, 4, 0, 5)
)
if mibBuilder.loadTexts:
    mtsManualBypassEnabled.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RIELLOMTS-MIB",
    **{"mtsMIB": mtsMIB,
       "mtsIdent": mtsIdent,
       "mtsIdentManufacturer": mtsIdentManufacturer,
       "mtsIdentModel": mtsIdentModel,
       "mtsIdentSoftwareVersion": mtsIdentSoftwareVersion,
       "mtsIdentIOConfiguration": mtsIdentIOConfiguration,
       "mtsIdentType": mtsIdentType,
       "mtsIdentInputSockets": mtsIdentInputSockets,
       "mtsIdentOutputSockets": mtsIdentOutputSockets,
       "mtsIdentNominalCurrent": mtsIdentNominalCurrent,
       "mtsIdentNominalVoltage": mtsIdentNominalVoltage,
       "mtsIdentNominalFrequency": mtsIdentNominalFrequency,
       "mtsStatus": mtsStatus,
       "mtsS1Frequency": mtsS1Frequency,
       "mtsS1VoltageL1": mtsS1VoltageL1,
       "mtsS1VoltageL2": mtsS1VoltageL2,
       "mtsS1VoltageL3": mtsS1VoltageL3,
       "mtsS2Frequency": mtsS2Frequency,
       "mtsS2VoltageL1": mtsS2VoltageL1,
       "mtsS2VoltageL2": mtsS2VoltageL2,
       "mtsS2VoltageL3": mtsS2VoltageL3,
       "mtsPhaseDifference": mtsPhaseDifference,
       "mtsLoadL1": mtsLoadL1,
       "mtsLoadL2": mtsLoadL2,
       "mtsLoadL3": mtsLoadL3,
       "mtsOutputCurrentL1": mtsOutputCurrentL1,
       "mtsOutputCurrentL2": mtsOutputCurrentL2,
       "mtsOutputCurrentL3": mtsOutputCurrentL3,
       "mtsTemperature": mtsTemperature,
       "mtsSoundOff": mtsSoundOff,
       "mtsTestInProgress": mtsTestInProgress,
       "mtsAuxPower2fail": mtsAuxPower2fail,
       "mtsAuxPower1fail": mtsAuxPower1fail,
       "mtsSynchrobad": mtsSynchrobad,
       "mtsPreferredSource": mtsPreferredSource,
       "mtsTransferhinibit": mtsTransferhinibit,
       "mtsNonSynchInibit": mtsNonSynchInibit,
       "mtsSourceS2bad": mtsSourceS2bad,
       "mtsSourceS1bad": mtsSourceS1bad,
       "mtsOnSourceS2": mtsOnSourceS2,
       "mtsOnSourceS1": mtsOnSourceS1,
       "mtsLocked": mtsLocked,
       "mtsOutputSwitchOff": mtsOutputSwitchOff,
       "mtsS2Blackout": mtsS2Blackout,
       "mtsS2PhaseseqNotok": mtsS2PhaseseqNotok,
       "mtsS2VoltOutoftolerance": mtsS2VoltOutoftolerance,
       "mtsS1SCRAlternateLoss": mtsS1SCRAlternateLoss,
       "mtsS1InputSWOff": mtsS1InputSWOff,
       "mtsS1Frequencybad": mtsS1Frequencybad,
       "mtsS1Balancebad": mtsS1Balancebad,
       "mtsS1Blackout": mtsS1Blackout,
       "mtsS1PhaseseqNotok": mtsS1PhaseseqNotok,
       "mtsS1VoltOutoftolerance": mtsS1VoltOutoftolerance,
       "mtsUserlogin": mtsUserlogin,
       "mtsAlarmTemperature": mtsAlarmTemperature,
       "mtsAlarmOverload": mtsAlarmOverload,
       "mtsGeneralFailure": mtsGeneralFailure,
       "mtsS2InputMCCBtrip": mtsS2InputMCCBtrip,
       "mtsS1InputMCCBtrip": mtsS1InputMCCBtrip,
       "mtsServicelogin": mtsServicelogin,
       "mtsOutputSCRalternanceloss": mtsOutputSCRalternanceloss,
       "mtsManBypassS2": mtsManBypassS2,
       "mtsManBypassS1": mtsManBypassS1,
       "mtsManTransferS2": mtsManTransferS2,
       "mtsManTransferS1": mtsManTransferS1,
       "mtsS2SCRalternanceloss": mtsS2SCRalternanceloss,
       "mtsS2InputSWoff": mtsS2InputSWoff,
       "mtsS2Frequencybad": mtsS2Frequencybad,
       "mtsS2Balancebad": mtsS2Balancebad,
       "mtsTraps": mtsTraps,
       "mtsNormal": mtsNormal,
       "mtsAnomaly": mtsAnomaly,
       "mtsFault": mtsFault,
       "mtsLock": mtsLock,
       "mtsManualBypassEnabled": mtsManualBypassEnabled}
)
