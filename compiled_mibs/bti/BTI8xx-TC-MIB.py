# SNMP MIB module (BTI8xx-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\bti\BTI8xx-TC-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:22:37 2025
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

(bti8xx,) = mibBuilder.importSymbols(
    "BTI8xx-MIB",
    "bti8xx")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(PerfCurrentCount,
 PerfIntervalCount,
 PerfTotalCount) = mibBuilder.importSymbols(
    "PerfHist-TC-MIB",
    "PerfCurrentCount",
    "PerfIntervalCount",
    "PerfTotalCount")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

privateManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100)
)
if mibBuilder.loadTexts:
    privateManagement.setRevisions(
        ("2015-11-20 12:00",
         "2015-02-25 15:00",
         "2014-10-29 12:00",
         "2013-12-27 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TcI1588ClkStratum(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              6,
              7,
              128,
              248,
              254,
              255)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("force", 1),
          ("stratum1", 6),
          ("stratum2", 7),
          ("bestClockStratumthatcanbeSlave", 128),
          ("stratum3", 248),
          ("stratum4", 254),
          ("defaultStratum", 255))
    )



class TcI1588ClkAccuracy(TextualConvention, Integer32):
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
        *(("t25ns", 32),
          ("t100ns", 33),
          ("t250ns", 34),
          ("t1us", 35),
          ("t2dot5us", 36),
          ("t10us", 37),
          ("t25us", 38),
          ("t100us", 39),
          ("t250us", 40),
          ("t1ms", 41),
          ("t2dot5ms", 42),
          ("t10ms", 43),
          ("t25ms", 44),
          ("t100ms", 45),
          ("t250ms", 46),
          ("t1s", 47),
          ("t10s", 48),
          ("t10sExcess", 49),
          ("tUnknown", 254))
    )



class TcI1588LogPeriod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              8,
              16,
              32,
              64)
        )
    )
    namedValues = NamedValues(
        *(("period0", 1),
          ("period1", 2),
          ("period2", 4),
          ("period3", 8),
          ("period4", 16),
          ("period5", 32),
          ("period6", 64))
    )



class EnableType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )



class RuleAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )



class CounterClear(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("cleared", 1),
          ("nouse", 2))
    )



class PortOp(TextualConvention, Integer32):
    status = "current"
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
        *(("eq", 0),
          ("neq", 1),
          ("gt", 2),
          ("lt", 3),
          ("range", 4),
          ("invalid", 5))
    )



class PrecedenceValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )



class DSCPValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )



# MIB Managed Objects in the order of their OIDs

_ConfigManagement_ObjectIdentity = ObjectIdentity
configManagement = _ConfigManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1)
)
_SystemInfo_ObjectIdentity = ObjectIdentity
systemInfo = _SystemInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1)
)
_FruInfo_ObjectIdentity = ObjectIdentity
fruInfo = _FruInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1)
)
_FruBaseInfo_ObjectIdentity = ObjectIdentity
fruBaseInfo = _FruBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1)
)
_FruBaseInfoTable_Object = MibTable
fruBaseInfoTable = _FruBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fruBaseInfoTable.setStatus("current")
_FruBaseInfoEntry_Object = MibTableRow
fruBaseInfoEntry = _FruBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1)
)
fruBaseInfoEntry.setIndexNames(
    (0, "BTI8xx-TC-MIB", "fruBaseInfoIndex"),
)
if mibBuilder.loadTexts:
    fruBaseInfoEntry.setStatus("current")


class _FruBaseInfoIndex_Type(Integer32):
    """Custom type fruBaseInfoIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FruBaseInfoIndex_Type.__name__ = "Integer32"
_FruBaseInfoIndex_Object = MibTableColumn
fruBaseInfoIndex = _FruBaseInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 1),
    _FruBaseInfoIndex_Type()
)
fruBaseInfoIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfoIndex.setStatus("current")


class _FruBaseInfoLocation_Type(OctetString):
    """Custom type fruBaseInfoLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FruBaseInfoLocation_Type.__name__ = "OctetString"
_FruBaseInfoLocation_Object = MibTableColumn
fruBaseInfoLocation = _FruBaseInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 2),
    _FruBaseInfoLocation_Type()
)
fruBaseInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfoLocation.setStatus("current")


