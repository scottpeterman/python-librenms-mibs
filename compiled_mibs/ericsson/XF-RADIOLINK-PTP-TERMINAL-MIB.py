# SNMP MIB module (XF-RADIOLINK-PTP-TERMINAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\ericsson\XF-RADIOLINK-PTP-TERMINAL-MIB
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

(entLogicalIndex,
 entPhysicalIndex) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLogicalIndex",
    "entPhysicalIndex")

(HCPerfCurrentCount,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfCurrentCount")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(xfRadioLink,) = mibBuilder.importSymbols(
    "XF-TOP-MIB",
    "xfRadioLink")


# MODULE-IDENTITY

xfRadioLinkPtpTerminalMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1)
)
if mibBuilder.loadTexts:
    xfRadioLinkPtpTerminalMIB.setRevisions(
        ("2020-03-17 00:00",
         "2019-12-20 00:00",
         "2019-11-26 00:00",
         "2018-05-23 00:00",
         "2018-04-27 00:00",
         "2018-04-06 00:00",
         "2017-09-19 00:00",
         "2017-05-24 00:00",
         "2016-10-24 00:00",
         "2016-05-11 00:00",
         "2016-05-10 00:00",
         "2016-02-22 00:00",
         "2016-02-05 00:00",
         "2015-06-08 00:00",
         "2015-02-26 00:00",
         "2014-07-07 00:00",
         "2014-02-20 00:00",
         "2014-01-15 00:00",
         "2013-11-22 00:00",
         "2013-11-19 14:00",
         "2013-09-25 00:00",
         "2013-09-16 00:00",
         "2013-07-06 00:00",
         "2013-03-28 00:00",
         "2012-10-26 00:00",
         "2012-08-01 00:00",
         "2012-06-24 00:00",
         "2012-05-29 00:00",
         "2011-12-16 00:00",
         "2011-12-04 00:00",
         "2011-11-22 00:00",
         "2011-11-17 00:00",
         "2011-11-15 00:00",
         "2011-09-09 00:00",
         "2011-07-08 00:00",
         "2011-06-27 00:00",
         "2011-06-01 00:00",
         "2011-05-23 00:00",
         "2011-03-04 00:00",
         "2011-02-09 00:00",
         "2011-02-01 00:00",
         "2011-01-10 00:00",
         "2010-12-21 00:00",
         "2010-12-16 00:00",
         "2010-12-14 00:00",
         "2010-12-13 00:00",
         "2010-11-23 00:00",
         "2010-10-25 00:00",
         "2010-10-21 00:00",
         "2010-09-13 00:00",
         "2010-09-02 00:00",
         "2010-08-20 00:00",
         "2010-06-15 00:00",
         "2010-06-04 00:00",
         "2010-05-27 00:00",
         "2010-01-19 00:00",
         "2009-11-18 00:00",
         "2009-09-18 00:00",
         "2009-06-26 00:00",
         "2009-06-24 00:00",
         "2009-04-14 00:00",
         "2009-03-11 00:00",
         "2009-03-04 00:00",
         "2009-02-02 00:00",
         "2009-01-05 00:00",
         "2008-12-04 00:00",
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
         "2007-10-24 00:00",
         "2007-08-14 00:00",
         "2007-07-05 00:00",
         "2007-07-03 00:00",
         "2007-07-02 00:00",
         "2007-06-04 00:00",
         "2007-03-16 00:00",
         "2007-01-17 00:00",
         "2006-11-14 00:00",
         "2006-09-20 00:00",
         "2006-09-19 13:10",
         "2006-09-12 00:00",
         "2006-09-05 00:00",
         "2006-03-20 00:00",
         "2006-02-24 00:00",
         "2006-01-31 00:00",
         "2005-03-01 00:00",
         "2004-12-13 00:00",
         "2004-07-02 00:00",
         "2004-06-22 00:00",
         "2004-06-16 00:00",
         "2004-05-25 00:00",
         "2004-05-17 10:00",
         "2004-01-20 10:00",
         "2003-12-17 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TermAdaptiveManualMode(TextualConvention, Integer32):
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
          ("disable", 2),
          ("enable", 3),
          ("enabledAsRequest", 4))
    )



class TermModulation(TextualConvention, Integer32):
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



class TermOutputPowerStatus(TextualConvention, Integer32):
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
        *(("other", 1),
          ("rtpc", 2),
          ("atpc", 3),
          ("localControl", 4),
          ("ra1LocalControlRa2Rtpc", 5),
          ("ra1RtpcRa2LocalControl", 6))
    )



class ChannelMode(TextualConvention, Integer32):
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
          ("ccdp", 2),
          ("accp", 3),
          ("acap", 4))
    )



class TermRauSec(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 0),
          ("sec2", 1),
          ("sec4", 2),
          ("sec5b", 3))
    )



class TermAutoRemoveLoopEnable(TextualConvention, Integer32):
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
          ("enable", 2),
          ("disable", 3))
    )



# MIB Managed Objects in the order of their OIDs

_XfRadioLinkPtpTerminalObjects_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpTerminalObjects = _XfRadioLinkPtpTerminalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1)
)
_XfRLPtpTerminalTable_Object = MibTable
xfRLPtpTerminalTable = _XfRLPtpTerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1)
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalTable.setStatus("current")
_XfRLPtpTerminalEntry_Object = MibTableRow
xfRLPtpTerminalEntry = _XfRLPtpTerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1)
)
xfRLPtpTerminalEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalEntry.setStatus("current")


class _XfTermId_Type(SnmpAdminString):
    """Custom type xfTermId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_XfTermId_Type.__name__ = "SnmpAdminString"
_XfTermId_Object = MibTableColumn
xfTermId = _XfTermId_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 1),
    _XfTermId_Type()
)
xfTermId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermId.setStatus("current")


class _XfTermType_Type(Integer32):
    """Custom type xfTermType based on Integer32"""
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
        *(("other", 1),
          ("rlMLE", 2),
          ("rlXfMLE", 3),
          ("rlXfMLTN", 4),
          ("rlXfMLStandalone", 5),
          ("rlXfMLTNPT", 6))
    )


_XfTermType_Type.__name__ = "Integer32"
_XfTermType_Object = MibTableColumn
xfTermType = _XfTermType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 2),
    _XfTermType_Type()
)
xfTermType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermType.setStatus("current")


class _XfTermProtection_Type(Integer32):
    """Custom type xfTermProtection based on Integer32"""
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
        *(("other", 1),
          ("unprotected", 2),
          ("protectedHotStandby", 3),
          ("protectedWorkingStandby", 4),
          ("unProtectedSDC", 5),
          ("enhancedRLB", 6))
    )


_XfTermProtection_Type.__name__ = "Integer32"
_XfTermProtection_Object = MibTableColumn
xfTermProtection = _XfTermProtection_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 3),
    _XfTermProtection_Type()
)
xfTermProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermProtection.setStatus("current")


class _XfTermCapacity_Type(Integer32):
    """Custom type xfTermCapacity based on Integer32"""
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
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("twoE1", 2),
          ("fourE1", 3),
          ("oneE2", 4),
          ("twoE2", 5),
          ("oneE3oneE1", 6),
          ("twoE3", 7),
          ("fourE3", 8),
          ("fourDS1", 9),
          ("eightDS1", 10),
          ("sixteenDS1", 11),
          ("seventeenDS1", 12),
          ("oneStm0", 13),
          ("oneStm1oneE1", 14),
          ("thirtytwoDS1", 15),
          ("oneStm1oneDS1", 16),
          ("oneStm1oneE1at50MHz", 17),
          ("twentytwoE1", 18),
          ("thirtyfiveE1", 19),
          ("fortysixE1", 20),
          ("seventyfiveE1", 21),
          ("oneStm1OneJ1", 22),
          ("sixtynineDS1", 23),
          ("eightyDS1", 24),
          ("oneStm1OneE1LH", 25),
          ("oneStm1OneDS1LH", 26))
    )


_XfTermCapacity_Type.__name__ = "Integer32"
_XfTermCapacity_Object = MibTableColumn
xfTermCapacity = _XfTermCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 4),
    _XfTermCapacity_Type()
)
xfTermCapacity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermCapacity.setStatus("current")


class _XfTermCapacityCapability_Type(Bits):
    """Custom type xfTermCapacityCapability based on Bits"""
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
          ("oneStm0", 12),
          ("oneStm1oneE1", 13),
          ("thirtytwoDS1", 14),
          ("oneStm1oneDS1", 15),
          ("oneStm1oneE1at50MHz", 16),
          ("twentytwoE1", 17),
          ("thirtyfiveE1", 18),
          ("fortysixE1", 19),
          ("seventyfiveE1", 20),
          ("oneStm1OneJ1", 21),
          ("sixtynineDS1", 22),
          ("eightyDS1", 23),
          ("oneStm1OneE1LH", 24),
          ("oneStm1OneDS1LH", 25))
    )

_XfTermCapacityCapability_Type.__name__ = "Bits"
_XfTermCapacityCapability_Object = MibTableColumn
xfTermCapacityCapability = _XfTermCapacityCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 5),
    _XfTermCapacityCapability_Type()
)
xfTermCapacityCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermCapacityCapability.setStatus("current")
_XfTermModulation_Type = TermModulation
_XfTermModulation_Object = MibTableColumn
xfTermModulation = _XfTermModulation_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 6),
    _XfTermModulation_Type()
)
xfTermModulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermModulation.setStatus("current")


class _XfTermModulationCapability_Type(Bits):
    """Custom type xfTermModulationCapability based on Bits"""
    namedValues = NamedValues(
        *(("cqpsk", 0),
          ("qam16", 1),
          ("qam128", 2),
          ("qam32", 3),
          ("qam64", 4))
    )

_XfTermModulationCapability_Type.__name__ = "Bits"
_XfTermModulationCapability_Object = MibTableColumn
xfTermModulationCapability = _XfTermModulationCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 7),
    _XfTermModulationCapability_Type()
)
xfTermModulationCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermModulationCapability.setStatus("current")


class _XfTermRestore_Type(Integer32):
    """Custom type xfTermRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restore", 1)
    )


_XfTermRestore_Type.__name__ = "Integer32"
_XfTermRestore_Object = MibTableColumn
xfTermRestore = _XfTermRestore_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 8),
    _XfTermRestore_Type()
)
xfTermRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermRestore.setStatus("current")


class _XfTermAlarmSeverity_Type(Bits):
    """Custom type xfTermAlarmSeverity based on Bits"""
    namedValues = NamedValues(
        *(("termSeverity0", 0),
          ("termSeverity1", 1),
          ("termSeverity2", 2))
    )

_XfTermAlarmSeverity_Type.__name__ = "Bits"
_XfTermAlarmSeverity_Object = MibTableColumn
xfTermAlarmSeverity = _XfTermAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 9),
    _XfTermAlarmSeverity_Type()
)
xfTermAlarmSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermAlarmSeverity.setStatus("current")


class _XfTermTrapEnable_Type(Integer32):
    """Custom type xfTermTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enable", 2),
          ("disable", 3))
    )


_XfTermTrapEnable_Type.__name__ = "Integer32"
_XfTermTrapEnable_Object = MibTableColumn
xfTermTrapEnable = _XfTermTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 10),
    _XfTermTrapEnable_Type()
)
xfTermTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermTrapEnable.setStatus("current")


class _XfTermAsPort_Type(Integer32):
    """Custom type xfTermAsPort based on Integer32"""
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
              17,
              18,
              19,
              20,
              21)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 1),
          ("aspX002", 2),
          ("aspX003", 3),
          ("aspX004", 4),
          ("aspX005", 5),
          ("aspX006", 6),
          ("aspX007", 7),
          ("aspX008", 8),
          ("aspX009", 9),
          ("aspX010", 10),
          ("aspX011", 11),
          ("aspX012", 12),
          ("aspX013", 13),
          ("aspX014", 14),
          ("aspX015", 15),
          ("aspX016", 16),
          ("aspX017", 17),
          ("aspX018", 18),
          ("aspX019", 19),
          ("aspX020", 20),
          ("aspX021", 21))
    )


_XfTermAsPort_Type.__name__ = "Integer32"
_XfTermAsPort_Object = MibTableColumn
xfTermAsPort = _XfTermAsPort_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 11),
    _XfTermAsPort_Type()
)
xfTermAsPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermAsPort.setStatus("current")


class _XfTermRemoteIdCheck_Type(Integer32):
    """Custom type xfTermRemoteIdCheck based on Integer32"""
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


_XfTermRemoteIdCheck_Type.__name__ = "Integer32"
_XfTermRemoteIdCheck_Object = MibTableColumn
xfTermRemoteIdCheck = _XfTermRemoteIdCheck_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 12),
    _XfTermRemoteIdCheck_Type()
)
xfTermRemoteIdCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermRemoteIdCheck.setStatus("current")


class _XfTermRemoteId_Type(SnmpAdminString):
    """Custom type xfTermRemoteId based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_XfTermRemoteId_Type.__name__ = "SnmpAdminString"
_XfTermRemoteId_Object = MibTableColumn
xfTermRemoteId = _XfTermRemoteId_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 13),
    _XfTermRemoteId_Type()
)
xfTermRemoteId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermRemoteId.setStatus("current")


class _XfTermPreset_Type(Integer32):
    """Custom type xfTermPreset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("preset", 1)
    )


_XfTermPreset_Type.__name__ = "Integer32"
_XfTermPreset_Object = MibTableColumn
xfTermPreset = _XfTermPreset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 14),
    _XfTermPreset_Type()
)
xfTermPreset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermPreset.setStatus("current")


class _XfTermBerAlarmThreshold_Type(Integer32):
    """Custom type xfTermBerAlarmThreshold based on Integer32"""
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
          ("ber1e3", 2),
          ("ber1e4", 3),
          ("ber1e5", 4),
          ("ber1e6", 5))
    )


_XfTermBerAlarmThreshold_Type.__name__ = "Integer32"
_XfTermBerAlarmThreshold_Object = MibTableColumn
xfTermBerAlarmThreshold = _XfTermBerAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 15),
    _XfTermBerAlarmThreshold_Type()
)
xfTermBerAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermBerAlarmThreshold.setStatus("current")


class _XfTermFadeNotificationTimer_Type(Integer32):
    """Custom type xfTermFadeNotificationTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_XfTermFadeNotificationTimer_Type.__name__ = "Integer32"
_XfTermFadeNotificationTimer_Object = MibTableColumn
xfTermFadeNotificationTimer = _XfTermFadeNotificationTimer_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 16),
    _XfTermFadeNotificationTimer_Type()
)
xfTermFadeNotificationTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermFadeNotificationTimer.setStatus("current")
_XfTermEquipmentProtectionIndex_Type = Integer32
_XfTermEquipmentProtectionIndex_Object = MibTableColumn
xfTermEquipmentProtectionIndex = _XfTermEquipmentProtectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 17),
    _XfTermEquipmentProtectionIndex_Type()
)
xfTermEquipmentProtectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermEquipmentProtectionIndex.setStatus("current")


class _XfTermSysName_Type(DisplayString):
    """Custom type xfTermSysName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_XfTermSysName_Type.__name__ = "DisplayString"
_XfTermSysName_Object = MibTableColumn
xfTermSysName = _XfTermSysName_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 18),
    _XfTermSysName_Type()
)
xfTermSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermSysName.setStatus("current")
_XfTermChannelMode_Type = ChannelMode
_XfTermChannelMode_Object = MibTableColumn
xfTermChannelMode = _XfTermChannelMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 19),
    _XfTermChannelMode_Type()
)
xfTermChannelMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermChannelMode.setStatus("current")


class _XfTermChannelModeCapability_Type(Bits):
    """Custom type xfTermChannelModeCapability based on Bits"""
    namedValues = NamedValues(
        *(("ccdp", 0),
          ("accp", 1),
          ("acap", 2),
          ("ccdp16QAM", 3),
          ("ccdp64QAM", 4),
          ("ccdp128QAM", 5))
    )

_XfTermChannelModeCapability_Type.__name__ = "Bits"
_XfTermChannelModeCapability_Object = MibTableColumn
xfTermChannelModeCapability = _XfTermChannelModeCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 20),
    _XfTermChannelModeCapability_Type()
)
xfTermChannelModeCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermChannelModeCapability.setStatus("current")


class _XfTermTrafficAndDCN_Type(Integer32):
    """Custom type xfTermTrafficAndDCN based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trafficAndDCN", 1),
          ("dcnOnly", 2))
    )


_XfTermTrafficAndDCN_Type.__name__ = "Integer32"
_XfTermTrafficAndDCN_Object = MibTableColumn
xfTermTrafficAndDCN = _XfTermTrafficAndDCN_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 21),
    _XfTermTrafficAndDCN_Type()
)
xfTermTrafficAndDCN.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermTrafficAndDCN.setStatus("current")


class _XfTermFrameFormat_Type(Integer32):
    """Custom type xfTermFrameFormat based on Integer32"""
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
          ("version0", 2),
          ("version1", 3))
    )


_XfTermFrameFormat_Type.__name__ = "Integer32"
_XfTermFrameFormat_Object = MibTableColumn
xfTermFrameFormat = _XfTermFrameFormat_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 22),
    _XfTermFrameFormat_Type()
)
xfTermFrameFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermFrameFormat.setStatus("current")


class _XfTermFrameFormatCapability_Type(Bits):
    """Custom type xfTermFrameFormatCapability based on Bits"""
    namedValues = NamedValues(
        *(("version0", 0),
          ("version1", 1))
    )

_XfTermFrameFormatCapability_Type.__name__ = "Bits"
_XfTermFrameFormatCapability_Object = MibTableColumn
xfTermFrameFormatCapability = _XfTermFrameFormatCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 23),
    _XfTermFrameFormatCapability_Type()
)
xfTermFrameFormatCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermFrameFormatCapability.setStatus("current")


class _XfTermDCNRadioConfiguration_Type(Integer32):
    """Custom type xfTermDCNRadioConfiguration based on Integer32"""
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
          ("dcnRadio128kbps", 2),
          ("dcnRadio320kbpsDCCr", 3),
          ("dcnRadio320kbpsMSB", 4))
    )


_XfTermDCNRadioConfiguration_Type.__name__ = "Integer32"
_XfTermDCNRadioConfiguration_Object = MibTableColumn
xfTermDCNRadioConfiguration = _XfTermDCNRadioConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 24),
    _XfTermDCNRadioConfiguration_Type()
)
xfTermDCNRadioConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermDCNRadioConfiguration.setStatus("current")


class _XfTermDCNRadioCapability_Type(Bits):
    """Custom type xfTermDCNRadioCapability based on Bits"""
    namedValues = NamedValues(
        *(("dcnRadio128kbps", 0),
          ("dcnRadio320kbpsDCCr", 1),
          ("dcnRadio320kbpsMSB", 2))
    )

_XfTermDCNRadioCapability_Type.__name__ = "Bits"
_XfTermDCNRadioCapability_Object = MibTableColumn
xfTermDCNRadioCapability = _XfTermDCNRadioCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 25),
    _XfTermDCNRadioCapability_Type()
)
xfTermDCNRadioCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermDCNRadioCapability.setStatus("current")


class _XfTermDCNLineConfiguration_Type(Integer32):
    """Custom type xfTermDCNLineConfiguration based on Integer32"""
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
          ("transparent", 2),
          ("dcnLine192kbpsDCCr", 3),
          ("dcnLine192kbpsMSB", 4))
    )


_XfTermDCNLineConfiguration_Type.__name__ = "Integer32"
_XfTermDCNLineConfiguration_Object = MibTableColumn
xfTermDCNLineConfiguration = _XfTermDCNLineConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 26),
    _XfTermDCNLineConfiguration_Type()
)
xfTermDCNLineConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermDCNLineConfiguration.setStatus("current")


class _XfTermDCNLineCapability_Type(Bits):
    """Custom type xfTermDCNLineCapability based on Bits"""
    namedValues = NamedValues(
        *(("transparent", 0),
          ("dcnLine192kbpsDCCr", 1),
          ("dcnLine192kbpsMSB", 2))
    )

_XfTermDCNLineCapability_Type.__name__ = "Bits"
_XfTermDCNLineCapability_Object = MibTableColumn
xfTermDCNLineCapability = _XfTermDCNLineCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 27),
    _XfTermDCNLineCapability_Type()
)
xfTermDCNLineCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermDCNLineCapability.setStatus("current")


class _XfTermFadeNotificationConfiguration_Type(Integer32):
    """Custom type xfTermFadeNotificationConfiguration based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 3))
    )


_XfTermFadeNotificationConfiguration_Type.__name__ = "Integer32"
_XfTermFadeNotificationConfiguration_Object = MibTableColumn
xfTermFadeNotificationConfiguration = _XfTermFadeNotificationConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 28),
    _XfTermFadeNotificationConfiguration_Type()
)
xfTermFadeNotificationConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermFadeNotificationConfiguration.setStatus("current")


class _XfTermLineProtection_Type(Integer32):
    """Custom type xfTermLineProtection based on Integer32"""
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
        *(("other", 1),
          ("unProtected", 2),
          ("singleInterfaceLowSlot", 3),
          ("singleInterfaceHighSlot", 4),
          ("opticalSplitter", 5),
          ("equipmentAndLineProtection", 6))
    )


_XfTermLineProtection_Type.__name__ = "Integer32"
_XfTermLineProtection_Object = MibTableColumn
xfTermLineProtection = _XfTermLineProtection_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 1, 1, 29),
    _XfTermLineProtection_Type()
)
xfTermLineProtection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermLineProtection.setStatus("current")
_XfRLPtpTerminalOutputPowerTable_Object = MibTable
xfRLPtpTerminalOutputPowerTable = _XfRLPtpTerminalOutputPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 2)
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalOutputPowerTable.setStatus("current")
_XfRLPtpTerminalOutputPowerEntry_Object = MibTableRow
xfRLPtpTerminalOutputPowerEntry = _XfRLPtpTerminalOutputPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 2, 1)
)
xfRLPtpTerminalOutputPowerEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalOutputPowerEntry.setStatus("current")
_XfTermOutputPowerOperStatus_Type = TermOutputPowerStatus
_XfTermOutputPowerOperStatus_Object = MibTableColumn
xfTermOutputPowerOperStatus = _XfTermOutputPowerOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 2, 1, 1),
    _XfTermOutputPowerOperStatus_Type()
)
xfTermOutputPowerOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermOutputPowerOperStatus.setStatus("current")
_XfTermOutputPowerAdminStatus_Type = TermOutputPowerStatus
_XfTermOutputPowerAdminStatus_Object = MibTableColumn
xfTermOutputPowerAdminStatus = _XfTermOutputPowerAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 2, 1, 2),
    _XfTermOutputPowerAdminStatus_Type()
)
xfTermOutputPowerAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermOutputPowerAdminStatus.setStatus("current")


class _XfTermAtpcCapability_Type(Integer32):
    """Custom type xfTermAtpcCapability based on Integer32"""
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


_XfTermAtpcCapability_Type.__name__ = "Integer32"
_XfTermAtpcCapability_Object = MibTableColumn
xfTermAtpcCapability = _XfTermAtpcCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 2, 1, 3),
    _XfTermAtpcCapability_Type()
)
xfTermAtpcCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermAtpcCapability.setStatus("current")
_XfRLPtpTerminalPerformanceTable_Object = MibTable
xfRLPtpTerminalPerformanceTable = _XfRLPtpTerminalPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4)
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalPerformanceTable.setStatus("current")
_XfRLPtpTerminalPerformanceEntry_Object = MibTableRow
xfRLPtpTerminalPerformanceEntry = _XfRLPtpTerminalPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4, 1)
)
xfRLPtpTerminalPerformanceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalPerformanceEntry.setStatus("current")
_XfTermTimeElapsed_Type = Counter32
_XfTermTimeElapsed_Object = MibTableColumn
xfTermTimeElapsed = _XfTermTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4, 1, 1),
    _XfTermTimeElapsed_Type()
)
xfTermTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermTimeElapsed.setStatus("current")
_XfTermCurrentES_Type = Counter32
_XfTermCurrentES_Object = MibTableColumn
xfTermCurrentES = _XfTermCurrentES_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4, 1, 2),
    _XfTermCurrentES_Type()
)
xfTermCurrentES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermCurrentES.setStatus("current")
_XfTermCurrentSES_Type = Counter32
_XfTermCurrentSES_Object = MibTableColumn
xfTermCurrentSES = _XfTermCurrentSES_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4, 1, 3),
    _XfTermCurrentSES_Type()
)
xfTermCurrentSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermCurrentSES.setStatus("current")
_XfTermCurrentBBE_Type = Counter64
_XfTermCurrentBBE_Object = MibTableColumn
xfTermCurrentBBE = _XfTermCurrentBBE_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4, 1, 4),
    _XfTermCurrentBBE_Type()
)
xfTermCurrentBBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermCurrentBBE.setStatus("current")
_XfTermCurrentUAS_Type = Counter32
_XfTermCurrentUAS_Object = MibTableColumn
xfTermCurrentUAS = _XfTermCurrentUAS_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4, 1, 5),
    _XfTermCurrentUAS_Type()
)
xfTermCurrentUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermCurrentUAS.setStatus("current")
_XfTermCurrentBB_Type = Counter64
_XfTermCurrentBB_Object = MibTableColumn
xfTermCurrentBB = _XfTermCurrentBB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4, 1, 6),
    _XfTermCurrentBB_Type()
)
xfTermCurrentBB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermCurrentBB.setStatus("current")


class _XfTermPerfReset_Type(Integer32):
    """Custom type xfTermPerfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("performanceReset", 1)
    )


_XfTermPerfReset_Type.__name__ = "Integer32"
_XfTermPerfReset_Object = MibTableColumn
xfTermPerfReset = _XfTermPerfReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4, 1, 7),
    _XfTermPerfReset_Type()
)
xfTermPerfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermPerfReset.setStatus("current")
_XfTermTimeElapsedEnRLBExt_Type = Counter32
_XfTermTimeElapsedEnRLBExt_Object = MibTableColumn
xfTermTimeElapsedEnRLBExt = _XfTermTimeElapsedEnRLBExt_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 4, 1, 8),
    _XfTermTimeElapsedEnRLBExt_Type()
)
xfTermTimeElapsedEnRLBExt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermTimeElapsedEnRLBExt.setStatus("current")
_XfRLProtectionTable_Object = MibTable
xfRLProtectionTable = _XfRLProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5)
)
if mibBuilder.loadTexts:
    xfRLProtectionTable.setStatus("current")
_XfRLProtectionEntry_Object = MibTableRow
xfRLProtectionEntry = _XfRLProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5, 1)
)
xfRLProtectionEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    xfRLProtectionEntry.setStatus("current")


class _XfRLProtectionMode_Type(Integer32):
    """Custom type xfRLProtectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("unprotected", 2),
          ("protectedHotStandby", 3),
          ("protectedWorkingStandby", 4),
          ("unProtectedSDC", 5),
          ("enhancedRLBProtected", 7),
          ("enhancedRLBExtended", 8))
    )


_XfRLProtectionMode_Type.__name__ = "Integer32"
_XfRLProtectionMode_Object = MibTableColumn
xfRLProtectionMode = _XfRLProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5, 1, 1),
    _XfRLProtectionMode_Type()
)
xfRLProtectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLProtectionMode.setStatus("current")
_XfRLProtectionRau1_Type = Integer32
_XfRLProtectionRau1_Object = MibTableColumn
xfRLProtectionRau1 = _XfRLProtectionRau1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5, 1, 2),
    _XfRLProtectionRau1_Type()
)
xfRLProtectionRau1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLProtectionRau1.setStatus("current")
_XfRLProtectionRau2_Type = Integer32
_XfRLProtectionRau2_Object = MibTableColumn
xfRLProtectionRau2 = _XfRLProtectionRau2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5, 1, 3),
    _XfRLProtectionRau2_Type()
)
xfRLProtectionRau2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLProtectionRau2.setStatus("current")


class _XfRLActiveTxRadio_Type(Integer32):
    """Custom type xfRLActiveTxRadio based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txRadio1", 1),
          ("txRadio2", 2),
          ("txRadio1andtxRadio2", 3))
    )


_XfRLActiveTxRadio_Type.__name__ = "Integer32"
_XfRLActiveTxRadio_Object = MibTableColumn
xfRLActiveTxRadio = _XfRLActiveTxRadio_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5, 1, 4),
    _XfRLActiveTxRadio_Type()
)
xfRLActiveTxRadio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLActiveTxRadio.setStatus("current")


class _XfRLSwitchOverReset_Type(Integer32):
    """Custom type xfRLSwitchOverReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_XfRLSwitchOverReset_Type.__name__ = "Integer32"
_XfRLSwitchOverReset_Object = MibTableColumn
xfRLSwitchOverReset = _XfRLSwitchOverReset_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5, 1, 5),
    _XfRLSwitchOverReset_Type()
)
xfRLSwitchOverReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLSwitchOverReset.setStatus("current")


class _XfRLSwitchRevertiveTx_Type(Integer32):
    """Custom type xfRLSwitchRevertiveTx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("txRadio1", 1),
          ("txRadio2", 2),
          ("off", 3))
    )


_XfRLSwitchRevertiveTx_Type.__name__ = "Integer32"
_XfRLSwitchRevertiveTx_Object = MibTableColumn
xfRLSwitchRevertiveTx = _XfRLSwitchRevertiveTx_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5, 1, 6),
    _XfRLSwitchRevertiveTx_Type()
)
xfRLSwitchRevertiveTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLSwitchRevertiveTx.setStatus("current")


class _XfRLProtectionCapability_Type(Bits):
    """Custom type xfRLProtectionCapability based on Bits"""
    namedValues = NamedValues(
        *(("revertiveSwitching", 0),
          ("txSwitchOverConfiguration", 1))
    )

_XfRLProtectionCapability_Type.__name__ = "Bits"
_XfRLProtectionCapability_Object = MibTableColumn
xfRLProtectionCapability = _XfRLProtectionCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5, 1, 7),
    _XfRLProtectionCapability_Type()
)
xfRLProtectionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLProtectionCapability.setStatus("current")


