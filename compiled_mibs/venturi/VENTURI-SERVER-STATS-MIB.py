# SNMP MIB module (VENTURI-SERVER-STATS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\venturi\VENTURI-SERVER-STATS-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:33:50 2025
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

(vServerMgmt,) = mibBuilder.importSymbols(
    "VENTURI-SERVER-MIB",
    "vServerMgmt")

(VenturiHexUnsigned32,
 VenturiProtocolType,
 VenturiSubscriberType) = mibBuilder.importSymbols(
    "VENTURI-TC",
    "VenturiHexUnsigned32",
    "VenturiProtocolType",
    "VenturiSubscriberType")


# MODULE-IDENTITY

vServerStatistics = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3)
)
if mibBuilder.loadTexts:
    vServerStatistics.setRevisions(
        ("2013-02-22 00:00",
         "2013-01-27 00:00",
         "2013-01-21 00:00",
         "2011-02-08 00:00",
         "2011-01-03 00:00",
         "2010-09-20 00:00",
         "2010-01-06 00:00",
         "2008-04-30 00:00",
         "2008-02-19 00:00",
         "2006-04-27 00:00",
         "2005-07-22 00:00",
         "2005-02-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_VServerStatsSystem_ObjectIdentity = ObjectIdentity
vServerStatsSystem = _VServerStatsSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1)
)
_VServerStatsSystemScalars_ObjectIdentity = ObjectIdentity
vServerStatsSystemScalars = _VServerStatsSystemScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1)
)
_VServerSystemTotalVenturiBuffers_Type = Integer32
_VServerSystemTotalVenturiBuffers_Object = MibScalar
vServerSystemTotalVenturiBuffers = _VServerSystemTotalVenturiBuffers_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1, 1),
    _VServerSystemTotalVenturiBuffers_Type()
)
vServerSystemTotalVenturiBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSystemTotalVenturiBuffers.setStatus("current")
_VServerStatsSystemUsedVenturiBuffers_Type = Integer32
_VServerStatsSystemUsedVenturiBuffers_Object = MibScalar
vServerStatsSystemUsedVenturiBuffers = _VServerStatsSystemUsedVenturiBuffers_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1, 2),
    _VServerStatsSystemUsedVenturiBuffers_Type()
)
vServerStatsSystemUsedVenturiBuffers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStatsSystemUsedVenturiBuffers.setStatus("current")
_VServerTotalStreamContexts_Type = Integer32
_VServerTotalStreamContexts_Object = MibScalar
vServerTotalStreamContexts = _VServerTotalStreamContexts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1, 3),
    _VServerTotalStreamContexts_Type()
)
vServerTotalStreamContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTotalStreamContexts.setStatus("current")
_VServerUsedStreamContexts_Type = Integer32
_VServerUsedStreamContexts_Object = MibScalar
vServerUsedStreamContexts = _VServerUsedStreamContexts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1, 4),
    _VServerUsedStreamContexts_Type()
)
vServerUsedStreamContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerUsedStreamContexts.setStatus("current")
_VServerTotalCompressorContexts_Type = Integer32
_VServerTotalCompressorContexts_Object = MibScalar
vServerTotalCompressorContexts = _VServerTotalCompressorContexts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1, 5),
    _VServerTotalCompressorContexts_Type()
)
vServerTotalCompressorContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTotalCompressorContexts.setStatus("current")
_VServerUsedCompressorContexts_Type = Integer32
_VServerUsedCompressorContexts_Object = MibScalar
vServerUsedCompressorContexts = _VServerUsedCompressorContexts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1, 6),
    _VServerUsedCompressorContexts_Type()
)
vServerUsedCompressorContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerUsedCompressorContexts.setStatus("current")
_VServerCompressorQueueDepthMax_Type = Integer32
_VServerCompressorQueueDepthMax_Object = MibScalar
vServerCompressorQueueDepthMax = _VServerCompressorQueueDepthMax_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1, 7),
    _VServerCompressorQueueDepthMax_Type()
)
vServerCompressorQueueDepthMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCompressorQueueDepthMax.setStatus("current")
_VServerCompressorQueueDepth_Type = Integer32
_VServerCompressorQueueDepth_Object = MibScalar
vServerCompressorQueueDepth = _VServerCompressorQueueDepth_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1, 8),
    _VServerCompressorQueueDepth_Type()
)
vServerCompressorQueueDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCompressorQueueDepth.setStatus("current")
_VServerCpuUtilization_Type = Gauge32
_VServerCpuUtilization_Object = MibScalar
vServerCpuUtilization = _VServerCpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 1, 9),
    _VServerCpuUtilization_Type()
)
vServerCpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCpuUtilization.setStatus("current")
_VServerStatsSystemTables_ObjectIdentity = ObjectIdentity
vServerStatsSystemTables = _VServerStatsSystemTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 1, 2)
)
_VServerStatsTraffic_ObjectIdentity = ObjectIdentity
vServerStatsTraffic = _VServerStatsTraffic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2)
)
_VServerStatsTrafficScalars_ObjectIdentity = ObjectIdentity
vServerStatsTrafficScalars = _VServerStatsTrafficScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 1)
)
_VServerByteCountReclassification_Type = Counter64
_VServerByteCountReclassification_Object = MibScalar
vServerByteCountReclassification = _VServerByteCountReclassification_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 1, 1),
    _VServerByteCountReclassification_Type()
)
vServerByteCountReclassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerByteCountReclassification.setStatus("current")
_VServerPeriodicClearReclassification_Type = Counter64
_VServerPeriodicClearReclassification_Object = MibScalar
vServerPeriodicClearReclassification = _VServerPeriodicClearReclassification_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 1, 2),
    _VServerPeriodicClearReclassification_Type()
)
vServerPeriodicClearReclassification.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerPeriodicClearReclassification.setStatus("current")
_VServerPeriodicClearBytes_Type = Counter64
_VServerPeriodicClearBytes_Object = MibScalar
vServerPeriodicClearBytes = _VServerPeriodicClearBytes_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 1, 3),
    _VServerPeriodicClearBytes_Type()
)
vServerPeriodicClearBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerPeriodicClearBytes.setStatus("current")
_VServerStatsTrafficTables_ObjectIdentity = ObjectIdentity
vServerStatsTrafficTables = _VServerStatsTrafficTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2)
)
_VServerTrafficTable_Object = MibTable
vServerTrafficTable = _VServerTrafficTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1)
)
if mibBuilder.loadTexts:
    vServerTrafficTable.setStatus("current")
_VServerTrafficEntry_Object = MibTableRow
vServerTrafficEntry = _VServerTrafficEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1)
)
vServerTrafficEntry.setIndexNames(
    (0, "VENTURI-SERVER-STATS-MIB", "vServerTrafficVVSId"),
    (0, "VENTURI-SERVER-STATS-MIB", "vServerTrafficProtocolId"),
)
if mibBuilder.loadTexts:
    vServerTrafficEntry.setStatus("current")


class _VServerTrafficVVSId_Type(Integer32):
    """Custom type vServerTrafficVVSId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VServerTrafficVVSId_Type.__name__ = "Integer32"
_VServerTrafficVVSId_Object = MibTableColumn
vServerTrafficVVSId = _VServerTrafficVVSId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 1),
    _VServerTrafficVVSId_Type()
)
vServerTrafficVVSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficVVSId.setStatus("current")


class _VServerTrafficProtocolId_Type(Integer32):
    """Custom type vServerTrafficProtocolId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_VServerTrafficProtocolId_Type.__name__ = "Integer32"
