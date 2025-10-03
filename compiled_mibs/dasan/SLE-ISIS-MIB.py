# SNMP MIB module (SLE-ISIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-ISIS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:34 2025
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

(sleMgmt,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "sleMgmt")

(SleControlRequestResultType,
 SleControlStatusType) = mibBuilder.importSymbols(
    "SLE-TC-MIB",
    "SleControlRequestResultType",
    "SleControlStatusType")

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


# MODULE-IDENTITY

sleISIS = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56)
)
if mibBuilder.loadTexts:
    sleISIS.setRevisions(
        ("1970-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleISISBase_ObjectIdentity = ObjectIdentity
sleISISBase = _SleISISBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1)
)
_SleISISBaseInfo_ObjectIdentity = ObjectIdentity
sleISISBaseInfo = _SleISISBaseInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 1)
)


class _SleISISRestartSuppressAdjacency_Type(Integer32):
    """Custom type sleISISRestartSuppressAdjacency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISRestartSuppressAdjacency_Type.__name__ = "Integer32"
_SleISISRestartSuppressAdjacency_Object = MibScalar
sleISISRestartSuppressAdjacency = _SleISISRestartSuppressAdjacency_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 1, 1),
    _SleISISRestartSuppressAdjacency_Type()
)
sleISISRestartSuppressAdjacency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISRestartSuppressAdjacency.setStatus("current")


class _SleISISRestartHelper_Type(Integer32):
    """Custom type sleISISRestartHelper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISRestartHelper_Type.__name__ = "Integer32"
_SleISISRestartHelper_Object = MibScalar
sleISISRestartHelper = _SleISISRestartHelper_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 1, 2),
    _SleISISRestartHelper_Type()
)
sleISISRestartHelper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISRestartHelper.setStatus("current")


class _SleISISRestartGracePeriod_Type(Integer32):
    """Custom type sleISISRestartGracePeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleISISRestartGracePeriod_Type.__name__ = "Integer32"
_SleISISRestartGracePeriod_Object = MibScalar
sleISISRestartGracePeriod = _SleISISRestartGracePeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 1, 3),
    _SleISISRestartGracePeriod_Type()
)
sleISISRestartGracePeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISRestartGracePeriod.setStatus("current")
_SleISISBaseControl_ObjectIdentity = ObjectIdentity
sleISISBaseControl = _SleISISBaseControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2)
)


class _SleISISControlRequest_Type(Integer32):
    """Custom type sleISISControlRequest based on Integer32"""
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
        *(("setISISRestartSuppressAdj", 1),
          ("setISISRestartHelper", 2),
          ("setISISRestartGracefulPeriod", 3),
          ("clearISISClnsNeighbors", 4),
          ("clearISISClnsIsNeighbors", 5),
          ("clearISISCounter", 6),
          ("clearISISInterfaceCounter", 7),
          ("clearISISProcess", 8),
          ("clearISISRoute", 9),
          ("retartISISGraceful", 10),
          ("snmpRestartISIS", 11))
    )


_SleISISControlRequest_Type.__name__ = "Integer32"
_SleISISControlRequest_Object = MibScalar
sleISISControlRequest = _SleISISControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 1),
    _SleISISControlRequest_Type()
)
sleISISControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISControlRequest.setStatus("current")
_SleISISControlStatus_Type = SleControlStatusType
_SleISISControlStatus_Object = MibScalar
sleISISControlStatus = _SleISISControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 2),
    _SleISISControlStatus_Type()
)
sleISISControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISControlStatus.setStatus("current")
_SleISISControlTimer_Type = Gauge32
_SleISISControlTimer_Object = MibScalar
sleISISControlTimer = _SleISISControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 3),
    _SleISISControlTimer_Type()
)
sleISISControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISControlTimer.setStatus("current")
_SleISISControlTimeStamp_Type = TimeTicks
_SleISISControlTimeStamp_Object = MibScalar
sleISISControlTimeStamp = _SleISISControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 4),
    _SleISISControlTimeStamp_Type()
)
sleISISControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISControlTimeStamp.setStatus("current")
_SleISISControlReqResult_Type = SleControlRequestResultType
_SleISISControlReqResult_Object = MibScalar
sleISISControlReqResult = _SleISISControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 5),
    _SleISISControlReqResult_Type()
)
sleISISControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISControlReqResult.setStatus("current")


class _SleISISControlRestartSuppressAdjacency_Type(Integer32):
    """Custom type sleISISControlRestartSuppressAdjacency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("diable", 0),
          ("enable", 1))
    )


_SleISISControlRestartSuppressAdjacency_Type.__name__ = "Integer32"
_SleISISControlRestartSuppressAdjacency_Object = MibScalar
sleISISControlRestartSuppressAdjacency = _SleISISControlRestartSuppressAdjacency_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 6),
    _SleISISControlRestartSuppressAdjacency_Type()
)
sleISISControlRestartSuppressAdjacency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISControlRestartSuppressAdjacency.setStatus("current")


class _SleISISControlRestartHelper_Type(Integer32):
    """Custom type sleISISControlRestartHelper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISControlRestartHelper_Type.__name__ = "Integer32"
_SleISISControlRestartHelper_Object = MibScalar
sleISISControlRestartHelper = _SleISISControlRestartHelper_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 7),
    _SleISISControlRestartHelper_Type()
)
sleISISControlRestartHelper.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISControlRestartHelper.setStatus("current")


class _SleISISControlRestartPeriod_Type(Integer32):
    """Custom type sleISISControlRestartPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1800),
    )


_SleISISControlRestartPeriod_Type.__name__ = "Integer32"
_SleISISControlRestartPeriod_Object = MibScalar
sleISISControlRestartPeriod = _SleISISControlRestartPeriod_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 8),
    _SleISISControlRestartPeriod_Type()
)
sleISISControlRestartPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISControlRestartPeriod.setStatus("current")


class _SleISISControlClearSystemId_Type(OctetString):
    """Custom type sleISISControlClearSystemId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleISISControlClearSystemId_Type.__name__ = "OctetString"
_SleISISControlClearSystemId_Object = MibScalar
sleISISControlClearSystemId = _SleISISControlClearSystemId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 9),
    _SleISISControlClearSystemId_Type()
)
sleISISControlClearSystemId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISControlClearSystemId.setStatus("current")


class _SleISISControlClearIfName_Type(OctetString):
    """Custom type sleISISControlClearIfName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleISISControlClearIfName_Type.__name__ = "OctetString"
_SleISISControlClearIfName_Object = MibScalar
sleISISControlClearIfName = _SleISISControlClearIfName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 10),
    _SleISISControlClearIfName_Type()
)
sleISISControlClearIfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISControlClearIfName.setStatus("current")


class _SleISISControlClearRouteTag_Type(OctetString):
    """Custom type sleISISControlClearRouteTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleISISControlClearRouteTag_Type.__name__ = "OctetString"
_SleISISControlClearRouteTag_Object = MibScalar
sleISISControlClearRouteTag = _SleISISControlClearRouteTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 11),
    _SleISISControlClearRouteTag_Type()
)
sleISISControlClearRouteTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISControlClearRouteTag.setStatus("current")


class _SleISISControlClearRouteMode_Type(Integer32):
    """Custom type sleISISControlClearRouteMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("redistribution", 1),
          ("all", 2))
    )


_SleISISControlClearRouteMode_Type.__name__ = "Integer32"
_SleISISControlClearRouteMode_Object = MibScalar
sleISISControlClearRouteMode = _SleISISControlClearRouteMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 2, 12),
    _SleISISControlClearRouteMode_Type()
)
sleISISControlClearRouteMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISControlClearRouteMode.setStatus("current")
_SleISISBaseNotification_ObjectIdentity = ObjectIdentity
sleISISBaseNotification = _SleISISBaseNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 1, 3)
)
_SleISISProc_ObjectIdentity = ObjectIdentity
sleISISProc = _SleISISProc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2)
)
_SleISISProcInfo_ObjectIdentity = ObjectIdentity
sleISISProcInfo = _SleISISProcInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1)
)
_SleISISProcInfoTable_Object = MibTable
sleISISProcInfoTable = _SleISISProcInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1)
)
if mibBuilder.loadTexts:
    sleISISProcInfoTable.setStatus("current")
_SleISISProcInfoEntry_Object = MibTableRow
sleISISProcInfoEntry = _SleISISProcInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1)
)
sleISISProcInfoEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISProcInfoInstanceID"),
)
if mibBuilder.loadTexts:
    sleISISProcInfoEntry.setStatus("current")


class _SleISISProcInfoInstanceID_Type(Integer32):
    """Custom type sleISISProcInfoInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleISISProcInfoInstanceID_Type.__name__ = "Integer32"
_SleISISProcInfoInstanceID_Object = MibTableColumn
sleISISProcInfoInstanceID = _SleISISProcInfoInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 1),
    _SleISISProcInfoInstanceID_Type()
)
sleISISProcInfoInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcInfoInstanceID.setStatus("current")
_SleISISProcInfoTag_Type = OctetString
_SleISISProcInfoTag_Object = MibTableColumn
sleISISProcInfoTag = _SleISISProcInfoTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 2),
    _SleISISProcInfoTag_Type()
)
sleISISProcInfoTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcInfoTag.setStatus("current")


class _SleISISProcBfdAllInterface_Type(Integer32):
    """Custom type sleISISProcBfdAllInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcBfdAllInterface_Type.__name__ = "Integer32"
_SleISISProcBfdAllInterface_Object = MibTableColumn
sleISISProcBfdAllInterface = _SleISISProcBfdAllInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 3),
    _SleISISProcBfdAllInterface_Type()
)
sleISISProcBfdAllInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcBfdAllInterface.setStatus("current")


class _SleISISProcCapCspf_Type(Integer32):
    """Custom type sleISISProcCapCspf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcCapCspf_Type.__name__ = "Integer32"
_SleISISProcCapCspf_Object = MibTableColumn
sleISISProcCapCspf = _SleISISProcCapCspf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 4),
    _SleISISProcCapCspf_Type()
)
sleISISProcCapCspf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcCapCspf.setStatus("current")


class _SleISISProcDynHostname_Type(Integer32):
    """Custom type sleISISProcDynHostname based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcDynHostname_Type.__name__ = "Integer32"
_SleISISProcDynHostname_Object = MibTableColumn
sleISISProcDynHostname = _SleISISProcDynHostname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 5),
    _SleISISProcDynHostname_Type()
)
sleISISProcDynHostname.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDynHostname.setStatus("current")


class _SleISISProcDynHostnameAreaTag_Type(Integer32):
    """Custom type sleISISProcDynHostnameAreaTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcDynHostnameAreaTag_Type.__name__ = "Integer32"
_SleISISProcDynHostnameAreaTag_Object = MibTableColumn
sleISISProcDynHostnameAreaTag = _SleISISProcDynHostnameAreaTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 6),
    _SleISISProcDynHostnameAreaTag_Type()
)
sleISISProcDynHostnameAreaTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDynHostnameAreaTag.setStatus("current")


class _SleISISProcIgnLspErr_Type(Integer32):
    """Custom type sleISISProcIgnLspErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcIgnLspErr_Type.__name__ = "Integer32"
_SleISISProcIgnLspErr_Object = MibTableColumn
sleISISProcIgnLspErr = _SleISISProcIgnLspErr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 7),
    _SleISISProcIgnLspErr_Type()
)
sleISISProcIgnLspErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcIgnLspErr.setStatus("current")


class _SleISISProcRouteHighPriorityTag_Type(Gauge32):
    """Custom type sleISISProcRouteHighPriorityTag based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleISISProcRouteHighPriorityTag_Type.__name__ = "Gauge32"
_SleISISProcRouteHighPriorityTag_Object = MibTableColumn
sleISISProcRouteHighPriorityTag = _SleISISProcRouteHighPriorityTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 8),
    _SleISISProcRouteHighPriorityTag_Type()
)
sleISISProcRouteHighPriorityTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcRouteHighPriorityTag.setStatus("current")


class _SleISISProcIspfLevel_Type(Integer32):
    """Custom type sleISISProcIspfLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2only", 3))
    )


_SleISISProcIspfLevel_Type.__name__ = "Integer32"
_SleISISProcIspfLevel_Object = MibTableColumn
sleISISProcIspfLevel = _SleISISProcIspfLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 9),
    _SleISISProcIspfLevel_Type()
)
sleISISProcIspfLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcIspfLevel.setStatus("current")


class _SleISISProcIsTypeLevel_Type(Integer32):
    """Custom type sleISISProcIsTypeLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcIsTypeLevel_Type.__name__ = "Integer32"
_SleISISProcIsTypeLevel_Object = MibTableColumn
sleISISProcIsTypeLevel = _SleISISProcIsTypeLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 10),
    _SleISISProcIsTypeLevel_Type()
)
sleISISProcIsTypeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcIsTypeLevel.setStatus("current")


class _SleISISProcLspGenInterval_Type(Integer32):
    """Custom type sleISISProcLspGenInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SleISISProcLspGenInterval_Type.__name__ = "Integer32"
_SleISISProcLspGenInterval_Object = MibTableColumn
sleISISProcLspGenInterval = _SleISISProcLspGenInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 11),
    _SleISISProcLspGenInterval_Type()
)
sleISISProcLspGenInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcLspGenInterval.setStatus("current")


class _SleISISProcLspGenIntervalLevel_Type(Integer32):
    """Custom type sleISISProcLspGenIntervalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcLspGenIntervalLevel_Type.__name__ = "Integer32"
_SleISISProcLspGenIntervalLevel_Object = MibTableColumn
sleISISProcLspGenIntervalLevel = _SleISISProcLspGenIntervalLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 12),
    _SleISISProcLspGenIntervalLevel_Type()
)
sleISISProcLspGenIntervalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcLspGenIntervalLevel.setStatus("current")


class _SleISISProcLspMtu_Type(Integer32):
    """Custom type sleISISProcLspMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1492),
    )


_SleISISProcLspMtu_Type.__name__ = "Integer32"
_SleISISProcLspMtu_Object = MibTableColumn
sleISISProcLspMtu = _SleISISProcLspMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 13),
    _SleISISProcLspMtu_Type()
)
sleISISProcLspMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcLspMtu.setStatus("current")


class _SleISISProcLspMtuLevel_Type(Integer32):
    """Custom type sleISISProcLspMtuLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcLspMtuLevel_Type.__name__ = "Integer32"
_SleISISProcLspMtuLevel_Object = MibTableColumn
sleISISProcLspMtuLevel = _SleISISProcLspMtuLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 14),
    _SleISISProcLspMtuLevel_Type()
)
sleISISProcLspMtuLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcLspMtuLevel.setStatus("current")


class _SleISISProcLspRefreshInterval_Type(Integer32):
    """Custom type sleISISProcLspRefreshInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISProcLspRefreshInterval_Type.__name__ = "Integer32"
_SleISISProcLspRefreshInterval_Object = MibTableColumn
sleISISProcLspRefreshInterval = _SleISISProcLspRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 15),
    _SleISISProcLspRefreshInterval_Type()
)
sleISISProcLspRefreshInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcLspRefreshInterval.setStatus("current")


class _SleISISProcMaxAreaAddressNum_Type(Integer32):
    """Custom type sleISISProcMaxAreaAddressNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 254),
    )


_SleISISProcMaxAreaAddressNum_Type.__name__ = "Integer32"
_SleISISProcMaxAreaAddressNum_Object = MibTableColumn
sleISISProcMaxAreaAddressNum = _SleISISProcMaxAreaAddressNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 16),
    _SleISISProcMaxAreaAddressNum_Type()
)
sleISISProcMaxAreaAddressNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcMaxAreaAddressNum.setStatus("current")


class _SleISISProcMaxLspLifetime_Type(Integer32):
    """Custom type sleISISProcMaxLspLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_SleISISProcMaxLspLifetime_Type.__name__ = "Integer32"
_SleISISProcMaxLspLifetime_Object = MibTableColumn
sleISISProcMaxLspLifetime = _SleISISProcMaxLspLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 17),
    _SleISISProcMaxLspLifetime_Type()
)
sleISISProcMaxLspLifetime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcMaxLspLifetime.setStatus("current")


class _SleISISProcMetricStyle_Type(Integer32):
    """Custom type sleISISProcMetricStyle based on Integer32"""
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
        *(("none", 0),
          ("wide", 1),
          ("wideTransition", 2),
          ("transition", 3),
          ("narrowTransition", 4))
    )


_SleISISProcMetricStyle_Type.__name__ = "Integer32"
_SleISISProcMetricStyle_Object = MibTableColumn
sleISISProcMetricStyle = _SleISISProcMetricStyle_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 18),
    _SleISISProcMetricStyle_Type()
)
sleISISProcMetricStyle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcMetricStyle.setStatus("current")


class _SleISISProcMetricStyleLevel_Type(Integer32):
    """Custom type sleISISProcMetricStyleLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcMetricStyleLevel_Type.__name__ = "Integer32"
_SleISISProcMetricStyleLevel_Object = MibTableColumn
sleISISProcMetricStyleLevel = _SleISISProcMetricStyleLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 19),
    _SleISISProcMetricStyleLevel_Type()
)
sleISISProcMetricStyleLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcMetricStyleLevel.setStatus("current")


class _SleISISProcMplsTrafficEngLevel_Type(Integer32):
    """Custom type sleISISProcMplsTrafficEngLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcMplsTrafficEngLevel_Type.__name__ = "Integer32"
_SleISISProcMplsTrafficEngLevel_Object = MibTableColumn
sleISISProcMplsTrafficEngLevel = _SleISISProcMplsTrafficEngLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 20),
    _SleISISProcMplsTrafficEngLevel_Type()
)
sleISISProcMplsTrafficEngLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcMplsTrafficEngLevel.setStatus("current")
_SleISISProcMplsTrafficEngRouterID_Type = IpAddress
_SleISISProcMplsTrafficEngRouterID_Object = MibTableColumn
sleISISProcMplsTrafficEngRouterID = _SleISISProcMplsTrafficEngRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 21),
    _SleISISProcMplsTrafficEngRouterID_Type()
)
sleISISProcMplsTrafficEngRouterID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcMplsTrafficEngRouterID.setStatus("current")


class _SleISISProcPrcIntervalExpMinDelay_Type(Integer32):
    """Custom type sleISISProcPrcIntervalExpMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleISISProcPrcIntervalExpMinDelay_Type.__name__ = "Integer32"
_SleISISProcPrcIntervalExpMinDelay_Object = MibTableColumn
sleISISProcPrcIntervalExpMinDelay = _SleISISProcPrcIntervalExpMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 22),
    _SleISISProcPrcIntervalExpMinDelay_Type()
)
sleISISProcPrcIntervalExpMinDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcPrcIntervalExpMinDelay.setStatus("current")


class _SleISISProcPrcIntervalExpMaxDelay_Type(Integer32):
    """Custom type sleISISProcPrcIntervalExpMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleISISProcPrcIntervalExpMaxDelay_Type.__name__ = "Integer32"
_SleISISProcPrcIntervalExpMaxDelay_Object = MibTableColumn
sleISISProcPrcIntervalExpMaxDelay = _SleISISProcPrcIntervalExpMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 23),
    _SleISISProcPrcIntervalExpMaxDelay_Type()
)
sleISISProcPrcIntervalExpMaxDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcPrcIntervalExpMaxDelay.setStatus("current")


class _SleISISProcProtocolTopolgy_Type(Integer32):
    """Custom type sleISISProcProtocolTopolgy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcProtocolTopolgy_Type.__name__ = "Integer32"
_SleISISProcProtocolTopolgy_Object = MibTableColumn
sleISISProcProtocolTopolgy = _SleISISProcProtocolTopolgy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 24),
    _SleISISProcProtocolTopolgy_Type()
)
sleISISProcProtocolTopolgy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcProtocolTopolgy.setStatus("current")


class _SleISISProcRestartTimerVal_Type(Integer32):
    """Custom type sleISISProcRestartTimerVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_SleISISProcRestartTimerVal_Type.__name__ = "Integer32"
_SleISISProcRestartTimerVal_Object = MibTableColumn
sleISISProcRestartTimerVal = _SleISISProcRestartTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 25),
    _SleISISProcRestartTimerVal_Type()
)
sleISISProcRestartTimerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcRestartTimerVal.setStatus("current")


class _SleISISProcRestartTimerLevel_Type(Integer32):
    """Custom type sleISISProcRestartTimerLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcRestartTimerLevel_Type.__name__ = "Integer32"
_SleISISProcRestartTimerLevel_Object = MibTableColumn
sleISISProcRestartTimerLevel = _SleISISProcRestartTimerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 26),
    _SleISISProcRestartTimerLevel_Type()
)
sleISISProcRestartTimerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcRestartTimerLevel.setStatus("current")


class _SleISISProcSpfIntervalExpMin_Type(Integer32):
    """Custom type sleISISProcSpfIntervalExpMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleISISProcSpfIntervalExpMin_Type.__name__ = "Integer32"
_SleISISProcSpfIntervalExpMin_Object = MibTableColumn
sleISISProcSpfIntervalExpMin = _SleISISProcSpfIntervalExpMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 27),
    _SleISISProcSpfIntervalExpMin_Type()
)
sleISISProcSpfIntervalExpMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcSpfIntervalExpMin.setStatus("current")


class _SleISISProcSpfIntervalExpMax_Type(Integer32):
    """Custom type sleISISProcSpfIntervalExpMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleISISProcSpfIntervalExpMax_Type.__name__ = "Integer32"
_SleISISProcSpfIntervalExpMax_Object = MibTableColumn
sleISISProcSpfIntervalExpMax = _SleISISProcSpfIntervalExpMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 28),
    _SleISISProcSpfIntervalExpMax_Type()
)
sleISISProcSpfIntervalExpMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcSpfIntervalExpMax.setStatus("current")


class _SleISISProcSpfIntervalExpLevel_Type(Integer32):
    """Custom type sleISISProcSpfIntervalExpLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcSpfIntervalExpLevel_Type.__name__ = "Integer32"
_SleISISProcSpfIntervalExpLevel_Object = MibTableColumn
sleISISProcSpfIntervalExpLevel = _SleISISProcSpfIntervalExpLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 29),
    _SleISISProcSpfIntervalExpLevel_Type()
)
sleISISProcSpfIntervalExpLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcSpfIntervalExpLevel.setStatus("current")


class _SleISISProcAuthMode_Type(Integer32):
    """Custom type sleISISProcAuthMode based on Integer32"""
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
        *(("none", 0),
          ("md5", 1),
          ("text", 2),
          ("md5Text", 3))
    )


_SleISISProcAuthMode_Type.__name__ = "Integer32"
_SleISISProcAuthMode_Object = MibTableColumn
sleISISProcAuthMode = _SleISISProcAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 30),
    _SleISISProcAuthMode_Type()
)
sleISISProcAuthMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcAuthMode.setStatus("current")


class _SleISISProcAuthModeLevel_Type(Integer32):
    """Custom type sleISISProcAuthModeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcAuthModeLevel_Type.__name__ = "Integer32"
_SleISISProcAuthModeLevel_Object = MibTableColumn
sleISISProcAuthModeLevel = _SleISISProcAuthModeLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 31),
    _SleISISProcAuthModeLevel_Type()
)
sleISISProcAuthModeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcAuthModeLevel.setStatus("current")


class _SleISISProcAuthSendOnly_Type(Integer32):
    """Custom type sleISISProcAuthSendOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcAuthSendOnly_Type.__name__ = "Integer32"
_SleISISProcAuthSendOnly_Object = MibTableColumn
sleISISProcAuthSendOnly = _SleISISProcAuthSendOnly_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 32),
    _SleISISProcAuthSendOnly_Type()
)
sleISISProcAuthSendOnly.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcAuthSendOnly.setStatus("current")


class _SleISISProcAuthSendOnlyLevel_Type(Integer32):
    """Custom type sleISISProcAuthSendOnlyLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcAuthSendOnlyLevel_Type.__name__ = "Integer32"
_SleISISProcAuthSendOnlyLevel_Object = MibTableColumn
sleISISProcAuthSendOnlyLevel = _SleISISProcAuthSendOnlyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 33),
    _SleISISProcAuthSendOnlyLevel_Type()
)
sleISISProcAuthSendOnlyLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcAuthSendOnlyLevel.setStatus("current")


class _SleISISProcDomPassVal_Type(OctetString):
    """Custom type sleISISProcDomPassVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleISISProcDomPassVal_Type.__name__ = "OctetString"
_SleISISProcDomPassVal_Object = MibTableColumn
sleISISProcDomPassVal = _SleISISProcDomPassVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 34),
    _SleISISProcDomPassVal_Type()
)
sleISISProcDomPassVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDomPassVal.setStatus("current")


class _SleISISProcDomPassAuthSnp_Type(Integer32):
    """Custom type sleISISProcDomPassAuthSnp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("validate", 1),
          ("sendOnly", 2))
    )


_SleISISProcDomPassAuthSnp_Type.__name__ = "Integer32"
_SleISISProcDomPassAuthSnp_Object = MibTableColumn
sleISISProcDomPassAuthSnp = _SleISISProcDomPassAuthSnp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 35),
    _SleISISProcDomPassAuthSnp_Type()
)
sleISISProcDomPassAuthSnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDomPassAuthSnp.setStatus("current")


class _SleISISProcAreaPassVal_Type(OctetString):
    """Custom type sleISISProcAreaPassVal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleISISProcAreaPassVal_Type.__name__ = "OctetString"
_SleISISProcAreaPassVal_Object = MibTableColumn
sleISISProcAreaPassVal = _SleISISProcAreaPassVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 36),
    _SleISISProcAreaPassVal_Type()
)
sleISISProcAreaPassVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcAreaPassVal.setStatus("current")


class _SleISISProcAreaPassAuthSnp_Type(Integer32):
    """Custom type sleISISProcAreaPassAuthSnp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("validate", 1),
          ("sendOnly", 2))
    )


_SleISISProcAreaPassAuthSnp_Type.__name__ = "Integer32"
_SleISISProcAreaPassAuthSnp_Object = MibTableColumn
sleISISProcAreaPassAuthSnp = _SleISISProcAreaPassAuthSnp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 37),
    _SleISISProcAreaPassAuthSnp_Type()
)
sleISISProcAreaPassAuthSnp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcAreaPassAuthSnp.setStatus("current")


class _SleISISProcSetOverloadBit_Type(Integer32):
    """Custom type sleISISProcSetOverloadBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcSetOverloadBit_Type.__name__ = "Integer32"