class _XfRLTxSwitchOverConfiguration_Type(Integer32):
    """Custom type xfRLTxSwitchOverConfiguration based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 3))
    )


_XfRLTxSwitchOverConfiguration_Type.__name__ = "Integer32"
_XfRLTxSwitchOverConfiguration_Object = MibTableColumn
xfRLTxSwitchOverConfiguration = _XfRLTxSwitchOverConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 5, 1, 8),
    _XfRLTxSwitchOverConfiguration_Type()
)
xfRLTxSwitchOverConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfRLTxSwitchOverConfiguration.setStatus("current")
_XfRLLineProtectionTable_Object = MibTable
xfRLLineProtectionTable = _XfRLLineProtectionTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 6)
)
if mibBuilder.loadTexts:
    xfRLLineProtectionTable.setStatus("current")
_XfRLLineProtectionEntry_Object = MibTableRow
xfRLLineProtectionEntry = _XfRLLineProtectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 6, 1)
)
xfRLLineProtectionEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLLineProtectionEntry.setStatus("current")


class _XfRLLineProtectionStatus_Type(Bits):
    """Custom type xfRLLineProtectionStatus based on Bits"""
    namedValues = NamedValues(
        *(("hitlessPhase0", 0),
          ("hitlessPhase1", 1),
          ("hitlessPhase2", 2),
          ("txSwitchover0", 3),
          ("txSwitchover1", 4),
          ("txSwitchover2", 5),
          ("remoteTxSwitchOver0", 6),
          ("remoteTxSwitchOver1", 7),
          ("remoteTxSwitchOver2", 8),
          ("rfInputThresholdProtection0", 9),
          ("rfInputThresholdProtection1", 10),
          ("rfInputThresholdProtection2", 11))
    )

_XfRLLineProtectionStatus_Type.__name__ = "Bits"
_XfRLLineProtectionStatus_Object = MibTableColumn
xfRLLineProtectionStatus = _XfRLLineProtectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 6, 1, 1),
    _XfRLLineProtectionStatus_Type()
)
xfRLLineProtectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLLineProtectionStatus.setStatus("current")


class _XfRLLineProtectionMode_Type(Integer32):
    """Custom type xfRLLineProtectionMode based on Integer32"""
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
        *(("other", 1),
          ("unProtected", 2),
          ("singleInterfaceLowSlot", 3),
          ("singleInterfaceHighSlot", 4),
          ("opticalSplitter", 5),
          ("equipmentAndLineProtection", 6))
    )


_XfRLLineProtectionMode_Type.__name__ = "Integer32"
_XfRLLineProtectionMode_Object = MibTableColumn
xfRLLineProtectionMode = _XfRLLineProtectionMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 6, 1, 2),
    _XfRLLineProtectionMode_Type()
)
xfRLLineProtectionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRLLineProtectionMode.setStatus("current")
_XfRADIORSTable_Object = MibTable
xfRADIORSTable = _XfRADIORSTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 7)
)
if mibBuilder.loadTexts:
    xfRADIORSTable.setStatus("current")
_XfRADIORSEntry_Object = MibTableRow
xfRADIORSEntry = _XfRADIORSEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 7, 1)
)
xfRADIORSEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRADIORSEntry.setStatus("current")


class _XfRADIORSAlarms_Type(Bits):
    """Custom type xfRADIORSAlarms based on Bits"""
    namedValues = NamedValues(
        *(("timRadioSide0", 0),
          ("timRadioSide1", 1),
          ("timRadioSide2", 2))
    )

_XfRADIORSAlarms_Type.__name__ = "Bits"
_XfRADIORSAlarms_Object = MibTableColumn
xfRADIORSAlarms = _XfRADIORSAlarms_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 7, 1, 1),
    _XfRADIORSAlarms_Type()
)
xfRADIORSAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRADIORSAlarms.setStatus("current")
_XfRADIORSPerformanceTable_Object = MibTable
xfRADIORSPerformanceTable = _XfRADIORSPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 8)
)
if mibBuilder.loadTexts:
    xfRADIORSPerformanceTable.setStatus("current")
_XfRADIORSPerformanceEntry_Object = MibTableRow
xfRADIORSPerformanceEntry = _XfRADIORSPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 8, 1)
)
xfRADIORSPerformanceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRADIORSPerformanceEntry.setStatus("current")


class _XfRADIORSPerformanceAlarms_Type(Bits):
    """Custom type xfRADIORSPerformanceAlarms based on Bits"""
    namedValues = NamedValues(
        *(("b1UnavailablePeriod0", 0),
          ("b1UnavailablePeriod1", 1),
          ("b1UnavailablePeriod2", 2),
          ("b1Es15m0", 3),
          ("b1Es15m1", 4),
          ("b1Es15m2", 5),
          ("b1Ses15m0", 6),
          ("b1Ses15m1", 7),
          ("b1Ses15m2", 8),
          ("b1Bbe15m0", 9),
          ("b1Bbe15m1", 10),
          ("b1Bbe15m2", 11),
          ("b1Es24h0", 12),
          ("b1Es24h1", 13),
          ("b1Es24h2", 14),
          ("b1Ses24h0", 15),
          ("b1Ses24h1", 16),
          ("b1Ses24h2", 17),
          ("b1Bbe24h0", 18),
          ("b1Bbe24h1", 19),
          ("b1Bbe24h2", 20))
    )

_XfRADIORSPerformanceAlarms_Type.__name__ = "Bits"
_XfRADIORSPerformanceAlarms_Object = MibTableColumn
xfRADIORSPerformanceAlarms = _XfRADIORSPerformanceAlarms_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 8, 1, 1),
    _XfRADIORSPerformanceAlarms_Type()
)
xfRADIORSPerformanceAlarms.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfRADIORSPerformanceAlarms.setStatus("current")
_XfRLPMConfigTable_Object = MibTable
xfRLPMConfigTable = _XfRLPMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9)
)
if mibBuilder.loadTexts:
    xfRLPMConfigTable.setStatus("current")
_XfRLPMConfigEntry_Object = MibTableRow
xfRLPMConfigEntry = _XfRLPMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1)
)
xfRLPMConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMConfigEntry.setStatus("current")
_XfPMSetThreshold15mESs_Type = Integer32
_XfPMSetThreshold15mESs_Object = MibTableColumn
xfPMSetThreshold15mESs = _XfPMSetThreshold15mESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 1),
    _XfPMSetThreshold15mESs_Type()
)
xfPMSetThreshold15mESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold15mESs.setStatus("current")
_XfPMSetThreshold15mSESs_Type = Integer32
_XfPMSetThreshold15mSESs_Object = MibTableColumn
xfPMSetThreshold15mSESs = _XfPMSetThreshold15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 2),
    _XfPMSetThreshold15mSESs_Type()
)
xfPMSetThreshold15mSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold15mSESs.setStatus("current")
_XfPMSetThreshold15mBBEs_Type = Integer32
_XfPMSetThreshold15mBBEs_Object = MibTableColumn
xfPMSetThreshold15mBBEs = _XfPMSetThreshold15mBBEs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 3),
    _XfPMSetThreshold15mBBEs_Type()
)
xfPMSetThreshold15mBBEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold15mBBEs.setStatus("current")
_XfPMResetThreshold15mESs_Type = Integer32
_XfPMResetThreshold15mESs_Object = MibTableColumn
xfPMResetThreshold15mESs = _XfPMResetThreshold15mESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 4),
    _XfPMResetThreshold15mESs_Type()
)
xfPMResetThreshold15mESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMResetThreshold15mESs.setStatus("current")
_XfPMResetThreshold15mSESs_Type = Integer32
_XfPMResetThreshold15mSESs_Object = MibTableColumn
xfPMResetThreshold15mSESs = _XfPMResetThreshold15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 5),
    _XfPMResetThreshold15mSESs_Type()
)
xfPMResetThreshold15mSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMResetThreshold15mSESs.setStatus("current")
_XfPMResetThreshold15mBBEs_Type = Integer32
_XfPMResetThreshold15mBBEs_Object = MibTableColumn
xfPMResetThreshold15mBBEs = _XfPMResetThreshold15mBBEs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 6),
    _XfPMResetThreshold15mBBEs_Type()
)
xfPMResetThreshold15mBBEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMResetThreshold15mBBEs.setStatus("current")
_XfPMSetThreshold24hESs_Type = Integer32
_XfPMSetThreshold24hESs_Object = MibTableColumn
xfPMSetThreshold24hESs = _XfPMSetThreshold24hESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 7),
    _XfPMSetThreshold24hESs_Type()
)
xfPMSetThreshold24hESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold24hESs.setStatus("current")
_XfPMSetThreshold24hSESs_Type = Integer32
_XfPMSetThreshold24hSESs_Object = MibTableColumn
xfPMSetThreshold24hSESs = _XfPMSetThreshold24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 8),
    _XfPMSetThreshold24hSESs_Type()
)
xfPMSetThreshold24hSESs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold24hSESs.setStatus("current")
_XfPMSetThreshold24hBBEs_Type = Integer32
_XfPMSetThreshold24hBBEs_Object = MibTableColumn
xfPMSetThreshold24hBBEs = _XfPMSetThreshold24hBBEs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 9),
    _XfPMSetThreshold24hBBEs_Type()
)
xfPMSetThreshold24hBBEs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold24hBBEs.setStatus("current")


class _XfPMView_Type(Integer32):
    """Custom type xfPMView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pmEnable", 1),
          ("pmDisable", 2))
    )


_XfPMView_Type.__name__ = "Integer32"
_XfPMView_Object = MibTableColumn
xfPMView = _XfPMView_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 10),
    _XfPMView_Type()
)
xfPMView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMView.setStatus("current")


class _XfPMStatus_Type(Bits):
    """Custom type xfPMStatus based on Bits"""
    namedValues = NamedValues(
        *(("unavailablePeriod0", 0),
          ("unavailablePeriod1", 1),
          ("unavailablePeriod2", 2),
          ("es15m0", 3),
          ("es15m1", 4),
          ("es15m2", 5),
          ("ses15m0", 6),
          ("ses15m1", 7),
          ("ses15m2", 8),
          ("bbe15m0", 9),
          ("bbe15m1", 10),
          ("bbe15m2", 11),
          ("es24h0", 12),
          ("es24h1", 13),
          ("es24h2", 14),
          ("ses24h0", 15),
          ("ses24h1", 16),
          ("ses24h2", 17),
          ("bbe24h0", 18),
          ("bbe24h1", 19),
          ("bbe24h2", 20),
          ("rlts1Counter15m0", 21),
          ("rlts1Counter15m1", 22),
          ("rlts1Counter15m2", 23),
          ("rlts2Counter15m0", 24),
          ("rlts2Counter15m1", 25),
          ("rlts2Counter15m2", 26),
          ("rltmCounter15m0", 27),
          ("rltmCounter15m1", 28),
          ("rltmCounter15m2", 29),
          ("tlts1Counter15m0", 30),
          ("tlts1Counter15m1", 31),
          ("tlts1Counter15m2", 32),
          ("tltmCounter15m0", 33),
          ("tltmCounter15m1", 34),
          ("tltmCounter15m2", 35),
          ("rlts1Counter24h0", 36),
          ("rlts1Counter24h1", 37),
          ("rlts1Counter24h2", 38),
          ("rlts2Counter24h0", 39),
          ("rlts2Counter24h1", 40),
          ("rlts2Counter24h2", 41),
          ("rltmCounter24h0", 42),
          ("rltmCounter24h1", 43),
          ("rltmCounter24h2", 44),
          ("tlts1Counter24h0", 45),
          ("tlts1Counter24h1", 46),
          ("tlts1Counter24h2", 47),
          ("tltmCounter24h0", 48),
          ("tltmCounter24h1", 49),
          ("tltmCounter24h2", 50))
    )

_XfPMStatus_Type.__name__ = "Bits"
_XfPMStatus_Object = MibTableColumn
xfPMStatus = _XfPMStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 11),
    _XfPMStatus_Type()
)
xfPMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMStatus.setStatus("current")


class _XfPMRLTS1Threshold_Type(Integer32):
    """Custom type xfPMRLTS1Threshold based on Integer32"""
    defaultValue = -999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -201),
    )


_XfPMRLTS1Threshold_Type.__name__ = "Integer32"
_XfPMRLTS1Threshold_Object = MibTableColumn
xfPMRLTS1Threshold = _XfPMRLTS1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 12),
    _XfPMRLTS1Threshold_Type()
)
xfPMRLTS1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMRLTS1Threshold.setStatus("current")


class _XfPMSetThreshold15mRLTS1_Type(Integer32):
    """Custom type xfPMSetThreshold15mRLTS1 based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfPMSetThreshold15mRLTS1_Type.__name__ = "Integer32"
_XfPMSetThreshold15mRLTS1_Object = MibTableColumn
xfPMSetThreshold15mRLTS1 = _XfPMSetThreshold15mRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 13),
    _XfPMSetThreshold15mRLTS1_Type()
)
xfPMSetThreshold15mRLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold15mRLTS1.setStatus("current")


class _XfPMResetThreshold15mRLTS1_Type(Integer32):
    """Custom type xfPMResetThreshold15mRLTS1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfPMResetThreshold15mRLTS1_Type.__name__ = "Integer32"
_XfPMResetThreshold15mRLTS1_Object = MibTableColumn
xfPMResetThreshold15mRLTS1 = _XfPMResetThreshold15mRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 14),
    _XfPMResetThreshold15mRLTS1_Type()
)
xfPMResetThreshold15mRLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMResetThreshold15mRLTS1.setStatus("current")


class _XfPMRLTS2Threshold_Type(Integer32):
    """Custom type xfPMRLTS2Threshold based on Integer32"""
    defaultValue = -998

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-998, -200),
    )


_XfPMRLTS2Threshold_Type.__name__ = "Integer32"
_XfPMRLTS2Threshold_Object = MibTableColumn
xfPMRLTS2Threshold = _XfPMRLTS2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 15),
    _XfPMRLTS2Threshold_Type()
)
xfPMRLTS2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMRLTS2Threshold.setStatus("current")


class _XfPMSetThreshold15mRLTS2_Type(Integer32):
    """Custom type xfPMSetThreshold15mRLTS2 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfPMSetThreshold15mRLTS2_Type.__name__ = "Integer32"
_XfPMSetThreshold15mRLTS2_Object = MibTableColumn
xfPMSetThreshold15mRLTS2 = _XfPMSetThreshold15mRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 16),
    _XfPMSetThreshold15mRLTS2_Type()
)
xfPMSetThreshold15mRLTS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold15mRLTS2.setStatus("current")


class _XfPMResetThreshold15mRLTS2_Type(Integer32):
    """Custom type xfPMResetThreshold15mRLTS2 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfPMResetThreshold15mRLTS2_Type.__name__ = "Integer32"
_XfPMResetThreshold15mRLTS2_Object = MibTableColumn
xfPMResetThreshold15mRLTS2 = _XfPMResetThreshold15mRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 17),
    _XfPMResetThreshold15mRLTS2_Type()
)
xfPMResetThreshold15mRLTS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMResetThreshold15mRLTS2.setStatus("current")


class _XfPMSetThreshold15mRLTM_Type(Integer32):
    """Custom type xfPMSetThreshold15mRLTM based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 800),
    )


_XfPMSetThreshold15mRLTM_Type.__name__ = "Integer32"
_XfPMSetThreshold15mRLTM_Object = MibTableColumn
xfPMSetThreshold15mRLTM = _XfPMSetThreshold15mRLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 18),
    _XfPMSetThreshold15mRLTM_Type()
)
xfPMSetThreshold15mRLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold15mRLTM.setStatus("current")


class _XfPMResetThreshold15mRLTM_Type(Integer32):
    """Custom type xfPMResetThreshold15mRLTM based on Integer32"""
    defaultValue = 790

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 800),
    )


_XfPMResetThreshold15mRLTM_Type.__name__ = "Integer32"
_XfPMResetThreshold15mRLTM_Object = MibTableColumn
xfPMResetThreshold15mRLTM = _XfPMResetThreshold15mRLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 19),
    _XfPMResetThreshold15mRLTM_Type()
)
xfPMResetThreshold15mRLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMResetThreshold15mRLTM.setStatus("current")


class _XfPMTLTS1Threshold_Type(Integer32):
    """Custom type xfPMTLTS1Threshold based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
    )


_XfPMTLTS1Threshold_Type.__name__ = "Integer32"
_XfPMTLTS1Threshold_Object = MibTableColumn
xfPMTLTS1Threshold = _XfPMTLTS1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 20),
    _XfPMTLTS1Threshold_Type()
)
xfPMTLTS1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMTLTS1Threshold.setStatus("current")


class _XfPMSetThreshold15mTLTS1_Type(Integer32):
    """Custom type xfPMSetThreshold15mTLTS1 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfPMSetThreshold15mTLTS1_Type.__name__ = "Integer32"
_XfPMSetThreshold15mTLTS1_Object = MibTableColumn
xfPMSetThreshold15mTLTS1 = _XfPMSetThreshold15mTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 21),
    _XfPMSetThreshold15mTLTS1_Type()
)
xfPMSetThreshold15mTLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold15mTLTS1.setStatus("current")


class _XfPMResetThreshold15mTLTS1_Type(Integer32):
    """Custom type xfPMResetThreshold15mTLTS1 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfPMResetThreshold15mTLTS1_Type.__name__ = "Integer32"
_XfPMResetThreshold15mTLTS1_Object = MibTableColumn
xfPMResetThreshold15mTLTS1 = _XfPMResetThreshold15mTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 22),
    _XfPMResetThreshold15mTLTS1_Type()
)
xfPMResetThreshold15mTLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMResetThreshold15mTLTS1.setStatus("current")


class _XfPMSetThreshold15mTLTM_Type(Integer32):
    """Custom type xfPMSetThreshold15mTLTM based on Integer32"""
    defaultValue = 145

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 145),
    )


_XfPMSetThreshold15mTLTM_Type.__name__ = "Integer32"
_XfPMSetThreshold15mTLTM_Object = MibTableColumn
xfPMSetThreshold15mTLTM = _XfPMSetThreshold15mTLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 23),
    _XfPMSetThreshold15mTLTM_Type()
)
xfPMSetThreshold15mTLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold15mTLTM.setStatus("current")


class _XfPMResetThreshold15mTLTM_Type(Integer32):
    """Custom type xfPMResetThreshold15mTLTM based on Integer32"""
    defaultValue = 144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 145),
    )


_XfPMResetThreshold15mTLTM_Type.__name__ = "Integer32"
_XfPMResetThreshold15mTLTM_Object = MibTableColumn
xfPMResetThreshold15mTLTM = _XfPMResetThreshold15mTLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 24),
    _XfPMResetThreshold15mTLTM_Type()
)
xfPMResetThreshold15mTLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMResetThreshold15mTLTM.setStatus("current")


class _XfPMSetThreshold24hRLTS1_Type(Integer32):
    """Custom type xfPMSetThreshold24hRLTS1 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_XfPMSetThreshold24hRLTS1_Type.__name__ = "Integer32"
_XfPMSetThreshold24hRLTS1_Object = MibTableColumn
xfPMSetThreshold24hRLTS1 = _XfPMSetThreshold24hRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 25),
    _XfPMSetThreshold24hRLTS1_Type()
)
xfPMSetThreshold24hRLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold24hRLTS1.setStatus("current")


class _XfPMSetThreshold24hRLTS2_Type(Integer32):
    """Custom type xfPMSetThreshold24hRLTS2 based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_XfPMSetThreshold24hRLTS2_Type.__name__ = "Integer32"
_XfPMSetThreshold24hRLTS2_Object = MibTableColumn
xfPMSetThreshold24hRLTS2 = _XfPMSetThreshold24hRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 26),
    _XfPMSetThreshold24hRLTS2_Type()
)
xfPMSetThreshold24hRLTS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold24hRLTS2.setStatus("current")


class _XfPMSetThreshold24hRLTM_Type(Integer32):
    """Custom type xfPMSetThreshold24hRLTM based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 800),
    )


_XfPMSetThreshold24hRLTM_Type.__name__ = "Integer32"
_XfPMSetThreshold24hRLTM_Object = MibTableColumn
xfPMSetThreshold24hRLTM = _XfPMSetThreshold24hRLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 27),
    _XfPMSetThreshold24hRLTM_Type()
)
xfPMSetThreshold24hRLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold24hRLTM.setStatus("current")


class _XfPMSetThreshold24hTLTS1_Type(Integer32):
    """Custom type xfPMSetThreshold24hTLTS1 based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_XfPMSetThreshold24hTLTS1_Type.__name__ = "Integer32"
_XfPMSetThreshold24hTLTS1_Object = MibTableColumn
xfPMSetThreshold24hTLTS1 = _XfPMSetThreshold24hTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 28),
    _XfPMSetThreshold24hTLTS1_Type()
)
xfPMSetThreshold24hTLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold24hTLTS1.setStatus("current")


class _XfPMSetThreshold24hTLTM_Type(Integer32):
    """Custom type xfPMSetThreshold24hTLTM based on Integer32"""
    defaultValue = 145

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 145),
    )


_XfPMSetThreshold24hTLTM_Type.__name__ = "Integer32"
_XfPMSetThreshold24hTLTM_Object = MibTableColumn
xfPMSetThreshold24hTLTM = _XfPMSetThreshold24hTLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 9, 1, 29),
    _XfPMSetThreshold24hTLTM_Type()
)
xfPMSetThreshold24hTLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSetThreshold24hTLTM.setStatus("current")
_XfRLPMCurrent24hTable_Object = MibTable
xfRLPMCurrent24hTable = _XfRLPMCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10)
)
if mibBuilder.loadTexts:
    xfRLPMCurrent24hTable.setStatus("current")
_XfRLPMCurrent24hEntry_Object = MibTableRow
xfRLPMCurrent24hEntry = _XfRLPMCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1)
)
xfRLPMCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMCurrent24hEntry.setStatus("current")
_XfPMCurrent24hTimeElapsed_Type = Counter32
_XfPMCurrent24hTimeElapsed_Object = MibTableColumn
xfPMCurrent24hTimeElapsed = _XfPMCurrent24hTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 1),
    _XfPMCurrent24hTimeElapsed_Type()
)
xfPMCurrent24hTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hTimeElapsed.setStatus("current")
_XfPMCurrent24hESs_Type = PerfCurrentCount
_XfPMCurrent24hESs_Object = MibTableColumn
xfPMCurrent24hESs = _XfPMCurrent24hESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 2),
    _XfPMCurrent24hESs_Type()
)
xfPMCurrent24hESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hESs.setStatus("current")
_XfPMCurrent24hSESs_Type = PerfCurrentCount
_XfPMCurrent24hSESs_Object = MibTableColumn
xfPMCurrent24hSESs = _XfPMCurrent24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 3),
    _XfPMCurrent24hSESs_Type()
)
xfPMCurrent24hSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hSESs.setStatus("current")
_XfPMCurrent24hBBEs_Type = HCPerfCurrentCount
_XfPMCurrent24hBBEs_Object = MibTableColumn
xfPMCurrent24hBBEs = _XfPMCurrent24hBBEs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 4),
    _XfPMCurrent24hBBEs_Type()
)
xfPMCurrent24hBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hBBEs.setStatus("current")
_XfPMCurrent24hUASs_Type = PerfCurrentCount
_XfPMCurrent24hUASs_Object = MibTableColumn
xfPMCurrent24hUASs = _XfPMCurrent24hUASs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 5),
    _XfPMCurrent24hUASs_Type()
)
xfPMCurrent24hUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hUASs.setStatus("current")
_XfPMCurrent24hBBs_Type = HCPerfCurrentCount
_XfPMCurrent24hBBs_Object = MibTableColumn
xfPMCurrent24hBBs = _XfPMCurrent24hBBs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 6),
    _XfPMCurrent24hBBs_Type()
)
xfPMCurrent24hBBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hBBs.setStatus("current")


class _XfPMCurrent24hRLTS1_Type(Integer32):
    """Custom type xfPMCurrent24hRLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-1, -1),
    )


_XfPMCurrent24hRLTS1_Type.__name__ = "Integer32"
_XfPMCurrent24hRLTS1_Object = MibTableColumn
xfPMCurrent24hRLTS1 = _XfPMCurrent24hRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 7),
    _XfPMCurrent24hRLTS1_Type()
)
xfPMCurrent24hRLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hRLTS1.setStatus("current")


class _XfPMCurrent24hRLTS2_Type(Integer32):
    """Custom type xfPMCurrent24hRLTS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-1, -1),
    )


_XfPMCurrent24hRLTS2_Type.__name__ = "Integer32"
_XfPMCurrent24hRLTS2_Object = MibTableColumn
xfPMCurrent24hRLTS2 = _XfPMCurrent24hRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 8),
    _XfPMCurrent24hRLTS2_Type()
)
xfPMCurrent24hRLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hRLTS2.setStatus("current")


class _XfPMCurrent24hRLMin_Type(Integer32):
    """Custom type xfPMCurrent24hRLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfPMCurrent24hRLMin_Type.__name__ = "Integer32"
_XfPMCurrent24hRLMin_Object = MibTableColumn
xfPMCurrent24hRLMin = _XfPMCurrent24hRLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 9),
    _XfPMCurrent24hRLMin_Type()
)
xfPMCurrent24hRLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hRLMin.setStatus("current")


class _XfPMCurrent24hRLMax_Type(Integer32):
    """Custom type xfPMCurrent24hRLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfPMCurrent24hRLMax_Type.__name__ = "Integer32"
_XfPMCurrent24hRLMax_Object = MibTableColumn
xfPMCurrent24hRLMax = _XfPMCurrent24hRLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 10),
    _XfPMCurrent24hRLMax_Type()
)
xfPMCurrent24hRLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hRLMax.setStatus("current")


class _XfPMCurrent24hTLTS1_Type(Integer32):
    """Custom type xfPMCurrent24hTLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-1, -1),
    )


_XfPMCurrent24hTLTS1_Type.__name__ = "Integer32"
_XfPMCurrent24hTLTS1_Object = MibTableColumn
xfPMCurrent24hTLTS1 = _XfPMCurrent24hTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 11),
    _XfPMCurrent24hTLTS1_Type()
)
xfPMCurrent24hTLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hTLTS1.setStatus("current")


class _XfPMCurrent24hTLMin_Type(Integer32):
    """Custom type xfPMCurrent24hTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfPMCurrent24hTLMin_Type.__name__ = "Integer32"
_XfPMCurrent24hTLMin_Object = MibTableColumn
xfPMCurrent24hTLMin = _XfPMCurrent24hTLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 12),
    _XfPMCurrent24hTLMin_Type()
)
xfPMCurrent24hTLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hTLMin.setStatus("current")


class _XfPMCurrent24hTLMax_Type(Integer32):
    """Custom type xfPMCurrent24hTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfPMCurrent24hTLMax_Type.__name__ = "Integer32"
_XfPMCurrent24hTLMax_Object = MibTableColumn
xfPMCurrent24hTLMax = _XfPMCurrent24hTLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 13),
    _XfPMCurrent24hTLMax_Type()
)
xfPMCurrent24hTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hTLMax.setStatus("current")


class _XfPMCurrent24hMSEMin_Type(Integer32):
    """Custom type xfPMCurrent24hMSEMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMCurrent24hMSEMin_Type.__name__ = "Integer32"
_XfPMCurrent24hMSEMin_Object = MibTableColumn
xfPMCurrent24hMSEMin = _XfPMCurrent24hMSEMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 14),
    _XfPMCurrent24hMSEMin_Type()
)
xfPMCurrent24hMSEMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hMSEMin.setStatus("current")


class _XfPMCurrent24hMSEMax_Type(Integer32):
    """Custom type xfPMCurrent24hMSEMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMCurrent24hMSEMax_Type.__name__ = "Integer32"
_XfPMCurrent24hMSEMax_Object = MibTableColumn
xfPMCurrent24hMSEMax = _XfPMCurrent24hMSEMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 15),
    _XfPMCurrent24hMSEMax_Type()
)
xfPMCurrent24hMSEMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hMSEMax.setStatus("current")


class _XfPMCurrent24hXPIMin_Type(Integer32):
    """Custom type xfPMCurrent24hXPIMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMCurrent24hXPIMin_Type.__name__ = "Integer32"
_XfPMCurrent24hXPIMin_Object = MibTableColumn
xfPMCurrent24hXPIMin = _XfPMCurrent24hXPIMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 16),
    _XfPMCurrent24hXPIMin_Type()
)
xfPMCurrent24hXPIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hXPIMin.setStatus("current")


class _XfPMCurrent24hXPIMax_Type(Integer32):
    """Custom type xfPMCurrent24hXPIMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMCurrent24hXPIMax_Type.__name__ = "Integer32"
_XfPMCurrent24hXPIMax_Object = MibTableColumn
xfPMCurrent24hXPIMax = _XfPMCurrent24hXPIMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 17),
    _XfPMCurrent24hXPIMax_Type()
)
xfPMCurrent24hXPIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hXPIMax.setStatus("current")
_XfPMCurrent24hESR_Type = PerfCurrentCount
_XfPMCurrent24hESR_Object = MibTableColumn
xfPMCurrent24hESR = _XfPMCurrent24hESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 18),
    _XfPMCurrent24hESR_Type()
)
xfPMCurrent24hESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hESR.setStatus("current")
_XfPMCurrent24hSESR_Type = PerfCurrentCount
_XfPMCurrent24hSESR_Object = MibTableColumn
xfPMCurrent24hSESR = _XfPMCurrent24hSESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 19),
    _XfPMCurrent24hSESR_Type()
)
xfPMCurrent24hSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hSESR.setStatus("current")
_XfPMCurrent24hBBER_Type = HCPerfCurrentCount
_XfPMCurrent24hBBER_Object = MibTableColumn
xfPMCurrent24hBBER = _XfPMCurrent24hBBER_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 10, 1, 20),
    _XfPMCurrent24hBBER_Type()
)
xfPMCurrent24hBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent24hBBER.setStatus("current")
_XfRLPMInterval24hTable_Object = MibTable
xfRLPMInterval24hTable = _XfRLPMInterval24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11)
)
if mibBuilder.loadTexts:
    xfRLPMInterval24hTable.setStatus("current")
_XfRLPMInterval24hEntry_Object = MibTableRow
xfRLPMInterval24hEntry = _XfRLPMInterval24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1)
)
xfRLPMInterval24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMInterval24hEntry.setStatus("current")
_XfPMInterval24hESs_Type = PerfIntervalCount
_XfPMInterval24hESs_Object = MibTableColumn
xfPMInterval24hESs = _XfPMInterval24hESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 1),
    _XfPMInterval24hESs_Type()
)
xfPMInterval24hESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hESs.setStatus("current")
_XfPMInterval24hSESs_Type = PerfIntervalCount
_XfPMInterval24hSESs_Object = MibTableColumn
xfPMInterval24hSESs = _XfPMInterval24hSESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 2),
    _XfPMInterval24hSESs_Type()
)
xfPMInterval24hSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hSESs.setStatus("current")
_XfPMInterval24hBBEs_Type = HCPerfCurrentCount
_XfPMInterval24hBBEs_Object = MibTableColumn
xfPMInterval24hBBEs = _XfPMInterval24hBBEs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 3),
    _XfPMInterval24hBBEs_Type()
)
xfPMInterval24hBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hBBEs.setStatus("current")
_XfPMInterval24hUASs_Type = PerfIntervalCount
_XfPMInterval24hUASs_Object = MibTableColumn
xfPMInterval24hUASs = _XfPMInterval24hUASs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 4),
    _XfPMInterval24hUASs_Type()
)
xfPMInterval24hUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hUASs.setStatus("current")
_XfPMInterval24hBBs_Type = HCPerfCurrentCount
_XfPMInterval24hBBs_Object = MibTableColumn
xfPMInterval24hBBs = _XfPMInterval24hBBs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 5),
    _XfPMInterval24hBBs_Type()
)
xfPMInterval24hBBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hBBs.setStatus("current")
_XfPMInterval24hValidData_Type = TruthValue
_XfPMInterval24hValidData_Object = MibTableColumn
xfPMInterval24hValidData = _XfPMInterval24hValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 6),
    _XfPMInterval24hValidData_Type()
)
xfPMInterval24hValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hValidData.setStatus("current")


class _XfPMInterval24hRLTS1_Type(Integer32):
    """Custom type xfPMInterval24hRLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-1, -1),
    )


