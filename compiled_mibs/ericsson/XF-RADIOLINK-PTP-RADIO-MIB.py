# SNMP MIB module (XF-RADIOLINK-PTP-RADIO-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\XF-RADIOLINK-PTP-RADIO-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:42:47 2025
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

xfRadioLinkPtpRadioMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3)
)
if mibBuilder.loadTexts:
    xfRadioLinkPtpRadioMIB.setRevisions(
        ("2020-09-22 00:00",
         "2019-11-26 00:00",
         "2019-10-14 00:00",
         "2019-06-04 00:00",
         "2019-05-16 00:00",
         "2019-04-30 00:00",
         "2019-01-17 00:00",
         "2018-10-29 00:00",
         "2018-09-03 00:00",
         "2018-04-06 00:00",
         "2018-01-30 00:00",
         "2017-11-23 00:00",
         "2017-09-19 00:00",
         "2017-09-05 00:00",
         "2017-07-25 00:00",
         "2017-06-28 00:00",
         "2017-05-24 00:00",
         "2016-12-20 00:00",
         "2016-06-16 00:00",
         "2016-06-01 00:00",
         "2016-05-16 00:00",
         "2016-05-10 00:00",
         "2016-04-12 00:00",
         "2016-02-22 00:00",
         "2016-02-06 00:00",
         "2016-02-05 00:00",
         "2015-12-11 00:00",
         "2015-11-05 00:00",
         "2015-08-31 00:00",
         "2015-07-02 00:00",
         "2015-06-25 00:00",
         "2015-06-08 00:00",
         "2015-04-23 00:00",
         "2015-04-20 00:00",
         "2015-04-02 00:00",
         "2015-02-26 00:00",
         "2015-01-23 10:00",
         "2015-01-23 00:00",
         "2015-01-09 00:00",
         "2014-02-20 00:00",
         "2013-11-22 00:00",
         "2013-11-19 14:00",
         "2011-05-23 00:00",
         "2011-02-09 00:00",
         "2011-02-01 00:00",
         "2010-12-10 00:00",
         "2010-10-20 00:00",
         "2010-09-23 00:00",
         "2010-06-15 00:00",
         "2010-06-04 00:00",
         "2010-01-19 00:00",
         "2009-12-01 00:00",
         "2009-11-18 00:00",
         "2009-06-26 00:00",
         "2009-06-24 00:00",
         "2009-04-20 00:00",
         "2009-04-14 00:00",
         "2008-10-02 00:00",
         "2008-09-16 00:00",
         "2008-06-25 00:00",
         "2008-06-24 00:00",
         "2008-06-18 00:00",
         "2008-06-17 00:00",
         "2008-06-04 00:00",
         "2007-06-04 00:00",
         "2006-09-19 13:20",
         "2006-08-29 00:00",
         "2006-03-20 00:00",
         "2006-02-24 00:00",
         "2006-01-31 00:00",
         "2004-12-13 00:00",
         "2004-07-02 00:00",
         "2004-06-16 00:00",
         "2004-05-25 00:00",
         "2004-04-26 00:00",
         "2004-01-20 00:00",
         "2003-12-17 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RFTxOperStatus(TextualConvention, Integer32):
    status = "current"
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
          ("txOff", 2),
          ("txOn", 3),
          ("txStandby", 4))
    )



class RAURfLoopAvailable(TextualConvention, Integer32):
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
          ("rfLoopAvailable", 2),
          ("rfLoopNotAvailable", 3))
    )



class RAUAtpcCapability(TextualConvention, Integer32):
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
        *(("other", 1),
          ("noAtpcSupport", 2),
          ("doesNotExist", 3),
          ("atpcCapabilityUnknown", 4),
          ("supportsAtpc", 5))
    )



class RAUModCapability(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("cqpsk", 0),
          ("qam16", 1),
          ("qam128", 2),
          ("qam32", 3),
          ("qam64", 4))
    )


class RAUChannelSpacingCapability(TextualConvention, Integer32):
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
              10,
              11)
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
          ("chsp3500KHz", 10),
          ("chsp60MHz", 11))
    )



class RauSec(TextualConvention, Integer32):
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("sec2", 2),
          ("sec3", 3),
          ("sec4L", 4),
          ("sec4H", 5),
          ("sec5A", 6),
          ("sec5B", 7),
          ("sec6A", 8),
          ("sec6B", 9))
    )



class RAUModulation(TextualConvention, Integer32):
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



class ATPCFallbackEnable(TextualConvention, Integer32):
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
          ("disable", 2),
          ("enable", 3))
    )



class RfOutputPower(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )



class RfInputPower(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )



class BoosterCapability(TextualConvention, Integer32):
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
          ("noBoosterSupport", 2),
          ("boosterSupport", 3))
    )



# MIB Managed Objects in the order of their OIDs

_XfRadioLinkPtpRadioObjects_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpRadioObjects = _XfRadioLinkPtpRadioObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1)
)
_XfRAUTable_Object = MibTable
xfRAUTable = _XfRAUTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1)
)
if mibBuilder.loadTexts:
    xfRAUTable.setStatus("current")
_XfRAUEntry_Object = MibTableRow
xfRAUEntry = _XfRAUEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1)
)
xfRAUEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xfRAUEntry.setStatus("current")


class _XfRAUAlarmStatus_Type(Bits):
    """Custom type xfRAUAlarmStatus based on Bits"""
    namedValues = NamedValues(
        *(("atpcCapability0", 0),
          ("atpcCapability1", 1),
          ("atpcCapability2", 2),
          ("configurationInvalid0", 3),
          ("configurationInvalid1", 4),
          ("configurationInvalid2", 5),
          ("sdcHwErrorMain0", 6),
          ("sdcHwErrorMain1", 7),
          ("sdcHwErrorMain2", 8),
          ("sdcHwErrorDiv0", 9),
          ("sdcHwErrorDiv1", 10),
          ("sdcHwErrorDiv2", 11),
          ("sdcDadeCalMismatch0", 12),
          ("sdcDadeCalMismatch1", 13),
          ("sdcDadeCalMismatch2", 14),
          ("insufficientResourceRauXpic0", 15),
          ("insufficientResourceRauXpic1", 16),
          ("insufficientResourceRauXpic2", 17),
          ("companionRauMismatch0", 18),
          ("companionRauMismatch1", 19),
          ("companionRauMismatch2", 20))
    )

_XfRAUAlarmStatus_Type.__name__ = "Bits"
_XfRAUAlarmStatus_Object = MibTableColumn
xfRAUAlarmStatus = _XfRAUAlarmStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 1),
    _XfRAUAlarmStatus_Type()
)
xfRAUAlarmStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUAlarmStatus.setStatus("current")
_XfRAURfLoopAvailable_Type = RAURfLoopAvailable
_XfRAURfLoopAvailable_Object = MibTableColumn
xfRAURfLoopAvailable = _XfRAURfLoopAvailable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 2),
    _XfRAURfLoopAvailable_Type()
)
xfRAURfLoopAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAURfLoopAvailable.setStatus("current")
_XfRAUAtpcCapability_Type = RAUAtpcCapability
_XfRAUAtpcCapability_Object = MibTableColumn
xfRAUAtpcCapability = _XfRAUAtpcCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 3),
    _XfRAUAtpcCapability_Type()
)
xfRAUAtpcCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUAtpcCapability.setStatus("current")


class _XfRAULocalCtrlCapability_Type(Integer32):
    """Custom type xfRAULocalCtrlCapability based on Integer32"""
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
          ("noLocalControlSupport", 2),
          ("supportsLocalControl", 3))
    )


_XfRAULocalCtrlCapability_Type.__name__ = "Integer32"
_XfRAULocalCtrlCapability_Object = MibTableColumn
xfRAULocalCtrlCapability = _XfRAULocalCtrlCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 4),
    _XfRAULocalCtrlCapability_Type()
)
xfRAULocalCtrlCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAULocalCtrlCapability.setStatus("current")
_XfRAUModCapability_Type = RAUModCapability
_XfRAUModCapability_Object = MibTableColumn
xfRAUModCapability = _XfRAUModCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 5),
    _XfRAUModCapability_Type()
)
xfRAUModCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUModCapability.setStatus("current")


class _XfRAUFrequencyband_Type(Unsigned32):
    """Custom type xfRAUFrequencyband based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XfRAUFrequencyband_Type.__name__ = "Unsigned32"
_XfRAUFrequencyband_Object = MibTableColumn
xfRAUFrequencyband = _XfRAUFrequencyband_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 6),
    _XfRAUFrequencyband_Type()
)
xfRAUFrequencyband.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUFrequencyband.setStatus("current")


class _XfRAUSubBand_Type(Unsigned32):
    """Custom type xfRAUSubBand based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XfRAUSubBand_Type.__name__ = "Unsigned32"
_XfRAUSubBand_Object = MibTableColumn
xfRAUSubBand = _XfRAUSubBand_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 7),
    _XfRAUSubBand_Type()
)
xfRAUSubBand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRAUSubBand.setStatus("current")


class _XfRAUTemperature_Type(Integer32):
    """Custom type xfRAUTemperature based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-127, 127),
    )


_XfRAUTemperature_Type.__name__ = "Integer32"
_XfRAUTemperature_Object = MibTableColumn
xfRAUTemperature = _XfRAUTemperature_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 8),
    _XfRAUTemperature_Type()
)
xfRAUTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUTemperature.setStatus("current")


class _XfRAUProtectionPath_Type(Integer32):
    """Custom type xfRAUProtectionPath based on Integer32"""
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
          ("rauRa1", 2),
          ("rauRa2", 3))
    )


_XfRAUProtectionPath_Type.__name__ = "Integer32"
_XfRAUProtectionPath_Object = MibTableColumn
xfRAUProtectionPath = _XfRAUProtectionPath_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 9),
    _XfRAUProtectionPath_Type()
)
xfRAUProtectionPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUProtectionPath.setStatus("current")


class _XfRAURxCapability_Type(Integer32):
    """Custom type xfRAURxCapability based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("rxSupport", 2))
    )


_XfRAURxCapability_Type.__name__ = "Integer32"
_XfRAURxCapability_Object = MibTableColumn
xfRAURxCapability = _XfRAURxCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 10),
    _XfRAURxCapability_Type()
)
xfRAURxCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAURxCapability.setStatus("current")


class _XfRAUNotes_Type(OctetString):
    """Custom type xfRAUNotes based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 800),
    )


_XfRAUNotes_Type.__name__ = "OctetString"
_XfRAUNotes_Object = MibTableColumn
xfRAUNotes = _XfRAUNotes_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 11),
    _XfRAUNotes_Type()
)
xfRAUNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRAUNotes.setStatus("current")


class _XfRauAtpcVersion_Type(Integer32):
    """Custom type xfRauAtpcVersion based on Integer32"""
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
          ("version1", 2),
          ("version2", 3),
          ("version3", 4))
    )


_XfRauAtpcVersion_Type.__name__ = "Integer32"
_XfRauAtpcVersion_Object = MibTableColumn
xfRauAtpcVersion = _XfRauAtpcVersion_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 12),
    _XfRauAtpcVersion_Type()
)
xfRauAtpcVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRauAtpcVersion.setStatus("current")
_XfRauBoosterCapability_Type = BoosterCapability
_XfRauBoosterCapability_Object = MibTableColumn
xfRauBoosterCapability = _XfRauBoosterCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 13),
    _XfRauBoosterCapability_Type()
)
xfRauBoosterCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRauBoosterCapability.setStatus("current")


class _XfRauBoosterSelectedIndex_Type(Integer32):
    """Custom type xfRauBoosterSelectedIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_XfRauBoosterSelectedIndex_Type.__name__ = "Integer32"
_XfRauBoosterSelectedIndex_Object = MibTableColumn
xfRauBoosterSelectedIndex = _XfRauBoosterSelectedIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 1, 1, 14),
    _XfRauBoosterSelectedIndex_Type()
)
xfRauBoosterSelectedIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRauBoosterSelectedIndex.setStatus("current")
_XfRFIFTable_Object = MibTable
xfRFIFTable = _XfRFIFTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2)
)
if mibBuilder.loadTexts:
    xfRFIFTable.setStatus("current")
_XfRFIFEntry_Object = MibTableRow
xfRFIFEntry = _XfRFIFEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1)
)
xfRFIFEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRFIFEntry.setStatus("current")


class _XfRFBaseTxFrequency_Type(Unsigned32):
    """Custom type xfRFBaseTxFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFBaseTxFrequency_Type.__name__ = "Unsigned32"
_XfRFBaseTxFrequency_Object = MibTableColumn
xfRFBaseTxFrequency = _XfRFBaseTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 1),
    _XfRFBaseTxFrequency_Type()
)
xfRFBaseTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFBaseTxFrequency.setStatus("current")


class _XfRFBaseRxFrequency_Type(Unsigned32):
    """Custom type xfRFBaseRxFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFBaseRxFrequency_Type.__name__ = "Unsigned32"
_XfRFBaseRxFrequency_Object = MibTableColumn
xfRFBaseRxFrequency = _XfRFBaseRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 2),
    _XfRFBaseRxFrequency_Type()
)
xfRFBaseRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFBaseRxFrequency.setStatus("current")


class _XfRFStepSize_Type(Unsigned32):
    """Custom type xfRFStepSize based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFStepSize_Type.__name__ = "Unsigned32"
_XfRFStepSize_Object = MibTableColumn
xfRFStepSize = _XfRFStepSize_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 3),
    _XfRFStepSize_Type()
)
xfRFStepSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFStepSize.setStatus("current")


class _XfRFStepLimitLow_Type(Unsigned32):
    """Custom type xfRFStepLimitLow based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFStepLimitLow_Type.__name__ = "Unsigned32"
_XfRFStepLimitLow_Object = MibTableColumn
xfRFStepLimitLow = _XfRFStepLimitLow_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 4),
    _XfRFStepLimitLow_Type()
)
xfRFStepLimitLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFStepLimitLow.setStatus("current")


class _XfRFStepLimitHigh_Type(Unsigned32):
    """Custom type xfRFStepLimitHigh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFStepLimitHigh_Type.__name__ = "Unsigned32"
_XfRFStepLimitHigh_Object = MibTableColumn
xfRFStepLimitHigh = _XfRFStepLimitHigh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 5),
    _XfRFStepLimitHigh_Type()
)
xfRFStepLimitHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFStepLimitHigh.setStatus("current")


class _XfRFCurrentStepNumber_Type(Unsigned32):
    """Custom type xfRFCurrentStepNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFCurrentStepNumber_Type.__name__ = "Unsigned32"
