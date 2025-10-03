# SNMP MIB module (AT-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-PTP-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:35 2025
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

(AutonomousType,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "AutonomousType",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

atPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504)
)
if mibBuilder.loadTexts:
    atPtpMIB.setRevisions(
        ("2017-01-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PtpClockDomainType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PtpClockIdentity(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class PtpClockInstanceType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )



class PtpClockIntervalBase2(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )



class PtpClockMechanismType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              254)
        )
    )
    namedValues = NamedValues(
        *(("e2e", 1),
          ("p2p", 2),
          ("disabled", 254))
    )



class PtpClockPortNumber(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )



class PtpClockPortState(TextualConvention, Integer32):
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
        *(("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("preMaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )



class PtpClockPortTransportTypeAddress(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class PtpClockProfileType(TextualConvention, Integer32):
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
        *(("default", 1),
          ("telecom", 2),
          ("vendorspecific", 3))
    )



class PtpClockQualityAccuracyType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              254)
        )
    )
    namedValues = NamedValues(
        *(("nanoSecond25", 32),
          ("nanoSecond100", 33),
          ("nanoSecond250", 34),
          ("microSec1", 35),
          ("microSec2dot5", 36),
          ("microSec10", 37),
          ("microSec25", 38),
          ("microSec100", 39),
          ("microSec250", 40),
          ("milliSec1", 41),
          ("milliSec2dot5", 42),
          ("milliSec10", 43),
          ("milliSec25", 44),
          ("milliSec100", 45),
          ("milliSec250", 46),
          ("second1", 47),
          ("second10", 48),
          ("secondGreater10", 49),
          ("unknown", 254))
    )



class PtpClockQualityClassType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(6,
              7,
              13,
              14,
              52,
              58)
        )
    )
    namedValues = NamedValues(
        *(("clockclass6", 6),
          ("clockclass7", 7),
          ("clockclass13", 13),
          ("clockclass14", 14),
          ("clockclass52", 52),
          ("clockclass58", 58))
    )



class PtpClockRoleType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2))
    )



class PtpClockStateType(TextualConvention, Integer32):
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
        *(("freerun", 1),
          ("holdover", 2),
          ("acquiring", 3),
          ("frequencyLocked", 4),
          ("phaseAligned", 5))
    )



class PtpClockTimeInterval(TextualConvention, OctetString):
    status = "current"
    displayHint = "255a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )



class PtpClockTimeSourceType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              32,
              48,
              64,
              80,
              96,
              144,
              160)
        )
    )
    namedValues = NamedValues(
        *(("atomicClock", 16),
          ("gps", 32),
          ("terrestrialRadio", 48),
          ("ptp", 64),
          ("ntp", 80),
          ("handSet", 96),
          ("other", 144),
          ("internalOscillator", 160))
    )



class PtpClockTxModeType(TextualConvention, Integer32):
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
        *(("unicast", 1),
          ("multicast", 2),
          ("multicastmix", 3))
    )



class PtpClockType(TextualConvention, Integer32):
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
        *(("ordinaryClock", 1),
          ("boundaryClock", 2),
          ("transparentClock", 3),
          ("boundaryNode", 4))
    )



# MIB Managed Objects in the order of their OIDs

_PtpMIBNotifs_ObjectIdentity = ObjectIdentity
ptpMIBNotifs = _PtpMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 0)
)
_PtpMIBObjects_ObjectIdentity = ObjectIdentity
ptpMIBObjects = _PtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1)
)
_PtpMIBSystemInfo_ObjectIdentity = ObjectIdentity
ptpMIBSystemInfo = _PtpMIBSystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1)
)
_PtpSystemTable_Object = MibTable
ptpSystemTable = _PtpSystemTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ptpSystemTable.setStatus("current")
_PtpSystemEntry_Object = MibTableRow
ptpSystemEntry = _PtpSystemEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1, 1)
)
ptpSystemEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpDomainIndex"),
    (0, "AT-PTP-MIB", "ptpInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpSystemEntry.setStatus("current")
_PtpDomainIndex_Type = PtpClockDomainType
_PtpDomainIndex_Object = MibTableColumn
ptpDomainIndex = _PtpDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1, 1, 1),
    _PtpDomainIndex_Type()
)
ptpDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpDomainIndex.setStatus("current")
_PtpInstanceIndex_Type = PtpClockInstanceType
_PtpInstanceIndex_Object = MibTableColumn
ptpInstanceIndex = _PtpInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1, 1, 2),
    _PtpInstanceIndex_Type()
)
ptpInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpInstanceIndex.setStatus("current")
_PtpDomainClockPortsTotal_Type = Gauge32
_PtpDomainClockPortsTotal_Object = MibTableColumn
ptpDomainClockPortsTotal = _PtpDomainClockPortsTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 1, 1, 3),
    _PtpDomainClockPortsTotal_Type()
)
ptpDomainClockPortsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpDomainClockPortsTotal.setStatus("current")
if mibBuilder.loadTexts:
    ptpDomainClockPortsTotal.setUnits("ptp ports")
_PtpSystemDomainTable_Object = MibTable
ptpSystemDomainTable = _PtpSystemDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 2)
)
if mibBuilder.loadTexts:
    ptpSystemDomainTable.setStatus("current")
_PtpSystemDomainEntry_Object = MibTableRow
ptpSystemDomainEntry = _PtpSystemDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 2, 1)
)
ptpSystemDomainEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpSystemDomainClockTypeIndex"),
)
if mibBuilder.loadTexts:
    ptpSystemDomainEntry.setStatus("current")
_PtpSystemDomainClockTypeIndex_Type = PtpClockType
_PtpSystemDomainClockTypeIndex_Object = MibTableColumn
ptpSystemDomainClockTypeIndex = _PtpSystemDomainClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 2, 1, 1),
    _PtpSystemDomainClockTypeIndex_Type()
)
ptpSystemDomainClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpSystemDomainClockTypeIndex.setStatus("current")
_PtpSystemDomainTotals_Type = Unsigned32
_PtpSystemDomainTotals_Object = MibTableColumn
ptpSystemDomainTotals = _PtpSystemDomainTotals_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 2, 1, 2),
    _PtpSystemDomainTotals_Type()
)
ptpSystemDomainTotals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpSystemDomainTotals.setStatus("current")
if mibBuilder.loadTexts:
    ptpSystemDomainTotals.setUnits("domains")
_PtpSystemProfile_Type = PtpClockProfileType
_PtpSystemProfile_Object = MibScalar
ptpSystemProfile = _PtpSystemProfile_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 1, 3),
    _PtpSystemProfile_Type()
)
ptpSystemProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpSystemProfile.setStatus("current")
_PtpMIBClockInfo_ObjectIdentity = ObjectIdentity
ptpMIBClockInfo = _PtpMIBClockInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2)
)
_PtpClockCurrentDSTable_Object = MibTable
ptpClockCurrentDSTable = _PtpClockCurrentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1)
)
if mibBuilder.loadTexts:
    ptpClockCurrentDSTable.setStatus("current")
_PtpClockCurrentDSEntry_Object = MibTableRow
ptpClockCurrentDSEntry = _PtpClockCurrentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1)
)
ptpClockCurrentDSEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockCurrentDSDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockCurrentDSClockTypeIndex"),
    (0, "AT-PTP-MIB", "ptpClockCurrentDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpClockCurrentDSEntry.setStatus("current")
_PtpClockCurrentDSDomainIndex_Type = PtpClockDomainType
_PtpClockCurrentDSDomainIndex_Object = MibTableColumn
ptpClockCurrentDSDomainIndex = _PtpClockCurrentDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 1),
    _PtpClockCurrentDSDomainIndex_Type()
)
ptpClockCurrentDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockCurrentDSDomainIndex.setStatus("current")
_PtpClockCurrentDSClockTypeIndex_Type = PtpClockType
_PtpClockCurrentDSClockTypeIndex_Object = MibTableColumn
ptpClockCurrentDSClockTypeIndex = _PtpClockCurrentDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 2),
    _PtpClockCurrentDSClockTypeIndex_Type()
)
ptpClockCurrentDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockCurrentDSClockTypeIndex.setStatus("current")
_PtpClockCurrentDSInstanceIndex_Type = PtpClockInstanceType
_PtpClockCurrentDSInstanceIndex_Object = MibTableColumn
ptpClockCurrentDSInstanceIndex = _PtpClockCurrentDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 3),
    _PtpClockCurrentDSInstanceIndex_Type()
)
ptpClockCurrentDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockCurrentDSInstanceIndex.setStatus("current")
_PtpClockCurrentDSStepsRemoved_Type = Unsigned32
_PtpClockCurrentDSStepsRemoved_Object = MibTableColumn
ptpClockCurrentDSStepsRemoved = _PtpClockCurrentDSStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 4),
    _PtpClockCurrentDSStepsRemoved_Type()
)
ptpClockCurrentDSStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockCurrentDSStepsRemoved.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockCurrentDSStepsRemoved.setUnits("Steps")
_PtpClockCurrentDSOffsetFromMaster_Type = PtpClockTimeInterval
_PtpClockCurrentDSOffsetFromMaster_Object = MibTableColumn
ptpClockCurrentDSOffsetFromMaster = _PtpClockCurrentDSOffsetFromMaster_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 5),
    _PtpClockCurrentDSOffsetFromMaster_Type()
)
ptpClockCurrentDSOffsetFromMaster.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockCurrentDSOffsetFromMaster.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockCurrentDSOffsetFromMaster.setUnits("Time Interval")
_PtpClockCurrentDSMeanPathDelay_Type = PtpClockTimeInterval
_PtpClockCurrentDSMeanPathDelay_Object = MibTableColumn
ptpClockCurrentDSMeanPathDelay = _PtpClockCurrentDSMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 1, 1, 6),
    _PtpClockCurrentDSMeanPathDelay_Type()
)
ptpClockCurrentDSMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockCurrentDSMeanPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockCurrentDSMeanPathDelay.setUnits("Time Interval")
_PtpClockParentDSTable_Object = MibTable
ptpClockParentDSTable = _PtpClockParentDSTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ptpClockParentDSTable.setStatus("current")
_PtpClockParentDSEntry_Object = MibTableRow
ptpClockParentDSEntry = _PtpClockParentDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1)
)
ptpClockParentDSEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockParentDSDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockParentDSClockTypeIndex"),
    (0, "AT-PTP-MIB", "ptpClockParentDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpClockParentDSEntry.setStatus("current")
_PtpClockParentDSDomainIndex_Type = PtpClockDomainType
_PtpClockParentDSDomainIndex_Object = MibTableColumn
ptpClockParentDSDomainIndex = _PtpClockParentDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 1),
    _PtpClockParentDSDomainIndex_Type()
)
ptpClockParentDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockParentDSDomainIndex.setStatus("current")
_PtpClockParentDSClockTypeIndex_Type = PtpClockType
_PtpClockParentDSClockTypeIndex_Object = MibTableColumn
ptpClockParentDSClockTypeIndex = _PtpClockParentDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 2),
    _PtpClockParentDSClockTypeIndex_Type()
)
ptpClockParentDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockParentDSClockTypeIndex.setStatus("current")
_PtpClockParentDSInstanceIndex_Type = PtpClockInstanceType
_PtpClockParentDSInstanceIndex_Object = MibTableColumn
ptpClockParentDSInstanceIndex = _PtpClockParentDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 3),
    _PtpClockParentDSInstanceIndex_Type()
)
ptpClockParentDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockParentDSInstanceIndex.setStatus("current")