class _FruBaseInfopackSWVersion_Type(OctetString):
    """Custom type fruBaseInfopackSWVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FruBaseInfopackSWVersion_Type.__name__ = "OctetString"
_FruBaseInfopackSWVersion_Object = MibTableColumn
fruBaseInfopackSWVersion = _FruBaseInfopackSWVersion_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 3),
    _FruBaseInfopackSWVersion_Type()
)
fruBaseInfopackSWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfopackSWVersion.setStatus("current")


class _FruBaseInfopackShortName_Type(OctetString):
    """Custom type fruBaseInfopackShortName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_FruBaseInfopackShortName_Type.__name__ = "OctetString"
_FruBaseInfopackShortName_Object = MibTableColumn
fruBaseInfopackShortName = _FruBaseInfopackShortName_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 4),
    _FruBaseInfopackShortName_Type()
)
fruBaseInfopackShortName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfopackShortName.setStatus("current")


class _FruBaseInfopackName_Type(OctetString):
    """Custom type fruBaseInfopackName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruBaseInfopackName_Type.__name__ = "OctetString"
_FruBaseInfopackName_Object = MibTableColumn
fruBaseInfopackName = _FruBaseInfopackName_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 5),
    _FruBaseInfopackName_Type()
)
fruBaseInfopackName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfopackName.setStatus("current")


class _FruBaseInfoPECCode_Type(OctetString):
    """Custom type fruBaseInfoPECCode based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FruBaseInfoPECCode_Type.__name__ = "OctetString"
_FruBaseInfoPECCode_Object = MibTableColumn
fruBaseInfoPECCode = _FruBaseInfoPECCode_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 6),
    _FruBaseInfoPECCode_Type()
)
fruBaseInfoPECCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfoPECCode.setStatus("current")


class _FruBaseInfoCLEI_Type(OctetString):
    """Custom type fruBaseInfoCLEI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FruBaseInfoCLEI_Type.__name__ = "OctetString"
_FruBaseInfoCLEI_Object = MibTableColumn
fruBaseInfoCLEI = _FruBaseInfoCLEI_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 7),
    _FruBaseInfoCLEI_Type()
)
fruBaseInfoCLEI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfoCLEI.setStatus("current")


class _FruBaseInfoserialNumber_Type(OctetString):
    """Custom type fruBaseInfoserialNumber based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FruBaseInfoserialNumber_Type.__name__ = "OctetString"
_FruBaseInfoserialNumber_Object = MibTableColumn
fruBaseInfoserialNumber = _FruBaseInfoserialNumber_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 8),
    _FruBaseInfoserialNumber_Type()
)
fruBaseInfoserialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfoserialNumber.setStatus("current")


class _FruBaseInforevision_Type(Integer32):
    """Custom type fruBaseInforevision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FruBaseInforevision_Type.__name__ = "Integer32"
_FruBaseInforevision_Object = MibTableColumn
fruBaseInforevision = _FruBaseInforevision_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 9),
    _FruBaseInforevision_Type()
)
fruBaseInforevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInforevision.setStatus("current")


class _FruBaseInfomanufacturingDate_Type(OctetString):
    """Custom type fruBaseInfomanufacturingDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FruBaseInfomanufacturingDate_Type.__name__ = "OctetString"
_FruBaseInfomanufacturingDate_Object = MibTableColumn
fruBaseInfomanufacturingDate = _FruBaseInfomanufacturingDate_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 10),
    _FruBaseInfomanufacturingDate_Type()
)
fruBaseInfomanufacturingDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfomanufacturingDate.setStatus("current")


class _FruBaseInfomanufacturingLoc_Type(OctetString):
    """Custom type fruBaseInfomanufacturingLoc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FruBaseInfomanufacturingLoc_Type.__name__ = "OctetString"
_FruBaseInfomanufacturingLoc_Object = MibTableColumn
fruBaseInfomanufacturingLoc = _FruBaseInfomanufacturingLoc_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 11),
    _FruBaseInfomanufacturingLoc_Type()
)
fruBaseInfomanufacturingLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfomanufacturingLoc.setStatus("current")


class _FruBaseInfotestedDate_Type(OctetString):
    """Custom type fruBaseInfotestedDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_FruBaseInfotestedDate_Type.__name__ = "OctetString"