_XfRFCurrentStepNumber_Object = MibTableColumn
xfRFCurrentStepNumber = _XfRFCurrentStepNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 6),
    _XfRFCurrentStepNumber_Type()
)
xfRFCurrentStepNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFCurrentStepNumber.setStatus("current")
_XfRFTxOperStatus_Type = RFTxOperStatus
_XfRFTxOperStatus_Object = MibTableColumn
xfRFTxOperStatus = _XfRFTxOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 7),
    _XfRFTxOperStatus_Type()
)
xfRFTxOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFTxOperStatus.setStatus("current")


class _XfRFTxAdminStatus_Type(Integer32):
    """Custom type xfRFTxAdminStatus based on Integer32"""
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
          ("txOff", 2),
          ("txOn", 3))
    )


_XfRFTxAdminStatus_Type.__name__ = "Integer32"
_XfRFTxAdminStatus_Object = MibTableColumn
xfRFTxAdminStatus = _XfRFTxAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 8),
    _XfRFTxAdminStatus_Type()
)
xfRFTxAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFTxAdminStatus.setStatus("current")


class _XfRFLoopEnable_Type(Integer32):
    """Custom type xfRFLoopEnable based on Integer32"""
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


_XfRFLoopEnable_Type.__name__ = "Integer32"
_XfRFLoopEnable_Object = MibTableColumn
xfRFLoopEnable = _XfRFLoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 9),
    _XfRFLoopEnable_Type()
)
xfRFLoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFLoopEnable.setStatus("current")


class _XfRFAlarms_Type(Bits):
    """Custom type xfRFAlarms based on Bits"""
    namedValues = NamedValues(
        *(("txFrequency0", 0),
          ("txFrequency1", 1),
          ("txFrequency2", 2),
          ("rxFrequency0", 3),
          ("rxFrequency1", 4),
          ("rxFrequency2", 5),
          ("rfOutputLevel0", 6),
          ("rfOutputLevel1", 7),
          ("rfOutputLevel2", 8),
          ("rxAfc0", 9),
          ("rxAfc1", 10),
          ("rxAfc2", 11),
          ("rfInputLevel0", 12),
          ("rfInputLevel1", 13),
          ("rfInputLevel2", 14),
          ("rfInputThreshold0", 15),
          ("rfInputThreshold1", 16),
          ("rfInputThreshold2", 17),
          ("rfOutputLevelATPC0", 18),
          ("rfOutputLevelATPC1", 19),
          ("rfOutputLevelATPC2", 20),
          ("sdcRfInputLevelMain0", 21),
          ("sdcRfInputLevelMain1", 22),
          ("sdcRfInputLevelMain2", 23),
          ("sdcRfInputLevelDiv0", 24),
          ("sdcRfInputLevelDiv1", 25),
          ("sdcRfInputLevelDiv2", 26),
          ("rlts1Counter15m0", 27),
          ("rlts1Counter15m1", 28),
          ("rlts1Counter15m2", 29),
          ("rlts2Counter15m0", 30),
          ("rlts2Counter15m1", 31),
          ("rlts2Counter15m2", 32),
          ("rltmCounter15m0", 33),
          ("rltmCounter15m1", 34),
          ("rltmCounter15m2", 35),
          ("tlts1Counter15m0", 36),
          ("tlts1Counter15m1", 37),
          ("tlts1Counter15m2", 38),
          ("tltmCounter15m0", 39),
          ("tltmCounter15m1", 40),
          ("tltmCounter15m2", 41),
          ("rlts1Counter24h0", 42),
          ("rlts1Counter24h1", 43),
          ("rlts1Counter24h2", 44),
          ("rlts2Counter24h0", 45),
          ("rlts2Counter24h1", 46),
          ("rlts2Counter24h2", 47),
          ("rltmCounter24h0", 48),
          ("rltmCounter24h1", 49),
          ("rltmCounter24h2", 50),
          ("tlts1Counter24h0", 51),
          ("tlts1Counter24h1", 52),
          ("tlts1Counter24h2", 53),
          ("tltmCounter24h0", 54),
          ("tltmCounter24h1", 55),
          ("tltmCounter24h2", 56),
          ("remoteRfIfHighestSeverityAlarm0", 57),
          ("remoteRfIfHighestSeverityAlarm1", 58),
          ("remoteRfIfHighestSeverityAlarm2", 59),
          ("ifcabledamaged0", 60),
          ("ifcabledamaged1", 61),
          ("ifcabledamaged2", 62))
    )

_XfRFAlarms_Type.__name__ = "Bits"
_XfRFAlarms_Object = MibTableColumn
xfRFAlarms = _XfRFAlarms_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 10),
    _XfRFAlarms_Type()
)
xfRFAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFAlarms.setStatus("current")


class _XfRFStatus_Type(Bits):
    """Custom type xfRFStatus based on Bits"""
    namedValues = NamedValues(
        *(("rfLoop0", 0),
          ("rfLoop1", 1),
          ("rfLoop2", 2),
          ("txOff0", 3),
          ("txOff1", 4),
          ("txOff2", 5))
    )

_XfRFStatus_Type.__name__ = "Bits"
_XfRFStatus_Object = MibTableColumn
xfRFStatus = _XfRFStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 11),
    _XfRFStatus_Type()
)
xfRFStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFStatus.setStatus("current")


class _XfRFStepSizeRx_Type(Unsigned32):
    """Custom type xfRFStepSizeRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFStepSizeRx_Type.__name__ = "Unsigned32"
_XfRFStepSizeRx_Object = MibTableColumn
xfRFStepSizeRx = _XfRFStepSizeRx_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 12),
    _XfRFStepSizeRx_Type()
)
xfRFStepSizeRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFStepSizeRx.setStatus("current")


class _XfRFStepLimitLowRx_Type(Unsigned32):
    """Custom type xfRFStepLimitLowRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFStepLimitLowRx_Type.__name__ = "Unsigned32"
_XfRFStepLimitLowRx_Object = MibTableColumn
xfRFStepLimitLowRx = _XfRFStepLimitLowRx_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 13),
    _XfRFStepLimitLowRx_Type()
)
xfRFStepLimitLowRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFStepLimitLowRx.setStatus("current")


class _XfRFStepLimitHighRx_Type(Unsigned32):
    """Custom type xfRFStepLimitHighRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFStepLimitHighRx_Type.__name__ = "Unsigned32"
_XfRFStepLimitHighRx_Object = MibTableColumn
xfRFStepLimitHighRx = _XfRFStepLimitHighRx_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 14),
    _XfRFStepLimitHighRx_Type()
)
xfRFStepLimitHighRx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFStepLimitHighRx.setStatus("current")


class _XfRFCurrentStepNumberRx_Type(Unsigned32):
    """Custom type xfRFCurrentStepNumberRx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFCurrentStepNumberRx_Type.__name__ = "Unsigned32"
_XfRFCurrentStepNumberRx_Object = MibTableColumn
xfRFCurrentStepNumberRx = _XfRFCurrentStepNumberRx_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 15),
    _XfRFCurrentStepNumberRx_Type()
)
xfRFCurrentStepNumberRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFCurrentStepNumberRx.setStatus("current")


class _XfRFDuplexType_Type(Integer32):
    """Custom type xfRFDuplexType based on Integer32"""
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
          ("fixed", 2),
          ("variable", 3))
    )


_XfRFDuplexType_Type.__name__ = "Integer32"
_XfRFDuplexType_Object = MibTableColumn
xfRFDuplexType = _XfRFDuplexType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 16),
    _XfRFDuplexType_Type()
)
xfRFDuplexType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFDuplexType.setStatus("current")


class _XfRFDuplexConfig_Type(Integer32):
    """Custom type xfRFDuplexConfig based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3))
    )


_XfRFDuplexConfig_Type.__name__ = "Integer32"
_XfRFDuplexConfig_Object = MibTableColumn
xfRFDuplexConfig = _XfRFDuplexConfig_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 17),
    _XfRFDuplexConfig_Type()
)
xfRFDuplexConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFDuplexConfig.setStatus("current")


class _XfRFDuplexDistance_Type(Integer32):
    """Custom type xfRFDuplexDistance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_XfRFDuplexDistance_Type.__name__ = "Integer32"
_XfRFDuplexDistance_Object = MibTableColumn
xfRFDuplexDistance = _XfRFDuplexDistance_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 2, 1, 18),
    _XfRFDuplexDistance_Type()
)
xfRFDuplexDistance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFDuplexDistance.setStatus("current")
_XfRFPowerTable_Object = MibTable
xfRFPowerTable = _XfRFPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3)
)
if mibBuilder.loadTexts:
    xfRFPowerTable.setStatus("current")
_XfRFPowerEntry_Object = MibTableRow
xfRFPowerEntry = _XfRFPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1)
)
xfRFPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRFPowerEntry.setStatus("current")


class _XfRFCurrentOutputPower_Type(Integer32):
    """Custom type xfRFCurrentOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRFCurrentOutputPower_Type.__name__ = "Integer32"
_XfRFCurrentOutputPower_Object = MibTableColumn
xfRFCurrentOutputPower = _XfRFCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 1),
    _XfRFCurrentOutputPower_Type()
)
xfRFCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFCurrentOutputPower.setStatus("current")


class _XfRFRtpcMinOutputPower_Type(Integer32):
    """Custom type xfRFRtpcMinOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRFRtpcMinOutputPower_Type.__name__ = "Integer32"
_XfRFRtpcMinOutputPower_Object = MibTableColumn
xfRFRtpcMinOutputPower = _XfRFRtpcMinOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 2),
    _XfRFRtpcMinOutputPower_Type()
)
xfRFRtpcMinOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFRtpcMinOutputPower.setStatus("current")


class _XfRFRtpcMaxOutputPower_Type(Integer32):
    """Custom type xfRFRtpcMaxOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRFRtpcMaxOutputPower_Type.__name__ = "Integer32"
_XfRFRtpcMaxOutputPower_Object = MibTableColumn
xfRFRtpcMaxOutputPower = _XfRFRtpcMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 3),
    _XfRFRtpcMaxOutputPower_Type()
)
xfRFRtpcMaxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFRtpcMaxOutputPower.setStatus("current")


class _XfRFRtpcSelectedOutputPower_Type(Integer32):
    """Custom type xfRFRtpcSelectedOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(254, 254),
    )


_XfRFRtpcSelectedOutputPower_Type.__name__ = "Integer32"
_XfRFRtpcSelectedOutputPower_Object = MibTableColumn
xfRFRtpcSelectedOutputPower = _XfRFRtpcSelectedOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 4),
    _XfRFRtpcSelectedOutputPower_Type()
)
xfRFRtpcSelectedOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFRtpcSelectedOutputPower.setStatus("current")


class _XfRFAtpcMinOutputPower_Type(Integer32):
    """Custom type xfRFAtpcMinOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRFAtpcMinOutputPower_Type.__name__ = "Integer32"
_XfRFAtpcMinOutputPower_Object = MibTableColumn
xfRFAtpcMinOutputPower = _XfRFAtpcMinOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 5),
    _XfRFAtpcMinOutputPower_Type()
)
xfRFAtpcMinOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFAtpcMinOutputPower.setStatus("current")


class _XfRFAtpcMaxOutputPower_Type(Integer32):
    """Custom type xfRFAtpcMaxOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(254, 254),
    )


_XfRFAtpcMaxOutputPower_Type.__name__ = "Integer32"
_XfRFAtpcMaxOutputPower_Object = MibTableColumn
xfRFAtpcMaxOutputPower = _XfRFAtpcMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 6),
    _XfRFAtpcMaxOutputPower_Type()
)
xfRFAtpcMaxOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFAtpcMaxOutputPower.setStatus("current")


class _XfRFAtpcMinInputPowerFar_Type(Integer32):
    """Custom type xfRFAtpcMinInputPowerFar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -30),
        ValueRangeConstraint(255, 255),
    )


_XfRFAtpcMinInputPowerFar_Type.__name__ = "Integer32"
_XfRFAtpcMinInputPowerFar_Object = MibTableColumn
xfRFAtpcMinInputPowerFar = _XfRFAtpcMinInputPowerFar_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 7),
    _XfRFAtpcMinInputPowerFar_Type()
)
xfRFAtpcMinInputPowerFar.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFAtpcMinInputPowerFar.setStatus("current")


class _XfRFAtpcSelectedInputPowerFar_Type(Integer32):
    """Custom type xfRFAtpcSelectedInputPowerFar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -30),
    )


_XfRFAtpcSelectedInputPowerFar_Type.__name__ = "Integer32"
_XfRFAtpcSelectedInputPowerFar_Object = MibTableColumn
xfRFAtpcSelectedInputPowerFar = _XfRFAtpcSelectedInputPowerFar_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 8),
    _XfRFAtpcSelectedInputPowerFar_Type()
)
xfRFAtpcSelectedInputPowerFar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFAtpcSelectedInputPowerFar.setStatus("current")


class _XfRFAttenuator_Type(Integer32):
    """Custom type xfRFAttenuator based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XfRFAttenuator_Type.__name__ = "Integer32"
_XfRFAttenuator_Object = MibTableColumn
xfRFAttenuator = _XfRFAttenuator_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 9),
    _XfRFAttenuator_Type()
)
xfRFAttenuator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFAttenuator.setStatus("current")


class _XfRFCurrentInputPower_Type(Integer32):
    """Custom type xfRFCurrentInputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
    )


_XfRFCurrentInputPower_Type.__name__ = "Integer32"
_XfRFCurrentInputPower_Object = MibTableColumn
xfRFCurrentInputPower = _XfRFCurrentInputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 10),
    _XfRFCurrentInputPower_Type()
)
xfRFCurrentInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFCurrentInputPower.setStatus("current")


class _XfRFMaxInputPowerLast7Days_Type(Integer32):
    """Custom type xfRFMaxInputPowerLast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfRFMaxInputPowerLast7Days_Type.__name__ = "Integer32"
_XfRFMaxInputPowerLast7Days_Object = MibTableColumn
xfRFMaxInputPowerLast7Days = _XfRFMaxInputPowerLast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 11),
    _XfRFMaxInputPowerLast7Days_Type()
)
xfRFMaxInputPowerLast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMaxInputPowerLast7Days.setStatus("current")


class _XfRFMinInputPowerLast7Days_Type(Integer32):
    """Custom type xfRFMinInputPowerLast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfRFMinInputPowerLast7Days_Type.__name__ = "Integer32"
