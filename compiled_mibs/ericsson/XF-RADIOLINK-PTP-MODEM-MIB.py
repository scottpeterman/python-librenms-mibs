# SNMP MIB module (XF-RADIOLINK-PTP-MODEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\XF-RADIOLINK-PTP-MODEM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:45 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(xfTermRowIndex,) = mibBuilder.importSymbols(
    "XF-RADIOLINK-PTP-TERMINAL-MIB",
    "xfTermRowIndex")

(xfRadioLink,) = mibBuilder.importSymbols(
    "XF-TOP-MIB",
    "xfRadioLink")


# MODULE-IDENTITY

xfRadioLinkPtpModemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2)
)
if mibBuilder.loadTexts:
    xfRadioLinkPtpModemMIB.setRevisions(
        ("2012-06-24 00:00",
         "2012-05-29 00:00",
         "2011-05-23 00:00",
         "2011-04-06 00:00",
         "2011-02-01 00:00",
         "2010-12-13 00:00",
         "2010-01-19 00:00",
         "2009-11-30 00:00",
         "2009-11-26 00:00",
         "2009-11-18 00:00",
         "2009-09-18 00:00",
         "2009-06-26 00:00",
         "2009-06-24 00:00",
         "2009-04-20 00:00",
         "2009-04-14 00:00",
         "2009-03-04 00:00",
         "2008-10-02 00:00",
         "2008-09-16 00:00",
         "2008-08-15 00:00",
         "2008-06-25 00:00",
         "2008-06-24 00:00",
         "2008-06-18 00:00",
         "2008-06-04 00:00",
         "2008-06-03 00:00",
         "2008-04-09 00:00",
         "2008-03-03 00:00",
         "2008-02-26 00:00",
         "2007-11-12 00:00",
         "2007-10-24 00:00",
         "2007-08-14 00:00",
         "2007-07-03 00:00",
         "2007-06-04 00:00",
         "2007-01-17 00:00",
         "2006-11-14 00:00",
         "2006-09-19 13:25",
         "2006-03-20 00:00",
         "2006-02-24 00:00",
         "2006-01-31 00:00",
         "2005-03-02 00:00",
         "2004-12-13 00:00",
         "2004-07-02 00:00",
         "2004-06-16 00:00",
         "2004-05-25 00:00",
         "2004-04-26 00:00",
         "2004-01-20 00:00",
         "2003-12-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class MMUAlarmStatus(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("rcc0", 0),
          ("rcc1", 1),
          ("rcc2", 2),
          ("icc0", 3),
          ("icc1", 4),
          ("icc2", 5),
          ("atpcCapabilityAlarmFarEnd0", 6),
          ("atpcCapabilityAlarmFarEnd1", 7),
          ("atpcCapabilityAlarmFarEnd2", 8),
          ("hcc0", 9),
          ("hcc1", 10),
          ("hcc2", 11),
          ("xpicCable0", 12),
          ("xpicCable1", 13),
          ("xpicCable2", 14),
          ("xpicLos0", 15),
          ("xpicLos1", 16),
          ("xpicLos2", 17),
          ("interMMUChannelFailure0", 18),
          ("interMMUChannelFailure1", 19),
          ("interMMUChannelFailure2", 20),
          ("runningConfigNotAccepted0", 21),
          ("runningConfigNotAccepted1", 22),
          ("runningConfigNotAccepted2", 23),
          ("defaultConfigNotAccepted0", 24),
          ("defaultConfigNotAccepted1", 25),
          ("defaultConfigNotAccepted2", 26),
          ("syncOverRLNotSupported0", 27),
          ("syncOverRLNotSupported1", 28),
          ("syncOverRLNotSupported2", 29),
          ("rauPowerSupplyChanged0", 30),
          ("rauPowerSupplyChanged1", 31),
          ("rauPowerSupplyChanged2", 32),
          ("congestionControlNotSupported0", 33),
          ("congestionControlNotSupported1", 34),
          ("congestionControlNotSupported2", 35))
    )