_FruBaseInfotestedDate_Object = MibTableColumn
fruBaseInfotestedDate = _FruBaseInfotestedDate_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 12),
    _FruBaseInfotestedDate_Type()
)
fruBaseInfotestedDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfotestedDate.setStatus("current")


class _FruBaseInfotestedLoc_Type(OctetString):
    """Custom type fruBaseInfotestedLoc based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FruBaseInfotestedLoc_Type.__name__ = "OctetString"
_FruBaseInfotestedLoc_Object = MibTableColumn
fruBaseInfotestedLoc = _FruBaseInfotestedLoc_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 13),
    _FruBaseInfotestedLoc_Type()
)
fruBaseInfotestedLoc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfotestedLoc.setStatus("current")


class _FruBaseInfobaseMacaddress_Type(OctetString):
    """Custom type fruBaseInfobaseMacaddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_FruBaseInfobaseMacaddress_Type.__name__ = "OctetString"
_FruBaseInfobaseMacaddress_Object = MibTableColumn
fruBaseInfobaseMacaddress = _FruBaseInfobaseMacaddress_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 14),
    _FruBaseInfobaseMacaddress_Type()
)
fruBaseInfobaseMacaddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfobaseMacaddress.setStatus("current")


class _FruBaseInfonumberOfMacAddress_Type(Integer32):
    """Custom type fruBaseInfonumberOfMacAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_FruBaseInfonumberOfMacAddress_Type.__name__ = "Integer32"
_FruBaseInfonumberOfMacAddress_Object = MibTableColumn
fruBaseInfonumberOfMacAddress = _FruBaseInfonumberOfMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 15),
    _FruBaseInfonumberOfMacAddress_Type()
)
fruBaseInfonumberOfMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfonumberOfMacAddress.setStatus("current")


class _FruBaseInfoUSI_Type(OctetString):
    """Custom type fruBaseInfoUSI based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FruBaseInfoUSI_Type.__name__ = "OctetString"
_FruBaseInfoUSI_Object = MibTableColumn
fruBaseInfoUSI = _FruBaseInfoUSI_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 16),
    _FruBaseInfoUSI_Type()
)
fruBaseInfoUSI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfoUSI.setStatus("current")


class _FruBaseInfoIssuedNumber_Type(Integer32):
    """Custom type fruBaseInfoIssuedNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_FruBaseInfoIssuedNumber_Type.__name__ = "Integer32"
_FruBaseInfoIssuedNumber_Object = MibTableColumn
fruBaseInfoIssuedNumber = _FruBaseInfoIssuedNumber_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 1, 1, 1, 1, 17),
    _FruBaseInfoIssuedNumber_Type()
)
fruBaseInfoIssuedNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fruBaseInfoIssuedNumber.setStatus("current")
_ErrorInfo_ObjectIdentity = ObjectIdentity
errorInfo = _ErrorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2)
)
_ErrorInfoCode_Type = Integer32
_ErrorInfoCode_Object = MibScalar
errorInfoCode = _ErrorInfoCode_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2, 1),
    _ErrorInfoCode_Type()
)
errorInfoCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorInfoCode.setStatus("current")
_ErrorInfoDesc_Type = DisplayString
_ErrorInfoDesc_Object = MibScalar
errorInfoDesc = _ErrorInfoDesc_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2, 2),
    _ErrorInfoDesc_Type()
)
errorInfoDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    errorInfoDesc.setStatus("current")


class _ErrorInfoClear_Type(Integer32):
    """Custom type errorInfoClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("clear", 1))
    )


_ErrorInfoClear_Type.__name__ = "Integer32"
_ErrorInfoClear_Object = MibScalar
errorInfoClear = _ErrorInfoClear_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 1, 2, 3),
    _ErrorInfoClear_Type()
)
errorInfoClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    errorInfoClear.setStatus("current")
_MainSystem_ObjectIdentity = ObjectIdentity
mainSystem = _MainSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 1, 2)
)
_PerformanceManagement_ObjectIdentity = ObjectIdentity
performanceManagement = _PerformanceManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 3)
)
_FaultManagement_ObjectIdentity = ObjectIdentity
faultManagement = _FaultManagement_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 4)
)
_PrivateManagementConformance_ObjectIdentity = ObjectIdentity
privateManagementConformance = _PrivateManagementConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 9)
)
_PrivateManagementGroups_ObjectIdentity = ObjectIdentity
privateManagementGroups = _PrivateManagementGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 9, 1)
)
_PrivateManagementCompliances_ObjectIdentity = ObjectIdentity
privateManagementCompliances = _PrivateManagementCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 9, 2)
)
_PrivateManagementTC_ObjectIdentity = ObjectIdentity
privateManagementTC = _PrivateManagementTC_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10)
)