_XfPMInterval24hRLTS1_Type.__name__ = "Integer32"
_XfPMInterval24hRLTS1_Object = MibTableColumn
xfPMInterval24hRLTS1 = _XfPMInterval24hRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 7),
    _XfPMInterval24hRLTS1_Type()
)
xfPMInterval24hRLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hRLTS1.setStatus("current")


class _XfPMInterval24hRLTS2_Type(Integer32):
    """Custom type xfPMInterval24hRLTS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-1, -1),
    )


_XfPMInterval24hRLTS2_Type.__name__ = "Integer32"
_XfPMInterval24hRLTS2_Object = MibTableColumn
xfPMInterval24hRLTS2 = _XfPMInterval24hRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 8),
    _XfPMInterval24hRLTS2_Type()
)
xfPMInterval24hRLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hRLTS2.setStatus("current")


class _XfPMInterval24hRLMin_Type(Integer32):
    """Custom type xfPMInterval24hRLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfPMInterval24hRLMin_Type.__name__ = "Integer32"
_XfPMInterval24hRLMin_Object = MibTableColumn
xfPMInterval24hRLMin = _XfPMInterval24hRLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 9),
    _XfPMInterval24hRLMin_Type()
)
xfPMInterval24hRLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hRLMin.setStatus("current")


class _XfPMInterval24hRLMax_Type(Integer32):
    """Custom type xfPMInterval24hRLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfPMInterval24hRLMax_Type.__name__ = "Integer32"
_XfPMInterval24hRLMax_Object = MibTableColumn
xfPMInterval24hRLMax = _XfPMInterval24hRLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 10),
    _XfPMInterval24hRLMax_Type()
)
xfPMInterval24hRLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hRLMax.setStatus("current")


class _XfPMInterval24hTLTS1_Type(Integer32):
    """Custom type xfPMInterval24hTLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
        ValueRangeConstraint(-1, -1),
    )


_XfPMInterval24hTLTS1_Type.__name__ = "Integer32"
_XfPMInterval24hTLTS1_Object = MibTableColumn
xfPMInterval24hTLTS1 = _XfPMInterval24hTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 11),
    _XfPMInterval24hTLTS1_Type()
)
xfPMInterval24hTLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hTLTS1.setStatus("current")


class _XfPMInterval24hTLMin_Type(Integer32):
    """Custom type xfPMInterval24hTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfPMInterval24hTLMin_Type.__name__ = "Integer32"
_XfPMInterval24hTLMin_Object = MibTableColumn
xfPMInterval24hTLMin = _XfPMInterval24hTLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 12),
    _XfPMInterval24hTLMin_Type()
)
xfPMInterval24hTLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hTLMin.setStatus("current")


class _XfPMInterval24hTLMax_Type(Integer32):
    """Custom type xfPMInterval24hTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfPMInterval24hTLMax_Type.__name__ = "Integer32"
_XfPMInterval24hTLMax_Object = MibTableColumn
xfPMInterval24hTLMax = _XfPMInterval24hTLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 13),
    _XfPMInterval24hTLMax_Type()
)
xfPMInterval24hTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hTLMax.setStatus("current")


class _XfPMInterval24hMSEMin_Type(Integer32):
    """Custom type xfPMInterval24hMSEMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMInterval24hMSEMin_Type.__name__ = "Integer32"
_XfPMInterval24hMSEMin_Object = MibTableColumn
xfPMInterval24hMSEMin = _XfPMInterval24hMSEMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 14),
    _XfPMInterval24hMSEMin_Type()
)
xfPMInterval24hMSEMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hMSEMin.setStatus("current")


class _XfPMInterval24hMSEMax_Type(Integer32):
    """Custom type xfPMInterval24hMSEMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMInterval24hMSEMax_Type.__name__ = "Integer32"
_XfPMInterval24hMSEMax_Object = MibTableColumn
xfPMInterval24hMSEMax = _XfPMInterval24hMSEMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 15),
    _XfPMInterval24hMSEMax_Type()
)
xfPMInterval24hMSEMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hMSEMax.setStatus("current")


class _XfPMInterval24hXPIMin_Type(Integer32):
    """Custom type xfPMInterval24hXPIMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMInterval24hXPIMin_Type.__name__ = "Integer32"
_XfPMInterval24hXPIMin_Object = MibTableColumn
xfPMInterval24hXPIMin = _XfPMInterval24hXPIMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 16),
    _XfPMInterval24hXPIMin_Type()
)
xfPMInterval24hXPIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hXPIMin.setStatus("current")


class _XfPMInterval24hXPIMax_Type(Integer32):
    """Custom type xfPMInterval24hXPIMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMInterval24hXPIMax_Type.__name__ = "Integer32"
_XfPMInterval24hXPIMax_Object = MibTableColumn
xfPMInterval24hXPIMax = _XfPMInterval24hXPIMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 11, 1, 17),
    _XfPMInterval24hXPIMax_Type()
)
xfPMInterval24hXPIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval24hXPIMax.setStatus("current")
_XfRLPMCurrent15mTable_Object = MibTable
xfRLPMCurrent15mTable = _XfRLPMCurrent15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12)
)
if mibBuilder.loadTexts:
    xfRLPMCurrent15mTable.setStatus("current")
_XfRLPMCurrent15mEntry_Object = MibTableRow
xfRLPMCurrent15mEntry = _XfRLPMCurrent15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1)
)
xfRLPMCurrent15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMCurrent15mEntry.setStatus("current")
_XfPMCurrent15mElapsedTime_Type = Counter32
_XfPMCurrent15mElapsedTime_Object = MibTableColumn
xfPMCurrent15mElapsedTime = _XfPMCurrent15mElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 1),
    _XfPMCurrent15mElapsedTime_Type()
)
xfPMCurrent15mElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mElapsedTime.setStatus("current")
_XfPMCurrent15mESs_Type = PerfCurrentCount
_XfPMCurrent15mESs_Object = MibTableColumn
xfPMCurrent15mESs = _XfPMCurrent15mESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 2),
    _XfPMCurrent15mESs_Type()
)
xfPMCurrent15mESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mESs.setStatus("current")
_XfPMCurrent15mSESs_Type = PerfCurrentCount
_XfPMCurrent15mSESs_Object = MibTableColumn
xfPMCurrent15mSESs = _XfPMCurrent15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 3),
    _XfPMCurrent15mSESs_Type()
)
xfPMCurrent15mSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mSESs.setStatus("current")
_XfPMCurrent15mBBEs_Type = PerfCurrentCount
_XfPMCurrent15mBBEs_Object = MibTableColumn
xfPMCurrent15mBBEs = _XfPMCurrent15mBBEs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 4),
    _XfPMCurrent15mBBEs_Type()
)
xfPMCurrent15mBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mBBEs.setStatus("current")
_XfPMCurrent15mUASs_Type = PerfCurrentCount
_XfPMCurrent15mUASs_Object = MibTableColumn
xfPMCurrent15mUASs = _XfPMCurrent15mUASs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 5),
    _XfPMCurrent15mUASs_Type()
)
xfPMCurrent15mUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mUASs.setStatus("current")
_XfPMCurrent15mBBs_Type = PerfCurrentCount
_XfPMCurrent15mBBs_Object = MibTableColumn
xfPMCurrent15mBBs = _XfPMCurrent15mBBs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 6),
    _XfPMCurrent15mBBs_Type()
)
xfPMCurrent15mBBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mBBs.setStatus("current")


class _XfPMCurrent15mRLTS1_Type(Integer32):
    """Custom type xfPMCurrent15mRLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
        ValueRangeConstraint(-1, -1),
    )


_XfPMCurrent15mRLTS1_Type.__name__ = "Integer32"
_XfPMCurrent15mRLTS1_Object = MibTableColumn
xfPMCurrent15mRLTS1 = _XfPMCurrent15mRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 7),
    _XfPMCurrent15mRLTS1_Type()
)
xfPMCurrent15mRLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mRLTS1.setStatus("current")


class _XfPMCurrent15mRLTS2_Type(Integer32):
    """Custom type xfPMCurrent15mRLTS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
        ValueRangeConstraint(-1, -1),
    )


_XfPMCurrent15mRLTS2_Type.__name__ = "Integer32"
_XfPMCurrent15mRLTS2_Object = MibTableColumn
xfPMCurrent15mRLTS2 = _XfPMCurrent15mRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 8),
    _XfPMCurrent15mRLTS2_Type()
)
xfPMCurrent15mRLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mRLTS2.setStatus("current")


class _XfPMCurrent15mRLMin_Type(Integer32):
    """Custom type xfPMCurrent15mRLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfPMCurrent15mRLMin_Type.__name__ = "Integer32"
_XfPMCurrent15mRLMin_Object = MibTableColumn
xfPMCurrent15mRLMin = _XfPMCurrent15mRLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 9),
    _XfPMCurrent15mRLMin_Type()
)
xfPMCurrent15mRLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mRLMin.setStatus("current")


class _XfPMCurrent15mRLMax_Type(Integer32):
    """Custom type xfPMCurrent15mRLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfPMCurrent15mRLMax_Type.__name__ = "Integer32"
_XfPMCurrent15mRLMax_Object = MibTableColumn
xfPMCurrent15mRLMax = _XfPMCurrent15mRLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 10),
    _XfPMCurrent15mRLMax_Type()
)
xfPMCurrent15mRLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mRLMax.setStatus("current")


class _XfPMCurrent15mTLTS1_Type(Integer32):
    """Custom type xfPMCurrent15mTLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
        ValueRangeConstraint(-1, -1),
    )


_XfPMCurrent15mTLTS1_Type.__name__ = "Integer32"
_XfPMCurrent15mTLTS1_Object = MibTableColumn
xfPMCurrent15mTLTS1 = _XfPMCurrent15mTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 11),
    _XfPMCurrent15mTLTS1_Type()
)
xfPMCurrent15mTLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mTLTS1.setStatus("current")


class _XfPMCurrent15mTLMin_Type(Integer32):
    """Custom type xfPMCurrent15mTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfPMCurrent15mTLMin_Type.__name__ = "Integer32"
_XfPMCurrent15mTLMin_Object = MibTableColumn
xfPMCurrent15mTLMin = _XfPMCurrent15mTLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 12),
    _XfPMCurrent15mTLMin_Type()
)
xfPMCurrent15mTLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mTLMin.setStatus("current")


class _XfPMCurrent15mTLMax_Type(Integer32):
    """Custom type xfPMCurrent15mTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfPMCurrent15mTLMax_Type.__name__ = "Integer32"
_XfPMCurrent15mTLMax_Object = MibTableColumn
xfPMCurrent15mTLMax = _XfPMCurrent15mTLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 13),
    _XfPMCurrent15mTLMax_Type()
)
xfPMCurrent15mTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mTLMax.setStatus("current")


class _XfPMCurrent15mMSEMin_Type(Integer32):
    """Custom type xfPMCurrent15mMSEMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMCurrent15mMSEMin_Type.__name__ = "Integer32"
_XfPMCurrent15mMSEMin_Object = MibTableColumn
xfPMCurrent15mMSEMin = _XfPMCurrent15mMSEMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 14),
    _XfPMCurrent15mMSEMin_Type()
)
xfPMCurrent15mMSEMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mMSEMin.setStatus("current")


class _XfPMCurrent15mMSEMax_Type(Integer32):
    """Custom type xfPMCurrent15mMSEMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMCurrent15mMSEMax_Type.__name__ = "Integer32"
_XfPMCurrent15mMSEMax_Object = MibTableColumn
xfPMCurrent15mMSEMax = _XfPMCurrent15mMSEMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 15),
    _XfPMCurrent15mMSEMax_Type()
)
xfPMCurrent15mMSEMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mMSEMax.setStatus("current")


class _XfPMCurrent15mXPIMin_Type(Integer32):
    """Custom type xfPMCurrent15mXPIMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMCurrent15mXPIMin_Type.__name__ = "Integer32"
_XfPMCurrent15mXPIMin_Object = MibTableColumn
xfPMCurrent15mXPIMin = _XfPMCurrent15mXPIMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 16),
    _XfPMCurrent15mXPIMin_Type()
)
xfPMCurrent15mXPIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mXPIMin.setStatus("current")


class _XfPMCurrent15mXPIMax_Type(Integer32):
    """Custom type xfPMCurrent15mXPIMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMCurrent15mXPIMax_Type.__name__ = "Integer32"
_XfPMCurrent15mXPIMax_Object = MibTableColumn
xfPMCurrent15mXPIMax = _XfPMCurrent15mXPIMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 17),
    _XfPMCurrent15mXPIMax_Type()
)
xfPMCurrent15mXPIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mXPIMax.setStatus("current")
_XfPMCurrent15mESR_Type = PerfCurrentCount
_XfPMCurrent15mESR_Object = MibTableColumn
xfPMCurrent15mESR = _XfPMCurrent15mESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 18),
    _XfPMCurrent15mESR_Type()
)
xfPMCurrent15mESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mESR.setStatus("current")
_XfPMCurrent15mSESR_Type = PerfCurrentCount
_XfPMCurrent15mSESR_Object = MibTableColumn
xfPMCurrent15mSESR = _XfPMCurrent15mSESR_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 19),
    _XfPMCurrent15mSESR_Type()
)
xfPMCurrent15mSESR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mSESR.setStatus("current")
_XfPMCurrent15mBBER_Type = HCPerfCurrentCount
_XfPMCurrent15mBBER_Object = MibTableColumn
xfPMCurrent15mBBER = _XfPMCurrent15mBBER_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 12, 1, 20),
    _XfPMCurrent15mBBER_Type()
)
xfPMCurrent15mBBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMCurrent15mBBER.setStatus("current")
_XfRLPMInterval15mTable_Object = MibTable
xfRLPMInterval15mTable = _XfRLPMInterval15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13)
)
if mibBuilder.loadTexts:
    xfRLPMInterval15mTable.setStatus("current")
_XfRLPMInterval15mEntry_Object = MibTableRow
xfRLPMInterval15mEntry = _XfRLPMInterval15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1)
)
xfRLPMInterval15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mIntervalNumber"),
)
if mibBuilder.loadTexts:
    xfRLPMInterval15mEntry.setStatus("current")


class _XfPMInterval15mIntervalNumber_Type(Integer32):
    """Custom type xfPMInterval15mIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_XfPMInterval15mIntervalNumber_Type.__name__ = "Integer32"
_XfPMInterval15mIntervalNumber_Object = MibTableColumn
xfPMInterval15mIntervalNumber = _XfPMInterval15mIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 1),
    _XfPMInterval15mIntervalNumber_Type()
)
xfPMInterval15mIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mIntervalNumber.setStatus("current")
_XfPMInterval15mESs_Type = PerfIntervalCount
_XfPMInterval15mESs_Object = MibTableColumn
xfPMInterval15mESs = _XfPMInterval15mESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 2),
    _XfPMInterval15mESs_Type()
)
xfPMInterval15mESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mESs.setStatus("current")
_XfPMInterval15mSESs_Type = PerfIntervalCount
_XfPMInterval15mSESs_Object = MibTableColumn
xfPMInterval15mSESs = _XfPMInterval15mSESs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 3),
    _XfPMInterval15mSESs_Type()
)
xfPMInterval15mSESs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mSESs.setStatus("current")
_XfPMInterval15mBBEs_Type = PerfIntervalCount
_XfPMInterval15mBBEs_Object = MibTableColumn
xfPMInterval15mBBEs = _XfPMInterval15mBBEs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 4),
    _XfPMInterval15mBBEs_Type()
)
xfPMInterval15mBBEs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mBBEs.setStatus("current")
_XfPMInterval15mUASs_Type = PerfIntervalCount
_XfPMInterval15mUASs_Object = MibTableColumn
xfPMInterval15mUASs = _XfPMInterval15mUASs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 5),
    _XfPMInterval15mUASs_Type()
)
xfPMInterval15mUASs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mUASs.setStatus("current")
_XfPMInterval15mBBs_Type = PerfIntervalCount
_XfPMInterval15mBBs_Object = MibTableColumn
xfPMInterval15mBBs = _XfPMInterval15mBBs_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 6),
    _XfPMInterval15mBBs_Type()
)
xfPMInterval15mBBs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mBBs.setStatus("current")
_XfPMInterval15mValidData_Type = TruthValue
_XfPMInterval15mValidData_Object = MibTableColumn
xfPMInterval15mValidData = _XfPMInterval15mValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 7),
    _XfPMInterval15mValidData_Type()
)
xfPMInterval15mValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mValidData.setStatus("current")


class _XfPMInterval15mRLTS1_Type(Integer32):
    """Custom type xfPMInterval15mRLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
        ValueRangeConstraint(-1, -1),
    )


_XfPMInterval15mRLTS1_Type.__name__ = "Integer32"
_XfPMInterval15mRLTS1_Object = MibTableColumn
xfPMInterval15mRLTS1 = _XfPMInterval15mRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 8),
    _XfPMInterval15mRLTS1_Type()
)
xfPMInterval15mRLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mRLTS1.setStatus("current")


class _XfPMInterval15mRLTS2_Type(Integer32):
    """Custom type xfPMInterval15mRLTS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
        ValueRangeConstraint(-1, -1),
    )


_XfPMInterval15mRLTS2_Type.__name__ = "Integer32"
_XfPMInterval15mRLTS2_Object = MibTableColumn
xfPMInterval15mRLTS2 = _XfPMInterval15mRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 9),
    _XfPMInterval15mRLTS2_Type()
)
xfPMInterval15mRLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mRLTS2.setStatus("current")


class _XfPMInterval15mRLMin_Type(Integer32):
    """Custom type xfPMInterval15mRLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfPMInterval15mRLMin_Type.__name__ = "Integer32"
_XfPMInterval15mRLMin_Object = MibTableColumn
xfPMInterval15mRLMin = _XfPMInterval15mRLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 10),
    _XfPMInterval15mRLMin_Type()
)
xfPMInterval15mRLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mRLMin.setStatus("current")


class _XfPMInterval15mRLMax_Type(Integer32):
    """Custom type xfPMInterval15mRLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfPMInterval15mRLMax_Type.__name__ = "Integer32"
_XfPMInterval15mRLMax_Object = MibTableColumn
xfPMInterval15mRLMax = _XfPMInterval15mRLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 11),
    _XfPMInterval15mRLMax_Type()
)
xfPMInterval15mRLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mRLMax.setStatus("current")


class _XfPMInterval15mTLTS1_Type(Integer32):
    """Custom type xfPMInterval15mTLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
        ValueRangeConstraint(-1, -1),
    )


_XfPMInterval15mTLTS1_Type.__name__ = "Integer32"
_XfPMInterval15mTLTS1_Object = MibTableColumn
xfPMInterval15mTLTS1 = _XfPMInterval15mTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 12),
    _XfPMInterval15mTLTS1_Type()
)
xfPMInterval15mTLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mTLTS1.setStatus("current")


class _XfPMInterval15mTLMin_Type(Integer32):
    """Custom type xfPMInterval15mTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfPMInterval15mTLMin_Type.__name__ = "Integer32"
_XfPMInterval15mTLMin_Object = MibTableColumn
xfPMInterval15mTLMin = _XfPMInterval15mTLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 13),
    _XfPMInterval15mTLMin_Type()
)
xfPMInterval15mTLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mTLMin.setStatus("current")


class _XfPMInterval15mTLMax_Type(Integer32):
    """Custom type xfPMInterval15mTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfPMInterval15mTLMax_Type.__name__ = "Integer32"
_XfPMInterval15mTLMax_Object = MibTableColumn
xfPMInterval15mTLMax = _XfPMInterval15mTLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 14),
    _XfPMInterval15mTLMax_Type()
)
xfPMInterval15mTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mTLMax.setStatus("current")


class _XfPMInterval15mMSEMin_Type(Integer32):
    """Custom type xfPMInterval15mMSEMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMInterval15mMSEMin_Type.__name__ = "Integer32"
_XfPMInterval15mMSEMin_Object = MibTableColumn
xfPMInterval15mMSEMin = _XfPMInterval15mMSEMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 15),
    _XfPMInterval15mMSEMin_Type()
)
xfPMInterval15mMSEMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mMSEMin.setStatus("current")


class _XfPMInterval15mMSEMax_Type(Integer32):
    """Custom type xfPMInterval15mMSEMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMInterval15mMSEMax_Type.__name__ = "Integer32"
_XfPMInterval15mMSEMax_Object = MibTableColumn
xfPMInterval15mMSEMax = _XfPMInterval15mMSEMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 16),
    _XfPMInterval15mMSEMax_Type()
)
xfPMInterval15mMSEMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mMSEMax.setStatus("current")


class _XfPMInterval15mXPIMin_Type(Integer32):
    """Custom type xfPMInterval15mXPIMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMInterval15mXPIMin_Type.__name__ = "Integer32"
_XfPMInterval15mXPIMin_Object = MibTableColumn
xfPMInterval15mXPIMin = _XfPMInterval15mXPIMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 17),
    _XfPMInterval15mXPIMin_Type()
)
xfPMInterval15mXPIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mXPIMin.setStatus("current")


class _XfPMInterval15mXPIMax_Type(Integer32):
    """Custom type xfPMInterval15mXPIMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfPMInterval15mXPIMax_Type.__name__ = "Integer32"
_XfPMInterval15mXPIMax_Object = MibTableColumn
xfPMInterval15mXPIMax = _XfPMInterval15mXPIMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 13, 1, 18),
    _XfPMInterval15mXPIMax_Type()
)
xfPMInterval15mXPIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMInterval15mXPIMax.setStatus("current")
_XfRLPtpTerminalXTable_Object = MibTable
xfRLPtpTerminalXTable = _XfRLPtpTerminalXTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14)
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalXTable.setStatus("current")
_XfRLPtpTerminalXEntry_Object = MibTableRow
xfRLPtpTerminalXEntry = _XfRLPtpTerminalXEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1)
)
xfRLPtpTerminalXEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalXEntry.setStatus("current")


class _XfTermInterfaces_Type(Integer32):
    """Custom type xfTermInterfaces based on Integer32"""
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
          ("pdhToTdmHier", 2),
          ("pdhToTdmFlat", 3),
          ("pdhToTdmFlatAndBitpipeToPtp", 4),
          ("pdhToTdmAndSDHToSFP", 5),
          ("pdhToTdmAndSDHToPtp", 6),
          ("pdhToTdmAndSDHToSFPHAndSDHToPtP", 7))
    )


_XfTermInterfaces_Type.__name__ = "Integer32"
_XfTermInterfaces_Object = MibTableColumn
xfTermInterfaces = _XfTermInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 1),
    _XfTermInterfaces_Type()
)
xfTermInterfaces.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermInterfaces.setStatus("current")


class _XfTermInterfacesCapability_Type(Bits):
    """Custom type xfTermInterfacesCapability based on Bits"""
    namedValues = NamedValues(
        *(("pdhToTdmHier", 0),
          ("pdhToTdmFlat", 1),
          ("pdhToTdmFlatAndBitpipeToPtp", 2),
          ("pdhToTdmAndSDHToSFP", 3),
          ("pdhToTdmAndSDHToPtp", 4))
    )

_XfTermInterfacesCapability_Type.__name__ = "Bits"
_XfTermInterfacesCapability_Object = MibTableColumn
xfTermInterfacesCapability = _XfTermInterfacesCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 2),
    _XfTermInterfacesCapability_Type()
)
xfTermInterfacesCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermInterfacesCapability.setStatus("current")
_XfTermChannelModeOperStatus_Type = ChannelMode
_XfTermChannelModeOperStatus_Object = MibTableColumn
xfTermChannelModeOperStatus = _XfTermChannelModeOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 3),
    _XfTermChannelModeOperStatus_Type()
)
xfTermChannelModeOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermChannelModeOperStatus.setStatus("current")


class _XfTermXPICRestore_Type(Integer32):
    """Custom type xfTermXPICRestore based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("xPicRestore", 1)
    )


_XfTermXPICRestore_Type.__name__ = "Integer32"
_XfTermXPICRestore_Object = MibTableColumn
xfTermXPICRestore = _XfTermXPICRestore_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 4),
    _XfTermXPICRestore_Type()
)
xfTermXPICRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermXPICRestore.setStatus("current")
_XfTermTribCapacityActual_Type = Integer32
_XfTermTribCapacityActual_Object = MibTableColumn
xfTermTribCapacityActual = _XfTermTribCapacityActual_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 5),
    _XfTermTribCapacityActual_Type()
)
xfTermTribCapacityActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermTribCapacityActual.setStatus("current")
_XfTermTribCapacityDesired_Type = Integer32
_XfTermTribCapacityDesired_Object = MibTableColumn
xfTermTribCapacityDesired = _XfTermTribCapacityDesired_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 6),
    _XfTermTribCapacityDesired_Type()
)
xfTermTribCapacityDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermTribCapacityDesired.setStatus("current")
_XfTermBitPipeCapacity_Type = Integer32
_XfTermBitPipeCapacity_Object = MibTableColumn
xfTermBitPipeCapacity = _XfTermBitPipeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 7),
    _XfTermBitPipeCapacity_Type()
)
xfTermBitPipeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermBitPipeCapacity.setStatus("current")