_VServerTrafficProtocolId_Object = MibTableColumn
vServerTrafficProtocolId = _VServerTrafficProtocolId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 2),
    _VServerTrafficProtocolId_Type()
)
vServerTrafficProtocolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficProtocolId.setStatus("current")
_VServerTrafficVVSTag_Type = OctetString
_VServerTrafficVVSTag_Object = MibTableColumn
vServerTrafficVVSTag = _VServerTrafficVVSTag_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 3),
    _VServerTrafficVVSTag_Type()
)
vServerTrafficVVSTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficVVSTag.setStatus("current")
_VServerTrafficProtocolDescr_Type = OctetString
_VServerTrafficProtocolDescr_Object = MibTableColumn
vServerTrafficProtocolDescr = _VServerTrafficProtocolDescr_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 4),
    _VServerTrafficProtocolDescr_Type()
)
vServerTrafficProtocolDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficProtocolDescr.setStatus("current")
_VServerTrafficFromExternal_Type = Counter64
_VServerTrafficFromExternal_Object = MibTableColumn
vServerTrafficFromExternal = _VServerTrafficFromExternal_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 5),
    _VServerTrafficFromExternal_Type()
)
vServerTrafficFromExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficFromExternal.setStatus("current")
_VServerTrafficToExternal_Type = Counter64
_VServerTrafficToExternal_Object = MibTableColumn
vServerTrafficToExternal = _VServerTrafficToExternal_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 6),
    _VServerTrafficToExternal_Type()
)
vServerTrafficToExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficToExternal.setStatus("current")
_VServerTrafficFromTransport_Type = Counter64
_VServerTrafficFromTransport_Object = MibTableColumn
vServerTrafficFromTransport = _VServerTrafficFromTransport_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 7),
    _VServerTrafficFromTransport_Type()
)
vServerTrafficFromTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficFromTransport.setStatus("current")
_VServerTrafficToTransport_Type = Counter64
_VServerTrafficToTransport_Object = MibTableColumn
vServerTrafficToTransport = _VServerTrafficToTransport_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 8),
    _VServerTrafficToTransport_Type()
)
vServerTrafficToTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficToTransport.setStatus("current")
_VServerTrafficFromClientless_Type = Counter64
_VServerTrafficFromClientless_Object = MibTableColumn
vServerTrafficFromClientless = _VServerTrafficFromClientless_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 9),
    _VServerTrafficFromClientless_Type()
)
vServerTrafficFromClientless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficFromClientless.setStatus("current")
_VServerTrafficToClientless_Type = Counter64
_VServerTrafficToClientless_Object = MibTableColumn
vServerTrafficToClientless = _VServerTrafficToClientless_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 10),
    _VServerTrafficToClientless_Type()
)
vServerTrafficToClientless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficToClientless.setStatus("current")
_VServerTrafficTotalStreamContexts_Type = Counter64
_VServerTrafficTotalStreamContexts_Object = MibTableColumn
vServerTrafficTotalStreamContexts = _VServerTrafficTotalStreamContexts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 11),
    _VServerTrafficTotalStreamContexts_Type()
)
vServerTrafficTotalStreamContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficTotalStreamContexts.setStatus("current")
_VServerTrafficCurStreamContexts_Type = Counter64
_VServerTrafficCurStreamContexts_Object = MibTableColumn
vServerTrafficCurStreamContexts = _VServerTrafficCurStreamContexts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 12),
    _VServerTrafficCurStreamContexts_Type()
)
vServerTrafficCurStreamContexts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficCurStreamContexts.setStatus("current")
_VServerTrafficFromExternalCliented_Type = Counter64
_VServerTrafficFromExternalCliented_Object = MibTableColumn
vServerTrafficFromExternalCliented = _VServerTrafficFromExternalCliented_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 13),
    _VServerTrafficFromExternalCliented_Type()
)
vServerTrafficFromExternalCliented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficFromExternalCliented.setStatus("current")
_VServerTrafficToExternalCliented_Type = Counter64
_VServerTrafficToExternalCliented_Object = MibTableColumn
vServerTrafficToExternalCliented = _VServerTrafficToExternalCliented_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 14),
    _VServerTrafficToExternalCliented_Type()
)
vServerTrafficToExternalCliented.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficToExternalCliented.setStatus("current")
_VServerTrafficFromExternalClientless_Type = Counter64
_VServerTrafficFromExternalClientless_Object = MibTableColumn
vServerTrafficFromExternalClientless = _VServerTrafficFromExternalClientless_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 15),
    _VServerTrafficFromExternalClientless_Type()
)
vServerTrafficFromExternalClientless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficFromExternalClientless.setStatus("current")
_VServerTrafficToExternalClientless_Type = Counter64
_VServerTrafficToExternalClientless_Object = MibTableColumn
vServerTrafficToExternalClientless = _VServerTrafficToExternalClientless_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 2, 2, 1, 1, 16),
    _VServerTrafficToExternalClientless_Type()
)
vServerTrafficToExternalClientless.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTrafficToExternalClientless.setStatus("current")
_VServerStatsTransport_ObjectIdentity = ObjectIdentity
vServerStatsTransport = _VServerStatsTransport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3)
)
_VServerStatsTransportScalars_ObjectIdentity = ObjectIdentity
vServerStatsTransportScalars = _VServerStatsTransportScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 1)
)
_VServerStatsTransportTables_ObjectIdentity = ObjectIdentity
vServerStatsTransportTables = _VServerStatsTransportTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2)
)
_VServerTransportTable_Object = MibTable
vServerTransportTable = _VServerTransportTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1)
)
if mibBuilder.loadTexts:
    vServerTransportTable.setStatus("current")
_VServerTransportEntry_Object = MibTableRow
vServerTransportEntry = _VServerTransportEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1)
)
vServerTransportEntry.setIndexNames(
    (0, "VENTURI-SERVER-STATS-MIB", "vServerTransportVVSId"),
)
if mibBuilder.loadTexts:
    vServerTransportEntry.setStatus("current")


