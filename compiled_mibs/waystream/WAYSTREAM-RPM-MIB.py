# SNMP MIB module (WAYSTREAM-RPM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\waystream\WAYSTREAM-RPM-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:35:02 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(wsMgmt,) = mibBuilder.importSymbols(
    "WAYSTREAM-SMI",
    "wsMgmt")


# MODULE-IDENTITY

wsRpm = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14)
)
if mibBuilder.loadTexts:
    wsRpm.setRevisions(
        ("2017-02-10 11:00",
         "2011-01-11 17:59",
         "2010-01-27 05:41",
         "2009-04-29 13:52",
         "2009-03-27 12:13",
         "2009-03-23 10:56",
         "2008-04-30 13:40")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_WsRpmNotifications_ObjectIdentity = ObjectIdentity
wsRpmNotifications = _WsRpmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 0)
)
_WsRpmGrp_ObjectIdentity = ObjectIdentity
wsRpmGrp = _WsRpmGrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2)
)
if mibBuilder.loadTexts:
    wsRpmGrp.setStatus("current")
_WsRpmGrpRtp_ObjectIdentity = ObjectIdentity
wsRpmGrpRtp = _WsRpmGrpRtp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1)
)
if mibBuilder.loadTexts:
    wsRpmGrpRtp.setStatus("current")
_WsRpmGrpRtpTable_Object = MibTable
wsRpmGrpRtpTable = _WsRpmGrpRtpTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1)
)
if mibBuilder.loadTexts:
    wsRpmGrpRtpTable.setStatus("current")
_WsRpmGrpRtpEntry_Object = MibTableRow
wsRpmGrpRtpEntry = _WsRpmGrpRtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1)
)
wsRpmGrpRtpEntry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmGrpRtpSrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmGrpRtpDestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmGrpRtpSrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmGrpRtpDestPort"),
)
if mibBuilder.loadTexts:
    wsRpmGrpRtpEntry.setStatus("current")
_WsRpmGrpRtpSrcAddr_Type = IpAddress
_WsRpmGrpRtpSrcAddr_Object = MibTableColumn
wsRpmGrpRtpSrcAddr = _WsRpmGrpRtpSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 1),
    _WsRpmGrpRtpSrcAddr_Type()
)
wsRpmGrpRtpSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmGrpRtpSrcAddr.setStatus("current")
_WsRpmGrpRtpDestAddr_Type = IpAddress
_WsRpmGrpRtpDestAddr_Object = MibTableColumn
wsRpmGrpRtpDestAddr = _WsRpmGrpRtpDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 2),
    _WsRpmGrpRtpDestAddr_Type()
)
wsRpmGrpRtpDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmGrpRtpDestAddr.setStatus("current")


class _WsRpmGrpRtpSrcPort_Type(Unsigned32):
    """Custom type wsRpmGrpRtpSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmGrpRtpSrcPort_Type.__name__ = "Unsigned32"
_WsRpmGrpRtpSrcPort_Object = MibTableColumn
wsRpmGrpRtpSrcPort = _WsRpmGrpRtpSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 3),
    _WsRpmGrpRtpSrcPort_Type()
)
wsRpmGrpRtpSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmGrpRtpSrcPort.setStatus("current")


class _WsRpmGrpRtpDestPort_Type(Unsigned32):
    """Custom type wsRpmGrpRtpDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmGrpRtpDestPort_Type.__name__ = "Unsigned32"
_WsRpmGrpRtpDestPort_Object = MibTableColumn
wsRpmGrpRtpDestPort = _WsRpmGrpRtpDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 4),
    _WsRpmGrpRtpDestPort_Type()
)
wsRpmGrpRtpDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmGrpRtpDestPort.setStatus("current")
_WsRpmGrpRtpBps_Type = Unsigned32
_WsRpmGrpRtpBps_Object = MibTableColumn
wsRpmGrpRtpBps = _WsRpmGrpRtpBps_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 5),
    _WsRpmGrpRtpBps_Type()
)
wsRpmGrpRtpBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpBps.setStatus("current")
_WsRpmGrpRtpAge_Type = TimeTicks
_WsRpmGrpRtpAge_Object = MibTableColumn
wsRpmGrpRtpAge = _WsRpmGrpRtpAge_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 6),
    _WsRpmGrpRtpAge_Type()
)
wsRpmGrpRtpAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpAge.setStatus("current")
_WsRpmGrpRtpBytes_Type = Counter32
_WsRpmGrpRtpBytes_Object = MibTableColumn
wsRpmGrpRtpBytes = _WsRpmGrpRtpBytes_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 7),
    _WsRpmGrpRtpBytes_Type()
)
wsRpmGrpRtpBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpBytes.setStatus("current")
_WsRpmGrpRtpUnknownVersion_Type = Counter32
_WsRpmGrpRtpUnknownVersion_Object = MibTableColumn
wsRpmGrpRtpUnknownVersion = _WsRpmGrpRtpUnknownVersion_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 8),
    _WsRpmGrpRtpUnknownVersion_Type()
)
wsRpmGrpRtpUnknownVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpUnknownVersion.setStatus("current")
_WsRpmGrpRtpIpFragments_Type = Counter32
_WsRpmGrpRtpIpFragments_Object = MibTableColumn
wsRpmGrpRtpIpFragments = _WsRpmGrpRtpIpFragments_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 9),
    _WsRpmGrpRtpIpFragments_Type()
)
wsRpmGrpRtpIpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpIpFragments.setStatus("current")
_WsRpmGrpRtpSeqErrors_Type = Counter32
_WsRpmGrpRtpSeqErrors_Object = MibTableColumn
wsRpmGrpRtpSeqErrors = _WsRpmGrpRtpSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 10),
    _WsRpmGrpRtpSeqErrors_Type()
)
wsRpmGrpRtpSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpSeqErrors.setStatus("current")
_WsRpmGrpRtpJitter_Type = Unsigned32
_WsRpmGrpRtpJitter_Object = MibTableColumn
wsRpmGrpRtpJitter = _WsRpmGrpRtpJitter_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 11),
    _WsRpmGrpRtpJitter_Type()
)
wsRpmGrpRtpJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpJitter.setStatus("current")
_WsRpmGrpRtpErrSum_Type = Counter32
_WsRpmGrpRtpErrSum_Object = MibTableColumn
wsRpmGrpRtpErrSum = _WsRpmGrpRtpErrSum_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 12),
    _WsRpmGrpRtpErrSum_Type()
)
wsRpmGrpRtpErrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpErrSum.setStatus("current")
_WsRpmGrpRtpPeriodSeqErrors_Type = Counter32
_WsRpmGrpRtpPeriodSeqErrors_Object = MibTableColumn
wsRpmGrpRtpPeriodSeqErrors = _WsRpmGrpRtpPeriodSeqErrors_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 13),
    _WsRpmGrpRtpPeriodSeqErrors_Type()
)
wsRpmGrpRtpPeriodSeqErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpPeriodSeqErrors.setStatus("current")
_WsRpmGrpRtpPeriodMaxJitter_Type = Unsigned32
_WsRpmGrpRtpPeriodMaxJitter_Object = MibTableColumn
wsRpmGrpRtpPeriodMaxJitter = _WsRpmGrpRtpPeriodMaxJitter_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 1, 1, 14),
    _WsRpmGrpRtpPeriodMaxJitter_Type()
)
wsRpmGrpRtpPeriodMaxJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpPeriodMaxJitter.setStatus("current")
_WsRpmGrpRtpMdiTable_Object = MibTable
wsRpmGrpRtpMdiTable = _WsRpmGrpRtpMdiTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2)
)
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiTable.setStatus("current")
_WsRpmGrpRtpMdiEntry_Object = MibTableRow
wsRpmGrpRtpMdiEntry = _WsRpmGrpRtpMdiEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1)
)
wsRpmGrpRtpMdiEntry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmGrpRtpMdiSrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmGrpRtpMdiDestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmGrpRtpMdiSrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmGrpRtpMdiDestPort"),
)
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiEntry.setStatus("current")
_WsRpmGrpRtpMdiSrcAddr_Type = IpAddress
_WsRpmGrpRtpMdiSrcAddr_Object = MibTableColumn
wsRpmGrpRtpMdiSrcAddr = _WsRpmGrpRtpMdiSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 1),
    _WsRpmGrpRtpMdiSrcAddr_Type()
)
wsRpmGrpRtpMdiSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiSrcAddr.setStatus("current")
_WsRpmGrpRtpMdiDestAddr_Type = IpAddress
_WsRpmGrpRtpMdiDestAddr_Object = MibTableColumn
wsRpmGrpRtpMdiDestAddr = _WsRpmGrpRtpMdiDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 2),
    _WsRpmGrpRtpMdiDestAddr_Type()
)
wsRpmGrpRtpMdiDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiDestAddr.setStatus("current")


class _WsRpmGrpRtpMdiSrcPort_Type(Unsigned32):
    """Custom type wsRpmGrpRtpMdiSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmGrpRtpMdiSrcPort_Type.__name__ = "Unsigned32"
_WsRpmGrpRtpMdiSrcPort_Object = MibTableColumn
wsRpmGrpRtpMdiSrcPort = _WsRpmGrpRtpMdiSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 3),
    _WsRpmGrpRtpMdiSrcPort_Type()
)
wsRpmGrpRtpMdiSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiSrcPort.setStatus("current")


class _WsRpmGrpRtpMdiDestPort_Type(Unsigned32):
    """Custom type wsRpmGrpRtpMdiDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmGrpRtpMdiDestPort_Type.__name__ = "Unsigned32"