class _XfTermRowIndex_Type(Integer32):
    """Custom type xfTermRowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100000),
    )


_XfTermRowIndex_Type.__name__ = "Integer32"
_XfTermRowIndex_Object = MibTableColumn
xfTermRowIndex = _XfTermRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 8),
    _XfTermRowIndex_Type()
)
xfTermRowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermRowIndex.setStatus("current")
_XfTermCapabilitiesLastChange_Type = TimeTicks
_XfTermCapabilitiesLastChange_Object = MibTableColumn
xfTermCapabilitiesLastChange = _XfTermCapabilitiesLastChange_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 9),
    _XfTermCapabilitiesLastChange_Type()
)
xfTermCapabilitiesLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermCapabilitiesLastChange.setStatus("current")
_XfTermActualRowIndex_Type = Integer32
_XfTermActualRowIndex_Object = MibTableColumn
xfTermActualRowIndex = _XfTermActualRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 10),
    _XfTermActualRowIndex_Type()
)
xfTermActualRowIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermActualRowIndex.setStatus("current")
_XfTermMaxRowIndex_Type = Integer32
_XfTermMaxRowIndex_Object = MibTableColumn
xfTermMaxRowIndex = _XfTermMaxRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 11),
    _XfTermMaxRowIndex_Type()
)
xfTermMaxRowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermMaxRowIndex.setStatus("current")
_XfTermAdaptiveManualRowIndex_Type = Integer32
_XfTermAdaptiveManualRowIndex_Object = MibTableColumn
xfTermAdaptiveManualRowIndex = _XfTermAdaptiveManualRowIndex_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 12),
    _XfTermAdaptiveManualRowIndex_Type()
)
xfTermAdaptiveManualRowIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermAdaptiveManualRowIndex.setStatus("current")
_XfTermAdaptiveManualMode_Type = TermAdaptiveManualMode
_XfTermAdaptiveManualMode_Object = MibTableColumn
xfTermAdaptiveManualMode = _XfTermAdaptiveManualMode_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 13),
    _XfTermAdaptiveManualMode_Type()
)
xfTermAdaptiveManualMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermAdaptiveManualMode.setStatus("current")


class _XfTermSpectrumEfficiencyClass_Type(Integer32):
    """Custom type xfTermSpectrumEfficiencyClass based on Integer32"""
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


_XfTermSpectrumEfficiencyClass_Type.__name__ = "Integer32"
_XfTermSpectrumEfficiencyClass_Object = MibTableColumn
xfTermSpectrumEfficiencyClass = _XfTermSpectrumEfficiencyClass_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 14),
    _XfTermSpectrumEfficiencyClass_Type()
)
xfTermSpectrumEfficiencyClass.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermSpectrumEfficiencyClass.setStatus("current")


class _XfTermSpectrumEfficiencyClassCapability_Type(Bits):
    """Custom type xfTermSpectrumEfficiencyClassCapability based on Bits"""
    namedValues = NamedValues(
        *(("sec2", 0),
          ("sec3", 1),
          ("sec4L", 2),
          ("sec4H", 3),
          ("sec5A", 4),
          ("sec5B", 5),
          ("sec6A", 6),
          ("sec6B", 7))
    )

_XfTermSpectrumEfficiencyClassCapability_Type.__name__ = "Bits"
_XfTermSpectrumEfficiencyClassCapability_Object = MibTableColumn
xfTermSpectrumEfficiencyClassCapability = _XfTermSpectrumEfficiencyClassCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 15),
    _XfTermSpectrumEfficiencyClassCapability_Type()
)
xfTermSpectrumEfficiencyClassCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermSpectrumEfficiencyClassCapability.setStatus("current")
_XfTermIpAddress_Type = IpAddress
_XfTermIpAddress_Object = MibTableColumn
xfTermIpAddress = _XfTermIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 16),
    _XfTermIpAddress_Type()
)
xfTermIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermIpAddress.setStatus("current")


class _XfTermProtectionCapability_Type(Bits):
    """Custom type xfTermProtectionCapability based on Bits"""
    namedValues = NamedValues(
        *(("unprotected", 0),
          ("protectedHotStandby", 1),
          ("protectedWorkingStandby", 2),
          ("unprotectedSD", 3),
          ("nplus1", 4),
          ("enhancedRLB", 5))
    )

_XfTermProtectionCapability_Type.__name__ = "Bits"
_XfTermProtectionCapability_Object = MibTableColumn
xfTermProtectionCapability = _XfTermProtectionCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 17),
    _XfTermProtectionCapability_Type()
)
xfTermProtectionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermProtectionCapability.setStatus("current")


class _XfTermLineProtectionCapability_Type(Bits):
    """Custom type xfTermLineProtectionCapability based on Bits"""
    namedValues = NamedValues(
        *(("unprotected", 0),
          ("singleInterfaceLowSlot", 1),
          ("singleInterfaceHighSlot", 2),
          ("opticalSplitter", 3),
          ("equipmentAndLineProtection", 4))
    )

_XfTermLineProtectionCapability_Type.__name__ = "Bits"
_XfTermLineProtectionCapability_Object = MibTableColumn
xfTermLineProtectionCapability = _XfTermLineProtectionCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 18),
    _XfTermLineProtectionCapability_Type()
)
xfTermLineProtectionCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermLineProtectionCapability.setStatus("current")


class _XfTermTribAllocationActual_Type(Bits):
    """Custom type xfTermTribAllocationActual based on Bits"""
    namedValues = NamedValues(
        ("firstE1", 0)
    )

_XfTermTribAllocationActual_Type.__name__ = "Bits"
_XfTermTribAllocationActual_Object = MibTableColumn
xfTermTribAllocationActual = _XfTermTribAllocationActual_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 19),
    _XfTermTribAllocationActual_Type()
)
xfTermTribAllocationActual.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermTribAllocationActual.setStatus("current")


class _XfTermTribAllocationDesired_Type(Bits):
    """Custom type xfTermTribAllocationDesired based on Bits"""
    namedValues = NamedValues(
        ("firstE1", 0)
    )

_XfTermTribAllocationDesired_Type.__name__ = "Bits"
_XfTermTribAllocationDesired_Object = MibTableColumn
xfTermTribAllocationDesired = _XfTermTribAllocationDesired_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 20),
    _XfTermTribAllocationDesired_Type()
)
xfTermTribAllocationDesired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermTribAllocationDesired.setStatus("current")
_XfTermAutoRemoveLoopEnable_Type = TermAutoRemoveLoopEnable
_XfTermAutoRemoveLoopEnable_Object = MibTableColumn
xfTermAutoRemoveLoopEnable = _XfTermAutoRemoveLoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 21),
    _XfTermAutoRemoveLoopEnable_Type()
)
xfTermAutoRemoveLoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermAutoRemoveLoopEnable.setStatus("current")


class _XfTermCapability_Type(Bits):
    """Custom type xfTermCapability based on Bits"""
    namedValues = NamedValues(
        *(("adaptiveManualTx", 0),
          ("adaptiveManualRx", 1),
          ("fragmentedTributaries", 2),
          ("terminalCapacityLicense", 3))
    )

_XfTermCapability_Type.__name__ = "Bits"
_XfTermCapability_Object = MibTableColumn
xfTermCapability = _XfTermCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 22),
    _XfTermCapability_Type()
)
xfTermCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermCapability.setStatus("current")


class _XfTermCapacityLicense_Type(Integer32):
    """Custom type xfTermCapacityLicense based on Integer32"""
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
        *(("vr0", 0),
          ("vr10", 1),
          ("vr25", 2),
          ("vr50", 3),
          ("vr100", 4),
          ("vr15", 5),
          ("vr30", 6),
          ("vr60", 7),
          ("vr125", 8),
          ("vr200", 9),
          ("vr350", 10),
          ("vr4", 11),
          ("vr500", 12),
          ("vr150", 13),
          ("vr250", 14),
          ("vr300", 15),
          ("vr400", 16),
          ("vr450", 17))
    )


_XfTermCapacityLicense_Type.__name__ = "Integer32"
_XfTermCapacityLicense_Object = MibTableColumn
xfTermCapacityLicense = _XfTermCapacityLicense_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 23),
    _XfTermCapacityLicense_Type()
)
xfTermCapacityLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermCapacityLicense.setStatus("current")


class _XfTermFadingRates_Type(Integer32):
    """Custom type xfTermFadingRates based on Integer32"""
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
          ("fr50", 2),
          ("fr100", 3))
    )


_XfTermFadingRates_Type.__name__ = "Integer32"
_XfTermFadingRates_Object = MibTableColumn
xfTermFadingRates = _XfTermFadingRates_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 24),
    _XfTermFadingRates_Type()
)
xfTermFadingRates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfTermFadingRates.setStatus("current")


class _XfTermFadingRatesCapability_Type(Bits):
    """Custom type xfTermFadingRatesCapability based on Bits"""
    namedValues = NamedValues(
        *(("fr50", 0),
          ("fr100", 1))
    )

_XfTermFadingRatesCapability_Type.__name__ = "Bits"
_XfTermFadingRatesCapability_Object = MibTableColumn
xfTermFadingRatesCapability = _XfTermFadingRatesCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 25),
    _XfTermFadingRatesCapability_Type()
)
xfTermFadingRatesCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermFadingRatesCapability.setStatus("current")
_XfTermConfiguredBitPipeCapacity_Type = Integer32
_XfTermConfiguredBitPipeCapacity_Object = MibTableColumn
xfTermConfiguredBitPipeCapacity = _XfTermConfiguredBitPipeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 26),
    _XfTermConfiguredBitPipeCapacity_Type()
)
xfTermConfiguredBitPipeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermConfiguredBitPipeCapacity.setStatus("current")
_XfTermTribCapacityConfigured_Type = Integer32
_XfTermTribCapacityConfigured_Object = MibTableColumn
xfTermTribCapacityConfigured = _XfTermTribCapacityConfigured_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 27),
    _XfTermTribCapacityConfigured_Type()
)
xfTermTribCapacityConfigured.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermTribCapacityConfigured.setStatus("current")
_XfTermPacketMaxCapacity_Type = Integer32
_XfTermPacketMaxCapacity_Object = MibTableColumn
xfTermPacketMaxCapacity = _XfTermPacketMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 28),
    _XfTermPacketMaxCapacity_Type()
)
xfTermPacketMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermPacketMaxCapacity.setStatus("current")
_XfTermPacketMinCapacity_Type = Integer32
_XfTermPacketMinCapacity_Object = MibTableColumn
xfTermPacketMinCapacity = _XfTermPacketMinCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 14, 1, 29),
    _XfTermPacketMinCapacity_Type()
)
xfTermPacketMinCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermPacketMinCapacity.setStatus("current")
_XfRlPtpTerminalCapabilityTable_Object = MibTable
xfRlPtpTerminalCapabilityTable = _XfRlPtpTerminalCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15)
)
if mibBuilder.loadTexts:
    xfRlPtpTerminalCapabilityTable.setStatus("current")
_XfRlPtpTerminalCapabilityEntry_Object = MibTableRow
xfRlPtpTerminalCapabilityEntry = _XfRlPtpTerminalCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1)
)
xfRlPtpTerminalCapabilityEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
    (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRowIndex"),
)
if mibBuilder.loadTexts:
    xfRlPtpTerminalCapabilityEntry.setStatus("current")


class _XfTermChannelSpacing_Type(Integer32):
    """Custom type xfTermChannelSpacing based on Integer32"""
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
          ("chsp3500kHz", 10),
          ("chsp60MHz", 11))
    )


_XfTermChannelSpacing_Type.__name__ = "Integer32"
_XfTermChannelSpacing_Object = MibTableColumn
xfTermChannelSpacing = _XfTermChannelSpacing_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 1),
    _XfTermChannelSpacing_Type()
)
xfTermChannelSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermChannelSpacing.setStatus("current")
_XfTermChannelModulation_Type = TermModulation
_XfTermChannelModulation_Object = MibTableColumn
xfTermChannelModulation = _XfTermChannelModulation_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 2),
    _XfTermChannelModulation_Type()
)
xfTermChannelModulation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermChannelModulation.setStatus("current")
_XfTermMaxTribCapacity_Type = Integer32
_XfTermMaxTribCapacity_Object = MibTableColumn
xfTermMaxTribCapacity = _XfTermMaxTribCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 3),
    _XfTermMaxTribCapacity_Type()
)
xfTermMaxTribCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermMaxTribCapacity.setStatus("current")
_XfTermDCNCapacity_Type = Integer32
_XfTermDCNCapacity_Object = MibTableColumn
xfTermDCNCapacity = _XfTermDCNCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 4),
    _XfTermDCNCapacity_Type()
)
xfTermDCNCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermDCNCapacity.setStatus("current")


class _XfTermValidRow_Type(Integer32):
    """Custom type xfTermValidRow based on Integer32"""
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
        *(("vr0", 0),
          ("vr10", 1),
          ("vr25", 2),
          ("vr50", 3),
          ("vr100", 4),
          ("vr15", 5),
          ("vr30", 6),
          ("vr60", 7),
          ("vr125", 8),
          ("vr200", 9),
          ("vr350", 10),
          ("vr4", 11),
          ("vr500", 12),
          ("vr150", 13),
          ("vr250", 14),
          ("vr300", 15),
          ("vr400", 16),
          ("vr450", 17))
    )


_XfTermValidRow_Type.__name__ = "Integer32"
_XfTermValidRow_Object = MibTableColumn
xfTermValidRow = _XfTermValidRow_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 5),
    _XfTermValidRow_Type()
)
xfTermValidRow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermValidRow.setStatus("current")
_XfTermMaxCapacity_Type = Integer32
_XfTermMaxCapacity_Object = MibTableColumn
xfTermMaxCapacity = _XfTermMaxCapacity_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 6),
    _XfTermMaxCapacity_Type()
)
xfTermMaxCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermMaxCapacity.setStatus("current")
_XfTermSpectrumEfficiencyClassObsolete_Type = TermRauSec
_XfTermSpectrumEfficiencyClassObsolete_Object = MibTableColumn
xfTermSpectrumEfficiencyClassObsolete = _XfTermSpectrumEfficiencyClassObsolete_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 7),
    _XfTermSpectrumEfficiencyClassObsolete_Type()
)
xfTermSpectrumEfficiencyClassObsolete.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermSpectrumEfficiencyClassObsolete.setStatus("obsolete")


class _XfTermFrameFormatType_Type(Integer32):
    """Custom type xfTermFrameFormatType based on Integer32"""
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
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("fftOther", 0),
          ("fftStatic", 1),
          ("fftAdmod", 2),
          ("fftXpic", 3),
          ("fftXpicAdmod", 4),
          ("fftLegacy", 5),
          ("fftStaticLH", 6),
          ("fftAdmodLH", 7),
          ("fftXpicLH", 8),
          ("fftXpicAdmodLH", 9),
          ("fftAdmodStatic", 10),
          ("fftXpicAdmodStatic", 11),
          ("fftAdmodStaticLH", 12),
          ("fftXpicAdmodStaticLH", 13))
    )


_XfTermFrameFormatType_Type.__name__ = "Integer32"
_XfTermFrameFormatType_Object = MibTableColumn
xfTermFrameFormatType = _XfTermFrameFormatType_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 8),
    _XfTermFrameFormatType_Type()
)
xfTermFrameFormatType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermFrameFormatType.setStatus("current")


class _XfTermFrameFormatRev_Type(Integer32):
    """Custom type xfTermFrameFormatRev based on Integer32"""
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


_XfTermFrameFormatRev_Type.__name__ = "Integer32"
_XfTermFrameFormatRev_Object = MibTableColumn
xfTermFrameFormatRev = _XfTermFrameFormatRev_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 9),
    _XfTermFrameFormatRev_Type()
)
xfTermFrameFormatRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermFrameFormatRev.setStatus("current")


class _XfTermBerAlarmThresholdCapability_Type(Bits):
    """Custom type xfTermBerAlarmThresholdCapability based on Bits"""
    namedValues = NamedValues(
        *(("berThrCap1e3", 0),
          ("berThrCap1e4", 1),
          ("berThrCap1e5", 2),
          ("berThrCap1e6", 3))
    )

_XfTermBerAlarmThresholdCapability_Type.__name__ = "Bits"
_XfTermBerAlarmThresholdCapability_Object = MibTableColumn
xfTermBerAlarmThresholdCapability = _XfTermBerAlarmThresholdCapability_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 15, 1, 10),
    _XfTermBerAlarmThresholdCapability_Type()
)
xfTermBerAlarmThresholdCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermBerAlarmThresholdCapability.setStatus("current")
_XfRLPMAMConfigTable_Object = MibTable
xfRLPMAMConfigTable = _XfRLPMAMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 16)
)
if mibBuilder.loadTexts:
    xfRLPMAMConfigTable.setStatus("current")
_XfRLPMAMConfigEntry_Object = MibTableRow
xfRLPMAMConfigEntry = _XfRLPMAMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 16, 1)
)
xfRLPMAMConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMAMConfigEntry.setStatus("current")
_XfPMAMSetThreshold15m_Type = Integer32
_XfPMAMSetThreshold15m_Object = MibTableColumn
xfPMAMSetThreshold15m = _XfPMAMSetThreshold15m_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 16, 1, 1),
    _XfPMAMSetThreshold15m_Type()
)
xfPMAMSetThreshold15m.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMAMSetThreshold15m.setStatus("current")
_XfPMAMSetThreshold24h_Type = Integer32
_XfPMAMSetThreshold24h_Object = MibTableColumn
xfPMAMSetThreshold24h = _XfPMAMSetThreshold24h_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 16, 1, 2),
    _XfPMAMSetThreshold24h_Type()
)
xfPMAMSetThreshold24h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMAMSetThreshold24h.setStatus("current")
_XfPMAMResetThreshold15m_Type = Integer32
_XfPMAMResetThreshold15m_Object = MibTableColumn
xfPMAMResetThreshold15m = _XfPMAMResetThreshold15m_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 16, 1, 3),
    _XfPMAMResetThreshold15m_Type()
)
xfPMAMResetThreshold15m.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMAMResetThreshold15m.setStatus("current")


class _XfPMAMStatus_Type(Bits):
    """Custom type xfPMAMStatus based on Bits"""
    namedValues = NamedValues(
        *(("am15m1", 0),
          ("am15m2", 1),
          ("am15m3", 2),
          ("am24h1", 3),
          ("am24h2", 4),
          ("am24h3", 5))
    )

_XfPMAMStatus_Type.__name__ = "Bits"
_XfPMAMStatus_Object = MibTableColumn
xfPMAMStatus = _XfPMAMStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 16, 1, 4),
    _XfPMAMStatus_Type()
)
xfPMAMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMStatus.setStatus("current")


class _XfPMAMValidData_Type(Bits):
    """Custom type xfPMAMValidData based on Bits"""
    namedValues = NamedValues(
        *(("valid15m4QAM", 0),
          ("valid15m8QAM", 1),
          ("valid15m16QAM", 2),
          ("valid15m32QAM", 3),
          ("valid15m64QAM", 4),
          ("valid15m128QAM", 5),
          ("valid15m256QAM", 6),
          ("valid15m512QAM", 7),
          ("valid15m1024QAM", 8))
    )

_XfPMAMValidData_Type.__name__ = "Bits"
_XfPMAMValidData_Object = MibTableColumn
xfPMAMValidData = _XfPMAMValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 16, 1, 5),
    _XfPMAMValidData_Type()
)
xfPMAMValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMValidData.setStatus("current")
_XfRLPMAMCurrent24hTable_Object = MibTable
xfRLPMAMCurrent24hTable = _XfRLPMAMCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17)
)
if mibBuilder.loadTexts:
    xfRLPMAMCurrent24hTable.setStatus("current")
_XfRLPMAMCurrent24hEntry_Object = MibTableRow
xfRLPMAMCurrent24hEntry = _XfRLPMAMCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1)
)
xfRLPMAMCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMAMCurrent24hEntry.setStatus("current")
_XfPMAMCurrent24h4QAM_Type = PerfCurrentCount
_XfPMAMCurrent24h4QAM_Object = MibTableColumn
xfPMAMCurrent24h4QAM = _XfPMAMCurrent24h4QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 1),
    _XfPMAMCurrent24h4QAM_Type()
)
xfPMAMCurrent24h4QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h4QAM.setStatus("current")
_XfPMAMCurrent24h8QAM_Type = PerfCurrentCount
_XfPMAMCurrent24h8QAM_Object = MibTableColumn
xfPMAMCurrent24h8QAM = _XfPMAMCurrent24h8QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 2),
    _XfPMAMCurrent24h8QAM_Type()
)
xfPMAMCurrent24h8QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h8QAM.setStatus("current")
_XfPMAMCurrent24h16QAM_Type = PerfCurrentCount
_XfPMAMCurrent24h16QAM_Object = MibTableColumn
xfPMAMCurrent24h16QAM = _XfPMAMCurrent24h16QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 3),
    _XfPMAMCurrent24h16QAM_Type()
)
xfPMAMCurrent24h16QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h16QAM.setStatus("current")
_XfPMAMCurrent24h32QAM_Type = PerfCurrentCount
_XfPMAMCurrent24h32QAM_Object = MibTableColumn
xfPMAMCurrent24h32QAM = _XfPMAMCurrent24h32QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 4),
    _XfPMAMCurrent24h32QAM_Type()
)
xfPMAMCurrent24h32QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h32QAM.setStatus("current")
_XfPMAMCurrent24h64QAM_Type = PerfCurrentCount
_XfPMAMCurrent24h64QAM_Object = MibTableColumn
xfPMAMCurrent24h64QAM = _XfPMAMCurrent24h64QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 5),
    _XfPMAMCurrent24h64QAM_Type()
)
xfPMAMCurrent24h64QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h64QAM.setStatus("current")
_XfPMAMCurrent24h128QAM_Type = PerfCurrentCount
_XfPMAMCurrent24h128QAM_Object = MibTableColumn
xfPMAMCurrent24h128QAM = _XfPMAMCurrent24h128QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 6),
    _XfPMAMCurrent24h128QAM_Type()
)
xfPMAMCurrent24h128QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h128QAM.setStatus("current")
_XfPMAMCurrent24h256QAM_Type = PerfCurrentCount
_XfPMAMCurrent24h256QAM_Object = MibTableColumn
xfPMAMCurrent24h256QAM = _XfPMAMCurrent24h256QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 7),
    _XfPMAMCurrent24h256QAM_Type()
)
xfPMAMCurrent24h256QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h256QAM.setStatus("current")
_XfPMAMCurrent24h512QAM_Type = PerfCurrentCount
_XfPMAMCurrent24h512QAM_Object = MibTableColumn
xfPMAMCurrent24h512QAM = _XfPMAMCurrent24h512QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 8),
    _XfPMAMCurrent24h512QAM_Type()
)
xfPMAMCurrent24h512QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h512QAM.setStatus("current")
_XfPMAMCurrent24h1024QAM_Type = PerfCurrentCount
_XfPMAMCurrent24h1024QAM_Object = MibTableColumn
xfPMAMCurrent24h1024QAM = _XfPMAMCurrent24h1024QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 9),
    _XfPMAMCurrent24h1024QAM_Type()
)
xfPMAMCurrent24h1024QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h1024QAM.setStatus("current")
_XfPMAMCurrent24h4QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent24h4QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent24h4QAMEnRLB = _XfPMAMCurrent24h4QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 10),
    _XfPMAMCurrent24h4QAMEnRLB_Type()
)
xfPMAMCurrent24h4QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h4QAMEnRLB.setStatus("current")
_XfPMAMCurrent24h8QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent24h8QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent24h8QAMEnRLB = _XfPMAMCurrent24h8QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 11),
    _XfPMAMCurrent24h8QAMEnRLB_Type()
)
xfPMAMCurrent24h8QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h8QAMEnRLB.setStatus("current")
_XfPMAMCurrent24h16QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent24h16QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent24h16QAMEnRLB = _XfPMAMCurrent24h16QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 12),
    _XfPMAMCurrent24h16QAMEnRLB_Type()
)
xfPMAMCurrent24h16QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h16QAMEnRLB.setStatus("current")
_XfPMAMCurrent24h32QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent24h32QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent24h32QAMEnRLB = _XfPMAMCurrent24h32QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 13),
    _XfPMAMCurrent24h32QAMEnRLB_Type()
)
xfPMAMCurrent24h32QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h32QAMEnRLB.setStatus("current")
_XfPMAMCurrent24h64QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent24h64QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent24h64QAMEnRLB = _XfPMAMCurrent24h64QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 14),
    _XfPMAMCurrent24h64QAMEnRLB_Type()
)
xfPMAMCurrent24h64QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h64QAMEnRLB.setStatus("current")
_XfPMAMCurrent24h128QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent24h128QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent24h128QAMEnRLB = _XfPMAMCurrent24h128QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 15),
    _XfPMAMCurrent24h128QAMEnRLB_Type()
)
xfPMAMCurrent24h128QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h128QAMEnRLB.setStatus("current")
_XfPMAMCurrent24h256QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent24h256QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent24h256QAMEnRLB = _XfPMAMCurrent24h256QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 16),
    _XfPMAMCurrent24h256QAMEnRLB_Type()
)
xfPMAMCurrent24h256QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h256QAMEnRLB.setStatus("current")
_XfPMAMCurrent24h512QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent24h512QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent24h512QAMEnRLB = _XfPMAMCurrent24h512QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 17),
    _XfPMAMCurrent24h512QAMEnRLB_Type()
)
xfPMAMCurrent24h512QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h512QAMEnRLB.setStatus("current")
_XfPMAMCurrent24h1024QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent24h1024QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent24h1024QAMEnRLB = _XfPMAMCurrent24h1024QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 17, 1, 18),
    _XfPMAMCurrent24h1024QAMEnRLB_Type()
)
xfPMAMCurrent24h1024QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent24h1024QAMEnRLB.setStatus("current")
_XfRLPMAMInterval24hTable_Object = MibTable
xfRLPMAMInterval24hTable = _XfRLPMAMInterval24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18)
)
if mibBuilder.loadTexts:
    xfRLPMAMInterval24hTable.setStatus("current")
_XfRLPMAMInterval24hEntry_Object = MibTableRow
xfRLPMAMInterval24hEntry = _XfRLPMAMInterval24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1)
)
xfRLPMAMInterval24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMAMInterval24hEntry.setStatus("current")
_XfPMAMInterval24h4QAM_Type = PerfIntervalCount
_XfPMAMInterval24h4QAM_Object = MibTableColumn
xfPMAMInterval24h4QAM = _XfPMAMInterval24h4QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 1),
    _XfPMAMInterval24h4QAM_Type()
)
xfPMAMInterval24h4QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h4QAM.setStatus("current")
_XfPMAMInterval24h8QAM_Type = PerfIntervalCount
_XfPMAMInterval24h8QAM_Object = MibTableColumn
xfPMAMInterval24h8QAM = _XfPMAMInterval24h8QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 2),
    _XfPMAMInterval24h8QAM_Type()
)
xfPMAMInterval24h8QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h8QAM.setStatus("current")
_XfPMAMInterval24h16QAM_Type = PerfIntervalCount
_XfPMAMInterval24h16QAM_Object = MibTableColumn
xfPMAMInterval24h16QAM = _XfPMAMInterval24h16QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 3),
    _XfPMAMInterval24h16QAM_Type()
)
xfPMAMInterval24h16QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h16QAM.setStatus("current")
_XfPMAMInterval24h32QAM_Type = PerfIntervalCount
_XfPMAMInterval24h32QAM_Object = MibTableColumn
xfPMAMInterval24h32QAM = _XfPMAMInterval24h32QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 4),
    _XfPMAMInterval24h32QAM_Type()
)
xfPMAMInterval24h32QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h32QAM.setStatus("current")
_XfPMAMInterval24h64QAM_Type = PerfIntervalCount
_XfPMAMInterval24h64QAM_Object = MibTableColumn
xfPMAMInterval24h64QAM = _XfPMAMInterval24h64QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 5),
    _XfPMAMInterval24h64QAM_Type()
)
xfPMAMInterval24h64QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h64QAM.setStatus("current")
_XfPMAMInterval24h128QAM_Type = PerfIntervalCount
_XfPMAMInterval24h128QAM_Object = MibTableColumn
xfPMAMInterval24h128QAM = _XfPMAMInterval24h128QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 6),
    _XfPMAMInterval24h128QAM_Type()
)
xfPMAMInterval24h128QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h128QAM.setStatus("current")
_XfPMAMInterval24h256QAM_Type = PerfIntervalCount
_XfPMAMInterval24h256QAM_Object = MibTableColumn
xfPMAMInterval24h256QAM = _XfPMAMInterval24h256QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 7),
    _XfPMAMInterval24h256QAM_Type()
)
xfPMAMInterval24h256QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h256QAM.setStatus("current")
_XfPMAMInterval24h512QAM_Type = PerfIntervalCount
_XfPMAMInterval24h512QAM_Object = MibTableColumn
xfPMAMInterval24h512QAM = _XfPMAMInterval24h512QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 8),
    _XfPMAMInterval24h512QAM_Type()
)
xfPMAMInterval24h512QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h512QAM.setStatus("current")
_XfPMAMInterval24hValidData_Type = TruthValue
_XfPMAMInterval24hValidData_Object = MibTableColumn
xfPMAMInterval24hValidData = _XfPMAMInterval24hValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 9),
    _XfPMAMInterval24hValidData_Type()
)
xfPMAMInterval24hValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24hValidData.setStatus("current")
_XfPMAMInterval24h1024QAM_Type = PerfIntervalCount
_XfPMAMInterval24h1024QAM_Object = MibTableColumn
xfPMAMInterval24h1024QAM = _XfPMAMInterval24h1024QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 10),
    _XfPMAMInterval24h1024QAM_Type()
)
xfPMAMInterval24h1024QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h1024QAM.setStatus("current")
_XfPMAMInterval24h4QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval24h4QAMEnRLB_Object = MibTableColumn
xfPMAMInterval24h4QAMEnRLB = _XfPMAMInterval24h4QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 11),
    _XfPMAMInterval24h4QAMEnRLB_Type()
)
xfPMAMInterval24h4QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h4QAMEnRLB.setStatus("current")
_XfPMAMInterval24h8QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval24h8QAMEnRLB_Object = MibTableColumn
xfPMAMInterval24h8QAMEnRLB = _XfPMAMInterval24h8QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 12),
    _XfPMAMInterval24h8QAMEnRLB_Type()
)
xfPMAMInterval24h8QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h8QAMEnRLB.setStatus("current")
_XfPMAMInterval24h16QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval24h16QAMEnRLB_Object = MibTableColumn
xfPMAMInterval24h16QAMEnRLB = _XfPMAMInterval24h16QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 13),
    _XfPMAMInterval24h16QAMEnRLB_Type()
)
xfPMAMInterval24h16QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h16QAMEnRLB.setStatus("current")
_XfPMAMInterval24h32QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval24h32QAMEnRLB_Object = MibTableColumn
xfPMAMInterval24h32QAMEnRLB = _XfPMAMInterval24h32QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 14),
    _XfPMAMInterval24h32QAMEnRLB_Type()
)
xfPMAMInterval24h32QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h32QAMEnRLB.setStatus("current")
_XfPMAMInterval24h64QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval24h64QAMEnRLB_Object = MibTableColumn
xfPMAMInterval24h64QAMEnRLB = _XfPMAMInterval24h64QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 15),
    _XfPMAMInterval24h64QAMEnRLB_Type()
)
xfPMAMInterval24h64QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h64QAMEnRLB.setStatus("current")
_XfPMAMInterval24h128QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval24h128QAMEnRLB_Object = MibTableColumn
xfPMAMInterval24h128QAMEnRLB = _XfPMAMInterval24h128QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 16),
    _XfPMAMInterval24h128QAMEnRLB_Type()
)
xfPMAMInterval24h128QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h128QAMEnRLB.setStatus("current")
_XfPMAMInterval24h256QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval24h256QAMEnRLB_Object = MibTableColumn
xfPMAMInterval24h256QAMEnRLB = _XfPMAMInterval24h256QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 17),
    _XfPMAMInterval24h256QAMEnRLB_Type()
)
xfPMAMInterval24h256QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h256QAMEnRLB.setStatus("current")
_XfPMAMInterval24h512QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval24h512QAMEnRLB_Object = MibTableColumn
xfPMAMInterval24h512QAMEnRLB = _XfPMAMInterval24h512QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 18),
    _XfPMAMInterval24h512QAMEnRLB_Type()
)
xfPMAMInterval24h512QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h512QAMEnRLB.setStatus("current")
_XfPMAMInterval24h1024QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval24h1024QAMEnRLB_Object = MibTableColumn
xfPMAMInterval24h1024QAMEnRLB = _XfPMAMInterval24h1024QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 18, 1, 19),
    _XfPMAMInterval24h1024QAMEnRLB_Type()
)
xfPMAMInterval24h1024QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval24h1024QAMEnRLB.setStatus("current")
_XfRLPMAMCurrent15mTable_Object = MibTable
xfRLPMAMCurrent15mTable = _XfRLPMAMCurrent15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19)
)
if mibBuilder.loadTexts:
    xfRLPMAMCurrent15mTable.setStatus("current")
_XfRLPMAMCurrent15mEntry_Object = MibTableRow
xfRLPMAMCurrent15mEntry = _XfRLPMAMCurrent15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1)
)
xfRLPMAMCurrent15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMAMCurrent15mEntry.setStatus("current")
_XfPMAMCurrent15m4QAM_Type = PerfCurrentCount
_XfPMAMCurrent15m4QAM_Object = MibTableColumn
xfPMAMCurrent15m4QAM = _XfPMAMCurrent15m4QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 1),
    _XfPMAMCurrent15m4QAM_Type()
)
xfPMAMCurrent15m4QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m4QAM.setStatus("current")
_XfPMAMCurrent15m8QAM_Type = PerfCurrentCount
_XfPMAMCurrent15m8QAM_Object = MibTableColumn
xfPMAMCurrent15m8QAM = _XfPMAMCurrent15m8QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 2),
    _XfPMAMCurrent15m8QAM_Type()
)
xfPMAMCurrent15m8QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m8QAM.setStatus("current")
_XfPMAMCurrent15m16QAM_Type = PerfCurrentCount
_XfPMAMCurrent15m16QAM_Object = MibTableColumn
xfPMAMCurrent15m16QAM = _XfPMAMCurrent15m16QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 3),
    _XfPMAMCurrent15m16QAM_Type()
)
xfPMAMCurrent15m16QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m16QAM.setStatus("current")
_XfPMAMCurrent15m32QAM_Type = PerfCurrentCount
_XfPMAMCurrent15m32QAM_Object = MibTableColumn
xfPMAMCurrent15m32QAM = _XfPMAMCurrent15m32QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 4),
    _XfPMAMCurrent15m32QAM_Type()
)
xfPMAMCurrent15m32QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m32QAM.setStatus("current")
_XfPMAMCurrent15m64QAM_Type = PerfCurrentCount
_XfPMAMCurrent15m64QAM_Object = MibTableColumn
xfPMAMCurrent15m64QAM = _XfPMAMCurrent15m64QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 5),
    _XfPMAMCurrent15m64QAM_Type()
)
xfPMAMCurrent15m64QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m64QAM.setStatus("current")
_XfPMAMCurrent15m128QAM_Type = PerfCurrentCount
_XfPMAMCurrent15m128QAM_Object = MibTableColumn
xfPMAMCurrent15m128QAM = _XfPMAMCurrent15m128QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 6),
    _XfPMAMCurrent15m128QAM_Type()
)
xfPMAMCurrent15m128QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m128QAM.setStatus("current")
_XfPMAMCurrent15m256QAM_Type = PerfCurrentCount
_XfPMAMCurrent15m256QAM_Object = MibTableColumn
xfPMAMCurrent15m256QAM = _XfPMAMCurrent15m256QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 7),
    _XfPMAMCurrent15m256QAM_Type()
)
xfPMAMCurrent15m256QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m256QAM.setStatus("current")
_XfPMAMCurrent15m512QAM_Type = PerfCurrentCount
_XfPMAMCurrent15m512QAM_Object = MibTableColumn
xfPMAMCurrent15m512QAM = _XfPMAMCurrent15m512QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 8),
    _XfPMAMCurrent15m512QAM_Type()
)
xfPMAMCurrent15m512QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m512QAM.setStatus("current")
_XfPMAMCurrent15m1024QAM_Type = PerfCurrentCount
_XfPMAMCurrent15m1024QAM_Object = MibTableColumn
xfPMAMCurrent15m1024QAM = _XfPMAMCurrent15m1024QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 9),
    _XfPMAMCurrent15m1024QAM_Type()
)
xfPMAMCurrent15m1024QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m1024QAM.setStatus("current")
_XfPMAMCurrent15m4QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent15m4QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent15m4QAMEnRLB = _XfPMAMCurrent15m4QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 10),
    _XfPMAMCurrent15m4QAMEnRLB_Type()
)
xfPMAMCurrent15m4QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m4QAMEnRLB.setStatus("current")
_XfPMAMCurrent15m8QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent15m8QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent15m8QAMEnRLB = _XfPMAMCurrent15m8QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 11),
    _XfPMAMCurrent15m8QAMEnRLB_Type()
)
xfPMAMCurrent15m8QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m8QAMEnRLB.setStatus("current")
_XfPMAMCurrent15m16QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent15m16QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent15m16QAMEnRLB = _XfPMAMCurrent15m16QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 12),
    _XfPMAMCurrent15m16QAMEnRLB_Type()
)
xfPMAMCurrent15m16QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m16QAMEnRLB.setStatus("current")
_XfPMAMCurrent15m32QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent15m32QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent15m32QAMEnRLB = _XfPMAMCurrent15m32QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 13),
    _XfPMAMCurrent15m32QAMEnRLB_Type()
)
xfPMAMCurrent15m32QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m32QAMEnRLB.setStatus("current")
_XfPMAMCurrent15m64QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent15m64QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent15m64QAMEnRLB = _XfPMAMCurrent15m64QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 14),
    _XfPMAMCurrent15m64QAMEnRLB_Type()
)
xfPMAMCurrent15m64QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m64QAMEnRLB.setStatus("current")
_XfPMAMCurrent15m128QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent15m128QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent15m128QAMEnRLB = _XfPMAMCurrent15m128QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 15),
    _XfPMAMCurrent15m128QAMEnRLB_Type()
)
xfPMAMCurrent15m128QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m128QAMEnRLB.setStatus("current")
_XfPMAMCurrent15m256QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent15m256QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent15m256QAMEnRLB = _XfPMAMCurrent15m256QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 16),
    _XfPMAMCurrent15m256QAMEnRLB_Type()
)
xfPMAMCurrent15m256QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m256QAMEnRLB.setStatus("current")
_XfPMAMCurrent15m512QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent15m512QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent15m512QAMEnRLB = _XfPMAMCurrent15m512QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 17),
    _XfPMAMCurrent15m512QAMEnRLB_Type()
)
xfPMAMCurrent15m512QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m512QAMEnRLB.setStatus("current")
_XfPMAMCurrent15m1024QAMEnRLB_Type = PerfCurrentCount
_XfPMAMCurrent15m1024QAMEnRLB_Object = MibTableColumn
xfPMAMCurrent15m1024QAMEnRLB = _XfPMAMCurrent15m1024QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 19, 1, 18),
    _XfPMAMCurrent15m1024QAMEnRLB_Type()
)
xfPMAMCurrent15m1024QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMCurrent15m1024QAMEnRLB.setStatus("current")
_XfRLPMAMInterval15mTable_Object = MibTable
xfRLPMAMInterval15mTable = _XfRLPMAMInterval15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20)
)
if mibBuilder.loadTexts:
    xfRLPMAMInterval15mTable.setStatus("current")
_XfRLPMAMInterval15mEntry_Object = MibTableRow
xfRLPMAMInterval15mEntry = _XfRLPMAMInterval15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1)
)
xfRLPMAMInterval15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15mIntervalNumber"),
)
if mibBuilder.loadTexts:
    xfRLPMAMInterval15mEntry.setStatus("current")


class _XfPMAMInterval15mIntervalNumber_Type(Integer32):
    """Custom type xfPMAMInterval15mIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_XfPMAMInterval15mIntervalNumber_Type.__name__ = "Integer32"