_SleISISProcSetOverloadBit_Object = MibTableColumn
sleISISProcSetOverloadBit = _SleISISProcSetOverloadBit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 38),
    _SleISISProcSetOverloadBit_Type()
)
sleISISProcSetOverloadBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcSetOverloadBit.setStatus("current")


class _SleISISProcSetOverloadBitOnStartup_Type(Integer32):
    """Custom type sleISISProcSetOverloadBitOnStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("overload", 1),
          ("waitForBgp", 2))
    )


_SleISISProcSetOverloadBitOnStartup_Type.__name__ = "Integer32"
_SleISISProcSetOverloadBitOnStartup_Object = MibTableColumn
sleISISProcSetOverloadBitOnStartup = _SleISISProcSetOverloadBitOnStartup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 39),
    _SleISISProcSetOverloadBitOnStartup_Type()
)
sleISISProcSetOverloadBitOnStartup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcSetOverloadBitOnStartup.setStatus("current")


class _SleISISProcSetOverloadBitOnStartupInterval_Type(Integer32):
    """Custom type sleISISProcSetOverloadBitOnStartupInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_SleISISProcSetOverloadBitOnStartupInterval_Type.__name__ = "Integer32"
_SleISISProcSetOverloadBitOnStartupInterval_Object = MibTableColumn
sleISISProcSetOverloadBitOnStartupInterval = _SleISISProcSetOverloadBitOnStartupInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 40),
    _SleISISProcSetOverloadBitOnStartupInterval_Type()
)
sleISISProcSetOverloadBitOnStartupInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcSetOverloadBitOnStartupInterval.setStatus("current")


class _SleISISProcSetOverloadBitSuppress_Type(Integer32):
    """Custom type sleISISProcSetOverloadBitSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("external", 1),
          ("interlevel", 2))
    )


_SleISISProcSetOverloadBitSuppress_Type.__name__ = "Integer32"
_SleISISProcSetOverloadBitSuppress_Object = MibTableColumn
sleISISProcSetOverloadBitSuppress = _SleISISProcSetOverloadBitSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 41),
    _SleISISProcSetOverloadBitSuppress_Type()
)
sleISISProcSetOverloadBitSuppress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcSetOverloadBitSuppress.setStatus("current")


class _SleISISProcWaitTimerVal_Type(Integer32):
    """Custom type sleISISProcWaitTimerVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISProcWaitTimerVal_Type.__name__ = "Integer32"
_SleISISProcWaitTimerVal_Object = MibTableColumn
sleISISProcWaitTimerVal = _SleISISProcWaitTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 42),
    _SleISISProcWaitTimerVal_Type()
)
sleISISProcWaitTimerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcWaitTimerVal.setStatus("current")


class _SleISISProcWaitTimerLevel_Type(Integer32):
    """Custom type sleISISProcWaitTimerLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcWaitTimerLevel_Type.__name__ = "Integer32"
_SleISISProcWaitTimerLevel_Object = MibTableColumn
sleISISProcWaitTimerLevel = _SleISISProcWaitTimerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 43),
    _SleISISProcWaitTimerLevel_Type()
)
sleISISProcWaitTimerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcWaitTimerLevel.setStatus("current")
_SleISISProcAuthenKeyChainL1_Type = OctetString
_SleISISProcAuthenKeyChainL1_Object = MibTableColumn
sleISISProcAuthenKeyChainL1 = _SleISISProcAuthenKeyChainL1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 44),
    _SleISISProcAuthenKeyChainL1_Type()
)
sleISISProcAuthenKeyChainL1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcAuthenKeyChainL1.setStatus("current")
_SleISISProcAuthenKeyChainL2_Type = OctetString
_SleISISProcAuthenKeyChainL2_Object = MibTableColumn
sleISISProcAuthenKeyChainL2 = _SleISISProcAuthenKeyChainL2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 45),
    _SleISISProcAuthenKeyChainL2_Type()
)
sleISISProcAuthenKeyChainL2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcAuthenKeyChainL2.setStatus("current")
_SleISISProcAuthenKeyChainL1L2_Type = OctetString
_SleISISProcAuthenKeyChainL1L2_Object = MibTableColumn
sleISISProcAuthenKeyChainL1L2 = _SleISISProcAuthenKeyChainL1L2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 1, 1, 46),
    _SleISISProcAuthenKeyChainL1L2_Type()
)
sleISISProcAuthenKeyChainL1L2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcAuthenKeyChainL1L2.setStatus("current")
_SleISISProcInfoControl_ObjectIdentity = ObjectIdentity
sleISISProcInfoControl = _SleISISProcInfoControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2)
)


class _SleISISProcInfoControlRequest_Type(Integer32):
    """Custom type sleISISProcInfoControlRequest based on Integer32"""
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
              26,
              27,
              28,
              29)
        )
    )
    namedValues = NamedValues(
        *(("createISISProcess", 1),
          ("deleteISISProcess", 2),
          ("setISISProcBfdAllInterface", 3),
          ("setISISProcCapabilityCspf", 4),
          ("setISISProcDynamicHostname", 5),
          ("setISISProcIgnoreLspErr", 6),
          ("setISISProcRouteHighPriorityTag", 7),
          ("setISISProcIspfLevel", 8),
          ("setISISProcIsTypeLevel", 9),
          ("setISISProcLspGenInterval", 10),
          ("setISISProcLspMtu", 11),
          ("setISISProcLspRefreshInterval", 12),
          ("setISISProcMaxAreaAddress", 13),
          ("setISISProcMaxLspLifetime", 14),
          ("setISISProcMetricStyle", 15),
          ("setISISProcMplsTrafficEngLevel", 16),
          ("setISISProcMplsTrafficEngRouterID", 17),
          ("setISISProcPrcIntervalExp", 18),
          ("setISISProcProtocoalTopology", 19),
          ("setISISProcRestartTimer", 20),
          ("setISISProcSpfIntervalExp", 21),
          ("setISISProcAuthMode", 22),
          ("setISISProcAuthSendOnly", 23),
          ("setISISProcDomPassword", 24),
          ("setISISProcAreaPassword", 25),
          ("setISISProcSetOverloadBit", 26),
          ("setISISProcWaitTimer", 27),
          ("setISISProcAuthenKeyChain", 28),
          ("delISISProcAuthenKeyChain", 29))
    )


_SleISISProcInfoControlRequest_Type.__name__ = "Integer32"
_SleISISProcInfoControlRequest_Object = MibScalar
sleISISProcInfoControlRequest = _SleISISProcInfoControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 1),
    _SleISISProcInfoControlRequest_Type()
)
sleISISProcInfoControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlRequest.setStatus("current")
_SleISISProcInfoControlStatus_Type = SleControlStatusType
_SleISISProcInfoControlStatus_Object = MibScalar
sleISISProcInfoControlStatus = _SleISISProcInfoControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 2),
    _SleISISProcInfoControlStatus_Type()
)
sleISISProcInfoControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcInfoControlStatus.setStatus("current")
_SleISISProcInfoControlTimer_Type = Gauge32
_SleISISProcInfoControlTimer_Object = MibScalar
sleISISProcInfoControlTimer = _SleISISProcInfoControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 3),
    _SleISISProcInfoControlTimer_Type()
)
sleISISProcInfoControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlTimer.setStatus("current")
_SleISISProcInfoControlTimeStamp_Type = TimeTicks
_SleISISProcInfoControlTimeStamp_Object = MibScalar
sleISISProcInfoControlTimeStamp = _SleISISProcInfoControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 4),
    _SleISISProcInfoControlTimeStamp_Type()
)
sleISISProcInfoControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcInfoControlTimeStamp.setStatus("current")
_SleISISProcInfoControlReqResult_Type = SleControlRequestResultType
_SleISISProcInfoControlReqResult_Object = MibScalar
sleISISProcInfoControlReqResult = _SleISISProcInfoControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 5),
    _SleISISProcInfoControlReqResult_Type()
)
sleISISProcInfoControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcInfoControlReqResult.setStatus("current")


class _SleISISProcInfoControlTag_Type(OctetString):
    """Custom type sleISISProcInfoControlTag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleISISProcInfoControlTag_Type.__name__ = "OctetString"
_SleISISProcInfoControlTag_Object = MibScalar
sleISISProcInfoControlTag = _SleISISProcInfoControlTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 6),
    _SleISISProcInfoControlTag_Type()
)
sleISISProcInfoControlTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlTag.setStatus("current")


class _SleISISProcInfoControlBfdAllInterface_Type(Integer32):
    """Custom type sleISISProcInfoControlBfdAllInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcInfoControlBfdAllInterface_Type.__name__ = "Integer32"
_SleISISProcInfoControlBfdAllInterface_Object = MibScalar
sleISISProcInfoControlBfdAllInterface = _SleISISProcInfoControlBfdAllInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 7),
    _SleISISProcInfoControlBfdAllInterface_Type()
)
sleISISProcInfoControlBfdAllInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlBfdAllInterface.setStatus("current")


class _SleISISProcInfoControlCapCspf_Type(Integer32):
    """Custom type sleISISProcInfoControlCapCspf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcInfoControlCapCspf_Type.__name__ = "Integer32"
_SleISISProcInfoControlCapCspf_Object = MibScalar
sleISISProcInfoControlCapCspf = _SleISISProcInfoControlCapCspf_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 8),
    _SleISISProcInfoControlCapCspf_Type()
)
sleISISProcInfoControlCapCspf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlCapCspf.setStatus("current")


class _SleISISProcInfoControlDynHostname_Type(Integer32):
    """Custom type sleISISProcInfoControlDynHostname based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcInfoControlDynHostname_Type.__name__ = "Integer32"
_SleISISProcInfoControlDynHostname_Object = MibScalar
sleISISProcInfoControlDynHostname = _SleISISProcInfoControlDynHostname_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 9),
    _SleISISProcInfoControlDynHostname_Type()
)
sleISISProcInfoControlDynHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlDynHostname.setStatus("current")


class _SleISISProcInfoControlDynHostnameAreaTag_Type(Integer32):
    """Custom type sleISISProcInfoControlDynHostnameAreaTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcInfoControlDynHostnameAreaTag_Type.__name__ = "Integer32"
_SleISISProcInfoControlDynHostnameAreaTag_Object = MibScalar
sleISISProcInfoControlDynHostnameAreaTag = _SleISISProcInfoControlDynHostnameAreaTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 10),
    _SleISISProcInfoControlDynHostnameAreaTag_Type()
)
sleISISProcInfoControlDynHostnameAreaTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlDynHostnameAreaTag.setStatus("current")


class _SleISISProcInfoControlIgnLspErr_Type(Integer32):
    """Custom type sleISISProcInfoControlIgnLspErr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcInfoControlIgnLspErr_Type.__name__ = "Integer32"
_SleISISProcInfoControlIgnLspErr_Object = MibScalar
sleISISProcInfoControlIgnLspErr = _SleISISProcInfoControlIgnLspErr_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 11),
    _SleISISProcInfoControlIgnLspErr_Type()
)
sleISISProcInfoControlIgnLspErr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlIgnLspErr.setStatus("current")


class _SleISISProcInfoControlRouteHighPriorityTag_Type(Gauge32):
    """Custom type sleISISProcInfoControlRouteHighPriorityTag based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleISISProcInfoControlRouteHighPriorityTag_Type.__name__ = "Gauge32"
_SleISISProcInfoControlRouteHighPriorityTag_Object = MibScalar
sleISISProcInfoControlRouteHighPriorityTag = _SleISISProcInfoControlRouteHighPriorityTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 12),
    _SleISISProcInfoControlRouteHighPriorityTag_Type()
)
sleISISProcInfoControlRouteHighPriorityTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlRouteHighPriorityTag.setStatus("current")


class _SleISISProcInfoControlIspfLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlIspfLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcInfoControlIspfLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlIspfLevel_Object = MibScalar
sleISISProcInfoControlIspfLevel = _SleISISProcInfoControlIspfLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 13),
    _SleISISProcInfoControlIspfLevel_Type()
)
sleISISProcInfoControlIspfLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlIspfLevel.setStatus("current")


class _SleISISProcInfoControlIsTypeLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlIsTypeLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcInfoControlIsTypeLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlIsTypeLevel_Object = MibScalar
sleISISProcInfoControlIsTypeLevel = _SleISISProcInfoControlIsTypeLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 14),
    _SleISISProcInfoControlIsTypeLevel_Type()
)
sleISISProcInfoControlIsTypeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlIsTypeLevel.setStatus("current")


class _SleISISProcInfoControlLspGenInterval_Type(Integer32):
    """Custom type sleISISProcInfoControlLspGenInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SleISISProcInfoControlLspGenInterval_Type.__name__ = "Integer32"
_SleISISProcInfoControlLspGenInterval_Object = MibScalar
sleISISProcInfoControlLspGenInterval = _SleISISProcInfoControlLspGenInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 15),
    _SleISISProcInfoControlLspGenInterval_Type()
)
sleISISProcInfoControlLspGenInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlLspGenInterval.setStatus("current")


class _SleISISProcInfoControlLspGenIntervalLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlLspGenIntervalLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcInfoControlLspGenIntervalLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlLspGenIntervalLevel_Object = MibScalar
sleISISProcInfoControlLspGenIntervalLevel = _SleISISProcInfoControlLspGenIntervalLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 16),
    _SleISISProcInfoControlLspGenIntervalLevel_Type()
)
sleISISProcInfoControlLspGenIntervalLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlLspGenIntervalLevel.setStatus("current")


class _SleISISProcInfoControlLspMtu_Type(Integer32):
    """Custom type sleISISProcInfoControlLspMtu based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 1492),
    )


_SleISISProcInfoControlLspMtu_Type.__name__ = "Integer32"
_SleISISProcInfoControlLspMtu_Object = MibScalar
sleISISProcInfoControlLspMtu = _SleISISProcInfoControlLspMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 17),
    _SleISISProcInfoControlLspMtu_Type()
)
sleISISProcInfoControlLspMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlLspMtu.setStatus("current")


class _SleISISProcInfoControlLspMtuLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlLspMtuLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcInfoControlLspMtuLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlLspMtuLevel_Object = MibScalar
sleISISProcInfoControlLspMtuLevel = _SleISISProcInfoControlLspMtuLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 18),
    _SleISISProcInfoControlLspMtuLevel_Type()
)
sleISISProcInfoControlLspMtuLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlLspMtuLevel.setStatus("current")


class _SleISISProcInfoControlLspRefreshInterval_Type(Integer32):
    """Custom type sleISISProcInfoControlLspRefreshInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISProcInfoControlLspRefreshInterval_Type.__name__ = "Integer32"
_SleISISProcInfoControlLspRefreshInterval_Object = MibScalar
sleISISProcInfoControlLspRefreshInterval = _SleISISProcInfoControlLspRefreshInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 19),
    _SleISISProcInfoControlLspRefreshInterval_Type()
)
sleISISProcInfoControlLspRefreshInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlLspRefreshInterval.setStatus("current")


class _SleISISProcInfoControlMaxAreaAddressNum_Type(Integer32):
    """Custom type sleISISProcInfoControlMaxAreaAddressNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 254),
    )


_SleISISProcInfoControlMaxAreaAddressNum_Type.__name__ = "Integer32"
_SleISISProcInfoControlMaxAreaAddressNum_Object = MibScalar
sleISISProcInfoControlMaxAreaAddressNum = _SleISISProcInfoControlMaxAreaAddressNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 20),
    _SleISISProcInfoControlMaxAreaAddressNum_Type()
)
sleISISProcInfoControlMaxAreaAddressNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlMaxAreaAddressNum.setStatus("current")


class _SleISISProcInfoControlMaxLspLifetime_Type(Integer32):
    """Custom type sleISISProcInfoControlMaxLspLifetime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(350, 65535),
    )


_SleISISProcInfoControlMaxLspLifetime_Type.__name__ = "Integer32"
_SleISISProcInfoControlMaxLspLifetime_Object = MibScalar
sleISISProcInfoControlMaxLspLifetime = _SleISISProcInfoControlMaxLspLifetime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 21),
    _SleISISProcInfoControlMaxLspLifetime_Type()
)
sleISISProcInfoControlMaxLspLifetime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlMaxLspLifetime.setStatus("current")


class _SleISISProcInfoControlMetricStyle_Type(Integer32):
    """Custom type sleISISProcInfoControlMetricStyle based on Integer32"""
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
        *(("none", 0),
          ("wide", 1),
          ("wideTransition", 2),
          ("transition", 3),
          ("narrowTransition", 4))
    )


_SleISISProcInfoControlMetricStyle_Type.__name__ = "Integer32"
_SleISISProcInfoControlMetricStyle_Object = MibScalar
sleISISProcInfoControlMetricStyle = _SleISISProcInfoControlMetricStyle_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 22),
    _SleISISProcInfoControlMetricStyle_Type()
)
sleISISProcInfoControlMetricStyle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlMetricStyle.setStatus("current")


class _SleISISProcInfoControlMetricStyleLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlMetricStyleLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcInfoControlMetricStyleLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlMetricStyleLevel_Object = MibScalar
sleISISProcInfoControlMetricStyleLevel = _SleISISProcInfoControlMetricStyleLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 23),
    _SleISISProcInfoControlMetricStyleLevel_Type()
)
sleISISProcInfoControlMetricStyleLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlMetricStyleLevel.setStatus("current")


class _SleISISProcInfoControlMplsTrafficEngLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlMplsTrafficEngLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcInfoControlMplsTrafficEngLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlMplsTrafficEngLevel_Object = MibScalar
sleISISProcInfoControlMplsTrafficEngLevel = _SleISISProcInfoControlMplsTrafficEngLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 24),
    _SleISISProcInfoControlMplsTrafficEngLevel_Type()
)
sleISISProcInfoControlMplsTrafficEngLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlMplsTrafficEngLevel.setStatus("current")
_SleISISProcInfoControlMplsTrafficEngRouterID_Type = IpAddress
_SleISISProcInfoControlMplsTrafficEngRouterID_Object = MibScalar
sleISISProcInfoControlMplsTrafficEngRouterID = _SleISISProcInfoControlMplsTrafficEngRouterID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 25),
    _SleISISProcInfoControlMplsTrafficEngRouterID_Type()
)
sleISISProcInfoControlMplsTrafficEngRouterID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlMplsTrafficEngRouterID.setStatus("current")


class _SleISISProcInfoControlPrcIntervalExpMinDelay_Type(Integer32):
    """Custom type sleISISProcInfoControlPrcIntervalExpMinDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleISISProcInfoControlPrcIntervalExpMinDelay_Type.__name__ = "Integer32"
_SleISISProcInfoControlPrcIntervalExpMinDelay_Object = MibScalar
sleISISProcInfoControlPrcIntervalExpMinDelay = _SleISISProcInfoControlPrcIntervalExpMinDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 26),
    _SleISISProcInfoControlPrcIntervalExpMinDelay_Type()
)
sleISISProcInfoControlPrcIntervalExpMinDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlPrcIntervalExpMinDelay.setStatus("current")


class _SleISISProcInfoControlPrcIntervalExpMaxDelay_Type(Integer32):
    """Custom type sleISISProcInfoControlPrcIntervalExpMaxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleISISProcInfoControlPrcIntervalExpMaxDelay_Type.__name__ = "Integer32"
_SleISISProcInfoControlPrcIntervalExpMaxDelay_Object = MibScalar
sleISISProcInfoControlPrcIntervalExpMaxDelay = _SleISISProcInfoControlPrcIntervalExpMaxDelay_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 27),
    _SleISISProcInfoControlPrcIntervalExpMaxDelay_Type()
)
sleISISProcInfoControlPrcIntervalExpMaxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlPrcIntervalExpMaxDelay.setStatus("current")


class _SleISISProcInfoControlProtocolTopolgy_Type(Integer32):
    """Custom type sleISISProcInfoControlProtocolTopolgy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcInfoControlProtocolTopolgy_Type.__name__ = "Integer32"
_SleISISProcInfoControlProtocolTopolgy_Object = MibScalar
sleISISProcInfoControlProtocolTopolgy = _SleISISProcInfoControlProtocolTopolgy_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 28),
    _SleISISProcInfoControlProtocolTopolgy_Type()
)
sleISISProcInfoControlProtocolTopolgy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlProtocolTopolgy.setStatus("current")


class _SleISISProcInfoControlRestartTimerVal_Type(Integer32):
    """Custom type sleISISProcInfoControlRestartTimerVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 65535),
    )


_SleISISProcInfoControlRestartTimerVal_Type.__name__ = "Integer32"
_SleISISProcInfoControlRestartTimerVal_Object = MibScalar
sleISISProcInfoControlRestartTimerVal = _SleISISProcInfoControlRestartTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 29),
    _SleISISProcInfoControlRestartTimerVal_Type()
)
sleISISProcInfoControlRestartTimerVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlRestartTimerVal.setStatus("current")


class _SleISISProcInfoControlRestartTimerLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlRestartTimerLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcInfoControlRestartTimerLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlRestartTimerLevel_Object = MibScalar
sleISISProcInfoControlRestartTimerLevel = _SleISISProcInfoControlRestartTimerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 30),
    _SleISISProcInfoControlRestartTimerLevel_Type()
)
sleISISProcInfoControlRestartTimerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlRestartTimerLevel.setStatus("current")


class _SleISISProcInfoControlSpfIntervalExpMin_Type(Integer32):
    """Custom type sleISISProcInfoControlSpfIntervalExpMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleISISProcInfoControlSpfIntervalExpMin_Type.__name__ = "Integer32"
_SleISISProcInfoControlSpfIntervalExpMin_Object = MibScalar
sleISISProcInfoControlSpfIntervalExpMin = _SleISISProcInfoControlSpfIntervalExpMin_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 31),
    _SleISISProcInfoControlSpfIntervalExpMin_Type()
)
sleISISProcInfoControlSpfIntervalExpMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlSpfIntervalExpMin.setStatus("current")


class _SleISISProcInfoControlSpfIntervalExpMax_Type(Integer32):
    """Custom type sleISISProcInfoControlSpfIntervalExpMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SleISISProcInfoControlSpfIntervalExpMax_Type.__name__ = "Integer32"
_SleISISProcInfoControlSpfIntervalExpMax_Object = MibScalar
sleISISProcInfoControlSpfIntervalExpMax = _SleISISProcInfoControlSpfIntervalExpMax_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 32),
    _SleISISProcInfoControlSpfIntervalExpMax_Type()
)
sleISISProcInfoControlSpfIntervalExpMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlSpfIntervalExpMax.setStatus("current")


class _SleISISProcInfoControlSpfIntervalExpLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlSpfIntervalExpLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcInfoControlSpfIntervalExpLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlSpfIntervalExpLevel_Object = MibScalar
sleISISProcInfoControlSpfIntervalExpLevel = _SleISISProcInfoControlSpfIntervalExpLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 33),
    _SleISISProcInfoControlSpfIntervalExpLevel_Type()
)
sleISISProcInfoControlSpfIntervalExpLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlSpfIntervalExpLevel.setStatus("current")


class _SleISISProcInfoControlAuthMode_Type(Integer32):
    """Custom type sleISISProcInfoControlAuthMode based on Integer32"""
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
        *(("none", 0),
          ("md5", 1),
          ("text", 2),
          ("md5Text", 3))
    )


_SleISISProcInfoControlAuthMode_Type.__name__ = "Integer32"
_SleISISProcInfoControlAuthMode_Object = MibScalar
sleISISProcInfoControlAuthMode = _SleISISProcInfoControlAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 34),
    _SleISISProcInfoControlAuthMode_Type()
)
sleISISProcInfoControlAuthMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlAuthMode.setStatus("current")


class _SleISISProcInfoControlAuthModeLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlAuthModeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcInfoControlAuthModeLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlAuthModeLevel_Object = MibScalar
sleISISProcInfoControlAuthModeLevel = _SleISISProcInfoControlAuthModeLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 35),
    _SleISISProcInfoControlAuthModeLevel_Type()
)
sleISISProcInfoControlAuthModeLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlAuthModeLevel.setStatus("current")


class _SleISISProcInfoControlAuthSendOnly_Type(Integer32):
    """Custom type sleISISProcInfoControlAuthSendOnly based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcInfoControlAuthSendOnly_Type.__name__ = "Integer32"
_SleISISProcInfoControlAuthSendOnly_Object = MibScalar
sleISISProcInfoControlAuthSendOnly = _SleISISProcInfoControlAuthSendOnly_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 36),
    _SleISISProcInfoControlAuthSendOnly_Type()
)
sleISISProcInfoControlAuthSendOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlAuthSendOnly.setStatus("current")


class _SleISISProcInfoControlAuthSendOnlyLevel_Type(Integer32):
    """Custom type sleISISProcInfoControlAuthSendOnlyLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISProcInfoControlAuthSendOnlyLevel_Type.__name__ = "Integer32"
_SleISISProcInfoControlAuthSendOnlyLevel_Object = MibScalar
sleISISProcInfoControlAuthSendOnlyLevel = _SleISISProcInfoControlAuthSendOnlyLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 37),
    _SleISISProcInfoControlAuthSendOnlyLevel_Type()
)
sleISISProcInfoControlAuthSendOnlyLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlAuthSendOnlyLevel.setStatus("current")
_SleISISProcInfoControlDomPassVal_Type = OctetString
_SleISISProcInfoControlDomPassVal_Object = MibScalar
sleISISProcInfoControlDomPassVal = _SleISISProcInfoControlDomPassVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 38),
    _SleISISProcInfoControlDomPassVal_Type()
)
sleISISProcInfoControlDomPassVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlDomPassVal.setStatus("current")


class _SleISISProcInfoControlDomPassAuthSnp_Type(Integer32):
    """Custom type sleISISProcInfoControlDomPassAuthSnp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("validate", 1),
          ("sendOnly", 2))
    )