_WsRpmGrpRtpMdiDestPort_Object = MibTableColumn
wsRpmGrpRtpMdiDestPort = _WsRpmGrpRtpMdiDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 4),
    _WsRpmGrpRtpMdiDestPort_Type()
)
wsRpmGrpRtpMdiDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiDestPort.setStatus("current")
_WsRpmGrpRtpMdiDLFactor_Type = Unsigned32
_WsRpmGrpRtpMdiDLFactor_Object = MibTableColumn
wsRpmGrpRtpMdiDLFactor = _WsRpmGrpRtpMdiDLFactor_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 5),
    _WsRpmGrpRtpMdiDLFactor_Type()
)
wsRpmGrpRtpMdiDLFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiDLFactor.setStatus("current")
_WsRpmGrpRtpMdiMLRFactor_Type = Unsigned32
_WsRpmGrpRtpMdiMLRFactor_Object = MibTableColumn
wsRpmGrpRtpMdiMLRFactor = _WsRpmGrpRtpMdiMLRFactor_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 6),
    _WsRpmGrpRtpMdiMLRFactor_Type()
)
wsRpmGrpRtpMdiMLRFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiMLRFactor.setStatus("current")
_WsRpmGrpRtpMdiDFThreshold_Type = Unsigned32
_WsRpmGrpRtpMdiDFThreshold_Object = MibTableColumn
wsRpmGrpRtpMdiDFThreshold = _WsRpmGrpRtpMdiDFThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 7),
    _WsRpmGrpRtpMdiDFThreshold_Type()
)
wsRpmGrpRtpMdiDFThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiDFThreshold.setStatus("current")
_WsRpmGrpRtpMdiMLRThreshold_Type = Unsigned32
_WsRpmGrpRtpMdiMLRThreshold_Object = MibTableColumn
wsRpmGrpRtpMdiMLRThreshold = _WsRpmGrpRtpMdiMLRThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 8),
    _WsRpmGrpRtpMdiMLRThreshold_Type()
)
wsRpmGrpRtpMdiMLRThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiMLRThreshold.setStatus("current")
_WsRpmGrpRtpMdiDFErrorIntervals_Type = Unsigned32
_WsRpmGrpRtpMdiDFErrorIntervals_Object = MibTableColumn
wsRpmGrpRtpMdiDFErrorIntervals = _WsRpmGrpRtpMdiDFErrorIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 9),
    _WsRpmGrpRtpMdiDFErrorIntervals_Type()
)
wsRpmGrpRtpMdiDFErrorIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiDFErrorIntervals.setStatus("current")
_WsRpmGrpRtpMdiMLRErrorIntervals_Type = Unsigned32
_WsRpmGrpRtpMdiMLRErrorIntervals_Object = MibTableColumn
wsRpmGrpRtpMdiMLRErrorIntervals = _WsRpmGrpRtpMdiMLRErrorIntervals_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 2, 1, 2, 1, 10),
    _WsRpmGrpRtpMdiMLRErrorIntervals_Type()
)
wsRpmGrpRtpMdiMLRErrorIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmGrpRtpMdiMLRErrorIntervals.setStatus("current")
_WsRpmTS_ObjectIdentity = ObjectIdentity
wsRpmTS = _WsRpmTS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3)
)
if mibBuilder.loadTexts:
    wsRpmTS.setStatus("current")
_WsRpmTSMpeg_ObjectIdentity = ObjectIdentity
wsRpmTSMpeg = _WsRpmTSMpeg_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1)
)
if mibBuilder.loadTexts:
    wsRpmTSMpeg.setStatus("current")
_WsRpmTSMpegTable_Object = MibTable
wsRpmTSMpegTable = _WsRpmTSMpegTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1)
)
if mibBuilder.loadTexts:
    wsRpmTSMpegTable.setStatus("current")
_WsRpmTSMpegEntry_Object = MibTableRow
wsRpmTSMpegEntry = _WsRpmTSMpegEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1)
)
wsRpmTSMpegEntry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmTSMpegSrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmTSMpegDestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmTSMpegSrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmTSMpegDestPort"),
)
if mibBuilder.loadTexts:
    wsRpmTSMpegEntry.setStatus("current")
_WsRpmTSMpegSrcAddr_Type = IpAddress
_WsRpmTSMpegSrcAddr_Object = MibTableColumn
wsRpmTSMpegSrcAddr = _WsRpmTSMpegSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 1),
    _WsRpmTSMpegSrcAddr_Type()
)
wsRpmTSMpegSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmTSMpegSrcAddr.setStatus("current")
_WsRpmTSMpegDestAddr_Type = IpAddress
_WsRpmTSMpegDestAddr_Object = MibTableColumn
wsRpmTSMpegDestAddr = _WsRpmTSMpegDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 2),
    _WsRpmTSMpegDestAddr_Type()
)
wsRpmTSMpegDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmTSMpegDestAddr.setStatus("current")


class _WsRpmTSMpegSrcPort_Type(Unsigned32):
    """Custom type wsRpmTSMpegSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmTSMpegSrcPort_Type.__name__ = "Unsigned32"
_WsRpmTSMpegSrcPort_Object = MibTableColumn
wsRpmTSMpegSrcPort = _WsRpmTSMpegSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 3),
    _WsRpmTSMpegSrcPort_Type()
)
wsRpmTSMpegSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmTSMpegSrcPort.setStatus("current")


class _WsRpmTSMpegDestPort_Type(Unsigned32):
    """Custom type wsRpmTSMpegDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmTSMpegDestPort_Type.__name__ = "Unsigned32"
_WsRpmTSMpegDestPort_Object = MibTableColumn
wsRpmTSMpegDestPort = _WsRpmTSMpegDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 4),
    _WsRpmTSMpegDestPort_Type()
)
wsRpmTSMpegDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmTSMpegDestPort.setStatus("current")
_WsRpmTSMpegBps_Type = Unsigned32
_WsRpmTSMpegBps_Object = MibTableColumn
wsRpmTSMpegBps = _WsRpmTSMpegBps_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 5),
    _WsRpmTSMpegBps_Type()
)
wsRpmTSMpegBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegBps.setStatus("current")
_WsRpmTSMpegAge_Type = TimeTicks
_WsRpmTSMpegAge_Object = MibTableColumn
wsRpmTSMpegAge = _WsRpmTSMpegAge_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 6),
    _WsRpmTSMpegAge_Type()
)
wsRpmTSMpegAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegAge.setStatus("current")
_WsRpmTSMpegBytes_Type = Counter32
_WsRpmTSMpegBytes_Object = MibTableColumn
wsRpmTSMpegBytes = _WsRpmTSMpegBytes_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 7),
    _WsRpmTSMpegBytes_Type()
)
wsRpmTSMpegBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegBytes.setStatus("current")
_WsRpmTSMpegMissingSync_Type = Counter32
_WsRpmTSMpegMissingSync_Object = MibTableColumn
wsRpmTSMpegMissingSync = _WsRpmTSMpegMissingSync_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 8),
    _WsRpmTSMpegMissingSync_Type()
)
wsRpmTSMpegMissingSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegMissingSync.setStatus("current")
_WsRpmTSMpegIpFragments_Type = Counter32
_WsRpmTSMpegIpFragments_Object = MibTableColumn
wsRpmTSMpegIpFragments = _WsRpmTSMpegIpFragments_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 9),
    _WsRpmTSMpegIpFragments_Type()
)
wsRpmTSMpegIpFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegIpFragments.setStatus("current")
_WsRpmTSMpegMisalignments_Type = Counter32
_WsRpmTSMpegMisalignments_Object = MibTableColumn
wsRpmTSMpegMisalignments = _WsRpmTSMpegMisalignments_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 10),
    _WsRpmTSMpegMisalignments_Type()
)
wsRpmTSMpegMisalignments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegMisalignments.setStatus("current")
_WsRpmTSMpegFlowAge_Type = TimeTicks
_WsRpmTSMpegFlowAge_Object = MibTableColumn
wsRpmTSMpegFlowAge = _WsRpmTSMpegFlowAge_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 11),
    _WsRpmTSMpegFlowAge_Type()
)
wsRpmTSMpegFlowAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegFlowAge.setStatus("current")
_WsRpmTSMpegIngressIf_Type = Unsigned32
_WsRpmTSMpegIngressIf_Object = MibTableColumn
wsRpmTSMpegIngressIf = _WsRpmTSMpegIngressIf_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 12),
    _WsRpmTSMpegIngressIf_Type()
)
wsRpmTSMpegIngressIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegIngressIf.setStatus("current")
_WsRpmTSMpegErrSum_Type = Counter32
_WsRpmTSMpegErrSum_Object = MibTableColumn
wsRpmTSMpegErrSum = _WsRpmTSMpegErrSum_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 13),
    _WsRpmTSMpegErrSum_Type()
)
wsRpmTSMpegErrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegErrSum.setStatus("current")
_WsRpmTSMpegPeriodMissingSync_Type = Counter32
_WsRpmTSMpegPeriodMissingSync_Object = MibTableColumn
wsRpmTSMpegPeriodMissingSync = _WsRpmTSMpegPeriodMissingSync_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 14),
    _WsRpmTSMpegPeriodMissingSync_Type()
)
wsRpmTSMpegPeriodMissingSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegPeriodMissingSync.setStatus("current")
_WsRpmTSMpegPeriodMisalignments_Type = Counter32
_WsRpmTSMpegPeriodMisalignments_Object = MibTableColumn
wsRpmTSMpegPeriodMisalignments = _WsRpmTSMpegPeriodMisalignments_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 3, 1, 1, 1, 15),
    _WsRpmTSMpegPeriodMisalignments_Type()
)
wsRpmTSMpegPeriodMisalignments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmTSMpegPeriodMisalignments.setStatus("current")
_WsRpmES_ObjectIdentity = ObjectIdentity
wsRpmES = _WsRpmES_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4)
)
if mibBuilder.loadTexts:
    wsRpmES.setStatus("current")