class _PtpClockParentDSParentPortIdentity_Type(OctetString):
    """Custom type ptpClockParentDSParentPortIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PtpClockParentDSParentPortIdentity_Type.__name__ = "OctetString"
_PtpClockParentDSParentPortIdentity_Object = MibTableColumn
ptpClockParentDSParentPortIdentity = _PtpClockParentDSParentPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 4),
    _PtpClockParentDSParentPortIdentity_Type()
)
ptpClockParentDSParentPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSParentPortIdentity.setStatus("current")
_PtpClockParentDSParentStats_Type = TruthValue
_PtpClockParentDSParentStats_Object = MibTableColumn
ptpClockParentDSParentStats = _PtpClockParentDSParentStats_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 5),
    _PtpClockParentDSParentStats_Type()
)
ptpClockParentDSParentStats.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSParentStats.setStatus("current")


class _PtpClockParentDSOffset_Type(PtpClockIntervalBase2):
    """Custom type ptpClockParentDSOffset based on PtpClockIntervalBase2"""
    subtypeSpec = PtpClockIntervalBase2.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-128, 127),
    )


_PtpClockParentDSOffset_Type.__name__ = "PtpClockIntervalBase2"
_PtpClockParentDSOffset_Object = MibTableColumn
ptpClockParentDSOffset = _PtpClockParentDSOffset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 6),
    _PtpClockParentDSOffset_Type()
)
ptpClockParentDSOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSOffset.setStatus("current")
_PtpClockParentDSClockPhChRate_Type = Integer32
_PtpClockParentDSClockPhChRate_Object = MibTableColumn
ptpClockParentDSClockPhChRate = _PtpClockParentDSClockPhChRate_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 7),
    _PtpClockParentDSClockPhChRate_Type()
)
ptpClockParentDSClockPhChRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSClockPhChRate.setStatus("current")
_PtpClockParentDSGMClockIdentity_Type = PtpClockIdentity
_PtpClockParentDSGMClockIdentity_Object = MibTableColumn
ptpClockParentDSGMClockIdentity = _PtpClockParentDSGMClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 8),
    _PtpClockParentDSGMClockIdentity_Type()
)
ptpClockParentDSGMClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSGMClockIdentity.setStatus("current")
_PtpClockParentDSGMClockPriority1_Type = Unsigned32
_PtpClockParentDSGMClockPriority1_Object = MibTableColumn
ptpClockParentDSGMClockPriority1 = _PtpClockParentDSGMClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 9),
    _PtpClockParentDSGMClockPriority1_Type()
)
ptpClockParentDSGMClockPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSGMClockPriority1.setStatus("current")
_PtpClockParentDSGMClockPriority2_Type = Unsigned32
_PtpClockParentDSGMClockPriority2_Object = MibTableColumn
ptpClockParentDSGMClockPriority2 = _PtpClockParentDSGMClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 10),
    _PtpClockParentDSGMClockPriority2_Type()
)
ptpClockParentDSGMClockPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSGMClockPriority2.setStatus("current")
_PtpClockParentDSGMClockQualityClass_Type = PtpClockQualityClassType
_PtpClockParentDSGMClockQualityClass_Object = MibTableColumn
ptpClockParentDSGMClockQualityClass = _PtpClockParentDSGMClockQualityClass_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 11),
    _PtpClockParentDSGMClockQualityClass_Type()
)
ptpClockParentDSGMClockQualityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSGMClockQualityClass.setStatus("current")
_PtpClockParentDSGMClockQualityAccuracy_Type = PtpClockQualityAccuracyType
_PtpClockParentDSGMClockQualityAccuracy_Object = MibTableColumn
ptpClockParentDSGMClockQualityAccuracy = _PtpClockParentDSGMClockQualityAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 12),
    _PtpClockParentDSGMClockQualityAccuracy_Type()
)
ptpClockParentDSGMClockQualityAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSGMClockQualityAccuracy.setStatus("current")
_PtpClockParentDSGMClockQualityOffset_Type = Unsigned32
_PtpClockParentDSGMClockQualityOffset_Object = MibTableColumn
ptpClockParentDSGMClockQualityOffset = _PtpClockParentDSGMClockQualityOffset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 2, 1, 13),
    _PtpClockParentDSGMClockQualityOffset_Type()
)
ptpClockParentDSGMClockQualityOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockParentDSGMClockQualityOffset.setStatus("current")
_PtpClockDefaultDSTable_Object = MibTable
ptpClockDefaultDSTable = _PtpClockDefaultDSTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3)
)
if mibBuilder.loadTexts:
    ptpClockDefaultDSTable.setStatus("current")
_PtpClockDefaultDSEntry_Object = MibTableRow
ptpClockDefaultDSEntry = _PtpClockDefaultDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1)
)
ptpClockDefaultDSEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockDefaultDSDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockDefaultDSClockTypeIndex"),
    (0, "AT-PTP-MIB", "ptpClockDefaultDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpClockDefaultDSEntry.setStatus("current")
_PtpClockDefaultDSDomainIndex_Type = PtpClockDomainType
_PtpClockDefaultDSDomainIndex_Object = MibTableColumn
ptpClockDefaultDSDomainIndex = _PtpClockDefaultDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 1),
    _PtpClockDefaultDSDomainIndex_Type()
)
ptpClockDefaultDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockDefaultDSDomainIndex.setStatus("current")
_PtpClockDefaultDSClockTypeIndex_Type = PtpClockType
_PtpClockDefaultDSClockTypeIndex_Object = MibTableColumn
ptpClockDefaultDSClockTypeIndex = _PtpClockDefaultDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 2),
    _PtpClockDefaultDSClockTypeIndex_Type()
)
ptpClockDefaultDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockDefaultDSClockTypeIndex.setStatus("current")
_PtpClockDefaultDSInstanceIndex_Type = PtpClockInstanceType
_PtpClockDefaultDSInstanceIndex_Object = MibTableColumn
ptpClockDefaultDSInstanceIndex = _PtpClockDefaultDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 3),
    _PtpClockDefaultDSInstanceIndex_Type()
)
ptpClockDefaultDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockDefaultDSInstanceIndex.setStatus("current")
_PtpClockDefaultDSTwoStepFlag_Type = TruthValue
_PtpClockDefaultDSTwoStepFlag_Object = MibTableColumn
ptpClockDefaultDSTwoStepFlag = _PtpClockDefaultDSTwoStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 4),
    _PtpClockDefaultDSTwoStepFlag_Type()
)
ptpClockDefaultDSTwoStepFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDefaultDSTwoStepFlag.setStatus("current")
_PtpClockDefaultDSClockIdentity_Type = PtpClockIdentity
_PtpClockDefaultDSClockIdentity_Object = MibTableColumn
ptpClockDefaultDSClockIdentity = _PtpClockDefaultDSClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 5),
    _PtpClockDefaultDSClockIdentity_Type()
)
ptpClockDefaultDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDefaultDSClockIdentity.setStatus("current")
_PtpClockDefaultDSPriority1_Type = Unsigned32
_PtpClockDefaultDSPriority1_Object = MibTableColumn
ptpClockDefaultDSPriority1 = _PtpClockDefaultDSPriority1_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 6),
    _PtpClockDefaultDSPriority1_Type()
)
ptpClockDefaultDSPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDefaultDSPriority1.setStatus("current")
_PtpClockDefaultDSPriority2_Type = Unsigned32
_PtpClockDefaultDSPriority2_Object = MibTableColumn
ptpClockDefaultDSPriority2 = _PtpClockDefaultDSPriority2_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 7),
    _PtpClockDefaultDSPriority2_Type()
)
ptpClockDefaultDSPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDefaultDSPriority2.setStatus("current")
_PtpClockDefaultDSSlaveOnly_Type = TruthValue
_PtpClockDefaultDSSlaveOnly_Object = MibTableColumn
ptpClockDefaultDSSlaveOnly = _PtpClockDefaultDSSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 8),
    _PtpClockDefaultDSSlaveOnly_Type()
)
ptpClockDefaultDSSlaveOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDefaultDSSlaveOnly.setStatus("current")
_PtpClockDefaultDSQualityClass_Type = PtpClockQualityClassType
_PtpClockDefaultDSQualityClass_Object = MibTableColumn
ptpClockDefaultDSQualityClass = _PtpClockDefaultDSQualityClass_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 9),
    _PtpClockDefaultDSQualityClass_Type()
)
ptpClockDefaultDSQualityClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDefaultDSQualityClass.setStatus("current")
_PtpClockDefaultDSQualityAccuracy_Type = PtpClockQualityAccuracyType
_PtpClockDefaultDSQualityAccuracy_Object = MibTableColumn
ptpClockDefaultDSQualityAccuracy = _PtpClockDefaultDSQualityAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 10),
    _PtpClockDefaultDSQualityAccuracy_Type()
)
ptpClockDefaultDSQualityAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDefaultDSQualityAccuracy.setStatus("current")
_PtpClockDefaultDSQualityOffset_Type = Integer32
_PtpClockDefaultDSQualityOffset_Object = MibTableColumn
ptpClockDefaultDSQualityOffset = _PtpClockDefaultDSQualityOffset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 3, 1, 11),
    _PtpClockDefaultDSQualityOffset_Type()
)
ptpClockDefaultDSQualityOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockDefaultDSQualityOffset.setStatus("current")
_PtpClockRunningTable_Object = MibTable
ptpClockRunningTable = _PtpClockRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4)
)
if mibBuilder.loadTexts:
    ptpClockRunningTable.setStatus("current")
_PtpClockRunningEntry_Object = MibTableRow
ptpClockRunningEntry = _PtpClockRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1)
)
ptpClockRunningEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockRunningDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockRunningClockTypeIndex"),
    (0, "AT-PTP-MIB", "ptpClockRunningInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpClockRunningEntry.setStatus("current")
_PtpClockRunningDomainIndex_Type = PtpClockDomainType
_PtpClockRunningDomainIndex_Object = MibTableColumn
ptpClockRunningDomainIndex = _PtpClockRunningDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 1),
    _PtpClockRunningDomainIndex_Type()
)
ptpClockRunningDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockRunningDomainIndex.setStatus("current")
_PtpClockRunningClockTypeIndex_Type = PtpClockType
_PtpClockRunningClockTypeIndex_Object = MibTableColumn
ptpClockRunningClockTypeIndex = _PtpClockRunningClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 2),
    _PtpClockRunningClockTypeIndex_Type()
)
ptpClockRunningClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockRunningClockTypeIndex.setStatus("current")
_PtpClockRunningInstanceIndex_Type = PtpClockInstanceType
_PtpClockRunningInstanceIndex_Object = MibTableColumn
ptpClockRunningInstanceIndex = _PtpClockRunningInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 3),
    _PtpClockRunningInstanceIndex_Type()
)
ptpClockRunningInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockRunningInstanceIndex.setStatus("current")
_PtpClockRunningState_Type = PtpClockStateType
_PtpClockRunningState_Object = MibTableColumn
ptpClockRunningState = _PtpClockRunningState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 4),
    _PtpClockRunningState_Type()
)
ptpClockRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockRunningState.setStatus("current")
_PtpClockRunningPacketsSent_Type = Counter64
_PtpClockRunningPacketsSent_Object = MibTableColumn
ptpClockRunningPacketsSent = _PtpClockRunningPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 5),
    _PtpClockRunningPacketsSent_Type()
)
ptpClockRunningPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockRunningPacketsSent.setStatus("current")
_PtpClockRunningPacketsReceived_Type = Counter64
_PtpClockRunningPacketsReceived_Object = MibTableColumn
ptpClockRunningPacketsReceived = _PtpClockRunningPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 4, 1, 6),
    _PtpClockRunningPacketsReceived_Type()
)
ptpClockRunningPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockRunningPacketsReceived.setStatus("current")
_PtpClockTimePropertiesDSTable_Object = MibTable
ptpClockTimePropertiesDSTable = _PtpClockTimePropertiesDSTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5)
)
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSTable.setStatus("current")
_PtpClockTimePropertiesDSEntry_Object = MibTableRow
ptpClockTimePropertiesDSEntry = _PtpClockTimePropertiesDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1)
)
ptpClockTimePropertiesDSEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockTimePropertiesDSDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockTimePropertiesDSClockTypeIndex"),
    (0, "AT-PTP-MIB", "ptpClockTimePropertiesDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSEntry.setStatus("current")
_PtpClockTimePropertiesDSDomainIndex_Type = PtpClockDomainType
_PtpClockTimePropertiesDSDomainIndex_Object = MibTableColumn
ptpClockTimePropertiesDSDomainIndex = _PtpClockTimePropertiesDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 1),
    _PtpClockTimePropertiesDSDomainIndex_Type()
)
ptpClockTimePropertiesDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSDomainIndex.setStatus("current")
_PtpClockTimePropertiesDSClockTypeIndex_Type = PtpClockType
_PtpClockTimePropertiesDSClockTypeIndex_Object = MibTableColumn
ptpClockTimePropertiesDSClockTypeIndex = _PtpClockTimePropertiesDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 2),
    _PtpClockTimePropertiesDSClockTypeIndex_Type()
)
ptpClockTimePropertiesDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSClockTypeIndex.setStatus("current")
_PtpClockTimePropertiesDSInstanceIndex_Type = PtpClockInstanceType
_PtpClockTimePropertiesDSInstanceIndex_Object = MibTableColumn
ptpClockTimePropertiesDSInstanceIndex = _PtpClockTimePropertiesDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 3),
    _PtpClockTimePropertiesDSInstanceIndex_Type()
)
ptpClockTimePropertiesDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSInstanceIndex.setStatus("current")
_PtpClockTimePropertiesDSCurrentUTCOffsetValid_Type = TruthValue
_PtpClockTimePropertiesDSCurrentUTCOffsetValid_Object = MibTableColumn
ptpClockTimePropertiesDSCurrentUTCOffsetValid = _PtpClockTimePropertiesDSCurrentUTCOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 4),
    _PtpClockTimePropertiesDSCurrentUTCOffsetValid_Type()
)
ptpClockTimePropertiesDSCurrentUTCOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSCurrentUTCOffsetValid.setStatus("current")
_PtpClockTimePropertiesDSCurrentUTCOffset_Type = Integer32
_PtpClockTimePropertiesDSCurrentUTCOffset_Object = MibTableColumn
ptpClockTimePropertiesDSCurrentUTCOffset = _PtpClockTimePropertiesDSCurrentUTCOffset_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 5),
    _PtpClockTimePropertiesDSCurrentUTCOffset_Type()
)
ptpClockTimePropertiesDSCurrentUTCOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSCurrentUTCOffset.setStatus("current")
_PtpClockTimePropertiesDSLeap59_Type = TruthValue
_PtpClockTimePropertiesDSLeap59_Object = MibTableColumn
ptpClockTimePropertiesDSLeap59 = _PtpClockTimePropertiesDSLeap59_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 6),
    _PtpClockTimePropertiesDSLeap59_Type()
)
ptpClockTimePropertiesDSLeap59.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSLeap59.setStatus("current")
_PtpClockTimePropertiesDSLeap61_Type = TruthValue
_PtpClockTimePropertiesDSLeap61_Object = MibTableColumn
ptpClockTimePropertiesDSLeap61 = _PtpClockTimePropertiesDSLeap61_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 7),
    _PtpClockTimePropertiesDSLeap61_Type()
)
ptpClockTimePropertiesDSLeap61.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSLeap61.setStatus("current")
_PtpClockTimePropertiesDSTimeTraceable_Type = TruthValue
_PtpClockTimePropertiesDSTimeTraceable_Object = MibTableColumn
ptpClockTimePropertiesDSTimeTraceable = _PtpClockTimePropertiesDSTimeTraceable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 8),
    _PtpClockTimePropertiesDSTimeTraceable_Type()
)
ptpClockTimePropertiesDSTimeTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSTimeTraceable.setStatus("current")
_PtpClockTimePropertiesDSFreqTraceable_Type = TruthValue
_PtpClockTimePropertiesDSFreqTraceable_Object = MibTableColumn
ptpClockTimePropertiesDSFreqTraceable = _PtpClockTimePropertiesDSFreqTraceable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 9),
    _PtpClockTimePropertiesDSFreqTraceable_Type()
)
ptpClockTimePropertiesDSFreqTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSFreqTraceable.setStatus("current")
_PtpClockTimePropertiesDSPTPTimescale_Type = TruthValue
_PtpClockTimePropertiesDSPTPTimescale_Object = MibTableColumn
ptpClockTimePropertiesDSPTPTimescale = _PtpClockTimePropertiesDSPTPTimescale_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 10),
    _PtpClockTimePropertiesDSPTPTimescale_Type()
)
ptpClockTimePropertiesDSPTPTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSPTPTimescale.setStatus("current")
_PtpClockTimePropertiesDSSource_Type = PtpClockTimeSourceType
_PtpClockTimePropertiesDSSource_Object = MibTableColumn
ptpClockTimePropertiesDSSource = _PtpClockTimePropertiesDSSource_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 5, 1, 11),
    _PtpClockTimePropertiesDSSource_Type()
)
ptpClockTimePropertiesDSSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTimePropertiesDSSource.setStatus("current")
_PtpClockTransDefaultDSTable_Object = MibTable
ptpClockTransDefaultDSTable = _PtpClockTransDefaultDSTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6)
)
if mibBuilder.loadTexts:
    ptpClockTransDefaultDSTable.setStatus("current")
_PtpClockTransDefaultDSEntry_Object = MibTableRow
ptpClockTransDefaultDSEntry = _PtpClockTransDefaultDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1)
)
ptpClockTransDefaultDSEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockTransDefaultDSDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockTransDefaultDSInstanceIndex"),
)
if mibBuilder.loadTexts:
    ptpClockTransDefaultDSEntry.setStatus("current")
_PtpClockTransDefaultDSDomainIndex_Type = PtpClockDomainType
_PtpClockTransDefaultDSDomainIndex_Object = MibTableColumn
ptpClockTransDefaultDSDomainIndex = _PtpClockTransDefaultDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 1),
    _PtpClockTransDefaultDSDomainIndex_Type()
)
ptpClockTransDefaultDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockTransDefaultDSDomainIndex.setStatus("current")
_PtpClockTransDefaultDSInstanceIndex_Type = PtpClockInstanceType
_PtpClockTransDefaultDSInstanceIndex_Object = MibTableColumn
ptpClockTransDefaultDSInstanceIndex = _PtpClockTransDefaultDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 2),
    _PtpClockTransDefaultDSInstanceIndex_Type()
)
ptpClockTransDefaultDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockTransDefaultDSInstanceIndex.setStatus("current")
_PtpClockTransDefaultDSClockIdentity_Type = PtpClockIdentity
_PtpClockTransDefaultDSClockIdentity_Object = MibTableColumn
ptpClockTransDefaultDSClockIdentity = _PtpClockTransDefaultDSClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 3),
    _PtpClockTransDefaultDSClockIdentity_Type()
)
ptpClockTransDefaultDSClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTransDefaultDSClockIdentity.setStatus("current")
_PtpClockTransDefaultDSNumOfPorts_Type = Counter32
_PtpClockTransDefaultDSNumOfPorts_Object = MibTableColumn
ptpClockTransDefaultDSNumOfPorts = _PtpClockTransDefaultDSNumOfPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 4),
    _PtpClockTransDefaultDSNumOfPorts_Type()
)
ptpClockTransDefaultDSNumOfPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTransDefaultDSNumOfPorts.setStatus("current")
_PtpClockTransDefaultDSDelay_Type = PtpClockMechanismType
_PtpClockTransDefaultDSDelay_Object = MibTableColumn
ptpClockTransDefaultDSDelay = _PtpClockTransDefaultDSDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 5),
    _PtpClockTransDefaultDSDelay_Type()
)
ptpClockTransDefaultDSDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTransDefaultDSDelay.setStatus("current")
_PtpClockTransDefaultDSPrimaryDomain_Type = PtpClockDomainType
_PtpClockTransDefaultDSPrimaryDomain_Object = MibTableColumn
ptpClockTransDefaultDSPrimaryDomain = _PtpClockTransDefaultDSPrimaryDomain_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 6, 1, 6),
    _PtpClockTransDefaultDSPrimaryDomain_Type()
)
ptpClockTransDefaultDSPrimaryDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockTransDefaultDSPrimaryDomain.setStatus("current")
_PtpClockPortTable_Object = MibTable
ptpClockPortTable = _PtpClockPortTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7)
)
if mibBuilder.loadTexts:
    ptpClockPortTable.setStatus("current")
_PtpClockPortEntry_Object = MibTableRow
ptpClockPortEntry = _PtpClockPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1)
)
ptpClockPortEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockPortDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortClockTypeIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortClockInstanceIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortTablePortNumberIndex"),
)
if mibBuilder.loadTexts:
    ptpClockPortEntry.setStatus("current")
_PtpClockPortDomainIndex_Type = PtpClockDomainType
_PtpClockPortDomainIndex_Object = MibTableColumn
ptpClockPortDomainIndex = _PtpClockPortDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 1),
    _PtpClockPortDomainIndex_Type()
)
ptpClockPortDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortDomainIndex.setStatus("current")
_PtpClockPortClockTypeIndex_Type = PtpClockType
_PtpClockPortClockTypeIndex_Object = MibTableColumn
ptpClockPortClockTypeIndex = _PtpClockPortClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 2),
    _PtpClockPortClockTypeIndex_Type()
)
ptpClockPortClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortClockTypeIndex.setStatus("current")
_PtpClockPortClockInstanceIndex_Type = PtpClockInstanceType
_PtpClockPortClockInstanceIndex_Object = MibTableColumn
ptpClockPortClockInstanceIndex = _PtpClockPortClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 3),
    _PtpClockPortClockInstanceIndex_Type()
)
ptpClockPortClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortClockInstanceIndex.setStatus("current")
_PtpClockPortTablePortNumberIndex_Type = PtpClockPortNumber
_PtpClockPortTablePortNumberIndex_Object = MibTableColumn
ptpClockPortTablePortNumberIndex = _PtpClockPortTablePortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 4),
    _PtpClockPortTablePortNumberIndex_Type()
)
ptpClockPortTablePortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortTablePortNumberIndex.setStatus("current")


class _PtpClockPortName_Type(DisplayString):
    """Custom type ptpClockPortName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PtpClockPortName_Type.__name__ = "DisplayString"