_SleISISProcInfoControlDomPassAuthSnp_Type.__name__ = "Integer32"
_SleISISProcInfoControlDomPassAuthSnp_Object = MibScalar
sleISISProcInfoControlDomPassAuthSnp = _SleISISProcInfoControlDomPassAuthSnp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 39),
    _SleISISProcInfoControlDomPassAuthSnp_Type()
)
sleISISProcInfoControlDomPassAuthSnp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlDomPassAuthSnp.setStatus("current")
_SleISISProcInfoControlAreaPassVal_Type = OctetString
_SleISISProcInfoControlAreaPassVal_Object = MibScalar
sleISISProcInfoControlAreaPassVal = _SleISISProcInfoControlAreaPassVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 40),
    _SleISISProcInfoControlAreaPassVal_Type()
)
sleISISProcInfoControlAreaPassVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlAreaPassVal.setStatus("current")


class _SleISISProcInfoControlAreaPassAuthSnp_Type(Integer32):
    """Custom type sleISISProcInfoControlAreaPassAuthSnp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("validate", 1),
          ("sendOnly", 2))
    )


_SleISISProcInfoControlAreaPassAuthSnp_Type.__name__ = "Integer32"
_SleISISProcInfoControlAreaPassAuthSnp_Object = MibScalar
sleISISProcInfoControlAreaPassAuthSnp = _SleISISProcInfoControlAreaPassAuthSnp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 41),
    _SleISISProcInfoControlAreaPassAuthSnp_Type()
)
sleISISProcInfoControlAreaPassAuthSnp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlAreaPassAuthSnp.setStatus("current")


class _SleISISProcInfoControlSetOverloadBit_Type(Integer32):
    """Custom type sleISISProcInfoControlSetOverloadBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISProcInfoControlSetOverloadBit_Type.__name__ = "Integer32"
_SleISISProcInfoControlSetOverloadBit_Object = MibScalar
sleISISProcInfoControlSetOverloadBit = _SleISISProcInfoControlSetOverloadBit_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 42),
    _SleISISProcInfoControlSetOverloadBit_Type()
)
sleISISProcInfoControlSetOverloadBit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlSetOverloadBit.setStatus("current")


class _SleISISProcInfoControlSetOverloadBitOnStartup_Type(Integer32):
    """Custom type sleISISProcInfoControlSetOverloadBitOnStartup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("overload", 1),
          ("waitForBgp", 2))
    )


_SleISISProcInfoControlSetOverloadBitOnStartup_Type.__name__ = "Integer32"
_SleISISProcInfoControlSetOverloadBitOnStartup_Object = MibScalar
sleISISProcInfoControlSetOverloadBitOnStartup = _SleISISProcInfoControlSetOverloadBitOnStartup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 43),
    _SleISISProcInfoControlSetOverloadBitOnStartup_Type()
)
sleISISProcInfoControlSetOverloadBitOnStartup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlSetOverloadBitOnStartup.setStatus("current")


class _SleISISProcInfoControlSetOverloadBitOnStartupInterval_Type(Integer32):
    """Custom type sleISISProcInfoControlSetOverloadBitOnStartupInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 86400),
    )


_SleISISProcInfoControlSetOverloadBitOnStartupInterval_Type.__name__ = "Integer32"
_SleISISProcInfoControlSetOverloadBitOnStartupInterval_Object = MibScalar
sleISISProcInfoControlSetOverloadBitOnStartupInterval = _SleISISProcInfoControlSetOverloadBitOnStartupInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 44),
    _SleISISProcInfoControlSetOverloadBitOnStartupInterval_Type()
)
sleISISProcInfoControlSetOverloadBitOnStartupInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlSetOverloadBitOnStartupInterval.setStatus("current")


class _SleISISProcInfoControlSetOverloadBitSuppress_Type(Integer32):
    """Custom type sleISISProcInfoControlSetOverloadBitSuppress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("external", 1),
          ("interlevel", 2))
    )


_SleISISProcInfoControlSetOverloadBitSuppress_Type.__name__ = "Integer32"
_SleISISProcInfoControlSetOverloadBitSuppress_Object = MibScalar
sleISISProcInfoControlSetOverloadBitSuppress = _SleISISProcInfoControlSetOverloadBitSuppress_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 45),
    _SleISISProcInfoControlSetOverloadBitSuppress_Type()
)
sleISISProcInfoControlSetOverloadBitSuppress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcInfoControlSetOverloadBitSuppress.setStatus("current")


class _SleISISProcControlWaitTimerVal_Type(Integer32):
    """Custom type sleISISProcControlWaitTimerVal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISProcControlWaitTimerVal_Type.__name__ = "Integer32"
_SleISISProcControlWaitTimerVal_Object = MibScalar
sleISISProcControlWaitTimerVal = _SleISISProcControlWaitTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 46),
    _SleISISProcControlWaitTimerVal_Type()
)
sleISISProcControlWaitTimerVal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcControlWaitTimerVal.setStatus("current")


class _SleISISProcControlWaitTimerLevel_Type(Integer32):
    """Custom type sleISISProcControlWaitTimerLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2Only", 3))
    )


_SleISISProcControlWaitTimerLevel_Type.__name__ = "Integer32"
_SleISISProcControlWaitTimerLevel_Object = MibScalar
sleISISProcControlWaitTimerLevel = _SleISISProcControlWaitTimerLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 47),
    _SleISISProcControlWaitTimerLevel_Type()
)
sleISISProcControlWaitTimerLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcControlWaitTimerLevel.setStatus("current")
_SleISISProcControlAuthenkeyChain_Type = OctetString
_SleISISProcControlAuthenkeyChain_Object = MibScalar
sleISISProcControlAuthenkeyChain = _SleISISProcControlAuthenkeyChain_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 48),
    _SleISISProcControlAuthenkeyChain_Type()
)
sleISISProcControlAuthenkeyChain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcControlAuthenkeyChain.setStatus("current")


class _SleISISProcControlAuthenkeyChainLevel_Type(Integer32):
    """Custom type sleISISProcControlAuthenkeyChainLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level2", 2),
          ("level1And2", 3))
    )


_SleISISProcControlAuthenkeyChainLevel_Type.__name__ = "Integer32"
_SleISISProcControlAuthenkeyChainLevel_Object = MibScalar
sleISISProcControlAuthenkeyChainLevel = _SleISISProcControlAuthenkeyChainLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 2, 49),
    _SleISISProcControlAuthenkeyChainLevel_Type()
)
sleISISProcControlAuthenkeyChainLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcControlAuthenkeyChainLevel.setStatus("current")
_SleISISProcInfoNotification_ObjectIdentity = ObjectIdentity
sleISISProcInfoNotification = _SleISISProcInfoNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 1, 3)
)
_SleISISProcNet_ObjectIdentity = ObjectIdentity
sleISISProcNet = _SleISISProcNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2)
)
_SleISISProcNetTable_Object = MibTable
sleISISProcNetTable = _SleISISProcNetTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 1)
)
if mibBuilder.loadTexts:
    sleISISProcNetTable.setStatus("current")
_SleISISProcNetEntry_Object = MibTableRow
sleISISProcNetEntry = _SleISISProcNetEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 1, 1)
)
sleISISProcNetEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISProcNetInstanceID"),
    (0, "SLE-ISIS-MIB", "sleISISProcNetTitle"),
)
if mibBuilder.loadTexts:
    sleISISProcNetEntry.setStatus("current")


class _SleISISProcNetInstanceID_Type(Integer32):
    """Custom type sleISISProcNetInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleISISProcNetInstanceID_Type.__name__ = "Integer32"
_SleISISProcNetInstanceID_Object = MibTableColumn
sleISISProcNetInstanceID = _SleISISProcNetInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 1, 1, 1),
    _SleISISProcNetInstanceID_Type()
)
sleISISProcNetInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcNetInstanceID.setStatus("current")
_SleISISProcNetTitle_Type = OctetString
_SleISISProcNetTitle_Object = MibTableColumn
sleISISProcNetTitle = _SleISISProcNetTitle_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 1, 1, 2),
    _SleISISProcNetTitle_Type()
)
sleISISProcNetTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcNetTitle.setStatus("current")
_SleISISProcNetControl_ObjectIdentity = ObjectIdentity
sleISISProcNetControl = _SleISISProcNetControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 2)
)


class _SleISISProcNetControlRequest_Type(Integer32):
    """Custom type sleISISProcNetControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createISISProcNet", 1),
          ("deleteISISProcNet", 2))
    )


_SleISISProcNetControlRequest_Type.__name__ = "Integer32"
_SleISISProcNetControlRequest_Object = MibScalar
sleISISProcNetControlRequest = _SleISISProcNetControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 2, 1),
    _SleISISProcNetControlRequest_Type()
)
sleISISProcNetControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcNetControlRequest.setStatus("current")
_SleISISProcNetControlStatus_Type = SleControlStatusType
_SleISISProcNetControlStatus_Object = MibScalar
sleISISProcNetControlStatus = _SleISISProcNetControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 2, 2),
    _SleISISProcNetControlStatus_Type()
)
sleISISProcNetControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcNetControlStatus.setStatus("current")
_SleISISProcNetControlTimer_Type = Gauge32
_SleISISProcNetControlTimer_Object = MibScalar
sleISISProcNetControlTimer = _SleISISProcNetControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 2, 3),
    _SleISISProcNetControlTimer_Type()
)
sleISISProcNetControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcNetControlTimer.setStatus("current")
_SleISISProcNetControlTimeStamp_Type = TimeTicks
_SleISISProcNetControlTimeStamp_Object = MibScalar
sleISISProcNetControlTimeStamp = _SleISISProcNetControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 2, 4),
    _SleISISProcNetControlTimeStamp_Type()
)
sleISISProcNetControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcNetControlTimeStamp.setStatus("current")
_SleISISProcNetControlReqResult_Type = SleControlRequestResultType
_SleISISProcNetControlReqResult_Object = MibScalar
sleISISProcNetControlReqResult = _SleISISProcNetControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 2, 5),
    _SleISISProcNetControlReqResult_Type()
)
sleISISProcNetControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcNetControlReqResult.setStatus("current")


class _SleISISProcNetControlInstanceID_Type(Integer32):
    """Custom type sleISISProcNetControlInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleISISProcNetControlInstanceID_Type.__name__ = "Integer32"
_SleISISProcNetControlInstanceID_Object = MibScalar
sleISISProcNetControlInstanceID = _SleISISProcNetControlInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 2, 6),
    _SleISISProcNetControlInstanceID_Type()
)
sleISISProcNetControlInstanceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcNetControlInstanceID.setStatus("current")


class _SleISISProcNetControlTitle_Type(OctetString):
    """Custom type sleISISProcNetControlTitle based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_SleISISProcNetControlTitle_Type.__name__ = "OctetString"
_SleISISProcNetControlTitle_Object = MibScalar
sleISISProcNetControlTitle = _SleISISProcNetControlTitle_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 2, 7),
    _SleISISProcNetControlTitle_Type()
)
sleISISProcNetControlTitle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcNetControlTitle.setStatus("current")
_SleISISProcNetNotification_ObjectIdentity = ObjectIdentity
sleISISProcNetNotification = _SleISISProcNetNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 2, 3)
)
_SleISISProcDistanceV4_ObjectIdentity = ObjectIdentity
sleISISProcDistanceV4 = _SleISISProcDistanceV4_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3)
)
_SleISISProcDistanceV4Table_Object = MibTable
sleISISProcDistanceV4Table = _SleISISProcDistanceV4Table_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 1)
)
if mibBuilder.loadTexts:
    sleISISProcDistanceV4Table.setStatus("current")
_SleISISProcDistanceV4Entry_Object = MibTableRow
sleISISProcDistanceV4Entry = _SleISISProcDistanceV4Entry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 1, 1)
)
sleISISProcDistanceV4Entry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISProcDistanceV4InstanceID"),
    (0, "SLE-ISIS-MIB", "sleISISProcDistanceV4SytemID"),
)
if mibBuilder.loadTexts:
    sleISISProcDistanceV4Entry.setStatus("current")


class _SleISISProcDistanceV4InstanceID_Type(Integer32):
    """Custom type sleISISProcDistanceV4InstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISProcDistanceV4InstanceID_Type.__name__ = "Integer32"
_SleISISProcDistanceV4InstanceID_Object = MibTableColumn
sleISISProcDistanceV4InstanceID = _SleISISProcDistanceV4InstanceID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 1, 1, 1),
    _SleISISProcDistanceV4InstanceID_Type()
)
sleISISProcDistanceV4InstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4InstanceID.setStatus("current")


class _SleISISProcDistanceV4Dist_Type(Integer32):
    """Custom type sleISISProcDistanceV4Dist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_SleISISProcDistanceV4Dist_Type.__name__ = "Integer32"
_SleISISProcDistanceV4Dist_Object = MibTableColumn
sleISISProcDistanceV4Dist = _SleISISProcDistanceV4Dist_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 1, 1, 2),
    _SleISISProcDistanceV4Dist_Type()
)
sleISISProcDistanceV4Dist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4Dist.setStatus("current")


class _SleISISProcDistanceV4SytemID_Type(OctetString):
    """Custom type sleISISProcDistanceV4SytemID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 112),
    )


_SleISISProcDistanceV4SytemID_Type.__name__ = "OctetString"
_SleISISProcDistanceV4SytemID_Object = MibTableColumn
sleISISProcDistanceV4SytemID = _SleISISProcDistanceV4SytemID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 1, 1, 3),
    _SleISISProcDistanceV4SytemID_Type()
)
sleISISProcDistanceV4SytemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4SytemID.setStatus("current")
_SleISISProcDistanceV4AccessList_Type = OctetString
_SleISISProcDistanceV4AccessList_Object = MibTableColumn
sleISISProcDistanceV4AccessList = _SleISISProcDistanceV4AccessList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 1, 1, 4),
    _SleISISProcDistanceV4AccessList_Type()
)
sleISISProcDistanceV4AccessList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4AccessList.setStatus("current")
_SleISISProcDistanceV4Control_ObjectIdentity = ObjectIdentity
sleISISProcDistanceV4Control = _SleISISProcDistanceV4Control_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2)
)


class _SleISISProcDistanceV4ControlRequest_Type(Integer32):
    """Custom type sleISISProcDistanceV4ControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("createRIPNetworkIfname", 1),
          ("deleteRIPNetworkIfname", 2))
    )


_SleISISProcDistanceV4ControlRequest_Type.__name__ = "Integer32"
_SleISISProcDistanceV4ControlRequest_Object = MibScalar
sleISISProcDistanceV4ControlRequest = _SleISISProcDistanceV4ControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2, 1),
    _SleISISProcDistanceV4ControlRequest_Type()
)
sleISISProcDistanceV4ControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4ControlRequest.setStatus("current")
_SleISISProcDistanceV4ControlStatus_Type = SleControlStatusType
_SleISISProcDistanceV4ControlStatus_Object = MibScalar
sleISISProcDistanceV4ControlStatus = _SleISISProcDistanceV4ControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2, 2),
    _SleISISProcDistanceV4ControlStatus_Type()
)
sleISISProcDistanceV4ControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4ControlStatus.setStatus("current")
_SleISISProcDistanceV4ControlTimer_Type = Gauge32
_SleISISProcDistanceV4ControlTimer_Object = MibScalar
sleISISProcDistanceV4ControlTimer = _SleISISProcDistanceV4ControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2, 3),
    _SleISISProcDistanceV4ControlTimer_Type()
)
sleISISProcDistanceV4ControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4ControlTimer.setStatus("current")
_SleISISProcDistanceV4TimeStamp_Type = TimeTicks
_SleISISProcDistanceV4TimeStamp_Object = MibScalar
sleISISProcDistanceV4TimeStamp = _SleISISProcDistanceV4TimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2, 4),
    _SleISISProcDistanceV4TimeStamp_Type()
)
sleISISProcDistanceV4TimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4TimeStamp.setStatus("current")
_SleISISProcDistanceV4ntrolReqResult_Type = SleControlRequestResultType
_SleISISProcDistanceV4ntrolReqResult_Object = MibScalar
sleISISProcDistanceV4ntrolReqResult = _SleISISProcDistanceV4ntrolReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2, 5),
    _SleISISProcDistanceV4ntrolReqResult_Type()
)
sleISISProcDistanceV4ntrolReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4ntrolReqResult.setStatus("current")


class _SleISISProcDistanceV4ControlInstanceID_Type(Integer32):
    """Custom type sleISISProcDistanceV4ControlInstanceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleISISProcDistanceV4ControlInstanceID_Type.__name__ = "Integer32"
_SleISISProcDistanceV4ControlInstanceID_Object = MibScalar
sleISISProcDistanceV4ControlInstanceID = _SleISISProcDistanceV4ControlInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2, 6),
    _SleISISProcDistanceV4ControlInstanceID_Type()
)
sleISISProcDistanceV4ControlInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4ControlInstanceID.setStatus("current")


class _SleISISProcDistanceV4ControlDist_Type(Integer32):
    """Custom type sleISISProcDistanceV4ControlDist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SleISISProcDistanceV4ControlDist_Type.__name__ = "Integer32"
_SleISISProcDistanceV4ControlDist_Object = MibScalar
sleISISProcDistanceV4ControlDist = _SleISISProcDistanceV4ControlDist_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2, 7),
    _SleISISProcDistanceV4ControlDist_Type()
)
sleISISProcDistanceV4ControlDist.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4ControlDist.setStatus("current")
_SleISISProcDistanceV4ControlSytemID_Type = OctetString
_SleISISProcDistanceV4ControlSytemID_Object = MibScalar
sleISISProcDistanceV4ControlSytemID = _SleISISProcDistanceV4ControlSytemID_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2, 8),
    _SleISISProcDistanceV4ControlSytemID_Type()
)
sleISISProcDistanceV4ControlSytemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4ControlSytemID.setStatus("current")
_SleISISProcDistanceV4ControlAccessList_Type = OctetString
_SleISISProcDistanceV4ControlAccessList_Object = MibScalar
sleISISProcDistanceV4ControlAccessList = _SleISISProcDistanceV4ControlAccessList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 2, 9),
    _SleISISProcDistanceV4ControlAccessList_Type()
)
sleISISProcDistanceV4ControlAccessList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISProcDistanceV4ControlAccessList.setStatus("current")
_SleISISProcDistanceV4Notification_ObjectIdentity = ObjectIdentity
sleISISProcDistanceV4Notification = _SleISISProcDistanceV4Notification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 2, 3, 3)
)
_SleISISIf_ObjectIdentity = ObjectIdentity
sleISISIf = _SleISISIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3)
)
_SlsISISIfTable_Object = MibTable
slsISISIfTable = _SlsISISIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1)
)
if mibBuilder.loadTexts:
    slsISISIfTable.setStatus("current")
_SlsISISIfEntry_Object = MibTableRow
slsISISIfEntry = _SlsISISIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1)
)
slsISISIfEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISIfIndex"),
)
if mibBuilder.loadTexts:
    slsISISIfEntry.setStatus("current")


class _SleISISIfIndex_Type(Integer32):
    """Custom type sleISISIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfIndex_Type.__name__ = "Integer32"
_SleISISIfIndex_Object = MibTableColumn
sleISISIfIndex = _SleISISIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 1),
    _SleISISIfIndex_Type()
)
sleISISIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfIndex.setStatus("current")


class _SleISISIfMplsLdpIgpSync_Type(Integer32):
    """Custom type sleISISIfMplsLdpIgpSync based on Integer32"""
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
        *(("diaable", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2", 3))
    )


_SleISISIfMplsLdpIgpSync_Type.__name__ = "Integer32"
_SleISISIfMplsLdpIgpSync_Object = MibTableColumn
sleISISIfMplsLdpIgpSync = _SleISISIfMplsLdpIgpSync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 2),
    _SleISISIfMplsLdpIgpSync_Type()
)
sleISISIfMplsLdpIgpSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfMplsLdpIgpSync.setStatus("current")


class _SleISISIfIpRouter_Type(Integer32):
    """Custom type sleISISIfIpRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfIpRouter_Type.__name__ = "Integer32"
_SleISISIfIpRouter_Object = MibTableColumn
sleISISIfIpRouter = _SleISISIfIpRouter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 3),
    _SleISISIfIpRouter_Type()
)
sleISISIfIpRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfIpRouter.setStatus("current")


class _SleISISIfAuthSendLevel1_Type(Integer32):
    """Custom type sleISISIfAuthSendLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfAuthSendLevel1_Type.__name__ = "Integer32"
_SleISISIfAuthSendLevel1_Object = MibTableColumn
sleISISIfAuthSendLevel1 = _SleISISIfAuthSendLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 4),
    _SleISISIfAuthSendLevel1_Type()
)
sleISISIfAuthSendLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfAuthSendLevel1.setStatus("current")


class _SleISISIfAuthSendLevel2_Type(Integer32):
    """Custom type sleISISIfAuthSendLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfAuthSendLevel2_Type.__name__ = "Integer32"
_SleISISIfAuthSendLevel2_Object = MibTableColumn
sleISISIfAuthSendLevel2 = _SleISISIfAuthSendLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 5),
    _SleISISIfAuthSendLevel2_Type()
)
sleISISIfAuthSendLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfAuthSendLevel2.setStatus("current")


class _SleISISIfAuthModeMd5Levle1_Type(Integer32):
    """Custom type sleISISIfAuthModeMd5Levle1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfAuthModeMd5Levle1_Type.__name__ = "Integer32"
_SleISISIfAuthModeMd5Levle1_Object = MibTableColumn
sleISISIfAuthModeMd5Levle1 = _SleISISIfAuthModeMd5Levle1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 6),
    _SleISISIfAuthModeMd5Levle1_Type()
)
sleISISIfAuthModeMd5Levle1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfAuthModeMd5Levle1.setStatus("current")


class _SleISISIfAuthModeMd5Levle2_Type(Integer32):
    """Custom type sleISISIfAuthModeMd5Levle2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfAuthModeMd5Levle2_Type.__name__ = "Integer32"
_SleISISIfAuthModeMd5Levle2_Object = MibTableColumn
sleISISIfAuthModeMd5Levle2 = _SleISISIfAuthModeMd5Levle2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 7),
    _SleISISIfAuthModeMd5Levle2_Type()
)
sleISISIfAuthModeMd5Levle2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfAuthModeMd5Levle2.setStatus("current")


class _SleISISIfAuthModeTextLevle1_Type(Integer32):
    """Custom type sleISISIfAuthModeTextLevle1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfAuthModeTextLevle1_Type.__name__ = "Integer32"
_SleISISIfAuthModeTextLevle1_Object = MibTableColumn
sleISISIfAuthModeTextLevle1 = _SleISISIfAuthModeTextLevle1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 8),
    _SleISISIfAuthModeTextLevle1_Type()
)
sleISISIfAuthModeTextLevle1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfAuthModeTextLevle1.setStatus("current")


class _SleISISIfAuthModeTextLevle2_Type(Integer32):
    """Custom type sleISISIfAuthModeTextLevle2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfAuthModeTextLevle2_Type.__name__ = "Integer32"
_SleISISIfAuthModeTextLevle2_Object = MibTableColumn
sleISISIfAuthModeTextLevle2 = _SleISISIfAuthModeTextLevle2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 9),
    _SleISISIfAuthModeTextLevle2_Type()
)
sleISISIfAuthModeTextLevle2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfAuthModeTextLevle2.setStatus("current")
_SleISISIfAuthKeyChainLevle1_Type = OctetString
_SleISISIfAuthKeyChainLevle1_Object = MibTableColumn
sleISISIfAuthKeyChainLevle1 = _SleISISIfAuthKeyChainLevle1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 10),
    _SleISISIfAuthKeyChainLevle1_Type()
)
sleISISIfAuthKeyChainLevle1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfAuthKeyChainLevle1.setStatus("current")
_SleISISIfAuthKeyChainLevle2_Type = OctetString
_SleISISIfAuthKeyChainLevle2_Object = MibTableColumn
sleISISIfAuthKeyChainLevle2 = _SleISISIfAuthKeyChainLevle2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 11),
    _SleISISIfAuthKeyChainLevle2_Type()
)
sleISISIfAuthKeyChainLevle2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfAuthKeyChainLevle2.setStatus("current")


class _SleISISIfBfd_Type(Integer32):
    """Custom type sleISISIfBfd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfBfd_Type.__name__ = "Integer32"
_SleISISIfBfd_Object = MibTableColumn
sleISISIfBfd = _SleISISIfBfd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 12),
    _SleISISIfBfd_Type()
)
sleISISIfBfd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfBfd.setStatus("current")


class _SleISISIfBfdDisable_Type(Integer32):
    """Custom type sleISISIfBfdDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfBfdDisable_Type.__name__ = "Integer32"
_SleISISIfBfdDisable_Object = MibTableColumn
sleISISIfBfdDisable = _SleISISIfBfdDisable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 13),
    _SleISISIfBfdDisable_Type()
)
sleISISIfBfdDisable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfBfdDisable.setStatus("current")


class _SleISISIfCircuitType_Type(Integer32):
    """Custom type sleISISIfCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("level1", 1),
          ("level1To2", 2),
          ("level2", 3))
    )


_SleISISIfCircuitType_Type.__name__ = "Integer32"
_SleISISIfCircuitType_Object = MibTableColumn
sleISISIfCircuitType = _SleISISIfCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 14),
    _SleISISIfCircuitType_Type()
)
sleISISIfCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfCircuitType.setStatus("current")


class _SleISISIfCsnpIntervalLevel1_Type(Integer32):
    """Custom type sleISISIfCsnpIntervalLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfCsnpIntervalLevel1_Type.__name__ = "Integer32"
_SleISISIfCsnpIntervalLevel1_Object = MibTableColumn
sleISISIfCsnpIntervalLevel1 = _SleISISIfCsnpIntervalLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 15),
    _SleISISIfCsnpIntervalLevel1_Type()
)
sleISISIfCsnpIntervalLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfCsnpIntervalLevel1.setStatus("current")