_WsRpmESPat_ObjectIdentity = ObjectIdentity
wsRpmESPat = _WsRpmESPat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1)
)
if mibBuilder.loadTexts:
    wsRpmESPat.setStatus("current")
_WsRpmESPatTable_Object = MibTable
wsRpmESPatTable = _WsRpmESPatTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1)
)
if mibBuilder.loadTexts:
    wsRpmESPatTable.setStatus("current")
_WsRpmESPatEntry_Object = MibTableRow
wsRpmESPatEntry = _WsRpmESPatEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1)
)
wsRpmESPatEntry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPatSrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPatDestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPatSrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPatDestPort"),
)
if mibBuilder.loadTexts:
    wsRpmESPatEntry.setStatus("current")
_WsRpmESPatSrcAddr_Type = IpAddress
_WsRpmESPatSrcAddr_Object = MibTableColumn
wsRpmESPatSrcAddr = _WsRpmESPatSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 1),
    _WsRpmESPatSrcAddr_Type()
)
wsRpmESPatSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPatSrcAddr.setStatus("current")
_WsRpmESPatDestAddr_Type = IpAddress
_WsRpmESPatDestAddr_Object = MibTableColumn
wsRpmESPatDestAddr = _WsRpmESPatDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 2),
    _WsRpmESPatDestAddr_Type()
)
wsRpmESPatDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPatDestAddr.setStatus("current")


class _WsRpmESPatSrcPort_Type(Unsigned32):
    """Custom type wsRpmESPatSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESPatSrcPort_Type.__name__ = "Unsigned32"
_WsRpmESPatSrcPort_Object = MibTableColumn
wsRpmESPatSrcPort = _WsRpmESPatSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 3),
    _WsRpmESPatSrcPort_Type()
)
wsRpmESPatSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPatSrcPort.setStatus("current")


class _WsRpmESPatDestPort_Type(Unsigned32):
    """Custom type wsRpmESPatDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESPatDestPort_Type.__name__ = "Unsigned32"
_WsRpmESPatDestPort_Object = MibTableColumn
wsRpmESPatDestPort = _WsRpmESPatDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 4),
    _WsRpmESPatDestPort_Type()
)
wsRpmESPatDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPatDestPort.setStatus("current")
_WsRpmESPatBps_Type = Unsigned32
_WsRpmESPatBps_Object = MibTableColumn
wsRpmESPatBps = _WsRpmESPatBps_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 5),
    _WsRpmESPatBps_Type()
)
wsRpmESPatBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPatBps.setStatus("current")
_WsRpmESPatAge_Type = TimeTicks
_WsRpmESPatAge_Object = MibTableColumn
wsRpmESPatAge = _WsRpmESPatAge_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 6),
    _WsRpmESPatAge_Type()
)
wsRpmESPatAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPatAge.setStatus("current")
_WsRpmESPatBytes_Type = Counter32
_WsRpmESPatBytes_Object = MibTableColumn
wsRpmESPatBytes = _WsRpmESPatBytes_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 7),
    _WsRpmESPatBytes_Type()
)
wsRpmESPatBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPatBytes.setStatus("current")
_WsRpmESPatInterCcErr_Type = Counter32
_WsRpmESPatInterCcErr_Object = MibTableColumn
wsRpmESPatInterCcErr = _WsRpmESPatInterCcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 8),
    _WsRpmESPatInterCcErr_Type()
)
wsRpmESPatInterCcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPatInterCcErr.setStatus("current")
_WsRpmESPatIntraCcErr_Type = Counter32
_WsRpmESPatIntraCcErr_Object = MibTableColumn
wsRpmESPatIntraCcErr = _WsRpmESPatIntraCcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 9),
    _WsRpmESPatIntraCcErr_Type()
)
wsRpmESPatIntraCcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPatIntraCcErr.setStatus("current")
_WsRpmESPatCcErrSum_Type = Counter32
_WsRpmESPatCcErrSum_Object = MibTableColumn
wsRpmESPatCcErrSum = _WsRpmESPatCcErrSum_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 1, 1, 10),
    _WsRpmESPatCcErrSum_Type()
)
wsRpmESPatCcErrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPatCcErrSum.setStatus("current")
_WsRpmESPatTr290Table_Object = MibTable
wsRpmESPatTr290Table = _WsRpmESPatTr290Table_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 2)
)
if mibBuilder.loadTexts:
    wsRpmESPatTr290Table.setStatus("current")
_WsRpmESPatTr290Entry_Object = MibTableRow
wsRpmESPatTr290Entry = _WsRpmESPatTr290Entry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 2, 1)
)
wsRpmESPatTr290Entry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPatTr290SrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPatTr290DestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPatTr290SrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPatTr290DestPort"),
)
if mibBuilder.loadTexts:
    wsRpmESPatTr290Entry.setStatus("current")
_WsRpmESPatTr290SrcAddr_Type = IpAddress
_WsRpmESPatTr290SrcAddr_Object = MibTableColumn
wsRpmESPatTr290SrcAddr = _WsRpmESPatTr290SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 2, 1, 1),
    _WsRpmESPatTr290SrcAddr_Type()
)
wsRpmESPatTr290SrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPatTr290SrcAddr.setStatus("current")
_WsRpmESPatTr290DestAddr_Type = IpAddress
_WsRpmESPatTr290DestAddr_Object = MibTableColumn
wsRpmESPatTr290DestAddr = _WsRpmESPatTr290DestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 2, 1, 2),
    _WsRpmESPatTr290DestAddr_Type()
)
wsRpmESPatTr290DestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPatTr290DestAddr.setStatus("current")


class _WsRpmESPatTr290SrcPort_Type(Unsigned32):
    """Custom type wsRpmESPatTr290SrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESPatTr290SrcPort_Type.__name__ = "Unsigned32"
_WsRpmESPatTr290SrcPort_Object = MibTableColumn
wsRpmESPatTr290SrcPort = _WsRpmESPatTr290SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 2, 1, 3),
    _WsRpmESPatTr290SrcPort_Type()
)
wsRpmESPatTr290SrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPatTr290SrcPort.setStatus("current")


class _WsRpmESPatTr290DestPort_Type(Unsigned32):
    """Custom type wsRpmESPatTr290DestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESPatTr290DestPort_Type.__name__ = "Unsigned32"
_WsRpmESPatTr290DestPort_Object = MibTableColumn
wsRpmESPatTr290DestPort = _WsRpmESPatTr290DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 2, 1, 4),
    _WsRpmESPatTr290DestPort_Type()
)
wsRpmESPatTr290DestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPatTr290DestPort.setStatus("current")
_WsRpmESPatTr290PatErr_Type = Counter32
_WsRpmESPatTr290PatErr_Object = MibTableColumn
wsRpmESPatTr290PatErr = _WsRpmESPatTr290PatErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 2, 1, 5),
    _WsRpmESPatTr290PatErr_Type()
)
wsRpmESPatTr290PatErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPatTr290PatErr.setStatus("current")
_WsRpmESPatTr290CrcErr_Type = Counter32
_WsRpmESPatTr290CrcErr_Object = MibTableColumn
wsRpmESPatTr290CrcErr = _WsRpmESPatTr290CrcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 1, 2, 1, 6),
    _WsRpmESPatTr290CrcErr_Type()
)
wsRpmESPatTr290CrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPatTr290CrcErr.setStatus("current")
_WsRpmESPmt_ObjectIdentity = ObjectIdentity
wsRpmESPmt = _WsRpmESPmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2)
)
if mibBuilder.loadTexts:
    wsRpmESPmt.setStatus("current")
_WsRpmESPmtTable_Object = MibTable
wsRpmESPmtTable = _WsRpmESPmtTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1)
)
if mibBuilder.loadTexts:
    wsRpmESPmtTable.setStatus("current")
_WsRpmESPmtEntry_Object = MibTableRow
wsRpmESPmtEntry = _WsRpmESPmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1)
)
wsRpmESPmtEntry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtSrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtDestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtSrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtDestPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtPid"),
)
if mibBuilder.loadTexts:
    wsRpmESPmtEntry.setStatus("current")