_PtpClockPortName_Object = MibTableColumn
ptpClockPortName = _PtpClockPortName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 5),
    _PtpClockPortName_Type()
)
ptpClockPortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortName.setStatus("current")
_PtpClockPortRole_Type = PtpClockRoleType
_PtpClockPortRole_Object = MibTableColumn
ptpClockPortRole = _PtpClockPortRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 6),
    _PtpClockPortRole_Type()
)
ptpClockPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRole.setStatus("current")
_PtpClockPortSyncTwoStep_Type = TruthValue
_PtpClockPortSyncTwoStep_Object = MibTableColumn
ptpClockPortSyncTwoStep = _PtpClockPortSyncTwoStep_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 7),
    _PtpClockPortSyncTwoStep_Type()
)
ptpClockPortSyncTwoStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortSyncTwoStep.setStatus("current")
_PtpClockPortCurrentPeerAddressType_Type = AutonomousType
_PtpClockPortCurrentPeerAddressType_Object = MibTableColumn
ptpClockPortCurrentPeerAddressType = _PtpClockPortCurrentPeerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 8),
    _PtpClockPortCurrentPeerAddressType_Type()
)
ptpClockPortCurrentPeerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortCurrentPeerAddressType.setStatus("current")
_PtpClockPortCurrentPeerAddress_Type = PtpClockPortTransportTypeAddress
_PtpClockPortCurrentPeerAddress_Object = MibTableColumn
ptpClockPortCurrentPeerAddress = _PtpClockPortCurrentPeerAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 9),
    _PtpClockPortCurrentPeerAddress_Type()
)
ptpClockPortCurrentPeerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortCurrentPeerAddress.setStatus("current")
_PtpClockPortNumOfAssociatedPorts_Type = Gauge32
_PtpClockPortNumOfAssociatedPorts_Object = MibTableColumn
ptpClockPortNumOfAssociatedPorts = _PtpClockPortNumOfAssociatedPorts_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 7, 1, 10),
    _PtpClockPortNumOfAssociatedPorts_Type()
)
ptpClockPortNumOfAssociatedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortNumOfAssociatedPorts.setStatus("current")
_PtpClockPortDSTable_Object = MibTable
ptpClockPortDSTable = _PtpClockPortDSTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8)
)
if mibBuilder.loadTexts:
    ptpClockPortDSTable.setStatus("current")
