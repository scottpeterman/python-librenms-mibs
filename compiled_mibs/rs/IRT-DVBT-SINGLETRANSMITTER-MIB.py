# SNMP MIB module (IRT-DVBT-SINGLETRANSMITTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\rs\IRT-DVBT-SINGLETRANSMITTER-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:23:36 2025
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

(eventCounter,
 eventPriority,
 eventTimeStamp,
 mibRelease) = mibBuilder.importSymbols(
    "IRT-COMMONVARBINDS-MIB",
    "eventCounter",
    "eventPriority",
    "eventTimeStamp",
    "mibRelease")

(FaultOK,
 Input1Input2,
 LocalRemote,
 MuteOk,
 OkNotOk,
 PresentNotPresent,
 SFNMFN,
 SelectManualAuto,
 SelectOnOff,
 WarningOK,
 dvbT) = mibBuilder.importSymbols(
    "IRT-TRANSMITTER-SMI-MIB",
    "FaultOK",
    "Input1Input2",
    "LocalRemote",
    "MuteOk",
    "OkNotOk",
    "PresentNotPresent",
    "SFNMFN",
    "SelectManualAuto",
    "SelectOnOff",
    "WarningOK",
    "dvbT")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

(sysDescr,
 sysLocation,
 sysName) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysDescr",
    "sysLocation",
    "sysName")

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

dvbSingleTransmitter = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dvbSingleTransmitter.setRevisions(
        ("2007-05-04 14:00",
         "2006-12-20 14:00",
         "2006-09-21 14:00",
         "2006-09-19 14:00",
         "2006-09-07 14:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DvbEventsST_ObjectIdentity = ObjectIdentity
dvbEventsST = _DvbEventsST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0)
)
_DvbSTGeneral_ObjectIdentity = ObjectIdentity
dvbSTGeneral = _DvbSTGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1)
)
_DvbSTInputPreselection_Type = Input1Input2
_DvbSTInputPreselection_Object = MibScalar
dvbSTInputPreselection = _DvbSTInputPreselection_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 1),
    _DvbSTInputPreselection_Type()
)
dvbSTInputPreselection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInputPreselection.setStatus("current")
if mibBuilder.loadTexts:
    dvbSTInputPreselection.setUnits(" ")
_DvbSTInputAutomatic_Type = SelectManualAuto
_DvbSTInputAutomatic_Object = MibScalar
dvbSTInputAutomatic = _DvbSTInputAutomatic_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 2),
    _DvbSTInputAutomatic_Type()
)
dvbSTInputAutomatic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInputAutomatic.setStatus("current")
if mibBuilder.loadTexts:
    dvbSTInputAutomatic.setUnits(" ")
_DvbSTTransmitterOpMode_Type = SelectOnOff
_DvbSTTransmitterOpMode_Object = MibScalar
dvbSTTransmitterOpMode = _DvbSTTransmitterOpMode_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 3),
    _DvbSTTransmitterOpMode_Type()
)
dvbSTTransmitterOpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTTransmitterOpMode.setStatus("current")
if mibBuilder.loadTexts:
    dvbSTTransmitterOpMode.setUnits(" ")
_DvbSTRFPresent_Type = PresentNotPresent
_DvbSTRFPresent_Object = MibScalar
dvbSTRFPresent = _DvbSTRFPresent_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 4),
    _DvbSTRFPresent_Type()
)
dvbSTRFPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTRFPresent.setStatus("current")
_DvbSTResetFault_Type = Unsigned32
_DvbSTResetFault_Object = MibScalar
dvbSTResetFault = _DvbSTResetFault_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 5),
    _DvbSTResetFault_Type()
)
dvbSTResetFault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTResetFault.setStatus("obsolete")
_DvbSTFault_Type = FaultOK
_DvbSTFault_Object = MibScalar
dvbSTFault = _DvbSTFault_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 6),
    _DvbSTFault_Type()
)
dvbSTFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTFault.setStatus("current")
_DvbSTWarning_Type = WarningOK
_DvbSTWarning_Object = MibScalar
dvbSTWarning = _DvbSTWarning_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 7),
    _DvbSTWarning_Type()
)
dvbSTWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTWarning.setStatus("current")
_DvbSTInput1OK_Type = OkNotOk
_DvbSTInput1OK_Object = MibScalar
dvbSTInput1OK = _DvbSTInput1OK_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 8),
    _DvbSTInput1OK_Type()
)
dvbSTInput1OK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTInput1OK.setStatus("current")
_DvbSTInput2OK_Type = OkNotOk
_DvbSTInput2OK_Object = MibScalar
dvbSTInput2OK = _DvbSTInput2OK_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 9),
    _DvbSTInput2OK_Type()
)
dvbSTInput2OK.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTInput2OK.setStatus("current")
_DvbSTLocalMode_Type = LocalRemote
_DvbSTLocalMode_Object = MibScalar
dvbSTLocalMode = _DvbSTLocalMode_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 10),
    _DvbSTLocalMode_Type()
)
dvbSTLocalMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTLocalMode.setStatus("current")