_WsRpmESPmtSrcAddr_Type = IpAddress
_WsRpmESPmtSrcAddr_Object = MibTableColumn
wsRpmESPmtSrcAddr = _WsRpmESPmtSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 1),
    _WsRpmESPmtSrcAddr_Type()
)
wsRpmESPmtSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtSrcAddr.setStatus("current")
_WsRpmESPmtDestAddr_Type = IpAddress
_WsRpmESPmtDestAddr_Object = MibTableColumn
wsRpmESPmtDestAddr = _WsRpmESPmtDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 2),
    _WsRpmESPmtDestAddr_Type()
)
wsRpmESPmtDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtDestAddr.setStatus("current")


class _WsRpmESPmtSrcPort_Type(Unsigned32):
    """Custom type wsRpmESPmtSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESPmtSrcPort_Type.__name__ = "Unsigned32"
_WsRpmESPmtSrcPort_Object = MibTableColumn
wsRpmESPmtSrcPort = _WsRpmESPmtSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 3),
    _WsRpmESPmtSrcPort_Type()
)
wsRpmESPmtSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtSrcPort.setStatus("current")


class _WsRpmESPmtDestPort_Type(Unsigned32):
    """Custom type wsRpmESPmtDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESPmtDestPort_Type.__name__ = "Unsigned32"
_WsRpmESPmtDestPort_Object = MibTableColumn
wsRpmESPmtDestPort = _WsRpmESPmtDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 4),
    _WsRpmESPmtDestPort_Type()
)
wsRpmESPmtDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtDestPort.setStatus("current")


class _WsRpmESPmtPid_Type(Unsigned32):
    """Custom type wsRpmESPmtPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_WsRpmESPmtPid_Type.__name__ = "Unsigned32"
_WsRpmESPmtPid_Object = MibTableColumn
wsRpmESPmtPid = _WsRpmESPmtPid_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 5),
    _WsRpmESPmtPid_Type()
)
wsRpmESPmtPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtPid.setStatus("current")
_WsRpmESPmtBps_Type = Unsigned32
_WsRpmESPmtBps_Object = MibTableColumn
wsRpmESPmtBps = _WsRpmESPmtBps_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 6),
    _WsRpmESPmtBps_Type()
)
wsRpmESPmtBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPmtBps.setStatus("current")
_WsRpmESPmtAge_Type = TimeTicks
_WsRpmESPmtAge_Object = MibTableColumn
wsRpmESPmtAge = _WsRpmESPmtAge_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 7),
    _WsRpmESPmtAge_Type()
)
wsRpmESPmtAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPmtAge.setStatus("current")
_WsRpmESPmtBytes_Type = Counter32
_WsRpmESPmtBytes_Object = MibTableColumn
wsRpmESPmtBytes = _WsRpmESPmtBytes_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 8),
    _WsRpmESPmtBytes_Type()
)
wsRpmESPmtBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPmtBytes.setStatus("current")
_WsRpmESPmtInterCcErr_Type = Counter32
_WsRpmESPmtInterCcErr_Object = MibTableColumn
wsRpmESPmtInterCcErr = _WsRpmESPmtInterCcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 9),
    _WsRpmESPmtInterCcErr_Type()
)
wsRpmESPmtInterCcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPmtInterCcErr.setStatus("current")
_WsRpmESPmtIntraCcErr_Type = Counter32
_WsRpmESPmtIntraCcErr_Object = MibTableColumn
wsRpmESPmtIntraCcErr = _WsRpmESPmtIntraCcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 10),
    _WsRpmESPmtIntraCcErr_Type()
)
wsRpmESPmtIntraCcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPmtIntraCcErr.setStatus("current")
_WsRpmESPmtCcErrSum_Type = Counter32
_WsRpmESPmtCcErrSum_Object = MibTableColumn
wsRpmESPmtCcErrSum = _WsRpmESPmtCcErrSum_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 1, 1, 11),
    _WsRpmESPmtCcErrSum_Type()
)
wsRpmESPmtCcErrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPmtCcErrSum.setStatus("current")
_WsRpmESPmtTr290Table_Object = MibTable
wsRpmESPmtTr290Table = _WsRpmESPmtTr290Table_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 2)
)
if mibBuilder.loadTexts:
    wsRpmESPmtTr290Table.setStatus("current")
_WsRpmESPmtTr290Entry_Object = MibTableRow
wsRpmESPmtTr290Entry = _WsRpmESPmtTr290Entry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 2, 1)
)
wsRpmESPmtTr290Entry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtTr290SrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtTr290DestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtTr290SrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtTr290DestPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESPmtTr290Pid"),
)
if mibBuilder.loadTexts:
    wsRpmESPmtTr290Entry.setStatus("current")
_WsRpmESPmtTr290SrcAddr_Type = IpAddress
_WsRpmESPmtTr290SrcAddr_Object = MibTableColumn
wsRpmESPmtTr290SrcAddr = _WsRpmESPmtTr290SrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 2, 1, 1),
    _WsRpmESPmtTr290SrcAddr_Type()
)
wsRpmESPmtTr290SrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtTr290SrcAddr.setStatus("current")
_WsRpmESPmtTr290DestAddr_Type = IpAddress
_WsRpmESPmtTr290DestAddr_Object = MibTableColumn
wsRpmESPmtTr290DestAddr = _WsRpmESPmtTr290DestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 2, 1, 2),
    _WsRpmESPmtTr290DestAddr_Type()
)
wsRpmESPmtTr290DestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtTr290DestAddr.setStatus("current")


class _WsRpmESPmtTr290SrcPort_Type(Unsigned32):
    """Custom type wsRpmESPmtTr290SrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESPmtTr290SrcPort_Type.__name__ = "Unsigned32"
_WsRpmESPmtTr290SrcPort_Object = MibTableColumn
wsRpmESPmtTr290SrcPort = _WsRpmESPmtTr290SrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 2, 1, 3),
    _WsRpmESPmtTr290SrcPort_Type()
)
wsRpmESPmtTr290SrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtTr290SrcPort.setStatus("current")


class _WsRpmESPmtTr290DestPort_Type(Unsigned32):
    """Custom type wsRpmESPmtTr290DestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESPmtTr290DestPort_Type.__name__ = "Unsigned32"
_WsRpmESPmtTr290DestPort_Object = MibTableColumn
wsRpmESPmtTr290DestPort = _WsRpmESPmtTr290DestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 2, 1, 4),
    _WsRpmESPmtTr290DestPort_Type()
)
wsRpmESPmtTr290DestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtTr290DestPort.setStatus("current")


class _WsRpmESPmtTr290Pid_Type(Unsigned32):
    """Custom type wsRpmESPmtTr290Pid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_WsRpmESPmtTr290Pid_Type.__name__ = "Unsigned32"
_WsRpmESPmtTr290Pid_Object = MibTableColumn
wsRpmESPmtTr290Pid = _WsRpmESPmtTr290Pid_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 2, 1, 5),
    _WsRpmESPmtTr290Pid_Type()
)
wsRpmESPmtTr290Pid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESPmtTr290Pid.setStatus("current")
_WsRpmESPmtTr290PmtErr_Type = Counter32
_WsRpmESPmtTr290PmtErr_Object = MibTableColumn
wsRpmESPmtTr290PmtErr = _WsRpmESPmtTr290PmtErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 2, 1, 6),
    _WsRpmESPmtTr290PmtErr_Type()
)
wsRpmESPmtTr290PmtErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPmtTr290PmtErr.setStatus("current")
_WsRpmESPmtTr290CrcErr_Type = Counter32
_WsRpmESPmtTr290CrcErr_Object = MibTableColumn
wsRpmESPmtTr290CrcErr = _WsRpmESPmtTr290CrcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 2, 2, 1, 7),
    _WsRpmESPmtTr290CrcErr_Type()
)
wsRpmESPmtTr290CrcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESPmtTr290CrcErr.setStatus("current")
_WsRpmESVideo_ObjectIdentity = ObjectIdentity
wsRpmESVideo = _WsRpmESVideo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3)
)
if mibBuilder.loadTexts:
    wsRpmESVideo.setStatus("current")
_WsRpmESVideoTable_Object = MibTable
wsRpmESVideoTable = _WsRpmESVideoTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1)
)
if mibBuilder.loadTexts:
    wsRpmESVideoTable.setStatus("current")
_WsRpmESVideoEntry_Object = MibTableRow
wsRpmESVideoEntry = _WsRpmESVideoEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1)
)
wsRpmESVideoEntry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoSrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoDestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoSrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoDestPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoPid"),
)
if mibBuilder.loadTexts:
    wsRpmESVideoEntry.setStatus("current")
_WsRpmESVideoSrcAddr_Type = IpAddress
_WsRpmESVideoSrcAddr_Object = MibTableColumn
wsRpmESVideoSrcAddr = _WsRpmESVideoSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 1),
    _WsRpmESVideoSrcAddr_Type()
)
wsRpmESVideoSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoSrcAddr.setStatus("current")
_WsRpmESVideoDestAddr_Type = IpAddress
_WsRpmESVideoDestAddr_Object = MibTableColumn
wsRpmESVideoDestAddr = _WsRpmESVideoDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 2),
    _WsRpmESVideoDestAddr_Type()
)
wsRpmESVideoDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoDestAddr.setStatus("current")