_PtpClockPortDSEntry_Object = MibTableRow
ptpClockPortDSEntry = _PtpClockPortDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1)
)
ptpClockPortDSEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockPortDSDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortDSClockTypeIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortDSClockInstanceIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortDSPortNumberIndex"),
)
if mibBuilder.loadTexts:
    ptpClockPortDSEntry.setStatus("current")
_PtpClockPortDSDomainIndex_Type = PtpClockDomainType
_PtpClockPortDSDomainIndex_Object = MibTableColumn
ptpClockPortDSDomainIndex = _PtpClockPortDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 1),
    _PtpClockPortDSDomainIndex_Type()
)
ptpClockPortDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortDSDomainIndex.setStatus("current")
_PtpClockPortDSClockTypeIndex_Type = PtpClockType
_PtpClockPortDSClockTypeIndex_Object = MibTableColumn
ptpClockPortDSClockTypeIndex = _PtpClockPortDSClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 2),
    _PtpClockPortDSClockTypeIndex_Type()
)
ptpClockPortDSClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortDSClockTypeIndex.setStatus("current")
_PtpClockPortDSClockInstanceIndex_Type = PtpClockInstanceType
_PtpClockPortDSClockInstanceIndex_Object = MibTableColumn
ptpClockPortDSClockInstanceIndex = _PtpClockPortDSClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 3),
    _PtpClockPortDSClockInstanceIndex_Type()
)
ptpClockPortDSClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortDSClockInstanceIndex.setStatus("current")
_PtpClockPortDSPortNumberIndex_Type = PtpClockPortNumber
_PtpClockPortDSPortNumberIndex_Object = MibTableColumn
ptpClockPortDSPortNumberIndex = _PtpClockPortDSPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 4),
    _PtpClockPortDSPortNumberIndex_Type()
)
ptpClockPortDSPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortDSPortNumberIndex.setStatus("current")


class _PtpClockPortDSName_Type(DisplayString):
    """Custom type ptpClockPortDSName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PtpClockPortDSName_Type.__name__ = "DisplayString"
_PtpClockPortDSName_Object = MibTableColumn
ptpClockPortDSName = _PtpClockPortDSName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 5),
    _PtpClockPortDSName_Type()
)
ptpClockPortDSName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSName.setStatus("current")


class _PtpClockPortDSPortIdentity_Type(OctetString):
    """Custom type ptpClockPortDSPortIdentity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_PtpClockPortDSPortIdentity_Type.__name__ = "OctetString"
_PtpClockPortDSPortIdentity_Object = MibTableColumn
ptpClockPortDSPortIdentity = _PtpClockPortDSPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 6),
    _PtpClockPortDSPortIdentity_Type()
)
ptpClockPortDSPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSPortIdentity.setStatus("current")
_PtpClockPortDSlogAnnouncementInterval_Type = PtpClockIntervalBase2
_PtpClockPortDSlogAnnouncementInterval_Object = MibTableColumn
ptpClockPortDSlogAnnouncementInterval = _PtpClockPortDSlogAnnouncementInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 7),
    _PtpClockPortDSlogAnnouncementInterval_Type()
)
ptpClockPortDSlogAnnouncementInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSlogAnnouncementInterval.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortDSlogAnnouncementInterval.setUnits("Time Interval")
_PtpClockPortDSAnnounceRctTimeout_Type = Integer32
_PtpClockPortDSAnnounceRctTimeout_Object = MibTableColumn
ptpClockPortDSAnnounceRctTimeout = _PtpClockPortDSAnnounceRctTimeout_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 8),
    _PtpClockPortDSAnnounceRctTimeout_Type()
)
ptpClockPortDSAnnounceRctTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSAnnounceRctTimeout.setStatus("current")
_PtpClockPortDSlogSyncInterval_Type = PtpClockIntervalBase2
_PtpClockPortDSlogSyncInterval_Object = MibTableColumn
ptpClockPortDSlogSyncInterval = _PtpClockPortDSlogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 9),
    _PtpClockPortDSlogSyncInterval_Type()
)
ptpClockPortDSlogSyncInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSlogSyncInterval.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortDSlogSyncInterval.setUnits("Time Interval")
_PtpClockPortDSMinDelayReqInterval_Type = Integer32
_PtpClockPortDSMinDelayReqInterval_Object = MibTableColumn
ptpClockPortDSMinDelayReqInterval = _PtpClockPortDSMinDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 10),
    _PtpClockPortDSMinDelayReqInterval_Type()
)
ptpClockPortDSMinDelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSMinDelayReqInterval.setStatus("current")
_PtpClockPortDSPeerDelayReqInterval_Type = Integer32
_PtpClockPortDSPeerDelayReqInterval_Object = MibTableColumn
ptpClockPortDSPeerDelayReqInterval = _PtpClockPortDSPeerDelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 11),
    _PtpClockPortDSPeerDelayReqInterval_Type()
)
ptpClockPortDSPeerDelayReqInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSPeerDelayReqInterval.setStatus("current")
_PtpClockPortDSDelayMech_Type = PtpClockMechanismType
_PtpClockPortDSDelayMech_Object = MibTableColumn
ptpClockPortDSDelayMech = _PtpClockPortDSDelayMech_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 12),
    _PtpClockPortDSDelayMech_Type()
)
ptpClockPortDSDelayMech.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSDelayMech.setStatus("current")
_PtpClockPortDSPeerMeanPathDelay_Type = PtpClockTimeInterval
_PtpClockPortDSPeerMeanPathDelay_Object = MibTableColumn
ptpClockPortDSPeerMeanPathDelay = _PtpClockPortDSPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 13),
    _PtpClockPortDSPeerMeanPathDelay_Type()
)
ptpClockPortDSPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSPeerMeanPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortDSPeerMeanPathDelay.setUnits("Time Interval")
_PtpClockPortDSGrantDuration_Type = Unsigned32
_PtpClockPortDSGrantDuration_Object = MibTableColumn
ptpClockPortDSGrantDuration = _PtpClockPortDSGrantDuration_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 14),
    _PtpClockPortDSGrantDuration_Type()
)
ptpClockPortDSGrantDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSGrantDuration.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortDSGrantDuration.setUnits("seconds")
_PtpClockPortDSPTPVersion_Type = Unsigned32
_PtpClockPortDSPTPVersion_Object = MibTableColumn
ptpClockPortDSPTPVersion = _PtpClockPortDSPTPVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 8, 1, 15),
    _PtpClockPortDSPTPVersion_Type()
)
ptpClockPortDSPTPVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortDSPTPVersion.setStatus("current")
_PtpClockPortRunningTable_Object = MibTable
ptpClockPortRunningTable = _PtpClockPortRunningTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9)
)
if mibBuilder.loadTexts:
    ptpClockPortRunningTable.setStatus("current")
_PtpClockPortRunningEntry_Object = MibTableRow
ptpClockPortRunningEntry = _PtpClockPortRunningEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1)
)
ptpClockPortRunningEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockPortRunningDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortRunningClockTypeIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortRunningClockInstanceIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortRunningPortNumberIndex"),
)
if mibBuilder.loadTexts:
    ptpClockPortRunningEntry.setStatus("current")
_PtpClockPortRunningDomainIndex_Type = PtpClockDomainType
_PtpClockPortRunningDomainIndex_Object = MibTableColumn
ptpClockPortRunningDomainIndex = _PtpClockPortRunningDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 1),
    _PtpClockPortRunningDomainIndex_Type()
)
ptpClockPortRunningDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortRunningDomainIndex.setStatus("current")
_PtpClockPortRunningClockTypeIndex_Type = PtpClockType
_PtpClockPortRunningClockTypeIndex_Object = MibTableColumn
ptpClockPortRunningClockTypeIndex = _PtpClockPortRunningClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 2),
    _PtpClockPortRunningClockTypeIndex_Type()
)
ptpClockPortRunningClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortRunningClockTypeIndex.setStatus("current")
_PtpClockPortRunningClockInstanceIndex_Type = PtpClockInstanceType
_PtpClockPortRunningClockInstanceIndex_Object = MibTableColumn
ptpClockPortRunningClockInstanceIndex = _PtpClockPortRunningClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 3),
    _PtpClockPortRunningClockInstanceIndex_Type()
)
ptpClockPortRunningClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortRunningClockInstanceIndex.setStatus("current")
_PtpClockPortRunningPortNumberIndex_Type = PtpClockPortNumber
_PtpClockPortRunningPortNumberIndex_Object = MibTableColumn
ptpClockPortRunningPortNumberIndex = _PtpClockPortRunningPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 4),
    _PtpClockPortRunningPortNumberIndex_Type()
)
ptpClockPortRunningPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortRunningPortNumberIndex.setStatus("current")