_XfRFMinInputPowerLast7Days_Object = MibTableColumn
xfRFMinInputPowerLast7Days = _XfRFMinInputPowerLast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 12),
    _XfRFMinInputPowerLast7Days_Type()
)
xfRFMinInputPowerLast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMinInputPowerLast7Days.setStatus("current")


class _XfRFMaxInputPowerSinceReset_Type(Integer32):
    """Custom type xfRFMaxInputPowerSinceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
    )


_XfRFMaxInputPowerSinceReset_Type.__name__ = "Integer32"
_XfRFMaxInputPowerSinceReset_Object = MibTableColumn
xfRFMaxInputPowerSinceReset = _XfRFMaxInputPowerSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 13),
    _XfRFMaxInputPowerSinceReset_Type()
)
xfRFMaxInputPowerSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMaxInputPowerSinceReset.setStatus("current")


class _XfRFMinInputPowerSinceReset_Type(Integer32):
    """Custom type xfRFMinInputPowerSinceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
    )


_XfRFMinInputPowerSinceReset_Type.__name__ = "Integer32"
_XfRFMinInputPowerSinceReset_Object = MibTableColumn
xfRFMinInputPowerSinceReset = _XfRFMinInputPowerSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 14),
    _XfRFMinInputPowerSinceReset_Type()
)
xfRFMinInputPowerSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMinInputPowerSinceReset.setStatus("current")


class _XfRFInputPowerReset_Type(Integer32):
    """Custom type xfRFInputPowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("inputPowerReset", 1)
    )


_XfRFInputPowerReset_Type.__name__ = "Integer32"
_XfRFInputPowerReset_Object = MibTableColumn
xfRFInputPowerReset = _XfRFInputPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 15),
    _XfRFInputPowerReset_Type()
)
xfRFInputPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFInputPowerReset.setStatus("current")


class _XfRFInputAlarmThreshold_Type(Integer32):
    """Custom type xfRFInputAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -30),
    )


_XfRFInputAlarmThreshold_Type.__name__ = "Integer32"
_XfRFInputAlarmThreshold_Object = MibTableColumn
xfRFInputAlarmThreshold = _XfRFInputAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 16),
    _XfRFInputAlarmThreshold_Type()
)
xfRFInputAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFInputAlarmThreshold.setStatus("current")
_XfRFOutputPower4QAM_Type = Integer32
_XfRFOutputPower4QAM_Object = MibTableColumn
xfRFOutputPower4QAM = _XfRFOutputPower4QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 17),
    _XfRFOutputPower4QAM_Type()
)
xfRFOutputPower4QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutputPower4QAM.setStatus("current")
_XfRFOutputPower8QAM_Type = Integer32
_XfRFOutputPower8QAM_Object = MibTableColumn
xfRFOutputPower8QAM = _XfRFOutputPower8QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 18),
    _XfRFOutputPower8QAM_Type()
)
xfRFOutputPower8QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutputPower8QAM.setStatus("current")
_XfRFOutputPower16QAM_Type = Integer32
_XfRFOutputPower16QAM_Object = MibTableColumn
xfRFOutputPower16QAM = _XfRFOutputPower16QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 19),
    _XfRFOutputPower16QAM_Type()
)
xfRFOutputPower16QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutputPower16QAM.setStatus("current")
_XfRFOutputPower32QAM_Type = Integer32
_XfRFOutputPower32QAM_Object = MibTableColumn
xfRFOutputPower32QAM = _XfRFOutputPower32QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 20),
    _XfRFOutputPower32QAM_Type()
)
xfRFOutputPower32QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutputPower32QAM.setStatus("current")
_XfRFOutputPower64QAM_Type = Integer32
_XfRFOutputPower64QAM_Object = MibTableColumn
xfRFOutputPower64QAM = _XfRFOutputPower64QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 21),
    _XfRFOutputPower64QAM_Type()
)
xfRFOutputPower64QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutputPower64QAM.setStatus("current")
_XfRFOutputPower128QAM_Type = Integer32
_XfRFOutputPower128QAM_Object = MibTableColumn
xfRFOutputPower128QAM = _XfRFOutputPower128QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 22),
    _XfRFOutputPower128QAM_Type()
)
xfRFOutputPower128QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutputPower128QAM.setStatus("current")
_XfRFOutputPower256QAM_Type = Integer32
_XfRFOutputPower256QAM_Object = MibTableColumn
xfRFOutputPower256QAM = _XfRFOutputPower256QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 23),
    _XfRFOutputPower256QAM_Type()
)
xfRFOutputPower256QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutputPower256QAM.setStatus("current")
_XfRFOutputPower512QAM_Type = Integer32
_XfRFOutputPower512QAM_Object = MibTableColumn
xfRFOutputPower512QAM = _XfRFOutputPower512QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 24),
    _XfRFOutputPower512QAM_Type()
)
xfRFOutputPower512QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutputPower512QAM.setStatus("current")


class _XfRFAtpcFallbackOutputPower_Type(Integer32):
    """Custom type xfRFAtpcFallbackOutputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(254, 254),
    )


_XfRFAtpcFallbackOutputPower_Type.__name__ = "Integer32"
_XfRFAtpcFallbackOutputPower_Object = MibTableColumn
xfRFAtpcFallbackOutputPower = _XfRFAtpcFallbackOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 25),
    _XfRFAtpcFallbackOutputPower_Type()
)
xfRFAtpcFallbackOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFAtpcFallbackOutputPower.setStatus("current")
_XfRFAtpcFallbackEnable_Type = ATPCFallbackEnable
_XfRFAtpcFallbackEnable_Object = MibTableColumn
xfRFAtpcFallbackEnable = _XfRFAtpcFallbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 26),
    _XfRFAtpcFallbackEnable_Type()
)
xfRFAtpcFallbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFAtpcFallbackEnable.setStatus("current")


class _XfRFAtpcFallbackTimer_Type(Integer32):
    """Custom type xfRFAtpcFallbackTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_XfRFAtpcFallbackTimer_Type.__name__ = "Integer32"
_XfRFAtpcFallbackTimer_Object = MibTableColumn
xfRFAtpcFallbackTimer = _XfRFAtpcFallbackTimer_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 27),
    _XfRFAtpcFallbackTimer_Type()
)
xfRFAtpcFallbackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFAtpcFallbackTimer.setStatus("current")
_XfRFOutputPower1024QAM_Type = Integer32
_XfRFOutputPower1024QAM_Object = MibTableColumn
xfRFOutputPower1024QAM = _XfRFOutputPower1024QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 28),
    _XfRFOutputPower1024QAM_Type()
)
xfRFOutputPower1024QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutputPower1024QAM.setStatus("current")
_XfRFMaxOutputPowerNotLimited_Type = Integer32
_XfRFMaxOutputPowerNotLimited_Object = MibTableColumn
xfRFMaxOutputPowerNotLimited = _XfRFMaxOutputPowerNotLimited_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 29),
    _XfRFMaxOutputPowerNotLimited_Type()
)
xfRFMaxOutputPowerNotLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMaxOutputPowerNotLimited.setStatus("current")


class _XfRFMaxOutputPowerNotPossible_Type(Integer32):
    """Custom type xfRFMaxOutputPowerNotPossible based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("isPossible", 1),
          ("isNotPossible", 2))
    )


_XfRFMaxOutputPowerNotPossible_Type.__name__ = "Integer32"
_XfRFMaxOutputPowerNotPossible_Object = MibTableColumn
xfRFMaxOutputPowerNotPossible = _XfRFMaxOutputPowerNotPossible_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 30),
    _XfRFMaxOutputPowerNotPossible_Type()
)
xfRFMaxOutputPowerNotPossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMaxOutputPowerNotPossible.setStatus("current")


class _XfRFCurrentInputPowerSdcMain_Type(Integer32):
    """Custom type xfRFCurrentInputPowerSdcMain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfRFCurrentInputPowerSdcMain_Type.__name__ = "Integer32"
_XfRFCurrentInputPowerSdcMain_Object = MibTableColumn
xfRFCurrentInputPowerSdcMain = _XfRFCurrentInputPowerSdcMain_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 31),
    _XfRFCurrentInputPowerSdcMain_Type()
)
xfRFCurrentInputPowerSdcMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFCurrentInputPowerSdcMain.setStatus("current")


class _XfRFCurrentInputPowerSdcDiv_Type(Integer32):
    """Custom type xfRFCurrentInputPowerSdcDiv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfRFCurrentInputPowerSdcDiv_Type.__name__ = "Integer32"
_XfRFCurrentInputPowerSdcDiv_Object = MibTableColumn
xfRFCurrentInputPowerSdcDiv = _XfRFCurrentInputPowerSdcDiv_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 32),
    _XfRFCurrentInputPowerSdcDiv_Type()
)
xfRFCurrentInputPowerSdcDiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFCurrentInputPowerSdcDiv.setStatus("current")


class _XfRFMeanInputPower1m_Type(Integer32):
    """Custom type xfRFMeanInputPower1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfRFMeanInputPower1m_Type.__name__ = "Integer32"
_XfRFMeanInputPower1m_Object = MibTableColumn
xfRFMeanInputPower1m = _XfRFMeanInputPower1m_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 33),
    _XfRFMeanInputPower1m_Type()
)
xfRFMeanInputPower1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMeanInputPower1m.setStatus("current")


class _XfRFMaxOutputPowerLast7Days_Type(Integer32):
    """Custom type xfRFMaxOutputPowerLast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRFMaxOutputPowerLast7Days_Type.__name__ = "Integer32"
_XfRFMaxOutputPowerLast7Days_Object = MibTableColumn
xfRFMaxOutputPowerLast7Days = _XfRFMaxOutputPowerLast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 34),
    _XfRFMaxOutputPowerLast7Days_Type()
)
xfRFMaxOutputPowerLast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMaxOutputPowerLast7Days.setStatus("current")


class _XfRFMinOutputPowerLast7Days_Type(Integer32):
    """Custom type xfRFMinOutputPowerLast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRFMinOutputPowerLast7Days_Type.__name__ = "Integer32"
_XfRFMinOutputPowerLast7Days_Object = MibTableColumn
xfRFMinOutputPowerLast7Days = _XfRFMinOutputPowerLast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 35),
    _XfRFMinOutputPowerLast7Days_Type()
)
xfRFMinOutputPowerLast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMinOutputPowerLast7Days.setStatus("current")


class _XfRFMaxOutputPowerSinceReset_Type(Integer32):
    """Custom type xfRFMaxOutputPowerSinceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRFMaxOutputPowerSinceReset_Type.__name__ = "Integer32"
_XfRFMaxOutputPowerSinceReset_Object = MibTableColumn
xfRFMaxOutputPowerSinceReset = _XfRFMaxOutputPowerSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 36),
    _XfRFMaxOutputPowerSinceReset_Type()
)
xfRFMaxOutputPowerSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMaxOutputPowerSinceReset.setStatus("current")


class _XfRFMinOutputPowerSinceReset_Type(Integer32):
    """Custom type xfRFMinOutputPowerSinceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRFMinOutputPowerSinceReset_Type.__name__ = "Integer32"
_XfRFMinOutputPowerSinceReset_Object = MibTableColumn
xfRFMinOutputPowerSinceReset = _XfRFMinOutputPowerSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 37),
    _XfRFMinOutputPowerSinceReset_Type()
)
xfRFMinOutputPowerSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMinOutputPowerSinceReset.setStatus("current")


class _XfRFMaxMSELast7Days_Type(Integer32):
    """Custom type xfRFMaxMSELast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfRFMaxMSELast7Days_Type.__name__ = "Integer32"
_XfRFMaxMSELast7Days_Object = MibTableColumn
xfRFMaxMSELast7Days = _XfRFMaxMSELast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 38),
    _XfRFMaxMSELast7Days_Type()
)
xfRFMaxMSELast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMaxMSELast7Days.setStatus("current")


class _XfRFMinMSELast7Days_Type(Integer32):
    """Custom type xfRFMinMSELast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfRFMinMSELast7Days_Type.__name__ = "Integer32"
_XfRFMinMSELast7Days_Object = MibTableColumn
xfRFMinMSELast7Days = _XfRFMinMSELast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 39),
    _XfRFMinMSELast7Days_Type()
)
xfRFMinMSELast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMinMSELast7Days.setStatus("current")


class _XfRFMaxXPILast7Days_Type(Integer32):
    """Custom type xfRFMaxXPILast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfRFMaxXPILast7Days_Type.__name__ = "Integer32"
_XfRFMaxXPILast7Days_Object = MibTableColumn
xfRFMaxXPILast7Days = _XfRFMaxXPILast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 40),
    _XfRFMaxXPILast7Days_Type()
)
xfRFMaxXPILast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMaxXPILast7Days.setStatus("current")


class _XfRFMinXPILast7Days_Type(Integer32):
    """Custom type xfRFMinXPILast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfRFMinXPILast7Days_Type.__name__ = "Integer32"
_XfRFMinXPILast7Days_Object = MibTableColumn
xfRFMinXPILast7Days = _XfRFMinXPILast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 41),
    _XfRFMinXPILast7Days_Type()
)
xfRFMinXPILast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMinXPILast7Days.setStatus("current")


class _XfRFOutputPowerReset_Type(Integer32):
    """Custom type xfRFOutputPowerReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("outputPowerReset", 1)
    )


_XfRFOutputPowerReset_Type.__name__ = "Integer32"
_XfRFOutputPowerReset_Object = MibTableColumn
xfRFOutputPowerReset = _XfRFOutputPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 42),
    _XfRFOutputPowerReset_Type()
)
xfRFOutputPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFOutputPowerReset.setStatus("current")


class _XfRFBoosterGain_Type(Integer32):
    """Custom type xfRFBoosterGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XfRFBoosterGain_Type.__name__ = "Integer32"
_XfRFBoosterGain_Object = MibTableColumn
xfRFBoosterGain = _XfRFBoosterGain_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 43),
    _XfRFBoosterGain_Type()
)
xfRFBoosterGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFBoosterGain.setStatus("current")