class _WsRpmESVideoSrcPort_Type(Unsigned32):
    """Custom type wsRpmESVideoSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESVideoSrcPort_Type.__name__ = "Unsigned32"
_WsRpmESVideoSrcPort_Object = MibTableColumn
wsRpmESVideoSrcPort = _WsRpmESVideoSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 3),
    _WsRpmESVideoSrcPort_Type()
)
wsRpmESVideoSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoSrcPort.setStatus("current")


class _WsRpmESVideoDestPort_Type(Unsigned32):
    """Custom type wsRpmESVideoDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESVideoDestPort_Type.__name__ = "Unsigned32"
_WsRpmESVideoDestPort_Object = MibTableColumn
wsRpmESVideoDestPort = _WsRpmESVideoDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 4),
    _WsRpmESVideoDestPort_Type()
)
wsRpmESVideoDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoDestPort.setStatus("current")


class _WsRpmESVideoPid_Type(Unsigned32):
    """Custom type wsRpmESVideoPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_WsRpmESVideoPid_Type.__name__ = "Unsigned32"
_WsRpmESVideoPid_Object = MibTableColumn
wsRpmESVideoPid = _WsRpmESVideoPid_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 5),
    _WsRpmESVideoPid_Type()
)
wsRpmESVideoPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoPid.setStatus("current")
_WsRpmESVideoBps_Type = Unsigned32
_WsRpmESVideoBps_Object = MibTableColumn
wsRpmESVideoBps = _WsRpmESVideoBps_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 6),
    _WsRpmESVideoBps_Type()
)
wsRpmESVideoBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoBps.setStatus("current")
_WsRpmESVideoAge_Type = TimeTicks
_WsRpmESVideoAge_Object = MibTableColumn
wsRpmESVideoAge = _WsRpmESVideoAge_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 7),
    _WsRpmESVideoAge_Type()
)
wsRpmESVideoAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoAge.setStatus("current")
_WsRpmESVideoBytes_Type = Counter32
_WsRpmESVideoBytes_Object = MibTableColumn
wsRpmESVideoBytes = _WsRpmESVideoBytes_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 8),
    _WsRpmESVideoBytes_Type()
)
wsRpmESVideoBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoBytes.setStatus("current")
_WsRpmESVideoInterCcErr_Type = Counter32
_WsRpmESVideoInterCcErr_Object = MibTableColumn
wsRpmESVideoInterCcErr = _WsRpmESVideoInterCcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 9),
    _WsRpmESVideoInterCcErr_Type()
)
wsRpmESVideoInterCcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoInterCcErr.setStatus("current")
_WsRpmESVideoIntraCcErr_Type = Counter32
_WsRpmESVideoIntraCcErr_Object = MibTableColumn
wsRpmESVideoIntraCcErr = _WsRpmESVideoIntraCcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 10),
    _WsRpmESVideoIntraCcErr_Type()
)
wsRpmESVideoIntraCcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoIntraCcErr.setStatus("current")
_WsRpmESVideoPCRJitter_Type = Unsigned32
_WsRpmESVideoPCRJitter_Object = MibTableColumn
wsRpmESVideoPCRJitter = _WsRpmESVideoPCRJitter_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 11),
    _WsRpmESVideoPCRJitter_Type()
)
wsRpmESVideoPCRJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPCRJitter.setStatus("current")
_WsRpmESVideoCcErrSum_Type = Counter32
_WsRpmESVideoCcErrSum_Object = MibTableColumn
wsRpmESVideoCcErrSum = _WsRpmESVideoCcErrSum_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 1, 1, 12),
    _WsRpmESVideoCcErrSum_Type()
)
wsRpmESVideoCcErrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoCcErrSum.setStatus("current")
_WsRpmESVideoPicTable_Object = MibTable
wsRpmESVideoPicTable = _WsRpmESVideoPicTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2)
)
if mibBuilder.loadTexts:
    wsRpmESVideoPicTable.setStatus("current")
_WsRpmESVideoPicEntry_Object = MibTableRow
wsRpmESVideoPicEntry = _WsRpmESVideoPicEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1)
)
wsRpmESVideoPicEntry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoPicSrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoPicDestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoPicSrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoPicDestPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESVideoPicPid"),
)
if mibBuilder.loadTexts:
    wsRpmESVideoPicEntry.setStatus("current")
_WsRpmESVideoPicSrcAddr_Type = IpAddress
_WsRpmESVideoPicSrcAddr_Object = MibTableColumn
wsRpmESVideoPicSrcAddr = _WsRpmESVideoPicSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 1),
    _WsRpmESVideoPicSrcAddr_Type()
)
wsRpmESVideoPicSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoPicSrcAddr.setStatus("current")
_WsRpmESVideoPicDestAddr_Type = IpAddress
_WsRpmESVideoPicDestAddr_Object = MibTableColumn
wsRpmESVideoPicDestAddr = _WsRpmESVideoPicDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 2),
    _WsRpmESVideoPicDestAddr_Type()
)
wsRpmESVideoPicDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoPicDestAddr.setStatus("current")


class _WsRpmESVideoPicSrcPort_Type(Unsigned32):
    """Custom type wsRpmESVideoPicSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESVideoPicSrcPort_Type.__name__ = "Unsigned32"
_WsRpmESVideoPicSrcPort_Object = MibTableColumn
wsRpmESVideoPicSrcPort = _WsRpmESVideoPicSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 3),
    _WsRpmESVideoPicSrcPort_Type()
)
wsRpmESVideoPicSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoPicSrcPort.setStatus("current")


class _WsRpmESVideoPicDestPort_Type(Unsigned32):
    """Custom type wsRpmESVideoPicDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESVideoPicDestPort_Type.__name__ = "Unsigned32"
_WsRpmESVideoPicDestPort_Object = MibTableColumn
wsRpmESVideoPicDestPort = _WsRpmESVideoPicDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 4),
    _WsRpmESVideoPicDestPort_Type()
)
wsRpmESVideoPicDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoPicDestPort.setStatus("current")


class _WsRpmESVideoPicPid_Type(Unsigned32):
    """Custom type wsRpmESVideoPicPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_WsRpmESVideoPicPid_Type.__name__ = "Unsigned32"
_WsRpmESVideoPicPid_Object = MibTableColumn
wsRpmESVideoPicPid = _WsRpmESVideoPicPid_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 5),
    _WsRpmESVideoPicPid_Type()
)
wsRpmESVideoPicPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESVideoPicPid.setStatus("current")
_WsRpmESVideoPicTsLossInIframe_Type = Counter32
_WsRpmESVideoPicTsLossInIframe_Object = MibTableColumn
wsRpmESVideoPicTsLossInIframe = _WsRpmESVideoPicTsLossInIframe_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 6),
    _WsRpmESVideoPicTsLossInIframe_Type()
)
wsRpmESVideoPicTsLossInIframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPicTsLossInIframe.setStatus("current")
_WsRpmESVideoPicImpairedIframe_Type = Counter32
_WsRpmESVideoPicImpairedIframe_Object = MibTableColumn
wsRpmESVideoPicImpairedIframe = _WsRpmESVideoPicImpairedIframe_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 7),
    _WsRpmESVideoPicImpairedIframe_Type()
)
wsRpmESVideoPicImpairedIframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPicImpairedIframe.setStatus("current")
_WsRpmESVideoPicGoodIframe_Type = Counter32
_WsRpmESVideoPicGoodIframe_Object = MibTableColumn
wsRpmESVideoPicGoodIframe = _WsRpmESVideoPicGoodIframe_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 8),
    _WsRpmESVideoPicGoodIframe_Type()
)
wsRpmESVideoPicGoodIframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPicGoodIframe.setStatus("current")
_WsRpmESVideoPicTsLossInPframe_Type = Counter32
_WsRpmESVideoPicTsLossInPframe_Object = MibTableColumn
wsRpmESVideoPicTsLossInPframe = _WsRpmESVideoPicTsLossInPframe_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 9),
    _WsRpmESVideoPicTsLossInPframe_Type()
)
wsRpmESVideoPicTsLossInPframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPicTsLossInPframe.setStatus("current")
_WsRpmESVideoPicImpairedPframe_Type = Counter32
_WsRpmESVideoPicImpairedPframe_Object = MibTableColumn
wsRpmESVideoPicImpairedPframe = _WsRpmESVideoPicImpairedPframe_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 10),
    _WsRpmESVideoPicImpairedPframe_Type()
)
wsRpmESVideoPicImpairedPframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPicImpairedPframe.setStatus("current")
_WsRpmESVideoPicGoodPframe_Type = Counter32
_WsRpmESVideoPicGoodPframe_Object = MibTableColumn
wsRpmESVideoPicGoodPframe = _WsRpmESVideoPicGoodPframe_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 11),
    _WsRpmESVideoPicGoodPframe_Type()
)
wsRpmESVideoPicGoodPframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPicGoodPframe.setStatus("current")
_WsRpmESVideoPicTsLossInBframe_Type = Counter32
_WsRpmESVideoPicTsLossInBframe_Object = MibTableColumn
wsRpmESVideoPicTsLossInBframe = _WsRpmESVideoPicTsLossInBframe_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 12),
    _WsRpmESVideoPicTsLossInBframe_Type()
)
wsRpmESVideoPicTsLossInBframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPicTsLossInBframe.setStatus("current")
_WsRpmESVideoPicImpairedBframe_Type = Counter32
_WsRpmESVideoPicImpairedBframe_Object = MibTableColumn
wsRpmESVideoPicImpairedBframe = _WsRpmESVideoPicImpairedBframe_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 13),
    _WsRpmESVideoPicImpairedBframe_Type()
)
wsRpmESVideoPicImpairedBframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPicImpairedBframe.setStatus("current")
_WsRpmESVideoPicGoodBframe_Type = Counter32
_WsRpmESVideoPicGoodBframe_Object = MibTableColumn
wsRpmESVideoPicGoodBframe = _WsRpmESVideoPicGoodBframe_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 3, 2, 1, 14),
    _WsRpmESVideoPicGoodBframe_Type()
)
wsRpmESVideoPicGoodBframe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESVideoPicGoodBframe.setStatus("current")
_WsRpmESAudio_ObjectIdentity = ObjectIdentity
wsRpmESAudio = _WsRpmESAudio_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4)
)
if mibBuilder.loadTexts:
    wsRpmESAudio.setStatus("current")