_XfPMAMInterval15mIntervalNumber_Object = MibTableColumn
xfPMAMInterval15mIntervalNumber = _XfPMAMInterval15mIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 1),
    _XfPMAMInterval15mIntervalNumber_Type()
)
xfPMAMInterval15mIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15mIntervalNumber.setStatus("current")
_XfPMAMInterval15m4QAM_Type = PerfIntervalCount
_XfPMAMInterval15m4QAM_Object = MibTableColumn
xfPMAMInterval15m4QAM = _XfPMAMInterval15m4QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 2),
    _XfPMAMInterval15m4QAM_Type()
)
xfPMAMInterval15m4QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m4QAM.setStatus("current")
_XfPMAMInterval15m8QAM_Type = PerfIntervalCount
_XfPMAMInterval15m8QAM_Object = MibTableColumn
xfPMAMInterval15m8QAM = _XfPMAMInterval15m8QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 3),
    _XfPMAMInterval15m8QAM_Type()
)
xfPMAMInterval15m8QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m8QAM.setStatus("current")
_XfPMAMInterval15m16QAM_Type = PerfIntervalCount
_XfPMAMInterval15m16QAM_Object = MibTableColumn
xfPMAMInterval15m16QAM = _XfPMAMInterval15m16QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 4),
    _XfPMAMInterval15m16QAM_Type()
)
xfPMAMInterval15m16QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m16QAM.setStatus("current")
_XfPMAMInterval15m32QAM_Type = PerfIntervalCount
_XfPMAMInterval15m32QAM_Object = MibTableColumn
xfPMAMInterval15m32QAM = _XfPMAMInterval15m32QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 5),
    _XfPMAMInterval15m32QAM_Type()
)
xfPMAMInterval15m32QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m32QAM.setStatus("current")
_XfPMAMInterval15m64QAM_Type = PerfIntervalCount
_XfPMAMInterval15m64QAM_Object = MibTableColumn
xfPMAMInterval15m64QAM = _XfPMAMInterval15m64QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 6),
    _XfPMAMInterval15m64QAM_Type()
)
xfPMAMInterval15m64QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m64QAM.setStatus("current")
_XfPMAMInterval15m128QAM_Type = PerfIntervalCount
_XfPMAMInterval15m128QAM_Object = MibTableColumn
xfPMAMInterval15m128QAM = _XfPMAMInterval15m128QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 7),
    _XfPMAMInterval15m128QAM_Type()
)
xfPMAMInterval15m128QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m128QAM.setStatus("current")
_XfPMAMInterval15m256QAM_Type = PerfIntervalCount
_XfPMAMInterval15m256QAM_Object = MibTableColumn
xfPMAMInterval15m256QAM = _XfPMAMInterval15m256QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 8),
    _XfPMAMInterval15m256QAM_Type()
)
xfPMAMInterval15m256QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m256QAM.setStatus("current")
_XfPMAMInterval15m512QAM_Type = PerfIntervalCount
_XfPMAMInterval15m512QAM_Object = MibTableColumn
xfPMAMInterval15m512QAM = _XfPMAMInterval15m512QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 9),
    _XfPMAMInterval15m512QAM_Type()
)
xfPMAMInterval15m512QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m512QAM.setStatus("current")
_XfPMAMInterval15mValidData_Type = TruthValue
_XfPMAMInterval15mValidData_Object = MibTableColumn
xfPMAMInterval15mValidData = _XfPMAMInterval15mValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 10),
    _XfPMAMInterval15mValidData_Type()
)
xfPMAMInterval15mValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15mValidData.setStatus("current")
_XfPMAMInterval15m1024QAM_Type = PerfIntervalCount
_XfPMAMInterval15m1024QAM_Object = MibTableColumn
xfPMAMInterval15m1024QAM = _XfPMAMInterval15m1024QAM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 11),
    _XfPMAMInterval15m1024QAM_Type()
)
xfPMAMInterval15m1024QAM.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m1024QAM.setStatus("current")
_XfPMAMInterval15m4QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval15m4QAMEnRLB_Object = MibTableColumn
xfPMAMInterval15m4QAMEnRLB = _XfPMAMInterval15m4QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 12),
    _XfPMAMInterval15m4QAMEnRLB_Type()
)
xfPMAMInterval15m4QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m4QAMEnRLB.setStatus("current")
_XfPMAMInterval15m8QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval15m8QAMEnRLB_Object = MibTableColumn
xfPMAMInterval15m8QAMEnRLB = _XfPMAMInterval15m8QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 13),
    _XfPMAMInterval15m8QAMEnRLB_Type()
)
xfPMAMInterval15m8QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m8QAMEnRLB.setStatus("current")
_XfPMAMInterval15m16QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval15m16QAMEnRLB_Object = MibTableColumn
xfPMAMInterval15m16QAMEnRLB = _XfPMAMInterval15m16QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 14),
    _XfPMAMInterval15m16QAMEnRLB_Type()
)
xfPMAMInterval15m16QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m16QAMEnRLB.setStatus("current")
_XfPMAMInterval15m32QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval15m32QAMEnRLB_Object = MibTableColumn
xfPMAMInterval15m32QAMEnRLB = _XfPMAMInterval15m32QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 15),
    _XfPMAMInterval15m32QAMEnRLB_Type()
)
xfPMAMInterval15m32QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m32QAMEnRLB.setStatus("current")
_XfPMAMInterval15m64QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval15m64QAMEnRLB_Object = MibTableColumn
xfPMAMInterval15m64QAMEnRLB = _XfPMAMInterval15m64QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 16),
    _XfPMAMInterval15m64QAMEnRLB_Type()
)
xfPMAMInterval15m64QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m64QAMEnRLB.setStatus("current")
_XfPMAMInterval15m128QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval15m128QAMEnRLB_Object = MibTableColumn
xfPMAMInterval15m128QAMEnRLB = _XfPMAMInterval15m128QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 17),
    _XfPMAMInterval15m128QAMEnRLB_Type()
)
xfPMAMInterval15m128QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m128QAMEnRLB.setStatus("current")
_XfPMAMInterval15m256QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval15m256QAMEnRLB_Object = MibTableColumn
xfPMAMInterval15m256QAMEnRLB = _XfPMAMInterval15m256QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 18),
    _XfPMAMInterval15m256QAMEnRLB_Type()
)
xfPMAMInterval15m256QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m256QAMEnRLB.setStatus("current")
_XfPMAMInterval15m512QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval15m512QAMEnRLB_Object = MibTableColumn
xfPMAMInterval15m512QAMEnRLB = _XfPMAMInterval15m512QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 19),
    _XfPMAMInterval15m512QAMEnRLB_Type()
)
xfPMAMInterval15m512QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m512QAMEnRLB.setStatus("current")
_XfPMAMInterval15m1024QAMEnRLB_Type = PerfIntervalCount
_XfPMAMInterval15m1024QAMEnRLB_Object = MibTableColumn
xfPMAMInterval15m1024QAMEnRLB = _XfPMAMInterval15m1024QAMEnRLB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 20, 1, 20),
    _XfPMAMInterval15m1024QAMEnRLB_Type()
)
xfPMAMInterval15m1024QAMEnRLB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMAMInterval15m1024QAMEnRLB.setStatus("current")
_XfRLPtpTerminalCapacityLicenseTable_Object = MibTable
xfRLPtpTerminalCapacityLicenseTable = _XfRLPtpTerminalCapacityLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 21)
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalCapacityLicenseTable.setStatus("current")
_XfRLPtpTerminalCapacityLicenseEntry_Object = MibTableRow
xfRLPtpTerminalCapacityLicenseEntry = _XfRLPtpTerminalCapacityLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 21, 1)
)
xfRLPtpTerminalCapacityLicenseEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLogicalIndex"),
    (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRowIndex"),
)
if mibBuilder.loadTexts:
    xfRLPtpTerminalCapacityLicenseEntry.setStatus("current")


class _XfTermCapacityLicenseRange_Type(Integer32):
    """Custom type xfTermCapacityLicenseRange based on Integer32"""
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
        *(("vr0", 0),
          ("vr10", 1),
          ("vr25", 2),
          ("vr50", 3),
          ("vr100", 4),
          ("vr15", 5),
          ("vr30", 6),
          ("vr60", 7),
          ("vr125", 8),
          ("vr200", 9),
          ("vr350", 10),
          ("vr4", 11),
          ("vr500", 12),
          ("vr150", 13),
          ("vr250", 14),
          ("vr300", 15),
          ("vr400", 16),
          ("vr450", 17))
    )


_XfTermCapacityLicenseRange_Type.__name__ = "Integer32"
_XfTermCapacityLicenseRange_Object = MibTableColumn
xfTermCapacityLicenseRange = _XfTermCapacityLicenseRange_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 21, 1, 1),
    _XfTermCapacityLicenseRange_Type()
)
xfTermCapacityLicenseRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermCapacityLicenseRange.setStatus("current")
_XfTermMaxCapacityRange_Type = Integer32
_XfTermMaxCapacityRange_Object = MibTableColumn
xfTermMaxCapacityRange = _XfTermMaxCapacityRange_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 21, 1, 2),
    _XfTermMaxCapacityRange_Type()
)
xfTermMaxCapacityRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermMaxCapacityRange.setStatus("current")
_XfTermMaxTribCapacityRange_Type = Integer32
_XfTermMaxTribCapacityRange_Object = MibTableColumn
xfTermMaxTribCapacityRange = _XfTermMaxTribCapacityRange_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 21, 1, 3),
    _XfTermMaxTribCapacityRange_Type()
)
xfTermMaxTribCapacityRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfTermMaxTribCapacityRange.setStatus("current")
_XfRLPMSDCGainCurrent15mTable_Object = MibTable
xfRLPMSDCGainCurrent15mTable = _XfRLPMSDCGainCurrent15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 22)
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainCurrent15mTable.setStatus("current")
_XfRLPMSDCGainCurrent15mEntry_Object = MibTableRow
xfRLPMSDCGainCurrent15mEntry = _XfRLPMSDCGainCurrent15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 22, 1)
)
xfRLPMSDCGainCurrent15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainCurrent15mEntry.setStatus("current")
_XfPMSDCGainCurrent15m0005dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent15m0005dB_Object = MibTableColumn
xfPMSDCGainCurrent15m0005dB = _XfPMSDCGainCurrent15m0005dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 22, 1, 1),
    _XfPMSDCGainCurrent15m0005dB_Type()
)
xfPMSDCGainCurrent15m0005dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent15m0005dB.setStatus("current")
_XfPMSDCGainCurrent15m0510dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent15m0510dB_Object = MibTableColumn
xfPMSDCGainCurrent15m0510dB = _XfPMSDCGainCurrent15m0510dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 22, 1, 2),
    _XfPMSDCGainCurrent15m0510dB_Type()
)
xfPMSDCGainCurrent15m0510dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent15m0510dB.setStatus("current")
_XfPMSDCGainCurrent15m1015dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent15m1015dB_Object = MibTableColumn
xfPMSDCGainCurrent15m1015dB = _XfPMSDCGainCurrent15m1015dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 22, 1, 3),
    _XfPMSDCGainCurrent15m1015dB_Type()
)
xfPMSDCGainCurrent15m1015dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent15m1015dB.setStatus("current")
_XfPMSDCGainCurrent15m1520dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent15m1520dB_Object = MibTableColumn
xfPMSDCGainCurrent15m1520dB = _XfPMSDCGainCurrent15m1520dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 22, 1, 4),
    _XfPMSDCGainCurrent15m1520dB_Type()
)
xfPMSDCGainCurrent15m1520dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent15m1520dB.setStatus("current")
_XfPMSDCGainCurrent15m2025dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent15m2025dB_Object = MibTableColumn
xfPMSDCGainCurrent15m2025dB = _XfPMSDCGainCurrent15m2025dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 22, 1, 5),
    _XfPMSDCGainCurrent15m2025dB_Type()
)
xfPMSDCGainCurrent15m2025dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent15m2025dB.setStatus("current")
_XfPMSDCGainCurrent15m2530dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent15m2530dB_Object = MibTableColumn
xfPMSDCGainCurrent15m2530dB = _XfPMSDCGainCurrent15m2530dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 22, 1, 6),
    _XfPMSDCGainCurrent15m2530dB_Type()
)
xfPMSDCGainCurrent15m2530dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent15m2530dB.setStatus("current")
_XfRLPMSDCGainInterval15mTable_Object = MibTable
xfRLPMSDCGainInterval15mTable = _XfRLPMSDCGainInterval15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 23)
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainInterval15mTable.setStatus("current")
_XfRLPMSDCGainInterval15mEntry_Object = MibTableRow
xfRLPMSDCGainInterval15mEntry = _XfRLPMSDCGainInterval15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 23, 1)
)
xfRLPMSDCGainInterval15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval15mIntervalNumber"),
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainInterval15mEntry.setStatus("current")


class _XfPMSDCGainInterval15mIntervalNumber_Type(Integer32):
    """Custom type xfPMSDCGainInterval15mIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_XfPMSDCGainInterval15mIntervalNumber_Type.__name__ = "Integer32"
_XfPMSDCGainInterval15mIntervalNumber_Object = MibTableColumn
xfPMSDCGainInterval15mIntervalNumber = _XfPMSDCGainInterval15mIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 23, 1, 1),
    _XfPMSDCGainInterval15mIntervalNumber_Type()
)
xfPMSDCGainInterval15mIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval15mIntervalNumber.setStatus("current")
_XfPMSDCGainInterval15m0005dB_Type = PerfIntervalCount
_XfPMSDCGainInterval15m0005dB_Object = MibTableColumn
xfPMSDCGainInterval15m0005dB = _XfPMSDCGainInterval15m0005dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 23, 1, 2),
    _XfPMSDCGainInterval15m0005dB_Type()
)
xfPMSDCGainInterval15m0005dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval15m0005dB.setStatus("current")
_XfPMSDCGainInterval15m0510dB_Type = PerfIntervalCount
_XfPMSDCGainInterval15m0510dB_Object = MibTableColumn
xfPMSDCGainInterval15m0510dB = _XfPMSDCGainInterval15m0510dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 23, 1, 3),
    _XfPMSDCGainInterval15m0510dB_Type()
)
xfPMSDCGainInterval15m0510dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval15m0510dB.setStatus("current")
_XfPMSDCGainInterval15m1015dB_Type = PerfIntervalCount
_XfPMSDCGainInterval15m1015dB_Object = MibTableColumn
xfPMSDCGainInterval15m1015dB = _XfPMSDCGainInterval15m1015dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 23, 1, 4),
    _XfPMSDCGainInterval15m1015dB_Type()
)
xfPMSDCGainInterval15m1015dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval15m1015dB.setStatus("current")
_XfPMSDCGainInterval15m1520dB_Type = PerfIntervalCount
_XfPMSDCGainInterval15m1520dB_Object = MibTableColumn
xfPMSDCGainInterval15m1520dB = _XfPMSDCGainInterval15m1520dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 23, 1, 5),
    _XfPMSDCGainInterval15m1520dB_Type()
)
xfPMSDCGainInterval15m1520dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval15m1520dB.setStatus("current")
_XfPMSDCGainInterval15m2025dB_Type = PerfIntervalCount
_XfPMSDCGainInterval15m2025dB_Object = MibTableColumn
xfPMSDCGainInterval15m2025dB = _XfPMSDCGainInterval15m2025dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 23, 1, 6),
    _XfPMSDCGainInterval15m2025dB_Type()
)
xfPMSDCGainInterval15m2025dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval15m2025dB.setStatus("current")
_XfPMSDCGainInterval15m2530dB_Type = PerfIntervalCount
_XfPMSDCGainInterval15m2530dB_Object = MibTableColumn
xfPMSDCGainInterval15m2530dB = _XfPMSDCGainInterval15m2530dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 23, 1, 7),
    _XfPMSDCGainInterval15m2530dB_Type()
)
xfPMSDCGainInterval15m2530dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval15m2530dB.setStatus("current")
_XfRLPMSDCGainCurrent24hTable_Object = MibTable
xfRLPMSDCGainCurrent24hTable = _XfRLPMSDCGainCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 24)
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainCurrent24hTable.setStatus("current")
_XfRLPMSDCGainCurrent24hEntry_Object = MibTableRow
xfRLPMSDCGainCurrent24hEntry = _XfRLPMSDCGainCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 24, 1)
)
xfRLPMSDCGainCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainCurrent24hEntry.setStatus("current")
_XfPMSDCGainCurrent24h0005dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent24h0005dB_Object = MibTableColumn
xfPMSDCGainCurrent24h0005dB = _XfPMSDCGainCurrent24h0005dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 24, 1, 1),
    _XfPMSDCGainCurrent24h0005dB_Type()
)
xfPMSDCGainCurrent24h0005dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent24h0005dB.setStatus("current")
_XfPMSDCGainCurrent24h0510dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent24h0510dB_Object = MibTableColumn
xfPMSDCGainCurrent24h0510dB = _XfPMSDCGainCurrent24h0510dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 24, 1, 2),
    _XfPMSDCGainCurrent24h0510dB_Type()
)
xfPMSDCGainCurrent24h0510dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent24h0510dB.setStatus("current")
_XfPMSDCGainCurrent24h1015dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent24h1015dB_Object = MibTableColumn
xfPMSDCGainCurrent24h1015dB = _XfPMSDCGainCurrent24h1015dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 24, 1, 3),
    _XfPMSDCGainCurrent24h1015dB_Type()
)
xfPMSDCGainCurrent24h1015dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent24h1015dB.setStatus("current")
_XfPMSDCGainCurrent24h1520dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent24h1520dB_Object = MibTableColumn
xfPMSDCGainCurrent24h1520dB = _XfPMSDCGainCurrent24h1520dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 24, 1, 4),
    _XfPMSDCGainCurrent24h1520dB_Type()
)
xfPMSDCGainCurrent24h1520dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent24h1520dB.setStatus("current")
_XfPMSDCGainCurrent24h2025dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent24h2025dB_Object = MibTableColumn
xfPMSDCGainCurrent24h2025dB = _XfPMSDCGainCurrent24h2025dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 24, 1, 5),
    _XfPMSDCGainCurrent24h2025dB_Type()
)
xfPMSDCGainCurrent24h2025dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent24h2025dB.setStatus("current")
_XfPMSDCGainCurrent24h2530dB_Type = PerfCurrentCount
_XfPMSDCGainCurrent24h2530dB_Object = MibTableColumn
xfPMSDCGainCurrent24h2530dB = _XfPMSDCGainCurrent24h2530dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 24, 1, 6),
    _XfPMSDCGainCurrent24h2530dB_Type()
)
xfPMSDCGainCurrent24h2530dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainCurrent24h2530dB.setStatus("current")
_XfRLPMSDCGainInterval24hTable_Object = MibTable
xfRLPMSDCGainInterval24hTable = _XfRLPMSDCGainInterval24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 25)
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainInterval24hTable.setStatus("current")
_XfRLPMSDCGainInterval24hEntry_Object = MibTableRow
xfRLPMSDCGainInterval24hEntry = _XfRLPMSDCGainInterval24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 25, 1)
)
xfRLPMSDCGainInterval24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainInterval24hEntry.setStatus("current")
_XfPMSDCGainInterval24h0005dB_Type = PerfIntervalCount
_XfPMSDCGainInterval24h0005dB_Object = MibTableColumn
xfPMSDCGainInterval24h0005dB = _XfPMSDCGainInterval24h0005dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 25, 1, 1),
    _XfPMSDCGainInterval24h0005dB_Type()
)
xfPMSDCGainInterval24h0005dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval24h0005dB.setStatus("current")
_XfPMSDCGainInterval24h0510dB_Type = PerfIntervalCount
_XfPMSDCGainInterval24h0510dB_Object = MibTableColumn
xfPMSDCGainInterval24h0510dB = _XfPMSDCGainInterval24h0510dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 25, 1, 2),
    _XfPMSDCGainInterval24h0510dB_Type()
)
xfPMSDCGainInterval24h0510dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval24h0510dB.setStatus("current")
_XfPMSDCGainInterval24h1015dB_Type = PerfIntervalCount
_XfPMSDCGainInterval24h1015dB_Object = MibTableColumn
xfPMSDCGainInterval24h1015dB = _XfPMSDCGainInterval24h1015dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 25, 1, 3),
    _XfPMSDCGainInterval24h1015dB_Type()
)
xfPMSDCGainInterval24h1015dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval24h1015dB.setStatus("current")
_XfPMSDCGainInterval24h1520dB_Type = PerfIntervalCount
_XfPMSDCGainInterval24h1520dB_Object = MibTableColumn
xfPMSDCGainInterval24h1520dB = _XfPMSDCGainInterval24h1520dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 25, 1, 4),
    _XfPMSDCGainInterval24h1520dB_Type()
)
xfPMSDCGainInterval24h1520dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval24h1520dB.setStatus("current")
_XfPMSDCGainInterval24h2025dB_Type = PerfIntervalCount
_XfPMSDCGainInterval24h2025dB_Object = MibTableColumn
xfPMSDCGainInterval24h2025dB = _XfPMSDCGainInterval24h2025dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 25, 1, 5),
    _XfPMSDCGainInterval24h2025dB_Type()
)
xfPMSDCGainInterval24h2025dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval24h2025dB.setStatus("current")
_XfPMSDCGainInterval24h2530dB_Type = PerfIntervalCount
_XfPMSDCGainInterval24h2530dB_Object = MibTableColumn
xfPMSDCGainInterval24h2530dB = _XfPMSDCGainInterval24h2530dB_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 25, 1, 6),
    _XfPMSDCGainInterval24h2530dB_Type()
)
xfPMSDCGainInterval24h2530dB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainInterval24h2530dB.setStatus("current")
_XfRLPMSDCGainConfigTable_Object = MibTable
xfRLPMSDCGainConfigTable = _XfRLPMSDCGainConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 26)
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainConfigTable.setStatus("current")
_XfRLPMSDCGainConfigEntry_Object = MibTableRow
xfRLPMSDCGainConfigEntry = _XfRLPMSDCGainConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 26, 1)
)
xfRLPMSDCGainConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLPMSDCGainConfigEntry.setStatus("current")
_XfPMSDCGainSetThreshold15m_Type = Integer32
_XfPMSDCGainSetThreshold15m_Object = MibTableColumn
xfPMSDCGainSetThreshold15m = _XfPMSDCGainSetThreshold15m_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 26, 1, 1),
    _XfPMSDCGainSetThreshold15m_Type()
)
xfPMSDCGainSetThreshold15m.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSDCGainSetThreshold15m.setStatus("current")
_XfPMSDCGainSetThreshold24h_Type = Integer32
_XfPMSDCGainSetThreshold24h_Object = MibTableColumn
xfPMSDCGainSetThreshold24h = _XfPMSDCGainSetThreshold24h_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 26, 1, 2),
    _XfPMSDCGainSetThreshold24h_Type()
)
xfPMSDCGainSetThreshold24h.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSDCGainSetThreshold24h.setStatus("current")
_XfPMSDCGainResetThreshold15m_Type = Integer32
_XfPMSDCGainResetThreshold15m_Object = MibTableColumn
xfPMSDCGainResetThreshold15m = _XfPMSDCGainResetThreshold15m_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 26, 1, 3),
    _XfPMSDCGainResetThreshold15m_Type()
)
xfPMSDCGainResetThreshold15m.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfPMSDCGainResetThreshold15m.setStatus("current")


class _XfPMSDCGainStatus_Type(Bits):
    """Custom type xfPMSDCGainStatus based on Bits"""
    namedValues = NamedValues(
        *(("sdcGain15m", 0),
          ("sdcGain24h", 1))
    )

_XfPMSDCGainStatus_Type.__name__ = "Bits"
_XfPMSDCGainStatus_Object = MibTableColumn
xfPMSDCGainStatus = _XfPMSDCGainStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 26, 1, 4),
    _XfPMSDCGainStatus_Type()
)
xfPMSDCGainStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfPMSDCGainStatus.setStatus("current")
_XfRLExtRFPMConfigTable_Object = MibTable
xfRLExtRFPMConfigTable = _XfRLExtRFPMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27)
)
if mibBuilder.loadTexts:
    xfRLExtRFPMConfigTable.setStatus("current")
_XfRLExtRFPMConfigEntry_Object = MibTableRow
xfRLExtRFPMConfigEntry = _XfRLExtRFPMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1)
)
xfRLExtRFPMConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLExtRFPMConfigEntry.setStatus("current")


class _XfExtRFPMRLTS1Threshold_Type(Integer32):
    """Custom type xfExtRFPMRLTS1Threshold based on Integer32"""
    defaultValue = -999

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -201),
    )


_XfExtRFPMRLTS1Threshold_Type.__name__ = "Integer32"
_XfExtRFPMRLTS1Threshold_Object = MibTableColumn
xfExtRFPMRLTS1Threshold = _XfExtRFPMRLTS1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 1),
    _XfExtRFPMRLTS1Threshold_Type()
)
xfExtRFPMRLTS1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMRLTS1Threshold.setStatus("current")


class _XfExtRFPMSetThreshold15mRLTS1_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold15mRLTS1 based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfExtRFPMSetThreshold15mRLTS1_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold15mRLTS1_Object = MibTableColumn
xfExtRFPMSetThreshold15mRLTS1 = _XfExtRFPMSetThreshold15mRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 2),
    _XfExtRFPMSetThreshold15mRLTS1_Type()
)
xfExtRFPMSetThreshold15mRLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold15mRLTS1.setStatus("current")


class _XfExtRFPMResetThreshold15mRLTS1_Type(Integer32):
    """Custom type xfExtRFPMResetThreshold15mRLTS1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfExtRFPMResetThreshold15mRLTS1_Type.__name__ = "Integer32"
_XfExtRFPMResetThreshold15mRLTS1_Object = MibTableColumn
xfExtRFPMResetThreshold15mRLTS1 = _XfExtRFPMResetThreshold15mRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 3),
    _XfExtRFPMResetThreshold15mRLTS1_Type()
)
xfExtRFPMResetThreshold15mRLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMResetThreshold15mRLTS1.setStatus("current")


class _XfExtRFPMRLTS2Threshold_Type(Integer32):
    """Custom type xfExtRFPMRLTS2Threshold based on Integer32"""
    defaultValue = -998

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-998, -200),
    )


_XfExtRFPMRLTS2Threshold_Type.__name__ = "Integer32"
_XfExtRFPMRLTS2Threshold_Object = MibTableColumn
xfExtRFPMRLTS2Threshold = _XfExtRFPMRLTS2Threshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 4),
    _XfExtRFPMRLTS2Threshold_Type()
)
xfExtRFPMRLTS2Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMRLTS2Threshold.setStatus("current")