class _PtpClockPortRunningName_Type(DisplayString):
    """Custom type ptpClockPortRunningName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_PtpClockPortRunningName_Type.__name__ = "DisplayString"
_PtpClockPortRunningName_Object = MibTableColumn
ptpClockPortRunningName = _PtpClockPortRunningName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 5),
    _PtpClockPortRunningName_Type()
)
ptpClockPortRunningName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningName.setStatus("current")
_PtpClockPortRunningState_Type = PtpClockPortState
_PtpClockPortRunningState_Object = MibTableColumn
ptpClockPortRunningState = _PtpClockPortRunningState_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 6),
    _PtpClockPortRunningState_Type()
)
ptpClockPortRunningState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningState.setStatus("current")
_PtpClockPortRunningRole_Type = PtpClockRoleType
_PtpClockPortRunningRole_Object = MibTableColumn
ptpClockPortRunningRole = _PtpClockPortRunningRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 7),
    _PtpClockPortRunningRole_Type()
)
ptpClockPortRunningRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningRole.setStatus("current")
_PtpClockPortRunningInterfaceIndex_Type = InterfaceIndexOrZero
_PtpClockPortRunningInterfaceIndex_Object = MibTableColumn
ptpClockPortRunningInterfaceIndex = _PtpClockPortRunningInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 8),
    _PtpClockPortRunningInterfaceIndex_Type()
)
ptpClockPortRunningInterfaceIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningInterfaceIndex.setStatus("current")
_PtpClockPortRunningTransport_Type = AutonomousType
_PtpClockPortRunningTransport_Object = MibTableColumn
ptpClockPortRunningTransport = _PtpClockPortRunningTransport_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 9),
    _PtpClockPortRunningTransport_Type()
)
ptpClockPortRunningTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningTransport.setStatus("current")
_PtpClockPortRunningEncapsulationType_Type = AutonomousType
_PtpClockPortRunningEncapsulationType_Object = MibTableColumn
ptpClockPortRunningEncapsulationType = _PtpClockPortRunningEncapsulationType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 10),
    _PtpClockPortRunningEncapsulationType_Type()
)
ptpClockPortRunningEncapsulationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningEncapsulationType.setStatus("current")
_PtpClockPortRunningTxMode_Type = PtpClockTxModeType
_PtpClockPortRunningTxMode_Object = MibTableColumn
ptpClockPortRunningTxMode = _PtpClockPortRunningTxMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 11),
    _PtpClockPortRunningTxMode_Type()
)
ptpClockPortRunningTxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningTxMode.setStatus("current")
_PtpClockPortRunningRxMode_Type = PtpClockTxModeType
_PtpClockPortRunningRxMode_Object = MibTableColumn
ptpClockPortRunningRxMode = _PtpClockPortRunningRxMode_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 12),
    _PtpClockPortRunningRxMode_Type()
)
ptpClockPortRunningRxMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningRxMode.setStatus("current")
_PtpClockPortRunningPacketsReceived_Type = Counter64
_PtpClockPortRunningPacketsReceived_Object = MibTableColumn
ptpClockPortRunningPacketsReceived = _PtpClockPortRunningPacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 13),
    _PtpClockPortRunningPacketsReceived_Type()
)
ptpClockPortRunningPacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningPacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortRunningPacketsReceived.setUnits("packets")
_PtpClockPortRunningPacketsSent_Type = Counter64
_PtpClockPortRunningPacketsSent_Object = MibTableColumn
ptpClockPortRunningPacketsSent = _PtpClockPortRunningPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 9, 1, 14),
    _PtpClockPortRunningPacketsSent_Type()
)
ptpClockPortRunningPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortRunningPacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortRunningPacketsSent.setUnits("packets")
_PtpClockPortTransDSTable_Object = MibTable
ptpClockPortTransDSTable = _PtpClockPortTransDSTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10)
)
if mibBuilder.loadTexts:
    ptpClockPortTransDSTable.setStatus("current")
_PtpClockPortTransDSEntry_Object = MibTableRow
ptpClockPortTransDSEntry = _PtpClockPortTransDSEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1)
)
ptpClockPortTransDSEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockPortTransDSDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortTransDSInstanceIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortTransDSPortNumberIndex"),
)
if mibBuilder.loadTexts:
    ptpClockPortTransDSEntry.setStatus("current")
_PtpClockPortTransDSDomainIndex_Type = PtpClockDomainType
_PtpClockPortTransDSDomainIndex_Object = MibTableColumn
ptpClockPortTransDSDomainIndex = _PtpClockPortTransDSDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 1),
    _PtpClockPortTransDSDomainIndex_Type()
)
ptpClockPortTransDSDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortTransDSDomainIndex.setStatus("current")
_PtpClockPortTransDSInstanceIndex_Type = PtpClockInstanceType
_PtpClockPortTransDSInstanceIndex_Object = MibTableColumn
ptpClockPortTransDSInstanceIndex = _PtpClockPortTransDSInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 2),
    _PtpClockPortTransDSInstanceIndex_Type()
)
ptpClockPortTransDSInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortTransDSInstanceIndex.setStatus("current")
_PtpClockPortTransDSPortNumberIndex_Type = PtpClockPortNumber
_PtpClockPortTransDSPortNumberIndex_Object = MibTableColumn
ptpClockPortTransDSPortNumberIndex = _PtpClockPortTransDSPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 3),
    _PtpClockPortTransDSPortNumberIndex_Type()
)
ptpClockPortTransDSPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortTransDSPortNumberIndex.setStatus("current")
_PtpClockPortTransDSPortIdentity_Type = PtpClockIdentity
_PtpClockPortTransDSPortIdentity_Object = MibTableColumn
ptpClockPortTransDSPortIdentity = _PtpClockPortTransDSPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 4),
    _PtpClockPortTransDSPortIdentity_Type()
)
ptpClockPortTransDSPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortTransDSPortIdentity.setStatus("current")
_PtpClockPortTransDSlogMinPdelayReqInt_Type = PtpClockIntervalBase2
_PtpClockPortTransDSlogMinPdelayReqInt_Object = MibTableColumn
ptpClockPortTransDSlogMinPdelayReqInt = _PtpClockPortTransDSlogMinPdelayReqInt_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 5),
    _PtpClockPortTransDSlogMinPdelayReqInt_Type()
)
ptpClockPortTransDSlogMinPdelayReqInt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortTransDSlogMinPdelayReqInt.setStatus("current")
_PtpClockPortTransDSFaultyFlag_Type = TruthValue
_PtpClockPortTransDSFaultyFlag_Object = MibTableColumn
ptpClockPortTransDSFaultyFlag = _PtpClockPortTransDSFaultyFlag_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 6),
    _PtpClockPortTransDSFaultyFlag_Type()
)
ptpClockPortTransDSFaultyFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortTransDSFaultyFlag.setStatus("current")
_PtpClockPortTransDSPeerMeanPathDelay_Type = PtpClockTimeInterval
_PtpClockPortTransDSPeerMeanPathDelay_Object = MibTableColumn
ptpClockPortTransDSPeerMeanPathDelay = _PtpClockPortTransDSPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 10, 1, 7),
    _PtpClockPortTransDSPeerMeanPathDelay_Type()
)
ptpClockPortTransDSPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortTransDSPeerMeanPathDelay.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortTransDSPeerMeanPathDelay.setUnits("Time Interval")
_PtpClockPortAssociateTable_Object = MibTable
ptpClockPortAssociateTable = _PtpClockPortAssociateTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11)
)
if mibBuilder.loadTexts:
    ptpClockPortAssociateTable.setStatus("current")
_PtpClockPortAssociateEntry_Object = MibTableRow
ptpClockPortAssociateEntry = _PtpClockPortAssociateEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1)
)
ptpClockPortAssociateEntry.setIndexNames(
    (0, "AT-PTP-MIB", "ptpClockPortCurrentDomainIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortCurrentClockTypeIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortCurrentClockInstanceIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortCurrentPortNumberIndex"),
    (0, "AT-PTP-MIB", "ptpClockPortAssociatePortIndex"),
)
if mibBuilder.loadTexts:
    ptpClockPortAssociateEntry.setStatus("current")
_PtpClockPortCurrentDomainIndex_Type = PtpClockDomainType
_PtpClockPortCurrentDomainIndex_Object = MibTableColumn
ptpClockPortCurrentDomainIndex = _PtpClockPortCurrentDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 1),
    _PtpClockPortCurrentDomainIndex_Type()
)
ptpClockPortCurrentDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortCurrentDomainIndex.setStatus("current")
_PtpClockPortCurrentClockTypeIndex_Type = PtpClockType
_PtpClockPortCurrentClockTypeIndex_Object = MibTableColumn
ptpClockPortCurrentClockTypeIndex = _PtpClockPortCurrentClockTypeIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 2),
    _PtpClockPortCurrentClockTypeIndex_Type()
)
ptpClockPortCurrentClockTypeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortCurrentClockTypeIndex.setStatus("current")
_PtpClockPortCurrentClockInstanceIndex_Type = PtpClockInstanceType
_PtpClockPortCurrentClockInstanceIndex_Object = MibTableColumn
ptpClockPortCurrentClockInstanceIndex = _PtpClockPortCurrentClockInstanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 3),
    _PtpClockPortCurrentClockInstanceIndex_Type()
)
ptpClockPortCurrentClockInstanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortCurrentClockInstanceIndex.setStatus("current")
_PtpClockPortCurrentPortNumberIndex_Type = PtpClockPortNumber
_PtpClockPortCurrentPortNumberIndex_Object = MibTableColumn
ptpClockPortCurrentPortNumberIndex = _PtpClockPortCurrentPortNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 4),
    _PtpClockPortCurrentPortNumberIndex_Type()
)
ptpClockPortCurrentPortNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortCurrentPortNumberIndex.setStatus("current")


class _PtpClockPortAssociatePortIndex_Type(Unsigned32):
    """Custom type ptpClockPortAssociatePortIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PtpClockPortAssociatePortIndex_Type.__name__ = "Unsigned32"