_WsRpmESAudioTable_Object = MibTable
wsRpmESAudioTable = _WsRpmESAudioTable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1)
)
if mibBuilder.loadTexts:
    wsRpmESAudioTable.setStatus("current")
_WsRpmESAudioEntry_Object = MibTableRow
wsRpmESAudioEntry = _WsRpmESAudioEntry_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1)
)
wsRpmESAudioEntry.setIndexNames(
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESAudioSrcAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESAudioDestAddr"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESAudioSrcPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESAudioDestPort"),
    (0, "WAYSTREAM-RPM-MIB", "wsRpmESAudioPid"),
)
if mibBuilder.loadTexts:
    wsRpmESAudioEntry.setStatus("current")
_WsRpmESAudioSrcAddr_Type = IpAddress
_WsRpmESAudioSrcAddr_Object = MibTableColumn
wsRpmESAudioSrcAddr = _WsRpmESAudioSrcAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 1),
    _WsRpmESAudioSrcAddr_Type()
)
wsRpmESAudioSrcAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESAudioSrcAddr.setStatus("current")
_WsRpmESAudioDestAddr_Type = IpAddress
_WsRpmESAudioDestAddr_Object = MibTableColumn
wsRpmESAudioDestAddr = _WsRpmESAudioDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 2),
    _WsRpmESAudioDestAddr_Type()
)
wsRpmESAudioDestAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESAudioDestAddr.setStatus("current")


class _WsRpmESAudioSrcPort_Type(Unsigned32):
    """Custom type wsRpmESAudioSrcPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESAudioSrcPort_Type.__name__ = "Unsigned32"
_WsRpmESAudioSrcPort_Object = MibTableColumn
wsRpmESAudioSrcPort = _WsRpmESAudioSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 3),
    _WsRpmESAudioSrcPort_Type()
)
wsRpmESAudioSrcPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESAudioSrcPort.setStatus("current")


class _WsRpmESAudioDestPort_Type(Unsigned32):
    """Custom type wsRpmESAudioDestPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_WsRpmESAudioDestPort_Type.__name__ = "Unsigned32"
_WsRpmESAudioDestPort_Object = MibTableColumn
wsRpmESAudioDestPort = _WsRpmESAudioDestPort_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 4),
    _WsRpmESAudioDestPort_Type()
)
wsRpmESAudioDestPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESAudioDestPort.setStatus("current")


class _WsRpmESAudioPid_Type(Unsigned32):
    """Custom type wsRpmESAudioPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_WsRpmESAudioPid_Type.__name__ = "Unsigned32"
_WsRpmESAudioPid_Object = MibTableColumn
wsRpmESAudioPid = _WsRpmESAudioPid_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 5),
    _WsRpmESAudioPid_Type()
)
wsRpmESAudioPid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    wsRpmESAudioPid.setStatus("current")
_WsRpmESAudioBps_Type = Unsigned32
_WsRpmESAudioBps_Object = MibTableColumn
wsRpmESAudioBps = _WsRpmESAudioBps_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 6),
    _WsRpmESAudioBps_Type()
)
wsRpmESAudioBps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESAudioBps.setStatus("current")
_WsRpmESAudioAge_Type = TimeTicks
_WsRpmESAudioAge_Object = MibTableColumn
wsRpmESAudioAge = _WsRpmESAudioAge_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 7),
    _WsRpmESAudioAge_Type()
)
wsRpmESAudioAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESAudioAge.setStatus("current")
_WsRpmESAudioBytes_Type = Counter32
_WsRpmESAudioBytes_Object = MibTableColumn
wsRpmESAudioBytes = _WsRpmESAudioBytes_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 8),
    _WsRpmESAudioBytes_Type()
)
wsRpmESAudioBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESAudioBytes.setStatus("current")
_WsRpmESAudioInterCcErr_Type = Counter32
_WsRpmESAudioInterCcErr_Object = MibTableColumn
wsRpmESAudioInterCcErr = _WsRpmESAudioInterCcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 9),
    _WsRpmESAudioInterCcErr_Type()
)
wsRpmESAudioInterCcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESAudioInterCcErr.setStatus("current")
_WsRpmESAudioIntraCcErr_Type = Counter32
_WsRpmESAudioIntraCcErr_Object = MibTableColumn
wsRpmESAudioIntraCcErr = _WsRpmESAudioIntraCcErr_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 10),
    _WsRpmESAudioIntraCcErr_Type()
)
wsRpmESAudioIntraCcErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESAudioIntraCcErr.setStatus("current")
_WsRpmESAudioCcErrSum_Type = Counter32
_WsRpmESAudioCcErrSum_Object = MibTableColumn
wsRpmESAudioCcErrSum = _WsRpmESAudioCcErrSum_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 4, 4, 1, 1, 11),
    _WsRpmESAudioCcErrSum_Type()
)
wsRpmESAudioCcErrSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wsRpmESAudioCcErrSum.setStatus("current")
_WsRpmConfig_ObjectIdentity = ObjectIdentity
wsRpmConfig = _WsRpmConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5)
)


class _WsRpmTrapEnable_Type(Integer32):
    """Custom type wsRpmTrapEnable based on Integer32"""
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


_WsRpmTrapEnable_Type.__name__ = "Integer32"
_WsRpmTrapEnable_Object = MibScalar
wsRpmTrapEnable = _WsRpmTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 1),
    _WsRpmTrapEnable_Type()
)
wsRpmTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmTrapEnable.setStatus("current")


class _WsRpmLogEnable_Type(Integer32):
    """Custom type wsRpmLogEnable based on Integer32"""
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


_WsRpmLogEnable_Type.__name__ = "Integer32"
_WsRpmLogEnable_Object = MibScalar
wsRpmLogEnable = _WsRpmLogEnable_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 2),
    _WsRpmLogEnable_Type()
)
wsRpmLogEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmLogEnable.setStatus("current")
_WsRpmThresholdConfig_ObjectIdentity = ObjectIdentity
wsRpmThresholdConfig = _WsRpmThresholdConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 3)
)


class _WsRpmRtpSeqErrThreshold_Type(Integer32):
    """Custom type wsRpmRtpSeqErrThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WsRpmRtpSeqErrThreshold_Type.__name__ = "Integer32"
_WsRpmRtpSeqErrThreshold_Object = MibScalar
wsRpmRtpSeqErrThreshold = _WsRpmRtpSeqErrThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 3, 1),
    _WsRpmRtpSeqErrThreshold_Type()
)
wsRpmRtpSeqErrThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmRtpSeqErrThreshold.setStatus("current")


class _WsRpmRtpJitterThreshold_Type(Integer32):
    """Custom type wsRpmRtpJitterThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WsRpmRtpJitterThreshold_Type.__name__ = "Integer32"
_WsRpmRtpJitterThreshold_Object = MibScalar
wsRpmRtpJitterThreshold = _WsRpmRtpJitterThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 3, 2),
    _WsRpmRtpJitterThreshold_Type()
)
wsRpmRtpJitterThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmRtpJitterThreshold.setStatus("current")


class _WsRpmTSMpegMissSyncThreshold_Type(Integer32):
    """Custom type wsRpmTSMpegMissSyncThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WsRpmTSMpegMissSyncThreshold_Type.__name__ = "Integer32"
_WsRpmTSMpegMissSyncThreshold_Object = MibScalar
wsRpmTSMpegMissSyncThreshold = _WsRpmTSMpegMissSyncThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 3, 3),
    _WsRpmTSMpegMissSyncThreshold_Type()
)
wsRpmTSMpegMissSyncThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmTSMpegMissSyncThreshold.setStatus("current")