class _VServerTransportVVSId_Type(Integer32):
    """Custom type vServerTransportVVSId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VServerTransportVVSId_Type.__name__ = "Integer32"
_VServerTransportVVSId_Object = MibTableColumn
vServerTransportVVSId = _VServerTransportVVSId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 1),
    _VServerTransportVVSId_Type()
)
vServerTransportVVSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportVVSId.setStatus("current")
_VServerTransportVVSTag_Type = OctetString
_VServerTransportVVSTag_Object = MibTableColumn
vServerTransportVVSTag = _VServerTransportVVSTag_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 2),
    _VServerTransportVVSTag_Type()
)
vServerTransportVVSTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportVVSTag.setStatus("current")
_VServerTransportPacketsSent_Type = Counter64
_VServerTransportPacketsSent_Object = MibTableColumn
vServerTransportPacketsSent = _VServerTransportPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 3),
    _VServerTransportPacketsSent_Type()
)
vServerTransportPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportPacketsSent.setStatus("current")
_VServerTransportPacketsRecd_Type = Counter64
_VServerTransportPacketsRecd_Object = MibTableColumn
vServerTransportPacketsRecd = _VServerTransportPacketsRecd_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 4),
    _VServerTransportPacketsRecd_Type()
)
vServerTransportPacketsRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportPacketsRecd.setStatus("current")
_VServerTransportPacketsRetransmitted_Type = Counter64
_VServerTransportPacketsRetransmitted_Object = MibTableColumn
vServerTransportPacketsRetransmitted = _VServerTransportPacketsRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 5),
    _VServerTransportPacketsRetransmitted_Type()
)
vServerTransportPacketsRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportPacketsRetransmitted.setStatus("current")
_VServerTransportBytesSent_Type = Counter64
_VServerTransportBytesSent_Object = MibTableColumn
vServerTransportBytesSent = _VServerTransportBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 6),
    _VServerTransportBytesSent_Type()
)
vServerTransportBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportBytesSent.setStatus("current")
_VServerTransportBytesRecd_Type = Counter64
_VServerTransportBytesRecd_Object = MibTableColumn
vServerTransportBytesRecd = _VServerTransportBytesRecd_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 7),
    _VServerTransportBytesRecd_Type()
)
vServerTransportBytesRecd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportBytesRecd.setStatus("current")
_VServerTransportBytesRetransmitted_Type = Counter64
_VServerTransportBytesRetransmitted_Object = MibTableColumn
vServerTransportBytesRetransmitted = _VServerTransportBytesRetransmitted_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 8),
    _VServerTransportBytesRetransmitted_Type()
)
vServerTransportBytesRetransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportBytesRetransmitted.setStatus("current")
_VServerTransportUndeliverableToClients_Type = Counter64
_VServerTransportUndeliverableToClients_Object = MibTableColumn
vServerTransportUndeliverableToClients = _VServerTransportUndeliverableToClients_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 9),
    _VServerTransportUndeliverableToClients_Type()
)
vServerTransportUndeliverableToClients.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportUndeliverableToClients.setStatus("current")
_VServerTransportUndeliverableToComp_Type = Counter64
_VServerTransportUndeliverableToComp_Object = MibTableColumn
vServerTransportUndeliverableToComp = _VServerTransportUndeliverableToComp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 10),
    _VServerTransportUndeliverableToComp_Type()
)
vServerTransportUndeliverableToComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportUndeliverableToComp.setStatus("current")
_VServerTransportTotalConnections_Type = Counter64
_VServerTransportTotalConnections_Object = MibTableColumn
vServerTransportTotalConnections = _VServerTransportTotalConnections_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 11),
    _VServerTransportTotalConnections_Type()
)
vServerTransportTotalConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportTotalConnections.setStatus("current")
_VServerTransportFailedConnections_Type = Counter64
_VServerTransportFailedConnections_Object = MibTableColumn
vServerTransportFailedConnections = _VServerTransportFailedConnections_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 12),
    _VServerTransportFailedConnections_Type()
)
vServerTransportFailedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportFailedConnections.setStatus("current")
_VServerTransportCurrentConnections_Type = Counter64
_VServerTransportCurrentConnections_Object = MibTableColumn
vServerTransportCurrentConnections = _VServerTransportCurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 13),
    _VServerTransportCurrentConnections_Type()
)
vServerTransportCurrentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportCurrentConnections.setStatus("current")
_VServerTransportBytesToComp_Type = Counter64
_VServerTransportBytesToComp_Object = MibTableColumn
vServerTransportBytesToComp = _VServerTransportBytesToComp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 14),
    _VServerTransportBytesToComp_Type()
)
vServerTransportBytesToComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportBytesToComp.setStatus("current")
_VServerTransportBytesFromComp_Type = Counter64
_VServerTransportBytesFromComp_Object = MibTableColumn
vServerTransportBytesFromComp = _VServerTransportBytesFromComp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 3, 2, 1, 1, 15),
    _VServerTransportBytesFromComp_Type()
)
vServerTransportBytesFromComp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerTransportBytesFromComp.setStatus("current")
_VServerStatsSubscriber_ObjectIdentity = ObjectIdentity
vServerStatsSubscriber = _VServerStatsSubscriber_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4)
)
_VServerStatsSubscriberScalars_ObjectIdentity = ObjectIdentity
vServerStatsSubscriberScalars = _VServerStatsSubscriberScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 1)
)
_VServerClientLimitExceeded_Type = Counter64
_VServerClientLimitExceeded_Object = MibScalar
vServerClientLimitExceeded = _VServerClientLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 1, 1),
    _VServerClientLimitExceeded_Type()
)
vServerClientLimitExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientLimitExceeded.setStatus("current")
_VServerClientlessLimitExceeded_Type = Counter64
_VServerClientlessLimitExceeded_Object = MibScalar
vServerClientlessLimitExceeded = _VServerClientlessLimitExceeded_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 1, 2),
    _VServerClientlessLimitExceeded_Type()
)
vServerClientlessLimitExceeded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientlessLimitExceeded.setStatus("current")
_VServerStatsSubscriberTables_ObjectIdentity = ObjectIdentity
vServerStatsSubscriberTables = _VServerStatsSubscriberTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2)
)
_VServerSubscriberUsageTable_Object = MibTable
vServerSubscriberUsageTable = _VServerSubscriberUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1)
)
if mibBuilder.loadTexts:
    vServerSubscriberUsageTable.setStatus("current")
_VServerSubscriberUsageEntry_Object = MibTableRow
vServerSubscriberUsageEntry = _VServerSubscriberUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1)
)
vServerSubscriberUsageEntry.setIndexNames(
    (0, "VENTURI-SERVER-STATS-MIB", "vServerSubscriberType"),
    (0, "VENTURI-SERVER-STATS-MIB", "vServerSubscriberVVSId"),
)
if mibBuilder.loadTexts:
    vServerSubscriberUsageEntry.setStatus("current")
_VServerSubscriberType_Type = VenturiSubscriberType
_VServerSubscriberType_Object = MibTableColumn
vServerSubscriberType = _VServerSubscriberType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 1),
    _VServerSubscriberType_Type()
)
vServerSubscriberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberType.setStatus("current")


class _VServerSubscriberVVSId_Type(Integer32):
    """Custom type vServerSubscriberVVSId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_VServerSubscriberVVSId_Type.__name__ = "Integer32"
_VServerSubscriberVVSId_Object = MibTableColumn
vServerSubscriberVVSId = _VServerSubscriberVVSId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 2),
    _VServerSubscriberVVSId_Type()
)
vServerSubscriberVVSId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberVVSId.setStatus("current")
_VServerSubscriberVVSTag_Type = OctetString
_VServerSubscriberVVSTag_Object = MibTableColumn
vServerSubscriberVVSTag = _VServerSubscriberVVSTag_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 3),
    _VServerSubscriberVVSTag_Type()
)
vServerSubscriberVVSTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberVVSTag.setStatus("current")
_VServerSubscriberTotalCount_Type = Counter64
_VServerSubscriberTotalCount_Object = MibTableColumn
vServerSubscriberTotalCount = _VServerSubscriberTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 4),
    _VServerSubscriberTotalCount_Type()
)
vServerSubscriberTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberTotalCount.setStatus("current")
_VServerSubscriberCurrCount_Type = Gauge32
_VServerSubscriberCurrCount_Object = MibTableColumn
vServerSubscriberCurrCount = _VServerSubscriberCurrCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 5),
    _VServerSubscriberCurrCount_Type()
)
vServerSubscriberCurrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberCurrCount.setStatus("current")
_VServerSubscriberAuthenticationFailures_Type = Counter64
_VServerSubscriberAuthenticationFailures_Object = MibTableColumn
vServerSubscriberAuthenticationFailures = _VServerSubscriberAuthenticationFailures_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 6),
    _VServerSubscriberAuthenticationFailures_Type()
)
vServerSubscriberAuthenticationFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberAuthenticationFailures.setStatus("current")
_VServerSubscriberAbortedConnections_Type = Counter64
_VServerSubscriberAbortedConnections_Object = MibTableColumn
vServerSubscriberAbortedConnections = _VServerSubscriberAbortedConnections_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 7),
    _VServerSubscriberAbortedConnections_Type()
)
vServerSubscriberAbortedConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberAbortedConnections.setStatus("current")
_VServerSubscriberReassignmentFailures_Type = Counter64
_VServerSubscriberReassignmentFailures_Object = MibTableColumn
vServerSubscriberReassignmentFailures = _VServerSubscriberReassignmentFailures_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 8),
    _VServerSubscriberReassignmentFailures_Type()
)
vServerSubscriberReassignmentFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberReassignmentFailures.setStatus("current")
_VServerSubscriberStandbyCount_Type = Counter64
_VServerSubscriberStandbyCount_Object = MibTableColumn
vServerSubscriberStandbyCount = _VServerSubscriberStandbyCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 9),
    _VServerSubscriberStandbyCount_Type()
)
vServerSubscriberStandbyCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberStandbyCount.setStatus("current")
_VServerSubscriberInactiveCount_Type = Counter64
_VServerSubscriberInactiveCount_Object = MibTableColumn
vServerSubscriberInactiveCount = _VServerSubscriberInactiveCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 10),
    _VServerSubscriberInactiveCount_Type()
)
vServerSubscriberInactiveCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberInactiveCount.setStatus("current")
_VServerSubscriberReassignmentCount_Type = Counter64
_VServerSubscriberReassignmentCount_Object = MibTableColumn
vServerSubscriberReassignmentCount = _VServerSubscriberReassignmentCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 11),
    _VServerSubscriberReassignmentCount_Type()
)
vServerSubscriberReassignmentCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberReassignmentCount.setStatus("current")
_VServerSubscriberByteCount_Type = Counter64
_VServerSubscriberByteCount_Object = MibTableColumn
vServerSubscriberByteCount = _VServerSubscriberByteCount_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 1, 1, 12),
    _VServerSubscriberByteCount_Type()
)
vServerSubscriberByteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberByteCount.setStatus("current")
_VServerSubscriberClientTable_Object = MibTable
vServerSubscriberClientTable = _VServerSubscriberClientTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2)
)
if mibBuilder.loadTexts:
    vServerSubscriberClientTable.setStatus("current")