class _PortIndex_Type(Integer32):
    """Custom type portIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 84),
    )


_PortIndex_Type.__name__ = "Integer32"
_PortIndex_Object = MibScalar
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _EthPortIndex_Type(Integer32):
    """Custom type ethPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_EthPortIndex_Type.__name__ = "Integer32"
_EthPortIndex_Object = MibScalar
ethPortIndex = _EthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 3),
    _EthPortIndex_Type()
)
ethPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethPortIndex.setStatus("current")


class _EthopIndex_Type(Integer32):
    """Custom type ethopIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_EthopIndex_Type.__name__ = "Integer32"
_EthopIndex_Object = MibScalar
ethopIndex = _EthopIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 4),
    _EthopIndex_Type()
)
ethopIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ethopIndex.setStatus("current")


class _PowerIndex_Type(Integer32):
    """Custom type powerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_PowerIndex_Type.__name__ = "Integer32"
_PowerIndex_Object = MibScalar
powerIndex = _PowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 5),
    _PowerIndex_Type()
)
powerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    powerIndex.setStatus("current")


class _UniIndex_Type(Integer32):
    """Custom type uniIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_UniIndex_Type.__name__ = "Integer32"
_UniIndex_Object = MibScalar
uniIndex = _UniIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 6),
    _UniIndex_Type()
)
uniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniIndex.setStatus("current")


class _EvcIndex_Type(Unsigned32):
    """Custom type evcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_EvcIndex_Type.__name__ = "Unsigned32"
_EvcIndex_Object = MibScalar
evcIndex = _EvcIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 7),
    _EvcIndex_Type()
)
evcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    evcIndex.setStatus("current")


class _CosIndex_Type(Integer32):
    """Custom type cosIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_CosIndex_Type.__name__ = "Integer32"
_CosIndex_Object = MibScalar
cosIndex = _CosIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 8),
    _CosIndex_Type()
)
cosIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cosIndex.setStatus("current")


class _BwCfgIndex_Type(Integer32):
    """Custom type bwCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BwCfgIndex_Type.__name__ = "Integer32"
_BwCfgIndex_Object = MibScalar
bwCfgIndex = _BwCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 9),
    _BwCfgIndex_Type()
)
bwCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwCfgIndex.setStatus("current")


class _BwpDirection_Type(Integer32):
    """Custom type bwpDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )


_BwpDirection_Type.__name__ = "Integer32"
_BwpDirection_Object = MibScalar
bwpDirection = _BwpDirection_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 10),
    _BwpDirection_Type()
)
bwpDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bwpDirection.setStatus("current")


class _L2cpIndex_Type(Integer32):
    """Custom type l2cpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_L2cpIndex_Type.__name__ = "Integer32"
_L2cpIndex_Object = MibScalar
l2cpIndex = _L2cpIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 11),
    _L2cpIndex_Type()
)
l2cpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    l2cpIndex.setStatus("current")


class _MpIndex_Type(Integer32):
    """Custom type mpIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_MpIndex_Type.__name__ = "Integer32"
_MpIndex_Object = MibScalar
mpIndex = _MpIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 12),
    _MpIndex_Type()
)
mpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mpIndex.setStatus("current")


class _SessionResponderEntryId_Type(Integer32):
    """Custom type sessionResponderEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_SessionResponderEntryId_Type.__name__ = "Integer32"
_SessionResponderEntryId_Object = MibScalar
sessionResponderEntryId = _SessionResponderEntryId_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 13),
    _SessionResponderEntryId_Type()
)
sessionResponderEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionResponderEntryId.setStatus("current")