class MMUModIndexStatus(TextualConvention, Integer32):
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
        *(("other", 1),
          ("modIndexValid", 2),
          ("modIndexNotValid", 3))
    )



class MMUAtpcCapability(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("noAtpcSupport", 2),
          ("doesNotExist", 3),
          ("atpcCapabilityUnknown", 4),
          ("supportsAtpc", 5),
          ("supportsAtpcFallback", 6),
          ("supportsAtpcFallbackTimer", 7))
    )



class MMUModCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cqpsk", 0),
          ("qam16", 1),
          ("qam128", 2),
          ("qam32", 3),
          ("qam64", 4))
    )


class MMUCapCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("oneE1", 0),
          ("twoE1", 1),
          ("fourE1", 2),
          ("oneE2", 3),
          ("twoE2", 4),
          ("oneE3oneE1", 5),
          ("twoE3", 6),
          ("fourE3", 7),
          ("fourDS1", 8),
          ("eightDS1", 9),
          ("sixteenDS1", 10),
          ("seventeenDS1", 11),
          ("stm0", 12),
          ("stm1", 13),
          ("thirtytwoDS1", 14),
          ("stm1DS1", 15),
          ("stm150MHz", 16),
          ("twentytwoE1", 17),
          ("thirtyfiveE1", 18),
          ("fortysixE1", 19),
          ("seventyfiveE1", 20),
          ("oneStm1OneJ1", 21),
          ("sixtynineDS1", 22),
          ("eightyDS1", 23))
    )


class MMUChannelSpacingCapability(TextualConvention, Integer32):
    status = "current"
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
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("chspUnknown", 0),
          ("chsp7MHz", 1),
          ("chsp14MHz", 2),
          ("chsp20MHz", 3),
          ("chsp28MHz", 4),
          ("chsp30MHz", 5),
          ("chsp40MHz", 6),
          ("chsp50MHz", 7),
          ("chsp56MHz", 8),
          ("chsp10MHz", 9),
          ("chsp3500kHz", 10))
    )



class MMUFrameFormatType(TextualConvention, Integer32):
    status = "current"
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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("fftUnknown", 0),
          ("fftStatic", 1),
          ("fftAdMod", 2),
          ("fftXpic", 3),
          ("fftXpicAdmod", 4),
          ("fftLegacy", 5),
          ("fftStaticLH", 6),
          ("fftAdmodLH", 7),
          ("fftXpicLH", 8),
          ("fftXpicAdmodLH", 9))
    )



class ModemModulation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("cqpsk", 2),
          ("qam16", 3),
          ("qam128", 4),
          ("qam32", 5),
          ("qam64", 6),
          ("qam4", 7),
          ("qam8", 8),
          ("qam256", 9),
          ("qam512", 10),
          ("qam1024", 11))
    )



# MIB Managed Objects in the order of their OIDs

_XfRadioLinkPtpModemObjects_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpModemObjects = _XfRadioLinkPtpModemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1)
)
_XfModemTable_Object = MibTable
xfModemTable = _XfModemTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1)
)
if mibBuilder.loadTexts:
    xfModemTable.setStatus("current")