class _SleISISIfCsnpIntervalLevel2_Type(Integer32):
    """Custom type sleISISIfCsnpIntervalLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfCsnpIntervalLevel2_Type.__name__ = "Integer32"
_SleISISIfCsnpIntervalLevel2_Object = MibTableColumn
sleISISIfCsnpIntervalLevel2 = _SleISISIfCsnpIntervalLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 16),
    _SleISISIfCsnpIntervalLevel2_Type()
)
sleISISIfCsnpIntervalLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfCsnpIntervalLevel2.setStatus("current")


class _SleISISIfHelloPadding_Type(Integer32):
    """Custom type sleISISIfHelloPadding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfHelloPadding_Type.__name__ = "Integer32"
_SleISISIfHelloPadding_Object = MibTableColumn
sleISISIfHelloPadding = _SleISISIfHelloPadding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 17),
    _SleISISIfHelloPadding_Type()
)
sleISISIfHelloPadding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfHelloPadding.setStatus("current")


class _SleISISIfHelloIntervalLevel1_Type(Integer32):
    """Custom type sleISISIfHelloIntervalLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfHelloIntervalLevel1_Type.__name__ = "Integer32"
_SleISISIfHelloIntervalLevel1_Object = MibTableColumn
sleISISIfHelloIntervalLevel1 = _SleISISIfHelloIntervalLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 18),
    _SleISISIfHelloIntervalLevel1_Type()
)
sleISISIfHelloIntervalLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfHelloIntervalLevel1.setStatus("current")


class _SleISISIfHelloIntervalLevel2_Type(Integer32):
    """Custom type sleISISIfHelloIntervalLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfHelloIntervalLevel2_Type.__name__ = "Integer32"
_SleISISIfHelloIntervalLevel2_Object = MibTableColumn
sleISISIfHelloIntervalLevel2 = _SleISISIfHelloIntervalLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 19),
    _SleISISIfHelloIntervalLevel2_Type()
)
sleISISIfHelloIntervalLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfHelloIntervalLevel2.setStatus("current")


class _SleISISIfHelloIntervalMinimalLevel1_Type(Integer32):
    """Custom type sleISISIfHelloIntervalMinimalLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfHelloIntervalMinimalLevel1_Type.__name__ = "Integer32"
_SleISISIfHelloIntervalMinimalLevel1_Object = MibTableColumn
sleISISIfHelloIntervalMinimalLevel1 = _SleISISIfHelloIntervalMinimalLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 20),
    _SleISISIfHelloIntervalMinimalLevel1_Type()
)
sleISISIfHelloIntervalMinimalLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfHelloIntervalMinimalLevel1.setStatus("current")


class _SleISISIfHelloIntervalMinimalLevel2_Type(Integer32):
    """Custom type sleISISIfHelloIntervalMinimalLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfHelloIntervalMinimalLevel2_Type.__name__ = "Integer32"
_SleISISIfHelloIntervalMinimalLevel2_Object = MibTableColumn
sleISISIfHelloIntervalMinimalLevel2 = _SleISISIfHelloIntervalMinimalLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 21),
    _SleISISIfHelloIntervalMinimalLevel2_Type()
)
sleISISIfHelloIntervalMinimalLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfHelloIntervalMinimalLevel2.setStatus("current")


class _SleISISIfHelloMultiplierLevel1_Type(Integer32):
    """Custom type sleISISIfHelloMultiplierLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SleISISIfHelloMultiplierLevel1_Type.__name__ = "Integer32"
_SleISISIfHelloMultiplierLevel1_Object = MibTableColumn
sleISISIfHelloMultiplierLevel1 = _SleISISIfHelloMultiplierLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 22),
    _SleISISIfHelloMultiplierLevel1_Type()
)
sleISISIfHelloMultiplierLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfHelloMultiplierLevel1.setStatus("current")


class _SleISISIfHelloMultiplierLevel2_Type(Integer32):
    """Custom type sleISISIfHelloMultiplierLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SleISISIfHelloMultiplierLevel2_Type.__name__ = "Integer32"
_SleISISIfHelloMultiplierLevel2_Object = MibTableColumn
sleISISIfHelloMultiplierLevel2 = _SleISISIfHelloMultiplierLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 23),
    _SleISISIfHelloMultiplierLevel2_Type()
)
sleISISIfHelloMultiplierLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfHelloMultiplierLevel2.setStatus("current")


class _SleISISIfLspInterval_Type(Unsigned32):
    """Custom type sleISISIfLspInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleISISIfLspInterval_Type.__name__ = "Unsigned32"
_SleISISIfLspInterval_Object = MibTableColumn
sleISISIfLspInterval = _SleISISIfLspInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 24),
    _SleISISIfLspInterval_Type()
)
sleISISIfLspInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfLspInterval.setStatus("current")


class _SleISISIfMeshGroup_Type(Unsigned32):
    """Custom type sleISISIfMeshGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_SleISISIfMeshGroup_Type.__name__ = "Unsigned32"
_SleISISIfMeshGroup_Object = MibTableColumn
sleISISIfMeshGroup = _SleISISIfMeshGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 25),
    _SleISISIfMeshGroup_Type()
)
sleISISIfMeshGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfMeshGroup.setStatus("current")


class _SleISISIfMetricLevel1_Type(Integer32):
    """Custom type sleISISIfMetricLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SleISISIfMetricLevel1_Type.__name__ = "Integer32"
_SleISISIfMetricLevel1_Object = MibTableColumn
sleISISIfMetricLevel1 = _SleISISIfMetricLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 26),
    _SleISISIfMetricLevel1_Type()
)
sleISISIfMetricLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfMetricLevel1.setStatus("current")


class _SleISISIfMetricLevel2_Type(Integer32):
    """Custom type sleISISIfMetricLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SleISISIfMetricLevel2_Type.__name__ = "Integer32"
_SleISISIfMetricLevel2_Object = MibTableColumn
sleISISIfMetricLevel2 = _SleISISIfMetricLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 27),
    _SleISISIfMetricLevel2_Type()
)
sleISISIfMetricLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfMetricLevel2.setStatus("current")


class _SleISISIfNetwork_Type(Integer32):
    """Custom type sleISISIfNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("broadcast", 1),
          ("pointToPoint", 2))
    )


_SleISISIfNetwork_Type.__name__ = "Integer32"
_SleISISIfNetwork_Object = MibTableColumn
sleISISIfNetwork = _SleISISIfNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 28),
    _SleISISIfNetwork_Type()
)
sleISISIfNetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfNetwork.setStatus("current")


class _SleISISIfPriorityLevel1_Type(Integer32):
    """Custom type sleISISIfPriorityLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SleISISIfPriorityLevel1_Type.__name__ = "Integer32"
_SleISISIfPriorityLevel1_Object = MibTableColumn
sleISISIfPriorityLevel1 = _SleISISIfPriorityLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 29),
    _SleISISIfPriorityLevel1_Type()
)
sleISISIfPriorityLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfPriorityLevel1.setStatus("current")


class _SleISISIfPriorityLevel2_Type(Integer32):
    """Custom type sleISISIfPriorityLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SleISISIfPriorityLevel2_Type.__name__ = "Integer32"
_SleISISIfPriorityLevel2_Object = MibTableColumn
sleISISIfPriorityLevel2 = _SleISISIfPriorityLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 30),
    _SleISISIfPriorityLevel2_Type()
)
sleISISIfPriorityLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfPriorityLevel2.setStatus("current")


class _SleISISIfRestartHelloIntervalLevel1_Type(Integer32):
    """Custom type sleISISIfRestartHelloIntervalLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfRestartHelloIntervalLevel1_Type.__name__ = "Integer32"
_SleISISIfRestartHelloIntervalLevel1_Object = MibTableColumn
sleISISIfRestartHelloIntervalLevel1 = _SleISISIfRestartHelloIntervalLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 31),
    _SleISISIfRestartHelloIntervalLevel1_Type()
)
sleISISIfRestartHelloIntervalLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfRestartHelloIntervalLevel1.setStatus("current")


class _SleISISIfRestartHelloIntervalLevel2_Type(Integer32):
    """Custom type sleISISIfRestartHelloIntervalLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfRestartHelloIntervalLevel2_Type.__name__ = "Integer32"
_SleISISIfRestartHelloIntervalLevel2_Object = MibTableColumn
sleISISIfRestartHelloIntervalLevel2 = _SleISISIfRestartHelloIntervalLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 32),
    _SleISISIfRestartHelloIntervalLevel2_Type()
)
sleISISIfRestartHelloIntervalLevel2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfRestartHelloIntervalLevel2.setStatus("current")


class _SleISISIfRetransmitInterval_Type(Integer32):
    """Custom type sleISISIfRetransmitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleISISIfRetransmitInterval_Type.__name__ = "Integer32"
_SleISISIfRetransmitInterval_Object = MibTableColumn
sleISISIfRetransmitInterval = _SleISISIfRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 33),
    _SleISISIfRetransmitInterval_Type()
)
sleISISIfRetransmitInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfRetransmitInterval.setStatus("current")


class _SleISISIfWideMetricLevel1_Type(Integer32):
    """Custom type sleISISIfWideMetricLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleISISIfWideMetricLevel1_Type.__name__ = "Integer32"
_SleISISIfWideMetricLevel1_Object = MibTableColumn
sleISISIfWideMetricLevel1 = _SleISISIfWideMetricLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 34),
    _SleISISIfWideMetricLevel1_Type()
)
sleISISIfWideMetricLevel1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfWideMetricLevel1.setStatus("current")


class _SleISISIfWideMetricLevel2_Type(Integer32):
    """Custom type sleISISIfWideMetricLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleISISIfWideMetricLevel2_Type.__name__ = "Integer32"
_SleISISIfWideMetricLevel2_Object = MibTableColumn
sleISISIfWideMetricLevel2 = _SleISISIfWideMetricLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 1, 1, 35),
    _SleISISIfWideMetricLevel2_Type()
)
sleISISIfWideMetricLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfWideMetricLevel2.setStatus("current")
_SleISISIfControl_ObjectIdentity = ObjectIdentity
sleISISIfControl = _SleISISIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2)
)


class _SleISISIfControlRequest_Type(SleControlRequestResultType):
    """Custom type sleISISIfControlRequest based on SleControlRequestResultType"""
    subtypeSpec = SleControlRequestResultType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setISISIfProfile", 1)
    )


_SleISISIfControlRequest_Type.__name__ = "SleControlRequestResultType"
_SleISISIfControlRequest_Object = MibScalar
sleISISIfControlRequest = _SleISISIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 1),
    _SleISISIfControlRequest_Type()
)
sleISISIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlRequest.setStatus("current")
_SleISISIfControlStatus_Type = SleControlStatusType
_SleISISIfControlStatus_Object = MibScalar
sleISISIfControlStatus = _SleISISIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 2),
    _SleISISIfControlStatus_Type()
)
sleISISIfControlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlStatus.setStatus("current")
_SleISISIfControlTimer_Type = Gauge32
_SleISISIfControlTimer_Object = MibScalar
sleISISIfControlTimer = _SleISISIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 3),
    _SleISISIfControlTimer_Type()
)
sleISISIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlTimer.setStatus("current")
_SleISISIfControlTimeStamp_Type = TimeTicks
_SleISISIfControlTimeStamp_Object = MibScalar
sleISISIfControlTimeStamp = _SleISISIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 4),
    _SleISISIfControlTimeStamp_Type()
)
sleISISIfControlTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlTimeStamp.setStatus("current")
_SleISISIfControlReqResult_Type = SleControlRequestResultType
_SleISISIfControlReqResult_Object = MibScalar
sleISISIfControlReqResult = _SleISISIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 5),
    _SleISISIfControlReqResult_Type()
)
sleISISIfControlReqResult.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlReqResult.setStatus("current")
_SleISISIfControlIndex_Type = Integer32
_SleISISIfControlIndex_Object = MibScalar
sleISISIfControlIndex = _SleISISIfControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 6),
    _SleISISIfControlIndex_Type()
)
sleISISIfControlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlIndex.setStatus("current")


class _SleISISIfControlMplsLdpIgpSync_Type(Integer32):
    """Custom type sleISISIfControlMplsLdpIgpSync based on Integer32"""
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
        *(("disable", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2", 3))
    )


_SleISISIfControlMplsLdpIgpSync_Type.__name__ = "Integer32"
_SleISISIfControlMplsLdpIgpSync_Object = MibScalar
sleISISIfControlMplsLdpIgpSync = _SleISISIfControlMplsLdpIgpSync_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 7),
    _SleISISIfControlMplsLdpIgpSync_Type()
)
sleISISIfControlMplsLdpIgpSync.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlMplsLdpIgpSync.setStatus("current")


class _SleISISIfControlIpRouter_Type(Integer32):
    """Custom type sleISISIfControlIpRouter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("dissable", 0),
          ("enable", 1))
    )


_SleISISIfControlIpRouter_Type.__name__ = "Integer32"
_SleISISIfControlIpRouter_Object = MibScalar
sleISISIfControlIpRouter = _SleISISIfControlIpRouter_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 8),
    _SleISISIfControlIpRouter_Type()
)
sleISISIfControlIpRouter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlIpRouter.setStatus("current")


class _SleISISIfControlAuthSendLevel1_Type(Integer32):
    """Custom type sleISISIfControlAuthSendLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlAuthSendLevel1_Type.__name__ = "Integer32"
_SleISISIfControlAuthSendLevel1_Object = MibScalar
sleISISIfControlAuthSendLevel1 = _SleISISIfControlAuthSendLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 9),
    _SleISISIfControlAuthSendLevel1_Type()
)
sleISISIfControlAuthSendLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlAuthSendLevel1.setStatus("current")


class _SleISISIfControlAuthSendLevel2_Type(Integer32):
    """Custom type sleISISIfControlAuthSendLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlAuthSendLevel2_Type.__name__ = "Integer32"
_SleISISIfControlAuthSendLevel2_Object = MibScalar
sleISISIfControlAuthSendLevel2 = _SleISISIfControlAuthSendLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 10),
    _SleISISIfControlAuthSendLevel2_Type()
)
sleISISIfControlAuthSendLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlAuthSendLevel2.setStatus("current")


class _SleISISIfControlAuthModeMd5Levle1_Type(Integer32):
    """Custom type sleISISIfControlAuthModeMd5Levle1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlAuthModeMd5Levle1_Type.__name__ = "Integer32"
_SleISISIfControlAuthModeMd5Levle1_Object = MibScalar
sleISISIfControlAuthModeMd5Levle1 = _SleISISIfControlAuthModeMd5Levle1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 11),
    _SleISISIfControlAuthModeMd5Levle1_Type()
)
sleISISIfControlAuthModeMd5Levle1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlAuthModeMd5Levle1.setStatus("current")


class _SleISISIfControlAuthModeMd5Levle2_Type(Integer32):
    """Custom type sleISISIfControlAuthModeMd5Levle2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlAuthModeMd5Levle2_Type.__name__ = "Integer32"
_SleISISIfControlAuthModeMd5Levle2_Object = MibScalar
sleISISIfControlAuthModeMd5Levle2 = _SleISISIfControlAuthModeMd5Levle2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 12),
    _SleISISIfControlAuthModeMd5Levle2_Type()
)
sleISISIfControlAuthModeMd5Levle2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlAuthModeMd5Levle2.setStatus("current")


class _SleISISIfControlAuthModeTextLevle1_Type(Integer32):
    """Custom type sleISISIfControlAuthModeTextLevle1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlAuthModeTextLevle1_Type.__name__ = "Integer32"
_SleISISIfControlAuthModeTextLevle1_Object = MibScalar
sleISISIfControlAuthModeTextLevle1 = _SleISISIfControlAuthModeTextLevle1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 13),
    _SleISISIfControlAuthModeTextLevle1_Type()
)
sleISISIfControlAuthModeTextLevle1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlAuthModeTextLevle1.setStatus("current")


class _SleISISIfControlAuthModeTextLevle2_Type(Integer32):
    """Custom type sleISISIfControlAuthModeTextLevle2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlAuthModeTextLevle2_Type.__name__ = "Integer32"
_SleISISIfControlAuthModeTextLevle2_Object = MibScalar
sleISISIfControlAuthModeTextLevle2 = _SleISISIfControlAuthModeTextLevle2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 14),
    _SleISISIfControlAuthModeTextLevle2_Type()
)
sleISISIfControlAuthModeTextLevle2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlAuthModeTextLevle2.setStatus("current")
_SleISISIfControlAuthKeyChainLevle1_Type = OctetString
_SleISISIfControlAuthKeyChainLevle1_Object = MibScalar
sleISISIfControlAuthKeyChainLevle1 = _SleISISIfControlAuthKeyChainLevle1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 15),
    _SleISISIfControlAuthKeyChainLevle1_Type()
)
sleISISIfControlAuthKeyChainLevle1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlAuthKeyChainLevle1.setStatus("current")
_SleISISIfControlAuthKeyChainLevle2_Type = OctetString
_SleISISIfControlAuthKeyChainLevle2_Object = MibScalar
sleISISIfControlAuthKeyChainLevle2 = _SleISISIfControlAuthKeyChainLevle2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 16),
    _SleISISIfControlAuthKeyChainLevle2_Type()
)
sleISISIfControlAuthKeyChainLevle2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlAuthKeyChainLevle2.setStatus("current")


class _SleISISIfControlBfd_Type(Integer32):
    """Custom type sleISISIfControlBfd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlBfd_Type.__name__ = "Integer32"
_SleISISIfControlBfd_Object = MibScalar
sleISISIfControlBfd = _SleISISIfControlBfd_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 17),
    _SleISISIfControlBfd_Type()
)
sleISISIfControlBfd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlBfd.setStatus("current")


class _SleISISIfControlBfdDisable_Type(Integer32):
    """Custom type sleISISIfControlBfdDisable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlBfdDisable_Type.__name__ = "Integer32"
_SleISISIfControlBfdDisable_Object = MibScalar
sleISISIfControlBfdDisable = _SleISISIfControlBfdDisable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 18),
    _SleISISIfControlBfdDisable_Type()
)
sleISISIfControlBfdDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlBfdDisable.setStatus("current")


class _SleISISIfControlCircuitType_Type(Integer32):
    """Custom type sleISISIfControlCircuitType based on Integer32"""
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
        *(("disable", 0),
          ("level1", 1),
          ("level1To2", 2),
          ("level2", 3))
    )


_SleISISIfControlCircuitType_Type.__name__ = "Integer32"
_SleISISIfControlCircuitType_Object = MibScalar
sleISISIfControlCircuitType = _SleISISIfControlCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 19),
    _SleISISIfControlCircuitType_Type()
)
sleISISIfControlCircuitType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlCircuitType.setStatus("current")


class _SleISISIfControlCsnpIntervalLevel1_Type(Integer32):
    """Custom type sleISISIfControlCsnpIntervalLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfControlCsnpIntervalLevel1_Type.__name__ = "Integer32"
_SleISISIfControlCsnpIntervalLevel1_Object = MibScalar
sleISISIfControlCsnpIntervalLevel1 = _SleISISIfControlCsnpIntervalLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 20),
    _SleISISIfControlCsnpIntervalLevel1_Type()
)
sleISISIfControlCsnpIntervalLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlCsnpIntervalLevel1.setStatus("current")


class _SleISISIfControlCsnpIntervalLevel2_Type(Integer32):
    """Custom type sleISISIfControlCsnpIntervalLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfControlCsnpIntervalLevel2_Type.__name__ = "Integer32"
_SleISISIfControlCsnpIntervalLevel2_Object = MibScalar
sleISISIfControlCsnpIntervalLevel2 = _SleISISIfControlCsnpIntervalLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 21),
    _SleISISIfControlCsnpIntervalLevel2_Type()
)
sleISISIfControlCsnpIntervalLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlCsnpIntervalLevel2.setStatus("current")


class _SleISISIfControlHelloPadding_Type(Integer32):
    """Custom type sleISISIfControlHelloPadding based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlHelloPadding_Type.__name__ = "Integer32"
_SleISISIfControlHelloPadding_Object = MibScalar
sleISISIfControlHelloPadding = _SleISISIfControlHelloPadding_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 22),
    _SleISISIfControlHelloPadding_Type()
)
sleISISIfControlHelloPadding.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlHelloPadding.setStatus("current")


class _SleISISIfControlHelloIntervalLevel1_Type(Integer32):
    """Custom type sleISISIfControlHelloIntervalLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfControlHelloIntervalLevel1_Type.__name__ = "Integer32"
_SleISISIfControlHelloIntervalLevel1_Object = MibScalar
sleISISIfControlHelloIntervalLevel1 = _SleISISIfControlHelloIntervalLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 23),
    _SleISISIfControlHelloIntervalLevel1_Type()
)
sleISISIfControlHelloIntervalLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlHelloIntervalLevel1.setStatus("current")


class _SleISISIfControlHelloIntervalLevel2_Type(Integer32):
    """Custom type sleISISIfControlHelloIntervalLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfControlHelloIntervalLevel2_Type.__name__ = "Integer32"
_SleISISIfControlHelloIntervalLevel2_Object = MibScalar
sleISISIfControlHelloIntervalLevel2 = _SleISISIfControlHelloIntervalLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 24),
    _SleISISIfControlHelloIntervalLevel2_Type()
)
sleISISIfControlHelloIntervalLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlHelloIntervalLevel2.setStatus("current")


class _SleISISIfControlHelloIntervalMinimalLevel1_Type(Integer32):
    """Custom type sleISISIfControlHelloIntervalMinimalLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlHelloIntervalMinimalLevel1_Type.__name__ = "Integer32"
_SleISISIfControlHelloIntervalMinimalLevel1_Object = MibScalar
sleISISIfControlHelloIntervalMinimalLevel1 = _SleISISIfControlHelloIntervalMinimalLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 25),
    _SleISISIfControlHelloIntervalMinimalLevel1_Type()
)
sleISISIfControlHelloIntervalMinimalLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlHelloIntervalMinimalLevel1.setStatus("current")


class _SleISISIfControlHelloIntervalMinimalLevel2_Type(Integer32):
    """Custom type sleISISIfControlHelloIntervalMinimalLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_SleISISIfControlHelloIntervalMinimalLevel2_Type.__name__ = "Integer32"
_SleISISIfControlHelloIntervalMinimalLevel2_Object = MibScalar
sleISISIfControlHelloIntervalMinimalLevel2 = _SleISISIfControlHelloIntervalMinimalLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 26),
    _SleISISIfControlHelloIntervalMinimalLevel2_Type()
)
sleISISIfControlHelloIntervalMinimalLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlHelloIntervalMinimalLevel2.setStatus("current")


class _SleISISIfControlHelloMultiplierLevel1_Type(Integer32):
    """Custom type sleISISIfControlHelloMultiplierLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SleISISIfControlHelloMultiplierLevel1_Type.__name__ = "Integer32"
_SleISISIfControlHelloMultiplierLevel1_Object = MibScalar
sleISISIfControlHelloMultiplierLevel1 = _SleISISIfControlHelloMultiplierLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 27),
    _SleISISIfControlHelloMultiplierLevel1_Type()
)
sleISISIfControlHelloMultiplierLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlHelloMultiplierLevel1.setStatus("current")


class _SleISISIfControlHelloMultiplierLevel2_Type(Integer32):
    """Custom type sleISISIfControlHelloMultiplierLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_SleISISIfControlHelloMultiplierLevel2_Type.__name__ = "Integer32"
_SleISISIfControlHelloMultiplierLevel2_Object = MibScalar
sleISISIfControlHelloMultiplierLevel2 = _SleISISIfControlHelloMultiplierLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 28),
    _SleISISIfControlHelloMultiplierLevel2_Type()
)
sleISISIfControlHelloMultiplierLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlHelloMultiplierLevel2.setStatus("current")


class _SleISISIfControlLspInterval_Type(Unsigned32):
    """Custom type sleISISIfControlLspInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4294967295),
    )


_SleISISIfControlLspInterval_Type.__name__ = "Unsigned32"
_SleISISIfControlLspInterval_Object = MibScalar
sleISISIfControlLspInterval = _SleISISIfControlLspInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 29),
    _SleISISIfControlLspInterval_Type()
)
sleISISIfControlLspInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlLspInterval.setStatus("current")


class _SleISISIfControlMeshGroup_Type(Unsigned32):
    """Custom type sleISISIfControlMeshGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_SleISISIfControlMeshGroup_Type.__name__ = "Unsigned32"
_SleISISIfControlMeshGroup_Object = MibScalar
sleISISIfControlMeshGroup = _SleISISIfControlMeshGroup_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 30),
    _SleISISIfControlMeshGroup_Type()
)
sleISISIfControlMeshGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlMeshGroup.setStatus("current")


class _SleISISIfControlMetricLevel1_Type(Integer32):
    """Custom type sleISISIfControlMetricLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SleISISIfControlMetricLevel1_Type.__name__ = "Integer32"
_SleISISIfControlMetricLevel1_Object = MibScalar
sleISISIfControlMetricLevel1 = _SleISISIfControlMetricLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 31),
    _SleISISIfControlMetricLevel1_Type()
)
sleISISIfControlMetricLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlMetricLevel1.setStatus("current")


class _SleISISIfControlMetricLevel2_Type(Integer32):
    """Custom type sleISISIfControlMetricLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SleISISIfControlMetricLevel2_Type.__name__ = "Integer32"
_SleISISIfControlMetricLevel2_Object = MibScalar
sleISISIfControlMetricLevel2 = _SleISISIfControlMetricLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 32),
    _SleISISIfControlMetricLevel2_Type()
)
sleISISIfControlMetricLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlMetricLevel2.setStatus("current")


class _SleISISIfControlNetwork_Type(Integer32):
    """Custom type sleISISIfControlNetwork based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("broadcast", 1),
          ("pointToPoint", 2))
    )


_SleISISIfControlNetwork_Type.__name__ = "Integer32"
_SleISISIfControlNetwork_Object = MibScalar
sleISISIfControlNetwork = _SleISISIfControlNetwork_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 33),
    _SleISISIfControlNetwork_Type()
)
sleISISIfControlNetwork.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlNetwork.setStatus("current")


class _SleISISIfControlPriorityLevel1_Type(Integer32):
    """Custom type sleISISIfControlPriorityLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SleISISIfControlPriorityLevel1_Type.__name__ = "Integer32"