class _WsRpmTSMpegMisalignThreshold_Type(Integer32):
    """Custom type wsRpmTSMpegMisalignThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_WsRpmTSMpegMisalignThreshold_Type.__name__ = "Integer32"
_WsRpmTSMpegMisalignThreshold_Object = MibScalar
wsRpmTSMpegMisalignThreshold = _WsRpmTSMpegMisalignThreshold_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 3, 4),
    _WsRpmTSMpegMisalignThreshold_Type()
)
wsRpmTSMpegMisalignThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmTSMpegMisalignThreshold.setStatus("current")
_WsRpmPeriodConfig_ObjectIdentity = ObjectIdentity
wsRpmPeriodConfig = _WsRpmPeriodConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 4)
)


class _WsRpmRtpSeqErrPeriod_Type(Integer32):
    """Custom type wsRpmRtpSeqErrPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_WsRpmRtpSeqErrPeriod_Type.__name__ = "Integer32"
_WsRpmRtpSeqErrPeriod_Object = MibScalar
wsRpmRtpSeqErrPeriod = _WsRpmRtpSeqErrPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 4, 1),
    _WsRpmRtpSeqErrPeriod_Type()
)
wsRpmRtpSeqErrPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmRtpSeqErrPeriod.setStatus("current")


class _WsRpmRtpJitterPeriod_Type(Integer32):
    """Custom type wsRpmRtpJitterPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_WsRpmRtpJitterPeriod_Type.__name__ = "Integer32"
_WsRpmRtpJitterPeriod_Object = MibScalar
wsRpmRtpJitterPeriod = _WsRpmRtpJitterPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 4, 2),
    _WsRpmRtpJitterPeriod_Type()
)
wsRpmRtpJitterPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmRtpJitterPeriod.setStatus("current")


class _WsRpmTSMpegMissSyncPeriod_Type(Integer32):
    """Custom type wsRpmTSMpegMissSyncPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_WsRpmTSMpegMissSyncPeriod_Type.__name__ = "Integer32"
_WsRpmTSMpegMissSyncPeriod_Object = MibScalar
wsRpmTSMpegMissSyncPeriod = _WsRpmTSMpegMissSyncPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 4, 3),
    _WsRpmTSMpegMissSyncPeriod_Type()
)
wsRpmTSMpegMissSyncPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmTSMpegMissSyncPeriod.setStatus("current")