class _XfRFBoosterMaxInputPower_Type(Integer32):
    """Custom type xfRFBoosterMaxInputPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 35),
        ValueRangeConstraint(255, 255),
    )


_XfRFBoosterMaxInputPower_Type.__name__ = "Integer32"
_XfRFBoosterMaxInputPower_Object = MibTableColumn
xfRFBoosterMaxInputPower = _XfRFBoosterMaxInputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 44),
    _XfRFBoosterMaxInputPower_Type()
)
xfRFBoosterMaxInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFBoosterMaxInputPower.setStatus("current")
_XfRFBoosterCapability_Type = BoosterCapability
_XfRFBoosterCapability_Object = MibTableColumn
xfRFBoosterCapability = _XfRFBoosterCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 45),
    _XfRFBoosterCapability_Type()
)
xfRFBoosterCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFBoosterCapability.setStatus("current")


class _XfRFBoosterProductNumber_Type(DisplayString):
    """Custom type xfRFBoosterProductNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XfRFBoosterProductNumber_Type.__name__ = "DisplayString"
_XfRFBoosterProductNumber_Object = MibTableColumn
xfRFBoosterProductNumber = _XfRFBoosterProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 46),
    _XfRFBoosterProductNumber_Type()
)
xfRFBoosterProductNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFBoosterProductNumber.setStatus("current")


class _XfRFBoosterHWRevision_Type(DisplayString):
    """Custom type xfRFBoosterHWRevision based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_XfRFBoosterHWRevision_Type.__name__ = "DisplayString"
_XfRFBoosterHWRevision_Object = MibTableColumn
xfRFBoosterHWRevision = _XfRFBoosterHWRevision_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 3, 1, 47),
    _XfRFBoosterHWRevision_Type()
)
xfRFBoosterHWRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFBoosterHWRevision.setStatus("current")
_XfRAUCapabilityTable_Object = MibTable
xfRAUCapabilityTable = _XfRAUCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 4)
)
if mibBuilder.loadTexts:
    xfRAUCapabilityTable.setStatus("current")
_XfRAUCapabilityEntry_Object = MibTableRow
xfRAUCapabilityEntry = _XfRAUCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 4, 1)
)
xfRAUCapabilityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRowIndex"),
)
if mibBuilder.loadTexts:
    xfRAUCapabilityEntry.setStatus("current")
_XfRAUChannelSpacing_Type = RAUChannelSpacingCapability
_XfRAUChannelSpacing_Object = MibTableColumn
xfRAUChannelSpacing = _XfRAUChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 4, 1, 1),
    _XfRAUChannelSpacing_Type()
)
xfRAUChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUChannelSpacing.setStatus("current")
_XfRAUChannelModulation_Type = RAUModulation
_XfRAUChannelModulation_Object = MibTableColumn
xfRAUChannelModulation = _XfRAUChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 4, 1, 2),
    _XfRAUChannelModulation_Type()
)
xfRAUChannelModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUChannelModulation.setStatus("current")
_XfRAUSpectrumEfficiencyClass_Type = RauSec
_XfRAUSpectrumEfficiencyClass_Object = MibTableColumn
xfRAUSpectrumEfficiencyClass = _XfRAUSpectrumEfficiencyClass_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 4, 1, 3),
    _XfRAUSpectrumEfficiencyClass_Type()
)
xfRAUSpectrumEfficiencyClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUSpectrumEfficiencyClass.setStatus("current")


class _XfRAUCarrierMode_Type(Integer32):
    """Custom type xfRAUCarrierMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("singleCarrier", 1),
          ("xpicDualCarrier", 2),
          ("mimoMultiCarrier", 3))
    )


_XfRAUCarrierMode_Type.__name__ = "Integer32"
_XfRAUCarrierMode_Object = MibTableColumn
xfRAUCarrierMode = _XfRAUCarrierMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 4, 1, 4),
    _XfRAUCarrierMode_Type()
)
xfRAUCarrierMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUCarrierMode.setStatus("current")
_XfRAUSubBandTable_Object = MibTable
xfRAUSubBandTable = _XfRAUSubBandTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 5)
)
if mibBuilder.loadTexts:
    xfRAUSubBandTable.setStatus("current")
_XfRAUSubBandEntry_Object = MibTableRow
xfRAUSubBandEntry = _XfRAUSubBandEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 5, 1)
)
xfRAUSubBandEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
    (0, "XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUSubBandIndex"),
)
if mibBuilder.loadTexts:
    xfRAUSubBandEntry.setStatus("current")


class _XfRAUSubBandIndex_Type(Unsigned32):
    """Custom type xfRAUSubBandIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_XfRAUSubBandIndex_Type.__name__ = "Unsigned32"
_XfRAUSubBandIndex_Object = MibTableColumn
xfRAUSubBandIndex = _XfRAUSubBandIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 5, 1, 1),
    _XfRAUSubBandIndex_Type()
)
xfRAUSubBandIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUSubBandIndex.setStatus("current")


class _XfRAUSubBandRange_Type(Unsigned32):
    """Custom type xfRAUSubBandRange based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_XfRAUSubBandRange_Type.__name__ = "Unsigned32"
_XfRAUSubBandRange_Object = MibTableColumn
xfRAUSubBandRange = _XfRAUSubBandRange_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 5, 1, 2),
    _XfRAUSubBandRange_Type()
)
xfRAUSubBandRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRAUSubBandRange.setStatus("current")
_XfRFSpectrumDiagTable_Object = MibTable
xfRFSpectrumDiagTable = _XfRFSpectrumDiagTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6)
)
if mibBuilder.loadTexts:
    xfRFSpectrumDiagTable.setStatus("current")
_XfRFSpectrumDiagEntry_Object = MibTableRow
xfRFSpectrumDiagEntry = _XfRFSpectrumDiagEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1)
)
xfRFSpectrumDiagEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRFSpectrumDiagEntry.setStatus("current")


class _XfRFSpectrumDiagAdminStatus_Type(Integer32):
    """Custom type xfRFSpectrumDiagAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("channelScanStart", 2),
          ("subBandScanStart", 3),
          ("scanStop", 255))
    )


_XfRFSpectrumDiagAdminStatus_Type.__name__ = "Integer32"
_XfRFSpectrumDiagAdminStatus_Object = MibTableColumn
xfRFSpectrumDiagAdminStatus = _XfRFSpectrumDiagAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 1),
    _XfRFSpectrumDiagAdminStatus_Type()
)
xfRFSpectrumDiagAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagAdminStatus.setStatus("current")


class _XfRFSpectrumDiagOperStatus_Type(Integer32):
    """Custom type xfRFSpectrumDiagOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("scanNotStarted", 0),
          ("subBandScanOngoing", 1),
          ("channelScanOngoing", 2),
          ("scanCanceled", 3),
          ("subBandScanFinished", 4),
          ("channelScanFinished", 5))
    )


_XfRFSpectrumDiagOperStatus_Type.__name__ = "Integer32"
_XfRFSpectrumDiagOperStatus_Object = MibTableColumn
xfRFSpectrumDiagOperStatus = _XfRFSpectrumDiagOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 2),
    _XfRFSpectrumDiagOperStatus_Type()
)
xfRFSpectrumDiagOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagOperStatus.setStatus("current")


class _XfRFSpectrumDiagChannelScanEstTime_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagChannelScanEstTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagChannelScanEstTime_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagChannelScanEstTime_Object = MibTableColumn
xfRFSpectrumDiagChannelScanEstTime = _XfRFSpectrumDiagChannelScanEstTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 3),
    _XfRFSpectrumDiagChannelScanEstTime_Type()
)
xfRFSpectrumDiagChannelScanEstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagChannelScanEstTime.setStatus("current")


class _XfRFSpectrumDiagSubBandScanEstTime_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagSubBandScanEstTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagSubBandScanEstTime_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagSubBandScanEstTime_Object = MibTableColumn
xfRFSpectrumDiagSubBandScanEstTime = _XfRFSpectrumDiagSubBandScanEstTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 4),
    _XfRFSpectrumDiagSubBandScanEstTime_Type()
)
xfRFSpectrumDiagSubBandScanEstTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagSubBandScanEstTime.setStatus("current")


class _XfRFSpectrumDiagScanDate_Type(DisplayString):
    """Custom type xfRFSpectrumDiagScanDate based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_XfRFSpectrumDiagScanDate_Type.__name__ = "DisplayString"
_XfRFSpectrumDiagScanDate_Object = MibTableColumn
xfRFSpectrumDiagScanDate = _XfRFSpectrumDiagScanDate_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 5),
    _XfRFSpectrumDiagScanDate_Type()
)
xfRFSpectrumDiagScanDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagScanDate.setStatus("current")


class _XfRFSpectrumDiagChannelSpacing_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagChannelSpacing based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagChannelSpacing_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagChannelSpacing_Object = MibTableColumn
xfRFSpectrumDiagChannelSpacing = _XfRFSpectrumDiagChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 6),
    _XfRFSpectrumDiagChannelSpacing_Type()
)
xfRFSpectrumDiagChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagChannelSpacing.setStatus("current")


class _XfRFSpectrumDiagCurrRxFrequency_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagCurrRxFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagCurrRxFrequency_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagCurrRxFrequency_Object = MibTableColumn
xfRFSpectrumDiagCurrRxFrequency = _XfRFSpectrumDiagCurrRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 7),
    _XfRFSpectrumDiagCurrRxFrequency_Type()
)
xfRFSpectrumDiagCurrRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagCurrRxFrequency.setStatus("current")


class _XfRFSpectrumDiagMinRxFrequency_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagMinRxFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagMinRxFrequency_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagMinRxFrequency_Object = MibTableColumn
xfRFSpectrumDiagMinRxFrequency = _XfRFSpectrumDiagMinRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 8),
    _XfRFSpectrumDiagMinRxFrequency_Type()
)
xfRFSpectrumDiagMinRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagMinRxFrequency.setStatus("current")


class _XfRFSpectrumDiagMaxRxFrequency_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagMaxRxFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagMaxRxFrequency_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagMaxRxFrequency_Object = MibTableColumn
xfRFSpectrumDiagMaxRxFrequency = _XfRFSpectrumDiagMaxRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 9),
    _XfRFSpectrumDiagMaxRxFrequency_Type()
)
xfRFSpectrumDiagMaxRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagMaxRxFrequency.setStatus("current")


class _XfRFSpectrumDiagIdxCompanion1_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagIdxCompanion1 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagIdxCompanion1_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagIdxCompanion1_Object = MibTableColumn
xfRFSpectrumDiagIdxCompanion1 = _XfRFSpectrumDiagIdxCompanion1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 10),
    _XfRFSpectrumDiagIdxCompanion1_Type()
)
xfRFSpectrumDiagIdxCompanion1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagIdxCompanion1.setStatus("current")


class _XfRFSpectrumDiagIdxCompanion2_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagIdxCompanion2 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagIdxCompanion2_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagIdxCompanion2_Object = MibTableColumn
xfRFSpectrumDiagIdxCompanion2 = _XfRFSpectrumDiagIdxCompanion2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 11),
    _XfRFSpectrumDiagIdxCompanion2_Type()
)
xfRFSpectrumDiagIdxCompanion2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagIdxCompanion2.setStatus("current")


class _XfRFSpectrumDiagIdxCompanion3_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagIdxCompanion3 based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagIdxCompanion3_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagIdxCompanion3_Object = MibTableColumn
xfRFSpectrumDiagIdxCompanion3 = _XfRFSpectrumDiagIdxCompanion3_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 12),
    _XfRFSpectrumDiagIdxCompanion3_Type()
)
xfRFSpectrumDiagIdxCompanion3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagIdxCompanion3.setStatus("current")


class _XfRFSpectrumDiagProgress_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagProgress based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_XfRFSpectrumDiagProgress_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagProgress_Object = MibTableColumn
xfRFSpectrumDiagProgress = _XfRFSpectrumDiagProgress_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 6, 1, 13),
    _XfRFSpectrumDiagProgress_Type()
)
xfRFSpectrumDiagProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagProgress.setStatus("current")
_XfRFSpectrumDiagResultTable_Object = MibTable
xfRFSpectrumDiagResultTable = _XfRFSpectrumDiagResultTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 7)
)
if mibBuilder.loadTexts:
    xfRFSpectrumDiagResultTable.setStatus("current")
_XfRFSpectrumDiagResultEntry_Object = MibTableRow
xfRFSpectrumDiagResultEntry = _XfRFSpectrumDiagResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 7, 1)
)
xfRFSpectrumDiagResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagResultIndex"),
)
if mibBuilder.loadTexts:
    xfRFSpectrumDiagResultEntry.setStatus("current")


class _XfRFSpectrumDiagResultIndex_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagResultIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagResultIndex_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagResultIndex_Object = MibTableColumn
xfRFSpectrumDiagResultIndex = _XfRFSpectrumDiagResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 7, 1, 1),
    _XfRFSpectrumDiagResultIndex_Type()
)
xfRFSpectrumDiagResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagResultIndex.setStatus("current")


class _XfRFSpectrumDiagResultRxFrequency_Type(Unsigned32):
    """Custom type xfRFSpectrumDiagResultRxFrequency based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_XfRFSpectrumDiagResultRxFrequency_Type.__name__ = "Unsigned32"
_XfRFSpectrumDiagResultRxFrequency_Object = MibTableColumn
xfRFSpectrumDiagResultRxFrequency = _XfRFSpectrumDiagResultRxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 7, 1, 2),
    _XfRFSpectrumDiagResultRxFrequency_Type()
)
xfRFSpectrumDiagResultRxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagResultRxFrequency.setStatus("current")