_SleISISIfControlPriorityLevel1_Object = MibScalar
sleISISIfControlPriorityLevel1 = _SleISISIfControlPriorityLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 34),
    _SleISISIfControlPriorityLevel1_Type()
)
sleISISIfControlPriorityLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlPriorityLevel1.setStatus("current")


class _SleISISIfControlPriorityLevel2_Type(Integer32):
    """Custom type sleISISIfControlPriorityLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_SleISISIfControlPriorityLevel2_Type.__name__ = "Integer32"
_SleISISIfControlPriorityLevel2_Object = MibScalar
sleISISIfControlPriorityLevel2 = _SleISISIfControlPriorityLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 35),
    _SleISISIfControlPriorityLevel2_Type()
)
sleISISIfControlPriorityLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlPriorityLevel2.setStatus("current")


class _SleISISIfControlRestartHelloIntervalLevel1_Type(Integer32):
    """Custom type sleISISIfControlRestartHelloIntervalLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfControlRestartHelloIntervalLevel1_Type.__name__ = "Integer32"
_SleISISIfControlRestartHelloIntervalLevel1_Object = MibScalar
sleISISIfControlRestartHelloIntervalLevel1 = _SleISISIfControlRestartHelloIntervalLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 36),
    _SleISISIfControlRestartHelloIntervalLevel1_Type()
)
sleISISIfControlRestartHelloIntervalLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlRestartHelloIntervalLevel1.setStatus("current")


class _SleISISIfControlRestartHelloIntervalLevel2_Type(Integer32):
    """Custom type sleISISIfControlRestartHelloIntervalLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfControlRestartHelloIntervalLevel2_Type.__name__ = "Integer32"
_SleISISIfControlRestartHelloIntervalLevel2_Object = MibScalar
sleISISIfControlRestartHelloIntervalLevel2 = _SleISISIfControlRestartHelloIntervalLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 37),
    _SleISISIfControlRestartHelloIntervalLevel2_Type()
)
sleISISIfControlRestartHelloIntervalLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlRestartHelloIntervalLevel2.setStatus("current")


class _SleISISIfControlRetransmitInterval_Type(Integer32):
    """Custom type sleISISIfControlRetransmitInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleISISIfControlRetransmitInterval_Type.__name__ = "Integer32"
_SleISISIfControlRetransmitInterval_Object = MibScalar
sleISISIfControlRetransmitInterval = _SleISISIfControlRetransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 38),
    _SleISISIfControlRetransmitInterval_Type()
)
sleISISIfControlRetransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlRetransmitInterval.setStatus("current")


class _SleISISIfControlWideMetricLevel1_Type(Integer32):
    """Custom type sleISISIfControlWideMetricLevel1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleISISIfControlWideMetricLevel1_Type.__name__ = "Integer32"
_SleISISIfControlWideMetricLevel1_Object = MibScalar
sleISISIfControlWideMetricLevel1 = _SleISISIfControlWideMetricLevel1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 39),
    _SleISISIfControlWideMetricLevel1_Type()
)
sleISISIfControlWideMetricLevel1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlWideMetricLevel1.setStatus("current")


class _SleISISIfControlWideMetricLevel2_Type(Integer32):
    """Custom type sleISISIfControlWideMetricLevel2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16777214),
    )


_SleISISIfControlWideMetricLevel2_Type.__name__ = "Integer32"
_SleISISIfControlWideMetricLevel2_Object = MibScalar
sleISISIfControlWideMetricLevel2 = _SleISISIfControlWideMetricLevel2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 2, 40),
    _SleISISIfControlWideMetricLevel2_Type()
)
sleISISIfControlWideMetricLevel2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISIfControlWideMetricLevel2.setStatus("current")
_SlsISISNotification_ObjectIdentity = ObjectIdentity
slsISISNotification = _SlsISISNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 3)
)
_SleISISIfStatusTable_Object = MibTable
sleISISIfStatusTable = _SleISISIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4)
)
if mibBuilder.loadTexts:
    sleISISIfStatusTable.setStatus("current")
_SleISISIfStatusEntry_Object = MibTableRow
sleISISIfStatusEntry = _SleISISIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1)
)
sleISISIfStatusEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISIfStatusIfIndex"),
)
if mibBuilder.loadTexts:
    sleISISIfStatusEntry.setStatus("current")


class _SleISISIfStatusIfIndex_Type(Integer32):
    """Custom type sleISISIfStatusIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISIfStatusIfIndex_Type.__name__ = "Integer32"
_SleISISIfStatusIfIndex_Object = MibTableColumn
sleISISIfStatusIfIndex = _SleISISIfStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 1),
    _SleISISIfStatusIfIndex_Type()
)
sleISISIfStatusIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISIfStatusIfIndex.setStatus("current")


class _SleIsisIfStatusIfStatus_Type(Integer32):
    """Custom type sleIsisIfStatusIfStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("down", 0),
          ("up", 1))
    )


_SleIsisIfStatusIfStatus_Type.__name__ = "Integer32"
_SleIsisIfStatusIfStatus_Object = MibTableColumn
sleIsisIfStatusIfStatus = _SleIsisIfStatusIfStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 2),
    _SleIsisIfStatusIfStatus_Type()
)
sleIsisIfStatusIfStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusIfStatus.setStatus("current")
_SleIsisIfStatusIsisTag_Type = OctetString
_SleIsisIfStatusIsisTag_Object = MibTableColumn
sleIsisIfStatusIsisTag = _SleIsisIfStatusIsisTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 3),
    _SleIsisIfStatusIsisTag_Type()
)
sleIsisIfStatusIsisTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusIsisTag.setStatus("current")


class _SleIsisIfStatusNetworkType_Type(Integer32):
    """Custom type sleIsisIfStatusNetworkType based on Integer32"""
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
        *(("unknown", 0),
          ("broadcast", 1),
          ("point2Point", 2),
          ("loopback", 3))
    )


_SleIsisIfStatusNetworkType_Type.__name__ = "Integer32"
_SleIsisIfStatusNetworkType_Object = MibTableColumn
sleIsisIfStatusNetworkType = _SleIsisIfStatusNetworkType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 4),
    _SleIsisIfStatusNetworkType_Type()
)
sleIsisIfStatusNetworkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusNetworkType.setStatus("current")


class _SleIsisIfStatusCircuitType_Type(Integer32):
    """Custom type sleIsisIfStatusCircuitType based on Integer32"""
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
        *(("unknown", 0),
          ("level1", 1),
          ("level2", 2),
          ("level1And2", 3))
    )


_SleIsisIfStatusCircuitType_Type.__name__ = "Integer32"
_SleIsisIfStatusCircuitType_Object = MibTableColumn
sleIsisIfStatusCircuitType = _SleIsisIfStatusCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 5),
    _SleIsisIfStatusCircuitType_Type()
)
sleIsisIfStatusCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitType.setStatus("current")
_SleIsisIfStatusLocalCircuitId_Type = Integer32
_SleIsisIfStatusLocalCircuitId_Object = MibTableColumn
sleIsisIfStatusLocalCircuitId = _SleIsisIfStatusLocalCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 6),
    _SleIsisIfStatusLocalCircuitId_Type()
)
sleIsisIfStatusLocalCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusLocalCircuitId.setStatus("current")
_SleIsisIfStatusExtendedLocalCircuitId_Type = Integer32
_SleIsisIfStatusExtendedLocalCircuitId_Object = MibTableColumn
sleIsisIfStatusExtendedLocalCircuitId = _SleIsisIfStatusExtendedLocalCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 7),
    _SleIsisIfStatusExtendedLocalCircuitId_Type()
)
sleIsisIfStatusExtendedLocalCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusExtendedLocalCircuitId.setStatus("current")
_SleIsisIfStatusLocalSnpa_Type = OctetString
_SleIsisIfStatusLocalSnpa_Object = MibTableColumn
sleIsisIfStatusLocalSnpa = _SleIsisIfStatusLocalSnpa_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 8),
    _SleIsisIfStatusLocalSnpa_Type()
)
sleIsisIfStatusLocalSnpa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusLocalSnpa.setStatus("current")
_SleIsisIfStatusLdpSyncHoldTimer_Type = Integer32
_SleIsisIfStatusLdpSyncHoldTimer_Object = MibTableColumn
sleIsisIfStatusLdpSyncHoldTimer = _SleIsisIfStatusLdpSyncHoldTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 9),
    _SleIsisIfStatusLdpSyncHoldTimer_Type()
)
sleIsisIfStatusLdpSyncHoldTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusLdpSyncHoldTimer.setStatus("current")
_SleIsisIfStatusLdpSyncRemainingTime_Type = Integer32
_SleIsisIfStatusLdpSyncRemainingTime_Object = MibTableColumn
sleIsisIfStatusLdpSyncRemainingTime = _SleIsisIfStatusLdpSyncRemainingTime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 10),
    _SleIsisIfStatusLdpSyncRemainingTime_Type()
)
sleIsisIfStatusLdpSyncRemainingTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusLdpSyncRemainingTime.setStatus("current")
_SleIsisIfStatusCircuitL1Metric_Type = Integer32
_SleIsisIfStatusCircuitL1Metric_Object = MibTableColumn
sleIsisIfStatusCircuitL1Metric = _SleIsisIfStatusCircuitL1Metric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 11),
    _SleIsisIfStatusCircuitL1Metric_Type()
)
sleIsisIfStatusCircuitL1Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL1Metric.setStatus("current")
_SleIsisIfStatusCircuitL1WideMetric_Type = Integer32
_SleIsisIfStatusCircuitL1WideMetric_Object = MibTableColumn
sleIsisIfStatusCircuitL1WideMetric = _SleIsisIfStatusCircuitL1WideMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 12),
    _SleIsisIfStatusCircuitL1WideMetric_Type()
)
sleIsisIfStatusCircuitL1WideMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL1WideMetric.setStatus("current")
_SleIsisIfStatusCircuitL1Priority_Type = Integer32
_SleIsisIfStatusCircuitL1Priority_Object = MibTableColumn
sleIsisIfStatusCircuitL1Priority = _SleIsisIfStatusCircuitL1Priority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 13),
    _SleIsisIfStatusCircuitL1Priority_Type()
)
sleIsisIfStatusCircuitL1Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL1Priority.setStatus("current")
_SleIsisIfStatusCircuitL1CircuitId_Type = Integer32
_SleIsisIfStatusCircuitL1CircuitId_Object = MibTableColumn
sleIsisIfStatusCircuitL1CircuitId = _SleIsisIfStatusCircuitL1CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 14),
    _SleIsisIfStatusCircuitL1CircuitId_Type()
)
sleIsisIfStatusCircuitL1CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL1CircuitId.setStatus("current")
_SleIsisIfStatusCircuitL1ActiveAdjacencies_Type = Integer32
_SleIsisIfStatusCircuitL1ActiveAdjacencies_Object = MibTableColumn
sleIsisIfStatusCircuitL1ActiveAdjacencies = _SleIsisIfStatusCircuitL1ActiveAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 15),
    _SleIsisIfStatusCircuitL1ActiveAdjacencies_Type()
)
sleIsisIfStatusCircuitL1ActiveAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL1ActiveAdjacencies.setStatus("current")
_SleIsisIfStatusCircuitL1LscpMtu_Type = Integer32
_SleIsisIfStatusCircuitL1LscpMtu_Object = MibTableColumn
sleIsisIfStatusCircuitL1LscpMtu = _SleIsisIfStatusCircuitL1LscpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 16),
    _SleIsisIfStatusCircuitL1LscpMtu_Type()
)
sleIsisIfStatusCircuitL1LscpMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL1LscpMtu.setStatus("current")
_SleIsisIfStatusCircuitL2Metric_Type = Integer32
_SleIsisIfStatusCircuitL2Metric_Object = MibTableColumn
sleIsisIfStatusCircuitL2Metric = _SleIsisIfStatusCircuitL2Metric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 17),
    _SleIsisIfStatusCircuitL2Metric_Type()
)
sleIsisIfStatusCircuitL2Metric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL2Metric.setStatus("current")
_SleIsisIfStatusCircuitL2WideMetric_Type = Integer32
_SleIsisIfStatusCircuitL2WideMetric_Object = MibTableColumn
sleIsisIfStatusCircuitL2WideMetric = _SleIsisIfStatusCircuitL2WideMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 18),
    _SleIsisIfStatusCircuitL2WideMetric_Type()
)
sleIsisIfStatusCircuitL2WideMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL2WideMetric.setStatus("current")
_SleIsisIfStatusCircuitL2Priority_Type = Integer32
_SleIsisIfStatusCircuitL2Priority_Object = MibTableColumn
sleIsisIfStatusCircuitL2Priority = _SleIsisIfStatusCircuitL2Priority_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 19),
    _SleIsisIfStatusCircuitL2Priority_Type()
)
sleIsisIfStatusCircuitL2Priority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL2Priority.setStatus("current")
_SleIsisIfStatusCircuitL2CircuitId_Type = Integer32
_SleIsisIfStatusCircuitL2CircuitId_Object = MibTableColumn
sleIsisIfStatusCircuitL2CircuitId = _SleIsisIfStatusCircuitL2CircuitId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 20),
    _SleIsisIfStatusCircuitL2CircuitId_Type()
)
sleIsisIfStatusCircuitL2CircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL2CircuitId.setStatus("current")
_SleIsisIfStatusCircuitL2ActiveAdjacencies_Type = Integer32
_SleIsisIfStatusCircuitL2ActiveAdjacencies_Object = MibTableColumn
sleIsisIfStatusCircuitL2ActiveAdjacencies = _SleIsisIfStatusCircuitL2ActiveAdjacencies_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 21),
    _SleIsisIfStatusCircuitL2ActiveAdjacencies_Type()
)
sleIsisIfStatusCircuitL2ActiveAdjacencies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL2ActiveAdjacencies.setStatus("current")
_SleIsisIfStatusCircuitL2LscpMtu_Type = Integer32
_SleIsisIfStatusCircuitL2LscpMtu_Object = MibTableColumn
sleIsisIfStatusCircuitL2LscpMtu = _SleIsisIfStatusCircuitL2LscpMtu_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 22),
    _SleIsisIfStatusCircuitL2LscpMtu_Type()
)
sleIsisIfStatusCircuitL2LscpMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusCircuitL2LscpMtu.setStatus("current")
_SleIsisIfStatusL1HelloTimerBroadcast_Type = OctetString
_SleIsisIfStatusL1HelloTimerBroadcast_Object = MibTableColumn
sleIsisIfStatusL1HelloTimerBroadcast = _SleIsisIfStatusL1HelloTimerBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 23),
    _SleIsisIfStatusL1HelloTimerBroadcast_Type()
)
sleIsisIfStatusL1HelloTimerBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusL1HelloTimerBroadcast.setStatus("current")
_SleIsisIfStatusL2HelloTimerBroadcast_Type = OctetString
_SleIsisIfStatusL2HelloTimerBroadcast_Object = MibTableColumn
sleIsisIfStatusL2HelloTimerBroadcast = _SleIsisIfStatusL2HelloTimerBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 24),
    _SleIsisIfStatusL2HelloTimerBroadcast_Type()
)
sleIsisIfStatusL2HelloTimerBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusL2HelloTimerBroadcast.setStatus("current")
_SleIsisIfStatusL1HellotimerPoint2Point_Type = OctetString
_SleIsisIfStatusL1HellotimerPoint2Point_Object = MibTableColumn
sleIsisIfStatusL1HellotimerPoint2Point = _SleIsisIfStatusL1HellotimerPoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 25),
    _SleIsisIfStatusL1HellotimerPoint2Point_Type()
)
sleIsisIfStatusL1HellotimerPoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusL1HellotimerPoint2Point.setStatus("current")
_SleIsisIfStatusL2HellotimerPoint2Point_Type = OctetString
_SleIsisIfStatusL2HellotimerPoint2Point_Object = MibTableColumn
sleIsisIfStatusL2HellotimerPoint2Point = _SleIsisIfStatusL2HellotimerPoint2Point_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 3, 4, 1, 26),
    _SleIsisIfStatusL2HellotimerPoint2Point_Type()
)
sleIsisIfStatusL2HellotimerPoint2Point.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleIsisIfStatusL2HellotimerPoint2Point.setStatus("current")
_SleISISInstIf_ObjectIdentity = ObjectIdentity
sleISISInstIf = _SleISISInstIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4)
)
_SleISISInstIfTable_Object = MibTable
sleISISInstIfTable = _SleISISInstIfTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 1)
)
if mibBuilder.loadTexts:
    sleISISInstIfTable.setStatus("current")
_SleISISInstIfEntry_Object = MibTableRow
sleISISInstIfEntry = _SleISISInstIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 1, 1)
)
sleISISInstIfEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISInstIfInstanceId"),
    (0, "SLE-ISIS-MIB", "sleISISInstIfInterfaceId"),
)
if mibBuilder.loadTexts:
    sleISISInstIfEntry.setStatus("current")


class _SleISISInstIfInstanceId_Type(Integer32):
    """Custom type sleISISInstIfInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISInstIfInstanceId_Type.__name__ = "Integer32"
_SleISISInstIfInstanceId_Object = MibTableColumn
sleISISInstIfInstanceId = _SleISISInstIfInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 1, 1, 1),
    _SleISISInstIfInstanceId_Type()
)
sleISISInstIfInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstIfInstanceId.setStatus("current")


class _SleISISInstIfInterfaceId_Type(Integer32):
    """Custom type sleISISInstIfInterfaceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISInstIfInterfaceId_Type.__name__ = "Integer32"
_SleISISInstIfInterfaceId_Object = MibTableColumn
sleISISInstIfInterfaceId = _SleISISInstIfInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 1, 1, 2),
    _SleISISInstIfInterfaceId_Type()
)
sleISISInstIfInterfaceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstIfInterfaceId.setStatus("current")


class _SleISISPassiveInterface_Type(Integer32):
    """Custom type sleISISPassiveInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1))
    )


_SleISISPassiveInterface_Type.__name__ = "Integer32"
_SleISISPassiveInterface_Object = MibTableColumn
sleISISPassiveInterface = _SleISISPassiveInterface_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 1, 1, 3),
    _SleISISPassiveInterface_Type()
)
sleISISPassiveInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISPassiveInterface.setStatus("current")
_SleISISInstIfControl_ObjectIdentity = ObjectIdentity
sleISISInstIfControl = _SleISISInstIfControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 2)
)


class _SleISISInstIfControlRequest_Type(Integer32):
    """Custom type sleISISInstIfControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setISISInstIfPassiveIf", 1),
          ("delISISInstIfPassiveIf", 2))
    )


_SleISISInstIfControlRequest_Type.__name__ = "Integer32"
_SleISISInstIfControlRequest_Object = MibScalar
sleISISInstIfControlRequest = _SleISISInstIfControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 2, 1),
    _SleISISInstIfControlRequest_Type()
)
sleISISInstIfControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstIfControlRequest.setStatus("current")
_SleISISInstIfControlStatus_Type = SleControlStatusType
_SleISISInstIfControlStatus_Object = MibScalar
sleISISInstIfControlStatus = _SleISISInstIfControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 2, 2),
    _SleISISInstIfControlStatus_Type()
)
sleISISInstIfControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstIfControlStatus.setStatus("current")
_SleISISInstIfControlTimer_Type = Gauge32
_SleISISInstIfControlTimer_Object = MibScalar
sleISISInstIfControlTimer = _SleISISInstIfControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 2, 3),
    _SleISISInstIfControlTimer_Type()
)
sleISISInstIfControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstIfControlTimer.setStatus("current")
_SleISISInstIfControlTimeStamp_Type = TimeTicks
_SleISISInstIfControlTimeStamp_Object = MibScalar
sleISISInstIfControlTimeStamp = _SleISISInstIfControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 2, 4),
    _SleISISInstIfControlTimeStamp_Type()
)
sleISISInstIfControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstIfControlTimeStamp.setStatus("current")
_SleISISInstIfControlReqResult_Type = SleControlRequestResultType
_SleISISInstIfControlReqResult_Object = MibScalar
sleISISInstIfControlReqResult = _SleISISInstIfControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 2, 5),
    _SleISISInstIfControlReqResult_Type()
)
sleISISInstIfControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstIfControlReqResult.setStatus("current")
_SleISISInstIfControlInstanceId_Type = Integer32
_SleISISInstIfControlInstanceId_Object = MibScalar
sleISISInstIfControlInstanceId = _SleISISInstIfControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 2, 6),
    _SleISISInstIfControlInstanceId_Type()
)
sleISISInstIfControlInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstIfControlInstanceId.setStatus("current")
_SleISISInstIfControlInterfaceId_Type = Integer32
_SleISISInstIfControlInterfaceId_Object = MibScalar
sleISISInstIfControlInterfaceId = _SleISISInstIfControlInterfaceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 4, 2, 7),
    _SleISISInstIfControlInterfaceId_Type()
)
sleISISInstIfControlInterfaceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstIfControlInterfaceId.setStatus("current")
_SleISISInstRedistribute_ObjectIdentity = ObjectIdentity
sleISISInstRedistribute = _SleISISInstRedistribute_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5)
)
_SleISISInstRedistProtocol_ObjectIdentity = ObjectIdentity
sleISISInstRedistProtocol = _SleISISInstRedistProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1)
)
_SleISISInstRedistProtocolTable_Object = MibTable
sleISISInstRedistProtocolTable = _SleISISInstRedistProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 1)
)
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolTable.setStatus("current")
_SleISISInstRedistProtocolEntry_Object = MibTableRow
sleISISInstRedistProtocolEntry = _SleISISInstRedistProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 1, 1)
)
sleISISInstRedistProtocolEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISInstRedistProtocolInstanceId"),
    (0, "SLE-ISIS-MIB", "sleISISInstRedistProtocolId"),
)
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolEntry.setStatus("current")


class _SleISISInstRedistProtocolInstanceId_Type(Integer32):
    """Custom type sleISISInstRedistProtocolInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISInstRedistProtocolInstanceId_Type.__name__ = "Integer32"
_SleISISInstRedistProtocolInstanceId_Object = MibTableColumn
sleISISInstRedistProtocolInstanceId = _SleISISInstRedistProtocolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 1, 1, 1),
    _SleISISInstRedistProtocolInstanceId_Type()
)
sleISISInstRedistProtocolInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolInstanceId.setStatus("current")


class _SleISISInstRedistProtocolId_Type(Integer32):
    """Custom type sleISISInstRedistProtocolId based on Integer32"""
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
        *(("kernel", 1),
          ("connected", 2),
          ("static", 3),
          ("rip", 4),
          ("ospf", 5),
          ("bgp", 6))
    )


_SleISISInstRedistProtocolId_Type.__name__ = "Integer32"
_SleISISInstRedistProtocolId_Object = MibTableColumn
sleISISInstRedistProtocolId = _SleISISInstRedistProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 1, 1, 2),
    _SleISISInstRedistProtocolId_Type()
)
sleISISInstRedistProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolId.setStatus("current")


class _SleISISInstRedistProtocolMetric_Type(Gauge32):
    """Custom type sleISISInstRedistProtocolMetric based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4261412864),
    )


_SleISISInstRedistProtocolMetric_Type.__name__ = "Gauge32"
_SleISISInstRedistProtocolMetric_Object = MibTableColumn
sleISISInstRedistProtocolMetric = _SleISISInstRedistProtocolMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 1, 1, 3),
    _SleISISInstRedistProtocolMetric_Type()
)
sleISISInstRedistProtocolMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolMetric.setStatus("current")


class _SleISISInstRedistProtocolMetricType_Type(Integer32):
    """Custom type sleISISInstRedistProtocolMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("internal", 0),
          ("external", 1))
    )


_SleISISInstRedistProtocolMetricType_Type.__name__ = "Integer32"
_SleISISInstRedistProtocolMetricType_Object = MibTableColumn
sleISISInstRedistProtocolMetricType = _SleISISInstRedistProtocolMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 1, 1, 4),
    _SleISISInstRedistProtocolMetricType_Type()
)
sleISISInstRedistProtocolMetricType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolMetricType.setStatus("current")


class _SleISISInstRedistProtocolRouteLevelType_Type(Integer32):
    """Custom type sleISISInstRedistProtocolRouteLevelType based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level2", 2),
          ("level1To2", 3))
    )


_SleISISInstRedistProtocolRouteLevelType_Type.__name__ = "Integer32"
_SleISISInstRedistProtocolRouteLevelType_Object = MibTableColumn
sleISISInstRedistProtocolRouteLevelType = _SleISISInstRedistProtocolRouteLevelType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 1, 1, 5),
    _SleISISInstRedistProtocolRouteLevelType_Type()
)
sleISISInstRedistProtocolRouteLevelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolRouteLevelType.setStatus("current")
_SleISISInstRedistProtocolRouteMapName_Type = OctetString
_SleISISInstRedistProtocolRouteMapName_Object = MibTableColumn
sleISISInstRedistProtocolRouteMapName = _SleISISInstRedistProtocolRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 1, 1, 6),
    _SleISISInstRedistProtocolRouteMapName_Type()
)
sleISISInstRedistProtocolRouteMapName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolRouteMapName.setStatus("current")
_SleISISInstRedistProtocolControl_ObjectIdentity = ObjectIdentity
sleISISInstRedistProtocolControl = _SleISISInstRedistProtocolControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2)
)