_VServerSubscriberClientEntry_Object = MibTableRow
vServerSubscriberClientEntry = _VServerSubscriberClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1)
)
vServerSubscriberClientEntry.setIndexNames(
    (0, "VENTURI-SERVER-STATS-MIB", "vServerSubscriberClientRowId"),
)
if mibBuilder.loadTexts:
    vServerSubscriberClientEntry.setStatus("current")
_VServerSubscriberClientRowId_Type = Unsigned32
_VServerSubscriberClientRowId_Object = MibTableColumn
vServerSubscriberClientRowId = _VServerSubscriberClientRowId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 1),
    _VServerSubscriberClientRowId_Type()
)
vServerSubscriberClientRowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vServerSubscriberClientRowId.setStatus("current")
_VServerSubscriberClientUniqueId_Type = DisplayString
_VServerSubscriberClientUniqueId_Object = MibTableColumn
vServerSubscriberClientUniqueId = _VServerSubscriberClientUniqueId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 2),
    _VServerSubscriberClientUniqueId_Type()
)
vServerSubscriberClientUniqueId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientUniqueId.setStatus("current")
_VServerSubscriberClientIPAddress_Type = IpAddress
_VServerSubscriberClientIPAddress_Object = MibTableColumn
vServerSubscriberClientIPAddress = _VServerSubscriberClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 3),
    _VServerSubscriberClientIPAddress_Type()
)
vServerSubscriberClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientIPAddress.setStatus("current")
_VServerSubscriberClientVersion_Type = DisplayString
_VServerSubscriberClientVersion_Object = MibTableColumn
vServerSubscriberClientVersion = _VServerSubscriberClientVersion_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 4),
    _VServerSubscriberClientVersion_Type()
)
vServerSubscriberClientVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVersion.setStatus("current")
_VServerSubscriberClientLastAccessTime_Type = Integer32
_VServerSubscriberClientLastAccessTime_Object = MibTableColumn
vServerSubscriberClientLastAccessTime = _VServerSubscriberClientLastAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 5),
    _VServerSubscriberClientLastAccessTime_Type()
)
vServerSubscriberClientLastAccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientLastAccessTime.setStatus("current")
_VServerSubscriberClientTransportConnections_Type = Integer32
_VServerSubscriberClientTransportConnections_Object = MibTableColumn
vServerSubscriberClientTransportConnections = _VServerSubscriberClientTransportConnections_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 6),
    _VServerSubscriberClientTransportConnections_Type()
)
vServerSubscriberClientTransportConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientTransportConnections.setStatus("current")
_VServerSubscriberClientVVSTag_Type = DisplayString
_VServerSubscriberClientVVSTag_Object = MibTableColumn
vServerSubscriberClientVVSTag = _VServerSubscriberClientVVSTag_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 7),
    _VServerSubscriberClientVVSTag_Type()
)
vServerSubscriberClientVVSTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVVSTag.setStatus("current")
_VServerSubscriberClientUserInfo_Type = DisplayString
_VServerSubscriberClientUserInfo_Object = MibTableColumn
vServerSubscriberClientUserInfo = _VServerSubscriberClientUserInfo_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 8),
    _VServerSubscriberClientUserInfo_Type()
)
vServerSubscriberClientUserInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientUserInfo.setStatus("current")
_VServerSubscriberClientConnType_Type = DisplayString
_VServerSubscriberClientConnType_Object = MibTableColumn
vServerSubscriberClientConnType = _VServerSubscriberClientConnType_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 9),
    _VServerSubscriberClientConnType_Type()
)
vServerSubscriberClientConnType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientConnType.setStatus("current")
_VServerSubscriberClientOS_Type = DisplayString
_VServerSubscriberClientOS_Object = MibTableColumn
vServerSubscriberClientOS = _VServerSubscriberClientOS_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 10),
    _VServerSubscriberClientOS_Type()
)
vServerSubscriberClientOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientOS.setStatus("current")
_VServerSubscriberClientMAC_Type = DisplayString
_VServerSubscriberClientMAC_Object = MibTableColumn
vServerSubscriberClientMAC = _VServerSubscriberClientMAC_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 11),
    _VServerSubscriberClientMAC_Type()
)
vServerSubscriberClientMAC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientMAC.setStatus("current")
_VServerSubscriberClientPhone_Type = DisplayString
_VServerSubscriberClientPhone_Object = MibTableColumn
vServerSubscriberClientPhone = _VServerSubscriberClientPhone_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 12),
    _VServerSubscriberClientPhone_Type()
)
vServerSubscriberClientPhone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientPhone.setStatus("current")
_VServerSubscriberClientConnDuration_Type = TimeTicks
_VServerSubscriberClientConnDuration_Object = MibTableColumn
vServerSubscriberClientConnDuration = _VServerSubscriberClientConnDuration_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 13),
    _VServerSubscriberClientConnDuration_Type()
)
vServerSubscriberClientConnDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientConnDuration.setStatus("current")
_VServerSubscriberClientVTPPktsSent_Type = Counter64
_VServerSubscriberClientVTPPktsSent_Object = MibTableColumn
vServerSubscriberClientVTPPktsSent = _VServerSubscriberClientVTPPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 14),
    _VServerSubscriberClientVTPPktsSent_Type()
)
vServerSubscriberClientVTPPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPPktsSent.setStatus("current")
_VServerSubscriberClientVTPPktsRcvd_Type = Counter64
_VServerSubscriberClientVTPPktsRcvd_Object = MibTableColumn
vServerSubscriberClientVTPPktsRcvd = _VServerSubscriberClientVTPPktsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 15),
    _VServerSubscriberClientVTPPktsRcvd_Type()
)
vServerSubscriberClientVTPPktsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPPktsRcvd.setStatus("current")
_VServerSubscriberClientVTPBytesSent_Type = Counter64
_VServerSubscriberClientVTPBytesSent_Object = MibTableColumn
vServerSubscriberClientVTPBytesSent = _VServerSubscriberClientVTPBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 16),
    _VServerSubscriberClientVTPBytesSent_Type()
)
vServerSubscriberClientVTPBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPBytesSent.setStatus("current")
_VServerSubscriberClientVTPBytesRcvd_Type = Counter64
_VServerSubscriberClientVTPBytesRcvd_Object = MibTableColumn
vServerSubscriberClientVTPBytesRcvd = _VServerSubscriberClientVTPBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 17),
    _VServerSubscriberClientVTPBytesRcvd_Type()
)
vServerSubscriberClientVTPBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPBytesRcvd.setStatus("current")
_VServerSubscriberClientVTPDropPkts_Type = Counter64
_VServerSubscriberClientVTPDropPkts_Object = MibTableColumn
vServerSubscriberClientVTPDropPkts = _VServerSubscriberClientVTPDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 18),
    _VServerSubscriberClientVTPDropPkts_Type()
)
vServerSubscriberClientVTPDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPDropPkts.setStatus("current")
_VServerSubscriberClientVTPReXmitPkts_Type = Counter64
_VServerSubscriberClientVTPReXmitPkts_Object = MibTableColumn
vServerSubscriberClientVTPReXmitPkts = _VServerSubscriberClientVTPReXmitPkts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 19),
    _VServerSubscriberClientVTPReXmitPkts_Type()
)
vServerSubscriberClientVTPReXmitPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPReXmitPkts.setStatus("current")
_VServerSubscriberClientVTPErrorPkts_Type = Counter64
_VServerSubscriberClientVTPErrorPkts_Object = MibTableColumn
vServerSubscriberClientVTPErrorPkts = _VServerSubscriberClientVTPErrorPkts_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 20),
    _VServerSubscriberClientVTPErrorPkts_Type()
)
vServerSubscriberClientVTPErrorPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPErrorPkts.setStatus("current")
_VServerSubscriberClientVTPBWToClient_Type = Counter32
_VServerSubscriberClientVTPBWToClient_Object = MibTableColumn
vServerSubscriberClientVTPBWToClient = _VServerSubscriberClientVTPBWToClient_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 21),
    _VServerSubscriberClientVTPBWToClient_Type()
)
vServerSubscriberClientVTPBWToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPBWToClient.setStatus("current")
_VServerSubscriberClientVTPBWFromClient_Type = Counter32
_VServerSubscriberClientVTPBWFromClient_Object = MibTableColumn
vServerSubscriberClientVTPBWFromClient = _VServerSubscriberClientVTPBWFromClient_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 22),
    _VServerSubscriberClientVTPBWFromClient_Type()
)
vServerSubscriberClientVTPBWFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPBWFromClient.setStatus("current")
_VServerSubscriberClientFromExternal_Type = Counter64
_VServerSubscriberClientFromExternal_Object = MibTableColumn
vServerSubscriberClientFromExternal = _VServerSubscriberClientFromExternal_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 23),
    _VServerSubscriberClientFromExternal_Type()
)
vServerSubscriberClientFromExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientFromExternal.setStatus("current")
_VServerSubscriberClientToExternal_Type = Counter64
_VServerSubscriberClientToExternal_Object = MibTableColumn
vServerSubscriberClientToExternal = _VServerSubscriberClientToExternal_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 24),
    _VServerSubscriberClientToExternal_Type()
)
vServerSubscriberClientToExternal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientToExternal.setStatus("current")
_VServerSubscriberClientFromTransport_Type = Counter64
_VServerSubscriberClientFromTransport_Object = MibTableColumn
vServerSubscriberClientFromTransport = _VServerSubscriberClientFromTransport_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 25),
    _VServerSubscriberClientFromTransport_Type()
)
vServerSubscriberClientFromTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientFromTransport.setStatus("current")
_VServerSubscriberClientToTransport_Type = Counter64
_VServerSubscriberClientToTransport_Object = MibTableColumn
vServerSubscriberClientToTransport = _VServerSubscriberClientToTransport_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 26),
    _VServerSubscriberClientToTransport_Type()
)
vServerSubscriberClientToTransport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientToTransport.setStatus("current")