_XfModemEntry_Object = MibTableRow
xfModemEntry = _XfModemEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1)
)
xfModemEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xfModemEntry.setStatus("current")
_XfMMUAlarmStatus_Type = MMUAlarmStatus
_XfMMUAlarmStatus_Object = MibTableColumn
xfMMUAlarmStatus = _XfMMUAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 1),
    _XfMMUAlarmStatus_Type()
)
xfMMUAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUAlarmStatus.setStatus("current")
_XfMMUModIndexNotValid_Type = MMUModIndexStatus
_XfMMUModIndexNotValid_Object = MibTableColumn
xfMMUModIndexNotValid = _XfMMUModIndexNotValid_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 2),
    _XfMMUModIndexNotValid_Type()
)
xfMMUModIndexNotValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUModIndexNotValid.setStatus("obsolete")
_XfMMUAtpcCapability_Type = MMUAtpcCapability
_XfMMUAtpcCapability_Object = MibTableColumn
xfMMUAtpcCapability = _XfMMUAtpcCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 3),
    _XfMMUAtpcCapability_Type()
)
xfMMUAtpcCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUAtpcCapability.setStatus("current")
_XfMMUModCapability_Type = MMUModCapability
_XfMMUModCapability_Object = MibTableColumn
xfMMUModCapability = _XfMMUModCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 4),
    _XfMMUModCapability_Type()
)
xfMMUModCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUModCapability.setStatus("current")
_XfMMUCapacityCapability_Type = MMUCapCapability
_XfMMUCapacityCapability_Object = MibTableColumn
xfMMUCapacityCapability = _XfMMUCapacityCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 5),
    _XfMMUCapacityCapability_Type()
)
xfMMUCapacityCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUCapacityCapability.setStatus("current")


class _XfMMUProtectionPath_Type(Integer32):
    """Custom type xfMMUProtectionPath based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("mmuRa1", 2),
          ("mmuRa2", 3))
    )


_XfMMUProtectionPath_Type.__name__ = "Integer32"
_XfMMUProtectionPath_Object = MibTableColumn
xfMMUProtectionPath = _XfMMUProtectionPath_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 6),
    _XfMMUProtectionPath_Type()
)
xfMMUProtectionPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUProtectionPath.setStatus("current")
_XfMMUSlotPosition_Type = Integer32
_XfMMUSlotPosition_Object = MibTableColumn
xfMMUSlotPosition = _XfMMUSlotPosition_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 7),
    _XfMMUSlotPosition_Type()
)
xfMMUSlotPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUSlotPosition.setStatus("current")


class _XfMMUChannelModeCapability_Type(Bits):
    """Custom type xfMMUChannelModeCapability based on Bits"""
    namedValues = NamedValues(
        *(("ccdp", 0),
          ("accp", 1),
          ("acap", 2))
    )

_XfMMUChannelModeCapability_Type.__name__ = "Bits"
_XfMMUChannelModeCapability_Object = MibTableColumn
xfMMUChannelModeCapability = _XfMMUChannelModeCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 8),
    _XfMMUChannelModeCapability_Type()
)
xfMMUChannelModeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUChannelModeCapability.setStatus("current")
_XfMMUChannelCompanionSlot_Type = Integer32
_XfMMUChannelCompanionSlot_Object = MibTableColumn
xfMMUChannelCompanionSlot = _XfMMUChannelCompanionSlot_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 9),
    _XfMMUChannelCompanionSlot_Type()
)
xfMMUChannelCompanionSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfMMUChannelCompanionSlot.setStatus("current")
_XfMMUChannelCompanionIndex_Type = Integer32
_XfMMUChannelCompanionIndex_Object = MibTableColumn
xfMMUChannelCompanionIndex = _XfMMUChannelCompanionIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 10),
    _XfMMUChannelCompanionIndex_Type()
)
xfMMUChannelCompanionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUChannelCompanionIndex.setStatus("current")


class _XfMMUInterfaceCapability_Type(Bits):
    """Custom type xfMMUInterfaceCapability based on Bits"""
    namedValues = NamedValues(
        *(("pdhToTdmHier", 0),
          ("pdhToTdmFlat", 1),
          ("pdhToTdmFlatAndBitpipeToPtp", 2),
          ("pdhToTdmAndSDHToSFP", 3),
          ("pdhToTdmAndSDHToPtp", 4),
          ("pdhToTdmAndSDHToSFPHAndSDHToPtP", 5))
    )

_XfMMUInterfaceCapability_Type.__name__ = "Bits"
_XfMMUInterfaceCapability_Object = MibTableColumn
xfMMUInterfaceCapability = _XfMMUInterfaceCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 11),
    _XfMMUInterfaceCapability_Type()
)
xfMMUInterfaceCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUInterfaceCapability.setStatus("current")


class _XfMMURAUSupplyVoltage_Type(Integer32):
    """Custom type xfMMURAUSupplyVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("p55V", 2),
          ("m48V", 3),
          ("p24V", 4))
    )