class _SleISISInstRedistProtocolControlRequest_Type(Integer32):
    """Custom type sleISISInstRedistProtocolControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setISISInstIfRedistProtocol", 1),
          ("delISISInstIfRedistProtocol", 2))
    )


_SleISISInstRedistProtocolControlRequest_Type.__name__ = "Integer32"
_SleISISInstRedistProtocolControlRequest_Object = MibScalar
sleISISInstRedistProtocolControlRequest = _SleISISInstRedistProtocolControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 1),
    _SleISISInstRedistProtocolControlRequest_Type()
)
sleISISInstRedistProtocolControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlRequest.setStatus("current")
_SleISISInstRedistProtocolControlStatus_Type = SleControlStatusType
_SleISISInstRedistProtocolControlStatus_Object = MibScalar
sleISISInstRedistProtocolControlStatus = _SleISISInstRedistProtocolControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 2),
    _SleISISInstRedistProtocolControlStatus_Type()
)
sleISISInstRedistProtocolControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlStatus.setStatus("current")
_SleISISInstRedistProtocolControlTimer_Type = Gauge32
_SleISISInstRedistProtocolControlTimer_Object = MibScalar
sleISISInstRedistProtocolControlTimer = _SleISISInstRedistProtocolControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 3),
    _SleISISInstRedistProtocolControlTimer_Type()
)
sleISISInstRedistProtocolControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlTimer.setStatus("current")
_SleISISInstRedistProtocolControlTimeStamp_Type = TimeTicks
_SleISISInstRedistProtocolControlTimeStamp_Object = MibScalar
sleISISInstRedistProtocolControlTimeStamp = _SleISISInstRedistProtocolControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 4),
    _SleISISInstRedistProtocolControlTimeStamp_Type()
)
sleISISInstRedistProtocolControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlTimeStamp.setStatus("current")
_SleISISInstRedistProtocolControlReqResult_Type = SleControlRequestResultType
_SleISISInstRedistProtocolControlReqResult_Object = MibScalar
sleISISInstRedistProtocolControlReqResult = _SleISISInstRedistProtocolControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 5),
    _SleISISInstRedistProtocolControlReqResult_Type()
)
sleISISInstRedistProtocolControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlReqResult.setStatus("current")
_SleISISInstRedistProtocolControlInstanceId_Type = Integer32
_SleISISInstRedistProtocolControlInstanceId_Object = MibScalar
sleISISInstRedistProtocolControlInstanceId = _SleISISInstRedistProtocolControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 6),
    _SleISISInstRedistProtocolControlInstanceId_Type()
)
sleISISInstRedistProtocolControlInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlInstanceId.setStatus("current")


class _SleISISInstRedistProtocolControlId_Type(Integer32):
    """Custom type sleISISInstRedistProtocolControlId based on Integer32"""
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
        *(("kernel", 1),
          ("connected", 2),
          ("static", 3),
          ("rip", 4),
          ("ospf", 5),
          ("bgp", 6))
    )


_SleISISInstRedistProtocolControlId_Type.__name__ = "Integer32"
_SleISISInstRedistProtocolControlId_Object = MibScalar
sleISISInstRedistProtocolControlId = _SleISISInstRedistProtocolControlId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 7),
    _SleISISInstRedistProtocolControlId_Type()
)
sleISISInstRedistProtocolControlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlId.setStatus("current")


class _SleISISInstRedistProtocolControlMetric_Type(Gauge32):
    """Custom type sleISISInstRedistProtocolControlMetric based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4261412864),
    )


_SleISISInstRedistProtocolControlMetric_Type.__name__ = "Gauge32"
_SleISISInstRedistProtocolControlMetric_Object = MibScalar
sleISISInstRedistProtocolControlMetric = _SleISISInstRedistProtocolControlMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 8),
    _SleISISInstRedistProtocolControlMetric_Type()
)
sleISISInstRedistProtocolControlMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlMetric.setStatus("current")


class _SleISISInstRedistProtocolControlMetricType_Type(Integer32):
    """Custom type sleISISInstRedistProtocolControlMetricType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", -1),
          ("internal", 0),
          ("external", 1))
    )


_SleISISInstRedistProtocolControlMetricType_Type.__name__ = "Integer32"
_SleISISInstRedistProtocolControlMetricType_Object = MibScalar
sleISISInstRedistProtocolControlMetricType = _SleISISInstRedistProtocolControlMetricType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 9),
    _SleISISInstRedistProtocolControlMetricType_Type()
)
sleISISInstRedistProtocolControlMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlMetricType.setStatus("current")


class _SleISISInstRedistProtocolControlRouteLevelType_Type(Integer32):
    """Custom type sleISISInstRedistProtocolControlRouteLevelType based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level2", 2),
          ("level1To2", 3))
    )


_SleISISInstRedistProtocolControlRouteLevelType_Type.__name__ = "Integer32"
_SleISISInstRedistProtocolControlRouteLevelType_Object = MibScalar
sleISISInstRedistProtocolControlRouteLevelType = _SleISISInstRedistProtocolControlRouteLevelType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 10),
    _SleISISInstRedistProtocolControlRouteLevelType_Type()
)
sleISISInstRedistProtocolControlRouteLevelType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlRouteLevelType.setStatus("current")
_SleISISInstRedistProtocolControlRouteMapName_Type = OctetString
_SleISISInstRedistProtocolControlRouteMapName_Object = MibScalar
sleISISInstRedistProtocolControlRouteMapName = _SleISISInstRedistProtocolControlRouteMapName_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 1, 2, 11),
    _SleISISInstRedistProtocolControlRouteMapName_Type()
)
sleISISInstRedistProtocolControlRouteMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistProtocolControlRouteMapName.setStatus("current")
_SleISISInstRedistIsisProtocol_ObjectIdentity = ObjectIdentity
sleISISInstRedistIsisProtocol = _SleISISInstRedistIsisProtocol_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2)
)
_SleISISInstRedistIsisProtocolTable_Object = MibTable
sleISISInstRedistIsisProtocolTable = _SleISISInstRedistIsisProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 1)
)
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolTable.setStatus("current")
_SleISISInstRedistIsisProtocolEntry_Object = MibTableRow
sleISISInstRedistIsisProtocolEntry = _SleISISInstRedistIsisProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 1, 1)
)
sleISISInstRedistIsisProtocolEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolInstanceId"),
)
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolEntry.setStatus("current")


class _SleISISInstRedistIsisProtocolInstanceId_Type(Integer32):
    """Custom type sleISISInstRedistIsisProtocolInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISInstRedistIsisProtocolInstanceId_Type.__name__ = "Integer32"
_SleISISInstRedistIsisProtocolInstanceId_Object = MibTableColumn
sleISISInstRedistIsisProtocolInstanceId = _SleISISInstRedistIsisProtocolInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 1, 1, 1),
    _SleISISInstRedistIsisProtocolInstanceId_Type()
)
sleISISInstRedistIsisProtocolInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolInstanceId.setStatus("current")


class _SleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2_Type(Integer32):
    """Custom type sleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1))
    )


_SleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2_Type.__name__ = "Integer32"
_SleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2_Object = MibTableColumn
sleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2 = _SleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 1, 1, 2),
    _SleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2_Type()
)
sleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2.setStatus("current")
_SleISISInstRedistIsisProtocolLv1Lv2DistributeList_Type = OctetString
_SleISISInstRedistIsisProtocolLv1Lv2DistributeList_Object = MibTableColumn
sleISISInstRedistIsisProtocolLv1Lv2DistributeList = _SleISISInstRedistIsisProtocolLv1Lv2DistributeList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 1, 1, 3),
    _SleISISInstRedistIsisProtocolLv1Lv2DistributeList_Type()
)
sleISISInstRedistIsisProtocolLv1Lv2DistributeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolLv1Lv2DistributeList.setStatus("current")


class _SleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1_Type(Integer32):
    """Custom type sleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("enable", 1))
    )


_SleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1_Type.__name__ = "Integer32"
_SleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1_Object = MibTableColumn
sleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1 = _SleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 1, 1, 4),
    _SleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1_Type()
)
sleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1.setStatus("current")
_SleISISInstRedistIsisProtocolLv2Lv1DistributeList_Type = OctetString
_SleISISInstRedistIsisProtocolLv2Lv1DistributeList_Object = MibTableColumn
sleISISInstRedistIsisProtocolLv2Lv1DistributeList = _SleISISInstRedistIsisProtocolLv2Lv1DistributeList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 1, 1, 5),
    _SleISISInstRedistIsisProtocolLv2Lv1DistributeList_Type()
)
sleISISInstRedistIsisProtocolLv2Lv1DistributeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolLv2Lv1DistributeList.setStatus("current")
_SleISISInstRedistIsisProtocolControl_ObjectIdentity = ObjectIdentity
sleISISInstRedistIsisProtocolControl = _SleISISInstRedistIsisProtocolControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 2)
)


class _SleISISInstRedistIsisProtocolControlRequest_Type(Integer32):
    """Custom type sleISISInstRedistIsisProtocolControlRequest based on Integer32"""
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
        *(("setISISInstRedistIsisLv1Lv2", 1),
          ("delISISInstRedistIsisLv1Lv2", 2),
          ("setISISInstRedistIsisLv2Lv1", 3),
          ("delISISInstRedistIsisLv2Lv1", 4))
    )


_SleISISInstRedistIsisProtocolControlRequest_Type.__name__ = "Integer32"
_SleISISInstRedistIsisProtocolControlRequest_Object = MibScalar
sleISISInstRedistIsisProtocolControlRequest = _SleISISInstRedistIsisProtocolControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 2, 1),
    _SleISISInstRedistIsisProtocolControlRequest_Type()
)
sleISISInstRedistIsisProtocolControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolControlRequest.setStatus("current")
_SleISISInstRedistIsisProtocolControlStatus_Type = SleControlStatusType
_SleISISInstRedistIsisProtocolControlStatus_Object = MibScalar
sleISISInstRedistIsisProtocolControlStatus = _SleISISInstRedistIsisProtocolControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 2, 2),
    _SleISISInstRedistIsisProtocolControlStatus_Type()
)
sleISISInstRedistIsisProtocolControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolControlStatus.setStatus("current")
_SleISISInstRedistIsisProtocolControlTimer_Type = Gauge32
_SleISISInstRedistIsisProtocolControlTimer_Object = MibScalar
sleISISInstRedistIsisProtocolControlTimer = _SleISISInstRedistIsisProtocolControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 2, 3),
    _SleISISInstRedistIsisProtocolControlTimer_Type()
)
sleISISInstRedistIsisProtocolControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolControlTimer.setStatus("current")
_SleISISInstRedistIsisProtocolControlTimeStamp_Type = TimeTicks
_SleISISInstRedistIsisProtocolControlTimeStamp_Object = MibScalar
sleISISInstRedistIsisProtocolControlTimeStamp = _SleISISInstRedistIsisProtocolControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 2, 4),
    _SleISISInstRedistIsisProtocolControlTimeStamp_Type()
)
sleISISInstRedistIsisProtocolControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolControlTimeStamp.setStatus("current")
_SleISISInstRedistIsisProtocolControlReqResult_Type = SleControlRequestResultType
_SleISISInstRedistIsisProtocolControlReqResult_Object = MibScalar
sleISISInstRedistIsisProtocolControlReqResult = _SleISISInstRedistIsisProtocolControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 2, 5),
    _SleISISInstRedistIsisProtocolControlReqResult_Type()
)
sleISISInstRedistIsisProtocolControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolControlReqResult.setStatus("current")
_SleISISInstRedistIsisProtocolControlInstanceId_Type = Integer32
_SleISISInstRedistIsisProtocolControlInstanceId_Object = MibScalar
sleISISInstRedistIsisProtocolControlInstanceId = _SleISISInstRedistIsisProtocolControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 2, 6),
    _SleISISInstRedistIsisProtocolControlInstanceId_Type()
)
sleISISInstRedistIsisProtocolControlInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolControlInstanceId.setStatus("current")
_SleISISInstRedistIsisProtocolControlLv1Lv2DistributeList_Type = OctetString
_SleISISInstRedistIsisProtocolControlLv1Lv2DistributeList_Object = MibScalar
sleISISInstRedistIsisProtocolControlLv1Lv2DistributeList = _SleISISInstRedistIsisProtocolControlLv1Lv2DistributeList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 2, 7),
    _SleISISInstRedistIsisProtocolControlLv1Lv2DistributeList_Type()
)
sleISISInstRedistIsisProtocolControlLv1Lv2DistributeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolControlLv1Lv2DistributeList.setStatus("current")
_SleISISInstRedistIsisProtocolControlLv2Lv1DistributeList_Type = OctetString
_SleISISInstRedistIsisProtocolControlLv2Lv1DistributeList_Object = MibScalar
sleISISInstRedistIsisProtocolControlLv2Lv1DistributeList = _SleISISInstRedistIsisProtocolControlLv2Lv1DistributeList_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 5, 2, 2, 8),
    _SleISISInstRedistIsisProtocolControlLv2Lv1DistributeList_Type()
)
sleISISInstRedistIsisProtocolControlLv2Lv1DistributeList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISInstRedistIsisProtocolControlLv2Lv1DistributeList.setStatus("current")
_SleISISSummanryAddress_ObjectIdentity = ObjectIdentity
sleISISSummanryAddress = _SleISISSummanryAddress_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6)
)
_SleISISSummanryAddressTable_Object = MibTable
sleISISSummanryAddressTable = _SleISISSummanryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 1)
)
if mibBuilder.loadTexts:
    sleISISSummanryAddressTable.setStatus("current")
_SleISISSummanryAddressEntry_Object = MibTableRow
sleISISSummanryAddressEntry = _SleISISSummanryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 1, 1)
)
sleISISSummanryAddressEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISSummanryAddressInstanceId"),
    (0, "SLE-ISIS-MIB", "sleISISSummanryAddressIpValue"),
    (0, "SLE-ISIS-MIB", "sleISISSummanryAddressIpNetmask"),
)
if mibBuilder.loadTexts:
    sleISISSummanryAddressEntry.setStatus("current")


class _SleISISSummanryAddressInstanceId_Type(Integer32):
    """Custom type sleISISSummanryAddressInstanceId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SleISISSummanryAddressInstanceId_Type.__name__ = "Integer32"
_SleISISSummanryAddressInstanceId_Object = MibTableColumn
sleISISSummanryAddressInstanceId = _SleISISSummanryAddressInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 1, 1, 1),
    _SleISISSummanryAddressInstanceId_Type()
)
sleISISSummanryAddressInstanceId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISSummanryAddressInstanceId.setStatus("current")
_SleISISSummanryAddressIpValue_Type = IpAddress
_SleISISSummanryAddressIpValue_Object = MibTableColumn
sleISISSummanryAddressIpValue = _SleISISSummanryAddressIpValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 1, 1, 2),
    _SleISISSummanryAddressIpValue_Type()
)
sleISISSummanryAddressIpValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISSummanryAddressIpValue.setStatus("current")


class _SleISISSummanryAddressIpNetmask_Type(Integer32):
    """Custom type sleISISSummanryAddressIpNetmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleISISSummanryAddressIpNetmask_Type.__name__ = "Integer32"
_SleISISSummanryAddressIpNetmask_Object = MibTableColumn
sleISISSummanryAddressIpNetmask = _SleISISSummanryAddressIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 1, 1, 3),
    _SleISISSummanryAddressIpNetmask_Type()
)
sleISISSummanryAddressIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISSummanryAddressIpNetmask.setStatus("current")


class _SleISISSummanryAddressLevel_Type(Integer32):
    """Custom type sleISISSummanryAddressLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level2", 2),
          ("level1To2", 3))
    )


_SleISISSummanryAddressLevel_Type.__name__ = "Integer32"
_SleISISSummanryAddressLevel_Object = MibTableColumn
sleISISSummanryAddressLevel = _SleISISSummanryAddressLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 1, 1, 4),
    _SleISISSummanryAddressLevel_Type()
)
sleISISSummanryAddressLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISSummanryAddressLevel.setStatus("current")


class _SleISISSummanryAddressMetric_Type(Integer32):
    """Custom type sleISISSummanryAddressMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SleISISSummanryAddressMetric_Type.__name__ = "Integer32"
_SleISISSummanryAddressMetric_Object = MibTableColumn
sleISISSummanryAddressMetric = _SleISISSummanryAddressMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 1, 1, 5),
    _SleISISSummanryAddressMetric_Type()
)
sleISISSummanryAddressMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISSummanryAddressMetric.setStatus("current")
_SleISISSummanryAddressControl_ObjectIdentity = ObjectIdentity
sleISISSummanryAddressControl = _SleISISSummanryAddressControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2)
)


class _SleISISSummanryAddressControlRequest_Type(Integer32):
    """Custom type sleISISSummanryAddressControlRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("setISISSummaryAddress", 1),
          ("delISISSummaryAddress", 2))
    )


_SleISISSummanryAddressControlRequest_Type.__name__ = "Integer32"
_SleISISSummanryAddressControlRequest_Object = MibScalar
sleISISSummanryAddressControlRequest = _SleISISSummanryAddressControlRequest_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 1),
    _SleISISSummanryAddressControlRequest_Type()
)
sleISISSummanryAddressControlRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlRequest.setStatus("current")
_SleISISSummanryAddressControlStatus_Type = SleControlStatusType
_SleISISSummanryAddressControlStatus_Object = MibScalar
sleISISSummanryAddressControlStatus = _SleISISSummanryAddressControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 2),
    _SleISISSummanryAddressControlStatus_Type()
)
sleISISSummanryAddressControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlStatus.setStatus("current")
_SleISISSummanryAddressControlTimer_Type = Gauge32
_SleISISSummanryAddressControlTimer_Object = MibScalar
sleISISSummanryAddressControlTimer = _SleISISSummanryAddressControlTimer_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 3),
    _SleISISSummanryAddressControlTimer_Type()
)
sleISISSummanryAddressControlTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlTimer.setStatus("current")
_SleISISSummanryAddressControlTimeStamp_Type = TimeTicks
_SleISISSummanryAddressControlTimeStamp_Object = MibScalar
sleISISSummanryAddressControlTimeStamp = _SleISISSummanryAddressControlTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 4),
    _SleISISSummanryAddressControlTimeStamp_Type()
)
sleISISSummanryAddressControlTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlTimeStamp.setStatus("current")
_SleISISSummanryAddressControlReqResult_Type = SleControlRequestResultType
_SleISISSummanryAddressControlReqResult_Object = MibScalar
sleISISSummanryAddressControlReqResult = _SleISISSummanryAddressControlReqResult_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 5),
    _SleISISSummanryAddressControlReqResult_Type()
)
sleISISSummanryAddressControlReqResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlReqResult.setStatus("current")
_SleISISSummanryAddressControlInstanceId_Type = Integer32
_SleISISSummanryAddressControlInstanceId_Object = MibScalar
sleISISSummanryAddressControlInstanceId = _SleISISSummanryAddressControlInstanceId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 6),
    _SleISISSummanryAddressControlInstanceId_Type()
)
sleISISSummanryAddressControlInstanceId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlInstanceId.setStatus("current")
_SleISISSummanryAddressControlIpValue_Type = IpAddress
_SleISISSummanryAddressControlIpValue_Object = MibScalar
sleISISSummanryAddressControlIpValue = _SleISISSummanryAddressControlIpValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 7),
    _SleISISSummanryAddressControlIpValue_Type()
)
sleISISSummanryAddressControlIpValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlIpValue.setStatus("current")


class _SleISISSummanryAddressControlIpNetmask_Type(Integer32):
    """Custom type sleISISSummanryAddressControlIpNetmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_SleISISSummanryAddressControlIpNetmask_Type.__name__ = "Integer32"
_SleISISSummanryAddressControlIpNetmask_Object = MibScalar
sleISISSummanryAddressControlIpNetmask = _SleISISSummanryAddressControlIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 8),
    _SleISISSummanryAddressControlIpNetmask_Type()
)
sleISISSummanryAddressControlIpNetmask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlIpNetmask.setStatus("current")


class _SleISISSummanryAddressControlLevel_Type(Integer32):
    """Custom type sleISISSummanryAddressControlLevel based on Integer32"""
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
        *(("none", 0),
          ("level1", 1),
          ("level2", 2),
          ("level1To2", 3))
    )


_SleISISSummanryAddressControlLevel_Type.__name__ = "Integer32"
_SleISISSummanryAddressControlLevel_Object = MibScalar
sleISISSummanryAddressControlLevel = _SleISISSummanryAddressControlLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 9),
    _SleISISSummanryAddressControlLevel_Type()
)
sleISISSummanryAddressControlLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlLevel.setStatus("current")


class _SleISISSummanryAddressControlMetric_Type(Integer32):
    """Custom type sleISISSummanryAddressControlMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_SleISISSummanryAddressControlMetric_Type.__name__ = "Integer32"
_SleISISSummanryAddressControlMetric_Object = MibScalar
sleISISSummanryAddressControlMetric = _SleISISSummanryAddressControlMetric_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 6, 2, 10),
    _SleISISSummanryAddressControlMetric_Type()
)
sleISISSummanryAddressControlMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sleISISSummanryAddressControlMetric.setStatus("current")
_SleISISDatabase_ObjectIdentity = ObjectIdentity
sleISISDatabase = _SleISISDatabase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7)
)
_SleISISDatabaseTable_Object = MibTable
sleISISDatabaseTable = _SleISISDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1)
)
if mibBuilder.loadTexts:
    sleISISDatabaseTable.setStatus("current")
_SleISISDatabaseEntry_Object = MibTableRow
sleISISDatabaseEntry = _SleISISDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1)
)
sleISISDatabaseEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISDatabaseTag"),
    (0, "SLE-ISIS-MIB", "sleISISDatabaseLevel"),
    (0, "SLE-ISIS-MIB", "sleISISDatabaseLspId"),
)
if mibBuilder.loadTexts:
    sleISISDatabaseEntry.setStatus("current")
_SleISISDatabaseTag_Type = OctetString
_SleISISDatabaseTag_Object = MibTableColumn
sleISISDatabaseTag = _SleISISDatabaseTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1, 1),
    _SleISISDatabaseTag_Type()
)
sleISISDatabaseTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseTag.setStatus("current")


class _SleISISDatabaseLevel_Type(Integer32):
    """Custom type sleISISDatabaseLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SleISISDatabaseLevel_Type.__name__ = "Integer32"
_SleISISDatabaseLevel_Object = MibTableColumn
sleISISDatabaseLevel = _SleISISDatabaseLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1, 2),
    _SleISISDatabaseLevel_Type()
)
sleISISDatabaseLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseLevel.setStatus("current")
_SleISISDatabaseLspId_Type = OctetString
_SleISISDatabaseLspId_Object = MibTableColumn
sleISISDatabaseLspId = _SleISISDatabaseLspId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1, 3),
    _SleISISDatabaseLspId_Type()
)
sleISISDatabaseLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseLspId.setStatus("current")
_SleISISDatabaseLspSeqNum_Type = OctetString
_SleISISDatabaseLspSeqNum_Object = MibTableColumn
sleISISDatabaseLspSeqNum = _SleISISDatabaseLspSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1, 4),
    _SleISISDatabaseLspSeqNum_Type()
)
sleISISDatabaseLspSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseLspSeqNum.setStatus("current")
_SleISISDatabaseLspChecksum_Type = OctetString
_SleISISDatabaseLspChecksum_Object = MibTableColumn
sleISISDatabaseLspChecksum = _SleISISDatabaseLspChecksum_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1, 5),
    _SleISISDatabaseLspChecksum_Type()
)
sleISISDatabaseLspChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseLspChecksum.setStatus("current")
_SleISISDatabaseLspHoldtime_Type = OctetString
_SleISISDatabaseLspHoldtime_Object = MibTableColumn
sleISISDatabaseLspHoldtime = _SleISISDatabaseLspHoldtime_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1, 6),
    _SleISISDatabaseLspHoldtime_Type()
)
sleISISDatabaseLspHoldtime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseLspHoldtime.setStatus("current")
_SleISISDatabaseAtt_Type = Integer32
_SleISISDatabaseAtt_Object = MibTableColumn
sleISISDatabaseAtt = _SleISISDatabaseAtt_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1, 7),
    _SleISISDatabaseAtt_Type()
)
sleISISDatabaseAtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseAtt.setStatus("current")
_SleISISDatabaseP_Type = Integer32
_SleISISDatabaseP_Object = MibTableColumn
sleISISDatabaseP = _SleISISDatabaseP_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1, 8),
    _SleISISDatabaseP_Type()
)
sleISISDatabaseP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseP.setStatus("current")
_SleISISDatabaseOl_Type = Integer32
_SleISISDatabaseOl_Object = MibTableColumn
sleISISDatabaseOl = _SleISISDatabaseOl_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 7, 1, 1, 9),
    _SleISISDatabaseOl_Type()
)
sleISISDatabaseOl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseOl.setStatus("current")
_SleISISDatabaseDetail_ObjectIdentity = ObjectIdentity
sleISISDatabaseDetail = _SleISISDatabaseDetail_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8)
)
_SleISISDatabaseDetailTable_Object = MibTable
sleISISDatabaseDetailTable = _SleISISDatabaseDetailTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1)
)
if mibBuilder.loadTexts:
    sleISISDatabaseDetailTable.setStatus("current")
_SleISISDatabaseDetailEntry_Object = MibTableRow
sleISISDatabaseDetailEntry = _SleISISDatabaseDetailEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1, 1)
)
sleISISDatabaseDetailEntry.setIndexNames(
    (0, "SLE-ISIS-MIB", "sleISISDatabaseDetailTag"),
    (0, "SLE-ISIS-MIB", "sleISISDatabaseDetailLevel"),
    (0, "SLE-ISIS-MIB", "sleISISDatabaseDetailLspId"),
    (0, "SLE-ISIS-MIB", "sleISISDatabaseDetailType"),
    (0, "SLE-ISIS-MIB", "sleISISDatabaseDetailIndex"),
)
if mibBuilder.loadTexts:
    sleISISDatabaseDetailEntry.setStatus("current")
_SleISISDatabaseDetailTag_Type = OctetString
_SleISISDatabaseDetailTag_Object = MibTableColumn
sleISISDatabaseDetailTag = _SleISISDatabaseDetailTag_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1, 1, 1),
    _SleISISDatabaseDetailTag_Type()
)
sleISISDatabaseDetailTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseDetailTag.setStatus("current")


class _SleISISDatabaseDetailLevel_Type(Integer32):
    """Custom type sleISISDatabaseDetailLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 0),
          ("level1", 1),
          ("level2", 2))
    )