class _XfRFSpectrumDiagResultRxPower_Type(Integer32):
    """Custom type xfRFSpectrumDiagResultRxPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
    )


_XfRFSpectrumDiagResultRxPower_Type.__name__ = "Integer32"
_XfRFSpectrumDiagResultRxPower_Object = MibTableColumn
xfRFSpectrumDiagResultRxPower = _XfRFSpectrumDiagResultRxPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 7, 1, 3),
    _XfRFSpectrumDiagResultRxPower_Type()
)
xfRFSpectrumDiagResultRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFSpectrumDiagResultRxPower.setStatus("current")
_XfRfIfPowerTable_Object = MibTable
xfRfIfPowerTable = _XfRfIfPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8)
)
if mibBuilder.loadTexts:
    xfRfIfPowerTable.setStatus("current")
_XfRfIfPowerEntry_Object = MibTableRow
xfRfIfPowerEntry = _XfRfIfPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1)
)
xfRfIfPowerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRfIfPowerEntry.setStatus("current")
_XfRfSelectedMinOutputPower_Type = RfOutputPower
_XfRfSelectedMinOutputPower_Object = MibTableColumn
xfRfSelectedMinOutputPower = _XfRfSelectedMinOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 1),
    _XfRfSelectedMinOutputPower_Type()
)
xfRfSelectedMinOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfSelectedMinOutputPower.setStatus("current")
_XfRfSelectedMaxOutputPower_Type = RfOutputPower
_XfRfSelectedMaxOutputPower_Object = MibTableColumn
xfRfSelectedMaxOutputPower = _XfRfSelectedMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 2),
    _XfRfSelectedMaxOutputPower_Type()
)
xfRfSelectedMaxOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfSelectedMaxOutputPower.setStatus("current")
_XfRfCurrentOutputPower_Type = RfOutputPower
_XfRfCurrentOutputPower_Object = MibTableColumn
xfRfCurrentOutputPower = _XfRfCurrentOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 3),
    _XfRfCurrentOutputPower_Type()
)
xfRfCurrentOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfCurrentOutputPower.setStatus("current")
_XfRfMinOutputPower_Type = RfOutputPower
_XfRfMinOutputPower_Object = MibTableColumn
xfRfMinOutputPower = _XfRfMinOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 4),
    _XfRfMinOutputPower_Type()
)
xfRfMinOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMinOutputPower.setStatus("current")
_XfRfMaxOutputPower_Type = RfOutputPower
_XfRfMaxOutputPower_Object = MibTableColumn
xfRfMaxOutputPower = _XfRfMaxOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 5),
    _XfRfMaxOutputPower_Type()
)
xfRfMaxOutputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMaxOutputPower.setStatus("current")


class _XfRfAtpcTargetInputPowerFE_Type(Integer32):
    """Custom type xfRfAtpcTargetInputPowerFE based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -30),
    )


_XfRfAtpcTargetInputPowerFE_Type.__name__ = "Integer32"
_XfRfAtpcTargetInputPowerFE_Object = MibTableColumn
xfRfAtpcTargetInputPowerFE = _XfRfAtpcTargetInputPowerFE_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 6),
    _XfRfAtpcTargetInputPowerFE_Type()
)
xfRfAtpcTargetInputPowerFE.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfAtpcTargetInputPowerFE.setStatus("current")
_XfRfCurrentInputPower_Type = RfInputPower
_XfRfCurrentInputPower_Object = MibTableColumn
xfRfCurrentInputPower = _XfRfCurrentInputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 7),
    _XfRfCurrentInputPower_Type()
)
xfRfCurrentInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfCurrentInputPower.setStatus("current")
_XfRfMaxInputPowerLast7Days_Type = RfInputPower
_XfRfMaxInputPowerLast7Days_Object = MibTableColumn
xfRfMaxInputPowerLast7Days = _XfRfMaxInputPowerLast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 8),
    _XfRfMaxInputPowerLast7Days_Type()
)
xfRfMaxInputPowerLast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMaxInputPowerLast7Days.setStatus("current")
_XfRfMinInputPowerLast7Days_Type = RfInputPower
_XfRfMinInputPowerLast7Days_Object = MibTableColumn
xfRfMinInputPowerLast7Days = _XfRfMinInputPowerLast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 9),
    _XfRfMinInputPowerLast7Days_Type()
)
xfRfMinInputPowerLast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMinInputPowerLast7Days.setStatus("current")
_XfRfMaxInputPowerSinceReset_Type = RfInputPower
_XfRfMaxInputPowerSinceReset_Object = MibTableColumn
xfRfMaxInputPowerSinceReset = _XfRfMaxInputPowerSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 10),
    _XfRfMaxInputPowerSinceReset_Type()
)
xfRfMaxInputPowerSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMaxInputPowerSinceReset.setStatus("current")
_XfRfMinInputPowerSinceReset_Type = RfInputPower
_XfRfMinInputPowerSinceReset_Object = MibTableColumn
xfRfMinInputPowerSinceReset = _XfRfMinInputPowerSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 11),
    _XfRfMinInputPowerSinceReset_Type()
)
xfRfMinInputPowerSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMinInputPowerSinceReset.setStatus("current")


class _XfRfInputPowerReset_Type(Integer32):
    """Custom type xfRfInputPowerReset based on Integer32"""
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
          ("inputPowerNoReset", 2),
          ("inputPowerReset", 3))
    )


_XfRfInputPowerReset_Type.__name__ = "Integer32"
_XfRfInputPowerReset_Object = MibTableColumn
xfRfInputPowerReset = _XfRfInputPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 12),
    _XfRfInputPowerReset_Type()
)
xfRfInputPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfInputPowerReset.setStatus("current")


class _XfRfInputAlarmThreshold_Type(Integer32):
    """Custom type xfRfInputAlarmThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-99, -30),
    )


_XfRfInputAlarmThreshold_Type.__name__ = "Integer32"
_XfRfInputAlarmThreshold_Object = MibTableColumn
xfRfInputAlarmThreshold = _XfRfInputAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 13),
    _XfRfInputAlarmThreshold_Type()
)
xfRfInputAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfInputAlarmThreshold.setStatus("current")
_XfRfOutputPower4QAM_Type = RfOutputPower
_XfRfOutputPower4QAM_Object = MibTableColumn
xfRfOutputPower4QAM = _XfRfOutputPower4QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 14),
    _XfRfOutputPower4QAM_Type()
)
xfRfOutputPower4QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower4QAM.setStatus("current")
_XfRfOutputPower16QAM_Type = RfOutputPower
_XfRfOutputPower16QAM_Object = MibTableColumn
xfRfOutputPower16QAM = _XfRfOutputPower16QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 15),
    _XfRfOutputPower16QAM_Type()
)
xfRfOutputPower16QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower16QAM.setStatus("current")
_XfRfOutputPower32QAM_Type = RfOutputPower
_XfRfOutputPower32QAM_Object = MibTableColumn
xfRfOutputPower32QAM = _XfRfOutputPower32QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 16),
    _XfRfOutputPower32QAM_Type()
)
xfRfOutputPower32QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower32QAM.setStatus("current")
_XfRfOutputPower64QAM_Type = RfOutputPower
_XfRfOutputPower64QAM_Object = MibTableColumn
xfRfOutputPower64QAM = _XfRfOutputPower64QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 17),
    _XfRfOutputPower64QAM_Type()
)
xfRfOutputPower64QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower64QAM.setStatus("current")
_XfRfOutputPower128QAM_Type = RfOutputPower
_XfRfOutputPower128QAM_Object = MibTableColumn
xfRfOutputPower128QAM = _XfRfOutputPower128QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 18),
    _XfRfOutputPower128QAM_Type()
)
xfRfOutputPower128QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower128QAM.setStatus("current")
_XfRfOutputPower256QAM_Type = RfOutputPower
_XfRfOutputPower256QAM_Object = MibTableColumn
xfRfOutputPower256QAM = _XfRfOutputPower256QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 19),
    _XfRfOutputPower256QAM_Type()
)
xfRfOutputPower256QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower256QAM.setStatus("current")
_XfRfOutputPower512QAM_Type = RfOutputPower
_XfRfOutputPower512QAM_Object = MibTableColumn
xfRfOutputPower512QAM = _XfRfOutputPower512QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 20),
    _XfRfOutputPower512QAM_Type()
)
xfRfOutputPower512QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower512QAM.setStatus("current")
_XfRfOutputPower1024QAM_Type = RfOutputPower
_XfRfOutputPower1024QAM_Object = MibTableColumn
xfRfOutputPower1024QAM = _XfRfOutputPower1024QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 21),
    _XfRfOutputPower1024QAM_Type()
)
xfRfOutputPower1024QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower1024QAM.setStatus("current")
_XfRfOutputPower2048QAM_Type = RfOutputPower
_XfRfOutputPower2048QAM_Object = MibTableColumn
xfRfOutputPower2048QAM = _XfRfOutputPower2048QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 22),
    _XfRfOutputPower2048QAM_Type()
)
xfRfOutputPower2048QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower2048QAM.setStatus("current")
_XfRfOutputPower4096QAM_Type = RfOutputPower
_XfRfOutputPower4096QAM_Object = MibTableColumn
xfRfOutputPower4096QAM = _XfRfOutputPower4096QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 23),
    _XfRfOutputPower4096QAM_Type()
)
xfRfOutputPower4096QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower4096QAM.setStatus("current")
_XfRfMaxOutputPowerNotLimited_Type = RfOutputPower
_XfRfMaxOutputPowerNotLimited_Object = MibTableColumn
xfRfMaxOutputPowerNotLimited = _XfRfMaxOutputPowerNotLimited_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 24),
    _XfRfMaxOutputPowerNotLimited_Type()
)
xfRfMaxOutputPowerNotLimited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMaxOutputPowerNotLimited.setStatus("current")


class _XfRfMaxOutputPowerPossible_Type(Integer32):
    """Custom type xfRfMaxOutputPowerPossible based on Integer32"""
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
          ("possible", 2),
          ("notPossible", 3))
    )


_XfRfMaxOutputPowerPossible_Type.__name__ = "Integer32"
_XfRfMaxOutputPowerPossible_Object = MibTableColumn
xfRfMaxOutputPowerPossible = _XfRfMaxOutputPowerPossible_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 25),
    _XfRfMaxOutputPowerPossible_Type()
)
xfRfMaxOutputPowerPossible.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMaxOutputPowerPossible.setStatus("current")


class _XfRfMeanInputPower1m_Type(Integer32):
    """Custom type xfRfMeanInputPower1m based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfRfMeanInputPower1m_Type.__name__ = "Integer32"
_XfRfMeanInputPower1m_Object = MibTableColumn
xfRfMeanInputPower1m = _XfRfMeanInputPower1m_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 26),
    _XfRfMeanInputPower1m_Type()
)
xfRfMeanInputPower1m.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMeanInputPower1m.setStatus("current")


class _XfRfMaxOutputPowerLast7Days_Type(Integer32):
    """Custom type xfRfMaxOutputPowerLast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRfMaxOutputPowerLast7Days_Type.__name__ = "Integer32"
_XfRfMaxOutputPowerLast7Days_Object = MibTableColumn
xfRfMaxOutputPowerLast7Days = _XfRfMaxOutputPowerLast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 27),
    _XfRfMaxOutputPowerLast7Days_Type()
)
xfRfMaxOutputPowerLast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMaxOutputPowerLast7Days.setStatus("current")


class _XfRfMinOutputPowerLast7Days_Type(Integer32):
    """Custom type xfRfMinOutputPowerLast7Days based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRfMinOutputPowerLast7Days_Type.__name__ = "Integer32"
_XfRfMinOutputPowerLast7Days_Object = MibTableColumn
xfRfMinOutputPowerLast7Days = _XfRfMinOutputPowerLast7Days_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 28),
    _XfRfMinOutputPowerLast7Days_Type()
)
xfRfMinOutputPowerLast7Days.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMinOutputPowerLast7Days.setStatus("current")


class _XfRfMaxOutputPowerSinceReset_Type(Integer32):
    """Custom type xfRfMaxOutputPowerSinceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRfMaxOutputPowerSinceReset_Type.__name__ = "Integer32"
_XfRfMaxOutputPowerSinceReset_Object = MibTableColumn
xfRfMaxOutputPowerSinceReset = _XfRfMaxOutputPowerSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 29),
    _XfRfMaxOutputPowerSinceReset_Type()
)
xfRfMaxOutputPowerSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMaxOutputPowerSinceReset.setStatus("current")


class _XfRfMinOutputPowerSinceReset_Type(Integer32):
    """Custom type xfRfMinOutputPowerSinceReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfRfMinOutputPowerSinceReset_Type.__name__ = "Integer32"
_XfRfMinOutputPowerSinceReset_Object = MibTableColumn
xfRfMinOutputPowerSinceReset = _XfRfMinOutputPowerSinceReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 30),
    _XfRfMinOutputPowerSinceReset_Type()
)
xfRfMinOutputPowerSinceReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfMinOutputPowerSinceReset.setStatus("current")


class _XfRfOutputPowerReset_Type(Integer32):
    """Custom type xfRfOutputPowerReset based on Integer32"""
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
          ("outputPowerNoReset", 2),
          ("outputPowerReset", 3))
    )


_XfRfOutputPowerReset_Type.__name__ = "Integer32"
_XfRfOutputPowerReset_Object = MibTableColumn
xfRfOutputPowerReset = _XfRfOutputPowerReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 31),
    _XfRfOutputPowerReset_Type()
)
xfRfOutputPowerReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfOutputPowerReset.setStatus("current")


class _XfRfAvailableOutputPowerType_Type(Integer32):
    """Custom type xfRfAvailableOutputPowerType based on Integer32"""
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
          ("standardPower", 2),
          ("highPower", 3))
    )


_XfRfAvailableOutputPowerType_Type.__name__ = "Integer32"
_XfRfAvailableOutputPowerType_Object = MibTableColumn
xfRfAvailableOutputPowerType = _XfRfAvailableOutputPowerType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 32),
    _XfRfAvailableOutputPowerType_Type()
)
xfRfAvailableOutputPowerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfAvailableOutputPowerType.setStatus("current")


class _XfRfSelectedOutputPowerType_Type(Integer32):
    """Custom type xfRfSelectedOutputPowerType based on Integer32"""
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
          ("standardPower", 2),
          ("highPower", 3))
    )


_XfRfSelectedOutputPowerType_Type.__name__ = "Integer32"
_XfRfSelectedOutputPowerType_Object = MibTableColumn
xfRfSelectedOutputPowerType = _XfRfSelectedOutputPowerType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 33),
    _XfRfSelectedOutputPowerType_Type()
)
xfRfSelectedOutputPowerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfSelectedOutputPowerType.setStatus("current")


class _XfRfTaps_Type(Integer32):
    """Custom type xfRfTaps based on Integer32"""
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
          ("enabled", 2),
          ("disabled", 3),
          ("notAvailable", 4))
    )