class _XfExtRFPMSetThreshold15mRLTS2_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold15mRLTS2 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfExtRFPMSetThreshold15mRLTS2_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold15mRLTS2_Object = MibTableColumn
xfExtRFPMSetThreshold15mRLTS2 = _XfExtRFPMSetThreshold15mRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 5),
    _XfExtRFPMSetThreshold15mRLTS2_Type()
)
xfExtRFPMSetThreshold15mRLTS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold15mRLTS2.setStatus("current")


class _XfExtRFPMResetThreshold15mRLTS2_Type(Integer32):
    """Custom type xfExtRFPMResetThreshold15mRLTS2 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfExtRFPMResetThreshold15mRLTS2_Type.__name__ = "Integer32"
_XfExtRFPMResetThreshold15mRLTS2_Object = MibTableColumn
xfExtRFPMResetThreshold15mRLTS2 = _XfExtRFPMResetThreshold15mRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 6),
    _XfExtRFPMResetThreshold15mRLTS2_Type()
)
xfExtRFPMResetThreshold15mRLTS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMResetThreshold15mRLTS2.setStatus("current")


class _XfExtRFPMSetThreshold15mRLTM_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold15mRLTM based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 800),
    )


_XfExtRFPMSetThreshold15mRLTM_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold15mRLTM_Object = MibTableColumn
xfExtRFPMSetThreshold15mRLTM = _XfExtRFPMSetThreshold15mRLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 7),
    _XfExtRFPMSetThreshold15mRLTM_Type()
)
xfExtRFPMSetThreshold15mRLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold15mRLTM.setStatus("current")


class _XfExtRFPMResetThreshold15mRLTM_Type(Integer32):
    """Custom type xfExtRFPMResetThreshold15mRLTM based on Integer32"""
    defaultValue = 790

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 800),
    )


_XfExtRFPMResetThreshold15mRLTM_Type.__name__ = "Integer32"
_XfExtRFPMResetThreshold15mRLTM_Object = MibTableColumn
xfExtRFPMResetThreshold15mRLTM = _XfExtRFPMResetThreshold15mRLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 8),
    _XfExtRFPMResetThreshold15mRLTM_Type()
)
xfExtRFPMResetThreshold15mRLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMResetThreshold15mRLTM.setStatus("current")


class _XfExtRFPMTLTS1Threshold_Type(Integer32):
    """Custom type xfExtRFPMTLTS1Threshold based on Integer32"""
    defaultValue = 45

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
    )


_XfExtRFPMTLTS1Threshold_Type.__name__ = "Integer32"
_XfExtRFPMTLTS1Threshold_Object = MibTableColumn
xfExtRFPMTLTS1Threshold = _XfExtRFPMTLTS1Threshold_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 9),
    _XfExtRFPMTLTS1Threshold_Type()
)
xfExtRFPMTLTS1Threshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMTLTS1Threshold.setStatus("current")


class _XfExtRFPMSetThreshold15mTLTS1_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold15mTLTS1 based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfExtRFPMSetThreshold15mTLTS1_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold15mTLTS1_Object = MibTableColumn
xfExtRFPMSetThreshold15mTLTS1 = _XfExtRFPMSetThreshold15mTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 10),
    _XfExtRFPMSetThreshold15mTLTS1_Type()
)
xfExtRFPMSetThreshold15mTLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold15mTLTS1.setStatus("current")


class _XfExtRFPMResetThreshold15mTLTS1_Type(Integer32):
    """Custom type xfExtRFPMResetThreshold15mTLTS1 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 900),
    )


_XfExtRFPMResetThreshold15mTLTS1_Type.__name__ = "Integer32"
_XfExtRFPMResetThreshold15mTLTS1_Object = MibTableColumn
xfExtRFPMResetThreshold15mTLTS1 = _XfExtRFPMResetThreshold15mTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 11),
    _XfExtRFPMResetThreshold15mTLTS1_Type()
)
xfExtRFPMResetThreshold15mTLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMResetThreshold15mTLTS1.setStatus("current")


class _XfExtRFPMSetThreshold15mTLTM_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold15mTLTM based on Integer32"""
    defaultValue = 145

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 145),
    )


_XfExtRFPMSetThreshold15mTLTM_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold15mTLTM_Object = MibTableColumn
xfExtRFPMSetThreshold15mTLTM = _XfExtRFPMSetThreshold15mTLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 12),
    _XfExtRFPMSetThreshold15mTLTM_Type()
)
xfExtRFPMSetThreshold15mTLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold15mTLTM.setStatus("current")


class _XfExtRFPMResetThreshold15mTLTM_Type(Integer32):
    """Custom type xfExtRFPMResetThreshold15mTLTM based on Integer32"""
    defaultValue = 144

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 145),
    )


_XfExtRFPMResetThreshold15mTLTM_Type.__name__ = "Integer32"
_XfExtRFPMResetThreshold15mTLTM_Object = MibTableColumn
xfExtRFPMResetThreshold15mTLTM = _XfExtRFPMResetThreshold15mTLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 13),
    _XfExtRFPMResetThreshold15mTLTM_Type()
)
xfExtRFPMResetThreshold15mTLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMResetThreshold15mTLTM.setStatus("current")


class _XfExtRFPMSetThreshold24hRLTS1_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold24hRLTS1 based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_XfExtRFPMSetThreshold24hRLTS1_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold24hRLTS1_Object = MibTableColumn
xfExtRFPMSetThreshold24hRLTS1 = _XfExtRFPMSetThreshold24hRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 14),
    _XfExtRFPMSetThreshold24hRLTS1_Type()
)
xfExtRFPMSetThreshold24hRLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold24hRLTS1.setStatus("current")


class _XfExtRFPMSetThreshold24hRLTS2_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold24hRLTS2 based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_XfExtRFPMSetThreshold24hRLTS2_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold24hRLTS2_Object = MibTableColumn
xfExtRFPMSetThreshold24hRLTS2 = _XfExtRFPMSetThreshold24hRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 15),
    _XfExtRFPMSetThreshold24hRLTS2_Type()
)
xfExtRFPMSetThreshold24hRLTS2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold24hRLTS2.setStatus("current")


class _XfExtRFPMSetThreshold24hRLTM_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold24hRLTM based on Integer32"""
    defaultValue = 800

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 800),
    )


_XfExtRFPMSetThreshold24hRLTM_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold24hRLTM_Object = MibTableColumn
xfExtRFPMSetThreshold24hRLTM = _XfExtRFPMSetThreshold24hRLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 16),
    _XfExtRFPMSetThreshold24hRLTM_Type()
)
xfExtRFPMSetThreshold24hRLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold24hRLTM.setStatus("current")


class _XfExtRFPMSetThreshold24hTLTS1_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold24hTLTS1 based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_XfExtRFPMSetThreshold24hTLTS1_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold24hTLTS1_Object = MibTableColumn
xfExtRFPMSetThreshold24hTLTS1 = _XfExtRFPMSetThreshold24hTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 17),
    _XfExtRFPMSetThreshold24hTLTS1_Type()
)
xfExtRFPMSetThreshold24hTLTS1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold24hTLTS1.setStatus("current")


class _XfExtRFPMSetThreshold24hTLTM_Type(Integer32):
    """Custom type xfExtRFPMSetThreshold24hTLTM based on Integer32"""
    defaultValue = 145

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 145),
    )


_XfExtRFPMSetThreshold24hTLTM_Type.__name__ = "Integer32"
_XfExtRFPMSetThreshold24hTLTM_Object = MibTableColumn
xfExtRFPMSetThreshold24hTLTM = _XfExtRFPMSetThreshold24hTLTM_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 18),
    _XfExtRFPMSetThreshold24hTLTM_Type()
)
xfExtRFPMSetThreshold24hTLTM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMSetThreshold24hTLTM.setStatus("current")


class _XfExtRFPMStatus_Type(Bits):
    """Custom type xfExtRFPMStatus based on Bits"""
    namedValues = NamedValues(
        *(("rlts1Counter15m0", 0),
          ("rlts1Counter15m1", 1),
          ("rlts1Counter15m2", 2),
          ("rlts2Counter15m0", 3),
          ("rlts2Counter15m1", 4),
          ("rlts2Counter15m2", 5),
          ("rltmCounter15m0", 6),
          ("rltmCounter15m1", 7),
          ("rltmCounter15m2", 8),
          ("tlts1Counter15m0", 9),
          ("tlts1Counter15m1", 10),
          ("tlts1Counter15m2", 11),
          ("tltmCounter15m0", 12),
          ("tltmCounter15m1", 13),
          ("tltmCounter15m2", 14),
          ("rlts1Counter24h0", 15),
          ("rlts1Counter24h1", 16),
          ("rlts1Counter24h2", 17),
          ("rlts2Counter24h0", 18),
          ("rlts2Counter24h1", 19),
          ("rlts2Counter24h2", 20),
          ("rltmCounter24h0", 21),
          ("rltmCounter24h1", 22),
          ("rltmCounter24h2", 23),
          ("tlts1Counter24h0", 24),
          ("tlts1Counter24h1", 25),
          ("tlts1Counter24h2", 26),
          ("tltmCounter24h0", 27),
          ("tltmCounter24h1", 28),
          ("tltmCounter24h2", 29))
    )

_XfExtRFPMStatus_Type.__name__ = "Bits"
_XfExtRFPMStatus_Object = MibTableColumn
xfExtRFPMStatus = _XfExtRFPMStatus_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 19),
    _XfExtRFPMStatus_Type()
)
xfExtRFPMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMStatus.setStatus("current")


class _XfExtRFPMView_Type(Integer32):
    """Custom type xfExtRFPMView based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("extPmEnable", 1),
          ("extPmDisable", 2))
    )


_XfExtRFPMView_Type.__name__ = "Integer32"
_XfExtRFPMView_Object = MibTableColumn
xfExtRFPMView = _XfExtRFPMView_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 27, 1, 20),
    _XfExtRFPMView_Type()
)
xfExtRFPMView.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xfExtRFPMView.setStatus("current")
_XfRLExtRFPMCurrent24hTable_Object = MibTable
xfRLExtRFPMCurrent24hTable = _XfRLExtRFPMCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28)
)
if mibBuilder.loadTexts:
    xfRLExtRFPMCurrent24hTable.setStatus("current")
_XfRLExtRFPMCurrent24hEntry_Object = MibTableRow
xfRLExtRFPMCurrent24hEntry = _XfRLExtRFPMCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28, 1)
)
xfRLExtRFPMCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLExtRFPMCurrent24hEntry.setStatus("current")
_XfExtRFPMCurrent24hElapsedTime_Type = Counter32
_XfExtRFPMCurrent24hElapsedTime_Object = MibTableColumn
xfExtRFPMCurrent24hElapsedTime = _XfExtRFPMCurrent24hElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28, 1, 1),
    _XfExtRFPMCurrent24hElapsedTime_Type()
)
xfExtRFPMCurrent24hElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent24hElapsedTime.setStatus("current")


class _XfExtRFPMCurrent24hRLTS1_Type(Integer32):
    """Custom type xfExtRFPMCurrent24hRLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 86400),
    )


_XfExtRFPMCurrent24hRLTS1_Type.__name__ = "Integer32"
_XfExtRFPMCurrent24hRLTS1_Object = MibTableColumn
xfExtRFPMCurrent24hRLTS1 = _XfExtRFPMCurrent24hRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28, 1, 2),
    _XfExtRFPMCurrent24hRLTS1_Type()
)
xfExtRFPMCurrent24hRLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent24hRLTS1.setStatus("current")


class _XfExtRFPMCurrent24hRLTS2_Type(Integer32):
    """Custom type xfExtRFPMCurrent24hRLTS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 86400),
    )


_XfExtRFPMCurrent24hRLTS2_Type.__name__ = "Integer32"
_XfExtRFPMCurrent24hRLTS2_Object = MibTableColumn
xfExtRFPMCurrent24hRLTS2 = _XfExtRFPMCurrent24hRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28, 1, 3),
    _XfExtRFPMCurrent24hRLTS2_Type()
)
xfExtRFPMCurrent24hRLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent24hRLTS2.setStatus("current")


class _XfExtRFPMCurrent24hRLMin_Type(Integer32):
    """Custom type xfExtRFPMCurrent24hRLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfExtRFPMCurrent24hRLMin_Type.__name__ = "Integer32"
_XfExtRFPMCurrent24hRLMin_Object = MibTableColumn
xfExtRFPMCurrent24hRLMin = _XfExtRFPMCurrent24hRLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28, 1, 4),
    _XfExtRFPMCurrent24hRLMin_Type()
)
xfExtRFPMCurrent24hRLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent24hRLMin.setStatus("current")


class _XfExtRFPMCurrent24hRLMax_Type(Integer32):
    """Custom type xfExtRFPMCurrent24hRLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfExtRFPMCurrent24hRLMax_Type.__name__ = "Integer32"
_XfExtRFPMCurrent24hRLMax_Object = MibTableColumn
xfExtRFPMCurrent24hRLMax = _XfExtRFPMCurrent24hRLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28, 1, 5),
    _XfExtRFPMCurrent24hRLMax_Type()
)
xfExtRFPMCurrent24hRLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent24hRLMax.setStatus("current")


class _XfExtRFPMCurrent24hTLTS1_Type(Integer32):
    """Custom type xfExtRFPMCurrent24hTLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 86400),
    )


_XfExtRFPMCurrent24hTLTS1_Type.__name__ = "Integer32"
_XfExtRFPMCurrent24hTLTS1_Object = MibTableColumn
xfExtRFPMCurrent24hTLTS1 = _XfExtRFPMCurrent24hTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28, 1, 6),
    _XfExtRFPMCurrent24hTLTS1_Type()
)
xfExtRFPMCurrent24hTLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent24hTLTS1.setStatus("current")


class _XfExtRFPMCurrent24hTLMin_Type(Integer32):
    """Custom type xfExtRFPMCurrent24hTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfExtRFPMCurrent24hTLMin_Type.__name__ = "Integer32"
_XfExtRFPMCurrent24hTLMin_Object = MibTableColumn
xfExtRFPMCurrent24hTLMin = _XfExtRFPMCurrent24hTLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28, 1, 7),
    _XfExtRFPMCurrent24hTLMin_Type()
)
xfExtRFPMCurrent24hTLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent24hTLMin.setStatus("current")


class _XfExtRFPMCurrent24hTLMax_Type(Integer32):
    """Custom type xfExtRFPMCurrent24hTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfExtRFPMCurrent24hTLMax_Type.__name__ = "Integer32"
_XfExtRFPMCurrent24hTLMax_Object = MibTableColumn
xfExtRFPMCurrent24hTLMax = _XfExtRFPMCurrent24hTLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 28, 1, 8),
    _XfExtRFPMCurrent24hTLMax_Type()
)
xfExtRFPMCurrent24hTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent24hTLMax.setStatus("current")
_XfRLExtRFPMInterval24hTable_Object = MibTable
xfRLExtRFPMInterval24hTable = _XfRLExtRFPMInterval24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29)
)
if mibBuilder.loadTexts:
    xfRLExtRFPMInterval24hTable.setStatus("current")
_XfRLExtRFPMInterval24hEntry_Object = MibTableRow
xfRLExtRFPMInterval24hEntry = _XfRLExtRFPMInterval24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29, 1)
)
xfRLExtRFPMInterval24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLExtRFPMInterval24hEntry.setStatus("current")


class _XfExtRFPMInterval24hRLTS1_Type(Integer32):
    """Custom type xfExtRFPMInterval24hRLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 86400),
    )


_XfExtRFPMInterval24hRLTS1_Type.__name__ = "Integer32"
_XfExtRFPMInterval24hRLTS1_Object = MibTableColumn
xfExtRFPMInterval24hRLTS1 = _XfExtRFPMInterval24hRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29, 1, 1),
    _XfExtRFPMInterval24hRLTS1_Type()
)
xfExtRFPMInterval24hRLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval24hRLTS1.setStatus("current")


class _XfExtRFPMInterval24hRLTS2_Type(Integer32):
    """Custom type xfExtRFPMInterval24hRLTS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 86400),
    )


_XfExtRFPMInterval24hRLTS2_Type.__name__ = "Integer32"
_XfExtRFPMInterval24hRLTS2_Object = MibTableColumn
xfExtRFPMInterval24hRLTS2 = _XfExtRFPMInterval24hRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29, 1, 2),
    _XfExtRFPMInterval24hRLTS2_Type()
)
xfExtRFPMInterval24hRLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval24hRLTS2.setStatus("current")


class _XfExtRFPMInterval24hRLMin_Type(Integer32):
    """Custom type xfExtRFPMInterval24hRLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfExtRFPMInterval24hRLMin_Type.__name__ = "Integer32"
_XfExtRFPMInterval24hRLMin_Object = MibTableColumn
xfExtRFPMInterval24hRLMin = _XfExtRFPMInterval24hRLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29, 1, 3),
    _XfExtRFPMInterval24hRLMin_Type()
)
xfExtRFPMInterval24hRLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval24hRLMin.setStatus("current")


class _XfExtRFPMInterval24hRLMax_Type(Integer32):
    """Custom type xfExtRFPMInterval24hRLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfExtRFPMInterval24hRLMax_Type.__name__ = "Integer32"
_XfExtRFPMInterval24hRLMax_Object = MibTableColumn
xfExtRFPMInterval24hRLMax = _XfExtRFPMInterval24hRLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29, 1, 4),
    _XfExtRFPMInterval24hRLMax_Type()
)
xfExtRFPMInterval24hRLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval24hRLMax.setStatus("current")


class _XfExtRFPMInterval24hTLTS1_Type(Integer32):
    """Custom type xfExtRFPMInterval24hTLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 86400),
    )


_XfExtRFPMInterval24hTLTS1_Type.__name__ = "Integer32"
_XfExtRFPMInterval24hTLTS1_Object = MibTableColumn
xfExtRFPMInterval24hTLTS1 = _XfExtRFPMInterval24hTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29, 1, 5),
    _XfExtRFPMInterval24hTLTS1_Type()
)
xfExtRFPMInterval24hTLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval24hTLTS1.setStatus("current")


class _XfExtRFPMInterval24hTLMin_Type(Integer32):
    """Custom type xfExtRFPMInterval24hTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfExtRFPMInterval24hTLMin_Type.__name__ = "Integer32"
_XfExtRFPMInterval24hTLMin_Object = MibTableColumn
xfExtRFPMInterval24hTLMin = _XfExtRFPMInterval24hTLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29, 1, 6),
    _XfExtRFPMInterval24hTLMin_Type()
)
xfExtRFPMInterval24hTLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval24hTLMin.setStatus("current")


class _XfExtRFPMInterval24hTLMax_Type(Integer32):
    """Custom type xfExtRFPMInterval24hTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfExtRFPMInterval24hTLMax_Type.__name__ = "Integer32"
_XfExtRFPMInterval24hTLMax_Object = MibTableColumn
xfExtRFPMInterval24hTLMax = _XfExtRFPMInterval24hTLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29, 1, 7),
    _XfExtRFPMInterval24hTLMax_Type()
)
xfExtRFPMInterval24hTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval24hTLMax.setStatus("current")
_XfExtRFPMInterval24hValidData_Type = TruthValue
_XfExtRFPMInterval24hValidData_Object = MibTableColumn
xfExtRFPMInterval24hValidData = _XfExtRFPMInterval24hValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 29, 1, 8),
    _XfExtRFPMInterval24hValidData_Type()
)
xfExtRFPMInterval24hValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval24hValidData.setStatus("current")
_XfRLExtRFPMCurrent15mTable_Object = MibTable
xfRLExtRFPMCurrent15mTable = _XfRLExtRFPMCurrent15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30)
)
if mibBuilder.loadTexts:
    xfRLExtRFPMCurrent15mTable.setStatus("current")
_XfRLExtRFPMCurrent15mEntry_Object = MibTableRow
xfRLExtRFPMCurrent15mEntry = _XfRLExtRFPMCurrent15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30, 1)
)
xfRLExtRFPMCurrent15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLExtRFPMCurrent15mEntry.setStatus("current")
_XfExtRFPMCurrent15mElapsedTime_Type = Counter32
_XfExtRFPMCurrent15mElapsedTime_Object = MibTableColumn
xfExtRFPMCurrent15mElapsedTime = _XfExtRFPMCurrent15mElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30, 1, 1),
    _XfExtRFPMCurrent15mElapsedTime_Type()
)
xfExtRFPMCurrent15mElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent15mElapsedTime.setStatus("current")


class _XfExtRFPMCurrent15mRLTS1_Type(Integer32):
    """Custom type xfExtRFPMCurrent15mRLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 900),
    )


_XfExtRFPMCurrent15mRLTS1_Type.__name__ = "Integer32"
_XfExtRFPMCurrent15mRLTS1_Object = MibTableColumn
xfExtRFPMCurrent15mRLTS1 = _XfExtRFPMCurrent15mRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30, 1, 2),
    _XfExtRFPMCurrent15mRLTS1_Type()
)
xfExtRFPMCurrent15mRLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent15mRLTS1.setStatus("current")


class _XfExtRFPMCurrent15mRLTS2_Type(Integer32):
    """Custom type xfExtRFPMCurrent15mRLTS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 900),
    )


_XfExtRFPMCurrent15mRLTS2_Type.__name__ = "Integer32"
_XfExtRFPMCurrent15mRLTS2_Object = MibTableColumn
xfExtRFPMCurrent15mRLTS2 = _XfExtRFPMCurrent15mRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30, 1, 3),
    _XfExtRFPMCurrent15mRLTS2_Type()
)
xfExtRFPMCurrent15mRLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent15mRLTS2.setStatus("current")


class _XfExtRFPMCurrent15mRLMin_Type(Integer32):
    """Custom type xfExtRFPMCurrent15mRLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfExtRFPMCurrent15mRLMin_Type.__name__ = "Integer32"
_XfExtRFPMCurrent15mRLMin_Object = MibTableColumn
xfExtRFPMCurrent15mRLMin = _XfExtRFPMCurrent15mRLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30, 1, 4),
    _XfExtRFPMCurrent15mRLMin_Type()
)
xfExtRFPMCurrent15mRLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent15mRLMin.setStatus("current")


class _XfExtRFPMCurrent15mRLMax_Type(Integer32):
    """Custom type xfExtRFPMCurrent15mRLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfExtRFPMCurrent15mRLMax_Type.__name__ = "Integer32"
_XfExtRFPMCurrent15mRLMax_Object = MibTableColumn
xfExtRFPMCurrent15mRLMax = _XfExtRFPMCurrent15mRLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30, 1, 5),
    _XfExtRFPMCurrent15mRLMax_Type()
)
xfExtRFPMCurrent15mRLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent15mRLMax.setStatus("current")


class _XfExtRFPMCurrent15mTLTS1_Type(Integer32):
    """Custom type xfExtRFPMCurrent15mTLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 900),
    )


_XfExtRFPMCurrent15mTLTS1_Type.__name__ = "Integer32"
_XfExtRFPMCurrent15mTLTS1_Object = MibTableColumn
xfExtRFPMCurrent15mTLTS1 = _XfExtRFPMCurrent15mTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30, 1, 6),
    _XfExtRFPMCurrent15mTLTS1_Type()
)
xfExtRFPMCurrent15mTLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent15mTLTS1.setStatus("current")


class _XfExtRFPMCurrent15mTLMin_Type(Integer32):
    """Custom type xfExtRFPMCurrent15mTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfExtRFPMCurrent15mTLMin_Type.__name__ = "Integer32"
_XfExtRFPMCurrent15mTLMin_Object = MibTableColumn
xfExtRFPMCurrent15mTLMin = _XfExtRFPMCurrent15mTLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30, 1, 7),
    _XfExtRFPMCurrent15mTLMin_Type()
)
xfExtRFPMCurrent15mTLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent15mTLMin.setStatus("current")


class _XfExtRFPMCurrent15mTLMax_Type(Integer32):
    """Custom type xfExtRFPMCurrent15mTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfExtRFPMCurrent15mTLMax_Type.__name__ = "Integer32"
_XfExtRFPMCurrent15mTLMax_Object = MibTableColumn
xfExtRFPMCurrent15mTLMax = _XfExtRFPMCurrent15mTLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 30, 1, 8),
    _XfExtRFPMCurrent15mTLMax_Type()
)
xfExtRFPMCurrent15mTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMCurrent15mTLMax.setStatus("current")
_XfRLExtRFPMInterval15mTable_Object = MibTable
xfRLExtRFPMInterval15mTable = _XfRLExtRFPMInterval15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31)
)
if mibBuilder.loadTexts:
    xfRLExtRFPMInterval15mTable.setStatus("current")
_XfRLExtRFPMInterval15mEntry_Object = MibTableRow
xfRLExtRFPMInterval15mEntry = _XfRLExtRFPMInterval15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1)
)
xfRLExtRFPMInterval15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mIntervalNumber"),
)
if mibBuilder.loadTexts:
    xfRLExtRFPMInterval15mEntry.setStatus("current")


class _XfExtRFPMInterval15mIntervalNumber_Type(Integer32):
    """Custom type xfExtRFPMInterval15mIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_XfExtRFPMInterval15mIntervalNumber_Type.__name__ = "Integer32"
_XfExtRFPMInterval15mIntervalNumber_Object = MibTableColumn
xfExtRFPMInterval15mIntervalNumber = _XfExtRFPMInterval15mIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1, 1),
    _XfExtRFPMInterval15mIntervalNumber_Type()
)
xfExtRFPMInterval15mIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval15mIntervalNumber.setStatus("current")


class _XfExtRFPMInterval15mRLTS1_Type(Integer32):
    """Custom type xfExtRFPMInterval15mRLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 900),
    )


_XfExtRFPMInterval15mRLTS1_Type.__name__ = "Integer32"
_XfExtRFPMInterval15mRLTS1_Object = MibTableColumn
xfExtRFPMInterval15mRLTS1 = _XfExtRFPMInterval15mRLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1, 2),
    _XfExtRFPMInterval15mRLTS1_Type()
)
xfExtRFPMInterval15mRLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval15mRLTS1.setStatus("current")


class _XfExtRFPMInterval15mRLTS2_Type(Integer32):
    """Custom type xfExtRFPMInterval15mRLTS2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 900),
    )


_XfExtRFPMInterval15mRLTS2_Type.__name__ = "Integer32"
_XfExtRFPMInterval15mRLTS2_Object = MibTableColumn
xfExtRFPMInterval15mRLTS2 = _XfExtRFPMInterval15mRLTS2_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1, 3),
    _XfExtRFPMInterval15mRLTS2_Type()
)
xfExtRFPMInterval15mRLTS2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval15mRLTS2.setStatus("current")


class _XfExtRFPMInterval15mRLMin_Type(Integer32):
    """Custom type xfExtRFPMInterval15mRLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfExtRFPMInterval15mRLMin_Type.__name__ = "Integer32"
_XfExtRFPMInterval15mRLMin_Object = MibTableColumn
xfExtRFPMInterval15mRLMin = _XfExtRFPMInterval15mRLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1, 4),
    _XfExtRFPMInterval15mRLMin_Type()
)
xfExtRFPMInterval15mRLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval15mRLMin.setStatus("current")


class _XfExtRFPMInterval15mRLMax_Type(Integer32):
    """Custom type xfExtRFPMInterval15mRLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-999, -200),
        ValueRangeConstraint(0, 0),
    )


_XfExtRFPMInterval15mRLMax_Type.__name__ = "Integer32"
_XfExtRFPMInterval15mRLMax_Object = MibTableColumn
xfExtRFPMInterval15mRLMax = _XfExtRFPMInterval15mRLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1, 5),
    _XfExtRFPMInterval15mRLMax_Type()
)
xfExtRFPMInterval15mRLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval15mRLMax.setStatus("current")


class _XfExtRFPMInterval15mTLTS1_Type(Integer32):
    """Custom type xfExtRFPMInterval15mTLTS1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 900),
    )


_XfExtRFPMInterval15mTLTS1_Type.__name__ = "Integer32"
_XfExtRFPMInterval15mTLTS1_Object = MibTableColumn
xfExtRFPMInterval15mTLTS1 = _XfExtRFPMInterval15mTLTS1_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1, 6),
    _XfExtRFPMInterval15mTLTS1_Type()
)
xfExtRFPMInterval15mTLTS1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval15mTLTS1.setStatus("current")


class _XfExtRFPMInterval15mTLMin_Type(Integer32):
    """Custom type xfExtRFPMInterval15mTLMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfExtRFPMInterval15mTLMin_Type.__name__ = "Integer32"
_XfExtRFPMInterval15mTLMin_Object = MibTableColumn
xfExtRFPMInterval15mTLMin = _XfExtRFPMInterval15mTLMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1, 7),
    _XfExtRFPMInterval15mTLMin_Type()
)
xfExtRFPMInterval15mTLMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval15mTLMin.setStatus("current")


class _XfExtRFPMInterval15mTLMax_Type(Integer32):
    """Custom type xfExtRFPMInterval15mTLMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-100, 45),
        ValueRangeConstraint(255, 255),
    )


_XfExtRFPMInterval15mTLMax_Type.__name__ = "Integer32"
_XfExtRFPMInterval15mTLMax_Object = MibTableColumn
xfExtRFPMInterval15mTLMax = _XfExtRFPMInterval15mTLMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1, 8),
    _XfExtRFPMInterval15mTLMax_Type()
)
xfExtRFPMInterval15mTLMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval15mTLMax.setStatus("current")
_XfExtRFPMInterval15mValidData_Type = TruthValue
_XfExtRFPMInterval15mValidData_Object = MibTableColumn
xfExtRFPMInterval15mValidData = _XfExtRFPMInterval15mValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 31, 1, 9),
    _XfExtRFPMInterval15mValidData_Type()
)
xfExtRFPMInterval15mValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRFPMInterval15mValidData.setStatus("current")
_XfRLExtRAUPMCurrent24hTable_Object = MibTable
xfRLExtRAUPMCurrent24hTable = _XfRLExtRAUPMCurrent24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 32)
)
if mibBuilder.loadTexts:
    xfRLExtRAUPMCurrent24hTable.setStatus("current")
_XfRLExtRAUPMCurrent24hEntry_Object = MibTableRow
xfRLExtRAUPMCurrent24hEntry = _XfRLExtRAUPMCurrent24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 32, 1)
)
xfRLExtRAUPMCurrent24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLExtRAUPMCurrent24hEntry.setStatus("current")
_XfExtRAUPMCurrent24hElapsedTime_Type = Counter32
_XfExtRAUPMCurrent24hElapsedTime_Object = MibTableColumn
xfExtRAUPMCurrent24hElapsedTime = _XfExtRAUPMCurrent24hElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 32, 1, 1),
    _XfExtRAUPMCurrent24hElapsedTime_Type()
)
xfExtRAUPMCurrent24hElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent24hElapsedTime.setStatus("current")