_PtpClockPortAssociatePortIndex_Object = MibTableColumn
ptpClockPortAssociatePortIndex = _PtpClockPortAssociatePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 5),
    _PtpClockPortAssociatePortIndex_Type()
)
ptpClockPortAssociatePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ptpClockPortAssociatePortIndex.setStatus("current")
_PtpClockPortAssociateAddressType_Type = AutonomousType
_PtpClockPortAssociateAddressType_Object = MibTableColumn
ptpClockPortAssociateAddressType = _PtpClockPortAssociateAddressType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 6),
    _PtpClockPortAssociateAddressType_Type()
)
ptpClockPortAssociateAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortAssociateAddressType.setStatus("current")
_PtpClockPortAssociateAddress_Type = PtpClockPortTransportTypeAddress
_PtpClockPortAssociateAddress_Object = MibTableColumn
ptpClockPortAssociateAddress = _PtpClockPortAssociateAddress_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 7),
    _PtpClockPortAssociateAddress_Type()
)
ptpClockPortAssociateAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortAssociateAddress.setStatus("current")
_PtpClockPortAssociatePacketsSent_Type = Counter64
_PtpClockPortAssociatePacketsSent_Object = MibTableColumn
ptpClockPortAssociatePacketsSent = _PtpClockPortAssociatePacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 8),
    _PtpClockPortAssociatePacketsSent_Type()
)
ptpClockPortAssociatePacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortAssociatePacketsSent.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortAssociatePacketsSent.setUnits("packets")
_PtpClockPortAssociatePacketsReceived_Type = Counter64
_PtpClockPortAssociatePacketsReceived_Object = MibTableColumn
ptpClockPortAssociatePacketsReceived = _PtpClockPortAssociatePacketsReceived_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 9),
    _PtpClockPortAssociatePacketsReceived_Type()
)
ptpClockPortAssociatePacketsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortAssociatePacketsReceived.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortAssociatePacketsReceived.setUnits("packets")
_PtpClockPortAssociateInErrors_Type = Counter64
_PtpClockPortAssociateInErrors_Object = MibTableColumn
ptpClockPortAssociateInErrors = _PtpClockPortAssociateInErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 10),
    _PtpClockPortAssociateInErrors_Type()
)
ptpClockPortAssociateInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortAssociateInErrors.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortAssociateInErrors.setUnits("packets")
_PtpClockPortAssociateOutErrors_Type = Counter64
_PtpClockPortAssociateOutErrors_Object = MibTableColumn
ptpClockPortAssociateOutErrors = _PtpClockPortAssociateOutErrors_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 11, 1, 11),
    _PtpClockPortAssociateOutErrors_Type()
)
ptpClockPortAssociateOutErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ptpClockPortAssociateOutErrors.setStatus("current")
if mibBuilder.loadTexts:
    ptpClockPortAssociateOutErrors.setUnits("packets")
_PtpWellKnownTransportTypes_ObjectIdentity = ObjectIdentity
ptpWellKnownTransportTypes = _PtpWellKnownTransportTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12)
)
_PtpTransportTypeIPversion4_ObjectIdentity = ObjectIdentity
ptpTransportTypeIPversion4 = _PtpTransportTypeIPversion4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 1)
)
if mibBuilder.loadTexts:
    ptpTransportTypeIPversion4.setStatus("current")
_PtpTransportTypeIPversion6_ObjectIdentity = ObjectIdentity
ptpTransportTypeIPversion6 = _PtpTransportTypeIPversion6_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 2)
)
if mibBuilder.loadTexts:
    ptpTransportTypeIPversion6.setStatus("current")
_PtpTransportTypeEthernet_ObjectIdentity = ObjectIdentity
ptpTransportTypeEthernet = _PtpTransportTypeEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 3)
)
if mibBuilder.loadTexts:
    ptpTransportTypeEthernet.setStatus("current")
_PtpTransportTypeDeviceNET_ObjectIdentity = ObjectIdentity
ptpTransportTypeDeviceNET = _PtpTransportTypeDeviceNET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 4)
)
if mibBuilder.loadTexts:
    ptpTransportTypeDeviceNET.setStatus("current")
_PtpTransportTypeControlNET_ObjectIdentity = ObjectIdentity
ptpTransportTypeControlNET = _PtpTransportTypeControlNET_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 5)
)
if mibBuilder.loadTexts:
    ptpTransportTypeControlNET.setStatus("current")
_PtpTransportTypeIEC61158_ObjectIdentity = ObjectIdentity
ptpTransportTypeIEC61158 = _PtpTransportTypeIEC61158_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 12, 6)
)
if mibBuilder.loadTexts:
    ptpTransportTypeIEC61158.setStatus("current")
_PtpWellKnownEncapsulationTypes_ObjectIdentity = ObjectIdentity
ptpWellKnownEncapsulationTypes = _PtpWellKnownEncapsulationTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13)
)
_PtpEncapsulationTypeEthernet_ObjectIdentity = ObjectIdentity
ptpEncapsulationTypeEthernet = _PtpEncapsulationTypeEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 1)
)
if mibBuilder.loadTexts:
    ptpEncapsulationTypeEthernet.setStatus("current")
_PtpEncapsulationTypeVLAN_ObjectIdentity = ObjectIdentity
ptpEncapsulationTypeVLAN = _PtpEncapsulationTypeVLAN_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 2)
)
if mibBuilder.loadTexts:
    ptpEncapsulationTypeVLAN.setStatus("current")
_PtpEncapsulationTypeUDPIPLSP_ObjectIdentity = ObjectIdentity
ptpEncapsulationTypeUDPIPLSP = _PtpEncapsulationTypeUDPIPLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 3)
)
if mibBuilder.loadTexts:
    ptpEncapsulationTypeUDPIPLSP.setStatus("current")
_PtpEncapsulationTypePWUDPIPLSP_ObjectIdentity = ObjectIdentity
ptpEncapsulationTypePWUDPIPLSP = _PtpEncapsulationTypePWUDPIPLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 4)
)
if mibBuilder.loadTexts:
    ptpEncapsulationTypePWUDPIPLSP.setStatus("current")
_PtpEncapsulationTypePWEthernetLSP_ObjectIdentity = ObjectIdentity
ptpEncapsulationTypePWEthernetLSP = _PtpEncapsulationTypePWEthernetLSP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 1, 2, 13, 5)
)
if mibBuilder.loadTexts:
    ptpEncapsulationTypePWEthernetLSP.setStatus("current")
_PtpMIBConformance_ObjectIdentity = ObjectIdentity
ptpMIBConformance = _PtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2)
)
_PtpMIBCompliances_ObjectIdentity = ObjectIdentity
ptpMIBCompliances = _PtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1)
)
_PtpMIBGroups_ObjectIdentity = ObjectIdentity
ptpMIBGroups = _PtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2)
)

# Managed Objects groups

ptpMIBSystemInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 1)
)
ptpMIBSystemInfoGroup.setObjects(
      *(("AT-PTP-MIB", "ptpSystemDomainTotals"),
        ("AT-PTP-MIB", "ptpDomainClockPortsTotal"),
        ("AT-PTP-MIB", "ptpSystemProfile"))
)
if mibBuilder.loadTexts:
    ptpMIBSystemInfoGroup.setStatus("current")

ptpMIBClockCurrentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 2)
)
ptpMIBClockCurrentDSGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockCurrentDSStepsRemoved"),
        ("AT-PTP-MIB", "ptpClockCurrentDSOffsetFromMaster"),
        ("AT-PTP-MIB", "ptpClockCurrentDSMeanPathDelay"))
)
if mibBuilder.loadTexts:
    ptpMIBClockCurrentDSGroup.setStatus("current")

ptpMIBClockParentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 3)
)
ptpMIBClockParentDSGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockParentDSParentPortIdentity"),
        ("AT-PTP-MIB", "ptpClockParentDSParentStats"),
        ("AT-PTP-MIB", "ptpClockParentDSOffset"),
        ("AT-PTP-MIB", "ptpClockParentDSClockPhChRate"),
        ("AT-PTP-MIB", "ptpClockParentDSGMClockIdentity"),
        ("AT-PTP-MIB", "ptpClockParentDSGMClockPriority1"),
        ("AT-PTP-MIB", "ptpClockParentDSGMClockPriority2"),
        ("AT-PTP-MIB", "ptpClockParentDSGMClockQualityClass"),
        ("AT-PTP-MIB", "ptpClockParentDSGMClockQualityAccuracy"),
        ("AT-PTP-MIB", "ptpClockParentDSGMClockQualityOffset"))
)
if mibBuilder.loadTexts:
    ptpMIBClockParentDSGroup.setStatus("current")

ptpMIBClockDefaultDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 4)
)
ptpMIBClockDefaultDSGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockDefaultDSTwoStepFlag"),
        ("AT-PTP-MIB", "ptpClockDefaultDSClockIdentity"),
        ("AT-PTP-MIB", "ptpClockDefaultDSPriority1"),
        ("AT-PTP-MIB", "ptpClockDefaultDSPriority2"),
        ("AT-PTP-MIB", "ptpClockDefaultDSSlaveOnly"),
        ("AT-PTP-MIB", "ptpClockDefaultDSQualityClass"),
        ("AT-PTP-MIB", "ptpClockDefaultDSQualityAccuracy"),
        ("AT-PTP-MIB", "ptpClockDefaultDSQualityOffset"))
)
if mibBuilder.loadTexts:
    ptpMIBClockDefaultDSGroup.setStatus("current")

ptpMIBClockRunningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 5)
)
ptpMIBClockRunningGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockRunningState"),
        ("AT-PTP-MIB", "ptpClockRunningPacketsSent"),
        ("AT-PTP-MIB", "ptpClockRunningPacketsReceived"))
)
if mibBuilder.loadTexts:
    ptpMIBClockRunningGroup.setStatus("current")

ptpMIBClockTimepropertiesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 6)
)
ptpMIBClockTimepropertiesGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockTimePropertiesDSCurrentUTCOffsetValid"),
        ("AT-PTP-MIB", "ptpClockTimePropertiesDSCurrentUTCOffset"),
        ("AT-PTP-MIB", "ptpClockTimePropertiesDSLeap59"),
        ("AT-PTP-MIB", "ptpClockTimePropertiesDSLeap61"),
        ("AT-PTP-MIB", "ptpClockTimePropertiesDSTimeTraceable"),
        ("AT-PTP-MIB", "ptpClockTimePropertiesDSFreqTraceable"),
        ("AT-PTP-MIB", "ptpClockTimePropertiesDSPTPTimescale"),
        ("AT-PTP-MIB", "ptpClockTimePropertiesDSSource"))
)
if mibBuilder.loadTexts:
    ptpMIBClockTimepropertiesGroup.setStatus("current")

ptpMIBClockTranparentDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 7)
)
ptpMIBClockTranparentDSGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockTransDefaultDSClockIdentity"),
        ("AT-PTP-MIB", "ptpClockTransDefaultDSNumOfPorts"),
        ("AT-PTP-MIB", "ptpClockTransDefaultDSDelay"),
        ("AT-PTP-MIB", "ptpClockTransDefaultDSPrimaryDomain"))
)
if mibBuilder.loadTexts:
    ptpMIBClockTranparentDSGroup.setStatus("current")

ptpMIBClockPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 8)
)
ptpMIBClockPortGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockPortName"),
        ("AT-PTP-MIB", "ptpClockPortSyncTwoStep"),
        ("AT-PTP-MIB", "ptpClockPortCurrentPeerAddress"),
        ("AT-PTP-MIB", "ptpClockPortNumOfAssociatedPorts"),
        ("AT-PTP-MIB", "ptpClockPortCurrentPeerAddressType"),
        ("AT-PTP-MIB", "ptpClockPortRole"))
)
if mibBuilder.loadTexts:
    ptpMIBClockPortGroup.setStatus("current")

ptpMIBClockPortDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 9)
)
ptpMIBClockPortDSGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockPortDSName"),
        ("AT-PTP-MIB", "ptpClockPortDSPortIdentity"),
        ("AT-PTP-MIB", "ptpClockPortDSlogAnnouncementInterval"),
        ("AT-PTP-MIB", "ptpClockPortDSAnnounceRctTimeout"),
        ("AT-PTP-MIB", "ptpClockPortDSlogSyncInterval"),
        ("AT-PTP-MIB", "ptpClockPortDSMinDelayReqInterval"),
        ("AT-PTP-MIB", "ptpClockPortDSPeerDelayReqInterval"),
        ("AT-PTP-MIB", "ptpClockPortDSDelayMech"),
        ("AT-PTP-MIB", "ptpClockPortDSPeerMeanPathDelay"),
        ("AT-PTP-MIB", "ptpClockPortDSGrantDuration"),
        ("AT-PTP-MIB", "ptpClockPortDSPTPVersion"))
)
if mibBuilder.loadTexts:
    ptpMIBClockPortDSGroup.setStatus("current")

ptpMIBClockPortRunningGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 10)
)
ptpMIBClockPortRunningGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockPortRunningName"),
        ("AT-PTP-MIB", "ptpClockPortRunningState"),
        ("AT-PTP-MIB", "ptpClockPortRunningRole"),
        ("AT-PTP-MIB", "ptpClockPortRunningInterfaceIndex"),
        ("AT-PTP-MIB", "ptpClockPortRunningTransport"),
        ("AT-PTP-MIB", "ptpClockPortRunningEncapsulationType"),
        ("AT-PTP-MIB", "ptpClockPortRunningTxMode"),
        ("AT-PTP-MIB", "ptpClockPortRunningRxMode"),
        ("AT-PTP-MIB", "ptpClockPortRunningPacketsReceived"),
        ("AT-PTP-MIB", "ptpClockPortRunningPacketsSent"))
)
if mibBuilder.loadTexts:
    ptpMIBClockPortRunningGroup.setStatus("current")

ptpMIBClockPortTransDSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 11)
)
ptpMIBClockPortTransDSGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockPortTransDSPortIdentity"),
        ("AT-PTP-MIB", "ptpClockPortTransDSlogMinPdelayReqInt"),
        ("AT-PTP-MIB", "ptpClockPortTransDSFaultyFlag"),
        ("AT-PTP-MIB", "ptpClockPortTransDSPeerMeanPathDelay"))
)
if mibBuilder.loadTexts:
    ptpMIBClockPortTransDSGroup.setStatus("current")

ptpMIBClockPortAssociateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 2, 12)
)
ptpMIBClockPortAssociateGroup.setObjects(
      *(("AT-PTP-MIB", "ptpClockPortAssociatePacketsSent"),
        ("AT-PTP-MIB", "ptpClockPortAssociatePacketsReceived"),
        ("AT-PTP-MIB", "ptpClockPortAssociateAddress"),
        ("AT-PTP-MIB", "ptpClockPortAssociateAddressType"),
        ("AT-PTP-MIB", "ptpClockPortAssociateInErrors"),
        ("AT-PTP-MIB", "ptpClockPortAssociateOutErrors"))
)
if mibBuilder.loadTexts:
    ptpMIBClockPortAssociateGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ptpMIBCompliancesSystemInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1, 1)
)
ptpMIBCompliancesSystemInfo.setObjects(
    ("AT-PTP-MIB", "ptpMIBSystemInfoGroup")
)
if mibBuilder.loadTexts:
    ptpMIBCompliancesSystemInfo.setStatus(
        "current"
    )

ptpMIBCompliancesClockInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1, 2)
)
ptpMIBCompliancesClockInfo.setObjects(
      *(("AT-PTP-MIB", "ptpMIBClockCurrentDSGroup"),
        ("AT-PTP-MIB", "ptpMIBClockParentDSGroup"),
        ("AT-PTP-MIB", "ptpMIBClockDefaultDSGroup"),
        ("AT-PTP-MIB", "ptpMIBClockRunningGroup"),
        ("AT-PTP-MIB", "ptpMIBClockTimepropertiesGroup"))
)
if mibBuilder.loadTexts:
    ptpMIBCompliancesClockInfo.setStatus(
        "current"
    )

ptpMIBCompliancesClockPortInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1, 3)
)
ptpMIBCompliancesClockPortInfo.setObjects(
      *(("AT-PTP-MIB", "ptpMIBClockPortGroup"),
        ("AT-PTP-MIB", "ptpMIBClockPortDSGroup"),
        ("AT-PTP-MIB", "ptpMIBClockPortRunningGroup"),
        ("AT-PTP-MIB", "ptpMIBClockPortAssociateGroup"))
)
if mibBuilder.loadTexts:
    ptpMIBCompliancesClockPortInfo.setStatus(
        "current"
    )