_XfMMURAUSupplyVoltage_Type.__name__ = "Integer32"
_XfMMURAUSupplyVoltage_Object = MibTableColumn
xfMMURAUSupplyVoltage = _XfMMURAUSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 1, 1, 12),
    _XfMMURAUSupplyVoltage_Type()
)
xfMMURAUSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMURAUSupplyVoltage.setStatus("current")
_XfRAUIFTable_Object = MibTable
xfRAUIFTable = _XfRAUIFTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    xfRAUIFTable.setStatus("current")
_XfRAUIFEntry_Object = MibTableRow
xfRAUIFEntry = _XfRAUIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1)
)
xfRAUIFEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRAUIFEntry.setStatus("current")


class _XfRAUIFLoopEnable_Type(Integer32):
    """Custom type xfRAUIFLoopEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfRAUIFLoopEnable_Type.__name__ = "Integer32"
_XfRAUIFLoopEnable_Object = MibTableColumn
xfRAUIFLoopEnable = _XfRAUIFLoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 1),
    _XfRAUIFLoopEnable_Type()
)
xfRAUIFLoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRAUIFLoopEnable.setStatus("current")


class _XfRAUIFRxLoop_Type(Integer32):
    """Custom type xfRAUIFRxLoop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfRAUIFRxLoop_Type.__name__ = "Integer32"
_XfRAUIFRxLoop_Object = MibTableColumn
xfRAUIFRxLoop = _XfRAUIFRxLoop_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 2),
    _XfRAUIFRxLoop_Type()
)
xfRAUIFRxLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRAUIFRxLoop.setStatus("current")


class _XfRAUIFAlarms_Type(Bits):
    """Custom type xfRAUIFAlarms based on Bits"""
    namedValues = NamedValues(
        *(("dmodClock0", 0),
          ("dmodClock1", 1),
          ("dmodClock2", 2),
          ("los0", 3),
          ("los1", 4),
          ("los2", 5),
          ("rxIfInput0", 6),
          ("rxIfInput1", 7),
          ("rxIfInput2", 8),
          ("txIfInput0", 9),
          ("txIfInput1", 10),
          ("txIfInput2", 11),
          ("radioFrame0", 12),
          ("radioFrame1", 13),
          ("radioFrame2", 14),
          ("ber0", 15),
          ("ber1", 16),
          ("ber2", 17),
          ("radioId0", 18),
          ("radioId1", 19),
          ("radioId2", 20),
          ("modIndex0", 21),
          ("modIndex1", 22),
          ("modIndex2", 23),
          ("aisReceived0", 24),
          ("aisReceived1", 25),
          ("aisReceived2", 26),
          ("carrierRecoveryLoss0", 27),
          ("carrierRecoveryLoss1", 28),
          ("carrierRecoveryLoss2", 29),
          ("wstLosL2R0", 30),
          ("wstLosL2R1", 31),
          ("wstLosL2R2", 32),
          ("wstLosR2L0", 33),
          ("wstLosR2L1", 34),
          ("wstLosR2L2", 35),
          ("lofR2L0", 36),
          ("lofR2L1", 37),
          ("lofR2L2", 38),
          ("notused0", 39),
          ("notused1", 40),
          ("notused2", 41),
          ("ifLosR2L0", 42),
          ("ifLosR2L1", 43),
          ("ifLosR2L2", 44),
          ("earlyWarning0", 45),
          ("earlyWarning1", 46),
          ("earlyWarning2", 47),
          ("lber0", 48),
          ("lber1", 49),
          ("lber2", 50),
          ("hber0", 51),
          ("hber1", 52),
          ("hber2", 53))
    )