class _XfExtRAUPMCurrent24hMSEMin_Type(Integer32):
    """Custom type xfExtRAUPMCurrent24hMSEMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMCurrent24hMSEMin_Type.__name__ = "Integer32"
_XfExtRAUPMCurrent24hMSEMin_Object = MibTableColumn
xfExtRAUPMCurrent24hMSEMin = _XfExtRAUPMCurrent24hMSEMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 32, 1, 2),
    _XfExtRAUPMCurrent24hMSEMin_Type()
)
xfExtRAUPMCurrent24hMSEMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent24hMSEMin.setStatus("current")


class _XfExtRAUPMCurrent24hMSEMax_Type(Integer32):
    """Custom type xfExtRAUPMCurrent24hMSEMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMCurrent24hMSEMax_Type.__name__ = "Integer32"
_XfExtRAUPMCurrent24hMSEMax_Object = MibTableColumn
xfExtRAUPMCurrent24hMSEMax = _XfExtRAUPMCurrent24hMSEMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 32, 1, 3),
    _XfExtRAUPMCurrent24hMSEMax_Type()
)
xfExtRAUPMCurrent24hMSEMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent24hMSEMax.setStatus("current")


class _XfExtRAUPMCurrent24hXPIMin_Type(Integer32):
    """Custom type xfExtRAUPMCurrent24hXPIMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMCurrent24hXPIMin_Type.__name__ = "Integer32"
_XfExtRAUPMCurrent24hXPIMin_Object = MibTableColumn
xfExtRAUPMCurrent24hXPIMin = _XfExtRAUPMCurrent24hXPIMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 32, 1, 4),
    _XfExtRAUPMCurrent24hXPIMin_Type()
)
xfExtRAUPMCurrent24hXPIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent24hXPIMin.setStatus("current")


class _XfExtRAUPMCurrent24hXPIMax_Type(Integer32):
    """Custom type xfExtRAUPMCurrent24hXPIMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMCurrent24hXPIMax_Type.__name__ = "Integer32"
_XfExtRAUPMCurrent24hXPIMax_Object = MibTableColumn
xfExtRAUPMCurrent24hXPIMax = _XfExtRAUPMCurrent24hXPIMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 32, 1, 5),
    _XfExtRAUPMCurrent24hXPIMax_Type()
)
xfExtRAUPMCurrent24hXPIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent24hXPIMax.setStatus("current")
_XfRLExtRAUPMInterval24hTable_Object = MibTable
xfRLExtRAUPMInterval24hTable = _XfRLExtRAUPMInterval24hTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 33)
)
if mibBuilder.loadTexts:
    xfRLExtRAUPMInterval24hTable.setStatus("current")
_XfRLExtRAUPMInterval24hEntry_Object = MibTableRow
xfRLExtRAUPMInterval24hEntry = _XfRLExtRAUPMInterval24hEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 33, 1)
)
xfRLExtRAUPMInterval24hEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLExtRAUPMInterval24hEntry.setStatus("current")


class _XfExtRAUPMInterval24hMSEMin_Type(Integer32):
    """Custom type xfExtRAUPMInterval24hMSEMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMInterval24hMSEMin_Type.__name__ = "Integer32"
_XfExtRAUPMInterval24hMSEMin_Object = MibTableColumn
xfExtRAUPMInterval24hMSEMin = _XfExtRAUPMInterval24hMSEMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 33, 1, 1),
    _XfExtRAUPMInterval24hMSEMin_Type()
)
xfExtRAUPMInterval24hMSEMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval24hMSEMin.setStatus("current")


class _XfExtRAUPMInterval24hMSEMax_Type(Integer32):
    """Custom type xfExtRAUPMInterval24hMSEMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMInterval24hMSEMax_Type.__name__ = "Integer32"
_XfExtRAUPMInterval24hMSEMax_Object = MibTableColumn
xfExtRAUPMInterval24hMSEMax = _XfExtRAUPMInterval24hMSEMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 33, 1, 2),
    _XfExtRAUPMInterval24hMSEMax_Type()
)
xfExtRAUPMInterval24hMSEMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval24hMSEMax.setStatus("current")


class _XfExtRAUPMInterval24hXPIMin_Type(Integer32):
    """Custom type xfExtRAUPMInterval24hXPIMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMInterval24hXPIMin_Type.__name__ = "Integer32"
_XfExtRAUPMInterval24hXPIMin_Object = MibTableColumn
xfExtRAUPMInterval24hXPIMin = _XfExtRAUPMInterval24hXPIMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 33, 1, 3),
    _XfExtRAUPMInterval24hXPIMin_Type()
)
xfExtRAUPMInterval24hXPIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval24hXPIMin.setStatus("current")


class _XfExtRAUPMInterval24hXPIMax_Type(Integer32):
    """Custom type xfExtRAUPMInterval24hXPIMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMInterval24hXPIMax_Type.__name__ = "Integer32"
_XfExtRAUPMInterval24hXPIMax_Object = MibTableColumn
xfExtRAUPMInterval24hXPIMax = _XfExtRAUPMInterval24hXPIMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 33, 1, 4),
    _XfExtRAUPMInterval24hXPIMax_Type()
)
xfExtRAUPMInterval24hXPIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval24hXPIMax.setStatus("current")
_XfExtRAUPMInterval24hValidData_Type = TruthValue
_XfExtRAUPMInterval24hValidData_Object = MibTableColumn
xfExtRAUPMInterval24hValidData = _XfExtRAUPMInterval24hValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 33, 1, 5),
    _XfExtRAUPMInterval24hValidData_Type()
)
xfExtRAUPMInterval24hValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval24hValidData.setStatus("current")
_XfRLExtRAUPMCurrent15mTable_Object = MibTable
xfRLExtRAUPMCurrent15mTable = _XfRLExtRAUPMCurrent15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 34)
)
if mibBuilder.loadTexts:
    xfRLExtRAUPMCurrent15mTable.setStatus("current")
_XfRLExtRAUPMCurrent15mEntry_Object = MibTableRow
xfRLExtRAUPMCurrent15mEntry = _XfRLExtRAUPMCurrent15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 34, 1)
)
xfRLExtRAUPMCurrent15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    xfRLExtRAUPMCurrent15mEntry.setStatus("current")
_XfExtRAUPMCurrent15mElapsedTime_Type = Counter32
_XfExtRAUPMCurrent15mElapsedTime_Object = MibTableColumn
xfExtRAUPMCurrent15mElapsedTime = _XfExtRAUPMCurrent15mElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 34, 1, 1),
    _XfExtRAUPMCurrent15mElapsedTime_Type()
)
xfExtRAUPMCurrent15mElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent15mElapsedTime.setStatus("current")


class _XfExtRAUPMCurrent15mMSEMin_Type(Integer32):
    """Custom type xfExtRAUPMCurrent15mMSEMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMCurrent15mMSEMin_Type.__name__ = "Integer32"
_XfExtRAUPMCurrent15mMSEMin_Object = MibTableColumn
xfExtRAUPMCurrent15mMSEMin = _XfExtRAUPMCurrent15mMSEMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 34, 1, 2),
    _XfExtRAUPMCurrent15mMSEMin_Type()
)
xfExtRAUPMCurrent15mMSEMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent15mMSEMin.setStatus("current")


class _XfExtRAUPMCurrent15mMSEMax_Type(Integer32):
    """Custom type xfExtRAUPMCurrent15mMSEMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMCurrent15mMSEMax_Type.__name__ = "Integer32"
_XfExtRAUPMCurrent15mMSEMax_Object = MibTableColumn
xfExtRAUPMCurrent15mMSEMax = _XfExtRAUPMCurrent15mMSEMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 34, 1, 3),
    _XfExtRAUPMCurrent15mMSEMax_Type()
)
xfExtRAUPMCurrent15mMSEMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent15mMSEMax.setStatus("current")


class _XfExtRAUPMCurrent15mXPIMin_Type(Integer32):
    """Custom type xfExtRAUPMCurrent15mXPIMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMCurrent15mXPIMin_Type.__name__ = "Integer32"
_XfExtRAUPMCurrent15mXPIMin_Object = MibTableColumn
xfExtRAUPMCurrent15mXPIMin = _XfExtRAUPMCurrent15mXPIMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 34, 1, 4),
    _XfExtRAUPMCurrent15mXPIMin_Type()
)
xfExtRAUPMCurrent15mXPIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent15mXPIMin.setStatus("current")


class _XfExtRAUPMCurrent15mXPIMax_Type(Integer32):
    """Custom type xfExtRAUPMCurrent15mXPIMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMCurrent15mXPIMax_Type.__name__ = "Integer32"
_XfExtRAUPMCurrent15mXPIMax_Object = MibTableColumn
xfExtRAUPMCurrent15mXPIMax = _XfExtRAUPMCurrent15mXPIMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 34, 1, 5),
    _XfExtRAUPMCurrent15mXPIMax_Type()
)
xfExtRAUPMCurrent15mXPIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMCurrent15mXPIMax.setStatus("current")
_XfRLExtRAUPMInterval15mTable_Object = MibTable
xfRLExtRAUPMInterval15mTable = _XfRLExtRAUPMInterval15mTable_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 35)
)
if mibBuilder.loadTexts:
    xfRLExtRAUPMInterval15mTable.setStatus("current")
_XfRLExtRAUPMInterval15mEntry_Object = MibTableRow
xfRLExtRAUPMInterval15mEntry = _XfRLExtRAUPMInterval15mEntry_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 35, 1)
)
xfRLExtRAUPMInterval15mEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval15mIntervalNumber"),
)
if mibBuilder.loadTexts:
    xfRLExtRAUPMInterval15mEntry.setStatus("current")


class _XfExtRAUPMInterval15mIntervalNumber_Type(Integer32):
    """Custom type xfExtRAUPMInterval15mIntervalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_XfExtRAUPMInterval15mIntervalNumber_Type.__name__ = "Integer32"
_XfExtRAUPMInterval15mIntervalNumber_Object = MibTableColumn
xfExtRAUPMInterval15mIntervalNumber = _XfExtRAUPMInterval15mIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 35, 1, 1),
    _XfExtRAUPMInterval15mIntervalNumber_Type()
)
xfExtRAUPMInterval15mIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval15mIntervalNumber.setStatus("current")


class _XfExtRAUPMInterval15mMSEMin_Type(Integer32):
    """Custom type xfExtRAUPMInterval15mMSEMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMInterval15mMSEMin_Type.__name__ = "Integer32"
_XfExtRAUPMInterval15mMSEMin_Object = MibTableColumn
xfExtRAUPMInterval15mMSEMin = _XfExtRAUPMInterval15mMSEMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 35, 1, 2),
    _XfExtRAUPMInterval15mMSEMin_Type()
)
xfExtRAUPMInterval15mMSEMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval15mMSEMin.setStatus("current")


class _XfExtRAUPMInterval15mMSEMax_Type(Integer32):
    """Custom type xfExtRAUPMInterval15mMSEMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMInterval15mMSEMax_Type.__name__ = "Integer32"
_XfExtRAUPMInterval15mMSEMax_Object = MibTableColumn
xfExtRAUPMInterval15mMSEMax = _XfExtRAUPMInterval15mMSEMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 35, 1, 3),
    _XfExtRAUPMInterval15mMSEMax_Type()
)
xfExtRAUPMInterval15mMSEMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval15mMSEMax.setStatus("current")


class _XfExtRAUPMInterval15mXPIMin_Type(Integer32):
    """Custom type xfExtRAUPMInterval15mXPIMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMInterval15mXPIMin_Type.__name__ = "Integer32"
_XfExtRAUPMInterval15mXPIMin_Object = MibTableColumn
xfExtRAUPMInterval15mXPIMin = _XfExtRAUPMInterval15mXPIMin_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 35, 1, 4),
    _XfExtRAUPMInterval15mXPIMin_Type()
)
xfExtRAUPMInterval15mXPIMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval15mXPIMin.setStatus("current")