ptpMIBCompliancesTransparentClockInfo = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 504, 2, 1, 4)
)
ptpMIBCompliancesTransparentClockInfo.setObjects(
      *(("AT-PTP-MIB", "ptpMIBClockTranparentDSGroup"),
        ("AT-PTP-MIB", "ptpMIBClockPortTransDSGroup"))
)
if mibBuilder.loadTexts:
    ptpMIBCompliancesTransparentClockInfo.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-PTP-MIB",
    **{"PtpClockDomainType": PtpClockDomainType,
       "PtpClockIdentity": PtpClockIdentity,
       "PtpClockInstanceType": PtpClockInstanceType,
       "PtpClockIntervalBase2": PtpClockIntervalBase2,
       "PtpClockMechanismType": PtpClockMechanismType,
       "PtpClockPortNumber": PtpClockPortNumber,
       "PtpClockPortState": PtpClockPortState,
       "PtpClockPortTransportTypeAddress": PtpClockPortTransportTypeAddress,
       "PtpClockProfileType": PtpClockProfileType,
       "PtpClockQualityAccuracyType": PtpClockQualityAccuracyType,
       "PtpClockQualityClassType": PtpClockQualityClassType,
       "PtpClockRoleType": PtpClockRoleType,
       "PtpClockStateType": PtpClockStateType,
       "PtpClockTimeInterval": PtpClockTimeInterval,
       "PtpClockTimeSourceType": PtpClockTimeSourceType,
       "PtpClockTxModeType": PtpClockTxModeType,
       "PtpClockType": PtpClockType,
       "atPtpMIB": atPtpMIB,
       "ptpMIBNotifs": ptpMIBNotifs,
       "ptpMIBObjects": ptpMIBObjects,
       "ptpMIBSystemInfo": ptpMIBSystemInfo,
       "ptpSystemTable": ptpSystemTable,
       "ptpSystemEntry": ptpSystemEntry,
       "ptpDomainIndex": ptpDomainIndex,
       "ptpInstanceIndex": ptpInstanceIndex,
       "ptpDomainClockPortsTotal": ptpDomainClockPortsTotal,
       "ptpSystemDomainTable": ptpSystemDomainTable,
       "ptpSystemDomainEntry": ptpSystemDomainEntry,
       "ptpSystemDomainClockTypeIndex": ptpSystemDomainClockTypeIndex,
       "ptpSystemDomainTotals": ptpSystemDomainTotals,
       "ptpSystemProfile": ptpSystemProfile,
       "ptpMIBClockInfo": ptpMIBClockInfo,
       "ptpClockCurrentDSTable": ptpClockCurrentDSTable,
       "ptpClockCurrentDSEntry": ptpClockCurrentDSEntry,
       "ptpClockCurrentDSDomainIndex": ptpClockCurrentDSDomainIndex,
       "ptpClockCurrentDSClockTypeIndex": ptpClockCurrentDSClockTypeIndex,
       "ptpClockCurrentDSInstanceIndex": ptpClockCurrentDSInstanceIndex,
       "ptpClockCurrentDSStepsRemoved": ptpClockCurrentDSStepsRemoved,
       "ptpClockCurrentDSOffsetFromMaster": ptpClockCurrentDSOffsetFromMaster,
       "ptpClockCurrentDSMeanPathDelay": ptpClockCurrentDSMeanPathDelay,
       "ptpClockParentDSTable": ptpClockParentDSTable,
       "ptpClockParentDSEntry": ptpClockParentDSEntry,
       "ptpClockParentDSDomainIndex": ptpClockParentDSDomainIndex,
       "ptpClockParentDSClockTypeIndex": ptpClockParentDSClockTypeIndex,
       "ptpClockParentDSInstanceIndex": ptpClockParentDSInstanceIndex,
       "ptpClockParentDSParentPortIdentity": ptpClockParentDSParentPortIdentity,
       "ptpClockParentDSParentStats": ptpClockParentDSParentStats,
       "ptpClockParentDSOffset": ptpClockParentDSOffset,
       "ptpClockParentDSClockPhChRate": ptpClockParentDSClockPhChRate,
       "ptpClockParentDSGMClockIdentity": ptpClockParentDSGMClockIdentity,
       "ptpClockParentDSGMClockPriority1": ptpClockParentDSGMClockPriority1,
       "ptpClockParentDSGMClockPriority2": ptpClockParentDSGMClockPriority2,
       "ptpClockParentDSGMClockQualityClass": ptpClockParentDSGMClockQualityClass,
       "ptpClockParentDSGMClockQualityAccuracy": ptpClockParentDSGMClockQualityAccuracy,
       "ptpClockParentDSGMClockQualityOffset": ptpClockParentDSGMClockQualityOffset,
       "ptpClockDefaultDSTable": ptpClockDefaultDSTable,
       "ptpClockDefaultDSEntry": ptpClockDefaultDSEntry,
       "ptpClockDefaultDSDomainIndex": ptpClockDefaultDSDomainIndex,
       "ptpClockDefaultDSClockTypeIndex": ptpClockDefaultDSClockTypeIndex,
       "ptpClockDefaultDSInstanceIndex": ptpClockDefaultDSInstanceIndex,
       "ptpClockDefaultDSTwoStepFlag": ptpClockDefaultDSTwoStepFlag,
       "ptpClockDefaultDSClockIdentity": ptpClockDefaultDSClockIdentity,
       "ptpClockDefaultDSPriority1": ptpClockDefaultDSPriority1,
       "ptpClockDefaultDSPriority2": ptpClockDefaultDSPriority2,
       "ptpClockDefaultDSSlaveOnly": ptpClockDefaultDSSlaveOnly,
       "ptpClockDefaultDSQualityClass": ptpClockDefaultDSQualityClass,
       "ptpClockDefaultDSQualityAccuracy": ptpClockDefaultDSQualityAccuracy,
       "ptpClockDefaultDSQualityOffset": ptpClockDefaultDSQualityOffset,
       "ptpClockRunningTable": ptpClockRunningTable,
       "ptpClockRunningEntry": ptpClockRunningEntry,
       "ptpClockRunningDomainIndex": ptpClockRunningDomainIndex,
       "ptpClockRunningClockTypeIndex": ptpClockRunningClockTypeIndex,
       "ptpClockRunningInstanceIndex": ptpClockRunningInstanceIndex,
       "ptpClockRunningState": ptpClockRunningState,
       "ptpClockRunningPacketsSent": ptpClockRunningPacketsSent,
       "ptpClockRunningPacketsReceived": ptpClockRunningPacketsReceived,
       "ptpClockTimePropertiesDSTable": ptpClockTimePropertiesDSTable,
       "ptpClockTimePropertiesDSEntry": ptpClockTimePropertiesDSEntry,
       "ptpClockTimePropertiesDSDomainIndex": ptpClockTimePropertiesDSDomainIndex,
       "ptpClockTimePropertiesDSClockTypeIndex": ptpClockTimePropertiesDSClockTypeIndex,
       "ptpClockTimePropertiesDSInstanceIndex": ptpClockTimePropertiesDSInstanceIndex,
       "ptpClockTimePropertiesDSCurrentUTCOffsetValid": ptpClockTimePropertiesDSCurrentUTCOffsetValid,
       "ptpClockTimePropertiesDSCurrentUTCOffset": ptpClockTimePropertiesDSCurrentUTCOffset,
       "ptpClockTimePropertiesDSLeap59": ptpClockTimePropertiesDSLeap59,
       "ptpClockTimePropertiesDSLeap61": ptpClockTimePropertiesDSLeap61,
       "ptpClockTimePropertiesDSTimeTraceable": ptpClockTimePropertiesDSTimeTraceable,
       "ptpClockTimePropertiesDSFreqTraceable": ptpClockTimePropertiesDSFreqTraceable,
       "ptpClockTimePropertiesDSPTPTimescale": ptpClockTimePropertiesDSPTPTimescale,
       "ptpClockTimePropertiesDSSource": ptpClockTimePropertiesDSSource,
       "ptpClockTransDefaultDSTable": ptpClockTransDefaultDSTable,
       "ptpClockTransDefaultDSEntry": ptpClockTransDefaultDSEntry,
       "ptpClockTransDefaultDSDomainIndex": ptpClockTransDefaultDSDomainIndex,
       "ptpClockTransDefaultDSInstanceIndex": ptpClockTransDefaultDSInstanceIndex,
       "ptpClockTransDefaultDSClockIdentity": ptpClockTransDefaultDSClockIdentity,
       "ptpClockTransDefaultDSNumOfPorts": ptpClockTransDefaultDSNumOfPorts,
       "ptpClockTransDefaultDSDelay": ptpClockTransDefaultDSDelay,
       "ptpClockTransDefaultDSPrimaryDomain": ptpClockTransDefaultDSPrimaryDomain,
       "ptpClockPortTable": ptpClockPortTable,
       "ptpClockPortEntry": ptpClockPortEntry,
       "ptpClockPortDomainIndex": ptpClockPortDomainIndex,
       "ptpClockPortClockTypeIndex": ptpClockPortClockTypeIndex,
       "ptpClockPortClockInstanceIndex": ptpClockPortClockInstanceIndex,
       "ptpClockPortTablePortNumberIndex": ptpClockPortTablePortNumberIndex,
       "ptpClockPortName": ptpClockPortName,
       "ptpClockPortRole": ptpClockPortRole,
       "ptpClockPortSyncTwoStep": ptpClockPortSyncTwoStep,
       "ptpClockPortCurrentPeerAddressType": ptpClockPortCurrentPeerAddressType,
       "ptpClockPortCurrentPeerAddress": ptpClockPortCurrentPeerAddress,
       "ptpClockPortNumOfAssociatedPorts": ptpClockPortNumOfAssociatedPorts,
       "ptpClockPortDSTable": ptpClockPortDSTable,
       "ptpClockPortDSEntry": ptpClockPortDSEntry,
       "ptpClockPortDSDomainIndex": ptpClockPortDSDomainIndex,
       "ptpClockPortDSClockTypeIndex": ptpClockPortDSClockTypeIndex,
       "ptpClockPortDSClockInstanceIndex": ptpClockPortDSClockInstanceIndex,
       "ptpClockPortDSPortNumberIndex": ptpClockPortDSPortNumberIndex,
       "ptpClockPortDSName": ptpClockPortDSName,
       "ptpClockPortDSPortIdentity": ptpClockPortDSPortIdentity,
       "ptpClockPortDSlogAnnouncementInterval": ptpClockPortDSlogAnnouncementInterval,
       "ptpClockPortDSAnnounceRctTimeout": ptpClockPortDSAnnounceRctTimeout,
       "ptpClockPortDSlogSyncInterval": ptpClockPortDSlogSyncInterval,
       "ptpClockPortDSMinDelayReqInterval": ptpClockPortDSMinDelayReqInterval,
       "ptpClockPortDSPeerDelayReqInterval": ptpClockPortDSPeerDelayReqInterval,
       "ptpClockPortDSDelayMech": ptpClockPortDSDelayMech,
       "ptpClockPortDSPeerMeanPathDelay": ptpClockPortDSPeerMeanPathDelay,
       "ptpClockPortDSGrantDuration": ptpClockPortDSGrantDuration,
       "ptpClockPortDSPTPVersion": ptpClockPortDSPTPVersion,
       "ptpClockPortRunningTable": ptpClockPortRunningTable,
       "ptpClockPortRunningEntry": ptpClockPortRunningEntry,
       "ptpClockPortRunningDomainIndex": ptpClockPortRunningDomainIndex,
       "ptpClockPortRunningClockTypeIndex": ptpClockPortRunningClockTypeIndex,
       "ptpClockPortRunningClockInstanceIndex": ptpClockPortRunningClockInstanceIndex,
       "ptpClockPortRunningPortNumberIndex": ptpClockPortRunningPortNumberIndex,
       "ptpClockPortRunningName": ptpClockPortRunningName,
       "ptpClockPortRunningState": ptpClockPortRunningState,
       "ptpClockPortRunningRole": ptpClockPortRunningRole,
       "ptpClockPortRunningInterfaceIndex": ptpClockPortRunningInterfaceIndex,
       "ptpClockPortRunningTransport": ptpClockPortRunningTransport,
       "ptpClockPortRunningEncapsulationType": ptpClockPortRunningEncapsulationType,
       "ptpClockPortRunningTxMode": ptpClockPortRunningTxMode,
       "ptpClockPortRunningRxMode": ptpClockPortRunningRxMode,
       "ptpClockPortRunningPacketsReceived": ptpClockPortRunningPacketsReceived,
       "ptpClockPortRunningPacketsSent": ptpClockPortRunningPacketsSent,
       "ptpClockPortTransDSTable": ptpClockPortTransDSTable,
       "ptpClockPortTransDSEntry": ptpClockPortTransDSEntry,
       "ptpClockPortTransDSDomainIndex": ptpClockPortTransDSDomainIndex,
       "ptpClockPortTransDSInstanceIndex": ptpClockPortTransDSInstanceIndex,
       "ptpClockPortTransDSPortNumberIndex": ptpClockPortTransDSPortNumberIndex,
       "ptpClockPortTransDSPortIdentity": ptpClockPortTransDSPortIdentity,
       "ptpClockPortTransDSlogMinPdelayReqInt": ptpClockPortTransDSlogMinPdelayReqInt,
       "ptpClockPortTransDSFaultyFlag": ptpClockPortTransDSFaultyFlag,
       "ptpClockPortTransDSPeerMeanPathDelay": ptpClockPortTransDSPeerMeanPathDelay,
       "ptpClockPortAssociateTable": ptpClockPortAssociateTable,
       "ptpClockPortAssociateEntry": ptpClockPortAssociateEntry,
       "ptpClockPortCurrentDomainIndex": ptpClockPortCurrentDomainIndex,
       "ptpClockPortCurrentClockTypeIndex": ptpClockPortCurrentClockTypeIndex,
       "ptpClockPortCurrentClockInstanceIndex": ptpClockPortCurrentClockInstanceIndex,
       "ptpClockPortCurrentPortNumberIndex": ptpClockPortCurrentPortNumberIndex,
       "ptpClockPortAssociatePortIndex": ptpClockPortAssociatePortIndex,
       "ptpClockPortAssociateAddressType": ptpClockPortAssociateAddressType,
       "ptpClockPortAssociateAddress": ptpClockPortAssociateAddress,
       "ptpClockPortAssociatePacketsSent": ptpClockPortAssociatePacketsSent,
       "ptpClockPortAssociatePacketsReceived": ptpClockPortAssociatePacketsReceived,
       "ptpClockPortAssociateInErrors": ptpClockPortAssociateInErrors,
       "ptpClockPortAssociateOutErrors": ptpClockPortAssociateOutErrors,
       "ptpWellKnownTransportTypes": ptpWellKnownTransportTypes,
       "ptpTransportTypeIPversion4": ptpTransportTypeIPversion4,
       "ptpTransportTypeIPversion6": ptpTransportTypeIPversion6,
       "ptpTransportTypeEthernet": ptpTransportTypeEthernet,
       "ptpTransportTypeDeviceNET": ptpTransportTypeDeviceNET,
       "ptpTransportTypeControlNET": ptpTransportTypeControlNET,
       "ptpTransportTypeIEC61158": ptpTransportTypeIEC61158,
       "ptpWellKnownEncapsulationTypes": ptpWellKnownEncapsulationTypes,
       "ptpEncapsulationTypeEthernet": ptpEncapsulationTypeEthernet,
       "ptpEncapsulationTypeVLAN": ptpEncapsulationTypeVLAN,
       "ptpEncapsulationTypeUDPIPLSP": ptpEncapsulationTypeUDPIPLSP,
       "ptpEncapsulationTypePWUDPIPLSP": ptpEncapsulationTypePWUDPIPLSP,
       "ptpEncapsulationTypePWEthernetLSP": ptpEncapsulationTypePWEthernetLSP,
       "ptpMIBConformance": ptpMIBConformance,
       "ptpMIBCompliances": ptpMIBCompliances,
       "ptpMIBCompliancesSystemInfo": ptpMIBCompliancesSystemInfo,
       "ptpMIBCompliancesClockInfo": ptpMIBCompliancesClockInfo,
       "ptpMIBCompliancesClockPortInfo": ptpMIBCompliancesClockPortInfo,
       "ptpMIBCompliancesTransparentClockInfo": ptpMIBCompliancesTransparentClockInfo,
       "ptpMIBGroups": ptpMIBGroups,
       "ptpMIBSystemInfoGroup": ptpMIBSystemInfoGroup,
       "ptpMIBClockCurrentDSGroup": ptpMIBClockCurrentDSGroup,
       "ptpMIBClockParentDSGroup": ptpMIBClockParentDSGroup,
       "ptpMIBClockDefaultDSGroup": ptpMIBClockDefaultDSGroup,
       "ptpMIBClockRunningGroup": ptpMIBClockRunningGroup,
       "ptpMIBClockTimepropertiesGroup": ptpMIBClockTimepropertiesGroup,
       "ptpMIBClockTranparentDSGroup": ptpMIBClockTranparentDSGroup,
       "ptpMIBClockPortGroup": ptpMIBClockPortGroup,
       "ptpMIBClockPortDSGroup": ptpMIBClockPortDSGroup,
       "ptpMIBClockPortRunningGroup": ptpMIBClockPortRunningGroup,
       "ptpMIBClockPortTransDSGroup": ptpMIBClockPortTransDSGroup,
       "ptpMIBClockPortAssociateGroup": ptpMIBClockPortAssociateGroup}
)