class _DvbSTActiveInput_Type(Integer32):
    """Custom type dvbSTActiveInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 0),
          ("input1", 1),
          ("input2", 2),
          ("seamless", 3),
          ("hmHierarchicalModulation", 4))
    )


_DvbSTActiveInput_Type.__name__ = "Integer32"
_DvbSTActiveInput_Object = MibScalar
dvbSTActiveInput = _DvbSTActiveInput_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 11),
    _DvbSTActiveInput_Type()
)
dvbSTActiveInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTActiveInput.setStatus("current")
_DvbSTSFNMode_Type = SFNMFN
_DvbSTSFNMode_Object = MibScalar
dvbSTSFNMode = _DvbSTSFNMode_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 12),
    _DvbSTSFNMode_Type()
)
dvbSTSFNMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTSFNMode.setStatus("current")
_DvbSTRefFault_Type = FaultOK
_DvbSTRefFault_Object = MibScalar
dvbSTRefFault = _DvbSTRefFault_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 13),
    _DvbSTRefFault_Type()
)
dvbSTRefFault.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTRefFault.setStatus("current")
_DvbSTMute_Type = MuteOk
_DvbSTMute_Object = MibScalar
dvbSTMute = _DvbSTMute_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 14),
    _DvbSTMute_Type()
)
dvbSTMute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTMute.setStatus("current")
_DvbSTFaultMIP_Type = FaultOK
_DvbSTFaultMIP_Object = MibScalar
dvbSTFaultMIP = _DvbSTFaultMIP_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 15),
    _DvbSTFaultMIP_Type()
)
dvbSTFaultMIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTFaultMIP.setStatus("current")
_DvbSTStuffingMode_Type = SelectOnOff
_DvbSTStuffingMode_Object = MibScalar
dvbSTStuffingMode = _DvbSTStuffingMode_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 1, 16),
    _DvbSTStuffingMode_Type()
)
dvbSTStuffingMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvbSTStuffingMode.setStatus("current")
_DvbSTEventEnable_ObjectIdentity = ObjectIdentity
dvbSTEventEnable = _DvbSTEventEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2)
)
_DvbSTEventEnableGeneral_ObjectIdentity = ObjectIdentity
dvbSTEventEnableGeneral = _DvbSTEventEnableGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1)
)
_DvbSTInputPreselectionEnable_Type = TruthValue
_DvbSTInputPreselectionEnable_Object = MibScalar
dvbSTInputPreselectionEnable = _DvbSTInputPreselectionEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 1),
    _DvbSTInputPreselectionEnable_Type()
)
dvbSTInputPreselectionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInputPreselectionEnable.setStatus("current")
_DvbSTInputAutomaticEnable_Type = TruthValue
_DvbSTInputAutomaticEnable_Object = MibScalar
dvbSTInputAutomaticEnable = _DvbSTInputAutomaticEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 2),
    _DvbSTInputAutomaticEnable_Type()
)
dvbSTInputAutomaticEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInputAutomaticEnable.setStatus("current")
_DvbSTTransmitterOpModeEnable_Type = TruthValue
_DvbSTTransmitterOpModeEnable_Object = MibScalar
dvbSTTransmitterOpModeEnable = _DvbSTTransmitterOpModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 3),
    _DvbSTTransmitterOpModeEnable_Type()
)
dvbSTTransmitterOpModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTTransmitterOpModeEnable.setStatus("current")
_DvbSTRFPresentEnable_Type = TruthValue
_DvbSTRFPresentEnable_Object = MibScalar
dvbSTRFPresentEnable = _DvbSTRFPresentEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 4),
    _DvbSTRFPresentEnable_Type()
)
dvbSTRFPresentEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTRFPresentEnable.setStatus("current")
_DvbSTResetFaultEnable_Type = TruthValue
_DvbSTResetFaultEnable_Object = MibScalar
dvbSTResetFaultEnable = _DvbSTResetFaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 5),
    _DvbSTResetFaultEnable_Type()
)
dvbSTResetFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTResetFaultEnable.setStatus("obsolete")
_DvbSTFaultEnable_Type = TruthValue
_DvbSTFaultEnable_Object = MibScalar
dvbSTFaultEnable = _DvbSTFaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 6),
    _DvbSTFaultEnable_Type()
)
dvbSTFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTFaultEnable.setStatus("current")
_DvbSTWarningEnable_Type = TruthValue
_DvbSTWarningEnable_Object = MibScalar
dvbSTWarningEnable = _DvbSTWarningEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 7),
    _DvbSTWarningEnable_Type()
)
dvbSTWarningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTWarningEnable.setStatus("current")
_DvbSTInput1OKEnable_Type = TruthValue
_DvbSTInput1OKEnable_Object = MibScalar
dvbSTInput1OKEnable = _DvbSTInput1OKEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 8),
    _DvbSTInput1OKEnable_Type()
)
dvbSTInput1OKEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInput1OKEnable.setStatus("current")
_DvbSTInput2OKEnable_Type = TruthValue
_DvbSTInput2OKEnable_Object = MibScalar
dvbSTInput2OKEnable = _DvbSTInput2OKEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 9),
    _DvbSTInput2OKEnable_Type()
)
dvbSTInput2OKEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInput2OKEnable.setStatus("current")
_DvbSTLocalModeEnable_Type = TruthValue
_DvbSTLocalModeEnable_Object = MibScalar
dvbSTLocalModeEnable = _DvbSTLocalModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 10),
    _DvbSTLocalModeEnable_Type()
)
dvbSTLocalModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTLocalModeEnable.setStatus("current")
_DvbSTActiveInputEnable_Type = TruthValue
_DvbSTActiveInputEnable_Object = MibScalar
dvbSTActiveInputEnable = _DvbSTActiveInputEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 11),
    _DvbSTActiveInputEnable_Type()
)
dvbSTActiveInputEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTActiveInputEnable.setStatus("current")
_DvbSTSFNModeEnable_Type = TruthValue
_DvbSTSFNModeEnable_Object = MibScalar
dvbSTSFNModeEnable = _DvbSTSFNModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 12),
    _DvbSTSFNModeEnable_Type()
)
dvbSTSFNModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTSFNModeEnable.setStatus("current")
_DvbSTRefFaultEnable_Type = TruthValue
_DvbSTRefFaultEnable_Object = MibScalar
dvbSTRefFaultEnable = _DvbSTRefFaultEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 13),
    _DvbSTRefFaultEnable_Type()
)
dvbSTRefFaultEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTRefFaultEnable.setStatus("current")
_DvbSTMuteEnable_Type = TruthValue
_DvbSTMuteEnable_Object = MibScalar
dvbSTMuteEnable = _DvbSTMuteEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 14),
    _DvbSTMuteEnable_Type()
)
dvbSTMuteEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTMuteEnable.setStatus("current")
_DvbSTFaultMIPEnable_Type = TruthValue
_DvbSTFaultMIPEnable_Object = MibScalar
dvbSTFaultMIPEnable = _DvbSTFaultMIPEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 15),
    _DvbSTFaultMIPEnable_Type()
)
dvbSTFaultMIPEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTFaultMIPEnable.setStatus("current")
_DvbSTStuffingModeEnable_Type = TruthValue
_DvbSTStuffingModeEnable_Object = MibScalar
dvbSTStuffingModeEnable = _DvbSTStuffingModeEnable_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 2, 1, 16),
    _DvbSTStuffingModeEnable_Type()
)
dvbSTStuffingModeEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTStuffingModeEnable.setStatus("current")
_DvbSTEventPriority_ObjectIdentity = ObjectIdentity
dvbSTEventPriority = _DvbSTEventPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3)
)
_DvbSTEventPriorityGeneral_ObjectIdentity = ObjectIdentity
dvbSTEventPriorityGeneral = _DvbSTEventPriorityGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1)
)
_DvbSTInputPreselectionPriority_Type = Unsigned32
_DvbSTInputPreselectionPriority_Object = MibScalar
dvbSTInputPreselectionPriority = _DvbSTInputPreselectionPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 1),
    _DvbSTInputPreselectionPriority_Type()
)
dvbSTInputPreselectionPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInputPreselectionPriority.setStatus("current")
_DvbSTInputAutomaticPriority_Type = Unsigned32
_DvbSTInputAutomaticPriority_Object = MibScalar
dvbSTInputAutomaticPriority = _DvbSTInputAutomaticPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 2),
    _DvbSTInputAutomaticPriority_Type()
)
dvbSTInputAutomaticPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInputAutomaticPriority.setStatus("current")
_DvbSTTransmitterOpModePriority_Type = Unsigned32
_DvbSTTransmitterOpModePriority_Object = MibScalar
dvbSTTransmitterOpModePriority = _DvbSTTransmitterOpModePriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 3),
    _DvbSTTransmitterOpModePriority_Type()
)
dvbSTTransmitterOpModePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTTransmitterOpModePriority.setStatus("current")
_DvbSTRFPresentPriority_Type = Unsigned32
_DvbSTRFPresentPriority_Object = MibScalar
dvbSTRFPresentPriority = _DvbSTRFPresentPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 4),
    _DvbSTRFPresentPriority_Type()
)
dvbSTRFPresentPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTRFPresentPriority.setStatus("current")
_DvbSTResetFaultPriority_Type = Unsigned32
_DvbSTResetFaultPriority_Object = MibScalar
dvbSTResetFaultPriority = _DvbSTResetFaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 5),
    _DvbSTResetFaultPriority_Type()
)
dvbSTResetFaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTResetFaultPriority.setStatus("obsolete")
_DvbSTFaultPriority_Type = Unsigned32
_DvbSTFaultPriority_Object = MibScalar
dvbSTFaultPriority = _DvbSTFaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 6),
    _DvbSTFaultPriority_Type()
)
dvbSTFaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTFaultPriority.setStatus("current")
_DvbSTWarningPriority_Type = Unsigned32
_DvbSTWarningPriority_Object = MibScalar
dvbSTWarningPriority = _DvbSTWarningPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 7),
    _DvbSTWarningPriority_Type()
)
dvbSTWarningPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTWarningPriority.setStatus("current")
_DvbSTInput1OKPriority_Type = Unsigned32
_DvbSTInput1OKPriority_Object = MibScalar
dvbSTInput1OKPriority = _DvbSTInput1OKPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 8),
    _DvbSTInput1OKPriority_Type()
)
dvbSTInput1OKPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInput1OKPriority.setStatus("current")
_DvbSTInput2OKPriority_Type = Unsigned32
_DvbSTInput2OKPriority_Object = MibScalar
dvbSTInput2OKPriority = _DvbSTInput2OKPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 9),
    _DvbSTInput2OKPriority_Type()
)
dvbSTInput2OKPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTInput2OKPriority.setStatus("current")
_DvbSTLocalModePriority_Type = Unsigned32
_DvbSTLocalModePriority_Object = MibScalar
dvbSTLocalModePriority = _DvbSTLocalModePriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 10),
    _DvbSTLocalModePriority_Type()
)
dvbSTLocalModePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTLocalModePriority.setStatus("current")
_DvbSTActiveInputPriority_Type = Unsigned32
_DvbSTActiveInputPriority_Object = MibScalar
dvbSTActiveInputPriority = _DvbSTActiveInputPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 11),
    _DvbSTActiveInputPriority_Type()
)
dvbSTActiveInputPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTActiveInputPriority.setStatus("current")
_DvbSTSFNModePriority_Type = Unsigned32
_DvbSTSFNModePriority_Object = MibScalar
dvbSTSFNModePriority = _DvbSTSFNModePriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 12),
    _DvbSTSFNModePriority_Type()
)
dvbSTSFNModePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTSFNModePriority.setStatus("current")
_DvbSTRefFaultPriority_Type = Unsigned32
_DvbSTRefFaultPriority_Object = MibScalar
dvbSTRefFaultPriority = _DvbSTRefFaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 13),
    _DvbSTRefFaultPriority_Type()
)
dvbSTRefFaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTRefFaultPriority.setStatus("current")
_DvbSTMutePriority_Type = Unsigned32
_DvbSTMutePriority_Object = MibScalar
dvbSTMutePriority = _DvbSTMutePriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 14),
    _DvbSTMutePriority_Type()
)
dvbSTMutePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTMutePriority.setStatus("current")
_DvbSTFaultMIPPriority_Type = Unsigned32
_DvbSTFaultMIPPriority_Object = MibScalar
dvbSTFaultMIPPriority = _DvbSTFaultMIPPriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 15),
    _DvbSTFaultMIPPriority_Type()
)
dvbSTFaultMIPPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTFaultMIPPriority.setStatus("current")
_DvbSTStuffingModePriority_Type = Unsigned32
_DvbSTStuffingModePriority_Object = MibScalar
dvbSTStuffingModePriority = _DvbSTStuffingModePriority_Object(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 3, 1, 16),
    _DvbSTStuffingModePriority_Type()
)
dvbSTStuffingModePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvbSTStuffingModePriority.setStatus("current")
_GroupST_ObjectIdentity = ObjectIdentity
groupST = _GroupST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4)
)
_ComplianceST_ObjectIdentity = ObjectIdentity
complianceST = _ComplianceST_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 5)
)

# Managed Objects groups

objectGroupST = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 1)
)
objectGroupST.setObjects(
      *(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselection"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomatic"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpMode"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFault"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarning"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OK"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OK"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalMode"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInput"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNMode"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFault"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMute"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIP"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingMode"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselectionEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomaticEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpModeEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresentEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarningEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OKEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OKEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalModeEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInputEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNModeEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFaultEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMuteEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIPEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingModeEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselectionPriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomaticPriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpModePriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresentPriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultPriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarningPriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIPPriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMutePriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFaultPriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNModePriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingModePriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OKPriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OKPriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalModePriority"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInputPriority"))
)
if mibBuilder.loadTexts:
    objectGroupST.setStatus("current")

objectGroupSTobsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 3)
)
objectGroupSTobsolete.setObjects(
      *(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFault"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFaultEnable"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFaultPriority"))
)
if mibBuilder.loadTexts:
    objectGroupSTobsolete.setStatus("obsolete")


# Notification objects

dvbSTInputPreselectionEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 1)
)
dvbSTInputPreselectionEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselection"))
)
if mibBuilder.loadTexts:
    dvbSTInputPreselectionEvent.setStatus(
        "current"
    )

dvbSTInputAutomaticEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 2)
)
dvbSTInputAutomaticEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomatic"))
)
if mibBuilder.loadTexts:
    dvbSTInputAutomaticEvent.setStatus(
        "current"
    )

dvbSTTransmitterOpModeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 3)
)
dvbSTTransmitterOpModeEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpMode"))
)
if mibBuilder.loadTexts:
    dvbSTTransmitterOpModeEvent.setStatus(
        "current"
    )

dvbSTRFPresentEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 4)
)
dvbSTRFPresentEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresent"))
)
if mibBuilder.loadTexts:
    dvbSTRFPresentEvent.setStatus(
        "current"
    )

dvbSTResetFaultEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 5)
)
dvbSTResetFaultEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFault"))
)
if mibBuilder.loadTexts:
    dvbSTResetFaultEvent.setStatus(
        "obsolete"
    )

dvbSTFaultEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 6)
)
dvbSTFaultEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFault"))
)
if mibBuilder.loadTexts:
    dvbSTFaultEvent.setStatus(
        "current"
    )

dvbSTWarningEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 7)
)
dvbSTWarningEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarning"))
)
if mibBuilder.loadTexts:
    dvbSTWarningEvent.setStatus(
        "current"
    )

dvbSTInput1OKEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 8)
)
dvbSTInput1OKEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OK"))
)
if mibBuilder.loadTexts:
    dvbSTInput1OKEvent.setStatus(
        "current"
    )

dvbSTInput2OKEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 9)
)
dvbSTInput2OKEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OK"))
)
if mibBuilder.loadTexts:
    dvbSTInput2OKEvent.setStatus(
        "current"
    )

dvbSTLocalModeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 10)
)
dvbSTLocalModeEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalMode"))
)
if mibBuilder.loadTexts:
    dvbSTLocalModeEvent.setStatus(
        "current"
    )

dvbSTActiveInputEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 11)
)
dvbSTActiveInputEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInput"))
)
if mibBuilder.loadTexts:
    dvbSTActiveInputEvent.setStatus(
        "current"
    )

dvbSTSFNModeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 12)
)
dvbSTSFNModeEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNMode"))
)
if mibBuilder.loadTexts:
    dvbSTSFNModeEvent.setStatus(
        "current"
    )

dvbSTRefFaultEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 13)
)
dvbSTRefFaultEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFault"))
)
if mibBuilder.loadTexts:
    dvbSTRefFaultEvent.setStatus(
        "current"
    )

dvbSTMuteEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 14)
)
dvbSTMuteEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMute"))
)
if mibBuilder.loadTexts:
    dvbSTMuteEvent.setStatus(
        "current"
    )

dvbSTFaultMIPEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 15)
)
dvbSTFaultMIPEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIP"))
)
if mibBuilder.loadTexts:
    dvbSTFaultMIPEvent.setStatus(
        "current"
    )

dvbSTStuffingModeEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 0, 16)
)
dvbSTStuffingModeEvent.setObjects(
      *(("SNMPv2-MIB", "sysDescr"),
        ("SNMPv2-MIB", "sysName"),
        ("SNMPv2-MIB", "sysLocation"),
        ("IRT-COMMONVARBINDS-MIB", "eventTimeStamp"),
        ("IRT-COMMONVARBINDS-MIB", "eventPriority"),
        ("IRT-COMMONVARBINDS-MIB", "eventCounter"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingMode"))
)
if mibBuilder.loadTexts:
    dvbSTStuffingModeEvent.setStatus(
        "current"
    )


# Notifications groups

eventGroupST = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 2)
)
eventGroupST.setObjects(
      *(("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputPreselectionEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInputAutomaticEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTTransmitterOpModeEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRFPresentEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTWarningEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput1OKEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTInput2OKEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTLocalModeEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTActiveInputEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTSFNModeEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTRefFaultEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTStuffingModeEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTMuteEvent"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTFaultMIPEvent"))
)
if mibBuilder.loadTexts:
    eventGroupST.setStatus(
        "current"
    )

eventGroupSTobsolete = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 4, 4)
)
eventGroupSTobsolete.setObjects(
    ("IRT-DVBT-SINGLETRANSMITTER-MIB", "dvbSTResetFaultEvent")
)
if mibBuilder.loadTexts:
    eventGroupSTobsolete.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

dvbSingleTransmitterCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 19831, 1, 1, 1, 1, 5, 1)
)
dvbSingleTransmitterCompliance.setObjects(
      *(("IRT-DVBT-SINGLETRANSMITTER-MIB", "objectGroupST"),
        ("IRT-DVBT-SINGLETRANSMITTER-MIB", "eventGroupST"))
)
if mibBuilder.loadTexts:
    dvbSingleTransmitterCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IRT-DVBT-SINGLETRANSMITTER-MIB",
    **{"dvbSingleTransmitter": dvbSingleTransmitter,
       "dvbEventsST": dvbEventsST,
       "dvbSTInputPreselectionEvent": dvbSTInputPreselectionEvent,
       "dvbSTInputAutomaticEvent": dvbSTInputAutomaticEvent,
       "dvbSTTransmitterOpModeEvent": dvbSTTransmitterOpModeEvent,
       "dvbSTRFPresentEvent": dvbSTRFPresentEvent,
       "dvbSTResetFaultEvent": dvbSTResetFaultEvent,
       "dvbSTFaultEvent": dvbSTFaultEvent,
       "dvbSTWarningEvent": dvbSTWarningEvent,
       "dvbSTInput1OKEvent": dvbSTInput1OKEvent,
       "dvbSTInput2OKEvent": dvbSTInput2OKEvent,
       "dvbSTLocalModeEvent": dvbSTLocalModeEvent,
       "dvbSTActiveInputEvent": dvbSTActiveInputEvent,
       "dvbSTSFNModeEvent": dvbSTSFNModeEvent,
       "dvbSTRefFaultEvent": dvbSTRefFaultEvent,
       "dvbSTMuteEvent": dvbSTMuteEvent,
       "dvbSTFaultMIPEvent": dvbSTFaultMIPEvent,
       "dvbSTStuffingModeEvent": dvbSTStuffingModeEvent,
       "dvbSTGeneral": dvbSTGeneral,
       "dvbSTInputPreselection": dvbSTInputPreselection,
       "dvbSTInputAutomatic": dvbSTInputAutomatic,
       "dvbSTTransmitterOpMode": dvbSTTransmitterOpMode,
       "dvbSTRFPresent": dvbSTRFPresent,
       "dvbSTResetFault": dvbSTResetFault,
       "dvbSTFault": dvbSTFault,
       "dvbSTWarning": dvbSTWarning,
       "dvbSTInput1OK": dvbSTInput1OK,
       "dvbSTInput2OK": dvbSTInput2OK,
       "dvbSTLocalMode": dvbSTLocalMode,
       "dvbSTActiveInput": dvbSTActiveInput,
       "dvbSTSFNMode": dvbSTSFNMode,
       "dvbSTRefFault": dvbSTRefFault,
       "dvbSTMute": dvbSTMute,
       "dvbSTFaultMIP": dvbSTFaultMIP,
       "dvbSTStuffingMode": dvbSTStuffingMode,
       "dvbSTEventEnable": dvbSTEventEnable,
       "dvbSTEventEnableGeneral": dvbSTEventEnableGeneral,
       "dvbSTInputPreselectionEnable": dvbSTInputPreselectionEnable,
       "dvbSTInputAutomaticEnable": dvbSTInputAutomaticEnable,
       "dvbSTTransmitterOpModeEnable": dvbSTTransmitterOpModeEnable,
       "dvbSTRFPresentEnable": dvbSTRFPresentEnable,
       "dvbSTResetFaultEnable": dvbSTResetFaultEnable,
       "dvbSTFaultEnable": dvbSTFaultEnable,
       "dvbSTWarningEnable": dvbSTWarningEnable,
       "dvbSTInput1OKEnable": dvbSTInput1OKEnable,
       "dvbSTInput2OKEnable": dvbSTInput2OKEnable,
       "dvbSTLocalModeEnable": dvbSTLocalModeEnable,
       "dvbSTActiveInputEnable": dvbSTActiveInputEnable,
       "dvbSTSFNModeEnable": dvbSTSFNModeEnable,
       "dvbSTRefFaultEnable": dvbSTRefFaultEnable,
       "dvbSTMuteEnable": dvbSTMuteEnable,
       "dvbSTFaultMIPEnable": dvbSTFaultMIPEnable,
       "dvbSTStuffingModeEnable": dvbSTStuffingModeEnable,
       "dvbSTEventPriority": dvbSTEventPriority,
       "dvbSTEventPriorityGeneral": dvbSTEventPriorityGeneral,
       "dvbSTInputPreselectionPriority": dvbSTInputPreselectionPriority,
       "dvbSTInputAutomaticPriority": dvbSTInputAutomaticPriority,
       "dvbSTTransmitterOpModePriority": dvbSTTransmitterOpModePriority,
       "dvbSTRFPresentPriority": dvbSTRFPresentPriority,
       "dvbSTResetFaultPriority": dvbSTResetFaultPriority,
       "dvbSTFaultPriority": dvbSTFaultPriority,
       "dvbSTWarningPriority": dvbSTWarningPriority,
       "dvbSTInput1OKPriority": dvbSTInput1OKPriority,
       "dvbSTInput2OKPriority": dvbSTInput2OKPriority,
       "dvbSTLocalModePriority": dvbSTLocalModePriority,
       "dvbSTActiveInputPriority": dvbSTActiveInputPriority,
       "dvbSTSFNModePriority": dvbSTSFNModePriority,
       "dvbSTRefFaultPriority": dvbSTRefFaultPriority,
       "dvbSTMutePriority": dvbSTMutePriority,
       "dvbSTFaultMIPPriority": dvbSTFaultMIPPriority,
       "dvbSTStuffingModePriority": dvbSTStuffingModePriority,
       "groupST": groupST,
       "objectGroupST": objectGroupST,
       "eventGroupST": eventGroupST,
       "objectGroupSTobsolete": objectGroupSTobsolete,
       "eventGroupSTobsolete": eventGroupSTobsolete,
       "complianceST": complianceST,
       "dvbSingleTransmitterCompliance": dvbSingleTransmitterCompliance}
)