class _XfExtRAUPMInterval15mXPIMax_Type(Integer32):
    """Custom type xfExtRAUPMInterval15mXPIMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1000, 1000),
        ValueRangeConstraint(2000, 2000),
    )


_XfExtRAUPMInterval15mXPIMax_Type.__name__ = "Integer32"
_XfExtRAUPMInterval15mXPIMax_Object = MibTableColumn
xfExtRAUPMInterval15mXPIMax = _XfExtRAUPMInterval15mXPIMax_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 35, 1, 5),
    _XfExtRAUPMInterval15mXPIMax_Type()
)
xfExtRAUPMInterval15mXPIMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval15mXPIMax.setStatus("current")
_XfExtRAUPMInterval15mValidData_Type = TruthValue
_XfExtRAUPMInterval15mValidData_Object = MibTableColumn
xfExtRAUPMInterval15mValidData = _XfExtRAUPMInterval15mValidData_Object(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 1, 35, 1, 6),
    _XfExtRAUPMInterval15mValidData_Type()
)
xfExtRAUPMInterval15mValidData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xfExtRAUPMInterval15mValidData.setStatus("current")
_XfRadioLinkPtpTerminalConformance_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpTerminalConformance = _XfRadioLinkPtpTerminalConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 2)
)
_XfRadioLinkPtpTerminalCompliances_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpTerminalCompliances = _XfRadioLinkPtpTerminalCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 2, 1)
)
_XfRadioLinkPtpTerminalGroups_ObjectIdentity = ObjectIdentity
xfRadioLinkPtpTerminalGroups = _XfRadioLinkPtpTerminalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 2, 2)
)

# Managed Objects groups

xfRadioLinkPtpTerminalCompleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 2, 2, 1)
)
xfRadioLinkPtpTerminalCompleteGroup.setObjects(
      *(("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermId"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermType"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermProtection"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCapacity"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCapacityCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermModulation"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermModulationCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRestore"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermAlarmSeverity"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermTrapEnable"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermAsPort"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRemoteIdCheck"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRemoteId"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermPreset"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermBerAlarmThreshold"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermFadeNotificationTimer"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermEquipmentProtectionIndex"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermSysName"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermChannelMode"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermChannelModeCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermTrafficAndDCN"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermFrameFormat"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermFrameFormatCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermDCNRadioConfiguration"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermDCNRadioCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermDCNLineConfiguration"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermDCNLineCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermFadeNotificationConfiguration"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermLineProtection"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermOutputPowerOperStatus"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermOutputPowerAdminStatus"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermAtpcCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermTimeElapsed"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCurrentES"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCurrentSES"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCurrentBBE"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCurrentUAS"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCurrentBB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermPerfReset"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermTimeElapsedEnRLBExt"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLProtectionMode"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLProtectionRau1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLProtectionRau2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLActiveTxRadio"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLSwitchOverReset"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLSwitchRevertiveTx"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLProtectionCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLTxSwitchOverConfiguration"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLLineProtectionStatus"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRLLineProtectionMode"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRADIORSAlarms"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRADIORSPerformanceAlarms"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold15mESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold15mSESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold15mBBEs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMResetThreshold15mESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMResetThreshold15mSESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMResetThreshold15mBBEs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold24hESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold24hSESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold24hBBEs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMView"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMStatus"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hTimeElapsed"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hSESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hBBEs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hUASs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hBBs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hSESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hBBEs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hUASs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hBBs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hRLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hRLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hTLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hTLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hMSEMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hMSEMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hXPIMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hXPIMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval24hValidData"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mElapsedTime"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mSESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mBBEs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mUASs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mBBs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mIntervalNumber"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mSESs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mBBEs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mUASs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mBBs"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mRLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mRLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mTLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mTLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mMSEMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mMSEMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mXPIMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mXPIMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMInterval15mValidData"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermInterfaces"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermInterfacesCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermChannelModeOperStatus"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermXPICRestore"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermTribCapacityActual"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermTribCapacityDesired"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermBitPipeCapacity"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermRowIndex"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCapabilitiesLastChange"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermActualRowIndex"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermMaxRowIndex"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermAdaptiveManualRowIndex"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermAdaptiveManualMode"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermSpectrumEfficiencyClass"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermSpectrumEfficiencyClassCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermChannelSpacing"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermChannelModulation"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermMaxTribCapacity"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermDCNCapacity"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermValidRow"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermMaxCapacity"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermFrameFormatType"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermFrameFormatRev"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermBerAlarmThresholdCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMSetThreshold15m"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMSetThreshold24h"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMResetThreshold15m"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMStatus"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMValidData"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h4QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h8QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h16QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h32QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h64QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h128QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h256QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h512QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h1024QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h4QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h8QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h16QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h32QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h64QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h128QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h256QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h512QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24hValidData"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h1024QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m4QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m8QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m16QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m32QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m64QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m128QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m256QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m512QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m1024QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15mIntervalNumber"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m4QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m8QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m16QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m32QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m64QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m128QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m256QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m512QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15mValidData"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m1024QAM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h4QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h8QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h16QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h32QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h64QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h128QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h256QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h512QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent24h1024QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h4QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h8QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h16QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h32QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h64QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h128QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h256QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h512QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval24h1024QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m4QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m8QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m16QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m32QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m64QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m128QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m256QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m512QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMCurrent15m1024QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m4QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m8QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m16QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m32QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m64QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m128QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m256QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m512QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMAMInterval15m1024QAMEnRLB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermIpAddress"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermProtectionCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermLineProtectionCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermTribAllocationActual"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermTribAllocationDesired"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermAutoRemoveLoopEnable"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCapacityLicense"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermCapacityLicenseRange"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermMaxCapacityRange"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermMaxTribCapacityRange"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermFadingRates"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermFadingRatesCapability"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermConfiguredBitPipeCapacity"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermTribCapacityConfigured"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermPacketMaxCapacity"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermPacketMinCapacity"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent15m0005dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent15m0510dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent15m1015dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent15m1520dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent15m2025dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent15m2530dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval15mIntervalNumber"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval15m0005dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval15m0510dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval15m1015dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval15m1520dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval15m2025dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval15m2530dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent24h0005dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent24h0510dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent24h1015dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent24h1520dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent24h2025dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainCurrent24h2530dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval24h0005dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval24h0510dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval24h1015dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval24h1520dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval24h2025dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainInterval24h2530dB"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainSetThreshold15m"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainSetThreshold24h"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainResetThreshold15m"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSDCGainStatus"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMRLTS1Threshold"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold15mRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMResetThreshold15mRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMRLTS2Threshold"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold15mRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMResetThreshold15mRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold15mRLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMResetThreshold15mRLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMTLTS1Threshold"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold15mTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMResetThreshold15mTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold15mTLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMResetThreshold15mTLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold24hRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold24hRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold24hRLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold24hTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMSetThreshold24hTLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hRLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hRLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hTLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hTLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hMSEMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hMSEMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hXPIMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hXPIMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mRLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mRLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mTLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mTLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mMSEMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mMSEMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mXPIMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mXPIMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mESR"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mSESR"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent15mBBER"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hESR"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hSESR"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfPMCurrent24hBBER"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMRLTS1Threshold"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold15mRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMResetThreshold15mRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMRLTS2Threshold"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold15mRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMResetThreshold15mRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold15mRLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMResetThreshold15mRLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMTLTS1Threshold"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold15mTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMResetThreshold15mTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold15mTLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMResetThreshold15mTLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold24hRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold24hRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold24hRLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold24hTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMSetThreshold24hTLTM"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMStatus"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMView"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent24hElapsedTime"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent24hRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent24hRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent24hRLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent24hRLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent24hTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent24hTLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent24hTLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval24hRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval24hRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval24hRLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval24hRLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval24hTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval24hTLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval24hTLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval24hValidData"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent15mElapsedTime"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent15mRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent15mRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent15mRLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent15mRLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent15mTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent15mTLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMCurrent15mTLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mIntervalNumber"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mRLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mRLTS2"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mRLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mRLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mTLTS1"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mTLMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mTLMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRFPMInterval15mValidData"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent24hElapsedTime"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent24hMSEMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent24hMSEMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent24hXPIMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent24hXPIMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval24hMSEMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval24hMSEMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval24hXPIMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval24hXPIMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval24hValidData"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent15mElapsedTime"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent15mMSEMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent15mMSEMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent15mXPIMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMCurrent15mXPIMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval15mIntervalNumber"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval15mMSEMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval15mMSEMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval15mXPIMin"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval15mXPIMax"),
        ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfExtRAUPMInterval15mValidData"))
)
if mibBuilder.loadTexts:
    xfRadioLinkPtpTerminalCompleteGroup.setStatus("current")

xfRadioLinkPtpTerminalObsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 2, 2, 2)
)
xfRadioLinkPtpTerminalObsoleteGroup.setObjects(
    ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfTermSpectrumEfficiencyClassObsolete")
)
if mibBuilder.loadTexts:
    xfRadioLinkPtpTerminalObsoleteGroup.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xfRadioLinkPtpTerminalFullCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 193, 81, 3, 4, 1, 2, 1, 1)
)
xfRadioLinkPtpTerminalFullCompliance.setObjects(
    ("XF-RADIOLINK-PTP-TERMINAL-MIB", "xfRadioLinkPtpTerminalCompleteGroup")
)
if mibBuilder.loadTexts:
    xfRadioLinkPtpTerminalFullCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "XF-RADIOLINK-PTP-TERMINAL-MIB",
    **{"TermAdaptiveManualMode": TermAdaptiveManualMode,
       "TermModulation": TermModulation,
       "TermOutputPowerStatus": TermOutputPowerStatus,
       "ChannelMode": ChannelMode,
       "TermRauSec": TermRauSec,
       "TermAutoRemoveLoopEnable": TermAutoRemoveLoopEnable,
       "xfRadioLinkPtpTerminalMIB": xfRadioLinkPtpTerminalMIB,
       "xfRadioLinkPtpTerminalObjects": xfRadioLinkPtpTerminalObjects,
       "xfRLPtpTerminalTable": xfRLPtpTerminalTable,
       "xfRLPtpTerminalEntry": xfRLPtpTerminalEntry,
       "xfTermId": xfTermId,
       "xfTermType": xfTermType,
       "xfTermProtection": xfTermProtection,
       "xfTermCapacity": xfTermCapacity,
       "xfTermCapacityCapability": xfTermCapacityCapability,
       "xfTermModulation": xfTermModulation,
       "xfTermModulationCapability": xfTermModulationCapability,
       "xfTermRestore": xfTermRestore,
       "xfTermAlarmSeverity": xfTermAlarmSeverity,
       "xfTermTrapEnable": xfTermTrapEnable,
       "xfTermAsPort": xfTermAsPort,
       "xfTermRemoteIdCheck": xfTermRemoteIdCheck,
       "xfTermRemoteId": xfTermRemoteId,
       "xfTermPreset": xfTermPreset,
       "xfTermBerAlarmThreshold": xfTermBerAlarmThreshold,
       "xfTermFadeNotificationTimer": xfTermFadeNotificationTimer,
       "xfTermEquipmentProtectionIndex": xfTermEquipmentProtectionIndex,
       "xfTermSysName": xfTermSysName,
       "xfTermChannelMode": xfTermChannelMode,
       "xfTermChannelModeCapability": xfTermChannelModeCapability,
       "xfTermTrafficAndDCN": xfTermTrafficAndDCN,
       "xfTermFrameFormat": xfTermFrameFormat,
       "xfTermFrameFormatCapability": xfTermFrameFormatCapability,
       "xfTermDCNRadioConfiguration": xfTermDCNRadioConfiguration,
       "xfTermDCNRadioCapability": xfTermDCNRadioCapability,
       "xfTermDCNLineConfiguration": xfTermDCNLineConfiguration,
       "xfTermDCNLineCapability": xfTermDCNLineCapability,
       "xfTermFadeNotificationConfiguration": xfTermFadeNotificationConfiguration,
       "xfTermLineProtection": xfTermLineProtection,
       "xfRLPtpTerminalOutputPowerTable": xfRLPtpTerminalOutputPowerTable,
       "xfRLPtpTerminalOutputPowerEntry": xfRLPtpTerminalOutputPowerEntry,
       "xfTermOutputPowerOperStatus": xfTermOutputPowerOperStatus,
       "xfTermOutputPowerAdminStatus": xfTermOutputPowerAdminStatus,
       "xfTermAtpcCapability": xfTermAtpcCapability,
       "xfRLPtpTerminalPerformanceTable": xfRLPtpTerminalPerformanceTable,
       "xfRLPtpTerminalPerformanceEntry": xfRLPtpTerminalPerformanceEntry,
       "xfTermTimeElapsed": xfTermTimeElapsed,
       "xfTermCurrentES": xfTermCurrentES,
       "xfTermCurrentSES": xfTermCurrentSES,
       "xfTermCurrentBBE": xfTermCurrentBBE,
       "xfTermCurrentUAS": xfTermCurrentUAS,
       "xfTermCurrentBB": xfTermCurrentBB,
       "xfTermPerfReset": xfTermPerfReset,
       "xfTermTimeElapsedEnRLBExt": xfTermTimeElapsedEnRLBExt,
       "xfRLProtectionTable": xfRLProtectionTable,
       "xfRLProtectionEntry": xfRLProtectionEntry,
       "xfRLProtectionMode": xfRLProtectionMode,
       "xfRLProtectionRau1": xfRLProtectionRau1,
       "xfRLProtectionRau2": xfRLProtectionRau2,
       "xfRLActiveTxRadio": xfRLActiveTxRadio,
       "xfRLSwitchOverReset": xfRLSwitchOverReset,
       "xfRLSwitchRevertiveTx": xfRLSwitchRevertiveTx,
       "xfRLProtectionCapability": xfRLProtectionCapability,
       "xfRLTxSwitchOverConfiguration": xfRLTxSwitchOverConfiguration,
       "xfRLLineProtectionTable": xfRLLineProtectionTable,
       "xfRLLineProtectionEntry": xfRLLineProtectionEntry,
       "xfRLLineProtectionStatus": xfRLLineProtectionStatus,
       "xfRLLineProtectionMode": xfRLLineProtectionMode,
       "xfRADIORSTable": xfRADIORSTable,
       "xfRADIORSEntry": xfRADIORSEntry,
       "xfRADIORSAlarms": xfRADIORSAlarms,
       "xfRADIORSPerformanceTable": xfRADIORSPerformanceTable,
       "xfRADIORSPerformanceEntry": xfRADIORSPerformanceEntry,
       "xfRADIORSPerformanceAlarms": xfRADIORSPerformanceAlarms,
       "xfRLPMConfigTable": xfRLPMConfigTable,
       "xfRLPMConfigEntry": xfRLPMConfigEntry,
       "xfPMSetThreshold15mESs": xfPMSetThreshold15mESs,
       "xfPMSetThreshold15mSESs": xfPMSetThreshold15mSESs,
       "xfPMSetThreshold15mBBEs": xfPMSetThreshold15mBBEs,
       "xfPMResetThreshold15mESs": xfPMResetThreshold15mESs,
       "xfPMResetThreshold15mSESs": xfPMResetThreshold15mSESs,
       "xfPMResetThreshold15mBBEs": xfPMResetThreshold15mBBEs,
       "xfPMSetThreshold24hESs": xfPMSetThreshold24hESs,
       "xfPMSetThreshold24hSESs": xfPMSetThreshold24hSESs,
       "xfPMSetThreshold24hBBEs": xfPMSetThreshold24hBBEs,
       "xfPMView": xfPMView,
       "xfPMStatus": xfPMStatus,
       "xfPMRLTS1Threshold": xfPMRLTS1Threshold,
       "xfPMSetThreshold15mRLTS1": xfPMSetThreshold15mRLTS1,
       "xfPMResetThreshold15mRLTS1": xfPMResetThreshold15mRLTS1,
       "xfPMRLTS2Threshold": xfPMRLTS2Threshold,
       "xfPMSetThreshold15mRLTS2": xfPMSetThreshold15mRLTS2,
       "xfPMResetThreshold15mRLTS2": xfPMResetThreshold15mRLTS2,
       "xfPMSetThreshold15mRLTM": xfPMSetThreshold15mRLTM,
       "xfPMResetThreshold15mRLTM": xfPMResetThreshold15mRLTM,
       "xfPMTLTS1Threshold": xfPMTLTS1Threshold,
       "xfPMSetThreshold15mTLTS1": xfPMSetThreshold15mTLTS1,
       "xfPMResetThreshold15mTLTS1": xfPMResetThreshold15mTLTS1,
       "xfPMSetThreshold15mTLTM": xfPMSetThreshold15mTLTM,
       "xfPMResetThreshold15mTLTM": xfPMResetThreshold15mTLTM,
       "xfPMSetThreshold24hRLTS1": xfPMSetThreshold24hRLTS1,
       "xfPMSetThreshold24hRLTS2": xfPMSetThreshold24hRLTS2,
       "xfPMSetThreshold24hRLTM": xfPMSetThreshold24hRLTM,
       "xfPMSetThreshold24hTLTS1": xfPMSetThreshold24hTLTS1,
       "xfPMSetThreshold24hTLTM": xfPMSetThreshold24hTLTM,
       "xfRLPMCurrent24hTable": xfRLPMCurrent24hTable,
       "xfRLPMCurrent24hEntry": xfRLPMCurrent24hEntry,
       "xfPMCurrent24hTimeElapsed": xfPMCurrent24hTimeElapsed,
       "xfPMCurrent24hESs": xfPMCurrent24hESs,
       "xfPMCurrent24hSESs": xfPMCurrent24hSESs,
       "xfPMCurrent24hBBEs": xfPMCurrent24hBBEs,
       "xfPMCurrent24hUASs": xfPMCurrent24hUASs,
       "xfPMCurrent24hBBs": xfPMCurrent24hBBs,
       "xfPMCurrent24hRLTS1": xfPMCurrent24hRLTS1,
       "xfPMCurrent24hRLTS2": xfPMCurrent24hRLTS2,
       "xfPMCurrent24hRLMin": xfPMCurrent24hRLMin,
       "xfPMCurrent24hRLMax": xfPMCurrent24hRLMax,
       "xfPMCurrent24hTLTS1": xfPMCurrent24hTLTS1,
       "xfPMCurrent24hTLMin": xfPMCurrent24hTLMin,
       "xfPMCurrent24hTLMax": xfPMCurrent24hTLMax,
       "xfPMCurrent24hMSEMin": xfPMCurrent24hMSEMin,
       "xfPMCurrent24hMSEMax": xfPMCurrent24hMSEMax,
       "xfPMCurrent24hXPIMin": xfPMCurrent24hXPIMin,
       "xfPMCurrent24hXPIMax": xfPMCurrent24hXPIMax,
       "xfPMCurrent24hESR": xfPMCurrent24hESR,
       "xfPMCurrent24hSESR": xfPMCurrent24hSESR,
       "xfPMCurrent24hBBER": xfPMCurrent24hBBER,
       "xfRLPMInterval24hTable": xfRLPMInterval24hTable,
       "xfRLPMInterval24hEntry": xfRLPMInterval24hEntry,
       "xfPMInterval24hESs": xfPMInterval24hESs,
       "xfPMInterval24hSESs": xfPMInterval24hSESs,
       "xfPMInterval24hBBEs": xfPMInterval24hBBEs,
       "xfPMInterval24hUASs": xfPMInterval24hUASs,
       "xfPMInterval24hBBs": xfPMInterval24hBBs,
       "xfPMInterval24hValidData": xfPMInterval24hValidData,
       "xfPMInterval24hRLTS1": xfPMInterval24hRLTS1,
       "xfPMInterval24hRLTS2": xfPMInterval24hRLTS2,
       "xfPMInterval24hRLMin": xfPMInterval24hRLMin,
       "xfPMInterval24hRLMax": xfPMInterval24hRLMax,
       "xfPMInterval24hTLTS1": xfPMInterval24hTLTS1,
       "xfPMInterval24hTLMin": xfPMInterval24hTLMin,
       "xfPMInterval24hTLMax": xfPMInterval24hTLMax,
       "xfPMInterval24hMSEMin": xfPMInterval24hMSEMin,
       "xfPMInterval24hMSEMax": xfPMInterval24hMSEMax,
       "xfPMInterval24hXPIMin": xfPMInterval24hXPIMin,
       "xfPMInterval24hXPIMax": xfPMInterval24hXPIMax,
       "xfRLPMCurrent15mTable": xfRLPMCurrent15mTable,
       "xfRLPMCurrent15mEntry": xfRLPMCurrent15mEntry,
       "xfPMCurrent15mElapsedTime": xfPMCurrent15mElapsedTime,
       "xfPMCurrent15mESs": xfPMCurrent15mESs,
       "xfPMCurrent15mSESs": xfPMCurrent15mSESs,
       "xfPMCurrent15mBBEs": xfPMCurrent15mBBEs,
       "xfPMCurrent15mUASs": xfPMCurrent15mUASs,
       "xfPMCurrent15mBBs": xfPMCurrent15mBBs,
       "xfPMCurrent15mRLTS1": xfPMCurrent15mRLTS1,
       "xfPMCurrent15mRLTS2": xfPMCurrent15mRLTS2,
       "xfPMCurrent15mRLMin": xfPMCurrent15mRLMin,
       "xfPMCurrent15mRLMax": xfPMCurrent15mRLMax,
       "xfPMCurrent15mTLTS1": xfPMCurrent15mTLTS1,
       "xfPMCurrent15mTLMin": xfPMCurrent15mTLMin,
       "xfPMCurrent15mTLMax": xfPMCurrent15mTLMax,
       "xfPMCurrent15mMSEMin": xfPMCurrent15mMSEMin,
       "xfPMCurrent15mMSEMax": xfPMCurrent15mMSEMax,
       "xfPMCurrent15mXPIMin": xfPMCurrent15mXPIMin,
       "xfPMCurrent15mXPIMax": xfPMCurrent15mXPIMax,
       "xfPMCurrent15mESR": xfPMCurrent15mESR,
       "xfPMCurrent15mSESR": xfPMCurrent15mSESR,
       "xfPMCurrent15mBBER": xfPMCurrent15mBBER,
       "xfRLPMInterval15mTable": xfRLPMInterval15mTable,
       "xfRLPMInterval15mEntry": xfRLPMInterval15mEntry,
       "xfPMInterval15mIntervalNumber": xfPMInterval15mIntervalNumber,
       "xfPMInterval15mESs": xfPMInterval15mESs,
       "xfPMInterval15mSESs": xfPMInterval15mSESs,
       "xfPMInterval15mBBEs": xfPMInterval15mBBEs,
       "xfPMInterval15mUASs": xfPMInterval15mUASs,
       "xfPMInterval15mBBs": xfPMInterval15mBBs,
       "xfPMInterval15mValidData": xfPMInterval15mValidData,
       "xfPMInterval15mRLTS1": xfPMInterval15mRLTS1,
       "xfPMInterval15mRLTS2": xfPMInterval15mRLTS2,
       "xfPMInterval15mRLMin": xfPMInterval15mRLMin,
       "xfPMInterval15mRLMax": xfPMInterval15mRLMax,
       "xfPMInterval15mTLTS1": xfPMInterval15mTLTS1,
       "xfPMInterval15mTLMin": xfPMInterval15mTLMin,
       "xfPMInterval15mTLMax": xfPMInterval15mTLMax,
       "xfPMInterval15mMSEMin": xfPMInterval15mMSEMin,
       "xfPMInterval15mMSEMax": xfPMInterval15mMSEMax,
       "xfPMInterval15mXPIMin": xfPMInterval15mXPIMin,
       "xfPMInterval15mXPIMax": xfPMInterval15mXPIMax,
       "xfRLPtpTerminalXTable": xfRLPtpTerminalXTable,
       "xfRLPtpTerminalXEntry": xfRLPtpTerminalXEntry,
       "xfTermInterfaces": xfTermInterfaces,
       "xfTermInterfacesCapability": xfTermInterfacesCapability,
       "xfTermChannelModeOperStatus": xfTermChannelModeOperStatus,
       "xfTermXPICRestore": xfTermXPICRestore,
       "xfTermTribCapacityActual": xfTermTribCapacityActual,
       "xfTermTribCapacityDesired": xfTermTribCapacityDesired,
       "xfTermBitPipeCapacity": xfTermBitPipeCapacity,
       "xfTermRowIndex": xfTermRowIndex,
       "xfTermCapabilitiesLastChange": xfTermCapabilitiesLastChange,
       "xfTermActualRowIndex": xfTermActualRowIndex,
       "xfTermMaxRowIndex": xfTermMaxRowIndex,
       "xfTermAdaptiveManualRowIndex": xfTermAdaptiveManualRowIndex,
       "xfTermAdaptiveManualMode": xfTermAdaptiveManualMode,
       "xfTermSpectrumEfficiencyClass": xfTermSpectrumEfficiencyClass,
       "xfTermSpectrumEfficiencyClassCapability": xfTermSpectrumEfficiencyClassCapability,
       "xfTermIpAddress": xfTermIpAddress,
       "xfTermProtectionCapability": xfTermProtectionCapability,
       "xfTermLineProtectionCapability": xfTermLineProtectionCapability,
       "xfTermTribAllocationActual": xfTermTribAllocationActual,
       "xfTermTribAllocationDesired": xfTermTribAllocationDesired,
       "xfTermAutoRemoveLoopEnable": xfTermAutoRemoveLoopEnable,
       "xfTermCapability": xfTermCapability,
       "xfTermCapacityLicense": xfTermCapacityLicense,
       "xfTermFadingRates": xfTermFadingRates,
       "xfTermFadingRatesCapability": xfTermFadingRatesCapability,
       "xfTermConfiguredBitPipeCapacity": xfTermConfiguredBitPipeCapacity,
       "xfTermTribCapacityConfigured": xfTermTribCapacityConfigured,
       "xfTermPacketMaxCapacity": xfTermPacketMaxCapacity,
       "xfTermPacketMinCapacity": xfTermPacketMinCapacity,
       "xfRlPtpTerminalCapabilityTable": xfRlPtpTerminalCapabilityTable,
       "xfRlPtpTerminalCapabilityEntry": xfRlPtpTerminalCapabilityEntry,
       "xfTermChannelSpacing": xfTermChannelSpacing,
       "xfTermChannelModulation": xfTermChannelModulation,
       "xfTermMaxTribCapacity": xfTermMaxTribCapacity,
       "xfTermDCNCapacity": xfTermDCNCapacity,
       "xfTermValidRow": xfTermValidRow,
       "xfTermMaxCapacity": xfTermMaxCapacity,
       "xfTermSpectrumEfficiencyClassObsolete": xfTermSpectrumEfficiencyClassObsolete,
       "xfTermFrameFormatType": xfTermFrameFormatType,
       "xfTermFrameFormatRev": xfTermFrameFormatRev,
       "xfTermBerAlarmThresholdCapability": xfTermBerAlarmThresholdCapability,
       "xfRLPMAMConfigTable": xfRLPMAMConfigTable,
       "xfRLPMAMConfigEntry": xfRLPMAMConfigEntry,
       "xfPMAMSetThreshold15m": xfPMAMSetThreshold15m,
       "xfPMAMSetThreshold24h": xfPMAMSetThreshold24h,
       "xfPMAMResetThreshold15m": xfPMAMResetThreshold15m,
       "xfPMAMStatus": xfPMAMStatus,
       "xfPMAMValidData": xfPMAMValidData,
       "xfRLPMAMCurrent24hTable": xfRLPMAMCurrent24hTable,
       "xfRLPMAMCurrent24hEntry": xfRLPMAMCurrent24hEntry,
       "xfPMAMCurrent24h4QAM": xfPMAMCurrent24h4QAM,
       "xfPMAMCurrent24h8QAM": xfPMAMCurrent24h8QAM,
       "xfPMAMCurrent24h16QAM": xfPMAMCurrent24h16QAM,
       "xfPMAMCurrent24h32QAM": xfPMAMCurrent24h32QAM,
       "xfPMAMCurrent24h64QAM": xfPMAMCurrent24h64QAM,
       "xfPMAMCurrent24h128QAM": xfPMAMCurrent24h128QAM,
       "xfPMAMCurrent24h256QAM": xfPMAMCurrent24h256QAM,
       "xfPMAMCurrent24h512QAM": xfPMAMCurrent24h512QAM,
       "xfPMAMCurrent24h1024QAM": xfPMAMCurrent24h1024QAM,
       "xfPMAMCurrent24h4QAMEnRLB": xfPMAMCurrent24h4QAMEnRLB,
       "xfPMAMCurrent24h8QAMEnRLB": xfPMAMCurrent24h8QAMEnRLB,
       "xfPMAMCurrent24h16QAMEnRLB": xfPMAMCurrent24h16QAMEnRLB,
       "xfPMAMCurrent24h32QAMEnRLB": xfPMAMCurrent24h32QAMEnRLB,
       "xfPMAMCurrent24h64QAMEnRLB": xfPMAMCurrent24h64QAMEnRLB,
       "xfPMAMCurrent24h128QAMEnRLB": xfPMAMCurrent24h128QAMEnRLB,
       "xfPMAMCurrent24h256QAMEnRLB": xfPMAMCurrent24h256QAMEnRLB,
       "xfPMAMCurrent24h512QAMEnRLB": xfPMAMCurrent24h512QAMEnRLB,
       "xfPMAMCurrent24h1024QAMEnRLB": xfPMAMCurrent24h1024QAMEnRLB,
       "xfRLPMAMInterval24hTable": xfRLPMAMInterval24hTable,
       "xfRLPMAMInterval24hEntry": xfRLPMAMInterval24hEntry,
       "xfPMAMInterval24h4QAM": xfPMAMInterval24h4QAM,
       "xfPMAMInterval24h8QAM": xfPMAMInterval24h8QAM,
       "xfPMAMInterval24h16QAM": xfPMAMInterval24h16QAM,
       "xfPMAMInterval24h32QAM": xfPMAMInterval24h32QAM,
       "xfPMAMInterval24h64QAM": xfPMAMInterval24h64QAM,
       "xfPMAMInterval24h128QAM": xfPMAMInterval24h128QAM,
       "xfPMAMInterval24h256QAM": xfPMAMInterval24h256QAM,
       "xfPMAMInterval24h512QAM": xfPMAMInterval24h512QAM,
       "xfPMAMInterval24hValidData": xfPMAMInterval24hValidData,
       "xfPMAMInterval24h1024QAM": xfPMAMInterval24h1024QAM,
       "xfPMAMInterval24h4QAMEnRLB": xfPMAMInterval24h4QAMEnRLB,
       "xfPMAMInterval24h8QAMEnRLB": xfPMAMInterval24h8QAMEnRLB,
       "xfPMAMInterval24h16QAMEnRLB": xfPMAMInterval24h16QAMEnRLB,
       "xfPMAMInterval24h32QAMEnRLB": xfPMAMInterval24h32QAMEnRLB,
       "xfPMAMInterval24h64QAMEnRLB": xfPMAMInterval24h64QAMEnRLB,
       "xfPMAMInterval24h128QAMEnRLB": xfPMAMInterval24h128QAMEnRLB,
       "xfPMAMInterval24h256QAMEnRLB": xfPMAMInterval24h256QAMEnRLB,
       "xfPMAMInterval24h512QAMEnRLB": xfPMAMInterval24h512QAMEnRLB,
       "xfPMAMInterval24h1024QAMEnRLB": xfPMAMInterval24h1024QAMEnRLB,
       "xfRLPMAMCurrent15mTable": xfRLPMAMCurrent15mTable,
       "xfRLPMAMCurrent15mEntry": xfRLPMAMCurrent15mEntry,
       "xfPMAMCurrent15m4QAM": xfPMAMCurrent15m4QAM,
       "xfPMAMCurrent15m8QAM": xfPMAMCurrent15m8QAM,
       "xfPMAMCurrent15m16QAM": xfPMAMCurrent15m16QAM,
       "xfPMAMCurrent15m32QAM": xfPMAMCurrent15m32QAM,
       "xfPMAMCurrent15m64QAM": xfPMAMCurrent15m64QAM,
       "xfPMAMCurrent15m128QAM": xfPMAMCurrent15m128QAM,
       "xfPMAMCurrent15m256QAM": xfPMAMCurrent15m256QAM,
       "xfPMAMCurrent15m512QAM": xfPMAMCurrent15m512QAM,
       "xfPMAMCurrent15m1024QAM": xfPMAMCurrent15m1024QAM,
       "xfPMAMCurrent15m4QAMEnRLB": xfPMAMCurrent15m4QAMEnRLB,
       "xfPMAMCurrent15m8QAMEnRLB": xfPMAMCurrent15m8QAMEnRLB,
       "xfPMAMCurrent15m16QAMEnRLB": xfPMAMCurrent15m16QAMEnRLB,
       "xfPMAMCurrent15m32QAMEnRLB": xfPMAMCurrent15m32QAMEnRLB,
       "xfPMAMCurrent15m64QAMEnRLB": xfPMAMCurrent15m64QAMEnRLB,
       "xfPMAMCurrent15m128QAMEnRLB": xfPMAMCurrent15m128QAMEnRLB,
       "xfPMAMCurrent15m256QAMEnRLB": xfPMAMCurrent15m256QAMEnRLB,
       "xfPMAMCurrent15m512QAMEnRLB": xfPMAMCurrent15m512QAMEnRLB,
       "xfPMAMCurrent15m1024QAMEnRLB": xfPMAMCurrent15m1024QAMEnRLB,
       "xfRLPMAMInterval15mTable": xfRLPMAMInterval15mTable,
       "xfRLPMAMInterval15mEntry": xfRLPMAMInterval15mEntry,
       "xfPMAMInterval15mIntervalNumber": xfPMAMInterval15mIntervalNumber,
       "xfPMAMInterval15m4QAM": xfPMAMInterval15m4QAM,
       "xfPMAMInterval15m8QAM": xfPMAMInterval15m8QAM,
       "xfPMAMInterval15m16QAM": xfPMAMInterval15m16QAM,
       "xfPMAMInterval15m32QAM": xfPMAMInterval15m32QAM,
       "xfPMAMInterval15m64QAM": xfPMAMInterval15m64QAM,
       "xfPMAMInterval15m128QAM": xfPMAMInterval15m128QAM,
       "xfPMAMInterval15m256QAM": xfPMAMInterval15m256QAM,
       "xfPMAMInterval15m512QAM": xfPMAMInterval15m512QAM,
       "xfPMAMInterval15mValidData": xfPMAMInterval15mValidData,
       "xfPMAMInterval15m1024QAM": xfPMAMInterval15m1024QAM,
       "xfPMAMInterval15m4QAMEnRLB": xfPMAMInterval15m4QAMEnRLB,
       "xfPMAMInterval15m8QAMEnRLB": xfPMAMInterval15m8QAMEnRLB,
       "xfPMAMInterval15m16QAMEnRLB": xfPMAMInterval15m16QAMEnRLB,
       "xfPMAMInterval15m32QAMEnRLB": xfPMAMInterval15m32QAMEnRLB,
       "xfPMAMInterval15m64QAMEnRLB": xfPMAMInterval15m64QAMEnRLB,
       "xfPMAMInterval15m128QAMEnRLB": xfPMAMInterval15m128QAMEnRLB,
       "xfPMAMInterval15m256QAMEnRLB": xfPMAMInterval15m256QAMEnRLB,
       "xfPMAMInterval15m512QAMEnRLB": xfPMAMInterval15m512QAMEnRLB,
       "xfPMAMInterval15m1024QAMEnRLB": xfPMAMInterval15m1024QAMEnRLB,
       "xfRLPtpTerminalCapacityLicenseTable": xfRLPtpTerminalCapacityLicenseTable,
       "xfRLPtpTerminalCapacityLicenseEntry": xfRLPtpTerminalCapacityLicenseEntry,
       "xfTermCapacityLicenseRange": xfTermCapacityLicenseRange,
       "xfTermMaxCapacityRange": xfTermMaxCapacityRange,
       "xfTermMaxTribCapacityRange": xfTermMaxTribCapacityRange,
       "xfRLPMSDCGainCurrent15mTable": xfRLPMSDCGainCurrent15mTable,
       "xfRLPMSDCGainCurrent15mEntry": xfRLPMSDCGainCurrent15mEntry,
       "xfPMSDCGainCurrent15m0005dB": xfPMSDCGainCurrent15m0005dB,
       "xfPMSDCGainCurrent15m0510dB": xfPMSDCGainCurrent15m0510dB,
       "xfPMSDCGainCurrent15m1015dB": xfPMSDCGainCurrent15m1015dB,
       "xfPMSDCGainCurrent15m1520dB": xfPMSDCGainCurrent15m1520dB,
       "xfPMSDCGainCurrent15m2025dB": xfPMSDCGainCurrent15m2025dB,
       "xfPMSDCGainCurrent15m2530dB": xfPMSDCGainCurrent15m2530dB,
       "xfRLPMSDCGainInterval15mTable": xfRLPMSDCGainInterval15mTable,
       "xfRLPMSDCGainInterval15mEntry": xfRLPMSDCGainInterval15mEntry,
       "xfPMSDCGainInterval15mIntervalNumber": xfPMSDCGainInterval15mIntervalNumber,
       "xfPMSDCGainInterval15m0005dB": xfPMSDCGainInterval15m0005dB,
       "xfPMSDCGainInterval15m0510dB": xfPMSDCGainInterval15m0510dB,
       "xfPMSDCGainInterval15m1015dB": xfPMSDCGainInterval15m1015dB,
       "xfPMSDCGainInterval15m1520dB": xfPMSDCGainInterval15m1520dB,
       "xfPMSDCGainInterval15m2025dB": xfPMSDCGainInterval15m2025dB,
       "xfPMSDCGainInterval15m2530dB": xfPMSDCGainInterval15m2530dB,
       "xfRLPMSDCGainCurrent24hTable": xfRLPMSDCGainCurrent24hTable,
       "xfRLPMSDCGainCurrent24hEntry": xfRLPMSDCGainCurrent24hEntry,
       "xfPMSDCGainCurrent24h0005dB": xfPMSDCGainCurrent24h0005dB,
       "xfPMSDCGainCurrent24h0510dB": xfPMSDCGainCurrent24h0510dB,
       "xfPMSDCGainCurrent24h1015dB": xfPMSDCGainCurrent24h1015dB,
       "xfPMSDCGainCurrent24h1520dB": xfPMSDCGainCurrent24h1520dB,
       "xfPMSDCGainCurrent24h2025dB": xfPMSDCGainCurrent24h2025dB,
       "xfPMSDCGainCurrent24h2530dB": xfPMSDCGainCurrent24h2530dB,
       "xfRLPMSDCGainInterval24hTable": xfRLPMSDCGainInterval24hTable,
       "xfRLPMSDCGainInterval24hEntry": xfRLPMSDCGainInterval24hEntry,
       "xfPMSDCGainInterval24h0005dB": xfPMSDCGainInterval24h0005dB,
       "xfPMSDCGainInterval24h0510dB": xfPMSDCGainInterval24h0510dB,
       "xfPMSDCGainInterval24h1015dB": xfPMSDCGainInterval24h1015dB,
       "xfPMSDCGainInterval24h1520dB": xfPMSDCGainInterval24h1520dB,
       "xfPMSDCGainInterval24h2025dB": xfPMSDCGainInterval24h2025dB,
       "xfPMSDCGainInterval24h2530dB": xfPMSDCGainInterval24h2530dB,
       "xfRLPMSDCGainConfigTable": xfRLPMSDCGainConfigTable,
       "xfRLPMSDCGainConfigEntry": xfRLPMSDCGainConfigEntry,
       "xfPMSDCGainSetThreshold15m": xfPMSDCGainSetThreshold15m,
       "xfPMSDCGainSetThreshold24h": xfPMSDCGainSetThreshold24h,
       "xfPMSDCGainResetThreshold15m": xfPMSDCGainResetThreshold15m,
       "xfPMSDCGainStatus": xfPMSDCGainStatus,
       "xfRLExtRFPMConfigTable": xfRLExtRFPMConfigTable,
       "xfRLExtRFPMConfigEntry": xfRLExtRFPMConfigEntry,
       "xfExtRFPMRLTS1Threshold": xfExtRFPMRLTS1Threshold,
       "xfExtRFPMSetThreshold15mRLTS1": xfExtRFPMSetThreshold15mRLTS1,
       "xfExtRFPMResetThreshold15mRLTS1": xfExtRFPMResetThreshold15mRLTS1,
       "xfExtRFPMRLTS2Threshold": xfExtRFPMRLTS2Threshold,
       "xfExtRFPMSetThreshold15mRLTS2": xfExtRFPMSetThreshold15mRLTS2,
       "xfExtRFPMResetThreshold15mRLTS2": xfExtRFPMResetThreshold15mRLTS2,
       "xfExtRFPMSetThreshold15mRLTM": xfExtRFPMSetThreshold15mRLTM,
       "xfExtRFPMResetThreshold15mRLTM": xfExtRFPMResetThreshold15mRLTM,
       "xfExtRFPMTLTS1Threshold": xfExtRFPMTLTS1Threshold,
       "xfExtRFPMSetThreshold15mTLTS1": xfExtRFPMSetThreshold15mTLTS1,
       "xfExtRFPMResetThreshold15mTLTS1": xfExtRFPMResetThreshold15mTLTS1,
       "xfExtRFPMSetThreshold15mTLTM": xfExtRFPMSetThreshold15mTLTM,
       "xfExtRFPMResetThreshold15mTLTM": xfExtRFPMResetThreshold15mTLTM,
       "xfExtRFPMSetThreshold24hRLTS1": xfExtRFPMSetThreshold24hRLTS1,
       "xfExtRFPMSetThreshold24hRLTS2": xfExtRFPMSetThreshold24hRLTS2,
       "xfExtRFPMSetThreshold24hRLTM": xfExtRFPMSetThreshold24hRLTM,
       "xfExtRFPMSetThreshold24hTLTS1": xfExtRFPMSetThreshold24hTLTS1,
       "xfExtRFPMSetThreshold24hTLTM": xfExtRFPMSetThreshold24hTLTM,
       "xfExtRFPMStatus": xfExtRFPMStatus,
       "xfExtRFPMView": xfExtRFPMView,
       "xfRLExtRFPMCurrent24hTable": xfRLExtRFPMCurrent24hTable,
       "xfRLExtRFPMCurrent24hEntry": xfRLExtRFPMCurrent24hEntry,
       "xfExtRFPMCurrent24hElapsedTime": xfExtRFPMCurrent24hElapsedTime,
       "xfExtRFPMCurrent24hRLTS1": xfExtRFPMCurrent24hRLTS1,
       "xfExtRFPMCurrent24hRLTS2": xfExtRFPMCurrent24hRLTS2,
       "xfExtRFPMCurrent24hRLMin": xfExtRFPMCurrent24hRLMin,
       "xfExtRFPMCurrent24hRLMax": xfExtRFPMCurrent24hRLMax,
       "xfExtRFPMCurrent24hTLTS1": xfExtRFPMCurrent24hTLTS1,
       "xfExtRFPMCurrent24hTLMin": xfExtRFPMCurrent24hTLMin,
       "xfExtRFPMCurrent24hTLMax": xfExtRFPMCurrent24hTLMax,
       "xfRLExtRFPMInterval24hTable": xfRLExtRFPMInterval24hTable,
       "xfRLExtRFPMInterval24hEntry": xfRLExtRFPMInterval24hEntry,
       "xfExtRFPMInterval24hRLTS1": xfExtRFPMInterval24hRLTS1,
       "xfExtRFPMInterval24hRLTS2": xfExtRFPMInterval24hRLTS2,
       "xfExtRFPMInterval24hRLMin": xfExtRFPMInterval24hRLMin,
       "xfExtRFPMInterval24hRLMax": xfExtRFPMInterval24hRLMax,
       "xfExtRFPMInterval24hTLTS1": xfExtRFPMInterval24hTLTS1,
       "xfExtRFPMInterval24hTLMin": xfExtRFPMInterval24hTLMin,
       "xfExtRFPMInterval24hTLMax": xfExtRFPMInterval24hTLMax,
       "xfExtRFPMInterval24hValidData": xfExtRFPMInterval24hValidData,
       "xfRLExtRFPMCurrent15mTable": xfRLExtRFPMCurrent15mTable,
       "xfRLExtRFPMCurrent15mEntry": xfRLExtRFPMCurrent15mEntry,
       "xfExtRFPMCurrent15mElapsedTime": xfExtRFPMCurrent15mElapsedTime,
       "xfExtRFPMCurrent15mRLTS1": xfExtRFPMCurrent15mRLTS1,
       "xfExtRFPMCurrent15mRLTS2": xfExtRFPMCurrent15mRLTS2,
       "xfExtRFPMCurrent15mRLMin": xfExtRFPMCurrent15mRLMin,
       "xfExtRFPMCurrent15mRLMax": xfExtRFPMCurrent15mRLMax,
       "xfExtRFPMCurrent15mTLTS1": xfExtRFPMCurrent15mTLTS1,
       "xfExtRFPMCurrent15mTLMin": xfExtRFPMCurrent15mTLMin,
       "xfExtRFPMCurrent15mTLMax": xfExtRFPMCurrent15mTLMax,
       "xfRLExtRFPMInterval15mTable": xfRLExtRFPMInterval15mTable,
       "xfRLExtRFPMInterval15mEntry": xfRLExtRFPMInterval15mEntry,
       "xfExtRFPMInterval15mIntervalNumber": xfExtRFPMInterval15mIntervalNumber,
       "xfExtRFPMInterval15mRLTS1": xfExtRFPMInterval15mRLTS1,
       "xfExtRFPMInterval15mRLTS2": xfExtRFPMInterval15mRLTS2,
       "xfExtRFPMInterval15mRLMin": xfExtRFPMInterval15mRLMin,
       "xfExtRFPMInterval15mRLMax": xfExtRFPMInterval15mRLMax,
       "xfExtRFPMInterval15mTLTS1": xfExtRFPMInterval15mTLTS1,
       "xfExtRFPMInterval15mTLMin": xfExtRFPMInterval15mTLMin,
       "xfExtRFPMInterval15mTLMax": xfExtRFPMInterval15mTLMax,
       "xfExtRFPMInterval15mValidData": xfExtRFPMInterval15mValidData,
       "xfRLExtRAUPMCurrent24hTable": xfRLExtRAUPMCurrent24hTable,
       "xfRLExtRAUPMCurrent24hEntry": xfRLExtRAUPMCurrent24hEntry,
       "xfExtRAUPMCurrent24hElapsedTime": xfExtRAUPMCurrent24hElapsedTime,
       "xfExtRAUPMCurrent24hMSEMin": xfExtRAUPMCurrent24hMSEMin,
       "xfExtRAUPMCurrent24hMSEMax": xfExtRAUPMCurrent24hMSEMax,
       "xfExtRAUPMCurrent24hXPIMin": xfExtRAUPMCurrent24hXPIMin,
       "xfExtRAUPMCurrent24hXPIMax": xfExtRAUPMCurrent24hXPIMax,
       "xfRLExtRAUPMInterval24hTable": xfRLExtRAUPMInterval24hTable,
       "xfRLExtRAUPMInterval24hEntry": xfRLExtRAUPMInterval24hEntry,
       "xfExtRAUPMInterval24hMSEMin": xfExtRAUPMInterval24hMSEMin,
       "xfExtRAUPMInterval24hMSEMax": xfExtRAUPMInterval24hMSEMax,
       "xfExtRAUPMInterval24hXPIMin": xfExtRAUPMInterval24hXPIMin,
       "xfExtRAUPMInterval24hXPIMax": xfExtRAUPMInterval24hXPIMax,
       "xfExtRAUPMInterval24hValidData": xfExtRAUPMInterval24hValidData,
       "xfRLExtRAUPMCurrent15mTable": xfRLExtRAUPMCurrent15mTable,
       "xfRLExtRAUPMCurrent15mEntry": xfRLExtRAUPMCurrent15mEntry,
       "xfExtRAUPMCurrent15mElapsedTime": xfExtRAUPMCurrent15mElapsedTime,
       "xfExtRAUPMCurrent15mMSEMin": xfExtRAUPMCurrent15mMSEMin,
       "xfExtRAUPMCurrent15mMSEMax": xfExtRAUPMCurrent15mMSEMax,
       "xfExtRAUPMCurrent15mXPIMin": xfExtRAUPMCurrent15mXPIMin,
       "xfExtRAUPMCurrent15mXPIMax": xfExtRAUPMCurrent15mXPIMax,
       "xfRLExtRAUPMInterval15mTable": xfRLExtRAUPMInterval15mTable,
       "xfRLExtRAUPMInterval15mEntry": xfRLExtRAUPMInterval15mEntry,
       "xfExtRAUPMInterval15mIntervalNumber": xfExtRAUPMInterval15mIntervalNumber,
       "xfExtRAUPMInterval15mMSEMin": xfExtRAUPMInterval15mMSEMin,
       "xfExtRAUPMInterval15mMSEMax": xfExtRAUPMInterval15mMSEMax,
       "xfExtRAUPMInterval15mXPIMin": xfExtRAUPMInterval15mXPIMin,
       "xfExtRAUPMInterval15mXPIMax": xfExtRAUPMInterval15mXPIMax,
       "xfExtRAUPMInterval15mValidData": xfExtRAUPMInterval15mValidData,
       "xfRadioLinkPtpTerminalConformance": xfRadioLinkPtpTerminalConformance,
       "xfRadioLinkPtpTerminalCompliances": xfRadioLinkPtpTerminalCompliances,
       "xfRadioLinkPtpTerminalFullCompliance": xfRadioLinkPtpTerminalFullCompliance,
       "xfRadioLinkPtpTerminalGroups": xfRadioLinkPtpTerminalGroups,
       "xfRadioLinkPtpTerminalCompleteGroup": xfRadioLinkPtpTerminalCompleteGroup,
       "xfRadioLinkPtpTerminalObsoleteGroup": xfRadioLinkPtpTerminalObsoleteGroup}
)