class _TestSessionFarEndEntryId_Type(Integer32):
    """Custom type testSessionFarEndEntryId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TestSessionFarEndEntryId_Type.__name__ = "Integer32"
_TestSessionFarEndEntryId_Object = MibScalar
testSessionFarEndEntryId = _TestSessionFarEndEntryId_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 14),
    _TestSessionFarEndEntryId_Type()
)
testSessionFarEndEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    testSessionFarEndEntryId.setStatus("current")


class _SessionIndex_Type(Integer32):
    """Custom type sessionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_SessionIndex_Type.__name__ = "Integer32"
_SessionIndex_Object = MibScalar
sessionIndex = _SessionIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 15),
    _SessionIndex_Type()
)
sessionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sessionIndex.setStatus("current")


class _FsIndex_Type(Integer32):
    """Custom type fsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_FsIndex_Type.__name__ = "Integer32"
_FsIndex_Object = MibScalar
fsIndex = _FsIndex_Object(
    (1, 3, 6, 1, 4, 1, 30005, 1, 7, 100, 10, 16),
    _FsIndex_Type()
)
fsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsIndex.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BTI8xx-TC-MIB",
    **{"TcI1588ClkStratum": TcI1588ClkStratum,
       "TcI1588ClkAccuracy": TcI1588ClkAccuracy,
       "TcI1588LogPeriod": TcI1588LogPeriod,
       "EnableType": EnableType,
       "RuleAction": RuleAction,
       "CounterClear": CounterClear,
       "PortOp": PortOp,
       "PrecedenceValue": PrecedenceValue,
       "DSCPValue": DSCPValue,
       "privateManagement": privateManagement,
       "configManagement": configManagement,
       "systemInfo": systemInfo,
       "fruInfo": fruInfo,
       "fruBaseInfo": fruBaseInfo,
       "fruBaseInfoTable": fruBaseInfoTable,
       "fruBaseInfoEntry": fruBaseInfoEntry,
       "fruBaseInfoIndex": fruBaseInfoIndex,
       "fruBaseInfoLocation": fruBaseInfoLocation,
       "fruBaseInfopackSWVersion": fruBaseInfopackSWVersion,
       "fruBaseInfopackShortName": fruBaseInfopackShortName,
       "fruBaseInfopackName": fruBaseInfopackName,
       "fruBaseInfoPECCode": fruBaseInfoPECCode,
       "fruBaseInfoCLEI": fruBaseInfoCLEI,
       "fruBaseInfoserialNumber": fruBaseInfoserialNumber,
       "fruBaseInforevision": fruBaseInforevision,
       "fruBaseInfomanufacturingDate": fruBaseInfomanufacturingDate,
       "fruBaseInfomanufacturingLoc": fruBaseInfomanufacturingLoc,
       "fruBaseInfotestedDate": fruBaseInfotestedDate,
       "fruBaseInfotestedLoc": fruBaseInfotestedLoc,
       "fruBaseInfobaseMacaddress": fruBaseInfobaseMacaddress,
       "fruBaseInfonumberOfMacAddress": fruBaseInfonumberOfMacAddress,
       "fruBaseInfoUSI": fruBaseInfoUSI,
       "fruBaseInfoIssuedNumber": fruBaseInfoIssuedNumber,
       "errorInfo": errorInfo,
       "errorInfoCode": errorInfoCode,
       "errorInfoDesc": errorInfoDesc,
       "errorInfoClear": errorInfoClear,
       "mainSystem": mainSystem,
       "performanceManagement": performanceManagement,
       "faultManagement": faultManagement,
       "privateManagementConformance": privateManagementConformance,
       "privateManagementGroups": privateManagementGroups,
       "privateManagementCompliances": privateManagementCompliances,
       "privateManagementTC": privateManagementTC,
       "portIndex": portIndex,
       "ethPortIndex": ethPortIndex,
       "ethopIndex": ethopIndex,
       "powerIndex": powerIndex,
       "uniIndex": uniIndex,
       "evcIndex": evcIndex,
       "cosIndex": cosIndex,
       "bwCfgIndex": bwCfgIndex,
       "bwpDirection": bwpDirection,
       "l2cpIndex": l2cpIndex,
       "mpIndex": mpIndex,
       "sessionResponderEntryId": sessionResponderEntryId,
       "testSessionFarEndEntryId": testSessionFarEndEntryId,
       "sessionIndex": sessionIndex,
       "fsIndex": fsIndex}
)