class _VServerSubscriberClientRTT_Type(Integer32):
    """Custom type vServerSubscriberClientRTT based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VServerSubscriberClientRTT_Type.__name__ = "Integer32"
_VServerSubscriberClientRTT_Object = MibTableColumn
vServerSubscriberClientRTT = _VServerSubscriberClientRTT_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 27),
    _VServerSubscriberClientRTT_Type()
)
vServerSubscriberClientRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientRTT.setStatus("current")
if mibBuilder.loadTexts:
    vServerSubscriberClientRTT.setUnits("milliseconds")
_VServerSubscriberClientVTPReXmitBytes_Type = Counter64
_VServerSubscriberClientVTPReXmitBytes_Object = MibTableColumn
vServerSubscriberClientVTPReXmitBytes = _VServerSubscriberClientVTPReXmitBytes_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 2, 1, 28),
    _VServerSubscriberClientVTPReXmitBytes_Type()
)
vServerSubscriberClientVTPReXmitBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientVTPReXmitBytes.setStatus("current")
_VServerSubscriberClientlessTable_Object = MibTable
vServerSubscriberClientlessTable = _VServerSubscriberClientlessTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 3)
)
if mibBuilder.loadTexts:
    vServerSubscriberClientlessTable.setStatus("current")
_VServerSubscriberClientlessEntry_Object = MibTableRow
vServerSubscriberClientlessEntry = _VServerSubscriberClientlessEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 3, 1)
)
vServerSubscriberClientlessEntry.setIndexNames(
    (0, "VENTURI-SERVER-STATS-MIB", "vServerSubscriberClientlessRowId"),
)
if mibBuilder.loadTexts:
    vServerSubscriberClientlessEntry.setStatus("current")
_VServerSubscriberClientlessRowId_Type = Unsigned32
_VServerSubscriberClientlessRowId_Object = MibTableColumn
vServerSubscriberClientlessRowId = _VServerSubscriberClientlessRowId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 3, 1, 1),
    _VServerSubscriberClientlessRowId_Type()
)
vServerSubscriberClientlessRowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vServerSubscriberClientlessRowId.setStatus("current")
_VServerSubscriberClientlessIPAddress_Type = IpAddress
_VServerSubscriberClientlessIPAddress_Object = MibTableColumn
vServerSubscriberClientlessIPAddress = _VServerSubscriberClientlessIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 3, 1, 2),
    _VServerSubscriberClientlessIPAddress_Type()
)
vServerSubscriberClientlessIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientlessIPAddress.setStatus("current")
_VServerSubscriberClientlessLastAccessTime_Type = Integer32
_VServerSubscriberClientlessLastAccessTime_Object = MibTableColumn
vServerSubscriberClientlessLastAccessTime = _VServerSubscriberClientlessLastAccessTime_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 3, 1, 3),
    _VServerSubscriberClientlessLastAccessTime_Type()
)
vServerSubscriberClientlessLastAccessTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientlessLastAccessTime.setStatus("current")
_VServerSubscriberClientlessTransportConnections_Type = Integer32
_VServerSubscriberClientlessTransportConnections_Object = MibTableColumn
vServerSubscriberClientlessTransportConnections = _VServerSubscriberClientlessTransportConnections_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 3, 1, 4),
    _VServerSubscriberClientlessTransportConnections_Type()
)
vServerSubscriberClientlessTransportConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientlessTransportConnections.setStatus("current")
_VServerSubscriberClientlessVVSTag_Type = DisplayString
_VServerSubscriberClientlessVVSTag_Object = MibTableColumn
vServerSubscriberClientlessVVSTag = _VServerSubscriberClientlessVVSTag_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 3, 1, 5),
    _VServerSubscriberClientlessVVSTag_Type()
)
vServerSubscriberClientlessVVSTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerSubscriberClientlessVVSTag.setStatus("current")
_VServerAbbreviatedSubscriberClientTable_Object = MibTable
vServerAbbreviatedSubscriberClientTable = _VServerAbbreviatedSubscriberClientTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 4)
)
if mibBuilder.loadTexts:
    vServerAbbreviatedSubscriberClientTable.setStatus("current")
_VServerAbbreviatedSubscriberClientEntry_Object = MibTableRow
vServerAbbreviatedSubscriberClientEntry = _VServerAbbreviatedSubscriberClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 4, 1)
)
vServerAbbreviatedSubscriberClientEntry.setIndexNames(
    (0, "VENTURI-SERVER-STATS-MIB", "vServerAbbreviatedSubscriberClientRowId"),
)
if mibBuilder.loadTexts:
    vServerAbbreviatedSubscriberClientEntry.setStatus("current")
_VServerAbbreviatedSubscriberClientRowId_Type = Unsigned32
_VServerAbbreviatedSubscriberClientRowId_Object = MibTableColumn
vServerAbbreviatedSubscriberClientRowId = _VServerAbbreviatedSubscriberClientRowId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 4, 1, 1),
    _VServerAbbreviatedSubscriberClientRowId_Type()
)
vServerAbbreviatedSubscriberClientRowId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vServerAbbreviatedSubscriberClientRowId.setStatus("current")
_VServerAbbreviatedSubscriberClientIPAddress_Type = IpAddress
_VServerAbbreviatedSubscriberClientIPAddress_Object = MibTableColumn
vServerAbbreviatedSubscriberClientIPAddress = _VServerAbbreviatedSubscriberClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 4, 1, 2),
    _VServerAbbreviatedSubscriberClientIPAddress_Type()
)
vServerAbbreviatedSubscriberClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAbbreviatedSubscriberClientIPAddress.setStatus("current")
_VServerAbbreviatedSubscriberClientVTPBWToClient_Type = Unsigned32
_VServerAbbreviatedSubscriberClientVTPBWToClient_Object = MibTableColumn
vServerAbbreviatedSubscriberClientVTPBWToClient = _VServerAbbreviatedSubscriberClientVTPBWToClient_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 4, 1, 3),
    _VServerAbbreviatedSubscriberClientVTPBWToClient_Type()
)
vServerAbbreviatedSubscriberClientVTPBWToClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAbbreviatedSubscriberClientVTPBWToClient.setStatus("current")
_VServerAbbreviatedSubscriberClientVTPBWFromClient_Type = Unsigned32
_VServerAbbreviatedSubscriberClientVTPBWFromClient_Object = MibTableColumn
vServerAbbreviatedSubscriberClientVTPBWFromClient = _VServerAbbreviatedSubscriberClientVTPBWFromClient_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 4, 1, 4),
    _VServerAbbreviatedSubscriberClientVTPBWFromClient_Type()
)
vServerAbbreviatedSubscriberClientVTPBWFromClient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAbbreviatedSubscriberClientVTPBWFromClient.setStatus("current")


class _VServerAbbreviatedSubscriberClientRTT_Type(Unsigned32):
    """Custom type vServerAbbreviatedSubscriberClientRTT based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VServerAbbreviatedSubscriberClientRTT_Type.__name__ = "Unsigned32"