_XfRAUIFAlarms_Type.__name__ = "Bits"
_XfRAUIFAlarms_Object = MibTableColumn
xfRAUIFAlarms = _XfRAUIFAlarms_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 3),
    _XfRAUIFAlarms_Type()
)
xfRAUIFAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUIFAlarms.setStatus("current")


class _XfRAUIFStatus_Type(Bits):
    """Custom type xfRAUIFStatus based on Bits"""
    namedValues = NamedValues(
        *(("rxLoop0", 0),
          ("rxLoop1", 1),
          ("rxLoop2", 2),
          ("ifLoop0", 3),
          ("ifLoop1", 4),
          ("ifLoop2", 5))
    )

_XfRAUIFStatus_Type.__name__ = "Bits"
_XfRAUIFStatus_Object = MibTableColumn
xfRAUIFStatus = _XfRAUIFStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 2, 1, 4),
    _XfRAUIFStatus_Type()
)
xfRAUIFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUIFStatus.setStatus("current")
_XfLINERSTable_Object = MibTable
xfLINERSTable = _XfLINERSTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 3)
)
if mibBuilder.loadTexts:
    xfLINERSTable.setStatus("current")
_XfLINERSEntry_Object = MibTableRow
xfLINERSEntry = _XfLINERSEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 3, 1)
)
xfLINERSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfLINERSEntry.setStatus("current")


class _XfLINERSAlarms_Type(Bits):
    """Custom type xfLINERSAlarms based on Bits"""
    namedValues = NamedValues(
        *(("timLineSide0", 0),
          ("timLineSide1", 1),
          ("timLineSide2", 2),
          ("lofL2R0", 3),
          ("lofL2R1", 4),
          ("lofL2R2", 5),
          ("losL2R0", 6),
          ("losL2R1", 7),
          ("losL2R2", 8),
          ("sfpLos0", 9),
          ("sfpLos1", 10),
          ("sfpLos2", 11))
    )

_XfLINERSAlarms_Type.__name__ = "Bits"
_XfLINERSAlarms_Object = MibTableColumn
xfLINERSAlarms = _XfLINERSAlarms_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 3, 1, 1),
    _XfLINERSAlarms_Type()
)
xfLINERSAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfLINERSAlarms.setStatus("current")
_XfModemCapabilityTable_Object = MibTable
xfModemCapabilityTable = _XfModemCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4)
)
if mibBuilder.loadTexts:
    xfModemCapabilityTable.setStatus("current")
_XfModemCapabilityEntry_Object = MibTableRow
xfModemCapabilityEntry = _XfModemCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1)
)
xfModemCapabilityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRowIndex"),
)
if mibBuilder.loadTexts:
    xfModemCapabilityEntry.setStatus("current")
_XfMMUChannelSpacing_Type = MMUChannelSpacingCapability
_XfMMUChannelSpacing_Object = MibTableColumn
xfMMUChannelSpacing = _XfMMUChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 1),
    _XfMMUChannelSpacing_Type()
)
xfMMUChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUChannelSpacing.setStatus("current")
_XfMMUChannelModulation_Type = ModemModulation
_XfMMUChannelModulation_Object = MibTableColumn
xfMMUChannelModulation = _XfMMUChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 2),
    _XfMMUChannelModulation_Type()
)
xfMMUChannelModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUChannelModulation.setStatus("current")
_XfMMUMaxTribCapacity_Type = Integer32
_XfMMUMaxTribCapacity_Object = MibTableColumn
xfMMUMaxTribCapacity = _XfMMUMaxTribCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 3),
    _XfMMUMaxTribCapacity_Type()
)
xfMMUMaxTribCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUMaxTribCapacity.setStatus("current")
_XfMMUDCNCapacity_Type = Integer32
_XfMMUDCNCapacity_Object = MibTableColumn
xfMMUDCNCapacity = _XfMMUDCNCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 4),
    _XfMMUDCNCapacity_Type()
)
xfMMUDCNCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUDCNCapacity.setStatus("current")
_XfMMUMaxCapacity_Type = Integer32
_XfMMUMaxCapacity_Object = MibTableColumn
xfMMUMaxCapacity = _XfMMUMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 5),
    _XfMMUMaxCapacity_Type()
)
xfMMUMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUMaxCapacity.setStatus("current")
_XfMMUFrameFormatType_Type = MMUFrameFormatType
_XfMMUFrameFormatType_Object = MibTableColumn
xfMMUFrameFormatType = _XfMMUFrameFormatType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 6),
    _XfMMUFrameFormatType_Type()
)
xfMMUFrameFormatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUFrameFormatType.setStatus("current")