class _WsRpmTSMpegMisalignPeriod_Type(Integer32):
    """Custom type wsRpmTSMpegMisalignPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 604800),
    )


_WsRpmTSMpegMisalignPeriod_Type.__name__ = "Integer32"
_WsRpmTSMpegMisalignPeriod_Object = MibScalar
wsRpmTSMpegMisalignPeriod = _WsRpmTSMpegMisalignPeriod_Object(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 5, 4, 4),
    _WsRpmTSMpegMisalignPeriod_Type()
)
wsRpmTSMpegMisalignPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    wsRpmTSMpegMisalignPeriod.setStatus("current")

# Managed Objects groups


# Notification objects

notifyWsRpmRtpSeqError = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 0, 1)
)
notifyWsRpmRtpSeqError.setObjects(
      *(("WAYSTREAM-RPM-MIB", "wsRpmGrpRtpPeriodSeqErrors"),
        ("WAYSTREAM-RPM-MIB", "wsRpmRtpSeqErrThreshold"),
        ("WAYSTREAM-RPM-MIB", "wsRpmRtpSeqErrPeriod"))
)
if mibBuilder.loadTexts:
    notifyWsRpmRtpSeqError.setStatus(
        "current"
    )

notifyWsRpmRtpJitter = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 0, 2)
)
notifyWsRpmRtpJitter.setObjects(
      *(("WAYSTREAM-RPM-MIB", "wsRpmGrpRtpPeriodMaxJitter"),
        ("WAYSTREAM-RPM-MIB", "wsRpmRtpJitterThreshold"),
        ("WAYSTREAM-RPM-MIB", "wsRpmRtpJitterPeriod"))
)
if mibBuilder.loadTexts:
    notifyWsRpmRtpJitter.setStatus(
        "current"
    )

notifyWsRpmTSMpegMissSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 0, 3)
)
notifyWsRpmTSMpegMissSync.setObjects(
      *(("WAYSTREAM-RPM-MIB", "wsRpmTSMpegPeriodMissingSync"),
        ("WAYSTREAM-RPM-MIB", "wsRpmTSMpegMissSyncThreshold"),
        ("WAYSTREAM-RPM-MIB", "wsRpmTSMpegMissSyncPeriod"))
)
if mibBuilder.loadTexts:
    notifyWsRpmTSMpegMissSync.setStatus(
        "current"
    )

notifyWsRpmTSMpegMisalign = NotificationType(
    (1, 3, 6, 1, 4, 1, 9303, 4, 14, 0, 4)
)
notifyWsRpmTSMpegMisalign.setObjects(
      *(("WAYSTREAM-RPM-MIB", "wsRpmTSMpegPeriodMisalignments"),
        ("WAYSTREAM-RPM-MIB", "wsRpmTSMpegMisalignThreshold"),
        ("WAYSTREAM-RPM-MIB", "wsRpmTSMpegMisalignPeriod"))
)
if mibBuilder.loadTexts:
    notifyWsRpmTSMpegMisalign.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "WAYSTREAM-RPM-MIB",
    **{"wsRpm": wsRpm,
       "wsRpmNotifications": wsRpmNotifications,
       "notifyWsRpmRtpSeqError": notifyWsRpmRtpSeqError,
       "notifyWsRpmRtpJitter": notifyWsRpmRtpJitter,
       "notifyWsRpmTSMpegMissSync": notifyWsRpmTSMpegMissSync,
       "notifyWsRpmTSMpegMisalign": notifyWsRpmTSMpegMisalign,
       "wsRpmGrp": wsRpmGrp,
       "wsRpmGrpRtp": wsRpmGrpRtp,
       "wsRpmGrpRtpTable": wsRpmGrpRtpTable,
       "wsRpmGrpRtpEntry": wsRpmGrpRtpEntry,
       "wsRpmGrpRtpSrcAddr": wsRpmGrpRtpSrcAddr,
       "wsRpmGrpRtpDestAddr": wsRpmGrpRtpDestAddr,
       "wsRpmGrpRtpSrcPort": wsRpmGrpRtpSrcPort,
       "wsRpmGrpRtpDestPort": wsRpmGrpRtpDestPort,
       "wsRpmGrpRtpBps": wsRpmGrpRtpBps,
       "wsRpmGrpRtpAge": wsRpmGrpRtpAge,
       "wsRpmGrpRtpBytes": wsRpmGrpRtpBytes,
       "wsRpmGrpRtpUnknownVersion": wsRpmGrpRtpUnknownVersion,
       "wsRpmGrpRtpIpFragments": wsRpmGrpRtpIpFragments,
       "wsRpmGrpRtpSeqErrors": wsRpmGrpRtpSeqErrors,
       "wsRpmGrpRtpJitter": wsRpmGrpRtpJitter,
       "wsRpmGrpRtpErrSum": wsRpmGrpRtpErrSum,
       "wsRpmGrpRtpPeriodSeqErrors": wsRpmGrpRtpPeriodSeqErrors,
       "wsRpmGrpRtpPeriodMaxJitter": wsRpmGrpRtpPeriodMaxJitter,
       "wsRpmGrpRtpMdiTable": wsRpmGrpRtpMdiTable,
       "wsRpmGrpRtpMdiEntry": wsRpmGrpRtpMdiEntry,
       "wsRpmGrpRtpMdiSrcAddr": wsRpmGrpRtpMdiSrcAddr,
       "wsRpmGrpRtpMdiDestAddr": wsRpmGrpRtpMdiDestAddr,
       "wsRpmGrpRtpMdiSrcPort": wsRpmGrpRtpMdiSrcPort,
       "wsRpmGrpRtpMdiDestPort": wsRpmGrpRtpMdiDestPort,
       "wsRpmGrpRtpMdiDLFactor": wsRpmGrpRtpMdiDLFactor,
       "wsRpmGrpRtpMdiMLRFactor": wsRpmGrpRtpMdiMLRFactor,
       "wsRpmGrpRtpMdiDFThreshold": wsRpmGrpRtpMdiDFThreshold,
       "wsRpmGrpRtpMdiMLRThreshold": wsRpmGrpRtpMdiMLRThreshold,
       "wsRpmGrpRtpMdiDFErrorIntervals": wsRpmGrpRtpMdiDFErrorIntervals,
       "wsRpmGrpRtpMdiMLRErrorIntervals": wsRpmGrpRtpMdiMLRErrorIntervals,
       "wsRpmTS": wsRpmTS,
       "wsRpmTSMpeg": wsRpmTSMpeg,
       "wsRpmTSMpegTable": wsRpmTSMpegTable,
       "wsRpmTSMpegEntry": wsRpmTSMpegEntry,
       "wsRpmTSMpegSrcAddr": wsRpmTSMpegSrcAddr,
       "wsRpmTSMpegDestAddr": wsRpmTSMpegDestAddr,
       "wsRpmTSMpegSrcPort": wsRpmTSMpegSrcPort,
       "wsRpmTSMpegDestPort": wsRpmTSMpegDestPort,
       "wsRpmTSMpegBps": wsRpmTSMpegBps,
       "wsRpmTSMpegAge": wsRpmTSMpegAge,
       "wsRpmTSMpegBytes": wsRpmTSMpegBytes,
       "wsRpmTSMpegMissingSync": wsRpmTSMpegMissingSync,
       "wsRpmTSMpegIpFragments": wsRpmTSMpegIpFragments,
       "wsRpmTSMpegMisalignments": wsRpmTSMpegMisalignments,
       "wsRpmTSMpegFlowAge": wsRpmTSMpegFlowAge,
       "wsRpmTSMpegIngressIf": wsRpmTSMpegIngressIf,
       "wsRpmTSMpegErrSum": wsRpmTSMpegErrSum,
       "wsRpmTSMpegPeriodMissingSync": wsRpmTSMpegPeriodMissingSync,
       "wsRpmTSMpegPeriodMisalignments": wsRpmTSMpegPeriodMisalignments,
       "wsRpmES": wsRpmES,
       "wsRpmESPat": wsRpmESPat,
       "wsRpmESPatTable": wsRpmESPatTable,
       "wsRpmESPatEntry": wsRpmESPatEntry,
       "wsRpmESPatSrcAddr": wsRpmESPatSrcAddr,
       "wsRpmESPatDestAddr": wsRpmESPatDestAddr,
       "wsRpmESPatSrcPort": wsRpmESPatSrcPort,
       "wsRpmESPatDestPort": wsRpmESPatDestPort,
       "wsRpmESPatBps": wsRpmESPatBps,
       "wsRpmESPatAge": wsRpmESPatAge,
       "wsRpmESPatBytes": wsRpmESPatBytes,
       "wsRpmESPatInterCcErr": wsRpmESPatInterCcErr,
       "wsRpmESPatIntraCcErr": wsRpmESPatIntraCcErr,
       "wsRpmESPatCcErrSum": wsRpmESPatCcErrSum,
       "wsRpmESPatTr290Table": wsRpmESPatTr290Table,
       "wsRpmESPatTr290Entry": wsRpmESPatTr290Entry,
       "wsRpmESPatTr290SrcAddr": wsRpmESPatTr290SrcAddr,
       "wsRpmESPatTr290DestAddr": wsRpmESPatTr290DestAddr,
       "wsRpmESPatTr290SrcPort": wsRpmESPatTr290SrcPort,
       "wsRpmESPatTr290DestPort": wsRpmESPatTr290DestPort,
       "wsRpmESPatTr290PatErr": wsRpmESPatTr290PatErr,
       "wsRpmESPatTr290CrcErr": wsRpmESPatTr290CrcErr,
       "wsRpmESPmt": wsRpmESPmt,
       "wsRpmESPmtTable": wsRpmESPmtTable,
       "wsRpmESPmtEntry": wsRpmESPmtEntry,
       "wsRpmESPmtSrcAddr": wsRpmESPmtSrcAddr,
       "wsRpmESPmtDestAddr": wsRpmESPmtDestAddr,
       "wsRpmESPmtSrcPort": wsRpmESPmtSrcPort,
       "wsRpmESPmtDestPort": wsRpmESPmtDestPort,
       "wsRpmESPmtPid": wsRpmESPmtPid,
       "wsRpmESPmtBps": wsRpmESPmtBps,
       "wsRpmESPmtAge": wsRpmESPmtAge,
       "wsRpmESPmtBytes": wsRpmESPmtBytes,
       "wsRpmESPmtInterCcErr": wsRpmESPmtInterCcErr,
       "wsRpmESPmtIntraCcErr": wsRpmESPmtIntraCcErr,
       "wsRpmESPmtCcErrSum": wsRpmESPmtCcErrSum,
       "wsRpmESPmtTr290Table": wsRpmESPmtTr290Table,
       "wsRpmESPmtTr290Entry": wsRpmESPmtTr290Entry,
       "wsRpmESPmtTr290SrcAddr": wsRpmESPmtTr290SrcAddr,
       "wsRpmESPmtTr290DestAddr": wsRpmESPmtTr290DestAddr,
       "wsRpmESPmtTr290SrcPort": wsRpmESPmtTr290SrcPort,
       "wsRpmESPmtTr290DestPort": wsRpmESPmtTr290DestPort,
       "wsRpmESPmtTr290Pid": wsRpmESPmtTr290Pid,
       "wsRpmESPmtTr290PmtErr": wsRpmESPmtTr290PmtErr,
       "wsRpmESPmtTr290CrcErr": wsRpmESPmtTr290CrcErr,
       "wsRpmESVideo": wsRpmESVideo,
       "wsRpmESVideoTable": wsRpmESVideoTable,
       "wsRpmESVideoEntry": wsRpmESVideoEntry,
       "wsRpmESVideoSrcAddr": wsRpmESVideoSrcAddr,
       "wsRpmESVideoDestAddr": wsRpmESVideoDestAddr,
       "wsRpmESVideoSrcPort": wsRpmESVideoSrcPort,
       "wsRpmESVideoDestPort": wsRpmESVideoDestPort,
       "wsRpmESVideoPid": wsRpmESVideoPid,
       "wsRpmESVideoBps": wsRpmESVideoBps,
       "wsRpmESVideoAge": wsRpmESVideoAge,
       "wsRpmESVideoBytes": wsRpmESVideoBytes,
       "wsRpmESVideoInterCcErr": wsRpmESVideoInterCcErr,
       "wsRpmESVideoIntraCcErr": wsRpmESVideoIntraCcErr,
       "wsRpmESVideoPCRJitter": wsRpmESVideoPCRJitter,
       "wsRpmESVideoCcErrSum": wsRpmESVideoCcErrSum,
       "wsRpmESVideoPicTable": wsRpmESVideoPicTable,
       "wsRpmESVideoPicEntry": wsRpmESVideoPicEntry,
       "wsRpmESVideoPicSrcAddr": wsRpmESVideoPicSrcAddr,
       "wsRpmESVideoPicDestAddr": wsRpmESVideoPicDestAddr,
       "wsRpmESVideoPicSrcPort": wsRpmESVideoPicSrcPort,
       "wsRpmESVideoPicDestPort": wsRpmESVideoPicDestPort,
       "wsRpmESVideoPicPid": wsRpmESVideoPicPid,
       "wsRpmESVideoPicTsLossInIframe": wsRpmESVideoPicTsLossInIframe,
       "wsRpmESVideoPicImpairedIframe": wsRpmESVideoPicImpairedIframe,
       "wsRpmESVideoPicGoodIframe": wsRpmESVideoPicGoodIframe,
       "wsRpmESVideoPicTsLossInPframe": wsRpmESVideoPicTsLossInPframe,
       "wsRpmESVideoPicImpairedPframe": wsRpmESVideoPicImpairedPframe,
       "wsRpmESVideoPicGoodPframe": wsRpmESVideoPicGoodPframe,
       "wsRpmESVideoPicTsLossInBframe": wsRpmESVideoPicTsLossInBframe,
       "wsRpmESVideoPicImpairedBframe": wsRpmESVideoPicImpairedBframe,
       "wsRpmESVideoPicGoodBframe": wsRpmESVideoPicGoodBframe,
       "wsRpmESAudio": wsRpmESAudio,
       "wsRpmESAudioTable": wsRpmESAudioTable,
       "wsRpmESAudioEntry": wsRpmESAudioEntry,
       "wsRpmESAudioSrcAddr": wsRpmESAudioSrcAddr,
       "wsRpmESAudioDestAddr": wsRpmESAudioDestAddr,
       "wsRpmESAudioSrcPort": wsRpmESAudioSrcPort,
       "wsRpmESAudioDestPort": wsRpmESAudioDestPort,
       "wsRpmESAudioPid": wsRpmESAudioPid,
       "wsRpmESAudioBps": wsRpmESAudioBps,
       "wsRpmESAudioAge": wsRpmESAudioAge,
       "wsRpmESAudioBytes": wsRpmESAudioBytes,
       "wsRpmESAudioInterCcErr": wsRpmESAudioInterCcErr,
       "wsRpmESAudioIntraCcErr": wsRpmESAudioIntraCcErr,
       "wsRpmESAudioCcErrSum": wsRpmESAudioCcErrSum,
       "wsRpmConfig": wsRpmConfig,
       "wsRpmTrapEnable": wsRpmTrapEnable,
       "wsRpmLogEnable": wsRpmLogEnable,
       "wsRpmThresholdConfig": wsRpmThresholdConfig,
       "wsRpmRtpSeqErrThreshold": wsRpmRtpSeqErrThreshold,
       "wsRpmRtpJitterThreshold": wsRpmRtpJitterThreshold,
       "wsRpmTSMpegMissSyncThreshold": wsRpmTSMpegMissSyncThreshold,
       "wsRpmTSMpegMisalignThreshold": wsRpmTSMpegMisalignThreshold,
       "wsRpmPeriodConfig": wsRpmPeriodConfig,
       "wsRpmRtpSeqErrPeriod": wsRpmRtpSeqErrPeriod,
       "wsRpmRtpJitterPeriod": wsRpmRtpJitterPeriod,
       "wsRpmTSMpegMissSyncPeriod": wsRpmTSMpegMissSyncPeriod,
       "wsRpmTSMpegMisalignPeriod": wsRpmTSMpegMisalignPeriod}
)