_XfRfTaps_Type.__name__ = "Integer32"
_XfRfTaps_Object = MibTableColumn
xfRfTaps = _XfRfTaps_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 34),
    _XfRfTaps_Type()
)
xfRfTaps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfTaps.setStatus("current")
_XfRfCurrentInputPowerSdcMain_Type = RfInputPower
_XfRfCurrentInputPowerSdcMain_Object = MibTableColumn
xfRfCurrentInputPowerSdcMain = _XfRfCurrentInputPowerSdcMain_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 35),
    _XfRfCurrentInputPowerSdcMain_Type()
)
xfRfCurrentInputPowerSdcMain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfCurrentInputPowerSdcMain.setStatus("current")
_XfRfCurrentInputPowerSdcDiv_Type = RfInputPower
_XfRfCurrentInputPowerSdcDiv_Object = MibTableColumn
xfRfCurrentInputPowerSdcDiv = _XfRfCurrentInputPowerSdcDiv_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 36),
    _XfRfCurrentInputPowerSdcDiv_Type()
)
xfRfCurrentInputPowerSdcDiv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfCurrentInputPowerSdcDiv.setStatus("current")
_XfRfOutputPower8192QAM_Type = RfOutputPower
_XfRfOutputPower8192QAM_Object = MibTableColumn
xfRfOutputPower8192QAM = _XfRfOutputPower8192QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 37),
    _XfRfOutputPower8192QAM_Type()
)
xfRfOutputPower8192QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower8192QAM.setStatus("current")
_XfRfOutputPower16384QAM_Type = RfOutputPower
_XfRfOutputPower16384QAM_Object = MibTableColumn
xfRfOutputPower16384QAM = _XfRfOutputPower16384QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 38),
    _XfRfOutputPower16384QAM_Type()
)
xfRfOutputPower16384QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRfOutputPower16384QAM.setStatus("current")
_XfRfAtpcFallbackOutputPower_Type = RfOutputPower
_XfRfAtpcFallbackOutputPower_Object = MibTableColumn
xfRfAtpcFallbackOutputPower = _XfRfAtpcFallbackOutputPower_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 39),
    _XfRfAtpcFallbackOutputPower_Type()
)
xfRfAtpcFallbackOutputPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfAtpcFallbackOutputPower.setStatus("current")
_XfRfAtpcFallbackEnable_Type = ATPCFallbackEnable
_XfRfAtpcFallbackEnable_Object = MibTableColumn
xfRfAtpcFallbackEnable = _XfRfAtpcFallbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 40),
    _XfRfAtpcFallbackEnable_Type()
)
xfRfAtpcFallbackEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfAtpcFallbackEnable.setStatus("current")


class _XfRfAtpcFallbackTimer_Type(Integer32):
    """Custom type xfRfAtpcFallbackTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_XfRfAtpcFallbackTimer_Type.__name__ = "Integer32"
_XfRfAtpcFallbackTimer_Object = MibTableColumn
xfRfAtpcFallbackTimer = _XfRfAtpcFallbackTimer_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 8, 1, 41),
    _XfRfAtpcFallbackTimer_Type()
)
xfRfAtpcFallbackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRfAtpcFallbackTimer.setStatus("current")
_XfRFIFCableMonitoringTable_Object = MibTable
xfRFIFCableMonitoringTable = _XfRFIFCableMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9)
)
if mibBuilder.loadTexts:
    xfRFIFCableMonitoringTable.setStatus("current")
_XfRFIFCableMonitoringEntry_Object = MibTableRow
xfRFIFCableMonitoringEntry = _XfRFIFCableMonitoringEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1)
)
xfRFIFCableMonitoringEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRFIFCableMonitoringEntry.setStatus("current")


class _XfRFIFCMStatus_Type(Integer32):
    """Custom type xfRFIFCMStatus based on Integer32"""
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
          ("disable", 2),
          ("enable", 3))
    )


_XfRFIFCMStatus_Type.__name__ = "Integer32"
_XfRFIFCMStatus_Object = MibTableColumn
xfRFIFCMStatus = _XfRFIFCMStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 1),
    _XfRFIFCMStatus_Type()
)
xfRFIFCMStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFIFCMStatus.setStatus("current")


class _XfRFOutlierAgc_Type(Integer32):
    """Custom type xfRFOutlierAgc based on Integer32"""
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
          ("disable", 2),
          ("enable", 3))
    )


_XfRFOutlierAgc_Type.__name__ = "Integer32"
_XfRFOutlierAgc_Object = MibTableColumn
xfRFOutlierAgc = _XfRFOutlierAgc_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 2),
    _XfRFOutlierAgc_Type()
)
xfRFOutlierAgc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFOutlierAgc.setStatus("current")


class _XfRFOutlierSetTh_Type(Unsigned32):
    """Custom type xfRFOutlierSetTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFOutlierSetTh_Type.__name__ = "Unsigned32"
_XfRFOutlierSetTh_Object = MibTableColumn
xfRFOutlierSetTh = _XfRFOutlierSetTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 3),
    _XfRFOutlierSetTh_Type()
)
xfRFOutlierSetTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFOutlierSetTh.setStatus("current")


class _XfRFOutlierCeaseTh_Type(Unsigned32):
    """Custom type xfRFOutlierCeaseTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFOutlierCeaseTh_Type.__name__ = "Unsigned32"
_XfRFOutlierCeaseTh_Object = MibTableColumn
xfRFOutlierCeaseTh = _XfRFOutlierCeaseTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 4),
    _XfRFOutlierCeaseTh_Type()
)
xfRFOutlierCeaseTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFOutlierCeaseTh.setStatus("current")


class _XfRFRangeAgc_Type(Integer32):
    """Custom type xfRFRangeAgc based on Integer32"""
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
          ("disable", 2),
          ("enable", 3))
    )


_XfRFRangeAgc_Type.__name__ = "Integer32"
_XfRFRangeAgc_Object = MibTableColumn
xfRFRangeAgc = _XfRFRangeAgc_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 5),
    _XfRFRangeAgc_Type()
)
xfRFRangeAgc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFRangeAgc.setStatus("current")


class _XfRFRangeSetTh_Type(Unsigned32):
    """Custom type xfRFRangeSetTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFRangeSetTh_Type.__name__ = "Unsigned32"
_XfRFRangeSetTh_Object = MibTableColumn
xfRFRangeSetTh = _XfRFRangeSetTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 6),
    _XfRFRangeSetTh_Type()
)
xfRFRangeSetTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFRangeSetTh.setStatus("current")


class _XfRFRangeCeaseTh_Type(Unsigned32):
    """Custom type xfRFRangeCeaseTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFRangeCeaseTh_Type.__name__ = "Unsigned32"
_XfRFRangeCeaseTh_Object = MibTableColumn
xfRFRangeCeaseTh = _XfRFRangeCeaseTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 7),
    _XfRFRangeCeaseTh_Type()
)
xfRFRangeCeaseTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFRangeCeaseTh.setStatus("current")


class _XfRFStddevAgc_Type(Integer32):
    """Custom type xfRFStddevAgc based on Integer32"""
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
          ("disable", 2),
          ("enable", 3))
    )


_XfRFStddevAgc_Type.__name__ = "Integer32"
_XfRFStddevAgc_Object = MibTableColumn
xfRFStddevAgc = _XfRFStddevAgc_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 8),
    _XfRFStddevAgc_Type()
)
xfRFStddevAgc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFStddevAgc.setStatus("current")


class _XfRFStddevSetTh_Type(Unsigned32):
    """Custom type xfRFStddevSetTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFStddevSetTh_Type.__name__ = "Unsigned32"
_XfRFStddevSetTh_Object = MibTableColumn
xfRFStddevSetTh = _XfRFStddevSetTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 9),
    _XfRFStddevSetTh_Type()
)
xfRFStddevSetTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFStddevSetTh.setStatus("current")


class _XfRFStddevCeaseTh_Type(Unsigned32):
    """Custom type xfRFStddevCeaseTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFStddevCeaseTh_Type.__name__ = "Unsigned32"
_XfRFStddevCeaseTh_Object = MibTableColumn
xfRFStddevCeaseTh = _XfRFStddevCeaseTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 10),
    _XfRFStddevCeaseTh_Type()
)
xfRFStddevCeaseTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFStddevCeaseTh.setStatus("current")


class _XfRFDegradationAgc_Type(Integer32):
    """Custom type xfRFDegradationAgc based on Integer32"""
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
          ("disable", 2),
          ("enable", 3))
    )


_XfRFDegradationAgc_Type.__name__ = "Integer32"
_XfRFDegradationAgc_Object = MibTableColumn
xfRFDegradationAgc = _XfRFDegradationAgc_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 11),
    _XfRFDegradationAgc_Type()
)
xfRFDegradationAgc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFDegradationAgc.setStatus("current")


class _XfRFDegradationSetTh_Type(Unsigned32):
    """Custom type xfRFDegradationSetTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFDegradationSetTh_Type.__name__ = "Unsigned32"
_XfRFDegradationSetTh_Object = MibTableColumn
xfRFDegradationSetTh = _XfRFDegradationSetTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 12),
    _XfRFDegradationSetTh_Type()
)
xfRFDegradationSetTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFDegradationSetTh.setStatus("current")


class _XfRFDegradationCeaseTh_Type(Unsigned32):
    """Custom type xfRFDegradationCeaseTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFDegradationCeaseTh_Type.__name__ = "Unsigned32"
_XfRFDegradationCeaseTh_Object = MibTableColumn
xfRFDegradationCeaseTh = _XfRFDegradationCeaseTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 13),
    _XfRFDegradationCeaseTh_Type()
)
xfRFDegradationCeaseTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFDegradationCeaseTh.setStatus("current")


class _XfRFMarginAgc_Type(Integer32):
    """Custom type xfRFMarginAgc based on Integer32"""
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
          ("disable", 2),
          ("enable", 3))
    )


_XfRFMarginAgc_Type.__name__ = "Integer32"
_XfRFMarginAgc_Object = MibTableColumn
xfRFMarginAgc = _XfRFMarginAgc_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 14),
    _XfRFMarginAgc_Type()
)
xfRFMarginAgc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFMarginAgc.setStatus("current")


class _XfRFMarginSetTh_Type(Unsigned32):
    """Custom type xfRFMarginSetTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFMarginSetTh_Type.__name__ = "Unsigned32"
_XfRFMarginSetTh_Object = MibTableColumn
xfRFMarginSetTh = _XfRFMarginSetTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 15),
    _XfRFMarginSetTh_Type()
)
xfRFMarginSetTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFMarginSetTh.setStatus("current")


class _XfRFMarginCeaseTh_Type(Unsigned32):
    """Custom type xfRFMarginCeaseTh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_XfRFMarginCeaseTh_Type.__name__ = "Unsigned32"
_XfRFMarginCeaseTh_Object = MibTableColumn
xfRFMarginCeaseTh = _XfRFMarginCeaseTh_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 16),
    _XfRFMarginCeaseTh_Type()
)
xfRFMarginCeaseTh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRFMarginCeaseTh.setStatus("current")


class _XfRFOutlierValue_Type(Integer32):
    """Custom type xfRFOutlierValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_XfRFOutlierValue_Type.__name__ = "Integer32"
_XfRFOutlierValue_Object = MibTableColumn
xfRFOutlierValue = _XfRFOutlierValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 17),
    _XfRFOutlierValue_Type()
)
xfRFOutlierValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutlierValue.setStatus("current")


class _XfRFRangeValue_Type(Integer32):
    """Custom type xfRFRangeValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_XfRFRangeValue_Type.__name__ = "Integer32"
_XfRFRangeValue_Object = MibTableColumn
xfRFRangeValue = _XfRFRangeValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 18),
    _XfRFRangeValue_Type()
)
xfRFRangeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFRangeValue.setStatus("current")


class _XfRFStddevValue_Type(Integer32):
    """Custom type xfRFStddevValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_XfRFStddevValue_Type.__name__ = "Integer32"
_XfRFStddevValue_Object = MibTableColumn
xfRFStddevValue = _XfRFStddevValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 19),
    _XfRFStddevValue_Type()
)
xfRFStddevValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFStddevValue.setStatus("current")


class _XfRFDegradationValue_Type(Integer32):
    """Custom type xfRFDegradationValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_XfRFDegradationValue_Type.__name__ = "Integer32"
_XfRFDegradationValue_Object = MibTableColumn
xfRFDegradationValue = _XfRFDegradationValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 20),
    _XfRFDegradationValue_Type()
)
xfRFDegradationValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFDegradationValue.setStatus("current")


class _XfRFMarginValue_Type(Integer32):
    """Custom type xfRFMarginValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_XfRFMarginValue_Type.__name__ = "Integer32"
_XfRFMarginValue_Object = MibTableColumn
xfRFMarginValue = _XfRFMarginValue_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 21),
    _XfRFMarginValue_Type()
)
xfRFMarginValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMarginValue.setStatus("current")


class _XfRFOutlierTrigger_Type(Integer32):
    """Custom type xfRFOutlierTrigger based on Integer32"""
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
          ("noSetThreshold", 2),
          ("setThreshold", 3))
    )


_XfRFOutlierTrigger_Type.__name__ = "Integer32"
_XfRFOutlierTrigger_Object = MibTableColumn
xfRFOutlierTrigger = _XfRFOutlierTrigger_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 22),
    _XfRFOutlierTrigger_Type()
)
xfRFOutlierTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFOutlierTrigger.setStatus("current")


class _XfRFRangeTrigger_Type(Integer32):
    """Custom type xfRFRangeTrigger based on Integer32"""
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
          ("noSetThreshold", 2),
          ("setThreshold", 3))
    )


_XfRFRangeTrigger_Type.__name__ = "Integer32"
_XfRFRangeTrigger_Object = MibTableColumn
xfRFRangeTrigger = _XfRFRangeTrigger_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 23),
    _XfRFRangeTrigger_Type()
)
xfRFRangeTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFRangeTrigger.setStatus("current")


class _XfRFStddevTrigger_Type(Integer32):
    """Custom type xfRFStddevTrigger based on Integer32"""
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
          ("noSetThreshold", 2),
          ("setThreshold", 3))
    )


_XfRFStddevTrigger_Type.__name__ = "Integer32"
_XfRFStddevTrigger_Object = MibTableColumn
xfRFStddevTrigger = _XfRFStddevTrigger_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 24),
    _XfRFStddevTrigger_Type()
)
xfRFStddevTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFStddevTrigger.setStatus("current")


class _XfRFDegradationTrigger_Type(Integer32):
    """Custom type xfRFDegradationTrigger based on Integer32"""
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
          ("noSetThreshold", 2),
          ("setThreshold", 3))
    )