_SleISISDatabaseDetailLevel_Type.__name__ = "Integer32"
_SleISISDatabaseDetailLevel_Object = MibTableColumn
sleISISDatabaseDetailLevel = _SleISISDatabaseDetailLevel_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1, 1, 2),
    _SleISISDatabaseDetailLevel_Type()
)
sleISISDatabaseDetailLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseDetailLevel.setStatus("current")
_SleISISDatabaseDetailLspId_Type = OctetString
_SleISISDatabaseDetailLspId_Object = MibTableColumn
sleISISDatabaseDetailLspId = _SleISISDatabaseDetailLspId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1, 1, 3),
    _SleISISDatabaseDetailLspId_Type()
)
sleISISDatabaseDetailLspId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseDetailLspId.setStatus("current")


class _SleISISDatabaseDetailType_Type(Integer32):
    """Custom type sleISISDatabaseDetailType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              10,
              22,
              128,
              129,
              130,
              132,
              133,
              134,
              135,
              137,
              138,
              222,
              229,
              232,
              235,
              236,
              237)
        )
    )
    namedValues = NamedValues(
        *(("areaAddr", 1),
          ("lspIsNeighbor", 2),
          ("lspEsNeighbor", 3),
          ("authInfo", 10),
          ("extendedIsReachability", 22),
          ("ipInternalReachability", 128),
          ("protocolsSupportded", 129),
          ("ipExternalReachability", 130),
          ("ipIfAddr", 132),
          ("ipAuthInfo", 133),
          ("teRouteId", 134),
          ("extendedIpReachability", 135),
          ("hostname", 137),
          ("sharedRiskLinkGroup", 138),
          ("multiIsReachability", 222),
          ("multiTopology", 229),
          ("ipv6IfAddr", 232),
          ("multiIpv4Reachability", 235),
          ("ipv6Reachability", 236),
          ("multiIpv6Reachability", 237))
    )


_SleISISDatabaseDetailType_Type.__name__ = "Integer32"
_SleISISDatabaseDetailType_Object = MibTableColumn
sleISISDatabaseDetailType = _SleISISDatabaseDetailType_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1, 1, 4),
    _SleISISDatabaseDetailType_Type()
)
sleISISDatabaseDetailType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseDetailType.setStatus("current")


class _SleISISDatabaseDetailIndex_Type(Integer32):
    """Custom type sleISISDatabaseDetailIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_SleISISDatabaseDetailIndex_Type.__name__ = "Integer32"
_SleISISDatabaseDetailIndex_Object = MibTableColumn
sleISISDatabaseDetailIndex = _SleISISDatabaseDetailIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1, 1, 5),
    _SleISISDatabaseDetailIndex_Type()
)
sleISISDatabaseDetailIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseDetailIndex.setStatus("current")
_SleISISDatabaseDetailPad_Type = OctetString
_SleISISDatabaseDetailPad_Object = MibTableColumn
sleISISDatabaseDetailPad = _SleISISDatabaseDetailPad_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1, 1, 6),
    _SleISISDatabaseDetailPad_Type()
)
sleISISDatabaseDetailPad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseDetailPad.setStatus("current")
_SleISISDatabaseDetailValue_Type = Integer32
_SleISISDatabaseDetailValue_Object = MibTableColumn
sleISISDatabaseDetailValue = _SleISISDatabaseDetailValue_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1, 1, 7),
    _SleISISDatabaseDetailValue_Type()
)
sleISISDatabaseDetailValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseDetailValue.setStatus("current")
_SleISISDatabaseDetailDescription_Type = OctetString
_SleISISDatabaseDetailDescription_Object = MibTableColumn
sleISISDatabaseDetailDescription = _SleISISDatabaseDetailDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 8, 1, 1, 8),
    _SleISISDatabaseDetailDescription_Type()
)
sleISISDatabaseDetailDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleISISDatabaseDetailDescription.setStatus("current")

# Managed Objects groups

sleISISGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 101, 56, 9)
)
sleISISGroup.setObjects(
      *(("SLE-ISIS-MIB", "sleISISRestartSuppressAdjacency"),
        ("SLE-ISIS-MIB", "sleISISRestartHelper"),
        ("SLE-ISIS-MIB", "sleISISRestartGracePeriod"),
        ("SLE-ISIS-MIB", "sleISISControlRequest"),
        ("SLE-ISIS-MIB", "sleISISControlStatus"),
        ("SLE-ISIS-MIB", "sleISISControlTimer"),
        ("SLE-ISIS-MIB", "sleISISControlTimeStamp"),
        ("SLE-ISIS-MIB", "sleISISControlReqResult"),
        ("SLE-ISIS-MIB", "sleISISControlRestartSuppressAdjacency"),
        ("SLE-ISIS-MIB", "sleISISControlRestartHelper"),
        ("SLE-ISIS-MIB", "sleISISControlRestartPeriod"),
        ("SLE-ISIS-MIB", "sleISISControlClearSystemId"),
        ("SLE-ISIS-MIB", "sleISISControlClearIfName"),
        ("SLE-ISIS-MIB", "sleISISControlClearRouteTag"),
        ("SLE-ISIS-MIB", "sleISISControlClearRouteMode"),
        ("SLE-ISIS-MIB", "sleISISProcInfoInstanceID"),
        ("SLE-ISIS-MIB", "sleISISProcInfoTag"),
        ("SLE-ISIS-MIB", "sleISISProcBfdAllInterface"),
        ("SLE-ISIS-MIB", "sleISISProcCapCspf"),
        ("SLE-ISIS-MIB", "sleISISProcDynHostname"),
        ("SLE-ISIS-MIB", "sleISISProcDynHostnameAreaTag"),
        ("SLE-ISIS-MIB", "sleISISProcIgnLspErr"),
        ("SLE-ISIS-MIB", "sleISISProcRouteHighPriorityTag"),
        ("SLE-ISIS-MIB", "sleISISProcIspfLevel"),
        ("SLE-ISIS-MIB", "sleISISProcIsTypeLevel"),
        ("SLE-ISIS-MIB", "sleISISProcLspGenInterval"),
        ("SLE-ISIS-MIB", "sleISISProcLspGenIntervalLevel"),
        ("SLE-ISIS-MIB", "sleISISProcLspMtu"),
        ("SLE-ISIS-MIB", "sleISISProcLspMtuLevel"),
        ("SLE-ISIS-MIB", "sleISISProcLspRefreshInterval"),
        ("SLE-ISIS-MIB", "sleISISProcMaxAreaAddressNum"),
        ("SLE-ISIS-MIB", "sleISISProcMaxLspLifetime"),
        ("SLE-ISIS-MIB", "sleISISProcMetricStyle"),
        ("SLE-ISIS-MIB", "sleISISProcMetricStyleLevel"),
        ("SLE-ISIS-MIB", "sleISISProcMplsTrafficEngLevel"),
        ("SLE-ISIS-MIB", "sleISISProcMplsTrafficEngRouterID"),
        ("SLE-ISIS-MIB", "sleISISProcPrcIntervalExpMinDelay"),
        ("SLE-ISIS-MIB", "sleISISProcPrcIntervalExpMaxDelay"),
        ("SLE-ISIS-MIB", "sleISISProcProtocolTopolgy"),
        ("SLE-ISIS-MIB", "sleISISProcRestartTimerVal"),
        ("SLE-ISIS-MIB", "sleISISProcRestartTimerLevel"),
        ("SLE-ISIS-MIB", "sleISISProcSpfIntervalExpMin"),
        ("SLE-ISIS-MIB", "sleISISProcSpfIntervalExpMax"),
        ("SLE-ISIS-MIB", "sleISISProcSpfIntervalExpLevel"),
        ("SLE-ISIS-MIB", "sleISISProcAuthMode"),
        ("SLE-ISIS-MIB", "sleISISProcAuthModeLevel"),
        ("SLE-ISIS-MIB", "sleISISProcAuthSendOnly"),
        ("SLE-ISIS-MIB", "sleISISProcAuthSendOnlyLevel"),
        ("SLE-ISIS-MIB", "sleISISProcDomPassVal"),
        ("SLE-ISIS-MIB", "sleISISProcDomPassAuthSnp"),
        ("SLE-ISIS-MIB", "sleISISProcAreaPassVal"),
        ("SLE-ISIS-MIB", "sleISISProcAreaPassAuthSnp"),
        ("SLE-ISIS-MIB", "sleISISProcSetOverloadBit"),
        ("SLE-ISIS-MIB", "sleISISProcSetOverloadBitOnStartup"),
        ("SLE-ISIS-MIB", "sleISISProcSetOverloadBitOnStartupInterval"),
        ("SLE-ISIS-MIB", "sleISISProcSetOverloadBitSuppress"),
        ("SLE-ISIS-MIB", "sleISISProcWaitTimerVal"),
        ("SLE-ISIS-MIB", "sleISISProcWaitTimerLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlRequest"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlStatus"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlTimer"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlTimeStamp"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlReqResult"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlTag"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlBfdAllInterface"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlCapCspf"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlDynHostname"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlDynHostnameAreaTag"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlIgnLspErr"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlRouteHighPriorityTag"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlIspfLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlIsTypeLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlLspGenInterval"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlLspGenIntervalLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlLspMtu"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlLspMtuLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlLspRefreshInterval"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlMaxAreaAddressNum"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlMaxLspLifetime"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlMetricStyle"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlMetricStyleLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlMplsTrafficEngLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlMplsTrafficEngRouterID"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlPrcIntervalExpMinDelay"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlPrcIntervalExpMaxDelay"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlProtocolTopolgy"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlRestartTimerVal"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlRestartTimerLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlSpfIntervalExpMin"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlSpfIntervalExpMax"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlSpfIntervalExpLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlAuthMode"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlAuthModeLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlAuthSendOnly"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlAuthSendOnlyLevel"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlDomPassVal"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlDomPassAuthSnp"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlAreaPassVal"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlAreaPassAuthSnp"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlSetOverloadBit"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlSetOverloadBitOnStartup"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlSetOverloadBitOnStartupInterval"),
        ("SLE-ISIS-MIB", "sleISISProcInfoControlSetOverloadBitSuppress"),
        ("SLE-ISIS-MIB", "sleISISProcControlWaitTimerVal"),
        ("SLE-ISIS-MIB", "sleISISProcControlWaitTimerLevel"),
        ("SLE-ISIS-MIB", "sleISISProcNetInstanceID"),
        ("SLE-ISIS-MIB", "sleISISProcNetTitle"),
        ("SLE-ISIS-MIB", "sleISISProcNetControlRequest"),
        ("SLE-ISIS-MIB", "sleISISProcNetControlStatus"),
        ("SLE-ISIS-MIB", "sleISISProcNetControlTimer"),
        ("SLE-ISIS-MIB", "sleISISProcNetControlTimeStamp"),
        ("SLE-ISIS-MIB", "sleISISProcNetControlReqResult"),
        ("SLE-ISIS-MIB", "sleISISProcNetControlInstanceID"),
        ("SLE-ISIS-MIB", "sleISISProcNetControlTitle"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4InstanceID"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4Dist"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4SytemID"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4AccessList"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4ControlRequest"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4ControlStatus"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4ControlTimer"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4TimeStamp"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4ntrolReqResult"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4ControlInstanceID"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4ControlDist"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4ControlSytemID"),
        ("SLE-ISIS-MIB", "sleISISProcDistanceV4ControlAccessList"),
        ("SLE-ISIS-MIB", "sleISISIfIndex"),
        ("SLE-ISIS-MIB", "sleISISIfMplsLdpIgpSync"),
        ("SLE-ISIS-MIB", "sleISISIfIpRouter"),
        ("SLE-ISIS-MIB", "sleISISIfAuthSendLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfAuthSendLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfAuthModeMd5Levle1"),
        ("SLE-ISIS-MIB", "sleISISIfAuthModeMd5Levle2"),
        ("SLE-ISIS-MIB", "sleISISIfAuthModeTextLevle1"),
        ("SLE-ISIS-MIB", "sleISISIfAuthModeTextLevle2"),
        ("SLE-ISIS-MIB", "sleISISIfAuthKeyChainLevle1"),
        ("SLE-ISIS-MIB", "sleISISIfAuthKeyChainLevle2"),
        ("SLE-ISIS-MIB", "sleISISIfBfd"),
        ("SLE-ISIS-MIB", "sleISISIfBfdDisable"),
        ("SLE-ISIS-MIB", "sleISISIfCircuitType"),
        ("SLE-ISIS-MIB", "sleISISIfCsnpIntervalLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfCsnpIntervalLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfHelloPadding"),
        ("SLE-ISIS-MIB", "sleISISIfHelloIntervalLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfHelloIntervalLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfHelloIntervalMinimalLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfHelloIntervalMinimalLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfHelloMultiplierLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfHelloMultiplierLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfLspInterval"),
        ("SLE-ISIS-MIB", "sleISISIfMeshGroup"),
        ("SLE-ISIS-MIB", "sleISISIfMetricLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfMetricLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfNetwork"),
        ("SLE-ISIS-MIB", "sleISISIfPriorityLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfPriorityLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfRestartHelloIntervalLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfRestartHelloIntervalLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfRetransmitInterval"),
        ("SLE-ISIS-MIB", "sleISISIfWideMetricLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfWideMetricLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfControlRequest"),
        ("SLE-ISIS-MIB", "sleISISIfControlStatus"),
        ("SLE-ISIS-MIB", "sleISISIfControlTimer"),
        ("SLE-ISIS-MIB", "sleISISIfControlTimeStamp"),
        ("SLE-ISIS-MIB", "sleISISIfControlReqResult"),
        ("SLE-ISIS-MIB", "sleISISIfControlIndex"),
        ("SLE-ISIS-MIB", "sleISISIfControlMplsLdpIgpSync"),
        ("SLE-ISIS-MIB", "sleISISIfControlIpRouter"),
        ("SLE-ISIS-MIB", "sleISISIfControlAuthSendLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfControlAuthSendLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfControlAuthModeMd5Levle1"),
        ("SLE-ISIS-MIB", "sleISISIfControlAuthModeMd5Levle2"),
        ("SLE-ISIS-MIB", "sleISISIfControlAuthModeTextLevle1"),
        ("SLE-ISIS-MIB", "sleISISIfControlAuthModeTextLevle2"),
        ("SLE-ISIS-MIB", "sleISISIfControlAuthKeyChainLevle1"),
        ("SLE-ISIS-MIB", "sleISISIfControlAuthKeyChainLevle2"),
        ("SLE-ISIS-MIB", "sleISISIfControlBfd"),
        ("SLE-ISIS-MIB", "sleISISIfControlBfdDisable"),
        ("SLE-ISIS-MIB", "sleISISIfControlCircuitType"),
        ("SLE-ISIS-MIB", "sleISISIfControlCsnpIntervalLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfControlCsnpIntervalLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfControlHelloPadding"),
        ("SLE-ISIS-MIB", "sleISISIfControlHelloIntervalLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfControlHelloIntervalLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfControlHelloIntervalMinimalLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfControlHelloIntervalMinimalLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfControlHelloMultiplierLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfControlHelloMultiplierLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfControlLspInterval"),
        ("SLE-ISIS-MIB", "sleISISIfControlMeshGroup"),
        ("SLE-ISIS-MIB", "sleISISIfControlMetricLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfControlMetricLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfControlNetwork"),
        ("SLE-ISIS-MIB", "sleISISIfControlPriorityLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfControlPriorityLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfControlRestartHelloIntervalLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfControlRestartHelloIntervalLevel2"),
        ("SLE-ISIS-MIB", "sleISISIfControlRetransmitInterval"),
        ("SLE-ISIS-MIB", "sleISISIfControlWideMetricLevel1"),
        ("SLE-ISIS-MIB", "sleISISIfControlWideMetricLevel2"),
        ("SLE-ISIS-MIB", "sleISISInstIfInstanceId"),
        ("SLE-ISIS-MIB", "sleISISInstIfInterfaceId"),
        ("SLE-ISIS-MIB", "sleISISPassiveInterface"),
        ("SLE-ISIS-MIB", "sleISISInstIfControlRequest"),
        ("SLE-ISIS-MIB", "sleISISInstIfControlStatus"),
        ("SLE-ISIS-MIB", "sleISISInstIfControlTimer"),
        ("SLE-ISIS-MIB", "sleISISInstIfControlTimeStamp"),
        ("SLE-ISIS-MIB", "sleISISInstIfControlReqResult"),
        ("SLE-ISIS-MIB", "sleISISInstIfControlInstanceId"),
        ("SLE-ISIS-MIB", "sleISISInstIfControlInterfaceId"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolInstanceId"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolId"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolMetric"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolMetricType"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolRouteLevelType"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolRouteMapName"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlRequest"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlStatus"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlTimer"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlTimeStamp"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlReqResult"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlInstanceId"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlId"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlMetric"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlMetricType"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlRouteLevelType"),
        ("SLE-ISIS-MIB", "sleISISInstRedistProtocolControlRouteMapName"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolInstanceId"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolLv1Lv2DistributeList"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolLv2Lv1DistributeList"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolControlRequest"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolControlStatus"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolControlTimer"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolControlTimeStamp"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolControlReqResult"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolControlInstanceId"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolControlLv1Lv2DistributeList"),
        ("SLE-ISIS-MIB", "sleISISInstRedistIsisProtocolControlLv2Lv1DistributeList"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressInstanceId"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressIpValue"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressIpNetmask"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressLevel"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressMetric"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlRequest"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlStatus"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlTimer"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlTimeStamp"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlReqResult"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlInstanceId"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlIpValue"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlIpNetmask"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlLevel"),
        ("SLE-ISIS-MIB", "sleISISProcAuthenKeyChainL1"),
        ("SLE-ISIS-MIB", "sleISISProcAuthenKeyChainL2"),
        ("SLE-ISIS-MIB", "sleISISProcAuthenKeyChainL1L2"),
        ("SLE-ISIS-MIB", "sleISISProcControlAuthenkeyChain"),
        ("SLE-ISIS-MIB", "sleISISProcControlAuthenkeyChainLevel"),
        ("SLE-ISIS-MIB", "sleISISDatabaseTag"),
        ("SLE-ISIS-MIB", "sleISISDatabaseLevel"),
        ("SLE-ISIS-MIB", "sleISISDatabaseLspId"),
        ("SLE-ISIS-MIB", "sleISISDatabaseLspSeqNum"),
        ("SLE-ISIS-MIB", "sleISISDatabaseLspChecksum"),
        ("SLE-ISIS-MIB", "sleISISDatabaseLspHoldtime"),
        ("SLE-ISIS-MIB", "sleISISDatabaseAtt"),
        ("SLE-ISIS-MIB", "sleISISDatabaseP"),
        ("SLE-ISIS-MIB", "sleISISDatabaseOl"),
        ("SLE-ISIS-MIB", "sleISISDatabaseDetailTag"),
        ("SLE-ISIS-MIB", "sleISISDatabaseDetailLevel"),
        ("SLE-ISIS-MIB", "sleISISDatabaseDetailLspId"),
        ("SLE-ISIS-MIB", "sleISISDatabaseDetailType"),
        ("SLE-ISIS-MIB", "sleISISDatabaseDetailIndex"),
        ("SLE-ISIS-MIB", "sleISISDatabaseDetailPad"),
        ("SLE-ISIS-MIB", "sleISISDatabaseDetailValue"),
        ("SLE-ISIS-MIB", "sleISISDatabaseDetailDescription"),
        ("SLE-ISIS-MIB", "sleISISSummanryAddressControlMetric"),
        ("SLE-ISIS-MIB", "sleISISIfStatusIfIndex"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusIfStatus"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusIsisTag"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusNetworkType"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitType"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusLocalCircuitId"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusExtendedLocalCircuitId"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusLocalSnpa"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusLdpSyncHoldTimer"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusLdpSyncRemainingTime"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL1Metric"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL1WideMetric"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL1Priority"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL1CircuitId"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL1ActiveAdjacencies"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL1LscpMtu"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL2Metric"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL2WideMetric"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL2Priority"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL2CircuitId"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL2ActiveAdjacencies"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusCircuitL2LscpMtu"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusL1HelloTimerBroadcast"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusL2HelloTimerBroadcast"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusL1HellotimerPoint2Point"),
        ("SLE-ISIS-MIB", "sleIsisIfStatusL2HellotimerPoint2Point"))
)
if mibBuilder.loadTexts:
    sleISISGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-ISIS-MIB",
    **{"sleISIS": sleISIS,
       "sleISISBase": sleISISBase,
       "sleISISBaseInfo": sleISISBaseInfo,
       "sleISISRestartSuppressAdjacency": sleISISRestartSuppressAdjacency,
       "sleISISRestartHelper": sleISISRestartHelper,
       "sleISISRestartGracePeriod": sleISISRestartGracePeriod,
       "sleISISBaseControl": sleISISBaseControl,
       "sleISISControlRequest": sleISISControlRequest,
       "sleISISControlStatus": sleISISControlStatus,
       "sleISISControlTimer": sleISISControlTimer,
       "sleISISControlTimeStamp": sleISISControlTimeStamp,
       "sleISISControlReqResult": sleISISControlReqResult,
       "sleISISControlRestartSuppressAdjacency": sleISISControlRestartSuppressAdjacency,
       "sleISISControlRestartHelper": sleISISControlRestartHelper,
       "sleISISControlRestartPeriod": sleISISControlRestartPeriod,
       "sleISISControlClearSystemId": sleISISControlClearSystemId,
       "sleISISControlClearIfName": sleISISControlClearIfName,
       "sleISISControlClearRouteTag": sleISISControlClearRouteTag,
       "sleISISControlClearRouteMode": sleISISControlClearRouteMode,
       "sleISISBaseNotification": sleISISBaseNotification,
       "sleISISProc": sleISISProc,
       "sleISISProcInfo": sleISISProcInfo,
       "sleISISProcInfoTable": sleISISProcInfoTable,
       "sleISISProcInfoEntry": sleISISProcInfoEntry,
       "sleISISProcInfoInstanceID": sleISISProcInfoInstanceID,
       "sleISISProcInfoTag": sleISISProcInfoTag,
       "sleISISProcBfdAllInterface": sleISISProcBfdAllInterface,
       "sleISISProcCapCspf": sleISISProcCapCspf,
       "sleISISProcDynHostname": sleISISProcDynHostname,
       "sleISISProcDynHostnameAreaTag": sleISISProcDynHostnameAreaTag,
       "sleISISProcIgnLspErr": sleISISProcIgnLspErr,
       "sleISISProcRouteHighPriorityTag": sleISISProcRouteHighPriorityTag,
       "sleISISProcIspfLevel": sleISISProcIspfLevel,
       "sleISISProcIsTypeLevel": sleISISProcIsTypeLevel,
       "sleISISProcLspGenInterval": sleISISProcLspGenInterval,
       "sleISISProcLspGenIntervalLevel": sleISISProcLspGenIntervalLevel,
       "sleISISProcLspMtu": sleISISProcLspMtu,
       "sleISISProcLspMtuLevel": sleISISProcLspMtuLevel,
       "sleISISProcLspRefreshInterval": sleISISProcLspRefreshInterval,
       "sleISISProcMaxAreaAddressNum": sleISISProcMaxAreaAddressNum,
       "sleISISProcMaxLspLifetime": sleISISProcMaxLspLifetime,
       "sleISISProcMetricStyle": sleISISProcMetricStyle,
       "sleISISProcMetricStyleLevel": sleISISProcMetricStyleLevel,
       "sleISISProcMplsTrafficEngLevel": sleISISProcMplsTrafficEngLevel,
       "sleISISProcMplsTrafficEngRouterID": sleISISProcMplsTrafficEngRouterID,
       "sleISISProcPrcIntervalExpMinDelay": sleISISProcPrcIntervalExpMinDelay,
       "sleISISProcPrcIntervalExpMaxDelay": sleISISProcPrcIntervalExpMaxDelay,
       "sleISISProcProtocolTopolgy": sleISISProcProtocolTopolgy,
       "sleISISProcRestartTimerVal": sleISISProcRestartTimerVal,
       "sleISISProcRestartTimerLevel": sleISISProcRestartTimerLevel,
       "sleISISProcSpfIntervalExpMin": sleISISProcSpfIntervalExpMin,
       "sleISISProcSpfIntervalExpMax": sleISISProcSpfIntervalExpMax,
       "sleISISProcSpfIntervalExpLevel": sleISISProcSpfIntervalExpLevel,
       "sleISISProcAuthMode": sleISISProcAuthMode,
       "sleISISProcAuthModeLevel": sleISISProcAuthModeLevel,
       "sleISISProcAuthSendOnly": sleISISProcAuthSendOnly,
       "sleISISProcAuthSendOnlyLevel": sleISISProcAuthSendOnlyLevel,
       "sleISISProcDomPassVal": sleISISProcDomPassVal,
       "sleISISProcDomPassAuthSnp": sleISISProcDomPassAuthSnp,
       "sleISISProcAreaPassVal": sleISISProcAreaPassVal,
       "sleISISProcAreaPassAuthSnp": sleISISProcAreaPassAuthSnp,
       "sleISISProcSetOverloadBit": sleISISProcSetOverloadBit,
       "sleISISProcSetOverloadBitOnStartup": sleISISProcSetOverloadBitOnStartup,
       "sleISISProcSetOverloadBitOnStartupInterval": sleISISProcSetOverloadBitOnStartupInterval,
       "sleISISProcSetOverloadBitSuppress": sleISISProcSetOverloadBitSuppress,
       "sleISISProcWaitTimerVal": sleISISProcWaitTimerVal,
       "sleISISProcWaitTimerLevel": sleISISProcWaitTimerLevel,
       "sleISISProcAuthenKeyChainL1": sleISISProcAuthenKeyChainL1,
       "sleISISProcAuthenKeyChainL2": sleISISProcAuthenKeyChainL2,
       "sleISISProcAuthenKeyChainL1L2": sleISISProcAuthenKeyChainL1L2,
       "sleISISProcInfoControl": sleISISProcInfoControl,
       "sleISISProcInfoControlRequest": sleISISProcInfoControlRequest,
       "sleISISProcInfoControlStatus": sleISISProcInfoControlStatus,
       "sleISISProcInfoControlTimer": sleISISProcInfoControlTimer,
       "sleISISProcInfoControlTimeStamp": sleISISProcInfoControlTimeStamp,
       "sleISISProcInfoControlReqResult": sleISISProcInfoControlReqResult,
       "sleISISProcInfoControlTag": sleISISProcInfoControlTag,
       "sleISISProcInfoControlBfdAllInterface": sleISISProcInfoControlBfdAllInterface,
       "sleISISProcInfoControlCapCspf": sleISISProcInfoControlCapCspf,
       "sleISISProcInfoControlDynHostname": sleISISProcInfoControlDynHostname,
       "sleISISProcInfoControlDynHostnameAreaTag": sleISISProcInfoControlDynHostnameAreaTag,
       "sleISISProcInfoControlIgnLspErr": sleISISProcInfoControlIgnLspErr,
       "sleISISProcInfoControlRouteHighPriorityTag": sleISISProcInfoControlRouteHighPriorityTag,
       "sleISISProcInfoControlIspfLevel": sleISISProcInfoControlIspfLevel,
       "sleISISProcInfoControlIsTypeLevel": sleISISProcInfoControlIsTypeLevel,
       "sleISISProcInfoControlLspGenInterval": sleISISProcInfoControlLspGenInterval,
       "sleISISProcInfoControlLspGenIntervalLevel": sleISISProcInfoControlLspGenIntervalLevel,
       "sleISISProcInfoControlLspMtu": sleISISProcInfoControlLspMtu,
       "sleISISProcInfoControlLspMtuLevel": sleISISProcInfoControlLspMtuLevel,
       "sleISISProcInfoControlLspRefreshInterval": sleISISProcInfoControlLspRefreshInterval,
       "sleISISProcInfoControlMaxAreaAddressNum": sleISISProcInfoControlMaxAreaAddressNum,
       "sleISISProcInfoControlMaxLspLifetime": sleISISProcInfoControlMaxLspLifetime,
       "sleISISProcInfoControlMetricStyle": sleISISProcInfoControlMetricStyle,
       "sleISISProcInfoControlMetricStyleLevel": sleISISProcInfoControlMetricStyleLevel,
       "sleISISProcInfoControlMplsTrafficEngLevel": sleISISProcInfoControlMplsTrafficEngLevel,
       "sleISISProcInfoControlMplsTrafficEngRouterID": sleISISProcInfoControlMplsTrafficEngRouterID,
       "sleISISProcInfoControlPrcIntervalExpMinDelay": sleISISProcInfoControlPrcIntervalExpMinDelay,
       "sleISISProcInfoControlPrcIntervalExpMaxDelay": sleISISProcInfoControlPrcIntervalExpMaxDelay,
       "sleISISProcInfoControlProtocolTopolgy": sleISISProcInfoControlProtocolTopolgy,
       "sleISISProcInfoControlRestartTimerVal": sleISISProcInfoControlRestartTimerVal,
       "sleISISProcInfoControlRestartTimerLevel": sleISISProcInfoControlRestartTimerLevel,
       "sleISISProcInfoControlSpfIntervalExpMin": sleISISProcInfoControlSpfIntervalExpMin,
       "sleISISProcInfoControlSpfIntervalExpMax": sleISISProcInfoControlSpfIntervalExpMax,
       "sleISISProcInfoControlSpfIntervalExpLevel": sleISISProcInfoControlSpfIntervalExpLevel,
       "sleISISProcInfoControlAuthMode": sleISISProcInfoControlAuthMode,
       "sleISISProcInfoControlAuthModeLevel": sleISISProcInfoControlAuthModeLevel,
       "sleISISProcInfoControlAuthSendOnly": sleISISProcInfoControlAuthSendOnly,
       "sleISISProcInfoControlAuthSendOnlyLevel": sleISISProcInfoControlAuthSendOnlyLevel,
       "sleISISProcInfoControlDomPassVal": sleISISProcInfoControlDomPassVal,
       "sleISISProcInfoControlDomPassAuthSnp": sleISISProcInfoControlDomPassAuthSnp,
       "sleISISProcInfoControlAreaPassVal": sleISISProcInfoControlAreaPassVal,
       "sleISISProcInfoControlAreaPassAuthSnp": sleISISProcInfoControlAreaPassAuthSnp,
       "sleISISProcInfoControlSetOverloadBit": sleISISProcInfoControlSetOverloadBit,
       "sleISISProcInfoControlSetOverloadBitOnStartup": sleISISProcInfoControlSetOverloadBitOnStartup,
       "sleISISProcInfoControlSetOverloadBitOnStartupInterval": sleISISProcInfoControlSetOverloadBitOnStartupInterval,
       "sleISISProcInfoControlSetOverloadBitSuppress": sleISISProcInfoControlSetOverloadBitSuppress,
       "sleISISProcControlWaitTimerVal": sleISISProcControlWaitTimerVal,
       "sleISISProcControlWaitTimerLevel": sleISISProcControlWaitTimerLevel,
       "sleISISProcControlAuthenkeyChain": sleISISProcControlAuthenkeyChain,
       "sleISISProcControlAuthenkeyChainLevel": sleISISProcControlAuthenkeyChainLevel,
       "sleISISProcInfoNotification": sleISISProcInfoNotification,
       "sleISISProcNet": sleISISProcNet,
       "sleISISProcNetTable": sleISISProcNetTable,
       "sleISISProcNetEntry": sleISISProcNetEntry,
       "sleISISProcNetInstanceID": sleISISProcNetInstanceID,
       "sleISISProcNetTitle": sleISISProcNetTitle,
       "sleISISProcNetControl": sleISISProcNetControl,
       "sleISISProcNetControlRequest": sleISISProcNetControlRequest,
       "sleISISProcNetControlStatus": sleISISProcNetControlStatus,
       "sleISISProcNetControlTimer": sleISISProcNetControlTimer,
       "sleISISProcNetControlTimeStamp": sleISISProcNetControlTimeStamp,
       "sleISISProcNetControlReqResult": sleISISProcNetControlReqResult,
       "sleISISProcNetControlInstanceID": sleISISProcNetControlInstanceID,
       "sleISISProcNetControlTitle": sleISISProcNetControlTitle,
       "sleISISProcNetNotification": sleISISProcNetNotification,
       "sleISISProcDistanceV4": sleISISProcDistanceV4,
       "sleISISProcDistanceV4Table": sleISISProcDistanceV4Table,
       "sleISISProcDistanceV4Entry": sleISISProcDistanceV4Entry,
       "sleISISProcDistanceV4InstanceID": sleISISProcDistanceV4InstanceID,
       "sleISISProcDistanceV4Dist": sleISISProcDistanceV4Dist,
       "sleISISProcDistanceV4SytemID": sleISISProcDistanceV4SytemID,
       "sleISISProcDistanceV4AccessList": sleISISProcDistanceV4AccessList,
       "sleISISProcDistanceV4Control": sleISISProcDistanceV4Control,
       "sleISISProcDistanceV4ControlRequest": sleISISProcDistanceV4ControlRequest,
       "sleISISProcDistanceV4ControlStatus": sleISISProcDistanceV4ControlStatus,
       "sleISISProcDistanceV4ControlTimer": sleISISProcDistanceV4ControlTimer,
       "sleISISProcDistanceV4TimeStamp": sleISISProcDistanceV4TimeStamp,
       "sleISISProcDistanceV4ntrolReqResult": sleISISProcDistanceV4ntrolReqResult,
       "sleISISProcDistanceV4ControlInstanceID": sleISISProcDistanceV4ControlInstanceID,
       "sleISISProcDistanceV4ControlDist": sleISISProcDistanceV4ControlDist,
       "sleISISProcDistanceV4ControlSytemID": sleISISProcDistanceV4ControlSytemID,
       "sleISISProcDistanceV4ControlAccessList": sleISISProcDistanceV4ControlAccessList,
       "sleISISProcDistanceV4Notification": sleISISProcDistanceV4Notification,
       "sleISISIf": sleISISIf,
       "slsISISIfTable": slsISISIfTable,
       "slsISISIfEntry": slsISISIfEntry,
       "sleISISIfIndex": sleISISIfIndex,
       "sleISISIfMplsLdpIgpSync": sleISISIfMplsLdpIgpSync,
       "sleISISIfIpRouter": sleISISIfIpRouter,
       "sleISISIfAuthSendLevel1": sleISISIfAuthSendLevel1,
       "sleISISIfAuthSendLevel2": sleISISIfAuthSendLevel2,
       "sleISISIfAuthModeMd5Levle1": sleISISIfAuthModeMd5Levle1,
       "sleISISIfAuthModeMd5Levle2": sleISISIfAuthModeMd5Levle2,
       "sleISISIfAuthModeTextLevle1": sleISISIfAuthModeTextLevle1,
       "sleISISIfAuthModeTextLevle2": sleISISIfAuthModeTextLevle2,
       "sleISISIfAuthKeyChainLevle1": sleISISIfAuthKeyChainLevle1,
       "sleISISIfAuthKeyChainLevle2": sleISISIfAuthKeyChainLevle2,
       "sleISISIfBfd": sleISISIfBfd,
       "sleISISIfBfdDisable": sleISISIfBfdDisable,
       "sleISISIfCircuitType": sleISISIfCircuitType,
       "sleISISIfCsnpIntervalLevel1": sleISISIfCsnpIntervalLevel1,
       "sleISISIfCsnpIntervalLevel2": sleISISIfCsnpIntervalLevel2,
       "sleISISIfHelloPadding": sleISISIfHelloPadding,
       "sleISISIfHelloIntervalLevel1": sleISISIfHelloIntervalLevel1,
       "sleISISIfHelloIntervalLevel2": sleISISIfHelloIntervalLevel2,
       "sleISISIfHelloIntervalMinimalLevel1": sleISISIfHelloIntervalMinimalLevel1,
       "sleISISIfHelloIntervalMinimalLevel2": sleISISIfHelloIntervalMinimalLevel2,
       "sleISISIfHelloMultiplierLevel1": sleISISIfHelloMultiplierLevel1,
       "sleISISIfHelloMultiplierLevel2": sleISISIfHelloMultiplierLevel2,
       "sleISISIfLspInterval": sleISISIfLspInterval,
       "sleISISIfMeshGroup": sleISISIfMeshGroup,
       "sleISISIfMetricLevel1": sleISISIfMetricLevel1,
       "sleISISIfMetricLevel2": sleISISIfMetricLevel2,
       "sleISISIfNetwork": sleISISIfNetwork,
       "sleISISIfPriorityLevel1": sleISISIfPriorityLevel1,
       "sleISISIfPriorityLevel2": sleISISIfPriorityLevel2,
       "sleISISIfRestartHelloIntervalLevel1": sleISISIfRestartHelloIntervalLevel1,
       "sleISISIfRestartHelloIntervalLevel2": sleISISIfRestartHelloIntervalLevel2,
       "sleISISIfRetransmitInterval": sleISISIfRetransmitInterval,
       "sleISISIfWideMetricLevel1": sleISISIfWideMetricLevel1,
       "sleISISIfWideMetricLevel2": sleISISIfWideMetricLevel2,
       "sleISISIfControl": sleISISIfControl,
       "sleISISIfControlRequest": sleISISIfControlRequest,
       "sleISISIfControlStatus": sleISISIfControlStatus,
       "sleISISIfControlTimer": sleISISIfControlTimer,
       "sleISISIfControlTimeStamp": sleISISIfControlTimeStamp,
       "sleISISIfControlReqResult": sleISISIfControlReqResult,
       "sleISISIfControlIndex": sleISISIfControlIndex,
       "sleISISIfControlMplsLdpIgpSync": sleISISIfControlMplsLdpIgpSync,
       "sleISISIfControlIpRouter": sleISISIfControlIpRouter,
       "sleISISIfControlAuthSendLevel1": sleISISIfControlAuthSendLevel1,
       "sleISISIfControlAuthSendLevel2": sleISISIfControlAuthSendLevel2,
       "sleISISIfControlAuthModeMd5Levle1": sleISISIfControlAuthModeMd5Levle1,
       "sleISISIfControlAuthModeMd5Levle2": sleISISIfControlAuthModeMd5Levle2,
       "sleISISIfControlAuthModeTextLevle1": sleISISIfControlAuthModeTextLevle1,
       "sleISISIfControlAuthModeTextLevle2": sleISISIfControlAuthModeTextLevle2,
       "sleISISIfControlAuthKeyChainLevle1": sleISISIfControlAuthKeyChainLevle1,
       "sleISISIfControlAuthKeyChainLevle2": sleISISIfControlAuthKeyChainLevle2,
       "sleISISIfControlBfd": sleISISIfControlBfd,
       "sleISISIfControlBfdDisable": sleISISIfControlBfdDisable,
       "sleISISIfControlCircuitType": sleISISIfControlCircuitType,
       "sleISISIfControlCsnpIntervalLevel1": sleISISIfControlCsnpIntervalLevel1,
       "sleISISIfControlCsnpIntervalLevel2": sleISISIfControlCsnpIntervalLevel2,
       "sleISISIfControlHelloPadding": sleISISIfControlHelloPadding,
       "sleISISIfControlHelloIntervalLevel1": sleISISIfControlHelloIntervalLevel1,
       "sleISISIfControlHelloIntervalLevel2": sleISISIfControlHelloIntervalLevel2,
       "sleISISIfControlHelloIntervalMinimalLevel1": sleISISIfControlHelloIntervalMinimalLevel1,
       "sleISISIfControlHelloIntervalMinimalLevel2": sleISISIfControlHelloIntervalMinimalLevel2,
       "sleISISIfControlHelloMultiplierLevel1": sleISISIfControlHelloMultiplierLevel1,
       "sleISISIfControlHelloMultiplierLevel2": sleISISIfControlHelloMultiplierLevel2,
       "sleISISIfControlLspInterval": sleISISIfControlLspInterval,
       "sleISISIfControlMeshGroup": sleISISIfControlMeshGroup,
       "sleISISIfControlMetricLevel1": sleISISIfControlMetricLevel1,
       "sleISISIfControlMetricLevel2": sleISISIfControlMetricLevel2,
       "sleISISIfControlNetwork": sleISISIfControlNetwork,
       "sleISISIfControlPriorityLevel1": sleISISIfControlPriorityLevel1,
       "sleISISIfControlPriorityLevel2": sleISISIfControlPriorityLevel2,
       "sleISISIfControlRestartHelloIntervalLevel1": sleISISIfControlRestartHelloIntervalLevel1,
       "sleISISIfControlRestartHelloIntervalLevel2": sleISISIfControlRestartHelloIntervalLevel2,
       "sleISISIfControlRetransmitInterval": sleISISIfControlRetransmitInterval,
       "sleISISIfControlWideMetricLevel1": sleISISIfControlWideMetricLevel1,
       "sleISISIfControlWideMetricLevel2": sleISISIfControlWideMetricLevel2,
       "slsISISNotification": slsISISNotification,
       "sleISISIfStatusTable": sleISISIfStatusTable,
       "sleISISIfStatusEntry": sleISISIfStatusEntry,
       "sleISISIfStatusIfIndex": sleISISIfStatusIfIndex,
       "sleIsisIfStatusIfStatus": sleIsisIfStatusIfStatus,
       "sleIsisIfStatusIsisTag": sleIsisIfStatusIsisTag,
       "sleIsisIfStatusNetworkType": sleIsisIfStatusNetworkType,
       "sleIsisIfStatusCircuitType": sleIsisIfStatusCircuitType,
       "sleIsisIfStatusLocalCircuitId": sleIsisIfStatusLocalCircuitId,
       "sleIsisIfStatusExtendedLocalCircuitId": sleIsisIfStatusExtendedLocalCircuitId,
       "sleIsisIfStatusLocalSnpa": sleIsisIfStatusLocalSnpa,
       "sleIsisIfStatusLdpSyncHoldTimer": sleIsisIfStatusLdpSyncHoldTimer,
       "sleIsisIfStatusLdpSyncRemainingTime": sleIsisIfStatusLdpSyncRemainingTime,
       "sleIsisIfStatusCircuitL1Metric": sleIsisIfStatusCircuitL1Metric,
       "sleIsisIfStatusCircuitL1WideMetric": sleIsisIfStatusCircuitL1WideMetric,
       "sleIsisIfStatusCircuitL1Priority": sleIsisIfStatusCircuitL1Priority,
       "sleIsisIfStatusCircuitL1CircuitId": sleIsisIfStatusCircuitL1CircuitId,
       "sleIsisIfStatusCircuitL1ActiveAdjacencies": sleIsisIfStatusCircuitL1ActiveAdjacencies,
       "sleIsisIfStatusCircuitL1LscpMtu": sleIsisIfStatusCircuitL1LscpMtu,
       "sleIsisIfStatusCircuitL2Metric": sleIsisIfStatusCircuitL2Metric,
       "sleIsisIfStatusCircuitL2WideMetric": sleIsisIfStatusCircuitL2WideMetric,
       "sleIsisIfStatusCircuitL2Priority": sleIsisIfStatusCircuitL2Priority,
       "sleIsisIfStatusCircuitL2CircuitId": sleIsisIfStatusCircuitL2CircuitId,
       "sleIsisIfStatusCircuitL2ActiveAdjacencies": sleIsisIfStatusCircuitL2ActiveAdjacencies,
       "sleIsisIfStatusCircuitL2LscpMtu": sleIsisIfStatusCircuitL2LscpMtu,
       "sleIsisIfStatusL1HelloTimerBroadcast": sleIsisIfStatusL1HelloTimerBroadcast,
       "sleIsisIfStatusL2HelloTimerBroadcast": sleIsisIfStatusL2HelloTimerBroadcast,
       "sleIsisIfStatusL1HellotimerPoint2Point": sleIsisIfStatusL1HellotimerPoint2Point,
       "sleIsisIfStatusL2HellotimerPoint2Point": sleIsisIfStatusL2HellotimerPoint2Point,
       "sleISISInstIf": sleISISInstIf,
       "sleISISInstIfTable": sleISISInstIfTable,
       "sleISISInstIfEntry": sleISISInstIfEntry,
       "sleISISInstIfInstanceId": sleISISInstIfInstanceId,
       "sleISISInstIfInterfaceId": sleISISInstIfInterfaceId,
       "sleISISPassiveInterface": sleISISPassiveInterface,
       "sleISISInstIfControl": sleISISInstIfControl,
       "sleISISInstIfControlRequest": sleISISInstIfControlRequest,
       "sleISISInstIfControlStatus": sleISISInstIfControlStatus,
       "sleISISInstIfControlTimer": sleISISInstIfControlTimer,
       "sleISISInstIfControlTimeStamp": sleISISInstIfControlTimeStamp,
       "sleISISInstIfControlReqResult": sleISISInstIfControlReqResult,
       "sleISISInstIfControlInstanceId": sleISISInstIfControlInstanceId,
       "sleISISInstIfControlInterfaceId": sleISISInstIfControlInterfaceId,
       "sleISISInstRedistribute": sleISISInstRedistribute,
       "sleISISInstRedistProtocol": sleISISInstRedistProtocol,
       "sleISISInstRedistProtocolTable": sleISISInstRedistProtocolTable,
       "sleISISInstRedistProtocolEntry": sleISISInstRedistProtocolEntry,
       "sleISISInstRedistProtocolInstanceId": sleISISInstRedistProtocolInstanceId,
       "sleISISInstRedistProtocolId": sleISISInstRedistProtocolId,
       "sleISISInstRedistProtocolMetric": sleISISInstRedistProtocolMetric,
       "sleISISInstRedistProtocolMetricType": sleISISInstRedistProtocolMetricType,
       "sleISISInstRedistProtocolRouteLevelType": sleISISInstRedistProtocolRouteLevelType,
       "sleISISInstRedistProtocolRouteMapName": sleISISInstRedistProtocolRouteMapName,
       "sleISISInstRedistProtocolControl": sleISISInstRedistProtocolControl,
       "sleISISInstRedistProtocolControlRequest": sleISISInstRedistProtocolControlRequest,
       "sleISISInstRedistProtocolControlStatus": sleISISInstRedistProtocolControlStatus,
       "sleISISInstRedistProtocolControlTimer": sleISISInstRedistProtocolControlTimer,
       "sleISISInstRedistProtocolControlTimeStamp": sleISISInstRedistProtocolControlTimeStamp,
       "sleISISInstRedistProtocolControlReqResult": sleISISInstRedistProtocolControlReqResult,
       "sleISISInstRedistProtocolControlInstanceId": sleISISInstRedistProtocolControlInstanceId,
       "sleISISInstRedistProtocolControlId": sleISISInstRedistProtocolControlId,
       "sleISISInstRedistProtocolControlMetric": sleISISInstRedistProtocolControlMetric,
       "sleISISInstRedistProtocolControlMetricType": sleISISInstRedistProtocolControlMetricType,
       "sleISISInstRedistProtocolControlRouteLevelType": sleISISInstRedistProtocolControlRouteLevelType,
       "sleISISInstRedistProtocolControlRouteMapName": sleISISInstRedistProtocolControlRouteMapName,
       "sleISISInstRedistIsisProtocol": sleISISInstRedistIsisProtocol,
       "sleISISInstRedistIsisProtocolTable": sleISISInstRedistIsisProtocolTable,
       "sleISISInstRedistIsisProtocolEntry": sleISISInstRedistIsisProtocolEntry,
       "sleISISInstRedistIsisProtocolInstanceId": sleISISInstRedistIsisProtocolInstanceId,
       "sleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2": sleISISInstRedistIsisProtocolInterAreaFromLv1ToLv2,
       "sleISISInstRedistIsisProtocolLv1Lv2DistributeList": sleISISInstRedistIsisProtocolLv1Lv2DistributeList,
       "sleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1": sleISISInstRedistIsisProtocolInterAreaFromLv2ToLv1,
       "sleISISInstRedistIsisProtocolLv2Lv1DistributeList": sleISISInstRedistIsisProtocolLv2Lv1DistributeList,
       "sleISISInstRedistIsisProtocolControl": sleISISInstRedistIsisProtocolControl,
       "sleISISInstRedistIsisProtocolControlRequest": sleISISInstRedistIsisProtocolControlRequest,
       "sleISISInstRedistIsisProtocolControlStatus": sleISISInstRedistIsisProtocolControlStatus,
       "sleISISInstRedistIsisProtocolControlTimer": sleISISInstRedistIsisProtocolControlTimer,
       "sleISISInstRedistIsisProtocolControlTimeStamp": sleISISInstRedistIsisProtocolControlTimeStamp,
       "sleISISInstRedistIsisProtocolControlReqResult": sleISISInstRedistIsisProtocolControlReqResult,
       "sleISISInstRedistIsisProtocolControlInstanceId": sleISISInstRedistIsisProtocolControlInstanceId,
       "sleISISInstRedistIsisProtocolControlLv1Lv2DistributeList": sleISISInstRedistIsisProtocolControlLv1Lv2DistributeList,
       "sleISISInstRedistIsisProtocolControlLv2Lv1DistributeList": sleISISInstRedistIsisProtocolControlLv2Lv1DistributeList,
       "sleISISSummanryAddress": sleISISSummanryAddress,
       "sleISISSummanryAddressTable": sleISISSummanryAddressTable,
       "sleISISSummanryAddressEntry": sleISISSummanryAddressEntry,
       "sleISISSummanryAddressInstanceId": sleISISSummanryAddressInstanceId,
       "sleISISSummanryAddressIpValue": sleISISSummanryAddressIpValue,
       "sleISISSummanryAddressIpNetmask": sleISISSummanryAddressIpNetmask,
       "sleISISSummanryAddressLevel": sleISISSummanryAddressLevel,
       "sleISISSummanryAddressMetric": sleISISSummanryAddressMetric,
       "sleISISSummanryAddressControl": sleISISSummanryAddressControl,
       "sleISISSummanryAddressControlRequest": sleISISSummanryAddressControlRequest,
       "sleISISSummanryAddressControlStatus": sleISISSummanryAddressControlStatus,
       "sleISISSummanryAddressControlTimer": sleISISSummanryAddressControlTimer,
       "sleISISSummanryAddressControlTimeStamp": sleISISSummanryAddressControlTimeStamp,
       "sleISISSummanryAddressControlReqResult": sleISISSummanryAddressControlReqResult,
       "sleISISSummanryAddressControlInstanceId": sleISISSummanryAddressControlInstanceId,
       "sleISISSummanryAddressControlIpValue": sleISISSummanryAddressControlIpValue,
       "sleISISSummanryAddressControlIpNetmask": sleISISSummanryAddressControlIpNetmask,
       "sleISISSummanryAddressControlLevel": sleISISSummanryAddressControlLevel,
       "sleISISSummanryAddressControlMetric": sleISISSummanryAddressControlMetric,
       "sleISISDatabase": sleISISDatabase,
       "sleISISDatabaseTable": sleISISDatabaseTable,
       "sleISISDatabaseEntry": sleISISDatabaseEntry,
       "sleISISDatabaseTag": sleISISDatabaseTag,
       "sleISISDatabaseLevel": sleISISDatabaseLevel,
       "sleISISDatabaseLspId": sleISISDatabaseLspId,
       "sleISISDatabaseLspSeqNum": sleISISDatabaseLspSeqNum,
       "sleISISDatabaseLspChecksum": sleISISDatabaseLspChecksum,
       "sleISISDatabaseLspHoldtime": sleISISDatabaseLspHoldtime,
       "sleISISDatabaseAtt": sleISISDatabaseAtt,
       "sleISISDatabaseP": sleISISDatabaseP,
       "sleISISDatabaseOl": sleISISDatabaseOl,
       "sleISISDatabaseDetail": sleISISDatabaseDetail,
       "sleISISDatabaseDetailTable": sleISISDatabaseDetailTable,
       "sleISISDatabaseDetailEntry": sleISISDatabaseDetailEntry,
       "sleISISDatabaseDetailTag": sleISISDatabaseDetailTag,
       "sleISISDatabaseDetailLevel": sleISISDatabaseDetailLevel,
       "sleISISDatabaseDetailLspId": sleISISDatabaseDetailLspId,
       "sleISISDatabaseDetailType": sleISISDatabaseDetailType,
       "sleISISDatabaseDetailIndex": sleISISDatabaseDetailIndex,
       "sleISISDatabaseDetailPad": sleISISDatabaseDetailPad,
       "sleISISDatabaseDetailValue": sleISISDatabaseDetailValue,
       "sleISISDatabaseDetailDescription": sleISISDatabaseDetailDescription,
       "sleISISGroup": sleISISGroup}
)