class _XfMMUFrameFormatRev_Type(Integer32):
    """Custom type xfMMUFrameFormatRev based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("ffOther", 1),
          ("ffVersion0", 2),
          ("ffVersion1", 3),
          ("ffVersion2", 4),
          ("ffVersion3", 5),
          ("ffVersion4", 6),
          ("ffVersion5", 7),
          ("ffVersion6", 8),
          ("ffVersion7", 9),
          ("ffVersion8", 10),
          ("ffVersion9", 11),
          ("ffVersion10", 12),
          ("ffVersion11", 13),
          ("ffVersion12", 14),
          ("ffVersion13", 15),
          ("ffVersion14", 16),
          ("ffVersion15", 17))
    )


_XfMMUFrameFormatRev_Type.__name__ = "Integer32"
_XfMMUFrameFormatRev_Object = MibTableColumn
xfMMUFrameFormatRev = _XfMMUFrameFormatRev_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 7),
    _XfMMUFrameFormatRev_Type()
)
xfMMUFrameFormatRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUFrameFormatRev.setStatus("current")


class _XfMMUBerAlarmThresholdCapability_Type(Bits):
    """Custom type xfMMUBerAlarmThresholdCapability based on Bits"""
    namedValues = NamedValues(
        *(("berThrCap1e3", 0),
          ("berThrCap1e4", 1),
          ("berThrCap1e5", 2),
          ("berThrCap1e6", 3))
    )

_XfMMUBerAlarmThresholdCapability_Type.__name__ = "Bits"
_XfMMUBerAlarmThresholdCapability_Object = MibTableColumn
xfMMUBerAlarmThresholdCapability = _XfMMUBerAlarmThresholdCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 1, 4, 1, 8),
    _XfMMUBerAlarmThresholdCapability_Type()
)
xfMMUBerAlarmThresholdCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfMMUBerAlarmThresholdCapability.setStatus("current")
_XfRadioLinkPtpModemConformance_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpModemConformance = _XfRadioLinkPtpModemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2)
)
_XfRadioLinkPtpModemCompliances_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpModemCompliances = _XfRadioLinkPtpModemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 1)
)
_XfRadioLinkPtpModemGroups_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpModemGroups = _XfRadioLinkPtpModemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 2)
)

# Managed Objects groups

xfRadioLinkPtpModemCompleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 2, 1)
)
xfRadioLinkPtpModemCompleteGroup.setObjects(
      *(("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUAlarmStatus"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUModIndexNotValid"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUAtpcCapability"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUModCapability"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUCapacityCapability"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUProtectionPath"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUSlotPosition"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelModeCapability"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelCompanionSlot"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelCompanionIndex"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUInterfaceCapability"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFLoopEnable"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFRxLoop"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFAlarms"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRAUIFStatus"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfLINERSAlarms"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelSpacing"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUChannelModulation"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUMaxTribCapacity"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUDCNCapacity"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUMaxCapacity"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUFrameFormatType"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMUFrameFormatRev"),
        ("XF-RADIOLINK-PTP-MODEM-MIB", "xfMMURAUSupplyVoltage"))
)
if mibBuilder.loadTexts:
    xfRadioLinkPtpModemCompleteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xfRadioLinkPtpModemFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 2, 2, 1, 1)
)
xfRadioLinkPtpModemFullCompliance.setObjects(
    ("XF-RADIOLINK-PTP-MODEM-MIB", "xfRadioLinkPtpModemCompleteGroup")
)
if mibBuilder.loadTexts:
    xfRadioLinkPtpModemFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XF-RADIOLINK-PTP-MODEM-MIB",
    **{"MMUAlarmStatus": MMUAlarmStatus,
       "MMUModIndexStatus": MMUModIndexStatus,
       "MMUAtpcCapability": MMUAtpcCapability,
       "MMUModCapability": MMUModCapability,
       "MMUCapCapability": MMUCapCapability,
       "MMUChannelSpacingCapability": MMUChannelSpacingCapability,
       "MMUFrameFormatType": MMUFrameFormatType,
       "ModemModulation": ModemModulation,
       "xfRadioLinkPtpModemMIB": xfRadioLinkPtpModemMIB,
       "xfRadioLinkPtpModemObjects": xfRadioLinkPtpModemObjects,
       "xfModemTable": xfModemTable,
       "xfModemEntry": xfModemEntry,
       "xfMMUAlarmStatus": xfMMUAlarmStatus,
       "xfMMUModIndexNotValid": xfMMUModIndexNotValid,
       "xfMMUAtpcCapability": xfMMUAtpcCapability,
       "xfMMUModCapability": xfMMUModCapability,
       "xfMMUCapacityCapability": xfMMUCapacityCapability,
       "xfMMUProtectionPath": xfMMUProtectionPath,
       "xfMMUSlotPosition": xfMMUSlotPosition,
       "xfMMUChannelModeCapability": xfMMUChannelModeCapability,
       "xfMMUChannelCompanionSlot": xfMMUChannelCompanionSlot,
       "xfMMUChannelCompanionIndex": xfMMUChannelCompanionIndex,
       "xfMMUInterfaceCapability": xfMMUInterfaceCapability,
       "xfMMURAUSupplyVoltage": xfMMURAUSupplyVoltage,
       "xfRAUIFTable": xfRAUIFTable,
       "xfRAUIFEntry": xfRAUIFEntry,
       "xfRAUIFLoopEnable": xfRAUIFLoopEnable,
       "xfRAUIFRxLoop": xfRAUIFRxLoop,
       "xfRAUIFAlarms": xfRAUIFAlarms,
       "xfRAUIFStatus": xfRAUIFStatus,
       "xfLINERSTable": xfLINERSTable,
       "xfLINERSEntry": xfLINERSEntry,
       "xfLINERSAlarms": xfLINERSAlarms,
       "xfModemCapabilityTable": xfModemCapabilityTable,
       "xfModemCapabilityEntry": xfModemCapabilityEntry,
       "xfMMUChannelSpacing": xfMMUChannelSpacing,
       "xfMMUChannelModulation": xfMMUChannelModulation,
       "xfMMUMaxTribCapacity": xfMMUMaxTribCapacity,
       "xfMMUDCNCapacity": xfMMUDCNCapacity,
       "xfMMUMaxCapacity": xfMMUMaxCapacity,
       "xfMMUFrameFormatType": xfMMUFrameFormatType,
       "xfMMUFrameFormatRev": xfMMUFrameFormatRev,
       "xfMMUBerAlarmThresholdCapability": xfMMUBerAlarmThresholdCapability,
       "xfRadioLinkPtpModemConformance": xfRadioLinkPtpModemConformance,
       "xfRadioLinkPtpModemCompliances": xfRadioLinkPtpModemCompliances,
       "xfRadioLinkPtpModemFullCompliance": xfRadioLinkPtpModemFullCompliance,
       "xfRadioLinkPtpModemGroups": xfRadioLinkPtpModemGroups,
       "xfRadioLinkPtpModemCompleteGroup": xfRadioLinkPtpModemCompleteGroup}
)