_XfRFDegradationTrigger_Type.__name__ = "Integer32"
_XfRFDegradationTrigger_Object = MibTableColumn
xfRFDegradationTrigger = _XfRFDegradationTrigger_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 25),
    _XfRFDegradationTrigger_Type()
)
xfRFDegradationTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFDegradationTrigger.setStatus("current")


class _XfRFMarginTrigger_Type(Integer32):
    """Custom type xfRFMarginTrigger based on Integer32"""
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
          ("noSetThreshold", 2),
          ("setThreshold", 3))
    )


_XfRFMarginTrigger_Type.__name__ = "Integer32"
_XfRFMarginTrigger_Object = MibTableColumn
xfRFMarginTrigger = _XfRFMarginTrigger_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 9, 1, 26),
    _XfRFMarginTrigger_Type()
)
xfRFMarginTrigger.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRFMarginTrigger.setStatus("current")
_XfSdcTable_Object = MibTable
xfSdcTable = _XfSdcTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10)
)
if mibBuilder.loadTexts:
    xfSdcTable.setStatus("current")
_XfSdcEntry_Object = MibTableRow
xfSdcEntry = _XfSdcEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1)
)
xfSdcEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xfSdcEntry.setStatus("current")


class _XfSdcCapability_Type(Integer32):
    """Custom type xfSdcCapability based on Integer32"""
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
          ("sdcSupported", 2),
          ("sdcNotSupported", 3))
    )


_XfSdcCapability_Type.__name__ = "Integer32"
_XfSdcCapability_Object = MibTableColumn
xfSdcCapability = _XfSdcCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 1),
    _XfSdcCapability_Type()
)
xfSdcCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSdcCapability.setStatus("current")


class _XfSdcAdminStatus_Type(Integer32):
    """Custom type xfSdcAdminStatus based on Integer32"""
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
          ("sdcEnabled", 2),
          ("sdcDisabled", 3))
    )


_XfSdcAdminStatus_Type.__name__ = "Integer32"
_XfSdcAdminStatus_Object = MibTableColumn
xfSdcAdminStatus = _XfSdcAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 2),
    _XfSdcAdminStatus_Type()
)
xfSdcAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSdcAdminStatus.setStatus("current")


class _XfSdcOperStatus_Type(Integer32):
    """Custom type xfSdcOperStatus based on Integer32"""
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
          ("sdcEnabled", 2),
          ("sdcDisabled", 3),
          ("sdcInProgress", 4))
    )


_XfSdcOperStatus_Type.__name__ = "Integer32"
_XfSdcOperStatus_Object = MibTableColumn
xfSdcOperStatus = _XfSdcOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 3),
    _XfSdcOperStatus_Type()
)
xfSdcOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSdcOperStatus.setStatus("current")


class _XfSdcDadeControl_Type(Integer32):
    """Custom type xfSdcDadeControl based on Integer32"""
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
          ("sdcDadeStart", 2),
          ("sdcDadeAbort", 3))
    )


_XfSdcDadeControl_Type.__name__ = "Integer32"
_XfSdcDadeControl_Object = MibTableColumn
xfSdcDadeControl = _XfSdcDadeControl_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 4),
    _XfSdcDadeControl_Type()
)
xfSdcDadeControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSdcDadeControl.setStatus("current")


class _XfSdcDadeStatus_Type(Integer32):
    """Custom type xfSdcDadeStatus based on Integer32"""
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
        *(("other", 1),
          ("sdcCalibrated", 2),
          ("sdcNotCalibrated", 3),
          ("sdcCalInProgress", 4),
          ("sdcCalMismatch", 5))
    )


_XfSdcDadeStatus_Type.__name__ = "Integer32"
_XfSdcDadeStatus_Object = MibTableColumn
xfSdcDadeStatus = _XfSdcDadeStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 5),
    _XfSdcDadeStatus_Type()
)
xfSdcDadeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSdcDadeStatus.setStatus("current")


class _XfSdcPath_Type(Integer32):
    """Custom type xfSdcPath based on Integer32"""
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
          ("sdcAuto", 2),
          ("sdcMain", 3),
          ("sdcDiv", 4))
    )


_XfSdcPath_Type.__name__ = "Integer32"
_XfSdcPath_Object = MibTableColumn
xfSdcPath = _XfSdcPath_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 6),
    _XfSdcPath_Type()
)
xfSdcPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfSdcPath.setStatus("current")


class _XfSdcOduDateTimeCalibration_Type(DisplayString):
    """Custom type xfSdcOduDateTimeCalibration based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XfSdcOduDateTimeCalibration_Type.__name__ = "DisplayString"
_XfSdcOduDateTimeCalibration_Object = MibTableColumn
xfSdcOduDateTimeCalibration = _XfSdcOduDateTimeCalibration_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 7),
    _XfSdcOduDateTimeCalibration_Type()
)
xfSdcOduDateTimeCalibration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSdcOduDateTimeCalibration.setStatus("current")


class _XfSdcOduSerialNumber_Type(DisplayString):
    """Custom type xfSdcOduSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XfSdcOduSerialNumber_Type.__name__ = "DisplayString"
_XfSdcOduSerialNumber_Object = MibTableColumn
xfSdcOduSerialNumber = _XfSdcOduSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 8),
    _XfSdcOduSerialNumber_Type()
)
xfSdcOduSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSdcOduSerialNumber.setStatus("current")


class _XfSdcGain_Type(Integer32):
    """Custom type xfSdcGain based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_XfSdcGain_Type.__name__ = "Integer32"
_XfSdcGain_Object = MibTableColumn
xfSdcGain = _XfSdcGain_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 9),
    _XfSdcGain_Type()
)
xfSdcGain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSdcGain.setStatus("current")


class _XfSdcActualPath_Type(Integer32):
    """Custom type xfSdcActualPath based on Integer32"""
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
          ("sdcAuto", 2),
          ("sdcMain", 3),
          ("sdcDiv", 4))
    )


_XfSdcActualPath_Type.__name__ = "Integer32"
_XfSdcActualPath_Object = MibTableColumn
xfSdcActualPath = _XfSdcActualPath_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 10),
    _XfSdcActualPath_Type()
)
xfSdcActualPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSdcActualPath.setStatus("current")


class _XfSdcDadeDelay_Type(Integer32):
    """Custom type xfSdcDadeDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-2147483647, 2147483647),
    )


_XfSdcDadeDelay_Type.__name__ = "Integer32"
_XfSdcDadeDelay_Object = MibTableColumn
xfSdcDadeDelay = _XfSdcDadeDelay_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 1, 10, 1, 11),
    _XfSdcDadeDelay_Type()
)
xfSdcDadeDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfSdcDadeDelay.setStatus("current")
_XfRadioLinkPtpRadioConformance_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpRadioConformance = _XfRadioLinkPtpRadioConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 2)
)
_XfRadioLinkPtpRadioCompliances_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpRadioCompliances = _XfRadioLinkPtpRadioCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 2, 1)
)
_XfRadioLinkPtpRadioGroups_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpRadioGroups = _XfRadioLinkPtpRadioGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 2, 2)
)

# Managed Objects groups

xfRadioLinkPtpRadioCompleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 2, 2, 1)
)
xfRadioLinkPtpRadioCompleteGroup.setObjects(
      *(("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUAlarmStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAURfLoopAvailable"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUAtpcCapability"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAULocalCtrlCapability"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUModCapability"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUFrequencyband"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUSubBand"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUTemperature"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUProtectionPath"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAURxCapability"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUNotes"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRauAtpcVersion"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRauBoosterCapability"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRauBoosterSelectedIndex"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFBaseTxFrequency"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFBaseRxFrequency"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStepSize"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStepLimitLow"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStepLimitHigh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFCurrentStepNumber"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFTxOperStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFTxAdminStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFLoopEnable"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFAlarms"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStepSizeRx"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStepLimitLowRx"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStepLimitHighRx"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFCurrentStepNumberRx"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFDuplexType"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFDuplexConfig"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFDuplexDistance"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFCurrentOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFRtpcMinOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFRtpcMaxOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFRtpcSelectedOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFAtpcMinOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFAtpcMaxOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFAtpcMinInputPowerFar"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFAtpcSelectedInputPowerFar"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFAttenuator"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFCurrentInputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMaxInputPowerLast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMinInputPowerLast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMaxInputPowerSinceReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMinInputPowerSinceReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFInputPowerReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFInputAlarmThreshold"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUChannelSpacing"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUChannelModulation"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUSpectrumEfficiencyClass"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUCarrierMode"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPower4QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPower8QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPower16QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPower32QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPower64QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPower128QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPower256QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPower512QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFAtpcFallbackOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFAtpcFallbackEnable"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFAtpcFallbackTimer"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPower1024QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMaxOutputPowerNotLimited"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMaxOutputPowerNotPossible"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFCurrentInputPowerSdcMain"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFCurrentInputPowerSdcDiv"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUSubBandIndex"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRAUSubBandRange"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMeanInputPower1m"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMaxOutputPowerLast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMinOutputPowerLast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMaxOutputPowerSinceReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMinOutputPowerSinceReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMaxMSELast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMinMSELast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMaxXPILast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMinXPILast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutputPowerReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfAvailableOutputPowerType"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfSelectedOutputPowerType"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfTaps"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfSelectedMinOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfSelectedMaxOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfCurrentOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMinOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMaxOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfAtpcTargetInputPowerFE"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfCurrentInputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMaxInputPowerLast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMinInputPowerLast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMaxInputPowerSinceReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMinInputPowerSinceReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfInputPowerReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfInputAlarmThreshold"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower4QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower16QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower32QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower64QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower128QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower256QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower512QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower1024QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower2048QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower4096QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower8192QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPower16384QAM"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfAtpcFallbackOutputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfAtpcFallbackEnable"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfAtpcFallbackTimer"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMaxOutputPowerNotLimited"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMaxOutputPowerPossible"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMeanInputPower1m"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMaxOutputPowerLast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMinOutputPowerLast7Days"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMaxOutputPowerSinceReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfMinOutputPowerSinceReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfOutputPowerReset"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagAdminStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagOperStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagChannelScanEstTime"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagSubBandScanEstTime"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagScanDate"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagChannelSpacing"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagCurrRxFrequency"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagMinRxFrequency"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagMaxRxFrequency"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagIdxCompanion1"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagIdxCompanion2"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagIdxCompanion3"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagProgress"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagResultIndex"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagResultRxFrequency"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFSpectrumDiagResultRxPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFBoosterGain"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFBoosterMaxInputPower"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFBoosterCapability"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFBoosterProductNumber"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFBoosterHWRevision"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFIFCMStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutlierAgc"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutlierSetTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutlierCeaseTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFRangeAgc"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFRangeSetTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFRangeCeaseTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStddevAgc"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStddevSetTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStddevCeaseTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFDegradationAgc"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFDegradationSetTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFDegradationCeaseTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMarginAgc"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMarginSetTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMarginCeaseTh"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutlierValue"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFRangeValue"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStddevValue"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFDegradationValue"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMarginValue"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFOutlierTrigger"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFRangeTrigger"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFStddevTrigger"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFDegradationTrigger"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRFMarginTrigger"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcCapability"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcAdminStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcOperStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcDadeControl"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcDadeStatus"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcPath"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcOduDateTimeCalibration"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcOduSerialNumber"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcGain"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcActualPath"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfSdcDadeDelay"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfCurrentInputPowerSdcMain"),
        ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRfCurrentInputPowerSdcDiv"))
)
if mibBuilder.loadTexts:
    xfRadioLinkPtpRadioCompleteGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xfRADIOLINKPTPRADIOFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 3, 2, 1, 1)
)
xfRADIOLINKPTPRADIOFullCompliance.setObjects(
    ("XF-RADIOLINK-PTP-RADIO-MIB", "xfRadioLinkPtpRadioCompleteGroup")
)
if mibBuilder.loadTexts:
    xfRADIOLINKPTPRADIOFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XF-RADIOLINK-PTP-RADIO-MIB",
    **{"RFTxOperStatus": RFTxOperStatus,
       "RAURfLoopAvailable": RAURfLoopAvailable,
       "RAUAtpcCapability": RAUAtpcCapability,
       "RAUModCapability": RAUModCapability,
       "RAUChannelSpacingCapability": RAUChannelSpacingCapability,
       "RauSec": RauSec,
       "RAUModulation": RAUModulation,
       "ATPCFallbackEnable": ATPCFallbackEnable,
       "RfOutputPower": RfOutputPower,
       "RfInputPower": RfInputPower,
       "BoosterCapability": BoosterCapability,
       "xfRadioLinkPtpRadioMIB": xfRadioLinkPtpRadioMIB,
       "xfRadioLinkPtpRadioObjects": xfRadioLinkPtpRadioObjects,
       "xfRAUTable": xfRAUTable,
       "xfRAUEntry": xfRAUEntry,
       "xfRAUAlarmStatus": xfRAUAlarmStatus,
       "xfRAURfLoopAvailable": xfRAURfLoopAvailable,
       "xfRAUAtpcCapability": xfRAUAtpcCapability,
       "xfRAULocalCtrlCapability": xfRAULocalCtrlCapability,
       "xfRAUModCapability": xfRAUModCapability,
       "xfRAUFrequencyband": xfRAUFrequencyband,
       "xfRAUSubBand": xfRAUSubBand,
       "xfRAUTemperature": xfRAUTemperature,
       "xfRAUProtectionPath": xfRAUProtectionPath,
       "xfRAURxCapability": xfRAURxCapability,
       "xfRAUNotes": xfRAUNotes,
       "xfRauAtpcVersion": xfRauAtpcVersion,
       "xfRauBoosterCapability": xfRauBoosterCapability,
       "xfRauBoosterSelectedIndex": xfRauBoosterSelectedIndex,
       "xfRFIFTable": xfRFIFTable,
       "xfRFIFEntry": xfRFIFEntry,
       "xfRFBaseTxFrequency": xfRFBaseTxFrequency,
       "xfRFBaseRxFrequency": xfRFBaseRxFrequency,
       "xfRFStepSize": xfRFStepSize,
       "xfRFStepLimitLow": xfRFStepLimitLow,
       "xfRFStepLimitHigh": xfRFStepLimitHigh,
       "xfRFCurrentStepNumber": xfRFCurrentStepNumber,
       "xfRFTxOperStatus": xfRFTxOperStatus,
       "xfRFTxAdminStatus": xfRFTxAdminStatus,
       "xfRFLoopEnable": xfRFLoopEnable,
       "xfRFAlarms": xfRFAlarms,
       "xfRFStatus": xfRFStatus,
       "xfRFStepSizeRx": xfRFStepSizeRx,
       "xfRFStepLimitLowRx": xfRFStepLimitLowRx,
       "xfRFStepLimitHighRx": xfRFStepLimitHighRx,
       "xfRFCurrentStepNumberRx": xfRFCurrentStepNumberRx,
       "xfRFDuplexType": xfRFDuplexType,
       "xfRFDuplexConfig": xfRFDuplexConfig,
       "xfRFDuplexDistance": xfRFDuplexDistance,
       "xfRFPowerTable": xfRFPowerTable,
       "xfRFPowerEntry": xfRFPowerEntry,
       "xfRFCurrentOutputPower": xfRFCurrentOutputPower,
       "xfRFRtpcMinOutputPower": xfRFRtpcMinOutputPower,
       "xfRFRtpcMaxOutputPower": xfRFRtpcMaxOutputPower,
       "xfRFRtpcSelectedOutputPower": xfRFRtpcSelectedOutputPower,
       "xfRFAtpcMinOutputPower": xfRFAtpcMinOutputPower,
       "xfRFAtpcMaxOutputPower": xfRFAtpcMaxOutputPower,
       "xfRFAtpcMinInputPowerFar": xfRFAtpcMinInputPowerFar,
       "xfRFAtpcSelectedInputPowerFar": xfRFAtpcSelectedInputPowerFar,
       "xfRFAttenuator": xfRFAttenuator,
       "xfRFCurrentInputPower": xfRFCurrentInputPower,
       "xfRFMaxInputPowerLast7Days": xfRFMaxInputPowerLast7Days,
       "xfRFMinInputPowerLast7Days": xfRFMinInputPowerLast7Days,
       "xfRFMaxInputPowerSinceReset": xfRFMaxInputPowerSinceReset,
       "xfRFMinInputPowerSinceReset": xfRFMinInputPowerSinceReset,
       "xfRFInputPowerReset": xfRFInputPowerReset,
       "xfRFInputAlarmThreshold": xfRFInputAlarmThreshold,
       "xfRFOutputPower4QAM": xfRFOutputPower4QAM,
       "xfRFOutputPower8QAM": xfRFOutputPower8QAM,
       "xfRFOutputPower16QAM": xfRFOutputPower16QAM,
       "xfRFOutputPower32QAM": xfRFOutputPower32QAM,
       "xfRFOutputPower64QAM": xfRFOutputPower64QAM,
       "xfRFOutputPower128QAM": xfRFOutputPower128QAM,
       "xfRFOutputPower256QAM": xfRFOutputPower256QAM,
       "xfRFOutputPower512QAM": xfRFOutputPower512QAM,
       "xfRFAtpcFallbackOutputPower": xfRFAtpcFallbackOutputPower,
       "xfRFAtpcFallbackEnable": xfRFAtpcFallbackEnable,
       "xfRFAtpcFallbackTimer": xfRFAtpcFallbackTimer,
       "xfRFOutputPower1024QAM": xfRFOutputPower1024QAM,
       "xfRFMaxOutputPowerNotLimited": xfRFMaxOutputPowerNotLimited,
       "xfRFMaxOutputPowerNotPossible": xfRFMaxOutputPowerNotPossible,
       "xfRFCurrentInputPowerSdcMain": xfRFCurrentInputPowerSdcMain,
       "xfRFCurrentInputPowerSdcDiv": xfRFCurrentInputPowerSdcDiv,
       "xfRFMeanInputPower1m": xfRFMeanInputPower1m,
       "xfRFMaxOutputPowerLast7Days": xfRFMaxOutputPowerLast7Days,
       "xfRFMinOutputPowerLast7Days": xfRFMinOutputPowerLast7Days,
       "xfRFMaxOutputPowerSinceReset": xfRFMaxOutputPowerSinceReset,
       "xfRFMinOutputPowerSinceReset": xfRFMinOutputPowerSinceReset,
       "xfRFMaxMSELast7Days": xfRFMaxMSELast7Days,
       "xfRFMinMSELast7Days": xfRFMinMSELast7Days,
       "xfRFMaxXPILast7Days": xfRFMaxXPILast7Days,
       "xfRFMinXPILast7Days": xfRFMinXPILast7Days,
       "xfRFOutputPowerReset": xfRFOutputPowerReset,
       "xfRFBoosterGain": xfRFBoosterGain,
       "xfRFBoosterMaxInputPower": xfRFBoosterMaxInputPower,
       "xfRFBoosterCapability": xfRFBoosterCapability,
       "xfRFBoosterProductNumber": xfRFBoosterProductNumber,
       "xfRFBoosterHWRevision": xfRFBoosterHWRevision,
       "xfRAUCapabilityTable": xfRAUCapabilityTable,
       "xfRAUCapabilityEntry": xfRAUCapabilityEntry,
       "xfRAUChannelSpacing": xfRAUChannelSpacing,
       "xfRAUChannelModulation": xfRAUChannelModulation,
       "xfRAUSpectrumEfficiencyClass": xfRAUSpectrumEfficiencyClass,
       "xfRAUCarrierMode": xfRAUCarrierMode,
       "xfRAUSubBandTable": xfRAUSubBandTable,
       "xfRAUSubBandEntry": xfRAUSubBandEntry,
       "xfRAUSubBandIndex": xfRAUSubBandIndex,
       "xfRAUSubBandRange": xfRAUSubBandRange,
       "xfRFSpectrumDiagTable": xfRFSpectrumDiagTable,
       "xfRFSpectrumDiagEntry": xfRFSpectrumDiagEntry,
       "xfRFSpectrumDiagAdminStatus": xfRFSpectrumDiagAdminStatus,
       "xfRFSpectrumDiagOperStatus": xfRFSpectrumDiagOperStatus,
       "xfRFSpectrumDiagChannelScanEstTime": xfRFSpectrumDiagChannelScanEstTime,
       "xfRFSpectrumDiagSubBandScanEstTime": xfRFSpectrumDiagSubBandScanEstTime,
       "xfRFSpectrumDiagScanDate": xfRFSpectrumDiagScanDate,
       "xfRFSpectrumDiagChannelSpacing": xfRFSpectrumDiagChannelSpacing,
       "xfRFSpectrumDiagCurrRxFrequency": xfRFSpectrumDiagCurrRxFrequency,
       "xfRFSpectrumDiagMinRxFrequency": xfRFSpectrumDiagMinRxFrequency,
       "xfRFSpectrumDiagMaxRxFrequency": xfRFSpectrumDiagMaxRxFrequency,
       "xfRFSpectrumDiagIdxCompanion1": xfRFSpectrumDiagIdxCompanion1,
       "xfRFSpectrumDiagIdxCompanion2": xfRFSpectrumDiagIdxCompanion2,
       "xfRFSpectrumDiagIdxCompanion3": xfRFSpectrumDiagIdxCompanion3,
       "xfRFSpectrumDiagProgress": xfRFSpectrumDiagProgress,
       "xfRFSpectrumDiagResultTable": xfRFSpectrumDiagResultTable,
       "xfRFSpectrumDiagResultEntry": xfRFSpectrumDiagResultEntry,
       "xfRFSpectrumDiagResultIndex": xfRFSpectrumDiagResultIndex,
       "xfRFSpectrumDiagResultRxFrequency": xfRFSpectrumDiagResultRxFrequency,
       "xfRFSpectrumDiagResultRxPower": xfRFSpectrumDiagResultRxPower,
       "xfRfIfPowerTable": xfRfIfPowerTable,
       "xfRfIfPowerEntry": xfRfIfPowerEntry,
       "xfRfSelectedMinOutputPower": xfRfSelectedMinOutputPower,
       "xfRfSelectedMaxOutputPower": xfRfSelectedMaxOutputPower,
       "xfRfCurrentOutputPower": xfRfCurrentOutputPower,
       "xfRfMinOutputPower": xfRfMinOutputPower,
       "xfRfMaxOutputPower": xfRfMaxOutputPower,
       "xfRfAtpcTargetInputPowerFE": xfRfAtpcTargetInputPowerFE,
       "xfRfCurrentInputPower": xfRfCurrentInputPower,
       "xfRfMaxInputPowerLast7Days": xfRfMaxInputPowerLast7Days,
       "xfRfMinInputPowerLast7Days": xfRfMinInputPowerLast7Days,
       "xfRfMaxInputPowerSinceReset": xfRfMaxInputPowerSinceReset,
       "xfRfMinInputPowerSinceReset": xfRfMinInputPowerSinceReset,
       "xfRfInputPowerReset": xfRfInputPowerReset,
       "xfRfInputAlarmThreshold": xfRfInputAlarmThreshold,
       "xfRfOutputPower4QAM": xfRfOutputPower4QAM,
       "xfRfOutputPower16QAM": xfRfOutputPower16QAM,
       "xfRfOutputPower32QAM": xfRfOutputPower32QAM,
       "xfRfOutputPower64QAM": xfRfOutputPower64QAM,
       "xfRfOutputPower128QAM": xfRfOutputPower128QAM,
       "xfRfOutputPower256QAM": xfRfOutputPower256QAM,
       "xfRfOutputPower512QAM": xfRfOutputPower512QAM,
       "xfRfOutputPower1024QAM": xfRfOutputPower1024QAM,
       "xfRfOutputPower2048QAM": xfRfOutputPower2048QAM,
       "xfRfOutputPower4096QAM": xfRfOutputPower4096QAM,
       "xfRfMaxOutputPowerNotLimited": xfRfMaxOutputPowerNotLimited,
       "xfRfMaxOutputPowerPossible": xfRfMaxOutputPowerPossible,
       "xfRfMeanInputPower1m": xfRfMeanInputPower1m,
       "xfRfMaxOutputPowerLast7Days": xfRfMaxOutputPowerLast7Days,
       "xfRfMinOutputPowerLast7Days": xfRfMinOutputPowerLast7Days,
       "xfRfMaxOutputPowerSinceReset": xfRfMaxOutputPowerSinceReset,
       "xfRfMinOutputPowerSinceReset": xfRfMinOutputPowerSinceReset,
       "xfRfOutputPowerReset": xfRfOutputPowerReset,
       "xfRfAvailableOutputPowerType": xfRfAvailableOutputPowerType,
       "xfRfSelectedOutputPowerType": xfRfSelectedOutputPowerType,
       "xfRfTaps": xfRfTaps,
       "xfRfCurrentInputPowerSdcMain": xfRfCurrentInputPowerSdcMain,
       "xfRfCurrentInputPowerSdcDiv": xfRfCurrentInputPowerSdcDiv,
       "xfRfOutputPower8192QAM": xfRfOutputPower8192QAM,
       "xfRfOutputPower16384QAM": xfRfOutputPower16384QAM,
       "xfRfAtpcFallbackOutputPower": xfRfAtpcFallbackOutputPower,
       "xfRfAtpcFallbackEnable": xfRfAtpcFallbackEnable,
       "xfRfAtpcFallbackTimer": xfRfAtpcFallbackTimer,
       "xfRFIFCableMonitoringTable": xfRFIFCableMonitoringTable,
       "xfRFIFCableMonitoringEntry": xfRFIFCableMonitoringEntry,
       "xfRFIFCMStatus": xfRFIFCMStatus,
       "xfRFOutlierAgc": xfRFOutlierAgc,
       "xfRFOutlierSetTh": xfRFOutlierSetTh,
       "xfRFOutlierCeaseTh": xfRFOutlierCeaseTh,
       "xfRFRangeAgc": xfRFRangeAgc,
       "xfRFRangeSetTh": xfRFRangeSetTh,
       "xfRFRangeCeaseTh": xfRFRangeCeaseTh,
       "xfRFStddevAgc": xfRFStddevAgc,
       "xfRFStddevSetTh": xfRFStddevSetTh,
       "xfRFStddevCeaseTh": xfRFStddevCeaseTh,
       "xfRFDegradationAgc": xfRFDegradationAgc,
       "xfRFDegradationSetTh": xfRFDegradationSetTh,
       "xfRFDegradationCeaseTh": xfRFDegradationCeaseTh,
       "xfRFMarginAgc": xfRFMarginAgc,
       "xfRFMarginSetTh": xfRFMarginSetTh,
       "xfRFMarginCeaseTh": xfRFMarginCeaseTh,
       "xfRFOutlierValue": xfRFOutlierValue,
       "xfRFRangeValue": xfRFRangeValue,
       "xfRFStddevValue": xfRFStddevValue,
       "xfRFDegradationValue": xfRFDegradationValue,
       "xfRFMarginValue": xfRFMarginValue,
       "xfRFOutlierTrigger": xfRFOutlierTrigger,
       "xfRFRangeTrigger": xfRFRangeTrigger,
       "xfRFStddevTrigger": xfRFStddevTrigger,
       "xfRFDegradationTrigger": xfRFDegradationTrigger,
       "xfRFMarginTrigger": xfRFMarginTrigger,
       "xfSdcTable": xfSdcTable,
       "xfSdcEntry": xfSdcEntry,
       "xfSdcCapability": xfSdcCapability,
       "xfSdcAdminStatus": xfSdcAdminStatus,
       "xfSdcOperStatus": xfSdcOperStatus,
       "xfSdcDadeControl": xfSdcDadeControl,
       "xfSdcDadeStatus": xfSdcDadeStatus,
       "xfSdcPath": xfSdcPath,
       "xfSdcOduDateTimeCalibration": xfSdcOduDateTimeCalibration,
       "xfSdcOduSerialNumber": xfSdcOduSerialNumber,
       "xfSdcGain": xfSdcGain,
       "xfSdcActualPath": xfSdcActualPath,
       "xfSdcDadeDelay": xfSdcDadeDelay,
       "xfRadioLinkPtpRadioConformance": xfRadioLinkPtpRadioConformance,
       "xfRadioLinkPtpRadioCompliances": xfRadioLinkPtpRadioCompliances,
       "xfRADIOLINKPTPRADIOFullCompliance": xfRADIOLINKPTPRADIOFullCompliance,
       "xfRadioLinkPtpRadioGroups": xfRadioLinkPtpRadioGroups,
       "xfRadioLinkPtpRadioCompleteGroup": xfRadioLinkPtpRadioCompleteGroup}
)