_VServerAbbreviatedSubscriberClientRTT_Object = MibTableColumn
vServerAbbreviatedSubscriberClientRTT = _VServerAbbreviatedSubscriberClientRTT_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 4, 1, 5),
    _VServerAbbreviatedSubscriberClientRTT_Type()
)
vServerAbbreviatedSubscriberClientRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerAbbreviatedSubscriberClientRTT.setStatus("current")
if mibBuilder.loadTexts:
    vServerAbbreviatedSubscriberClientRTT.setUnits("milliseconds")
_VServerClientInfoTable_Object = MibTable
vServerClientInfoTable = _VServerClientInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5)
)
if mibBuilder.loadTexts:
    vServerClientInfoTable.setStatus("current")
_VServerClientInfoEntry_Object = MibTableRow
vServerClientInfoEntry = _VServerClientInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1)
)
vServerClientInfoEntry.setIndexNames(
    (0, "VENTURI-SERVER-STATS-MIB", "vServerClientInfoRowId"),
)
if mibBuilder.loadTexts:
    vServerClientInfoEntry.setStatus("current")
_VServerClientInfoRowId_Type = Unsigned32
_VServerClientInfoRowId_Object = MibTableColumn
vServerClientInfoRowId = _VServerClientInfoRowId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 1),
    _VServerClientInfoRowId_Type()
)
vServerClientInfoRowId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoRowId.setStatus("current")
_VServerClientInfoClientId_Type = DisplayString
_VServerClientInfoClientId_Object = MibTableColumn
vServerClientInfoClientId = _VServerClientInfoClientId_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 2),
    _VServerClientInfoClientId_Type()
)
vServerClientInfoClientId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoClientId.setStatus("current")
_VServerClientInfoRemoteIp_Type = IpAddress
_VServerClientInfoRemoteIp_Object = MibTableColumn
vServerClientInfoRemoteIp = _VServerClientInfoRemoteIp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 3),
    _VServerClientInfoRemoteIp_Type()
)
vServerClientInfoRemoteIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoRemoteIp.setStatus("current")
_VServerClientInfoSubIp_Type = IpAddress
_VServerClientInfoSubIp_Object = MibTableColumn
vServerClientInfoSubIp = _VServerClientInfoSubIp_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 4),
    _VServerClientInfoSubIp_Type()
)
vServerClientInfoSubIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoSubIp.setStatus("current")
_VServerClientInfoActVC_Type = Counter64
_VServerClientInfoActVC_Object = MibTableColumn
vServerClientInfoActVC = _VServerClientInfoActVC_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 5),
    _VServerClientInfoActVC_Type()
)
vServerClientInfoActVC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoActVC.setStatus("current")
_VServerClientInfoBytesSent_Type = Counter64
_VServerClientInfoBytesSent_Object = MibTableColumn
vServerClientInfoBytesSent = _VServerClientInfoBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 6),
    _VServerClientInfoBytesSent_Type()
)
vServerClientInfoBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoBytesSent.setStatus("current")
_VServerClientInfoBytesRcvd_Type = Counter64
_VServerClientInfoBytesRcvd_Object = MibTableColumn
vServerClientInfoBytesRcvd = _VServerClientInfoBytesRcvd_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 7),
    _VServerClientInfoBytesRcvd_Type()
)
vServerClientInfoBytesRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoBytesRcvd.setStatus("current")
_VServerClientInfoXmitRate_Type = Counter64
_VServerClientInfoXmitRate_Object = MibTableColumn
vServerClientInfoXmitRate = _VServerClientInfoXmitRate_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 8),
    _VServerClientInfoXmitRate_Type()
)
vServerClientInfoXmitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoXmitRate.setStatus("current")
_VServerClientInfoRecvRate_Type = Counter64
_VServerClientInfoRecvRate_Object = MibTableColumn
vServerClientInfoRecvRate = _VServerClientInfoRecvRate_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 9),
    _VServerClientInfoRecvRate_Type()
)
vServerClientInfoRecvRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoRecvRate.setStatus("current")
_VServerClientInfoRTT_Type = Counter64
_VServerClientInfoRTT_Object = MibTableColumn
vServerClientInfoRTT = _VServerClientInfoRTT_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 10),
    _VServerClientInfoRTT_Type()
)
vServerClientInfoRTT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoRTT.setStatus("current")
_VServerClientInfoNSub_Type = Counter64
_VServerClientInfoNSub_Object = MibTableColumn
vServerClientInfoNSub = _VServerClientInfoNSub_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 11),
    _VServerClientInfoNSub_Type()
)
vServerClientInfoNSub.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoNSub.setStatus("current")
_VServerClientInfoFsc_Type = OctetString
_VServerClientInfoFsc_Object = MibTableColumn
vServerClientInfoFsc = _VServerClientInfoFsc_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 12),
    _VServerClientInfoFsc_Type()
)
vServerClientInfoFsc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoFsc.setStatus("current")
_VServerClientInfoScale0_Type = OctetString
_VServerClientInfoScale0_Object = MibTableColumn
vServerClientInfoScale0 = _VServerClientInfoScale0_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 13),
    _VServerClientInfoScale0_Type()
)
vServerClientInfoScale0.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoScale0.setStatus("current")
_VServerClientInfoScale1_Type = OctetString
_VServerClientInfoScale1_Object = MibTableColumn
vServerClientInfoScale1 = _VServerClientInfoScale1_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 14),
    _VServerClientInfoScale1_Type()
)
vServerClientInfoScale1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoScale1.setStatus("current")
_VServerClientInfoScale2_Type = OctetString
_VServerClientInfoScale2_Object = MibTableColumn
vServerClientInfoScale2 = _VServerClientInfoScale2_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 15),
    _VServerClientInfoScale2_Type()
)
vServerClientInfoScale2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoScale2.setStatus("current")
_VServerClientInfoScale3_Type = OctetString
_VServerClientInfoScale3_Object = MibTableColumn
vServerClientInfoScale3 = _VServerClientInfoScale3_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 4, 2, 5, 1, 16),
    _VServerClientInfoScale3_Type()
)
vServerClientInfoScale3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerClientInfoScale3.setStatus("current")
_VServerStatsCapacity_ObjectIdentity = ObjectIdentity
vServerStatsCapacity = _VServerStatsCapacity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 5)
)
_VServerStatsCapacityScalars_ObjectIdentity = ObjectIdentity
vServerStatsCapacityScalars = _VServerStatsCapacityScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 5, 1)
)
_VServerCapacityPeakPeriod_Type = Integer32
_VServerCapacityPeakPeriod_Object = MibScalar
vServerCapacityPeakPeriod = _VServerCapacityPeakPeriod_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 5, 1, 1),
    _VServerCapacityPeakPeriod_Type()
)
vServerCapacityPeakPeriod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCapacityPeakPeriod.setStatus("current")
_VServerCapacityLoad_Type = Counter64
_VServerCapacityLoad_Object = MibScalar
vServerCapacityLoad = _VServerCapacityLoad_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 5, 1, 2),
    _VServerCapacityLoad_Type()
)
vServerCapacityLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerCapacityLoad.setStatus("current")
_VServerStatsCapacityTables_ObjectIdentity = ObjectIdentity
vServerStatsCapacityTables = _VServerStatsCapacityTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 5, 2)
)
_VServerStatsHealthcheck_ObjectIdentity = ObjectIdentity
vServerStatsHealthcheck = _VServerStatsHealthcheck_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 6)
)
_VServerStatsHealthcheckScalars_ObjectIdentity = ObjectIdentity
vServerStatsHealthcheckScalars = _VServerStatsHealthcheckScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 6, 1)
)
_VServerStatsHealthcheckClientless_ObjectIdentity = ObjectIdentity
vServerStatsHealthcheckClientless = _VServerStatsHealthcheckClientless_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 6, 1, 1)
)
_VServerHealthcheckClientlessRate_Type = Gauge32
_VServerHealthcheckClientlessRate_Object = MibScalar
vServerHealthcheckClientlessRate = _VServerHealthcheckClientlessRate_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 6, 1, 1, 1),
    _VServerHealthcheckClientlessRate_Type()
)
vServerHealthcheckClientlessRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerHealthcheckClientlessRate.setStatus("current")
_VServerHealthcheckClientlessFlow_Type = Gauge32
_VServerHealthcheckClientlessFlow_Object = MibScalar
vServerHealthcheckClientlessFlow = _VServerHealthcheckClientlessFlow_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 6, 1, 1, 2),
    _VServerHealthcheckClientlessFlow_Type()
)
vServerHealthcheckClientlessFlow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerHealthcheckClientlessFlow.setStatus("current")
_VServerStatsHealthcheckCliented_ObjectIdentity = ObjectIdentity
vServerStatsHealthcheckCliented = _VServerStatsHealthcheckCliented_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 6, 1, 2)
)
_VServerHealthcheckClientedRate_Type = Gauge32
_VServerHealthcheckClientedRate_Object = MibScalar
vServerHealthcheckClientedRate = _VServerHealthcheckClientedRate_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 6, 1, 2, 1),
    _VServerHealthcheckClientedRate_Type()
)
vServerHealthcheckClientedRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerHealthcheckClientedRate.setStatus("current")
_VServerStatsHealthcheckTables_ObjectIdentity = ObjectIdentity
vServerStatsHealthcheckTables = _VServerStatsHealthcheckTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 6, 2)
)
_VServerStatsPerfGraph_ObjectIdentity = ObjectIdentity
vServerStatsPerfGraph = _VServerStatsPerfGraph_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 7)
)
_VServerStatsPerfGraphScalars_ObjectIdentity = ObjectIdentity
vServerStatsPerfGraphScalars = _VServerStatsPerfGraphScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 7, 1)
)
_VServerStatsDirectInBytes_Type = Counter64
_VServerStatsDirectInBytes_Object = MibScalar
vServerStatsDirectInBytes = _VServerStatsDirectInBytes_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 7, 1, 1),
    _VServerStatsDirectInBytes_Type()
)
vServerStatsDirectInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStatsDirectInBytes.setStatus("current")
_VServerStatsProxyInBytes_Type = Counter64
_VServerStatsProxyInBytes_Object = MibScalar
vServerStatsProxyInBytes = _VServerStatsProxyInBytes_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 7, 1, 2),
    _VServerStatsProxyInBytes_Type()
)
vServerStatsProxyInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStatsProxyInBytes.setStatus("current")
_VServerStatsUncompressedCacheInBytes_Type = Counter64
_VServerStatsUncompressedCacheInBytes_Object = MibScalar
vServerStatsUncompressedCacheInBytes = _VServerStatsUncompressedCacheInBytes_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 7, 1, 3),
    _VServerStatsUncompressedCacheInBytes_Type()
)
vServerStatsUncompressedCacheInBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStatsUncompressedCacheInBytes.setStatus("current")
_VServerStatsSubscriberOutBytes_Type = Counter64
_VServerStatsSubscriberOutBytes_Object = MibScalar
vServerStatsSubscriberOutBytes = _VServerStatsSubscriberOutBytes_Object(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 7, 1, 4),
    _VServerStatsSubscriberOutBytes_Type()
)
vServerStatsSubscriberOutBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vServerStatsSubscriberOutBytes.setStatus("current")
_VServerStatsPerfGraphTables_ObjectIdentity = ObjectIdentity
vServerStatsPerfGraphTables = _VServerStatsPerfGraphTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3382, 12, 1, 3, 7, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "VENTURI-SERVER-STATS-MIB",
    **{"vServerStatistics": vServerStatistics,
       "vServerStatsSystem": vServerStatsSystem,
       "vServerStatsSystemScalars": vServerStatsSystemScalars,
       "vServerSystemTotalVenturiBuffers": vServerSystemTotalVenturiBuffers,
       "vServerStatsSystemUsedVenturiBuffers": vServerStatsSystemUsedVenturiBuffers,
       "vServerTotalStreamContexts": vServerTotalStreamContexts,
       "vServerUsedStreamContexts": vServerUsedStreamContexts,
       "vServerTotalCompressorContexts": vServerTotalCompressorContexts,
       "vServerUsedCompressorContexts": vServerUsedCompressorContexts,
       "vServerCompressorQueueDepthMax": vServerCompressorQueueDepthMax,
       "vServerCompressorQueueDepth": vServerCompressorQueueDepth,
       "vServerCpuUtilization": vServerCpuUtilization,
       "vServerStatsSystemTables": vServerStatsSystemTables,
       "vServerStatsTraffic": vServerStatsTraffic,
       "vServerStatsTrafficScalars": vServerStatsTrafficScalars,
       "vServerByteCountReclassification": vServerByteCountReclassification,
       "vServerPeriodicClearReclassification": vServerPeriodicClearReclassification,
       "vServerPeriodicClearBytes": vServerPeriodicClearBytes,
       "vServerStatsTrafficTables": vServerStatsTrafficTables,
       "vServerTrafficTable": vServerTrafficTable,
       "vServerTrafficEntry": vServerTrafficEntry,
       "vServerTrafficVVSId": vServerTrafficVVSId,
       "vServerTrafficProtocolId": vServerTrafficProtocolId,
       "vServerTrafficVVSTag": vServerTrafficVVSTag,
       "vServerTrafficProtocolDescr": vServerTrafficProtocolDescr,
       "vServerTrafficFromExternal": vServerTrafficFromExternal,
       "vServerTrafficToExternal": vServerTrafficToExternal,
       "vServerTrafficFromTransport": vServerTrafficFromTransport,
       "vServerTrafficToTransport": vServerTrafficToTransport,
       "vServerTrafficFromClientless": vServerTrafficFromClientless,
       "vServerTrafficToClientless": vServerTrafficToClientless,
       "vServerTrafficTotalStreamContexts": vServerTrafficTotalStreamContexts,
       "vServerTrafficCurStreamContexts": vServerTrafficCurStreamContexts,
       "vServerTrafficFromExternalCliented": vServerTrafficFromExternalCliented,
       "vServerTrafficToExternalCliented": vServerTrafficToExternalCliented,
       "vServerTrafficFromExternalClientless": vServerTrafficFromExternalClientless,
       "vServerTrafficToExternalClientless": vServerTrafficToExternalClientless,
       "vServerStatsTransport": vServerStatsTransport,
       "vServerStatsTransportScalars": vServerStatsTransportScalars,
       "vServerStatsTransportTables": vServerStatsTransportTables,
       "vServerTransportTable": vServerTransportTable,
       "vServerTransportEntry": vServerTransportEntry,
       "vServerTransportVVSId": vServerTransportVVSId,
       "vServerTransportVVSTag": vServerTransportVVSTag,
       "vServerTransportPacketsSent": vServerTransportPacketsSent,
       "vServerTransportPacketsRecd": vServerTransportPacketsRecd,
       "vServerTransportPacketsRetransmitted": vServerTransportPacketsRetransmitted,
       "vServerTransportBytesSent": vServerTransportBytesSent,
       "vServerTransportBytesRecd": vServerTransportBytesRecd,
       "vServerTransportBytesRetransmitted": vServerTransportBytesRetransmitted,
       "vServerTransportUndeliverableToClients": vServerTransportUndeliverableToClients,
       "vServerTransportUndeliverableToComp": vServerTransportUndeliverableToComp,
       "vServerTransportTotalConnections": vServerTransportTotalConnections,
       "vServerTransportFailedConnections": vServerTransportFailedConnections,
       "vServerTransportCurrentConnections": vServerTransportCurrentConnections,
       "vServerTransportBytesToComp": vServerTransportBytesToComp,
       "vServerTransportBytesFromComp": vServerTransportBytesFromComp,
       "vServerStatsSubscriber": vServerStatsSubscriber,
       "vServerStatsSubscriberScalars": vServerStatsSubscriberScalars,
       "vServerClientLimitExceeded": vServerClientLimitExceeded,
       "vServerClientlessLimitExceeded": vServerClientlessLimitExceeded,
       "vServerStatsSubscriberTables": vServerStatsSubscriberTables,
       "vServerSubscriberUsageTable": vServerSubscriberUsageTable,
       "vServerSubscriberUsageEntry": vServerSubscriberUsageEntry,
       "vServerSubscriberType": vServerSubscriberType,
       "vServerSubscriberVVSId": vServerSubscriberVVSId,
       "vServerSubscriberVVSTag": vServerSubscriberVVSTag,
       "vServerSubscriberTotalCount": vServerSubscriberTotalCount,
       "vServerSubscriberCurrCount": vServerSubscriberCurrCount,
       "vServerSubscriberAuthenticationFailures": vServerSubscriberAuthenticationFailures,
       "vServerSubscriberAbortedConnections": vServerSubscriberAbortedConnections,
       "vServerSubscriberReassignmentFailures": vServerSubscriberReassignmentFailures,
       "vServerSubscriberStandbyCount": vServerSubscriberStandbyCount,
       "vServerSubscriberInactiveCount": vServerSubscriberInactiveCount,
       "vServerSubscriberReassignmentCount": vServerSubscriberReassignmentCount,
       "vServerSubscriberByteCount": vServerSubscriberByteCount,
       "vServerSubscriberClientTable": vServerSubscriberClientTable,
       "vServerSubscriberClientEntry": vServerSubscriberClientEntry,
       "vServerSubscriberClientRowId": vServerSubscriberClientRowId,
       "vServerSubscriberClientUniqueId": vServerSubscriberClientUniqueId,
       "vServerSubscriberClientIPAddress": vServerSubscriberClientIPAddress,
       "vServerSubscriberClientVersion": vServerSubscriberClientVersion,
       "vServerSubscriberClientLastAccessTime": vServerSubscriberClientLastAccessTime,
       "vServerSubscriberClientTransportConnections": vServerSubscriberClientTransportConnections,
       "vServerSubscriberClientVVSTag": vServerSubscriberClientVVSTag,
       "vServerSubscriberClientUserInfo": vServerSubscriberClientUserInfo,
       "vServerSubscriberClientConnType": vServerSubscriberClientConnType,
       "vServerSubscriberClientOS": vServerSubscriberClientOS,
       "vServerSubscriberClientMAC": vServerSubscriberClientMAC,
       "vServerSubscriberClientPhone": vServerSubscriberClientPhone,
       "vServerSubscriberClientConnDuration": vServerSubscriberClientConnDuration,
       "vServerSubscriberClientVTPPktsSent": vServerSubscriberClientVTPPktsSent,
       "vServerSubscriberClientVTPPktsRcvd": vServerSubscriberClientVTPPktsRcvd,
       "vServerSubscriberClientVTPBytesSent": vServerSubscriberClientVTPBytesSent,
       "vServerSubscriberClientVTPBytesRcvd": vServerSubscriberClientVTPBytesRcvd,
       "vServerSubscriberClientVTPDropPkts": vServerSubscriberClientVTPDropPkts,
       "vServerSubscriberClientVTPReXmitPkts": vServerSubscriberClientVTPReXmitPkts,
       "vServerSubscriberClientVTPErrorPkts": vServerSubscriberClientVTPErrorPkts,
       "vServerSubscriberClientVTPBWToClient": vServerSubscriberClientVTPBWToClient,
       "vServerSubscriberClientVTPBWFromClient": vServerSubscriberClientVTPBWFromClient,
       "vServerSubscriberClientFromExternal": vServerSubscriberClientFromExternal,
       "vServerSubscriberClientToExternal": vServerSubscriberClientToExternal,
       "vServerSubscriberClientFromTransport": vServerSubscriberClientFromTransport,
       "vServerSubscriberClientToTransport": vServerSubscriberClientToTransport,
       "vServerSubscriberClientRTT": vServerSubscriberClientRTT,
       "vServerSubscriberClientVTPReXmitBytes": vServerSubscriberClientVTPReXmitBytes,
       "vServerSubscriberClientlessTable": vServerSubscriberClientlessTable,
       "vServerSubscriberClientlessEntry": vServerSubscriberClientlessEntry,
       "vServerSubscriberClientlessRowId": vServerSubscriberClientlessRowId,
       "vServerSubscriberClientlessIPAddress": vServerSubscriberClientlessIPAddress,
       "vServerSubscriberClientlessLastAccessTime": vServerSubscriberClientlessLastAccessTime,
       "vServerSubscriberClientlessTransportConnections": vServerSubscriberClientlessTransportConnections,
       "vServerSubscriberClientlessVVSTag": vServerSubscriberClientlessVVSTag,
       "vServerAbbreviatedSubscriberClientTable": vServerAbbreviatedSubscriberClientTable,
       "vServerAbbreviatedSubscriberClientEntry": vServerAbbreviatedSubscriberClientEntry,
       "vServerAbbreviatedSubscriberClientRowId": vServerAbbreviatedSubscriberClientRowId,
       "vServerAbbreviatedSubscriberClientIPAddress": vServerAbbreviatedSubscriberClientIPAddress,
       "vServerAbbreviatedSubscriberClientVTPBWToClient": vServerAbbreviatedSubscriberClientVTPBWToClient,
       "vServerAbbreviatedSubscriberClientVTPBWFromClient": vServerAbbreviatedSubscriberClientVTPBWFromClient,
       "vServerAbbreviatedSubscriberClientRTT": vServerAbbreviatedSubscriberClientRTT,
       "vServerClientInfoTable": vServerClientInfoTable,
       "vServerClientInfoEntry": vServerClientInfoEntry,
       "vServerClientInfoRowId": vServerClientInfoRowId,
       "vServerClientInfoClientId": vServerClientInfoClientId,
       "vServerClientInfoRemoteIp": vServerClientInfoRemoteIp,
       "vServerClientInfoSubIp": vServerClientInfoSubIp,
       "vServerClientInfoActVC": vServerClientInfoActVC,
       "vServerClientInfoBytesSent": vServerClientInfoBytesSent,
       "vServerClientInfoBytesRcvd": vServerClientInfoBytesRcvd,
       "vServerClientInfoXmitRate": vServerClientInfoXmitRate,
       "vServerClientInfoRecvRate": vServerClientInfoRecvRate,
       "vServerClientInfoRTT": vServerClientInfoRTT,
       "vServerClientInfoNSub": vServerClientInfoNSub,
       "vServerClientInfoFsc": vServerClientInfoFsc,
       "vServerClientInfoScale0": vServerClientInfoScale0,
       "vServerClientInfoScale1": vServerClientInfoScale1,
       "vServerClientInfoScale2": vServerClientInfoScale2,
       "vServerClientInfoScale3": vServerClientInfoScale3,
       "vServerStatsCapacity": vServerStatsCapacity,
       "vServerStatsCapacityScalars": vServerStatsCapacityScalars,
       "vServerCapacityPeakPeriod": vServerCapacityPeakPeriod,
       "vServerCapacityLoad": vServerCapacityLoad,
       "vServerStatsCapacityTables": vServerStatsCapacityTables,
       "vServerStatsHealthcheck": vServerStatsHealthcheck,
       "vServerStatsHealthcheckScalars": vServerStatsHealthcheckScalars,
       "vServerStatsHealthcheckClientless": vServerStatsHealthcheckClientless,
       "vServerHealthcheckClientlessRate": vServerHealthcheckClientlessRate,
       "vServerHealthcheckClientlessFlow": vServerHealthcheckClientlessFlow,
       "vServerStatsHealthcheckCliented": vServerStatsHealthcheckCliented,
       "vServerHealthcheckClientedRate": vServerHealthcheckClientedRate,
       "vServerStatsHealthcheckTables": vServerStatsHealthcheckTables,
       "vServerStatsPerfGraph": vServerStatsPerfGraph,
       "vServerStatsPerfGraphScalars": vServerStatsPerfGraphScalars,
       "vServerStatsDirectInBytes": vServerStatsDirectInBytes,
       "vServerStatsProxyInBytes": vServerStatsProxyInBytes,
       "vServerStatsUncompressedCacheInBytes": vServerStatsUncompressedCacheInBytes,
       "vServerStatsSubscriberOutBytes": vServerStatsSubscriberOutBytes,
       "vServerStatsPerfGraphTables": vServerStatsPerfGraphTables}
)
