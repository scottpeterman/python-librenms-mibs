# SNMP MIB module (NUTANIX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\nutanix-aos\NUTANIX-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:19:09 2025
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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nutanix = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 41263)
)
if mibBuilder.loadTexts:
    nutanix.setRevisions(
        ("2021-11-08 18:11",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SoftwareVersionTable_Object = MibTable
softwareVersionTable = _SoftwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1)
)
if mibBuilder.loadTexts:
    softwareVersionTable.setStatus("current")
_SvtEntry_Object = MibTableRow
svtEntry = _SvtEntry_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1, 1)
)
svtEntry.setIndexNames(
    (0, "NUTANIX-MIB", "svtIndex"),
)
if mibBuilder.loadTexts:
    svtEntry.setStatus("current")


class _SvtIndex_Type(Integer32):
    """Custom type svtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SvtIndex_Type.__name__ = "Integer32"
_SvtIndex_Object = MibTableColumn
svtIndex = _SvtIndex_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1, 1, 1),
    _SvtIndex_Type()
)
svtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svtIndex.setStatus("current")
_SvtControllerVMId_Type = DisplayString
_SvtControllerVMId_Object = MibTableColumn
svtControllerVMId = _SvtControllerVMId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1, 1, 2),
    _SvtControllerVMId_Type()
)
svtControllerVMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svtControllerVMId.setStatus("current")


class _SvtNutanixBootstrap_Type(DisplayString):
    """Custom type svtNutanixBootstrap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvtNutanixBootstrap_Type.__name__ = "DisplayString"
_SvtNutanixBootstrap_Object = MibTableColumn
svtNutanixBootstrap = _SvtNutanixBootstrap_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1, 1, 3),
    _SvtNutanixBootstrap_Type()
)
svtNutanixBootstrap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svtNutanixBootstrap.setStatus("current")


class _SvtNutanixInfrastructure_Type(DisplayString):
    """Custom type svtNutanixInfrastructure based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvtNutanixInfrastructure_Type.__name__ = "DisplayString"
_SvtNutanixInfrastructure_Object = MibTableColumn
svtNutanixInfrastructure = _SvtNutanixInfrastructure_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1, 1, 4),
    _SvtNutanixInfrastructure_Type()
)
svtNutanixInfrastructure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svtNutanixInfrastructure.setStatus("current")


class _SvtNutanixCore_Type(DisplayString):
    """Custom type svtNutanixCore based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvtNutanixCore_Type.__name__ = "DisplayString"
_SvtNutanixCore_Object = MibTableColumn
svtNutanixCore = _SvtNutanixCore_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1, 1, 5),
    _SvtNutanixCore_Type()
)
svtNutanixCore.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svtNutanixCore.setStatus("current")


class _SvtNutanixToolchain_Type(DisplayString):
    """Custom type svtNutanixToolchain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvtNutanixToolchain_Type.__name__ = "DisplayString"
_SvtNutanixToolchain_Object = MibTableColumn
svtNutanixToolchain = _SvtNutanixToolchain_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1, 1, 6),
    _SvtNutanixToolchain_Type()
)
svtNutanixToolchain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svtNutanixToolchain.setStatus("current")


class _SvtNutanixServiceability_Type(DisplayString):
    """Custom type svtNutanixServiceability based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvtNutanixServiceability_Type.__name__ = "DisplayString"
_SvtNutanixServiceability_Object = MibTableColumn
svtNutanixServiceability = _SvtNutanixServiceability_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1, 1, 7),
    _SvtNutanixServiceability_Type()
)
svtNutanixServiceability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svtNutanixServiceability.setStatus("current")


class _SvtLinuxKernel_Type(DisplayString):
    """Custom type svtLinuxKernel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SvtLinuxKernel_Type.__name__ = "DisplayString"
_SvtLinuxKernel_Object = MibTableColumn
svtLinuxKernel = _SvtLinuxKernel_Object(
    (1, 3, 6, 1, 4, 1, 41263, 1, 1, 8),
    _SvtLinuxKernel_Type()
)
svtLinuxKernel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    svtLinuxKernel.setStatus("current")
_ServiceStatusTable_Object = MibTable
serviceStatusTable = _ServiceStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2)
)
if mibBuilder.loadTexts:
    serviceStatusTable.setStatus("obsolete")
_SstEntry_Object = MibTableRow
sstEntry = _SstEntry_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1)
)
sstEntry.setIndexNames(
    (0, "NUTANIX-MIB", "sstIndex"),
)
if mibBuilder.loadTexts:
    sstEntry.setStatus("obsolete")


class _SstIndex_Type(Integer32):
    """Custom type sstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SstIndex_Type.__name__ = "Integer32"
_SstIndex_Object = MibTableColumn
sstIndex = _SstIndex_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 1),
    _SstIndex_Type()
)
sstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstIndex.setStatus("obsolete")
_SstControllerVMId_Type = DisplayString
_SstControllerVMId_Object = MibTableColumn
sstControllerVMId = _SstControllerVMId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 2),
    _SstControllerVMId_Type()
)
sstControllerVMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstControllerVMId.setStatus("obsolete")


class _SstControllerVMStatus_Type(DisplayString):
    """Custom type sstControllerVMStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstControllerVMStatus_Type.__name__ = "DisplayString"
_SstControllerVMStatus_Object = MibTableColumn
sstControllerVMStatus = _SstControllerVMStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 3),
    _SstControllerVMStatus_Type()
)
sstControllerVMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstControllerVMStatus.setStatus("obsolete")


class _SstZeusStatus_Type(DisplayString):
    """Custom type sstZeusStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstZeusStatus_Type.__name__ = "DisplayString"
_SstZeusStatus_Object = MibTableColumn
sstZeusStatus = _SstZeusStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 4),
    _SstZeusStatus_Type()
)
sstZeusStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstZeusStatus.setStatus("obsolete")


class _SstScavengerStatus_Type(DisplayString):
    """Custom type sstScavengerStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstScavengerStatus_Type.__name__ = "DisplayString"
_SstScavengerStatus_Object = MibTableColumn
sstScavengerStatus = _SstScavengerStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 5),
    _SstScavengerStatus_Type()
)
sstScavengerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstScavengerStatus.setStatus("obsolete")


class _SstMedusaStatus_Type(DisplayString):
    """Custom type sstMedusaStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstMedusaStatus_Type.__name__ = "DisplayString"
_SstMedusaStatus_Object = MibTableColumn
sstMedusaStatus = _SstMedusaStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 6),
    _SstMedusaStatus_Type()
)
sstMedusaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstMedusaStatus.setStatus("obsolete")


class _SstPithosStatus_Type(DisplayString):
    """Custom type sstPithosStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstPithosStatus_Type.__name__ = "DisplayString"
_SstPithosStatus_Object = MibTableColumn
sstPithosStatus = _SstPithosStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 7),
    _SstPithosStatus_Type()
)
sstPithosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstPithosStatus.setStatus("obsolete")


class _SstStargateStatus_Type(DisplayString):
    """Custom type sstStargateStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstStargateStatus_Type.__name__ = "DisplayString"
_SstStargateStatus_Object = MibTableColumn
sstStargateStatus = _SstStargateStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 8),
    _SstStargateStatus_Type()
)
sstStargateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstStargateStatus.setStatus("obsolete")


class _SstChronosStatus_Type(DisplayString):
    """Custom type sstChronosStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstChronosStatus_Type.__name__ = "DisplayString"
_SstChronosStatus_Object = MibTableColumn
sstChronosStatus = _SstChronosStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 9),
    _SstChronosStatus_Type()
)
sstChronosStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstChronosStatus.setStatus("obsolete")


class _SstCuratorStatus_Type(DisplayString):
    """Custom type sstCuratorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstCuratorStatus_Type.__name__ = "DisplayString"
_SstCuratorStatus_Object = MibTableColumn
sstCuratorStatus = _SstCuratorStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 10),
    _SstCuratorStatus_Type()
)
sstCuratorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstCuratorStatus.setStatus("obsolete")


class _SstPrismStatus_Type(DisplayString):
    """Custom type sstPrismStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstPrismStatus_Type.__name__ = "DisplayString"
_SstPrismStatus_Object = MibTableColumn
sstPrismStatus = _SstPrismStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 11),
    _SstPrismStatus_Type()
)
sstPrismStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstPrismStatus.setStatus("obsolete")


class _SstAlertManagerStatus_Type(DisplayString):
    """Custom type sstAlertManagerStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstAlertManagerStatus_Type.__name__ = "DisplayString"
_SstAlertManagerStatus_Object = MibTableColumn
sstAlertManagerStatus = _SstAlertManagerStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 12),
    _SstAlertManagerStatus_Type()
)
sstAlertManagerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstAlertManagerStatus.setStatus("obsolete")


class _SstStatsAggregatorStatus_Type(DisplayString):
    """Custom type sstStatsAggregatorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstStatsAggregatorStatus_Type.__name__ = "DisplayString"
_SstStatsAggregatorStatus_Object = MibTableColumn
sstStatsAggregatorStatus = _SstStatsAggregatorStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 13),
    _SstStatsAggregatorStatus_Type()
)
sstStatsAggregatorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstStatsAggregatorStatus.setStatus("obsolete")


class _SstSysStatCollectorStatus_Type(DisplayString):
    """Custom type sstSysStatCollectorStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SstSysStatCollectorStatus_Type.__name__ = "DisplayString"
_SstSysStatCollectorStatus_Object = MibTableColumn
sstSysStatCollectorStatus = _SstSysStatCollectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 2, 1, 14),
    _SstSysStatCollectorStatus_Type()
)
sstSysStatCollectorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sstSysStatCollectorStatus.setStatus("obsolete")
_DiskStatusTable_Object = MibTable
diskStatusTable = _DiskStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3)
)
if mibBuilder.loadTexts:
    diskStatusTable.setStatus("current")
_DstEntry_Object = MibTableRow
dstEntry = _DstEntry_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1)
)
dstEntry.setIndexNames(
    (0, "NUTANIX-MIB", "dstIndex"),
)
if mibBuilder.loadTexts:
    dstEntry.setStatus("current")


class _DstIndex_Type(Integer32):
    """Custom type dstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_DstIndex_Type.__name__ = "Integer32"
_DstIndex_Object = MibTableColumn
dstIndex = _DstIndex_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 1),
    _DstIndex_Type()
)
dstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstIndex.setStatus("current")
_DstDiskId_Type = DisplayString
_DstDiskId_Object = MibTableColumn
dstDiskId = _DstDiskId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 2),
    _DstDiskId_Type()
)
dstDiskId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstDiskId.setStatus("current")
_DstControllerVMId_Type = DisplayString
_DstControllerVMId_Object = MibTableColumn
dstControllerVMId = _DstControllerVMId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 3),
    _DstControllerVMId_Type()
)
dstControllerVMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstControllerVMId.setStatus("current")


class _DstSerial_Type(DisplayString):
    """Custom type dstSerial based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DstSerial_Type.__name__ = "DisplayString"
_DstSerial_Object = MibTableColumn
dstSerial = _DstSerial_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 4),
    _DstSerial_Type()
)
dstSerial.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstSerial.setStatus("current")
_DstNumRawBytes_Type = Counter64
_DstNumRawBytes_Object = MibTableColumn
dstNumRawBytes = _DstNumRawBytes_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 5),
    _DstNumRawBytes_Type()
)
dstNumRawBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstNumRawBytes.setStatus("current")
_DstNumTotalBytes_Type = Counter64
_DstNumTotalBytes_Object = MibTableColumn
dstNumTotalBytes = _DstNumTotalBytes_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 6),
    _DstNumTotalBytes_Type()
)
dstNumTotalBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstNumTotalBytes.setStatus("current")
_DstNumFreeBytes_Type = Counter64
_DstNumFreeBytes_Object = MibTableColumn
dstNumFreeBytes = _DstNumFreeBytes_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 7),
    _DstNumFreeBytes_Type()
)
dstNumFreeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstNumFreeBytes.setStatus("current")
_DstNumTotalInodes_Type = Counter64
_DstNumTotalInodes_Object = MibTableColumn
dstNumTotalInodes = _DstNumTotalInodes_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 8),
    _DstNumTotalInodes_Type()
)
dstNumTotalInodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstNumTotalInodes.setStatus("obsolete")
_DstNumFreeInodes_Type = Counter64
_DstNumFreeInodes_Object = MibTableColumn
dstNumFreeInodes = _DstNumFreeInodes_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 9),
    _DstNumFreeInodes_Type()
)
dstNumFreeInodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstNumFreeInodes.setStatus("obsolete")
_DstAverageLatency_Type = Counter64
_DstAverageLatency_Object = MibTableColumn
dstAverageLatency = _DstAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 10),
    _DstAverageLatency_Type()
)
dstAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstAverageLatency.setStatus("current")
_DstIOBandwidth_Type = Counter64
_DstIOBandwidth_Object = MibTableColumn
dstIOBandwidth = _DstIOBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 11),
    _DstIOBandwidth_Type()
)
dstIOBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstIOBandwidth.setStatus("current")
_DstNumberIops_Type = Counter64
_DstNumberIops_Object = MibTableColumn
dstNumberIops = _DstNumberIops_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 12),
    _DstNumberIops_Type()
)
dstNumberIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstNumberIops.setStatus("current")


class _DstState_Type(Integer32):
    """Custom type dstState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("online", 1),
          ("offline", 2))
    )


_DstState_Type.__name__ = "Integer32"
_DstState_Object = MibTableColumn
dstState = _DstState_Object(
    (1, 3, 6, 1, 4, 1, 41263, 3, 1, 13),
    _DstState_Type()
)
dstState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dstState.setStatus("current")
_ControllerVMResourceTable_Object = MibTable
controllerVMResourceTable = _ControllerVMResourceTable_Object(
    (1, 3, 6, 1, 4, 1, 41263, 4)
)
if mibBuilder.loadTexts:
    controllerVMResourceTable.setStatus("current")
_CrtEntry_Object = MibTableRow
crtEntry = _CrtEntry_Object(
    (1, 3, 6, 1, 4, 1, 41263, 4, 1)
)
crtEntry.setIndexNames(
    (0, "NUTANIX-MIB", "crtIndex"),
)
if mibBuilder.loadTexts:
    crtEntry.setStatus("current")


class _CrtIndex_Type(Integer32):
    """Custom type crtIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CrtIndex_Type.__name__ = "Integer32"
_CrtIndex_Object = MibTableColumn
crtIndex = _CrtIndex_Object(
    (1, 3, 6, 1, 4, 1, 41263, 4, 1, 1),
    _CrtIndex_Type()
)
crtIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crtIndex.setStatus("current")
_CrtControllerVMId_Type = DisplayString
_CrtControllerVMId_Object = MibTableColumn
crtControllerVMId = _CrtControllerVMId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 4, 1, 2),
    _CrtControllerVMId_Type()
)
crtControllerVMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crtControllerVMId.setStatus("current")
_CrtMemory_Type = Counter64
_CrtMemory_Object = MibTableColumn
crtMemory = _CrtMemory_Object(
    (1, 3, 6, 1, 4, 1, 41263, 4, 1, 3),
    _CrtMemory_Type()
)
crtMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crtMemory.setStatus("current")
_CrtNumCpus_Type = Integer32
_CrtNumCpus_Object = MibTableColumn
crtNumCpus = _CrtNumCpus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 4, 1, 4),
    _CrtNumCpus_Type()
)
crtNumCpus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crtNumCpus.setStatus("current")


class _CrtName_Type(DisplayString):
    """Custom type crtName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CrtName_Type.__name__ = "DisplayString"
_CrtName_Object = MibTableColumn
crtName = _CrtName_Object(
    (1, 3, 6, 1, 4, 1, 41263, 4, 1, 5),
    _CrtName_Type()
)
crtName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    crtName.setStatus("current")
_StoragePoolInformationTable_Object = MibTable
storagePoolInformationTable = _StoragePoolInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7)
)
if mibBuilder.loadTexts:
    storagePoolInformationTable.setStatus("current")
_SpitEntry_Object = MibTableRow
spitEntry = _SpitEntry_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7, 1)
)
spitEntry.setIndexNames(
    (0, "NUTANIX-MIB", "spitIndex"),
)
if mibBuilder.loadTexts:
    spitEntry.setStatus("current")


class _SpitIndex_Type(Integer32):
    """Custom type spitIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_SpitIndex_Type.__name__ = "Integer32"
_SpitIndex_Object = MibTableColumn
spitIndex = _SpitIndex_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7, 1, 1),
    _SpitIndex_Type()
)
spitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spitIndex.setStatus("current")
_SpitStoragePoolId_Type = DisplayString
_SpitStoragePoolId_Object = MibTableColumn
spitStoragePoolId = _SpitStoragePoolId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7, 1, 2),
    _SpitStoragePoolId_Type()
)
spitStoragePoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spitStoragePoolId.setStatus("current")


class _SpitStoragePoolName_Type(DisplayString):
    """Custom type spitStoragePoolName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SpitStoragePoolName_Type.__name__ = "DisplayString"
_SpitStoragePoolName_Object = MibTableColumn
spitStoragePoolName = _SpitStoragePoolName_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7, 1, 3),
    _SpitStoragePoolName_Type()
)
spitStoragePoolName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spitStoragePoolName.setStatus("current")
_SpitTotalCapacity_Type = Counter64
_SpitTotalCapacity_Object = MibTableColumn
spitTotalCapacity = _SpitTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7, 1, 4),
    _SpitTotalCapacity_Type()
)
spitTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spitTotalCapacity.setStatus("current")
_SpitUsedCapacity_Type = Counter64
_SpitUsedCapacity_Object = MibTableColumn
spitUsedCapacity = _SpitUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7, 1, 5),
    _SpitUsedCapacity_Type()
)
spitUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spitUsedCapacity.setStatus("current")
_SpitIOPerSecond_Type = Integer32
_SpitIOPerSecond_Object = MibTableColumn
spitIOPerSecond = _SpitIOPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7, 1, 6),
    _SpitIOPerSecond_Type()
)
spitIOPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spitIOPerSecond.setStatus("current")
_SpitAvgLatencyUsecs_Type = Counter64
_SpitAvgLatencyUsecs_Object = MibTableColumn
spitAvgLatencyUsecs = _SpitAvgLatencyUsecs_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7, 1, 7),
    _SpitAvgLatencyUsecs_Type()
)
spitAvgLatencyUsecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spitAvgLatencyUsecs.setStatus("current")
_SpitIOBandwidth_Type = Counter64
_SpitIOBandwidth_Object = MibTableColumn
spitIOBandwidth = _SpitIOBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41263, 7, 1, 8),
    _SpitIOBandwidth_Type()
)
spitIOBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    spitIOBandwidth.setStatus("current")
_ContainerInformationTable_Object = MibTable
containerInformationTable = _ContainerInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8)
)
if mibBuilder.loadTexts:
    containerInformationTable.setStatus("current")
_CitEntry_Object = MibTableRow
citEntry = _CitEntry_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8, 1)
)
citEntry.setIndexNames(
    (0, "NUTANIX-MIB", "citIndex"),
)
if mibBuilder.loadTexts:
    citEntry.setStatus("current")


class _CitIndex_Type(Integer32):
    """Custom type citIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CitIndex_Type.__name__ = "Integer32"
_CitIndex_Object = MibTableColumn
citIndex = _CitIndex_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8, 1, 1),
    _CitIndex_Type()
)
citIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citIndex.setStatus("current")
_CitContainerId_Type = DisplayString
_CitContainerId_Object = MibTableColumn
citContainerId = _CitContainerId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8, 1, 2),
    _CitContainerId_Type()
)
citContainerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citContainerId.setStatus("current")


class _CitContainerName_Type(DisplayString):
    """Custom type citContainerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CitContainerName_Type.__name__ = "DisplayString"
_CitContainerName_Object = MibTableColumn
citContainerName = _CitContainerName_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8, 1, 3),
    _CitContainerName_Type()
)
citContainerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citContainerName.setStatus("current")
_CitTotalCapacity_Type = Counter64
_CitTotalCapacity_Object = MibTableColumn
citTotalCapacity = _CitTotalCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8, 1, 4),
    _CitTotalCapacity_Type()
)
citTotalCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citTotalCapacity.setStatus("current")
_CitUsedCapacity_Type = Counter64
_CitUsedCapacity_Object = MibTableColumn
citUsedCapacity = _CitUsedCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8, 1, 5),
    _CitUsedCapacity_Type()
)
citUsedCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citUsedCapacity.setStatus("current")
_CitIOPerSecond_Type = Integer32
_CitIOPerSecond_Object = MibTableColumn
citIOPerSecond = _CitIOPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8, 1, 6),
    _CitIOPerSecond_Type()
)
citIOPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citIOPerSecond.setStatus("current")
_CitAvgLatencyUsecs_Type = Counter64
_CitAvgLatencyUsecs_Object = MibTableColumn
citAvgLatencyUsecs = _CitAvgLatencyUsecs_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8, 1, 7),
    _CitAvgLatencyUsecs_Type()
)
citAvgLatencyUsecs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citAvgLatencyUsecs.setStatus("current")
_CitIOBandwidth_Type = Counter64
_CitIOBandwidth_Object = MibTableColumn
citIOBandwidth = _CitIOBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41263, 8, 1, 8),
    _CitIOBandwidth_Type()
)
citIOBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    citIOBandwidth.setStatus("current")
_HypervisorInformationTable_Object = MibTable
hypervisorInformationTable = _HypervisorInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9)
)
if mibBuilder.loadTexts:
    hypervisorInformationTable.setStatus("current")
_HypervisorEntry_Object = MibTableRow
hypervisorEntry = _HypervisorEntry_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1)
)
hypervisorEntry.setIndexNames(
    (0, "NUTANIX-MIB", "hypervisorIndex"),
)
if mibBuilder.loadTexts:
    hypervisorEntry.setStatus("current")


class _HypervisorIndex_Type(Integer32):
    """Custom type hypervisorIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HypervisorIndex_Type.__name__ = "Integer32"
_HypervisorIndex_Object = MibTableColumn
hypervisorIndex = _HypervisorIndex_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 1),
    _HypervisorIndex_Type()
)
hypervisorIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorIndex.setStatus("current")
_HypervisorId_Type = DisplayString
_HypervisorId_Object = MibTableColumn
hypervisorId = _HypervisorId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 2),
    _HypervisorId_Type()
)
hypervisorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorId.setStatus("current")


class _HypervisorName_Type(DisplayString):
    """Custom type hypervisorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HypervisorName_Type.__name__ = "DisplayString"
_HypervisorName_Object = MibTableColumn
hypervisorName = _HypervisorName_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 3),
    _HypervisorName_Type()
)
hypervisorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorName.setStatus("current")
_HypervisorVmCount_Type = Unsigned32
_HypervisorVmCount_Object = MibTableColumn
hypervisorVmCount = _HypervisorVmCount_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 4),
    _HypervisorVmCount_Type()
)
hypervisorVmCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorVmCount.setStatus("current")
_HypervisorCpuCount_Type = Unsigned32
_HypervisorCpuCount_Object = MibTableColumn
hypervisorCpuCount = _HypervisorCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 5),
    _HypervisorCpuCount_Type()
)
hypervisorCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorCpuCount.setStatus("current")
_HypervisorCpuUsagePercent_Type = Unsigned32
_HypervisorCpuUsagePercent_Object = MibTableColumn
hypervisorCpuUsagePercent = _HypervisorCpuUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 6),
    _HypervisorCpuUsagePercent_Type()
)
hypervisorCpuUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorCpuUsagePercent.setStatus("current")
_HypervisorMemory_Type = Counter64
_HypervisorMemory_Object = MibTableColumn
hypervisorMemory = _HypervisorMemory_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 7),
    _HypervisorMemory_Type()
)
hypervisorMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorMemory.setStatus("current")
_HypervisorMemoryUsagePercent_Type = Unsigned32
_HypervisorMemoryUsagePercent_Object = MibTableColumn
hypervisorMemoryUsagePercent = _HypervisorMemoryUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 8),
    _HypervisorMemoryUsagePercent_Type()
)
hypervisorMemoryUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorMemoryUsagePercent.setStatus("current")
_HypervisorReadIOPerSecond_Type = Unsigned32
_HypervisorReadIOPerSecond_Object = MibTableColumn
hypervisorReadIOPerSecond = _HypervisorReadIOPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 9),
    _HypervisorReadIOPerSecond_Type()
)
hypervisorReadIOPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorReadIOPerSecond.setStatus("current")
_HypervisorWriteIOPerSecond_Type = Unsigned32
_HypervisorWriteIOPerSecond_Object = MibTableColumn
hypervisorWriteIOPerSecond = _HypervisorWriteIOPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 10),
    _HypervisorWriteIOPerSecond_Type()
)
hypervisorWriteIOPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorWriteIOPerSecond.setStatus("current")
_HypervisorAverageLatency_Type = Counter64
_HypervisorAverageLatency_Object = MibTableColumn
hypervisorAverageLatency = _HypervisorAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 11),
    _HypervisorAverageLatency_Type()
)
hypervisorAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorAverageLatency.setStatus("current")
_HypervisorIOBandwidth_Type = Counter64
_HypervisorIOBandwidth_Object = MibTableColumn
hypervisorIOBandwidth = _HypervisorIOBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 12),
    _HypervisorIOBandwidth_Type()
)
hypervisorIOBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorIOBandwidth.setStatus("current")
_HypervisorRxBytes_Type = Counter64
_HypervisorRxBytes_Object = MibTableColumn
hypervisorRxBytes = _HypervisorRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 13),
    _HypervisorRxBytes_Type()
)
hypervisorRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorRxBytes.setStatus("current")
_HypervisorTxBytes_Type = Counter64
_HypervisorTxBytes_Object = MibTableColumn
hypervisorTxBytes = _HypervisorTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 14),
    _HypervisorTxBytes_Type()
)
hypervisorTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorTxBytes.setStatus("current")
_HypervisorRxDropCount_Type = Counter64
_HypervisorRxDropCount_Object = MibTableColumn
hypervisorRxDropCount = _HypervisorRxDropCount_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 15),
    _HypervisorRxDropCount_Type()
)
hypervisorRxDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorRxDropCount.setStatus("current")
_HypervisorTxDropCount_Type = Counter64
_HypervisorTxDropCount_Object = MibTableColumn
hypervisorTxDropCount = _HypervisorTxDropCount_Object(
    (1, 3, 6, 1, 4, 1, 41263, 9, 1, 16),
    _HypervisorTxDropCount_Type()
)
hypervisorTxDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hypervisorTxDropCount.setStatus("current")
_VmInformationTable_Object = MibTable
vmInformationTable = _VmInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10)
)
if mibBuilder.loadTexts:
    vmInformationTable.setStatus("current")
_VmEntry_Object = MibTableRow
vmEntry = _VmEntry_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1)
)
vmEntry.setIndexNames(
    (0, "NUTANIX-MIB", "vmIndex"),
)
if mibBuilder.loadTexts:
    vmEntry.setStatus("current")


class _VmIndex_Type(Integer32):
    """Custom type vmIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VmIndex_Type.__name__ = "Integer32"
_VmIndex_Object = MibTableColumn
vmIndex = _VmIndex_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 1),
    _VmIndex_Type()
)
vmIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIndex.setStatus("current")


class _VmId_Type(DisplayString):
    """Custom type vmId based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmId_Type.__name__ = "DisplayString"
_VmId_Object = MibTableColumn
vmId = _VmId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 2),
    _VmId_Type()
)
vmId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmId.setStatus("current")


class _VmName_Type(DisplayString):
    """Custom type vmName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmName_Type.__name__ = "DisplayString"
_VmName_Object = MibTableColumn
vmName = _VmName_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 3),
    _VmName_Type()
)
vmName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmName.setStatus("current")
_VmHypervisorId_Type = DisplayString
_VmHypervisorId_Object = MibTableColumn
vmHypervisorId = _VmHypervisorId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 4),
    _VmHypervisorId_Type()
)
vmHypervisorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmHypervisorId.setStatus("current")
_VmPowerState_Type = DisplayString
_VmPowerState_Object = MibTableColumn
vmPowerState = _VmPowerState_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 5),
    _VmPowerState_Type()
)
vmPowerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmPowerState.setStatus("current")
_VmCpuCount_Type = Unsigned32
_VmCpuCount_Object = MibTableColumn
vmCpuCount = _VmCpuCount_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 6),
    _VmCpuCount_Type()
)
vmCpuCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmCpuCount.setStatus("current")
_VmCpuUsagePercent_Type = Unsigned32
_VmCpuUsagePercent_Object = MibTableColumn
vmCpuUsagePercent = _VmCpuUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 7),
    _VmCpuUsagePercent_Type()
)
vmCpuUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmCpuUsagePercent.setStatus("current")
_VmMemory_Type = Counter64
_VmMemory_Object = MibTableColumn
vmMemory = _VmMemory_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 8),
    _VmMemory_Type()
)
vmMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMemory.setStatus("current")
_VmMemoryUsagePercent_Type = Unsigned32
_VmMemoryUsagePercent_Object = MibTableColumn
vmMemoryUsagePercent = _VmMemoryUsagePercent_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 9),
    _VmMemoryUsagePercent_Type()
)
vmMemoryUsagePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmMemoryUsagePercent.setStatus("current")
_VmReadIOPerSecond_Type = Unsigned32
_VmReadIOPerSecond_Object = MibTableColumn
vmReadIOPerSecond = _VmReadIOPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 10),
    _VmReadIOPerSecond_Type()
)
vmReadIOPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmReadIOPerSecond.setStatus("current")
_VmWriteIOPerSecond_Type = Unsigned32
_VmWriteIOPerSecond_Object = MibTableColumn
vmWriteIOPerSecond = _VmWriteIOPerSecond_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 11),
    _VmWriteIOPerSecond_Type()
)
vmWriteIOPerSecond.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmWriteIOPerSecond.setStatus("current")
_VmAverageLatency_Type = Counter64
_VmAverageLatency_Object = MibTableColumn
vmAverageLatency = _VmAverageLatency_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 12),
    _VmAverageLatency_Type()
)
vmAverageLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmAverageLatency.setStatus("current")
_VmIOBandwidth_Type = Counter64
_VmIOBandwidth_Object = MibTableColumn
vmIOBandwidth = _VmIOBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 13),
    _VmIOBandwidth_Type()
)
vmIOBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmIOBandwidth.setStatus("current")
_VmRxBytes_Type = Counter64
_VmRxBytes_Object = MibTableColumn
vmRxBytes = _VmRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 14),
    _VmRxBytes_Type()
)
vmRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmRxBytes.setStatus("current")
_VmTxBytes_Type = Counter64
_VmTxBytes_Object = MibTableColumn
vmTxBytes = _VmTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 15),
    _VmTxBytes_Type()
)
vmTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmTxBytes.setStatus("current")
_VmRxDropCount_Type = Counter64
_VmRxDropCount_Object = MibTableColumn
vmRxDropCount = _VmRxDropCount_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 16),
    _VmRxDropCount_Type()
)
vmRxDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmRxDropCount.setStatus("current")
_VmTxDropCount_Type = Counter64
_VmTxDropCount_Object = MibTableColumn
vmTxDropCount = _VmTxDropCount_Object(
    (1, 3, 6, 1, 4, 1, 41263, 10, 1, 17),
    _VmTxDropCount_Type()
)
vmTxDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmTxDropCount.setStatus("current")
_ControllerStatusTable_Object = MibTable
controllerStatusTable = _ControllerStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 41263, 11)
)
if mibBuilder.loadTexts:
    controllerStatusTable.setStatus("current")
_CstEntry_Object = MibTableRow
cstEntry = _CstEntry_Object(
    (1, 3, 6, 1, 4, 1, 41263, 11, 1)
)
cstEntry.setIndexNames(
    (0, "NUTANIX-MIB", "cstIndex"),
)
if mibBuilder.loadTexts:
    cstEntry.setStatus("current")


class _CstIndex_Type(Integer32):
    """Custom type cstIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CstIndex_Type.__name__ = "Integer32"
_CstIndex_Object = MibTableColumn
cstIndex = _CstIndex_Object(
    (1, 3, 6, 1, 4, 1, 41263, 11, 1, 1),
    _CstIndex_Type()
)
cstIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstIndex.setStatus("current")
_CstControllerVMId_Type = DisplayString
_CstControllerVMId_Object = MibTableColumn
cstControllerVMId = _CstControllerVMId_Object(
    (1, 3, 6, 1, 4, 1, 41263, 11, 1, 2),
    _CstControllerVMId_Type()
)
cstControllerVMId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstControllerVMId.setStatus("current")


class _CstControllerVMStatus_Type(DisplayString):
    """Custom type cstControllerVMStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CstControllerVMStatus_Type.__name__ = "DisplayString"
_CstControllerVMStatus_Object = MibTableColumn
cstControllerVMStatus = _CstControllerVMStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 11, 1, 3),
    _CstControllerVMStatus_Type()
)
cstControllerVMStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstControllerVMStatus.setStatus("current")


class _CstDataServiceStatus_Type(DisplayString):
    """Custom type cstDataServiceStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CstDataServiceStatus_Type.__name__ = "DisplayString"
_CstDataServiceStatus_Object = MibTableColumn
cstDataServiceStatus = _CstDataServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 11, 1, 4),
    _CstDataServiceStatus_Type()
)
cstDataServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstDataServiceStatus.setStatus("current")


class _CstMetadataServiceStatus_Type(DisplayString):
    """Custom type cstMetadataServiceStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CstMetadataServiceStatus_Type.__name__ = "DisplayString"
_CstMetadataServiceStatus_Object = MibTableColumn
cstMetadataServiceStatus = _CstMetadataServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 11, 1, 5),
    _CstMetadataServiceStatus_Type()
)
cstMetadataServiceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cstMetadataServiceStatus.setStatus("current")


class _ClusterName_Type(DisplayString):
    """Custom type clusterName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClusterName_Type.__name__ = "DisplayString"
_ClusterName_Object = MibScalar
clusterName = _ClusterName_Object(
    (1, 3, 6, 1, 4, 1, 41263, 501),
    _ClusterName_Type()
)
clusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterName.setStatus("current")


class _ClusterVersion_Type(DisplayString):
    """Custom type clusterVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClusterVersion_Type.__name__ = "DisplayString"
_ClusterVersion_Object = MibScalar
clusterVersion = _ClusterVersion_Object(
    (1, 3, 6, 1, 4, 1, 41263, 502),
    _ClusterVersion_Type()
)
clusterVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterVersion.setStatus("current")


class _ClusterStatus_Type(DisplayString):
    """Custom type clusterStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ClusterStatus_Type.__name__ = "DisplayString"
_ClusterStatus_Object = MibScalar
clusterStatus = _ClusterStatus_Object(
    (1, 3, 6, 1, 4, 1, 41263, 503),
    _ClusterStatus_Type()
)
clusterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterStatus.setStatus("current")
_ClusterTotalStorageCapacity_Type = Counter64
_ClusterTotalStorageCapacity_Object = MibScalar
clusterTotalStorageCapacity = _ClusterTotalStorageCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41263, 504),
    _ClusterTotalStorageCapacity_Type()
)
clusterTotalStorageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterTotalStorageCapacity.setStatus("current")
_ClusterUsedStorageCapacity_Type = Counter64
_ClusterUsedStorageCapacity_Object = MibScalar
clusterUsedStorageCapacity = _ClusterUsedStorageCapacity_Object(
    (1, 3, 6, 1, 4, 1, 41263, 505),
    _ClusterUsedStorageCapacity_Type()
)
clusterUsedStorageCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterUsedStorageCapacity.setStatus("current")
_ClusterIops_Type = Counter64
_ClusterIops_Object = MibScalar
clusterIops = _ClusterIops_Object(
    (1, 3, 6, 1, 4, 1, 41263, 506),
    _ClusterIops_Type()
)
clusterIops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIops.setStatus("current")
_ClusterLatency_Type = Counter64
_ClusterLatency_Object = MibScalar
clusterLatency = _ClusterLatency_Object(
    (1, 3, 6, 1, 4, 1, 41263, 507),
    _ClusterLatency_Type()
)
clusterLatency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterLatency.setStatus("current")
_ClusterIOBandwidth_Type = Counter64
_ClusterIOBandwidth_Object = MibScalar
clusterIOBandwidth = _ClusterIOBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 41263, 508),
    _ClusterIOBandwidth_Type()
)
clusterIOBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterIOBandwidth.setStatus("current")
_NtxTrapName_Type = DisplayString
_NtxTrapName_Object = MibScalar
ntxTrapName = _NtxTrapName_Object(
    (1, 3, 6, 1, 4, 1, 41263, 992),
    _NtxTrapName_Type()
)
ntxTrapName.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntxTrapName.setStatus("current")
_NtxAlert_ObjectIdentity = ObjectIdentity
ntxAlert = _NtxAlert_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 41263, 999)
)
_NtxAlertCreationTime_Type = Counter64
_NtxAlertCreationTime_Object = MibScalar
ntxAlertCreationTime = _NtxAlertCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 1),
    _NtxAlertCreationTime_Type()
)
ntxAlertCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntxAlertCreationTime.setStatus("current")


class _NtxAlertDisplayMsg_Type(DisplayString):
    """Custom type ntxAlertDisplayMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1024),
    )


_NtxAlertDisplayMsg_Type.__name__ = "DisplayString"
_NtxAlertDisplayMsg_Object = MibScalar
ntxAlertDisplayMsg = _NtxAlertDisplayMsg_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 2),
    _NtxAlertDisplayMsg_Type()
)
ntxAlertDisplayMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntxAlertDisplayMsg.setStatus("current")
_NtxAlertTitle_Type = DisplayString
_NtxAlertTitle_Object = MibScalar
ntxAlertTitle = _NtxAlertTitle_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 3),
    _NtxAlertTitle_Type()
)
ntxAlertTitle.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntxAlertTitle.setStatus("current")


class _NtxAlertSeverity_Type(Integer32):
    """Custom type ntxAlertSeverity based on Integer32"""
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
        *(("informational", 1),
          ("warning", 2),
          ("critical", 3),
          ("audit", 4))
    )


_NtxAlertSeverity_Type.__name__ = "Integer32"
_NtxAlertSeverity_Object = MibScalar
ntxAlertSeverity = _NtxAlertSeverity_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 4),
    _NtxAlertSeverity_Type()
)
ntxAlertSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntxAlertSeverity.setStatus("current")
_NtxAlertUuid_Type = DisplayString
_NtxAlertUuid_Object = MibScalar
ntxAlertUuid = _NtxAlertUuid_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 5),
    _NtxAlertUuid_Type()
)
ntxAlertUuid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntxAlertUuid.setStatus("current")
_NtxAlertResolvedTime_Type = Counter64
_NtxAlertResolvedTime_Object = MibScalar
ntxAlertResolvedTime = _NtxAlertResolvedTime_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 6),
    _NtxAlertResolvedTime_Type()
)
ntxAlertResolvedTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    ntxAlertResolvedTime.setStatus("current")
_NtxAlertClusterName_Type = DisplayString
_NtxAlertClusterName_Object = MibScalar
ntxAlertClusterName = _NtxAlertClusterName_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 7),
    _NtxAlertClusterName_Type()
)
ntxAlertClusterName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntxAlertClusterName.setStatus("current")
_NtxAlertSourceEntityUuid_Type = DisplayString
_NtxAlertSourceEntityUuid_Object = MibScalar
ntxAlertSourceEntityUuid = _NtxAlertSourceEntityUuid_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 8),
    _NtxAlertSourceEntityUuid_Type()
)
ntxAlertSourceEntityUuid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntxAlertSourceEntityUuid.setStatus("current")
_NtxAlertSourceEntityName_Type = DisplayString
_NtxAlertSourceEntityName_Object = MibScalar
ntxAlertSourceEntityName = _NtxAlertSourceEntityName_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 9),
    _NtxAlertSourceEntityName_Type()
)
ntxAlertSourceEntityName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntxAlertSourceEntityName.setStatus("current")
_NtxAlertSourceEntityType_Type = DisplayString
_NtxAlertSourceEntityType_Object = MibScalar
ntxAlertSourceEntityType = _NtxAlertSourceEntityType_Object(
    (1, 3, 6, 1, 4, 1, 41263, 999, 10),
    _NtxAlertSourceEntityType_Type()
)
ntxAlertSourceEntityType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntxAlertSourceEntityType.setStatus("current")

# Managed Objects groups


# Notification objects

ntxTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 991)
)
ntxTrap.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"))
)
if mibBuilder.loadTexts:
    ntxTrap.setStatus(
        "current"
    )

ntxTrapResolved = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 993)
)
ntxTrapResolved.setObjects(
      *(("NUTANIX-MIB", "ntxTrapName"),
        ("NUTANIX-MIB", "ntxAlertResolvedTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapResolved.setStatus(
        "current"
    )

ntxTrapClusterRunningOutOfStorageCapacitylowRunway = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1000)
)
ntxTrapClusterRunningOutOfStorageCapacitylowRunway.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterRunningOutOfStorageCapacitylowRunway.setStatus(
        "current"
    )

ntxTrapClusterRunningOutOfCPUCapacitylowRunway = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1001)
)
ntxTrapClusterRunningOutOfCPUCapacitylowRunway.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterRunningOutOfCPUCapacitylowRunway.setStatus(
        "current"
    )

ntxTrapNodeRunningOutOfCPUCapacitylowRunway = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1002)
)
ntxTrapNodeRunningOutOfCPUCapacitylowRunway.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeRunningOutOfCPUCapacitylowRunway.setStatus(
        "current"
    )

ntxTrapClusterRunningOutOfMemoryCapacitylowRunway = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1003)
)
ntxTrapClusterRunningOutOfMemoryCapacitylowRunway.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterRunningOutOfMemoryCapacitylowRunway.setStatus(
        "current"
    )

ntxTrapNodeRunningOutOfMemoryCapacitylowRunway = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1004)
)
ntxTrapNodeRunningOutOfMemoryCapacitylowRunway.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeRunningOutOfMemoryCapacitylowRunway.setStatus(
        "current"
    )

ntxTrapStorageContainerRunningOutOfStorageCapacitylowRunway = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1005)
)
ntxTrapStorageContainerRunningOutOfStorageCapacitylowRunway.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStorageContainerRunningOutOfStorageCapacitylowRunway.setStatus(
        "current"
    )

ntxTrapTestAlertTitle = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1006)
)
ntxTrapTestAlertTitle.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTestAlertTitle.setStatus(
        "current"
    )

ntxTrapMetadataDriveAutoAddDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1007)
)
ntxTrapMetadataDriveAutoAddDisabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataDriveAutoAddDisabled.setStatus(
        "current"
    )

ntxTrapNodeDetachedFromMetadataRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1008)
)
ntxTrapNodeDetachedFromMetadataRing.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeDetachedFromMetadataRing.setStatus(
        "current"
    )

ntxTrapMetadataDynamicRingChangeOperationStuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1009)
)
ntxTrapMetadataDynamicRingChangeOperationStuck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataDynamicRingChangeOperationStuck.setStatus(
        "current"
    )

ntxTrapMetadataDynamicRingChangeOperationTooSlow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1010)
)
ntxTrapMetadataDynamicRingChangeOperationTooSlow.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataDynamicRingChangeOperationTooSlow.setStatus(
        "current"
    )

ntxTrapMetadataDriveFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1011)
)
ntxTrapMetadataDriveFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataDriveFailed.setStatus(
        "current"
    )

ntxTrapLargeMetadataSizeDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1012)
)
ntxTrapLargeMetadataSizeDetected.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLargeMetadataSizeDetected.setStatus(
        "current"
    )

ntxTrapMetadataDriveMarkedToBeAutoAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1013)
)
ntxTrapMetadataDriveMarkedToBeAutoAdded.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataDriveMarkedToBeAutoAdded.setStatus(
        "current"
    )

ntxTrapMetadataDriveDetached = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1014)
)
ntxTrapMetadataDriveDetached.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataDriveDetached.setStatus(
        "current"
    )

ntxTrapMetadataRingImbalance = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1015)
)
ntxTrapMetadataRingImbalance.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataRingImbalance.setStatus(
        "current"
    )

ntxTrapCassandraWaitingForDiskReplacement = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1016)
)
ntxTrapCassandraWaitingForDiskReplacement.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCassandraWaitingForDiskReplacement.setStatus(
        "current"
    )

ntxTrapCloudApplianceDeploymentFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1017)
)
ntxTrapCloudApplianceDeploymentFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCloudApplianceDeploymentFailed.setStatus(
        "current"
    )

ntxTrapUnableToRemountDatastore = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1018)
)
ntxTrapUnableToRemountDatastore.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnableToRemountDatastore.setStatus(
        "current"
    )

ntxTrapRemountedDatastore = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1019)
)
ntxTrapRemountedDatastore.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemountedDatastore.setStatus(
        "current"
    )

ntxTrapFailedToAllocateSnapshotReserveOnTheRemoteSite = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1020)
)
ntxTrapFailedToAllocateSnapshotReserveOnTheRemoteSite.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToAllocateSnapshotReserveOnTheRemoteSite.setStatus(
        "current"
    )

ntxTrapFailedToAllocateSnapshotReserve = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1021)
)
ntxTrapFailedToAllocateSnapshotReserve.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToAllocateSnapshotReserve.setStatus(
        "current"
    )

ntxTrapMetroTakeoverOldPrimarySiteIsHostingVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1022)
)
ntxTrapMetroTakeoverOldPrimarySiteIsHostingVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetroTakeoverOldPrimarySiteIsHostingVMs.setStatus(
        "current"
    )

ntxTrapProtectionDomainIsInDecoupledState = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1023)
)
ntxTrapProtectionDomainIsInDecoupledState.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainIsInDecoupledState.setStatus(
        "current"
    )

ntxTrapRemoteSiteLatencyIsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1024)
)
ntxTrapRemoteSiteLatencyIsHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteLatencyIsHigh.setStatus(
        "current"
    )

ntxTrapFailedToUpdateMetroAvailabilityFailureHandling = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1025)
)
ntxTrapFailedToUpdateMetroAvailabilityFailureHandling.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToUpdateMetroAvailabilityFailureHandling.setStatus(
        "current"
    )

ntxTrapStretchConnectivityIsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1026)
)
ntxTrapStretchConnectivityIsLost.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStretchConnectivityIsLost.setStatus(
        "current"
    )

ntxTrapVMRegistrationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1027)
)
ntxTrapVMRegistrationWarning.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRegistrationWarning.setStatus(
        "current"
    )

ntxTrapVMRenamedOnConversion = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1028)
)
ntxTrapVMRenamedOnConversion.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRenamedOnConversion.setStatus(
        "current"
    )

ntxTrapAuthenticationFailedInWitness = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1029)
)
ntxTrapAuthenticationFailedInWitness.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAuthenticationFailedInWitness.setStatus(
        "current"
    )

ntxTrapWitnessIsNotConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1030)
)
ntxTrapWitnessIsNotConfigured.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapWitnessIsNotConfigured.setStatus(
        "current"
    )

ntxTrapWitnessIsNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1031)
)
ntxTrapWitnessIsNotReachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapWitnessIsNotReachable.setStatus(
        "current"
    )

ntxTrapCuratorJobRunningTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1032)
)
ntxTrapCuratorJobRunningTooLong.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCuratorJobRunningTooLong.setStatus(
        "current"
    )

ntxTrapCuratorScanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1033)
)
ntxTrapCuratorScanFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCuratorScanFailure.setStatus(
        "current"
    )

ntxTrapFileServerSpaceUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1034)
)
ntxTrapFileServerSpaceUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerSpaceUsageHigh.setStatus(
        "current"
    )

ntxTrapFileServerSpaceUsageCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1035)
)
ntxTrapFileServerSpaceUsageCritical.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerSpaceUsageCritical.setStatus(
        "current"
    )

ntxTrapFileServerUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1036)
)
ntxTrapFileServerUnreachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerUnreachable.setStatus(
        "current"
    )

ntxTrapFileServerStorageIsNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1037)
)
ntxTrapFileServerStorageIsNotAvailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerStorageIsNotAvailable.setStatus(
        "current"
    )

ntxTrapFileServerScaleoutFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1038)
)
ntxTrapFileServerScaleoutFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerScaleoutFailed.setStatus(
        "current"
    )

ntxTrapFileServerCouldNotJoinTheADDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1039)
)
ntxTrapFileServerCouldNotJoinTheADDomain.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerCouldNotJoinTheADDomain.setStatus(
        "current"
    )

ntxTrapNodeFailedToJoinDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1040)
)
ntxTrapNodeFailedToJoinDomain.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeFailedToJoinDomain.setStatus(
        "current"
    )

ntxTrapFileServerTimeDifferenceHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1041)
)
ntxTrapFileServerTimeDifferenceHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerTimeDifferenceHigh.setStatus(
        "current"
    )

ntxTrapFileServerStorageCleanupFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1042)
)
ntxTrapFileServerStorageCleanupFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerStorageCleanupFailed.setStatus(
        "current"
    )

ntxTrapFileServerCannotConnectWithADServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1043)
)
ntxTrapFileServerCannotConnectWithADServer.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerCannotConnectWithADServer.setStatus(
        "current"
    )

ntxTrapFileServerPerformanceOptimizationRecommended = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1044)
)
ntxTrapFileServerPerformanceOptimizationRecommended.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerPerformanceOptimizationRecommended.setStatus(
        "current"
    )

ntxTrapAppropriateSiteNotFoundInActiveDirectory = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1045)
)
ntxTrapAppropriateSiteNotFoundInActiveDirectory.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAppropriateSiteNotFoundInActiveDirectory.setStatus(
        "current"
    )

ntxTrapFileServerDNSUpdatesPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1046)
)
ntxTrapFileServerDNSUpdatesPending.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerDNSUpdatesPending.setStatus(
        "current"
    )

ntxTrapUserQuotaAssignmentFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1047)
)
ntxTrapUserQuotaAssignmentFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUserQuotaAssignmentFailed.setStatus(
        "current"
    )

ntxTrapShareUtilizationReachedConfiguredLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1048)
)
ntxTrapShareUtilizationReachedConfiguredLimit.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapShareUtilizationReachedConfiguredLimit.setStatus(
        "current"
    )

ntxTrapFileServerFailedToGetUpdatedCVMIPAddress = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1049)
)
ntxTrapFileServerFailedToGetUpdatedCVMIPAddress.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerFailedToGetUpdatedCVMIPAddress.setStatus(
        "current"
    )

ntxTrapFileServerActivationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1050)
)
ntxTrapFileServerActivationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerActivationFailed.setStatus(
        "current"
    )

ntxTrapFailedToSetVMtoVMAntiaffinityRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1051)
)
ntxTrapFailedToSetVMtoVMAntiaffinityRule.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToSetVMtoVMAntiaffinityRule.setStatus(
        "current"
    )

ntxTrapFileServerHomeShareCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1052)
)
ntxTrapFileServerHomeShareCreationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerHomeShareCreationFailed.setStatus(
        "current"
    )

ntxTrapDiscoveryOfISCSITargetsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1053)
)
ntxTrapDiscoveryOfISCSITargetsFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDiscoveryOfISCSITargetsFailed.setStatus(
        "current"
    )

ntxTrapFileServerUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1054)
)
ntxTrapFileServerUpgradeFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerUpgradeFailed.setStatus(
        "current"
    )

ntxTrapIncompatibleFileServerActivated = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1055)
)
ntxTrapIncompatibleFileServerActivated.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIncompatibleFileServerActivated.setStatus(
        "current"
    )

ntxTrapFileServerInHeterogeneousState = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1056)
)
ntxTrapFileServerInHeterogeneousState.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerInHeterogeneousState.setStatus(
        "current"
    )

ntxTrapFailedToCorrectFileServerDataAndMetaDataInconsistencies = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1057)
)
ntxTrapFailedToCorrectFileServerDataAndMetaDataInconsistencies.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToCorrectFileServerDataAndMetaDataInconsistencies.setStatus(
        "current"
    )

ntxTrapFileServerShareDeletionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1058)
)
ntxTrapFileServerShareDeletionFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerShareDeletionFailed.setStatus(
        "current"
    )

ntxTrapFileServerCompatibilityCheckSkipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1059)
)
ntxTrapFileServerCompatibilityCheckSkipped.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerCompatibilityCheckSkipped.setStatus(
        "current"
    )

ntxTrapSnapshotInvalidForClone = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1060)
)
ntxTrapSnapshotInvalidForClone.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSnapshotInvalidForClone.setStatus(
        "current"
    )

ntxTrapFileServerAntiVirusICAPServerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1061)
)
ntxTrapFileServerAntiVirusICAPServerDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerAntiVirusICAPServerDown.setStatus(
        "current"
    )

ntxTrapFileServerAntiVirusAllICAPServersDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1062)
)
ntxTrapFileServerAntiVirusAllICAPServersDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerAntiVirusAllICAPServersDown.setStatus(
        "current"
    )

ntxTrapClusterInReadOnlyMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1063)
)
ntxTrapClusterInReadOnlyMode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterInReadOnlyMode.setStatus(
        "current"
    )

ntxTrapStorageContainerSpaceUsageExceededAOSCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1064)
)
ntxTrapStorageContainerSpaceUsageExceededAOSCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStorageContainerSpaceUsageExceededAOSCheck.setStatus(
        "current"
    )

ntxTrapDiskDiagnosticFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1065)
)
ntxTrapDiskDiagnosticFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDiskDiagnosticFailure.setStatus(
        "current"
    )

ntxTrapNodeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1066)
)
ntxTrapNodeFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeFailure.setStatus(
        "current"
    )

ntxTrapNodeInMaintenanceMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1067)
)
ntxTrapNodeInMaintenanceMode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeInMaintenanceMode.setStatus(
        "current"
    )

ntxTrapNonSelfEncryptionDriveDiskInserted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1068)
)
ntxTrapNonSelfEncryptionDriveDiskInserted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNonSelfEncryptionDriveDiskInserted.setStatus(
        "current"
    )

ntxTrapPhysicalDiskAddedToSlot = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1069)
)
ntxTrapPhysicalDiskAddedToSlot.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPhysicalDiskAddedToSlot.setStatus(
        "current"
    )

ntxTrapPhysicalDiskDriveHasFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1070)
)
ntxTrapPhysicalDiskDriveHasFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPhysicalDiskDriveHasFailed.setStatus(
        "current"
    )

ntxTrapPhysicalDiskRemovedFromSlot = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1071)
)
ntxTrapPhysicalDiskRemovedFromSlot.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPhysicalDiskRemovedFromSlot.setStatus(
        "current"
    )

ntxTrapSelfEncryptingDriveOperationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1072)
)
ntxTrapSelfEncryptingDriveOperationFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSelfEncryptingDriveOperationFailure.setStatus(
        "current"
    )

ntxTrapUnsupportedConfigurationForRedundancyFactor3 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1073)
)
ntxTrapUnsupportedConfigurationForRedundancyFactor3.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnsupportedConfigurationForRedundancyFactor3.setStatus(
        "current"
    )

ntxTrapCannotRemovePasswordProtectedDisks = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1074)
)
ntxTrapCannotRemovePasswordProtectedDisks.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCannotRemovePasswordProtectedDisks.setStatus(
        "current"
    )

ntxTrapDiskBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1075)
)
ntxTrapDiskBad.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDiskBad.setStatus(
        "current"
    )

ntxTrapDuplicateIPAddressDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1076)
)
ntxTrapDuplicateIPAddressDetected.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDuplicateIPAddressDetected.setStatus(
        "current"
    )

ntxTrapIPAddressNotHosted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1077)
)
ntxTrapIPAddressNotHosted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIPAddressNotHosted.setStatus(
        "current"
    )

ntxTrapSMTPError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1078)
)
ntxTrapSMTPError.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSMTPError.setStatus(
        "current"
    )

ntxTrapProtectionDomainReplicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1079)
)
ntxTrapProtectionDomainReplicationFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainReplicationFailure.setStatus(
        "current"
    )

ntxTrapProtectionDomainSnapshotFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1080)
)
ntxTrapProtectionDomainSnapshotFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainSnapshotFailure.setStatus(
        "current"
    )

ntxTrapNutanixGuestToolsAgentIsNotReachableOnTheVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1081)
)
ntxTrapNutanixGuestToolsAgentIsNotReachableOnTheVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixGuestToolsAgentIsNotReachableOnTheVM.setStatus(
        "current"
    )

ntxTrapMetroAvailabilityIsPromoted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1082)
)
ntxTrapMetroAvailabilityIsPromoted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetroAvailabilityIsPromoted.setStatus(
        "current"
    )

ntxTrapEntityRestoreAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1083)
)
ntxTrapEntityRestoreAborted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntityRestoreAborted.setStatus(
        "current"
    )

ntxTrapProtectionDomainReceiveSnapshotFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1084)
)
ntxTrapProtectionDomainReceiveSnapshotFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainReceiveSnapshotFailure.setStatus(
        "current"
    )

ntxTrapSecureTunnelToRemoteSiteDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1085)
)
ntxTrapSecureTunnelToRemoteSiteDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSecureTunnelToRemoteSiteDown.setStatus(
        "current"
    )

ntxTrapProtectedVolumeGroupNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1086)
)
ntxTrapProtectedVolumeGroupNotFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVolumeGroupNotFound.setStatus(
        "current"
    )

ntxTrapProtectionDomainActivation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1087)
)
ntxTrapProtectionDomainActivation.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainActivation.setStatus(
        "current"
    )

ntxTrapDuplicateRemoteClusterID = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1088)
)
ntxTrapDuplicateRemoteClusterID.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDuplicateRemoteClusterID.setStatus(
        "current"
    )

ntxTrapCloudRemoteSiteFailedToStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1089)
)
ntxTrapCloudRemoteSiteFailedToStart.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCloudRemoteSiteFailedToStart.setStatus(
        "current"
    )

ntxTrapRemoteSiteremotenameNetworkMappingMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1090)
)
ntxTrapRemoteSiteremotenameNetworkMappingMissing.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteremotenameNetworkMappingMissing.setStatus(
        "current"
    )

ntxTrapOperationForwardedToCloudRemoteFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1091)
)
ntxTrapOperationForwardedToCloudRemoteFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOperationForwardedToCloudRemoteFailed.setStatus(
        "current"
    )

ntxTrapRecoveryPointObjectiveCannotBeMet = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1092)
)
ntxTrapRecoveryPointObjectiveCannotBeMet.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPointObjectiveCannotBeMet.setStatus(
        "current"
    )

ntxTrapVStoreSnapshotStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1093)
)
ntxTrapVStoreSnapshotStatus.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVStoreSnapshotStatus.setStatus(
        "current"
    )

ntxTrapProtectionDomainSnapshotOperationSkipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1094)
)
ntxTrapProtectionDomainSnapshotOperationSkipped.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainSnapshotOperationSkipped.setStatus(
        "current"
    )

ntxTrapSkippedReplicationOfTheSnapshot = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1095)
)
ntxTrapSkippedReplicationOfTheSnapshot.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSkippedReplicationOfTheSnapshot.setStatus(
        "current"
    )

ntxTrapFailedToSnapshotEntities = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1096)
)
ntxTrapFailedToSnapshotEntities.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToSnapshotEntities.setStatus(
        "current"
    )

ntxTrapIncorrectClusterInformationInRemoteSite = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1097)
)
ntxTrapIncorrectClusterInformationInRemoteSite.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIncorrectClusterInformationInRemoteSite.setStatus(
        "current"
    )

ntxTrapVStoreIsBeingReplicatedToBackupOnlyRemoteSite = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1098)
)
ntxTrapVStoreIsBeingReplicatedToBackupOnlyRemoteSite.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVStoreIsBeingReplicatedToBackupOnlyRemoteSite.setStatus(
        "current"
    )

ntxTrapFailedToChangeStateOfOneOrMoreVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1099)
)
ntxTrapFailedToChangeStateOfOneOrMoreVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToChangeStateOfOneOrMoreVMs.setStatus(
        "current"
    )

ntxTrapRegistrationOfOneOrMoreVMsFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1100)
)
ntxTrapRegistrationOfOneOrMoreVMsFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRegistrationOfOneOrMoreVMsFailed.setStatus(
        "current"
    )

ntxTrapSelfServiceRestoreOperationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1101)
)
ntxTrapSelfServiceRestoreOperationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSelfServiceRestoreOperationFailed.setStatus(
        "current"
    )

ntxTrapMetadataVolumeSnapshotPersistentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1102)
)
ntxTrapMetadataVolumeSnapshotPersistentFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataVolumeSnapshotPersistentFailure.setStatus(
        "current"
    )

ntxTrapMetroAvailabilityIsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1103)
)
ntxTrapMetroAvailabilityIsDisabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetroAvailabilityIsDisabled.setStatus(
        "current"
    )

ntxTrapApplicationconsistentSnapshotNotTakenForTheVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1104)
)
ntxTrapApplicationconsistentSnapshotNotTakenForTheVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapApplicationconsistentSnapshotNotTakenForTheVM.setStatus(
        "current"
    )

ntxTrapInvalidConsistencyGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1105)
)
ntxTrapInvalidConsistencyGroup.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInvalidConsistencyGroup.setStatus(
        "current"
    )

ntxTrapFailedToReconfigureNutanixGuestToolsForTheRecoveredVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1106)
)
ntxTrapFailedToReconfigureNutanixGuestToolsForTheRecoveredVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToReconfigureNutanixGuestToolsForTheRecoveredVM.setStatus(
        "current"
    )

ntxTrapNutanixGuestToolsNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1107)
)
ntxTrapNutanixGuestToolsNotInstalled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixGuestToolsNotInstalled.setStatus(
        "current"
    )

ntxTrapRemoteSiteremotenameNetworkMappingInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1108)
)
ntxTrapRemoteSiteremotenameNetworkMappingInvalid.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteremotenameNetworkMappingInvalid.setStatus(
        "current"
    )

ntxTrapVSSSnapshotFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1109)
)
ntxTrapVSSSnapshotFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVSSSnapshotFailed.setStatus(
        "current"
    )

ntxTrapAlertRaisedOnCloudRemoteSiteremotenamealertmessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1110)
)
ntxTrapAlertRaisedOnCloudRemoteSiteremotenamealertmessage.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAlertRaisedOnCloudRemoteSiteremotenamealertmessage.setStatus(
        "current"
    )

ntxTrapProtectedVmsNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1111)
)
ntxTrapProtectedVmsNotFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVmsNotFound.setStatus(
        "current"
    )

ntxTrapProtectionDomainContainsMoreThanSpecifiedVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1112)
)
ntxTrapProtectionDomainContainsMoreThanSpecifiedVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainContainsMoreThanSpecifiedVMs.setStatus(
        "current"
    )

ntxTrapRelatedEntityProtectionStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1113)
)
ntxTrapRelatedEntityProtectionStatus.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRelatedEntityProtectionStatus.setStatus(
        "current"
    )

ntxTrapNutanixGuestToolsIsNotSupportedOnRemoteSite = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1114)
)
ntxTrapNutanixGuestToolsIsNotSupportedOnRemoteSite.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixGuestToolsIsNotSupportedOnRemoteSite.setStatus(
        "current"
    )

ntxTrapRemoteSiteOperationModeReadOnly = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1115)
)
ntxTrapRemoteSiteOperationModeReadOnly.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteOperationModeReadOnly.setStatus(
        "current"
    )

ntxTrapRemoteSiteIsUnhealthy = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1116)
)
ntxTrapRemoteSiteIsUnhealthy.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteIsUnhealthy.setStatus(
        "current"
    )

ntxTrapEntitiesRestoredButUnprotected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1117)
)
ntxTrapEntitiesRestoredButUnprotected.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntitiesRestoredButUnprotected.setStatus(
        "current"
    )

ntxTrapProtectionDomainFullReplicationPerformed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1118)
)
ntxTrapProtectionDomainFullReplicationPerformed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainFullReplicationPerformed.setStatus(
        "current"
    )

ntxTrapProtectedVMIsNotNutanixBackupAndRecoveryCompliant = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1119)
)
ntxTrapProtectedVMIsNotNutanixBackupAndRecoveryCompliant.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMIsNotNutanixBackupAndRecoveryCompliant.setStatus(
        "current"
    )

ntxTrapProtectedVMRenamedDuringClone = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1120)
)
ntxTrapProtectedVMRenamedDuringClone.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMRenamedDuringClone.setStatus(
        "current"
    )

ntxTrapProtectedVolumeGroupsNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1121)
)
ntxTrapProtectedVolumeGroupsNotFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVolumeGroupsNotFound.setStatus(
        "current"
    )

ntxTrapVMRegistrationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1122)
)
ntxTrapVMRegistrationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRegistrationFailed.setStatus(
        "current"
    )

ntxTrapProtectionDomainReplicationExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1123)
)
ntxTrapProtectionDomainReplicationExpired.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainReplicationExpired.setStatus(
        "current"
    )

ntxTrapVolumeGroupAttachmentsNotRestored = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1124)
)
ntxTrapVolumeGroupAttachmentsNotRestored.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVolumeGroupAttachmentsNotRestored.setStatus(
        "current"
    )

ntxTrapEntitiesSkippedDuringRestore = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1125)
)
ntxTrapEntitiesSkippedDuringRestore.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntitiesSkippedDuringRestore.setStatus(
        "current"
    )

ntxTrapProtectionDomainChangeModeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1126)
)
ntxTrapProtectionDomainChangeModeFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainChangeModeFailure.setStatus(
        "current"
    )

ntxTrapVSSSnapshotAborted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1127)
)
ntxTrapVSSSnapshotAborted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVSSSnapshotAborted.setStatus(
        "current"
    )

ntxTrapExternalISCSIAttachmentsNotSnapshotted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1128)
)
ntxTrapExternalISCSIAttachmentsNotSnapshotted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapExternalISCSIAttachmentsNotSnapshotted.setStatus(
        "current"
    )

ntxTrapVMVirtualHardwareVersionNotCompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1129)
)
ntxTrapVMVirtualHardwareVersionNotCompatible.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMVirtualHardwareVersionNotCompatible.setStatus(
        "current"
    )

ntxTrapVolumeGroupActionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1130)
)
ntxTrapVolumeGroupActionError.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVolumeGroupActionError.setStatus(
        "current"
    )

ntxTrapMetadataVolumeSnapshotTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1131)
)
ntxTrapMetadataVolumeSnapshotTimeout.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataVolumeSnapshotTimeout.setStatus(
        "current"
    )

ntxTrapSnapshotPartiallyCrashConsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1132)
)
ntxTrapSnapshotPartiallyCrashConsistent.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSnapshotPartiallyCrashConsistent.setStatus(
        "current"
    )

ntxTrapMetroAvailabilityPrechecksFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1133)
)
ntxTrapMetroAvailabilityPrechecksFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetroAvailabilityPrechecksFailed.setStatus(
        "current"
    )

ntxTrapProtectionDomainMightHaveSymlinks = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1134)
)
ntxTrapProtectionDomainMightHaveSymlinks.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainMightHaveSymlinks.setStatus(
        "current"
    )

ntxTrapVSSSnapshotIsNotSupportedForTheVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1135)
)
ntxTrapVSSSnapshotIsNotSupportedForTheVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVSSSnapshotIsNotSupportedForTheVM.setStatus(
        "current"
    )

ntxTrapSnapshotReserveOnSSDIsFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1136)
)
ntxTrapSnapshotReserveOnSSDIsFull.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSnapshotReserveOnSSDIsFull.setStatus(
        "current"
    )

ntxTrapMetroAvailabilityConfigurationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1137)
)
ntxTrapMetroAvailabilityConfigurationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetroAvailabilityConfigurationFailed.setStatus(
        "current"
    )

ntxTrapStaleNFSMount = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1138)
)
ntxTrapStaleNFSMount.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStaleNFSMount.setStatus(
        "current"
    )

ntxTrapVSSSoftwareOrprefreezepostthawScriptsNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1139)
)
ntxTrapVSSSoftwareOrprefreezepostthawScriptsNotInstalled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVSSSoftwareOrprefreezepostthawScriptsNotInstalled.setStatus(
        "current"
    )

ntxTrapProtectedVMNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1140)
)
ntxTrapProtectedVMNotFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMNotFound.setStatus(
        "current"
    )

ntxTrapProtectionDomainTransitioningToLowerFrequencySnapshotting = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1141)
)
ntxTrapProtectionDomainTransitioningToLowerFrequencySnapshotting.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainTransitioningToLowerFrequencySnapshotting.setStatus(
        "current"
    )

ntxTrapSnapshotQueuedForReplicationsToRemoteSite = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1142)
)
ntxTrapSnapshotQueuedForReplicationsToRemoteSite.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSnapshotQueuedForReplicationsToRemoteSite.setStatus(
        "current"
    )

ntxTrapAgentVMRestorationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1143)
)
ntxTrapAgentVMRestorationFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAgentVMRestorationFailure.setStatus(
        "current"
    )

ntxTrapCPSDeploymentEvaluationMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1144)
)
ntxTrapCPSDeploymentEvaluationMode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPSDeploymentEvaluationMode.setStatus(
        "current"
    )

ntxTrapHAHostEvacuationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1145)
)
ntxTrapHAHostEvacuationFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHAHostEvacuationFailure.setStatus(
        "current"
    )

ntxTrapFailureToRestartVMsForHAEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1146)
)
ntxTrapFailureToRestartVMsForHAEvent.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailureToRestartVMsForHAEvent.setStatus(
        "current"
    )

ntxTrapUpgradeBundleAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1147)
)
ntxTrapUpgradeBundleAvailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUpgradeBundleAvailable.setStatus(
        "current"
    )

ntxTrapVMActionError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1148)
)
ntxTrapVMActionError.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMActionError.setStatus(
        "current"
    )

ntxTrapHAHealingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1149)
)
ntxTrapHAHealingFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHAHealingFailure.setStatus(
        "current"
    )

ntxTrapVmHighAvailabilityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1150)
)
ntxTrapVmHighAvailabilityFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVmHighAvailabilityFailure.setStatus(
        "current"
    )

ntxTrapKerberosClockSkewFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1151)
)
ntxTrapKerberosClockSkewFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapKerberosClockSkewFailure.setStatus(
        "current"
    )

ntxTrapStargateTemporarilyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1152)
)
ntxTrapStargateTemporarilyDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStargateTemporarilyDown.setStatus(
        "current"
    )

ntxTrapVMGroupSnapshotAndCurrentMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1153)
)
ntxTrapVMGroupSnapshotAndCurrentMismatch.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMGroupSnapshotAndCurrentMismatch.setStatus(
        "current"
    )

ntxTrapCertificateCreationError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1154)
)
ntxTrapCertificateCreationError.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCertificateCreationError.setStatus(
        "current"
    )

ntxTrapFingerprintingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1156)
)
ntxTrapFingerprintingDisabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFingerprintingDisabled.setStatus(
        "current"
    )

ntxTrapSystemDefinedFlashModeUsageLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1157)
)
ntxTrapSystemDefinedFlashModeUsageLimitExceeded.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSystemDefinedFlashModeUsageLimitExceeded.setStatus(
        "current"
    )

ntxTrapMetadataUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1158)
)
ntxTrapMetadataUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataUsageHigh.setStatus(
        "current"
    )

ntxTrapNFSMetadataSizeOvershoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1159)
)
ntxTrapNFSMetadataSizeOvershoot.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNFSMetadataSizeOvershoot.setStatus(
        "current"
    )

ntxTrapOnDiskDedupDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1160)
)
ntxTrapOnDiskDedupDisabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOnDiskDedupDisabled.setStatus(
        "current"
    )

ntxTrapSpaceReservationViolated = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1161)
)
ntxTrapSpaceReservationViolated.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSpaceReservationViolated.setStatus(
        "current"
    )

ntxTrapPossibleDegradedNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1164)
)
ntxTrapPossibleDegradedNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPossibleDegradedNode.setStatus(
        "current"
    )

ntxTrapDynamicSchedulingFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1165)
)
ntxTrapDynamicSchedulingFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDynamicSchedulingFailure.setStatus(
        "current"
    )

ntxTrapRecoveredVMDiskConfigurationUpdateFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1166)
)
ntxTrapRecoveredVMDiskConfigurationUpdateFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveredVMDiskConfigurationUpdateFailed.setStatus(
        "current"
    )

ntxTrapISCSIConfigurationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1167)
)
ntxTrapISCSIConfigurationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapISCSIConfigurationFailed.setStatus(
        "current"
    )

ntxTrapA130104 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1168)
)
ntxTrapA130104.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130104.setStatus(
        "current"
    )

ntxTrapExecutionOfThePostThawScriptFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1169)
)
ntxTrapExecutionOfThePostThawScriptFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapExecutionOfThePostThawScriptFailed.setStatus(
        "current"
    )

ntxTrapNutanixGuestToolsMountFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1170)
)
ntxTrapNutanixGuestToolsMountFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixGuestToolsMountFailed.setStatus(
        "current"
    )

ntxTrapVMForciblyPoweredOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1171)
)
ntxTrapVMForciblyPoweredOff.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMForciblyPoweredOff.setStatus(
        "current"
    )

ntxTrapReportGenerationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1172)
)
ntxTrapReportGenerationFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapReportGenerationFailure.setStatus(
        "current"
    )

ntxTrapSendReportThroughEmailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1173)
)
ntxTrapSendReportThroughEmailFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSendReportThroughEmailFailure.setStatus(
        "current"
    )

ntxTrapReportQuotaScanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1174)
)
ntxTrapReportQuotaScanFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapReportQuotaScanFailure.setStatus(
        "current"
    )

ntxTrapCassandraServiceCrashed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1175)
)
ntxTrapCassandraServiceCrashed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCassandraServiceCrashed.setStatus(
        "current"
    )

ntxTrapCassandraServiceIsRunningOutOfMemory = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1176)
)
ntxTrapCassandraServiceIsRunningOutOfMemory.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCassandraServiceIsRunningOutOfMemory.setStatus(
        "current"
    )

ntxTrapMultipleCassandraNodesHaveSimilarTokens = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1177)
)
ntxTrapMultipleCassandraNodesHaveSimilarTokens.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMultipleCassandraNodesHaveSimilarTokens.setStatus(
        "current"
    )

ntxTrapCloudClusterDoesNotHaveRecommendedConfigurationLocally = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1178)
)
ntxTrapCloudClusterDoesNotHaveRecommendedConfigurationLocally.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCloudClusterDoesNotHaveRecommendedConfigurationLocally.setStatus(
        "current"
    )

ntxTrapAWSCloudInstanceNotConfiguredProperly = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1179)
)
ntxTrapAWSCloudInstanceNotConfiguredProperly.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAWSCloudInstanceNotConfiguredProperly.setStatus(
        "current"
    )

ntxTrapOldGenerationAWSInstanceConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1180)
)
ntxTrapOldGenerationAWSInstanceConfigured.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOldGenerationAWSInstanceConfigured.setStatus(
        "current"
    )

ntxTrapAOSVersionOfCloudRemoteSiteIsLessThanSourceCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1181)
)
ntxTrapAOSVersionOfCloudRemoteSiteIsLessThanSourceCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAOSVersionOfCloudRemoteSiteIsLessThanSourceCluster.setStatus(
        "current"
    )

ntxTrapCloudClusterDoesNotHaveAllRecommendedGflagsSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1182)
)
ntxTrapCloudClusterDoesNotHaveAllRecommendedGflagsSet.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCloudClusterDoesNotHaveAllRecommendedGflagsSet.setStatus(
        "current"
    )

ntxTrapEgroupCountOnCloudDiskIsHigherThanTheRecommendedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1183)
)
ntxTrapEgroupCountOnCloudDiskIsHigherThanTheRecommendedThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEgroupCountOnCloudDiskIsHigherThanTheRecommendedThreshold.setStatus(
        "current"
    )

ntxTrapFileServerMutipleVMsOnSingleNodeCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1184)
)
ntxTrapFileServerMutipleVMsOnSingleNodeCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerMutipleVMsOnSingleNodeCheck.setStatus(
        "current"
    )

ntxTrapFileServerServicesDownCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1185)
)
ntxTrapFileServerServicesDownCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerServicesDownCheck.setStatus(
        "current"
    )

ntxTrapFileServerUnreachableCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1186)
)
ntxTrapFileServerUnreachableCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerUnreachableCheck.setStatus(
        "current"
    )

ntxTrapFileServerDownCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1187)
)
ntxTrapFileServerDownCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerDownCheck.setStatus(
        "current"
    )

ntxTrapFileServerInvalidSnapshot = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1188)
)
ntxTrapFileServerInvalidSnapshot.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerInvalidSnapshot.setStatus(
        "current"
    )

ntxTrapFileServerEntitiesNotProtected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1189)
)
ntxTrapFileServerEntitiesNotProtected.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerEntitiesNotProtected.setStatus(
        "current"
    )

ntxTrapMultipleFileServerVersionsArePresentInTheCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1190)
)
ntxTrapMultipleFileServerVersionsArePresentInTheCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMultipleFileServerVersionsArePresentInTheCluster.setStatus(
        "current"
    )

ntxTrapFileServerUpgradeTaskHungForTooLong = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1191)
)
ntxTrapFileServerUpgradeTaskHungForTooLong.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerUpgradeTaskHungForTooLong.setStatus(
        "current"
    )

ntxTrapFileServerPDActivatesOnMultipleSites = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1192)
)
ntxTrapFileServerPDActivatesOnMultipleSites.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerPDActivatesOnMultipleSites.setStatus(
        "current"
    )

ntxTrapFileServerPDEnabledOnNoncompatibleRemoteSite = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1193)
)
ntxTrapFileServerPDEnabledOnNoncompatibleRemoteSite.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerPDEnabledOnNoncompatibleRemoteSite.setStatus(
        "current"
    )

ntxTrapHardwareClockFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1194)
)
ntxTrapHardwareClockFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHardwareClockFailure.setStatus(
        "current"
    )

ntxTrapWsmanConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1195)
)
ntxTrapWsmanConnectivityLost.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapWsmanConnectivityLost.setStatus(
        "current"
    )

ntxTrapVMMigrationCompromised = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1196)
)
ntxTrapVMMigrationCompromised.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMMigrationCompromised.setStatus(
        "current"
    )

ntxTrapCVMMemoryReservationIsIncorrectlyConfigured = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1197)
)
ntxTrapCVMMemoryReservationIsIncorrectlyConfigured.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMMemoryReservationIsIncorrectlyConfigured.setStatus(
        "current"
    )

ntxTrapHostMissingCriticalWindowsUpdates = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1198)
)
ntxTrapHostMissingCriticalWindowsUpdates.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHostMissingCriticalWindowsUpdates.setStatus(
        "current"
    )

ntxTrapHostdServiceNotRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1200)
)
ntxTrapHostdServiceNotRunning.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHostdServiceNotRunning.setStatus(
        "current"
    )

ntxTrapIncorrectKerberosSetup = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1201)
)
ntxTrapIncorrectKerberosSetup.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIncorrectKerberosSetup.setStatus(
        "current"
    )

ntxTrapUnableToConnectToVCenter = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1202)
)
ntxTrapUnableToConnectToVCenter.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnableToConnectToVCenter.setStatus(
        "current"
    )

ntxTrapVMHasNonASCIIName = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1203)
)
ntxTrapVMHasNonASCIIName.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMHasNonASCIIName.setStatus(
        "current"
    )

ntxTrapFanSpeedLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1204)
)
ntxTrapFanSpeedLow.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFanSpeedLow.setStatus(
        "current"
    )

ntxTrapFanSpeedHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1205)
)
ntxTrapFanSpeedHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFanSpeedHigh.setStatus(
        "current"
    )

ntxTrapRAMFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1206)
)
ntxTrapRAMFault.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRAMFault.setStatus(
        "current"
    )

ntxTrapPowerSupplyDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1207)
)
ntxTrapPowerSupplyDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPowerSupplyDown.setStatus(
        "current"
    )

ntxTrapCPUTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1208)
)
ntxTrapCPUTemperatureHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPUTemperatureHigh.setStatus(
        "current"
    )

ntxTrapCPUTemperatureReadingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1209)
)
ntxTrapCPUTemperatureReadingError.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPUTemperatureReadingError.setStatus(
        "current"
    )

ntxTrapCPUVoltageAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1210)
)
ntxTrapCPUVoltageAbnormal.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPUVoltageAbnormal.setStatus(
        "current"
    )

ntxTrapCPUVRMTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1211)
)
ntxTrapCPUVRMTemperatureHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPUVRMTemperatureHigh.setStatus(
        "current"
    )

ntxTrapRAMTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1212)
)
ntxTrapRAMTemperatureHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRAMTemperatureHigh.setStatus(
        "current"
    )

ntxTrapRAMVoltageAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1213)
)
ntxTrapRAMVoltageAbnormal.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRAMVoltageAbnormal.setStatus(
        "current"
    )

ntxTrapRAMVRMTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1214)
)
ntxTrapRAMVRMTemperatureHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRAMVRMTemperatureHigh.setStatus(
        "current"
    )

ntxTrapSystemTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1215)
)
ntxTrapSystemTemperatureHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSystemTemperatureHigh.setStatus(
        "current"
    )

ntxTrapGPUTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1216)
)
ntxTrapGPUTemperatureHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapGPUTemperatureHigh.setStatus(
        "current"
    )

ntxTrapIPMIError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1217)
)
ntxTrapIPMIError.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIPMIError.setStatus(
        "current"
    )

ntxTrapGPUFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1218)
)
ntxTrapGPUFault.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapGPUFault.setStatus(
        "current"
    )

ntxTrapHighNumberOfCorrectableECCErrorsInLast1Day = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1219)
)
ntxTrapHighNumberOfCorrectableECCErrorsInLast1Day.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHighNumberOfCorrectableECCErrorsInLast1Day.setStatus(
        "current"
    )

ntxTrapHighNumberOfCorrectableECCErrorsInLast10Days = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1220)
)
ntxTrapHighNumberOfCorrectableECCErrorsInLast10Days.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHighNumberOfCorrectableECCErrorsInLast10Days.setStatus(
        "current"
    )

ntxTrapLicenseExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1221)
)
ntxTrapLicenseExpiry.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLicenseExpiry.setStatus(
        "current"
    )

ntxTrapLicenseFeatureViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1222)
)
ntxTrapLicenseFeatureViolation.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLicenseFeatureViolation.setStatus(
        "current"
    )

ntxTrapLicenseStandbyMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1223)
)
ntxTrapLicenseStandbyMode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLicenseStandbyMode.setStatus(
        "current"
    )

ntxTrapLicenseNodeInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1224)
)
ntxTrapLicenseNodeInvalid.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLicenseNodeInvalid.setStatus(
        "current"
    )

ntxTrapSecondaryPDsNotInSync = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1225)
)
ntxTrapSecondaryPDsNotInSync.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSecondaryPDsNotInSync.setStatus(
        "current"
    )

ntxTrapNoCheckpointSnapshotsOnMetroPDInLastHour = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1226)
)
ntxTrapNoCheckpointSnapshotsOnMetroPDInLastHour.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNoCheckpointSnapshotsOnMetroPDInLastHour.setStatus(
        "current"
    )

ntxTrapCVMTimeDifferenceHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1227)
)
ntxTrapCVMTimeDifferenceHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMTimeDifferenceHigh.setStatus(
        "current"
    )

ntxTrapIPMIIPNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1228)
)
ntxTrapIPMIIPNotReachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIPMIIPNotReachable.setStatus(
        "current"
    )

ntxTrapHostIPNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1229)
)
ntxTrapHostIPNotReachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHostIPNotReachable.setStatus(
        "current"
    )

ntxTrapCVMNICSpeedLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1230)
)
ntxTrapCVMNICSpeedLow.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMNICSpeedLow.setStatus(
        "current"
    )

ntxTrapCVMNotUplinkedToActive10GbpsLink = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1231)
)
ntxTrapCVMNotUplinkedToActive10GbpsLink.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMNotUplinkedToActive10GbpsLink.setStatus(
        "current"
    )

ntxTrapNICErrorRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1232)
)
ntxTrapNICErrorRateHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNICErrorRateHigh.setStatus(
        "current"
    )

ntxTrapCVMHostSubnetMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1233)
)
ntxTrapCVMHostSubnetMismatch.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMHostSubnetMismatch.setStatus(
        "current"
    )

ntxTrapNICLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1234)
)
ntxTrapNICLinkDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNICLinkDown.setStatus(
        "current"
    )

ntxTrapCVMIPAddressMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1235)
)
ntxTrapCVMIPAddressMismatch.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMIPAddressMismatch.setStatus(
        "current"
    )

ntxTrapZeusConfigMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1236)
)
ntxTrapZeusConfigMismatch.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapZeusConfigMismatch.setStatus(
        "current"
    )

ntxTrapIPMIIPAddressMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1237)
)
ntxTrapIPMIIPAddressMismatch.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIPMIIPAddressMismatch.setStatus(
        "current"
    )

ntxTrapJumboFramesEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1238)
)
ntxTrapJumboFramesEnabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapJumboFramesEnabled.setStatus(
        "current"
    )

ntxTrapNICFlaps = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1239)
)
ntxTrapNICFlaps.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNICFlaps.setStatus(
        "current"
    )

ntxTrapIncorrectNTPConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1240)
)
ntxTrapIncorrectNTPConfiguration.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIncorrectNTPConfiguration.setStatus(
        "current"
    )

ntxTrapCVMIsUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1241)
)
ntxTrapCVMIsUnreachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMIsUnreachable.setStatus(
        "current"
    )

ntxTrapNGTInstallationRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1242)
)
ntxTrapNGTInstallationRequired.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNGTInstallationRequired.setStatus(
        "current"
    )

ntxTrapTooManyFilesInTheProtectionDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1243)
)
ntxTrapTooManyFilesInTheProtectionDomain.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTooManyFilesInTheProtectionDomain.setStatus(
        "current"
    )

ntxTrapTooManyFilesInTheConsistencyGroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1244)
)
ntxTrapTooManyFilesInTheConsistencyGroup.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTooManyFilesInTheConsistencyGroup.setStatus(
        "current"
    )

ntxTrapFoundOldClonesOnCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1245)
)
ntxTrapFoundOldClonesOnCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFoundOldClonesOnCluster.setStatus(
        "current"
    )

ntxTrapTooManyClonesOnCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1246)
)
ntxTrapTooManyClonesOnCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTooManyClonesOnCluster.setStatus(
        "current"
    )

ntxTrapProtectingVMsThatAreUsingSharedVHDXDisksIsUnsupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1247)
)
ntxTrapProtectingVMsThatAreUsingSharedVHDXDisksIsUnsupported.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectingVMsThatAreUsingSharedVHDXDisksIsUnsupported.setStatus(
        "current"
    )

ntxTrapSymlinksFoundOnMetrovstoreProtectedContainer = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1248)
)
ntxTrapSymlinksFoundOnMetrovstoreProtectedContainer.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSymlinksFoundOnMetrovstoreProtectedContainer.setStatus(
        "current"
    )

ntxTrapAgedThirdpartyBackupSnapshotsPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1249)
)
ntxTrapAgedThirdpartyBackupSnapshotsPresent.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAgedThirdpartyBackupSnapshotsPresent.setStatus(
        "current"
    )

ntxTrapProtectionDomainContainsMoreThanOneEntity = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1250)
)
ntxTrapProtectionDomainContainsMoreThanOneEntity.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainContainsMoreThanOneEntity.setStatus(
        "current"
    )

ntxTrapRemoteSiteConnectivityNotNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1251)
)
ntxTrapRemoteSiteConnectivityNotNormal.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteConnectivityNotNormal.setStatus(
        "current"
    )

ntxTrapCPUAverageLoadHighOnControllerVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1252)
)
ntxTrapCPUAverageLoadHighOnControllerVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPUAverageLoadHighOnControllerVM.setStatus(
        "current"
    )

ntxTrapCPUAverageLoadCriticallyHighOnControllerVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1253)
)
ntxTrapCPUAverageLoadCriticallyHighOnControllerVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPUAverageLoadCriticallyHighOnControllerVM.setStatus(
        "current"
    )

ntxTrapControllerVMCertificateExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1254)
)
ntxTrapControllerVMCertificateExpiring.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapControllerVMCertificateExpiring.setStatus(
        "current"
    )

ntxTrapClusterCertificateExpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1255)
)
ntxTrapClusterCertificateExpiring.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterCertificateExpiring.setStatus(
        "current"
    )

ntxTrapRemoteSiteInsecure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1256)
)
ntxTrapRemoteSiteInsecure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteInsecure.setStatus(
        "current"
    )

ntxTrapMixedSelfEncryptingDriveHardware = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1257)
)
ntxTrapMixedSelfEncryptingDriveHardware.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMixedSelfEncryptingDriveHardware.setStatus(
        "current"
    )

ntxTrapKeyManagementServerUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1258)
)
ntxTrapKeyManagementServerUnavailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapKeyManagementServerUnavailable.setStatus(
        "current"
    )

ntxTrapNumberOfOrphanedEgroupsIsOverTheRecommendedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1259)
)
ntxTrapNumberOfOrphanedEgroupsIsOverTheRecommendedThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNumberOfOrphanedEgroupsIsOverTheRecommendedThreshold.setStatus(
        "current"
    )

ntxTrapCVMRAMUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1260)
)
ntxTrapCVMRAMUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMRAMUsageHigh.setStatus(
        "current"
    )

ntxTrapClusterServicesAreDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1261)
)
ntxTrapClusterServicesAreDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterServicesAreDown.setStatus(
        "current"
    )

ntxTrapKernelMemoryUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1262)
)
ntxTrapKernelMemoryUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapKernelMemoryUsageHigh.setStatus(
        "current"
    )

ntxTrapCVMServicesRestartingFrequently = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1263)
)
ntxTrapCVMServicesRestartingFrequently.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMServicesRestartingFrequently.setStatus(
        "current"
    )

ntxTrapClusterServiceRestartingFrequently = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1264)
)
ntxTrapClusterServiceRestartingFrequently.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterServiceRestartingFrequently.setStatus(
        "current"
    )

ntxTrapCVMConnectivityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1265)
)
ntxTrapCVMConnectivityFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMConnectivityFailure.setStatus(
        "current"
    )

ntxTrapStorageContainerReplicationFactorLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1266)
)
ntxTrapStorageContainerReplicationFactorLow.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStorageContainerReplicationFactorLow.setStatus(
        "current"
    )

ntxTrapCVMRebooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1267)
)
ntxTrapCVMRebooted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMRebooted.setStatus(
        "current"
    )

ntxTrapRemoteSupportEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1268)
)
ntxTrapRemoteSupportEnabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSupportEnabled.setStatus(
        "current"
    )

ntxTrapDatastoreVMCountHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1269)
)
ntxTrapDatastoreVMCountHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDatastoreVMCountHigh.setStatus(
        "current"
    )

ntxTrapHighVDiskCountInTheCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1270)
)
ntxTrapHighVDiskCountInTheCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHighVDiskCountInTheCluster.setStatus(
        "current"
    )

ntxTrapAllFlashNodesMixedWithNonallflashNodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1271)
)
ntxTrapAllFlashNodesMixedWithNonallflashNodes.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAllFlashNodesMixedWithNonallflashNodes.setStatus(
        "current"
    )

ntxTrapHaswellAndBroadwellCPUsAreInTheSameChassis = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1272)
)
ntxTrapHaswellAndBroadwellCPUsAreInTheSameChassis.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHaswellAndBroadwellCPUsAreInTheSameChassis.setStatus(
        "current"
    )

ntxTrapTimeSinceLastCuratorScanIsBeyondThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1273)
)
ntxTrapTimeSinceLastCuratorScanIsBeyondThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTimeSinceLastCuratorScanIsBeyondThreshold.setStatus(
        "current"
    )

ntxTrapSnapshotChainHeightExceedsThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1274)
)
ntxTrapSnapshotChainHeightExceedsThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSnapshotChainHeightExceedsThreshold.setStatus(
        "current"
    )

ntxTrapDIMMsOfDifferentTypesInOneMemoryChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1275)
)
ntxTrapDIMMsOfDifferentTypesInOneMemoryChannel.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDIMMsOfDifferentTypesInOneMemoryChannel.setStatus(
        "current"
    )

ntxTrapZookeeperNotActiveOnAllCVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1276)
)
ntxTrapZookeeperNotActiveOnAllCVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapZookeeperNotActiveOnAllCVMs.setStatus(
        "current"
    )

ntxTrapM60GPUConfigurationWrongOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1277)
)
ntxTrapM60GPUConfigurationWrongOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapM60GPUConfigurationWrongOnTheNode.setStatus(
        "current"
    )

ntxTrapM10GPUConfigurationWrongOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1278)
)
ntxTrapM10GPUConfigurationWrongOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapM10GPUConfigurationWrongOnTheNode.setStatus(
        "current"
    )

ntxTrapM10AndM60GPUsInstalledOnTheSameNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1279)
)
ntxTrapM10AndM60GPUsInstalledOnTheSameNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapM10AndM60GPUsInstalledOnTheSameNode.setStatus(
        "current"
    )

ntxTrapPCVCPUAvailabilityCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1280)
)
ntxTrapPCVCPUAvailabilityCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPCVCPUAvailabilityCheck.setStatus(
        "current"
    )

ntxTrapPCSufficientDiskSpaceCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1281)
)
ntxTrapPCSufficientDiskSpaceCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPCSufficientDiskSpaceCheck.setStatus(
        "current"
    )

ntxTrapPCMemoryAvailabilityCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1282)
)
ntxTrapPCMemoryAvailabilityCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPCMemoryAvailabilityCheck.setStatus(
        "current"
    )

ntxTrapPCVMLimitCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1283)
)
ntxTrapPCVMLimitCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPCVMLimitCheck.setStatus(
        "current"
    )

ntxTrapStoragePoolSpaceUsageExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1284)
)
ntxTrapStoragePoolSpaceUsageExceeded.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStoragePoolSpaceUsageExceeded.setStatus(
        "current"
    )

ntxTrapDiskInodeUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1285)
)
ntxTrapDiskInodeUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDiskInodeUsageHigh.setStatus(
        "current"
    )

ntxTrapDiskUnused = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1286)
)
ntxTrapDiskUnused.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDiskUnused.setStatus(
        "current"
    )

ntxTrapFusionIOWearHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1287)
)
ntxTrapFusionIOWearHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFusionIOWearHigh.setStatus(
        "current"
    )

ntxTrapFusionIOTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1288)
)
ntxTrapFusionIOTemperatureHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFusionIOTemperatureHigh.setStatus(
        "current"
    )

ntxTrapFusionIOReserveLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1289)
)
ntxTrapFusionIOReserveLow.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFusionIOReserveLow.setStatus(
        "current"
    )

ntxTrapFusionIODiskFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1290)
)
ntxTrapFusionIODiskFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFusionIODiskFailed.setStatus(
        "current"
    )

ntxTrapStorageContainerSpaceUsageExceededNCCCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1291)
)
ntxTrapStorageContainerSpaceUsageExceededNCCCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStorageContainerSpaceUsageExceededNCCCheck.setStatus(
        "current"
    )

ntxTrapDataDiskSpaceUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1292)
)
ntxTrapDataDiskSpaceUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDataDiskSpaceUsageHigh.setStatus(
        "current"
    )

ntxTrapSystemPartitionsSpaceUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1293)
)
ntxTrapSystemPartitionsSpaceUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSystemPartitionsSpaceUsageHigh.setStatus(
        "current"
    )

ntxTrapStorageDeviceHealthBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1294)
)
ntxTrapStorageDeviceHealthBad.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStorageDeviceHealthBad.setStatus(
        "current"
    )

ntxTrapIntelSSDWearHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1295)
)
ntxTrapIntelSSDWearHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIntelSSDWearHigh.setStatus(
        "current"
    )

ntxTrapIntelSSDTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1296)
)
ntxTrapIntelSSDTemperatureHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIntelSSDTemperatureHigh.setStatus(
        "current"
    )

ntxTrapCVMBootRaidDegraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1297)
)
ntxTrapCVMBootRaidDegraded.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMBootRaidDegraded.setStatus(
        "current"
    )

ntxTrapAbnormalHostBootRAIDState = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1298)
)
ntxTrapAbnormalHostBootRAIDState.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAbnormalHostBootRAIDState.setStatus(
        "current"
    )

ntxTrapHypervisorDiskSpaceUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1299)
)
ntxTrapHypervisorDiskSpaceUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHypervisorDiskSpaceUsageHigh.setStatus(
        "current"
    )

ntxTrapInvalidDriveConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1300)
)
ntxTrapInvalidDriveConfiguration.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInvalidDriveConfiguration.setStatus(
        "current"
    )

ntxTrapSATADOMHasFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1301)
)
ntxTrapSATADOMHasFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSATADOMHasFailed.setStatus(
        "current"
    )

ntxTrapSATADOMNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1302)
)
ntxTrapSATADOMNotReachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSATADOMNotReachable.setStatus(
        "current"
    )

ntxTrapSATADOMHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1303)
)
ntxTrapSATADOMHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSATADOMHasWornOut.setStatus(
        "current"
    )

ntxTrapSATADOMSL3IE3HasHighWear = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1304)
)
ntxTrapSATADOMSL3IE3HasHighWear.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSATADOMSL3IE3HasHighWear.setStatus(
        "current"
    )

ntxTrapSATADOMNeedsFirmwareVersionUpgradeToS170119 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1305)
)
ntxTrapSATADOMNeedsFirmwareVersionUpgradeToS170119.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSATADOMNeedsFirmwareVersionUpgradeToS170119.setStatus(
        "current"
    )

ntxTrapmodelFirmwareVersionIsNotTheLatestFirmwareVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1306)
)
ntxTrapmodelFirmwareVersionIsNotTheLatestFirmwareVersion.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapmodelFirmwareVersionIsNotTheLatestFirmwareVersion.setStatus(
        "current"
    )

ntxTrapSATADOMHasGuestVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1307)
)
ntxTrapSATADOMHasGuestVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSATADOMHasGuestVM.setStatus(
        "current"
    )

ntxTrapSASConnectivityNotNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1308)
)
ntxTrapSASConnectivityNotNormal.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSASConnectivityNotNormal.setStatus(
        "current"
    )

ntxTrapSamsungPM1633DriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1309)
)
ntxTrapSamsungPM1633DriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSamsungPM1633DriveHasWornOut.setStatus(
        "current"
    )

ntxTrapToshibaPM3DriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1310)
)
ntxTrapToshibaPM3DriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapToshibaPM3DriveHasWornOut.setStatus(
        "current"
    )

ntxTrapToshibaPM4DriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1311)
)
ntxTrapToshibaPM4DriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapToshibaPM4DriveHasWornOut.setStatus(
        "current"
    )

ntxTrapSM863DriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1312)
)
ntxTrapSM863DriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSM863DriveHasWornOut.setStatus(
        "current"
    )

ntxTrapMicron5100DriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1313)
)
ntxTrapMicron5100DriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMicron5100DriveHasWornOut.setStatus(
        "current"
    )

ntxTrapIntelSSDS3610OnipaddressHasConfigurationProblems = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1314)
)
ntxTrapIntelSSDS3610OnipaddressHasConfigurationProblems.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIntelSSDS3610OnipaddressHasConfigurationProblems.setStatus(
        "current"
    )

ntxTrapOfflineDiskInACluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1315)
)
ntxTrapOfflineDiskInACluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOfflineDiskInACluster.setStatus(
        "current"
    )

ntxTrapNVMeDriveHasErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1316)
)
ntxTrapNVMeDriveHasErrors.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNVMeDriveHasErrors.setStatus(
        "current"
    )

ntxTrapHypervisorBootDriveWearHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1317)
)
ntxTrapHypervisorBootDriveWearHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHypervisorBootDriveWearHigh.setStatus(
        "current"
    )

ntxTrapVMIsProtectedInMultiplePDs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1318)
)
ntxTrapVMIsProtectedInMultiplePDs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMIsProtectedInMultiplePDs.setStatus(
        "current"
    )

ntxTrapProtectedVMsNotOnNutanixStorage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1319)
)
ntxTrapProtectedVMsNotOnNutanixStorage.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMsNotOnNutanixStorage.setStatus(
        "current"
    )

ntxTrapClusterConnectivityStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1320)
)
ntxTrapClusterConnectivityStatus.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterConnectivityStatus.setStatus(
        "current"
    )

ntxTrapHighGarbageDueToErasureCoding = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1321)
)
ntxTrapHighGarbageDueToErasureCoding.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHighGarbageDueToErasureCoding.setStatus(
        "current"
    )

ntxTrapA1175 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1322)
)
ntxTrapA1175.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA1175.setStatus(
        "current"
    )

ntxTrapInvalidErasureCodeDelayParameter = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1323)
)
ntxTrapInvalidErasureCodeDelayParameter.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInvalidErasureCodeDelayParameter.setStatus(
        "current"
    )

ntxTrapFlashModeUsageLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1325)
)
ntxTrapFlashModeUsageLimitExceeded.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFlashModeUsageLimitExceeded.setStatus(
        "current"
    )

ntxTrapFlashmodeenabledVMPowerStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1326)
)
ntxTrapFlashmodeenabledVMPowerStatus.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFlashmodeenabledVMPowerStatus.setStatus(
        "current"
    )

ntxTrapStoragePoolFlashModeConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1327)
)
ntxTrapStoragePoolFlashModeConfiguration.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStoragePoolFlashModeConfiguration.setStatus(
        "current"
    )

ntxTrapTestNotificationTitle = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1328)
)
ntxTrapTestNotificationTitle.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTestNotificationTitle.setStatus(
        "current"
    )

ntxTrapIncompatibleFileServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1329)
)
ntxTrapIncompatibleFileServer.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIncompatibleFileServer.setStatus(
        "current"
    )

ntxTrapA1202 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1330)
)
ntxTrapA1202.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA1202.setStatus(
        "current"
    )

ntxTrapFirmwareVersionOfSamsungPM1633DrivesIsOld = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1331)
)
ntxTrapFirmwareVersionOfSamsungPM1633DrivesIsOld.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFirmwareVersionOfSamsungPM1633DrivesIsOld.setStatus(
        "current"
    )

ntxTrapMoreThanOneTypeOfToshibaPM4DrivesInstalledOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1332)
)
ntxTrapMoreThanOneTypeOfToshibaPM4DrivesInstalledOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMoreThanOneTypeOfToshibaPM4DrivesInstalledOnTheNode.setStatus(
        "current"
    )

ntxTrapA1200 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1333)
)
ntxTrapA1200.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA1200.setStatus(
        "current"
    )

ntxTrapFirmwareVersionOfToshibaPM4DrivesIsOld = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1334)
)
ntxTrapFirmwareVersionOfToshibaPM4DrivesIsOld.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFirmwareVersionOfToshibaPM4DrivesIsOld.setStatus(
        "current"
    )

ntxTrapFirmwareVersionOfSM863DrivesIsOld = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1335)
)
ntxTrapFirmwareVersionOfSM863DrivesIsOld.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFirmwareVersionOfSM863DrivesIsOld.setStatus(
        "current"
    )

ntxTrapFewerThanTwoNonSamsungPM863aDrivesInstalledOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1336)
)
ntxTrapFewerThanTwoNonSamsungPM863aDrivesInstalledOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFewerThanTwoNonSamsungPM863aDrivesInstalledOnTheNode.setStatus(
        "current"
    )

ntxTrapFirmwareVersionOfPM863aDrivesIsOld = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1337)
)
ntxTrapFirmwareVersionOfPM863aDrivesIsOld.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFirmwareVersionOfPM863aDrivesIsOld.setStatus(
        "current"
    )

ntxTrapPM863aDriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1338)
)
ntxTrapPM863aDriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPM863aDriveHasWornOut.setStatus(
        "current"
    )

ntxTrapOfflineDiskInCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1339)
)
ntxTrapOfflineDiskInCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOfflineDiskInCluster.setStatus(
        "current"
    )

ntxTrapMetadataDisksNotMountedOnCVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1340)
)
ntxTrapMetadataDisksNotMountedOnCVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataDisksNotMountedOnCVM.setStatus(
        "current"
    )

ntxTrapFileServerUpgradeTaskIsNotProgressing = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1341)
)
ntxTrapFileServerUpgradeTaskIsNotProgressing.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerUpgradeTaskIsNotProgressing.setStatus(
        "current"
    )

ntxTrapA130129 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1342)
)
ntxTrapA130129.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130129.setStatus(
        "current"
    )

ntxTrapA130118 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1343)
)
ntxTrapA130118.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130118.setStatus(
        "current"
    )

ntxTrapFileServerCloneFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1344)
)
ntxTrapFileServerCloneFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerCloneFailed.setStatus(
        "current"
    )

ntxTrapFileServerRenameFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1345)
)
ntxTrapFileServerRenameFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerRenameFailed.setStatus(
        "current"
    )

ntxTrapA130097 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1346)
)
ntxTrapA130097.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130097.setStatus(
        "current"
    )

ntxTrapA130095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1347)
)
ntxTrapA130095.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130095.setStatus(
        "current"
    )

ntxTrapA130131 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1348)
)
ntxTrapA130131.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130131.setStatus(
        "current"
    )

ntxTrapA130137 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1349)
)
ntxTrapA130137.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130137.setStatus(
        "current"
    )

ntxTrapA106030 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1350)
)
ntxTrapA106030.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA106030.setStatus(
        "current"
    )

ntxTrapA106033 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1351)
)
ntxTrapA106033.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA106033.setStatus(
        "current"
    )

ntxTrapA111047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1352)
)
ntxTrapA111047.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA111047.setStatus(
        "current"
    )

ntxTrapA110219 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1353)
)
ntxTrapA110219.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110219.setStatus(
        "current"
    )

ntxTrapA110251 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1354)
)
ntxTrapA110251.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110251.setStatus(
        "current"
    )

ntxTrapA111044 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1355)
)
ntxTrapA111044.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA111044.setStatus(
        "current"
    )

ntxTrapMaximumConnectionsLimitReachedOnAFileServerVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1356)
)
ntxTrapMaximumConnectionsLimitReachedOnAFileServerVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMaximumConnectionsLimitReachedOnAFileServerVM.setStatus(
        "current"
    )

ntxTrapFailedToAddOneOrMoreFileServerAdministratorUsersOrGroups = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1357)
)
ntxTrapFailedToAddOneOrMoreFileServerAdministratorUsersOrGroups.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToAddOneOrMoreFileServerAdministratorUsersOrGroups.setStatus(
        "current"
    )

ntxTrapUserDefinedAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1358)
)
ntxTrapUserDefinedAlert.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUserDefinedAlert.setStatus(
        "current"
    )

ntxTrapFileServerNetworkChangeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1359)
)
ntxTrapFileServerNetworkChangeFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerNetworkChangeFailed.setStatus(
        "current"
    )

ntxTrapSnapshotCreationDelayed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1360)
)
ntxTrapSnapshotCreationDelayed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSnapshotCreationDelayed.setStatus(
        "current"
    )

ntxTrapA130146 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1361)
)
ntxTrapA130146.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130146.setStatus(
        "current"
    )

ntxTrapA130143 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1362)
)
ntxTrapA130143.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130143.setStatus(
        "current"
    )

ntxTrapA130144 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1363)
)
ntxTrapA130144.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130144.setStatus(
        "current"
    )

ntxTrapFoundationVersionsInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1364)
)
ntxTrapFoundationVersionsInconsistent.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFoundationVersionsInconsistent.setStatus(
        "current"
    )

ntxTrapMetadataDiskUsageIsHigherThanTheSpecifiedLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1365)
)
ntxTrapMetadataDiskUsageIsHigherThanTheSpecifiedLimit.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataDiskUsageIsHigherThanTheSpecifiedLimit.setStatus(
        "current"
    )

ntxTrapVolumeGroupSpaceUsageExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1366)
)
ntxTrapVolumeGroupSpaceUsageExceeded.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVolumeGroupSpaceUsageExceeded.setStatus(
        "current"
    )

ntxTrapVSSContainersHaveHighFileCount = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1367)
)
ntxTrapVSSContainersHaveHighFileCount.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVSSContainersHaveHighFileCount.setStatus(
        "current"
    )

ntxTrapCVMIpAddressIsUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1368)
)
ntxTrapCVMIpAddressIsUnreachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMIpAddressIsUnreachable.setStatus(
        "current"
    )

ntxTrapIncorrectClusterInformationInTheRemoteSite = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1369)
)
ntxTrapIncorrectClusterInformationInTheRemoteSite.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIncorrectClusterInformationInTheRemoteSite.setStatus(
        "current"
    )

ntxTrapProtectionDomainActivationMayFailAsConflictingFilesExist = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1370)
)
ntxTrapProtectionDomainActivationMayFailAsConflictingFilesExist.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainActivationMayFailAsConflictingFilesExist.setStatus(
        "current"
    )

ntxTrapVNUMAVMPinningFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1371)
)
ntxTrapVNUMAVMPinningFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVNUMAVMPinningFailure.setStatus(
        "current"
    )

ntxTrapGuestPowerOperationThroughNGTFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1372)
)
ntxTrapGuestPowerOperationThroughNGTFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapGuestPowerOperationThroughNGTFailed.setStatus(
        "current"
    )

ntxTrapMellanoxNICNotInstalledOrWithWrongTypeOnHostMachine = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1373)
)
ntxTrapMellanoxNICNotInstalledOrWithWrongTypeOnHostMachine.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMellanoxNICNotInstalledOrWithWrongTypeOnHostMachine.setStatus(
        "current"
    )

ntxTrapNonComplianceWithHostAffinityPolicies = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1374)
)
ntxTrapNonComplianceWithHostAffinityPolicies.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNonComplianceWithHostAffinityPolicies.setStatus(
        "current"
    )

ntxTrapPolicyNotApplicableToAnyHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1375)
)
ntxTrapPolicyNotApplicableToAnyHost.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPolicyNotApplicableToAnyHost.setStatus(
        "current"
    )

ntxTrapTheClusterIsNotSynchronizingTimeWithAnyExternalServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1376)
)
ntxTrapTheClusterIsNotSynchronizingTimeWithAnyExternalServers.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTheClusterIsNotSynchronizingTimeWithAnyExternalServers.setStatus(
        "current"
    )

ntxTrapTheHypervisorIsNotSynchronizingTimeWithAnyExternalServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1377)
)
ntxTrapTheHypervisorIsNotSynchronizingTimeWithAnyExternalServers.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTheHypervisorIsNotSynchronizingTimeWithAnyExternalServers.setStatus(
        "current"
    )

ntxTrapProtectionDomainActivationOrMigrationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1378)
)
ntxTrapProtectionDomainActivationOrMigrationFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainActivationOrMigrationFailure.setStatus(
        "current"
    )

ntxTrapProtectionDomainContainsMoreThanTheSpecifiedVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1379)
)
ntxTrapProtectionDomainContainsMoreThanTheSpecifiedVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainContainsMoreThanTheSpecifiedVMs.setStatus(
        "current"
    )

ntxTrapSATADOMML3SEHasHighWear = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1380)
)
ntxTrapSATADOMML3SEHasHighWear.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSATADOMML3SEHasHighWear.setStatus(
        "current"
    )

ntxTrapFileServerAntiVirusScanQueueFullOnFSVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1381)
)
ntxTrapFileServerAntiVirusScanQueueFullOnFSVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerAntiVirusScanQueueFullOnFSVM.setStatus(
        "current"
    )

ntxTrapFileServerAntiVirusScanQueuePilingUpOnFSVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1382)
)
ntxTrapFileServerAntiVirusScanQueuePilingUpOnFSVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerAntiVirusScanQueuePilingUpOnFSVM.setStatus(
        "current"
    )

ntxTrapFileServerAntiVirusExcessiveQuarantinedUnquarantinedFiles = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1383)
)
ntxTrapFileServerAntiVirusExcessiveQuarantinedUnquarantinedFiles.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerAntiVirusExcessiveQuarantinedUnquarantinedFiles.setStatus(
        "current"
    )

ntxTrapA160048 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1384)
)
ntxTrapA160048.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA160048.setStatus(
        "current"
    )

ntxTrapFailedToTakeTheApplicationconsistentSnapshotForTheVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1385)
)
ntxTrapFailedToTakeTheApplicationconsistentSnapshotForTheVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToTakeTheApplicationconsistentSnapshotForTheVM.setStatus(
        "current"
    )

ntxTrapRemovalOfTheTemporaryHypervisorSnapshotFailedForTheVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1386)
)
ntxTrapRemovalOfTheTemporaryHypervisorSnapshotFailedForTheVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemovalOfTheTemporaryHypervisorSnapshotFailedForTheVM.setStatus(
        "current"
    )

ntxTrapCloudDiskUsageIsNearingTheThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1387)
)
ntxTrapCloudDiskUsageIsNearingTheThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCloudDiskUsageIsNearingTheThreshold.setStatus(
        "current"
    )

ntxTrapDIMMsHaveInvalidPartNumber = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1388)
)
ntxTrapDIMMsHaveInvalidPartNumber.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDIMMsHaveInvalidPartNumber.setStatus(
        "current"
    )

ntxTrapAzureCloudControllerVMHasSmallerDisks = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1389)
)
ntxTrapAzureCloudControllerVMHasSmallerDisks.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAzureCloudControllerVMHasSmallerDisks.setStatus(
        "current"
    )

ntxTrapFirmwareVersionOfSM863OrSM863aDrivesIsOld = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1390)
)
ntxTrapFirmwareVersionOfSM863OrSM863aDrivesIsOld.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFirmwareVersionOfSM863OrSM863aDrivesIsOld.setStatus(
        "current"
    )

ntxTrapM2Micron5100HostBootDriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1391)
)
ntxTrapM2Micron5100HostBootDriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapM2Micron5100HostBootDriveHasWornOut.setStatus(
        "current"
    )

ntxTrapM2IntelS3520HostBootDriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1392)
)
ntxTrapM2IntelS3520HostBootDriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapM2IntelS3520HostBootDriveHasWornOut.setStatus(
        "current"
    )

ntxTrapClusterInOverrideMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1393)
)
ntxTrapClusterInOverrideMode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterInOverrideMode.setStatus(
        "current"
    )

ntxTrapMultipleVcentersDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1394)
)
ntxTrapMultipleVcentersDiscovered.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMultipleVcentersDiscovered.setStatus(
        "current"
    )

ntxTrapProtectionRuleTestAlertTitle = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1395)
)
ntxTrapProtectionRuleTestAlertTitle.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionRuleTestAlertTitle.setStatus(
        "current"
    )

ntxTrapExternalClientAuthentication = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1396)
)
ntxTrapExternalClientAuthentication.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapExternalClientAuthentication.setStatus(
        "current"
    )

ntxTrapTwoNodeClusterStateChangeToclusteroperationmode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1397)
)
ntxTrapTwoNodeClusterStateChangeToclusteroperationmode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTwoNodeClusterStateChangeToclusteroperationmode.setStatus(
        "current"
    )

ntxTrapWitnessIsUnreachableFromNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1398)
)
ntxTrapWitnessIsUnreachableFromNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapWitnessIsUnreachableFromNode.setStatus(
        "current"
    )

ntxTrapTwoNodeClusterChangedStateToStandaloneMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1399)
)
ntxTrapTwoNodeClusterChangedStateToStandaloneMode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTwoNodeClusterChangedStateToStandaloneMode.setStatus(
        "current"
    )

ntxTrapTwoNodeClusterStateChangeTostate = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1400)
)
ntxTrapTwoNodeClusterStateChangeTostate.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTwoNodeClusterStateChangeTostate.setStatus(
        "current"
    )

ntxTrapTwoNodeClusterStateChangeToStandaloneMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1401)
)
ntxTrapTwoNodeClusterStateChangeToStandaloneMode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTwoNodeClusterStateChangeToStandaloneMode.setStatus(
        "current"
    )

ntxTrapRecoveryPlanExecutionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1402)
)
ntxTrapRecoveryPlanExecutionFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPlanExecutionFailed.setStatus(
        "current"
    )

ntxTrapXiPaymentMissed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1403)
)
ntxTrapXiPaymentMissed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapXiPaymentMissed.setStatus(
        "current"
    )

ntxTrapFreeXiAccountExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1404)
)
ntxTrapFreeXiAccountExpired.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFreeXiAccountExpired.setStatus(
        "current"
    )

ntxTrapXiSubscriptionExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1405)
)
ntxTrapXiSubscriptionExpired.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapXiSubscriptionExpired.setStatus(
        "current"
    )

ntxTrapEntitySyncFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1406)
)
ntxTrapEntitySyncFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntitySyncFailure.setStatus(
        "current"
    )

ntxTrapNucalmInternalServiceHasStoppedWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1407)
)
ntxTrapNucalmInternalServiceHasStoppedWorking.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNucalmInternalServiceHasStoppedWorking.setStatus(
        "current"
    )

ntxTrapEpsilonInternalServiceHasStoppedWorking = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1408)
)
ntxTrapEpsilonInternalServiceHasStoppedWorking.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEpsilonInternalServiceHasStoppedWorking.setStatus(
        "current"
    )

ntxTrapProtectionRuleConflictOccurred = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1409)
)
ntxTrapProtectionRuleConflictOccurred.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionRuleConflictOccurred.setStatus(
        "current"
    )

ntxTrapDomainFaultToleranceIsReducedForMetadata = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1410)
)
ntxTrapDomainFaultToleranceIsReducedForMetadata.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDomainFaultToleranceIsReducedForMetadata.setStatus(
        "current"
    )

ntxTrapVMProtectionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1411)
)
ntxTrapVMProtectionFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMProtectionFailed.setStatus(
        "current"
    )

ntxTrapVMRecoveryPointReplicationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1412)
)
ntxTrapVMRecoveryPointReplicationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRecoveryPointReplicationFailed.setStatus(
        "current"
    )

ntxTrapVMRecoveryPointCreationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1413)
)
ntxTrapVMRecoveryPointCreationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRecoveryPointCreationFailed.setStatus(
        "current"
    )

ntxTrapMicrosegmentationControlPlaneFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1414)
)
ntxTrapMicrosegmentationControlPlaneFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMicrosegmentationControlPlaneFailed.setStatus(
        "current"
    )

ntxTrapMicrosegmentationRuleFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1415)
)
ntxTrapMicrosegmentationRuleFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMicrosegmentationRuleFailed.setStatus(
        "current"
    )

ntxTrapDriveRemovalStuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1416)
)
ntxTrapDriveRemovalStuck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDriveRemovalStuck.setStatus(
        "current"
    )

ntxTrapFileServerNTPServersConnectivityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1417)
)
ntxTrapFileServerNTPServersConnectivityFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerNTPServersConnectivityFailure.setStatus(
        "current"
    )

ntxTrapFileServerTimeIsOutOfSyncWithTheActiveDirectory = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1418)
)
ntxTrapFileServerTimeIsOutOfSyncWithTheActiveDirectory.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerTimeIsOutOfSyncWithTheActiveDirectory.setStatus(
        "current"
    )

ntxTrapFileServerDNSResolverIPConnectivityFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1419)
)
ntxTrapFileServerDNSResolverIPConnectivityFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerDNSResolverIPConnectivityFailure.setStatus(
        "current"
    )

ntxTrapFileServerUserManagementConfigurationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1420)
)
ntxTrapFileServerUserManagementConfigurationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerUserManagementConfigurationFailed.setStatus(
        "current"
    )

ntxTraphomePartitionUsageOnAFileServerVMHigherThanThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1421)
)
ntxTraphomePartitionUsageOnAFileServerVMHigherThanThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTraphomePartitionUsageOnAFileServerVMHigherThanThreshold.setStatus(
        "current"
    )

ntxTrapFileServerDNSRecordsCannotBeRefreshed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1422)
)
ntxTrapFileServerDNSRecordsCannotBeRefreshed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerDNSRecordsCannotBeRefreshed.setStatus(
        "current"
    )

ntxTrapFileServerShareBackupDiffPathTranslationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1423)
)
ntxTrapFileServerShareBackupDiffPathTranslationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerShareBackupDiffPathTranslationFailed.setStatus(
        "current"
    )

ntxTrapFileServerPartnerServerConnectivityDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1424)
)
ntxTrapFileServerPartnerServerConnectivityDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerPartnerServerConnectivityDown.setStatus(
        "current"
    )

ntxTrapFileServerPDActionToIncompatibleRemoteSiteAOS = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1425)
)
ntxTrapFileServerPDActionToIncompatibleRemoteSiteAOS.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerPDActionToIncompatibleRemoteSiteAOS.setStatus(
        "current"
    )

ntxTrapFileServerServicesGotInterrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1426)
)
ntxTrapFileServerServicesGotInterrupted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerServicesGotInterrupted.setStatus(
        "current"
    )

ntxTrapCommonPortGroupBetweenESXiHostsIsAbsent = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1427)
)
ntxTrapCommonPortGroupBetweenESXiHostsIsAbsent.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCommonPortGroupBetweenESXiHostsIsAbsent.setStatus(
        "current"
    )

ntxTrapFailedToReceiveSnapshotForTheProtectionDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1428)
)
ntxTrapFailedToReceiveSnapshotForTheProtectionDomain.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToReceiveSnapshotForTheProtectionDomain.setStatus(
        "current"
    )

ntxTrapHostNetworkUplinkConfigurationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1429)
)
ntxTrapHostNetworkUplinkConfigurationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHostNetworkUplinkConfigurationFailed.setStatus(
        "current"
    )

ntxTrapRestartVMsBeforePerformingUpgradeOrMigrateOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1430)
)
ntxTrapRestartVMsBeforePerformingUpgradeOrMigrateOperation.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRestartVMsBeforePerformingUpgradeOrMigrateOperation.setStatus(
        "current"
    )

ntxTrapOplogEpisodeCountCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1431)
)
ntxTrapOplogEpisodeCountCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOplogEpisodeCountCheck.setStatus(
        "current"
    )

ntxTrapCerebroStatsCollectorFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1432)
)
ntxTrapCerebroStatsCollectorFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCerebroStatsCollectorFailed.setStatus(
        "current"
    )

ntxTrapLatencyBetweenCVMsIsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1433)
)
ntxTrapLatencyBetweenCVMsIsHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLatencyBetweenCVMsIsHigh.setStatus(
        "current"
    )

ntxTrapLicenseInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1434)
)
ntxTrapLicenseInvalid.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLicenseInvalid.setStatus(
        "current"
    )

ntxTrapRemoteSiteAOSNotCompatibleWithFileServerVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1435)
)
ntxTrapRemoteSiteAOSNotCompatibleWithFileServerVersion.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteAOSNotCompatibleWithFileServerVersion.setStatus(
        "current"
    )

ntxTrapA106043 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1436)
)
ntxTrapA106043.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA106043.setStatus(
        "current"
    )

ntxTrapFirmwareVersionOfIntelS4600DrivesIsOld = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1437)
)
ntxTrapFirmwareVersionOfIntelS4600DrivesIsOld.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFirmwareVersionOfIntelS4600DrivesIsOld.setStatus(
        "current"
    )

ntxTrapIntelS4600DriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1438)
)
ntxTrapIntelS4600DriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIntelS4600DriveHasWornOut.setStatus(
        "current"
    )

ntxTrapHostBootDiskSerialNumberHasChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1439)
)
ntxTrapHostBootDiskSerialNumberHasChanged.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHostBootDiskSerialNumberHasChanged.setStatus(
        "current"
    )

ntxTrapSataControllerStatusIsBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1440)
)
ntxTrapSataControllerStatusIsBad.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSataControllerStatusIsBad.setStatus(
        "current"
    )

ntxTrapSamsung863Or863aOnipaddressHasConfigurationProblems = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1441)
)
ntxTrapSamsung863Or863aOnipaddressHasConfigurationProblems.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSamsung863Or863aOnipaddressHasConfigurationProblems.setStatus(
        "current"
    )

ntxTrapHypervisorBootDriveRAIDIsInAnUnhealthyState = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1442)
)
ntxTrapHypervisorBootDriveRAIDIsInAnUnhealthyState.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHypervisorBootDriveRAIDIsInAnUnhealthyState.setStatus(
        "current"
    )

ntxTrapCVMPortGroupRenamed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1443)
)
ntxTrapCVMPortGroupRenamed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMPortGroupRenamed.setStatus(
        "current"
    )

ntxTrapA106453 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1444)
)
ntxTrapA106453.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA106453.setStatus(
        "current"
    )

ntxTrapActiveDirectoryDCsAndorDNSServersRunningOnCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1445)
)
ntxTrapActiveDirectoryDCsAndorDNSServersRunningOnCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapActiveDirectoryDCsAndorDNSServersRunningOnCluster.setStatus(
        "current"
    )

ntxTrappowersourceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1446)
)
ntxTrappowersourceDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrappowersourceDown.setStatus(
        "current"
    )

ntxTrapCPUTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1447)
)
ntxTrapCPUTemperatureLow.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPUTemperatureLow.setStatus(
        "current"
    )

ntxTrapRAMTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1448)
)
ntxTrapRAMTemperatureLow.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRAMTemperatureLow.setStatus(
        "current"
    )

ntxTrapSystemTemperatureLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1449)
)
ntxTrapSystemTemperatureLow.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSystemTemperatureLow.setStatus(
        "current"
    )

ntxTrapIPMISELLogFetchFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1450)
)
ntxTrapIPMISELLogFetchFail.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIPMISELLogFetchFail.setStatus(
        "current"
    )

ntxTrapIPMISELLogPowerFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1451)
)
ntxTrapIPMISELLogPowerFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIPMISELLogPowerFailure.setStatus(
        "current"
    )

ntxTrapAggressiveBreakReplicationTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1452)
)
ntxTrapAggressiveBreakReplicationTimeout.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAggressiveBreakReplicationTimeout.setStatus(
        "current"
    )

ntxTrapCVMOrPCVMRAMUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1453)
)
ntxTrapCVMOrPCVMRAMUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMOrPCVMRAMUsageHigh.setStatus(
        "current"
    )

ntxTrapCVMOrPCVMCPULoadHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1454)
)
ntxTrapCVMOrPCVMCPULoadHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMOrPCVMCPULoadHigh.setStatus(
        "current"
    )

ntxTrapCVMRenamedIncorrectly = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1455)
)
ntxTrapCVMRenamedIncorrectly.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMRenamedIncorrectly.setStatus(
        "current"
    )

ntxTrapPCVMDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1457)
)
ntxTrapPCVMDiskUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPCVMDiskUsageHigh.setStatus(
        "current"
    )

ntxTrapvmtypeVirtualIPCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1458)
)
ntxTrapvmtypeVirtualIPCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapvmtypeVirtualIPCheck.setStatus(
        "current"
    )

ntxTrapvmtypeSameTimezoneCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1459)
)
ntxTrapvmtypeSameTimezoneCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapvmtypeSameTimezoneCheck.setStatus(
        "current"
    )

ntxTrapDIMMConfigurationIsWrong = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1460)
)
ntxTrapDIMMConfigurationIsWrong.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDIMMConfigurationIsWrong.setStatus(
        "current"
    )

ntxTrapP40GPUConfigurationWrongOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1461)
)
ntxTrapP40GPUConfigurationWrongOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapP40GPUConfigurationWrongOnTheNode.setStatus(
        "current"
    )

ntxTrapP40GPUBMCVersionIsOldOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1462)
)
ntxTrapP40GPUBMCVersionIsOldOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapP40GPUBMCVersionIsOldOnTheNode.setStatus(
        "current"
    )

ntxTrapMemoryConfigurationInconsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1463)
)
ntxTrapMemoryConfigurationInconsistent.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMemoryConfigurationInconsistent.setStatus(
        "current"
    )

ntxTrapEntityCountExceededTheMaximumLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1464)
)
ntxTrapEntityCountExceededTheMaximumLimit.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntityCountExceededTheMaximumLimit.setStatus(
        "current"
    )

ntxTrapAOSUpgradesAreDisabledOncvmip = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1465)
)
ntxTrapAOSUpgradesAreDisabledOncvmip.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAOSUpgradesAreDisabledOncvmip.setStatus(
        "current"
    )

ntxTrapFirmwareUpgradesAreDisabledOncvmip = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1466)
)
ntxTrapFirmwareUpgradesAreDisabledOncvmip.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFirmwareUpgradesAreDisabledOncvmip.setStatus(
        "current"
    )

ntxTrapHypervisorDiskdevnameSpaceUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1467)
)
ntxTrapHypervisorDiskdevnameSpaceUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHypervisorDiskdevnameSpaceUsageHigh.setStatus(
        "current"
    )

ntxTrapCVMPasswordlessSSHToHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1468)
)
ntxTrapCVMPasswordlessSSHToHost.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMPasswordlessSSHToHost.setStatus(
        "current"
    )

ntxTrapCPUsOfDifferentTypesOrModelsAreInTheSameChassis = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1469)
)
ntxTrapCPUsOfDifferentTypesOrModelsAreInTheSameChassis.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPUsOfDifferentTypesOrModelsAreInTheSameChassis.setStatus(
        "current"
    )

ntxTrapRecoveryPointReplicationSkipped = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1470)
)
ntxTrapRecoveryPointReplicationSkipped.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPointReplicationSkipped.setStatus(
        "current"
    )

ntxTrapNetworkCreationFailureForRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1471)
)
ntxTrapNetworkCreationFailureForRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNetworkCreationFailureForRecoveryPlan.setStatus(
        "current"
    )

ntxTrapVirtualIPAddressNotConfiguredOnTheRemoteCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1472)
)
ntxTrapVirtualIPAddressNotConfiguredOnTheRemoteCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVirtualIPAddressNotConfiguredOnTheRemoteCluster.setStatus(
        "current"
    )

ntxTrapEntityCountExceedDiscovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1473)
)
ntxTrapEntityCountExceedDiscovered.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntityCountExceedDiscovered.setStatus(
        "current"
    )

ntxTrapVMReplicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1474)
)
ntxTrapVMReplicationFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMReplicationFailure.setStatus(
        "current"
    )

ntxTrapVMReplicationExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1475)
)
ntxTrapVMReplicationExpired.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMReplicationExpired.setStatus(
        "current"
    )

ntxTrapApplicationConsistentRecoveryPointFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1476)
)
ntxTrapApplicationConsistentRecoveryPointFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapApplicationConsistentRecoveryPointFailed.setStatus(
        "current"
    )

ntxTrapReplicationTimeExceededTheRPOLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1477)
)
ntxTrapReplicationTimeExceededTheRPOLimit.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapReplicationTimeExceededTheRPOLimit.setStatus(
        "current"
    )

ntxTrapNGTOnVMvmnameWasNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1478)
)
ntxTrapNGTOnVMvmnameWasNotReachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNGTOnVMvmnameWasNotReachable.setStatus(
        "current"
    )

ntxTrapVMReplicationHasNotProgressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1479)
)
ntxTrapVMReplicationHasNotProgressed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMReplicationHasNotProgressed.setStatus(
        "current"
    )

ntxTrapVSSProviderOrprefreezepostthawScriptsNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1480)
)
ntxTrapVSSProviderOrprefreezepostthawScriptsNotInstalled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVSSProviderOrprefreezepostthawScriptsNotInstalled.setStatus(
        "current"
    )

ntxTrapPartialRecoveryPoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1481)
)
ntxTrapPartialRecoveryPoint.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPartialRecoveryPoint.setStatus(
        "current"
    )

ntxTrapPulseCannotConnectToRESTServerEndpoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1482)
)
ntxTrapPulseCannotConnectToRESTServerEndpoint.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPulseCannotConnectToRESTServerEndpoint.setStatus(
        "current"
    )

ntxTrapJumboFramesEnabledForNICnicnameOnservicevmexternalip = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1483)
)
ntxTrapJumboFramesEnabledForNICnicnameOnservicevmexternalip.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapJumboFramesEnabledForNICnicnameOnservicevmexternalip.setStatus(
        "current"
    )

ntxTrapUnableToRetrieveTheAvailabilityZoneEndpoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1484)
)
ntxTrapUnableToRetrieveTheAvailabilityZoneEndpoint.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnableToRetrieveTheAvailabilityZoneEndpoint.setStatus(
        "current"
    )

ntxTrapRecoveryPointReplicationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1485)
)
ntxTrapRecoveryPointReplicationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPointReplicationFailed.setStatus(
        "current"
    )

ntxTrapUnableToCommunicateWithTheDataCenterManager = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1486)
)
ntxTrapUnableToCommunicateWithTheDataCenterManager.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnableToCommunicateWithTheDataCenterManager.setStatus(
        "current"
    )

ntxTrapRemoteSiteInSameVCenterDatacenter = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1487)
)
ntxTrapRemoteSiteInSameVCenterDatacenter.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteInSameVCenterDatacenter.setStatus(
        "current"
    )

ntxTrapV100GPUConfigurationWrongOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1488)
)
ntxTrapV100GPUConfigurationWrongOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapV100GPUConfigurationWrongOnTheNode.setStatus(
        "current"
    )

ntxTrapApplicationsArchiveReadyForDownload = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1489)
)
ntxTrapApplicationsArchiveReadyForDownload.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapApplicationsArchiveReadyForDownload.setStatus(
        "current"
    )

ntxTrapMoreThanOneTypeOfGPUsInstalledOnTheSameNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1490)
)
ntxTrapMoreThanOneTypeOfGPUsInstalledOnTheSameNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMoreThanOneTypeOfGPUsInstalledOnTheSameNode.setStatus(
        "current"
    )

ntxTrapVmRegisteredWithoutNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1491)
)
ntxTrapVmRegisteredWithoutNetwork.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVmRegisteredWithoutNetwork.setStatus(
        "current"
    )

ntxTrapAlertEmailFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1492)
)
ntxTrapAlertEmailFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAlertEmailFailure.setStatus(
        "current"
    )

ntxTrapNICRXCRCErrorRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1493)
)
ntxTrapNICRXCRCErrorRateHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNICRXCRCErrorRateHigh.setStatus(
        "current"
    )

ntxTrapNICRXMissedErrorRateHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1494)
)
ntxTrapNICRXMissedErrorRateHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNICRXMissedErrorRateHigh.setStatus(
        "current"
    )

ntxTrapEntityUnprotectionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1495)
)
ntxTrapEntityUnprotectionFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntityUnprotectionFailed.setStatus(
        "current"
    )

ntxTrapAvailabilityZoneValidationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1496)
)
ntxTrapAvailabilityZoneValidationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAvailabilityZoneValidationFailed.setStatus(
        "current"
    )

ntxTrapInvalidNetworkMappingForRecoveryPlanrecoveryplanname = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1497)
)
ntxTrapInvalidNetworkMappingForRecoveryPlanrecoveryplanname.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInvalidNetworkMappingForRecoveryPlanrecoveryplanname.setStatus(
        "current"
    )

ntxTrapDataProtectionTasksAreNotProgressing = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1498)
)
ntxTrapDataProtectionTasksAreNotProgressing.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDataProtectionTasksAreNotProgressing.setStatus(
        "current"
    )

ntxTrapIncorrectClusterInformationInTheRemoteSiteremotename = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1499)
)
ntxTrapIncorrectClusterInformationInTheRemoteSiteremotename.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIncorrectClusterInformationInTheRemoteSiteremotename.setStatus(
        "current"
    )

ntxTrapVCenterNotRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1500)
)
ntxTrapVCenterNotRegistered.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVCenterNotRegistered.setStatus(
        "current"
    )

ntxTrapNGTUpdateAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1501)
)
ntxTrapNGTUpdateAvailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNGTUpdateAvailable.setStatus(
        "current"
    )

ntxTrapDuplicateCVMIPAddressDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1502)
)
ntxTrapDuplicateCVMIPAddressDetected.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDuplicateCVMIPAddressDetected.setStatus(
        "current"
    )

ntxTrapMTUConfigurationAcrossControllerVMsIsNotConsistent = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1503)
)
ntxTrapMTUConfigurationAcrossControllerVMsIsNotConsistent.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMTUConfigurationAcrossControllerVMsIsNotConsistent.setStatus(
        "current"
    )

ntxTrapMultipleCpuunblockProcessesRunning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1504)
)
ntxTrapMultipleCpuunblockProcessesRunning.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMultipleCpuunblockProcessesRunning.setStatus(
        "current"
    )

ntxTrapRecoveryLocationOperationChangedToReadOnlyMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1505)
)
ntxTrapRecoveryLocationOperationChangedToReadOnlyMode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryLocationOperationChangedToReadOnlyMode.setStatus(
        "current"
    )

ntxTrapA130181 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1506)
)
ntxTrapA130181.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130181.setStatus(
        "current"
    )

ntxTrapAvailabilityZoneConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1507)
)
ntxTrapAvailabilityZoneConnectionFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAvailabilityZoneConnectionFailure.setStatus(
        "current"
    )

ntxTrapPEPCConnectionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1508)
)
ntxTrapPEPCConnectionFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPEPCConnectionFailure.setStatus(
        "current"
    )

ntxTrapNutanixGuestToolsNotUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1509)
)
ntxTrapNutanixGuestToolsNotUpgraded.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixGuestToolsNotUpgraded.setStatus(
        "current"
    )

ntxTrapFileServerMultipleVMsOnSingleNodeCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1510)
)
ntxTrapFileServerMultipleVMsOnSingleNodeCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerMultipleVMsOnSingleNodeCheck.setStatus(
        "current"
    )

ntxTrapShareUsageReachingToConfiguredLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1511)
)
ntxTrapShareUsageReachingToConfiguredLimit.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapShareUsageReachingToConfiguredLimit.setStatus(
        "current"
    )

ntxTrapProtectedVMsNotRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1512)
)
ntxTrapProtectedVMsNotRecoverable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMsNotRecoverable.setStatus(
        "current"
    )

ntxTrapEntitySyncFailureForProtectionRule = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1513)
)
ntxTrapEntitySyncFailureForProtectionRule.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntitySyncFailureForProtectionRule.setStatus(
        "current"
    )

ntxTrapEntitySyncFailureForRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1514)
)
ntxTrapEntitySyncFailureForRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntitySyncFailureForRecoveryPlan.setStatus(
        "current"
    )

ntxTrapDataAtRestEncryptionKeyBackupWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1515)
)
ntxTrapDataAtRestEncryptionKeyBackupWarning.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDataAtRestEncryptionKeyBackupWarning.setStatus(
        "current"
    )

ntxTrapLocalKeyManagerMasterKeyRotationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1516)
)
ntxTrapLocalKeyManagerMasterKeyRotationWarning.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLocalKeyManagerMasterKeyRotationWarning.setStatus(
        "current"
    )

ntxTrapPulseCannotConnectToRESTServerEndpointOnFileServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1517)
)
ntxTrapPulseCannotConnectToRESTServerEndpointOnFileServer.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPulseCannotConnectToRESTServerEndpointOnFileServer.setStatus(
        "current"
    )

ntxTrapDetectedIncompatibleAHVVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1518)
)
ntxTrapDetectedIncompatibleAHVVersion.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDetectedIncompatibleAHVVersion.setStatus(
        "current"
    )

ntxTrapNucalmLicenseIsOvershooting = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1519)
)
ntxTrapNucalmLicenseIsOvershooting.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNucalmLicenseIsOvershooting.setStatus(
        "current"
    )

ntxTrapA300409 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1520)
)
ntxTrapA300409.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300409.setStatus(
        "current"
    )

ntxTrapValidationFailedForRecoveryPlanrecoveryplanname = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1521)
)
ntxTrapValidationFailedForRecoveryPlanrecoveryplanname.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapValidationFailedForRecoveryPlanrecoveryplanname.setStatus(
        "current"
    )

ntxTrapoperationtypeFailedForRecoveryPlanrecoveryplanname = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1522)
)
ntxTrapoperationtypeFailedForRecoveryPlanrecoveryplanname.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapoperationtypeFailedForRecoveryPlanrecoveryplanname.setStatus(
        "current"
    )

ntxTrapA300402 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1523)
)
ntxTrapA300402.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300402.setStatus(
        "current"
    )

ntxTrapEntitySyncFailureForAvailabilityZone = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1524)
)
ntxTrapEntitySyncFailureForAvailabilityZone.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntitySyncFailureForAvailabilityZone.setStatus(
        "current"
    )

ntxTrapRemoteAvailabilityZoneLatencyIsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1525)
)
ntxTrapRemoteAvailabilityZoneLatencyIsHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteAvailabilityZoneLatencyIsHigh.setStatus(
        "current"
    )

ntxTrapTheFrequencyOfCPUcpuidOnHosthostipIsExtremelyLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1526)
)
ntxTrapTheFrequencyOfCPUcpuidOnHosthostipIsExtremelyLow.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTheFrequencyOfCPUcpuidOnHosthostipIsExtremelyLow.setStatus(
        "current"
    )

ntxTrapCalmLicenseExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1527)
)
ntxTrapCalmLicenseExpiry.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCalmLicenseExpiry.setStatus(
        "current"
    )

ntxTrapPCVMCPULoadHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1528)
)
ntxTrapPCVMCPULoadHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPCVMCPULoadHigh.setStatus(
        "current"
    )

ntxTrapNodeMarkedToBeAutoAddedToMetadataRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1529)
)
ntxTrapNodeMarkedToBeAutoAddedToMetadataRing.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeMarkedToBeAutoAddedToMetadataRing.setStatus(
        "current"
    )

ntxTrapAutomaticAdditionOfNodeToMetadataRingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1530)
)
ntxTrapAutomaticAdditionOfNodeToMetadataRingDisabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAutomaticAdditionOfNodeToMetadataRingDisabled.setStatus(
        "current"
    )

ntxTrapNodeMarkedToBeDetachedFromMetadataRing = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1531)
)
ntxTrapNodeMarkedToBeDetachedFromMetadataRing.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeMarkedToBeDetachedFromMetadataRing.setStatus(
        "current"
    )

ntxTrapNodeForwardingMetadataRequests = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1532)
)
ntxTrapNodeForwardingMetadataRequests.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeForwardingMetadataRequests.setStatus(
        "current"
    )

ntxTrapRecoveryPlansHaveConflictingNetworkMappings = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1533)
)
ntxTrapRecoveryPlansHaveConflictingNetworkMappings.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPlansHaveConflictingNetworkMappings.setStatus(
        "current"
    )

ntxTrapVMRecoveryMayFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1534)
)
ntxTrapVMRecoveryMayFail.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRecoveryMayFail.setStatus(
        "current"
    )

ntxTrapNutanixCalmLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1535)
)
ntxTrapNutanixCalmLicenseViolation.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixCalmLicenseViolation.setStatus(
        "current"
    )

ntxTrapTranslatedAddressesRetrievalFailureInNGT = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1536)
)
ntxTrapTranslatedAddressesRetrievalFailureInNGT.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTranslatedAddressesRetrievalFailureInNGT.setStatus(
        "current"
    )

ntxTrapStoragePoolUsageReachingItsLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1537)
)
ntxTrapStoragePoolUsageReachingItsLimit.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStoragePoolUsageReachingItsLimit.setStatus(
        "current"
    )

ntxTrapTargetCouldNotBeFoundForReplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1538)
)
ntxTrapTargetCouldNotBeFoundForReplication.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTargetCouldNotBeFoundForReplication.setStatus(
        "current"
    )

ntxTrapClusterJoinToDomainFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1539)
)
ntxTrapClusterJoinToDomainFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterJoinToDomainFailure.setStatus(
        "current"
    )

ntxTrapUnplannedFailoverAndFailbackCanCauseFullReplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1540)
)
ntxTrapUnplannedFailoverAndFailbackCanCauseFullReplication.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnplannedFailoverAndFailbackCanCauseFullReplication.setStatus(
        "current"
    )

ntxTrapEntitySyncFailureForTheProtectionPolicy = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1541)
)
ntxTrapEntitySyncFailureForTheProtectionPolicy.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntitySyncFailureForTheProtectionPolicy.setStatus(
        "current"
    )

ntxTrapEntitySyncFailureForTheRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1542)
)
ntxTrapEntitySyncFailureForTheRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntitySyncFailureForTheRecoveryPlan.setStatus(
        "current"
    )

ntxTrapEntitySyncFailureForTheAvailabilityZone = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1543)
)
ntxTrapEntitySyncFailureForTheAvailabilityZone.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntitySyncFailureForTheAvailabilityZone.setStatus(
        "current"
    )

ntxTrapDeleteTheFailedOverVMsOnThePrimaryLocation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1544)
)
ntxTrapDeleteTheFailedOverVMsOnThePrimaryLocation.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDeleteTheFailedOverVMsOnThePrimaryLocation.setStatus(
        "current"
    )

ntxTrapVMvmnameMemoryOverprovisioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1545)
)
ntxTrapVMvmnameMemoryOverprovisioned.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMvmnameMemoryOverprovisioned.setStatus(
        "current"
    )

ntxTrapVMvmnameMemoryConstrained = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1546)
)
ntxTrapVMvmnameMemoryConstrained.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMvmnameMemoryConstrained.setStatus(
        "current"
    )

ntxTrapVMvmnameCPUOverprovisioned = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1547)
)
ntxTrapVMvmnameCPUOverprovisioned.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMvmnameCPUOverprovisioned.setStatus(
        "current"
    )

ntxTrapVMvmnameCPUConstrained = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1548)
)
ntxTrapVMvmnameCPUConstrained.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMvmnameCPUConstrained.setStatus(
        "current"
    )

ntxTrapVMvmnameInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1549)
)
ntxTrapVMvmnameInactive.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMvmnameInactive.setStatus(
        "current"
    )

ntxTrapVMBullyvmname = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1550)
)
ntxTrapVMBullyvmname.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMBullyvmname.setStatus(
        "current"
    )

ntxTrapNutanixGuestToolsFailedToInitiateVMReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1551)
)
ntxTrapNutanixGuestToolsFailedToInitiateVMReboot.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixGuestToolsFailedToInitiateVMReboot.setStatus(
        "current"
    )

ntxTrapMultipleRecoveryPlansHaveCategorycategory = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1552)
)
ntxTrapMultipleRecoveryPlansHaveCategorycategory.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMultipleRecoveryPlansHaveCategorycategory.setStatus(
        "current"
    )

ntxTrapFloatingIPfloatingipIsAssociatedWithMultipleVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1553)
)
ntxTrapFloatingIPfloatingipIsAssociatedWithMultipleVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFloatingIPfloatingipIsAssociatedWithMultipleVMs.setStatus(
        "current"
    )

ntxTrapRemoteReplicationIsLaggingForProtectionDomainSnapshot = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1554)
)
ntxTrapRemoteReplicationIsLaggingForProtectionDomainSnapshot.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteReplicationIsLaggingForProtectionDomainSnapshot.setStatus(
        "current"
    )

ntxTrapSameVMsPresentInMultipleStagesOfTheRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1555)
)
ntxTrapSameVMsPresentInMultipleStagesOfTheRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSameVMsPresentInMultipleStagesOfTheRecoveryPlan.setStatus(
        "current"
    )

ntxTrapZookeeperAliasIsIncorrectlyConfiguredInTheCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1556)
)
ntxTrapZookeeperAliasIsIncorrectlyConfiguredInTheCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapZookeeperAliasIsIncorrectlyConfiguredInTheCluster.setStatus(
        "current"
    )

ntxTrapValidationFailedForTheRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1557)
)
ntxTrapValidationFailedForTheRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapValidationFailedForTheRecoveryPlan.setStatus(
        "current"
    )

ntxTrapNetworkCreationFailureForTheRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1558)
)
ntxTrapNetworkCreationFailureForTheRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNetworkCreationFailureForTheRecoveryPlan.setStatus(
        "current"
    )

ntxTrapValidationFailedForTheRecoveryPlanrecoveryplanname = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1559)
)
ntxTrapValidationFailedForTheRecoveryPlanrecoveryplanname.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapValidationFailedForTheRecoveryPlanrecoveryplanname.setStatus(
        "current"
    )

ntxTrapVirtualIPAddressNotConfiguredOnTheCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1560)
)
ntxTrapVirtualIPAddressNotConfiguredOnTheCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVirtualIPAddressNotConfiguredOnTheCluster.setStatus(
        "current"
    )

ntxTrapNGTOnVMvmnameIsNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1561)
)
ntxTrapNGTOnVMvmnameIsNotReachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNGTOnVMvmnameIsNotReachable.setStatus(
        "current"
    )

ntxTrapCVMNICLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1562)
)
ntxTrapCVMNICLinkDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMNICLinkDown.setStatus(
        "current"
    )

ntxTrapA300417 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1563)
)
ntxTrapA300417.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300417.setStatus(
        "current"
    )

ntxTrapConflictingNgtPolicies = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1564)
)
ntxTrapConflictingNgtPolicies.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapConflictingNgtPolicies.setStatus(
        "current"
    )

ntxTrapSystemTemperatureReadingError = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1565)
)
ntxTrapSystemTemperatureReadingError.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSystemTemperatureReadingError.setStatus(
        "current"
    )

ntxTrapMultipleRecoveryPlansAreAssociatedWithCategorycategory = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1566)
)
ntxTrapMultipleRecoveryPlansAreAssociatedWithCategorycategory.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMultipleRecoveryPlansAreAssociatedWithCategorycategory.setStatus(
        "current"
    )

ntxTrapA300412 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1567)
)
ntxTrapA300412.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300412.setStatus(
        "current"
    )

ntxTrapA110401 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1568)
)
ntxTrapA110401.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110401.setStatus(
        "current"
    )

ntxTrapA300418 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1569)
)
ntxTrapA300418.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300418.setStatus(
        "current"
    )

ntxTrapA300416 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1570)
)
ntxTrapA300416.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300416.setStatus(
        "current"
    )

ntxTrapVMsArePartOfMultipleStagesInTheRecoveryPlanrecoveryplan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1571)
)
ntxTrapVMsArePartOfMultipleStagesInTheRecoveryPlanrecoveryplan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMsArePartOfMultipleStagesInTheRecoveryPlanrecoveryplan.setStatus(
        "current"
    )

ntxTrapA300414 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1572)
)
ntxTrapA300414.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300414.setStatus(
        "current"
    )

ntxTrapKaranServicesAreUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1573)
)
ntxTrapKaranServicesAreUnreachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapKaranServicesAreUnreachable.setStatus(
        "current"
    )

ntxTrapDataserviceIPIsUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1574)
)
ntxTrapDataserviceIPIsUnreachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDataserviceIPIsUnreachable.setStatus(
        "current"
    )

ntxTrapUSBBootDeviceMissingOnNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1575)
)
ntxTrapUSBBootDeviceMissingOnNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUSBBootDeviceMissingOnNode.setStatus(
        "current"
    )

ntxTrapVSSSnapshotOfContainerShareFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1576)
)
ntxTrapVSSSnapshotOfContainerShareFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVSSSnapshotOfContainerShareFailed.setStatus(
        "current"
    )

ntxTrapPrismIsRestartingFrequently = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1577)
)
ntxTrapPrismIsRestartingFrequently.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismIsRestartingFrequently.setStatus(
        "current"
    )

ntxTrapRecoveryPlanValidationFailedWithWarnings = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1578)
)
ntxTrapRecoveryPlanValidationFailedWithWarnings.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPlanValidationFailedWithWarnings.setStatus(
        "current"
    )

ntxTrapRecoveryPlanValidationFailedWithErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1579)
)
ntxTrapRecoveryPlanValidationFailedWithErrors.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPlanValidationFailedWithErrors.setStatus(
        "current"
    )

ntxTrapRecoveryPlanExecutionFailureDueToValidationErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1580)
)
ntxTrapRecoveryPlanExecutionFailureDueToValidationErrors.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPlanExecutionFailureDueToValidationErrors.setStatus(
        "current"
    )

ntxTrapInvalidNetworkSettingsForTheRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1581)
)
ntxTrapInvalidNetworkSettingsForTheRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInvalidNetworkSettingsForTheRecoveryPlan.setStatus(
        "current"
    )

ntxTrapRecoveryPlanExecutionFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1582)
)
ntxTrapRecoveryPlanExecutionFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPlanExecutionFailure.setStatus(
        "current"
    )

ntxTrapSubnetsDeletionFailureForTheRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1583)
)
ntxTrapSubnetsDeletionFailureForTheRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSubnetsDeletionFailureForTheRecoveryPlan.setStatus(
        "current"
    )

ntxTrapFloatingIPsDeallocationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1584)
)
ntxTrapFloatingIPsDeallocationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFloatingIPsDeallocationFailed.setStatus(
        "current"
    )

ntxTrapSubnetCreationFailureForTheRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1585)
)
ntxTrapSubnetCreationFailureForTheRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSubnetCreationFailureForTheRecoveryPlan.setStatus(
        "current"
    )

ntxTrapFloatingIPsAllocationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1586)
)
ntxTrapFloatingIPsAllocationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFloatingIPsAllocationFailed.setStatus(
        "current"
    )

ntxTrapFailoverOrFailbackOperationsAreNotPossible = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1587)
)
ntxTrapFailoverOrFailbackOperationsAreNotPossible.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailoverOrFailbackOperationsAreNotPossible.setStatus(
        "current"
    )

ntxTrapValidationWarningsFoundDuringRecoveryPlanExecution = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1588)
)
ntxTrapValidationWarningsFoundDuringRecoveryPlanExecution.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapValidationWarningsFoundDuringRecoveryPlanExecution.setStatus(
        "current"
    )

ntxTrapNodeRemovalFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1589)
)
ntxTrapNodeRemovalFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeRemovalFailure.setStatus(
        "current"
    )

ntxTrapConflictingNGTPolicies = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1590)
)
ntxTrapConflictingNGTPolicies.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapConflictingNGTPolicies.setStatus(
        "current"
    )

ntxTrapVmRestorationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1591)
)
ntxTrapVmRestorationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVmRestorationFailed.setStatus(
        "current"
    )

ntxTrapRecoveryLocationIsInReadOnlyMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1592)
)
ntxTrapRecoveryLocationIsInReadOnlyMode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryLocationIsInReadOnlyMode.setStatus(
        "current"
    )

ntxTrapNGTOnVMIsNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1593)
)
ntxTrapNGTOnVMIsNotReachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNGTOnVMIsNotReachable.setStatus(
        "current"
    )

ntxTrapNutanixGuestToolsNotInstalledOnTheVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1594)
)
ntxTrapNutanixGuestToolsNotInstalledOnTheVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixGuestToolsNotInstalledOnTheVM.setStatus(
        "current"
    )

ntxTrapFullReplicationStartedForTheVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1595)
)
ntxTrapFullReplicationStartedForTheVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFullReplicationStartedForTheVM.setStatus(
        "current"
    )

ntxTrapReplicationTimeExceededTheRPO = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1596)
)
ntxTrapReplicationTimeExceededTheRPO.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapReplicationTimeExceededTheRPO.setStatus(
        "current"
    )

ntxTrapNutanixVSSProviderOrprefreezepostthawScriptsNotInstalled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1597)
)
ntxTrapNutanixVSSProviderOrprefreezepostthawScriptsNotInstalled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixVSSProviderOrprefreezepostthawScriptsNotInstalled.setStatus(
        "current"
    )

ntxTrapFailedToFindTheTargetClusterForReplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1598)
)
ntxTrapFailedToFindTheTargetClusterForReplication.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToFindTheTargetClusterForReplication.setStatus(
        "current"
    )

ntxTrapVMVirtualHardwareVersionIncompatible = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1599)
)
ntxTrapVMVirtualHardwareVersionIncompatible.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMVirtualHardwareVersionIncompatible.setStatus(
        "current"
    )

ntxTrapVMMigrationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1600)
)
ntxTrapVMMigrationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMMigrationFailed.setStatus(
        "current"
    )

ntxTrapVMRegisteredWithoutAnyNetwork = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1601)
)
ntxTrapVMRegisteredWithoutAnyNetwork.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRegisteredWithoutAnyNetwork.setStatus(
        "current"
    )

ntxTrapProtectedVMNotRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1602)
)
ntxTrapProtectedVMNotRecoverable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMNotRecoverable.setStatus(
        "current"
    )

ntxTrapBackgroundEncryptionStuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1603)
)
ntxTrapBackgroundEncryptionStuck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapBackgroundEncryptionStuck.setStatus(
        "current"
    )

ntxTrapMaximumConnectionsLimitAboutToReachOnAFileServerVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1604)
)
ntxTrapMaximumConnectionsLimitAboutToReachOnAFileServerVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMaximumConnectionsLimitAboutToReachOnAFileServerVM.setStatus(
        "current"
    )

ntxTrapVSSSnapshotIsNotSupportedForSomeVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1605)
)
ntxTrapVSSSnapshotIsNotSupportedForSomeVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVSSSnapshotIsNotSupportedForSomeVMs.setStatus(
        "current"
    )

ntxTrapA110262 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1606)
)
ntxTrapA110262.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110262.setStatus(
        "current"
    )

ntxTrapIncorrectvmtypeNTPConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1607)
)
ntxTrapIncorrectvmtypeNTPConfiguration.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIncorrectvmtypeNTPConfiguration.setStatus(
        "current"
    )

ntxTrapThevmtypeIsNotSynchronizingTimeWithAnyExternalServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1608)
)
ntxTrapThevmtypeIsNotSynchronizingTimeWithAnyExternalServers.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapThevmtypeIsNotSynchronizingTimeWithAnyExternalServers.setStatus(
        "current"
    )

ntxTrapA103095 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1609)
)
ntxTrapA103095.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA103095.setStatus(
        "current"
    )

ntxTrapFirmwareVersionOfIntelS4600DrivesIsOldOrInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1610)
)
ntxTrapFirmwareVersionOfIntelS4600DrivesIsOldOrInvalid.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFirmwareVersionOfIntelS4600DrivesIsOldOrInvalid.setStatus(
        "current"
    )

ntxTrapRemotenameConnectivityStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1611)
)
ntxTrapRemotenameConnectivityStatus.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemotenameConnectivityStatus.setStatus(
        "current"
    )

ntxTrapIncompleteMetroSetup = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1612)
)
ntxTrapIncompleteMetroSetup.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIncompleteMetroSetup.setStatus(
        "current"
    )

ntxTrapA101047 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1613)
)
ntxTrapA101047.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA101047.setStatus(
        "current"
    )

ntxTrapP4GPUConfigurationWrongOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1614)
)
ntxTrapP4GPUConfigurationWrongOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapP4GPUConfigurationWrongOnTheNode.setStatus(
        "current"
    )

ntxTrapPCVMTypeOrAnnotationNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1615)
)
ntxTrapPCVMTypeOrAnnotationNotSet.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPCVMTypeOrAnnotationNotSet.setStatus(
        "current"
    )

ntxTrapFailedToConfigureHostForAtlasNetworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1616)
)
ntxTrapFailedToConfigureHostForAtlasNetworking.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToConfigureHostForAtlasNetworking.setStatus(
        "current"
    )

ntxTrapFailedToReserveHostMemoryForAtlasNetworking = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1617)
)
ntxTrapFailedToReserveHostMemoryForAtlasNetworking.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailedToReserveHostMemoryForAtlasNetworking.setStatus(
        "current"
    )

ntxTrapRecoveryPlanExecutionExceededTheTimeLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1618)
)
ntxTrapRecoveryPlanExecutionExceededTheTimeLimit.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPlanExecutionExceededTheTimeLimit.setStatus(
        "current"
    )

ntxTrapAHVPrismElementDetached = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1619)
)
ntxTrapAHVPrismElementDetached.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAHVPrismElementDetached.setStatus(
        "current"
    )

ntxTrapBeamIsNotReachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1620)
)
ntxTrapBeamIsNotReachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapBeamIsNotReachable.setStatus(
        "current"
    )

ntxTrapAHVPrismElementAttached = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1621)
)
ntxTrapAHVPrismElementAttached.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAHVPrismElementAttached.setStatus(
        "current"
    )

ntxTrapVPNIPSECTunnelBetweenOnpremAndXiDatacenterIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1622)
)
ntxTrapVPNIPSECTunnelBetweenOnpremAndXiDatacenterIsDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVPNIPSECTunnelBetweenOnpremAndXiDatacenterIsDown.setStatus(
        "current"
    )

ntxTrapEBGPSessionBetweenOnpremAndXiDatacenterIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1623)
)
ntxTrapEBGPSessionBetweenOnpremAndXiDatacenterIsDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEBGPSessionBetweenOnpremAndXiDatacenterIsDown.setStatus(
        "current"
    )

ntxTrapMaximumVPNBGPRouteLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1624)
)
ntxTrapMaximumVPNBGPRouteLimitReached.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMaximumVPNBGPRouteLimitReached.setStatus(
        "current"
    )

ntxTrapDomainFaultToleranceIsLowForMetadata = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1625)
)
ntxTrapDomainFaultToleranceIsLowForMetadata.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDomainFaultToleranceIsLowForMetadata.setStatus(
        "current"
    )

ntxTrapRecoveryLocationIsNotInGoodState = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1626)
)
ntxTrapRecoveryLocationIsNotInGoodState.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryLocationIsNotInGoodState.setStatus(
        "current"
    )

ntxTrapA110264 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1627)
)
ntxTrapA110264.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110264.setStatus(
        "current"
    )

ntxTrapFlowControlPlaneFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1628)
)
ntxTrapFlowControlPlaneFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFlowControlPlaneFailed.setStatus(
        "current"
    )

ntxTrapFlowRuleFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1629)
)
ntxTrapFlowRuleFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFlowRuleFailed.setStatus(
        "current"
    )

ntxTrapAnalyticsVMComponentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1630)
)
ntxTrapAnalyticsVMComponentFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAnalyticsVMComponentFailure.setStatus(
        "current"
    )

ntxTrapAnalyticsVMHighCPUUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1631)
)
ntxTrapAnalyticsVMHighCPUUsage.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAnalyticsVMHighCPUUsage.setStatus(
        "current"
    )

ntxTrapAnalyticsVMHighDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1632)
)
ntxTrapAnalyticsVMHighDiskUsage.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAnalyticsVMHighDiskUsage.setStatus(
        "current"
    )

ntxTrapAnalyticsVMLowMemoryAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1633)
)
ntxTrapAnalyticsVMLowMemoryAvailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAnalyticsVMLowMemoryAvailable.setStatus(
        "current"
    )

ntxTrapDuplicateIPAddressDetectedForAFileServerVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1634)
)
ntxTrapDuplicateIPAddressDetectedForAFileServerVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDuplicateIPAddressDetectedForAFileServerVM.setStatus(
        "current"
    )

ntxTrapFileServerUniqueFsidFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1635)
)
ntxTrapFileServerUniqueFsidFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerUniqueFsidFailure.setStatus(
        "current"
    )

ntxTrapUnequalDiskSizeOfPCVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1636)
)
ntxTrapUnequalDiskSizeOfPCVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnequalDiskSizeOfPCVMs.setStatus(
        "current"
    )

ntxTrapHighTimeDifferenceBetweenPCAndRegisteredPEs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1637)
)
ntxTrapHighTimeDifferenceBetweenPCAndRegisteredPEs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHighTimeDifferenceBetweenPCAndRegisteredPEs.setStatus(
        "current"
    )

ntxTrapPrismCentralVersionEOL = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1638)
)
ntxTrapPrismCentralVersionEOL.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralVersionEOL.setStatus(
        "current"
    )

ntxTrapPEPCIncompatibleAOSVersions = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1639)
)
ntxTrapPEPCIncompatibleAOSVersions.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPEPCIncompatibleAOSVersions.setStatus(
        "current"
    )

ntxTrapAplosGatewayIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1640)
)
ntxTrapAplosGatewayIsDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAplosGatewayIsDown.setStatus(
        "current"
    )

ntxTrapAplosEngineIsDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1641)
)
ntxTrapAplosEngineIsDown.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAplosEngineIsDown.setStatus(
        "current"
    )

ntxTrapStorageContainersAreNotMountedOnAllNodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1642)
)
ntxTrapStorageContainersAreNotMountedOnAllNodes.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStorageContainersAreNotMountedOnAllNodes.setStatus(
        "current"
    )

ntxTrapOldEntityCentricThirdPartyBackupSnapshotsPresent = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1643)
)
ntxTrapOldEntityCentricThirdPartyBackupSnapshotsPresent.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOldEntityCentricThirdPartyBackupSnapshotsPresent.setStatus(
        "current"
    )

ntxTrapUnsupportedSFPIsInstalledOnHostMachine = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1644)
)
ntxTrapUnsupportedSFPIsInstalledOnHostMachine.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnsupportedSFPIsInstalledOnHostMachine.setStatus(
        "current"
    )

ntxTrapMultipleRecoveryPlansAssociatedWithACategory = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1645)
)
ntxTrapMultipleRecoveryPlansAssociatedWithACategory.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMultipleRecoveryPlansAssociatedWithACategory.setStatus(
        "current"
    )

ntxTrapVMsArePartOfMultipleStagesInRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1646)
)
ntxTrapVMsArePartOfMultipleStagesInRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMsArePartOfMultipleStagesInRecoveryPlan.setStatus(
        "current"
    )

ntxTrapTestFailoverOnRecoveryPlanHasNotBeenExecutedRecently = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1647)
)
ntxTrapTestFailoverOnRecoveryPlanHasNotBeenExecutedRecently.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTestFailoverOnRecoveryPlanHasNotBeenExecutedRecently.setStatus(
        "current"
    )

ntxTrapNumberOfVMsInRecoveryPlanExceedsTheThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1648)
)
ntxTrapNumberOfVMsInRecoveryPlanExceedsTheThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNumberOfVMsInRecoveryPlanExceedsTheThreshold.setStatus(
        "current"
    )

ntxTrapSATADOMNeedsFirmwareUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1649)
)
ntxTrapSATADOMNeedsFirmwareUpgrade.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSATADOMNeedsFirmwareUpgrade.setStatus(
        "current"
    )

ntxTrapVCenterServerNotRegistered = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1650)
)
ntxTrapVCenterServerNotRegistered.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVCenterServerNotRegistered.setStatus(
        "current"
    )

ntxTrapDetectedOlderAHVVersion = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1651)
)
ntxTrapDetectedOlderAHVVersion.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDetectedOlderAHVVersion.setStatus(
        "current"
    )

ntxTrapNoProtectionPolicyFoundForVMsInRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1652)
)
ntxTrapNoProtectionPolicyFoundForVMsInRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNoProtectionPolicyFoundForVMsInRecoveryPlan.setStatus(
        "current"
    )

ntxTrapVMsNotCleanedUpFollowingTheTestFailoverForRecoveryPlan = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1653)
)
ntxTrapVMsNotCleanedUpFollowingTheTestFailoverForRecoveryPlan.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMsNotCleanedUpFollowingTheTestFailoverForRecoveryPlan.setStatus(
        "current"
    )

ntxTrapPowerSupplyStatusUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1654)
)
ntxTrapPowerSupplyStatusUnavailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPowerSupplyStatusUnavailable.setStatus(
        "current"
    )

ntxTrapCVMTimeAndIPMISELTimeDoNotMatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1655)
)
ntxTrapCVMTimeAndIPMISELTimeDoNotMatch.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMTimeAndIPMISELTimeDoNotMatch.setStatus(
        "current"
    )

ntxTrapProtectionPolicyMaxVMsPerCategoryCheckFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1656)
)
ntxTrapProtectionPolicyMaxVMsPerCategoryCheckFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionPolicyMaxVMsPerCategoryCheckFailed.setStatus(
        "current"
    )

ntxTrapPulseIsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1657)
)
ntxTrapPulseIsDisabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPulseIsDisabled.setStatus(
        "current"
    )

ntxTrapAOSVersionEOL = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1658)
)
ntxTrapAOSVersionEOL.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAOSVersionEOL.setStatus(
        "current"
    )

ntxTrapDIMMsOfDifferentManufacturersInOneMemoryChannel = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1659)
)
ntxTrapDIMMsOfDifferentManufacturersInOneMemoryChannel.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDIMMsOfDifferentManufacturersInOneMemoryChannel.setStatus(
        "current"
    )

ntxTrapPrismCentralUsingDefaultPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1660)
)
ntxTrapPrismCentralUsingDefaultPassword.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralUsingDefaultPassword.setStatus(
        "current"
    )

ntxTrapCVMUsingDefaultPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1661)
)
ntxTrapCVMUsingDefaultPassword.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMUsingDefaultPassword.setStatus(
        "current"
    )

ntxTrapHostUsingDefaultPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1662)
)
ntxTrapHostUsingDefaultPassword.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHostUsingDefaultPassword.setStatus(
        "current"
    )

ntxTrapIPMIUsingDefaultPassword = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1663)
)
ntxTrapIPMIUsingDefaultPassword.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIPMIUsingDefaultPassword.setStatus(
        "current"
    )

ntxTrapSM883DriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1664)
)
ntxTrapSM883DriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSM883DriveHasWornOut.setStatus(
        "current"
    )

ntxTrapFewerThanTwoNonSamsungPM883DrivesInstalledOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1665)
)
ntxTrapFewerThanTwoNonSamsungPM883DrivesInstalledOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFewerThanTwoNonSamsungPM883DrivesInstalledOnTheNode.setStatus(
        "current"
    )

ntxTrapPM883DriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1666)
)
ntxTrapPM883DriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPM883DriveHasWornOut.setStatus(
        "current"
    )

ntxTrapCalmVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1667)
)
ntxTrapCalmVersionMismatch.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCalmVersionMismatch.setStatus(
        "current"
    )

ntxTrapEpsilonVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1668)
)
ntxTrapEpsilonVersionMismatch.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEpsilonVersionMismatch.setStatus(
        "current"
    )

ntxTrapCalmShowbackIsUnableToReachBeamService = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1669)
)
ntxTrapCalmShowbackIsUnableToReachBeamService.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCalmShowbackIsUnableToReachBeamService.setStatus(
        "current"
    )

ntxTrapFileAnalyticsVMComponentFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1670)
)
ntxTrapFileAnalyticsVMComponentFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileAnalyticsVMComponentFailure.setStatus(
        "current"
    )

ntxTrapFileAnalyticsVMHighCPUUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1671)
)
ntxTrapFileAnalyticsVMHighCPUUsage.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileAnalyticsVMHighCPUUsage.setStatus(
        "current"
    )

ntxTrapFileAnalyticsVMHighDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1672)
)
ntxTrapFileAnalyticsVMHighDiskUsage.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileAnalyticsVMHighDiskUsage.setStatus(
        "current"
    )

ntxTrapFileAnalyticsVMLowMemoryAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1673)
)
ntxTrapFileAnalyticsVMLowMemoryAvailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileAnalyticsVMLowMemoryAvailable.setStatus(
        "current"
    )

ntxTrapFileServerVMTimeDriftFromNTPServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1674)
)
ntxTrapFileServerVMTimeDriftFromNTPServers.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerVMTimeDriftFromNTPServers.setStatus(
        "current"
    )

ntxTrapFileServerServiceInCrashLoop = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1675)
)
ntxTrapFileServerServiceInCrashLoop.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerServiceInCrashLoop.setStatus(
        "current"
    )

ntxTrapFileServerUpgradeTaskStuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1676)
)
ntxTrapFileServerUpgradeTaskStuck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerUpgradeTaskStuck.setStatus(
        "current"
    )

ntxTrapFilesClusterHATakeoverFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1677)
)
ntxTrapFilesClusterHATakeoverFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFilesClusterHATakeoverFailure.setStatus(
        "current"
    )

ntxTrapFileServerAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1678)
)
ntxTrapFileServerAlert.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerAlert.setStatus(
        "current"
    )

ntxTrapFlowModeChangeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1679)
)
ntxTrapFlowModeChangeFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFlowModeChangeFailed.setStatus(
        "current"
    )

ntxTrapOVSServiceRestart = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1680)
)
ntxTrapOVSServiceRestart.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOVSServiceRestart.setStatus(
        "current"
    )

ntxTrapRemoteSubnetIsNotConfiguredAppropriately = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1681)
)
ntxTrapRemoteSubnetIsNotConfiguredAppropriately.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSubnetIsNotConfiguredAppropriately.setStatus(
        "current"
    )

ntxTrapA130204 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1682)
)
ntxTrapA130204.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130204.setStatus(
        "current"
    )

ntxTrapA130205 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1683)
)
ntxTrapA130205.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130205.setStatus(
        "current"
    )

ntxTrapHostingOfVirtualIPOfTheNetworkSegmentationDRServiceFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1684)
)
ntxTrapHostingOfVirtualIPOfTheNetworkSegmentationDRServiceFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHostingOfVirtualIPOfTheNetworkSegmentationDRServiceFailed.setStatus(
        "current"
    )

ntxTrapFailureToCopyImageToCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1685)
)
ntxTrapFailureToCopyImageToCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFailureToCopyImageToCluster.setStatus(
        "current"
    )

ntxTrapIDFirewallConnectivityaccessLossToAD = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1686)
)
ntxTrapIDFirewallConnectivityaccessLossToAD.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIDFirewallConnectivityaccessLossToAD.setStatus(
        "current"
    )

ntxTrapEpochSaaSConnectivityIsLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1687)
)
ntxTrapEpochSaaSConnectivityIsLost.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEpochSaaSConnectivityIsLost.setStatus(
        "current"
    )

ntxTrapIDFirewallUnableToLocateMappedADObject = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1688)
)
ntxTrapIDFirewallUnableToLocateMappedADObject.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIDFirewallUnableToLocateMappedADObject.setStatus(
        "current"
    )

ntxTrapSecurityPlanningIsDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1689)
)
ntxTrapSecurityPlanningIsDisabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSecurityPlanningIsDisabled.setStatus(
        "current"
    )

ntxTrapEpochDataCollectorNeedsUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1690)
)
ntxTrapEpochDataCollectorNeedsUpgrade.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEpochDataCollectorNeedsUpgrade.setStatus(
        "current"
    )

ntxTrapIDFirewallUnableToRecoverStateFromADAfterDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1691)
)
ntxTrapIDFirewallUnableToRecoverStateFromADAfterDisconnect.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIDFirewallUnableToRecoverStateFromADAfterDisconnect.setStatus(
        "current"
    )

ntxTrapNGTCDROMNotUnmountedOnTheVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1692)
)
ntxTrapNGTCDROMNotUnmountedOnTheVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNGTCDROMNotUnmountedOnTheVM.setStatus(
        "current"
    )

ntxTrapFloatingIPsDeallocationFailedAfterFailbackFromXi = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1693)
)
ntxTrapFloatingIPsDeallocationFailedAfterFailbackFromXi.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFloatingIPsDeallocationFailedAfterFailbackFromXi.setStatus(
        "current"
    )

ntxTrapTomcatIsRestartingFrequently = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1694)
)
ntxTrapTomcatIsRestartingFrequently.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTomcatIsRestartingFrequently.setStatus(
        "current"
    )

ntxTrapExternalRepositoryAccessFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1695)
)
ntxTrapExternalRepositoryAccessFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapExternalRepositoryAccessFailure.setStatus(
        "current"
    )

ntxTrapIOFailuresToADataSourceInAnExternalRepository = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1697)
)
ntxTrapIOFailuresToADataSourceInAnExternalRepository.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIOFailuresToADataSourceInAnExternalRepository.setStatus(
        "current"
    )

ntxTrapUnequalDiskSizeOfPrismCentralVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1699)
)
ntxTrapUnequalDiskSizeOfPrismCentralVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnequalDiskSizeOfPrismCentralVMs.setStatus(
        "current"
    )

ntxTrapPCUpgradesAreDisabledOncvmip = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1700)
)
ntxTrapPCUpgradesAreDisabledOncvmip.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPCUpgradesAreDisabledOncvmip.setStatus(
        "current"
    )

ntxTrapCalmTrialLicenseExpiry = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1701)
)
ntxTrapCalmTrialLicenseExpiry.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCalmTrialLicenseExpiry.setStatus(
        "current"
    )

ntxTrapSystemNonRootPartitionsSpaceUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1702)
)
ntxTrapSystemNonRootPartitionsSpaceUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSystemNonRootPartitionsSpaceUsageHigh.setStatus(
        "current"
    )

ntxTrapSystemRootPartitionSpaceUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1703)
)
ntxTrapSystemRootPartitionSpaceUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSystemRootPartitionSpaceUsageHigh.setStatus(
        "current"
    )

ntxTrapscratchLocationSpaceUsageIsHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1704)
)
ntxTrapscratchLocationSpaceUsageIsHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapscratchLocationSpaceUsageIsHigh.setStatus(
        "current"
    )

ntxTrapFreeBlockCountOfSATADOMHasGoneBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1705)
)
ntxTrapFreeBlockCountOfSATADOMHasGoneBelowThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFreeBlockCountOfSATADOMHasGoneBelowThreshold.setStatus(
        "current"
    )

ntxTrapToshibaPM5DriveHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1706)
)
ntxTrapToshibaPM5DriveHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapToshibaPM5DriveHasWornOut.setStatus(
        "current"
    )

ntxTrapMoreThanOneTypeOfToshibaPM5DrivesInstalledOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1707)
)
ntxTrapMoreThanOneTypeOfToshibaPM5DrivesInstalledOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMoreThanOneTypeOfToshibaPM5DrivesInstalledOnTheNode.setStatus(
        "current"
    )

ntxTrapBootDriveIsInDegradedState = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1708)
)
ntxTrapBootDriveIsInDegradedState.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapBootDriveIsInDegradedState.setStatus(
        "current"
    )

ntxTrapTemperatureOfM2DiskIsOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1709)
)
ntxTrapTemperatureOfM2DiskIsOutOfRange.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTemperatureOfM2DiskIsOutOfRange.setStatus(
        "current"
    )

ntxTrapM2DiskReturnedUECCErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1710)
)
ntxTrapM2DiskReturnedUECCErrors.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapM2DiskReturnedUECCErrors.setStatus(
        "current"
    )

ntxTrapM2DiskHasWornOut = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1711)
)
ntxTrapM2DiskHasWornOut.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapM2DiskHasWornOut.setStatus(
        "current"
    )

ntxTrapFirmwareOfRaidM2DiskNeedsToBeUpgraded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1712)
)
ntxTrapFirmwareOfRaidM2DiskNeedsToBeUpgraded.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFirmwareOfRaidM2DiskNeedsToBeUpgraded.setStatus(
        "current"
    )

ntxTrapRAIDCardBIOSOrFirmwareOrBootLoaderNeedsToBeUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1713)
)
ntxTrapRAIDCardBIOSOrFirmwareOrBootLoaderNeedsToBeUpdated.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRAIDCardBIOSOrFirmwareOrBootLoaderNeedsToBeUpdated.setStatus(
        "current"
    )

ntxTrapDiskFirmwareNeedsUpgrade = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1714)
)
ntxTrapDiskFirmwareNeedsUpgrade.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDiskFirmwareNeedsUpgrade.setStatus(
        "current"
    )

ntxTrapFlowPolicyhitLoggingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1715)
)
ntxTrapFlowPolicyhitLoggingDisabled.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFlowPolicyhitLoggingDisabled.setStatus(
        "current"
    )

ntxTrapLatencyBetweenvmtypes = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1716)
)
ntxTrapLatencyBetweenvmtypes.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLatencyBetweenvmtypes.setStatus(
        "current"
    )

ntxTrapCVMdestipIsUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1717)
)
ntxTrapCVMdestipIsUnreachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMdestipIsUnreachable.setStatus(
        "current"
    )

ntxTrapComputeonlyMinimumBandwidthCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1718)
)
ntxTrapComputeonlyMinimumBandwidthCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapComputeonlyMinimumBandwidthCheck.setStatus(
        "current"
    )

ntxTrapFileServerVMDownCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1719)
)
ntxTrapFileServerVMDownCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerVMDownCheck.setStatus(
        "current"
    )

ntxTrapFileServerVMHardwareClockTimezoneNotSupported = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1720)
)
ntxTrapFileServerVMHardwareClockTimezoneNotSupported.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerVMHardwareClockTimezoneNotSupported.setStatus(
        "current"
    )

ntxTrapNutanixFilesVersionEOL = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1721)
)
ntxTrapNutanixFilesVersionEOL.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNutanixFilesVersionEOL.setStatus(
        "current"
    )

ntxTrapFileServerContainerDedupCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1722)
)
ntxTrapFileServerContainerDedupCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerContainerDedupCheck.setStatus(
        "current"
    )

ntxTrapCheckingIfTargetClusterVersionIsGreaterThan512 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1723)
)
ntxTrapCheckingIfTargetClusterVersionIsGreaterThan512.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCheckingIfTargetClusterVersionIsGreaterThan512.setStatus(
        "current"
    )

ntxTrapCheckingIfPortsOfRelevantServicesAreOpenOrNot = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1724)
)
ntxTrapCheckingIfPortsOfRelevantServicesAreOpenOrNot.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCheckingIfPortsOfRelevantServicesAreOpenOrNot.setStatus(
        "current"
    )

ntxTrapA110022 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1725)
)
ntxTrapA110022.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110022.setStatus(
        "current"
    )

ntxTrapCheckingIfDRServicesAreReachableOrNot = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1726)
)
ntxTrapCheckingIfDRServicesAreReachableOrNot.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCheckingIfDRServicesAreReachableOrNot.setStatus(
        "current"
    )

ntxTrapHighNumberOfCorrectableECCErrorsFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1727)
)
ntxTrapHighNumberOfCorrectableECCErrorsFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHighNumberOfCorrectableECCErrorsFound.setStatus(
        "current"
    )

ntxTrapPowerSuppliesOfDifferentTypesDetectedOnANode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1728)
)
ntxTrapPowerSuppliesOfDifferentTypesDetectedOnANode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPowerSuppliesOfDifferentTypesDetectedOnANode.setStatus(
        "current"
    )

ntxTrapPowerSupplyStatusDownUnretrievable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1729)
)
ntxTrapPowerSupplyStatusDownUnretrievable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPowerSupplyStatusDownUnretrievable.setStatus(
        "current"
    )

ntxTrapProtectedVMNameTooLongOrContainsRestrictedCharacters = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1730)
)
ntxTrapProtectedVMNameTooLongOrContainsRestrictedCharacters.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMNameTooLongOrContainsRestrictedCharacters.setStatus(
        "current"
    )

ntxTrapDetectedSnapshotsOnClusterWithHighDensityNodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1731)
)
ntxTrapDetectedSnapshotsOnClusterWithHighDensityNodes.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDetectedSnapshotsOnClusterWithHighDensityNodes.setStatus(
        "current"
    )

ntxTrapDataProtectionIsConfiguredOnClusterWithHighDensityNodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1732)
)
ntxTrapDataProtectionIsConfiguredOnClusterWithHighDensityNodes.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDataProtectionIsConfiguredOnClusterWithHighDensityNodes.setStatus(
        "current"
    )

ntxTrapA110452 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1733)
)
ntxTrapA110452.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110452.setStatus(
        "current"
    )

ntxTrapA110453 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1734)
)
ntxTrapA110453.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110453.setStatus(
        "current"
    )

ntxTrapNetworkIsNotProperlyConfiguredOnTheHost = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1735)
)
ntxTrapNetworkIsNotProperlyConfiguredOnTheHost.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNetworkIsNotProperlyConfiguredOnTheHost.setStatus(
        "current"
    )

ntxTrapDisconnectedAvailabilityZonesAreAffectingSomeEntities = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1736)
)
ntxTrapDisconnectedAvailabilityZonesAreAffectingSomeEntities.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDisconnectedAvailabilityZonesAreAffectingSomeEntities.setStatus(
        "current"
    )

ntxTrapRecoveryPlanHasMultipleAvailabilityZoneOrders = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1737)
)
ntxTrapRecoveryPlanHasMultipleAvailabilityZoneOrders.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPlanHasMultipleAvailabilityZoneOrders.setStatus(
        "current"
    )

ntxTrapRecoveryPlanContainsVMsWithUnsupportedCHDRVMConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1738)
)
ntxTrapRecoveryPlanContainsVMsWithUnsupportedCHDRVMConfiguration.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPlanContainsVMsWithUnsupportedCHDRVMConfiguration.setStatus(
        "current"
    )

ntxTrapA300426 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1739)
)
ntxTrapA300426.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300426.setStatus(
        "current"
    )

ntxTrapA300428 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1740)
)
ntxTrapA300428.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300428.setStatus(
        "current"
    )

ntxTrapvmtypeRebooted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1741)
)
ntxTrapvmtypeRebooted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapvmtypeRebooted.setStatus(
        "current"
    )

ntxTrapNodeIsInDegradedState = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1742)
)
ntxTrapNodeIsInDegradedState.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeIsInDegradedState.setStatus(
        "current"
    )

ntxTrapComputeonlyClusterSizingHyperconvergedNodeCountCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1743)
)
ntxTrapComputeonlyClusterSizingHyperconvergedNodeCountCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapComputeonlyClusterSizingHyperconvergedNodeCountCheck.setStatus(
        "current"
    )

ntxTrapA405001 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1744)
)
ntxTrapA405001.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA405001.setStatus(
        "current"
    )

ntxTrapComputeonlyClusterSizingCVMSizeCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1745)
)
ntxTrapComputeonlyClusterSizingCVMSizeCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapComputeonlyClusterSizingCVMSizeCheck.setStatus(
        "current"
    )

ntxTrapCalmContainersAreUnhealthy = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1746)
)
ntxTrapCalmContainersAreUnhealthy.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCalmContainersAreUnhealthy.setStatus(
        "current"
    )

ntxTrapHealthWarningsDetectedInMetadataService = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1747)
)
ntxTrapHealthWarningsDetectedInMetadataService.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHealthWarningsDetectedInMetadataService.setStatus(
        "current"
    )

ntxTrapProtectedVMsNotCBRCapable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1748)
)
ntxTrapProtectedVMsNotCBRCapable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMsNotCBRCapable.setStatus(
        "current"
    )

ntxTrapAutoSupportCheckFails = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1749)
)
ntxTrapAutoSupportCheckFails.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAutoSupportCheckFails.setStatus(
        "current"
    )

ntxTrapCoreDumpsAreEnabledOnThisCVMOrPCVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1750)
)
ntxTrapCoreDumpsAreEnabledOnThisCVMOrPCVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCoreDumpsAreEnabledOnThisCVMOrPCVM.setStatus(
        "current"
    )

ntxTrapUnequalMetadataPartitionSizesAcrossPrismCentralVMs = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1751)
)
ntxTrapUnequalMetadataPartitionSizesAcrossPrismCentralVMs.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapUnequalMetadataPartitionSizesAcrossPrismCentralVMs.setStatus(
        "current"
    )

ntxTrapFileServerCloneGracePeriodCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1752)
)
ntxTrapFileServerCloneGracePeriodCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerCloneGracePeriodCheck.setStatus(
        "current"
    )

ntxTrapVMRecoveryStorageContainerIsNotMountedOnAllHosts = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1753)
)
ntxTrapVMRecoveryStorageContainerIsNotMountedOnAllHosts.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRecoveryStorageContainerIsNotMountedOnAllHosts.setStatus(
        "current"
    )

ntxTrapOpenflowTableGettingFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1754)
)
ntxTrapOpenflowTableGettingFull.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOpenflowTableGettingFull.setStatus(
        "current"
    )

ntxTrapNumberOfDatastoresConfiguredIsHigherThanESXiMaxConnPerIP = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1755)
)
ntxTrapNumberOfDatastoresConfiguredIsHigherThanESXiMaxConnPerIP.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNumberOfDatastoresConfiguredIsHigherThanESXiMaxConnPerIP.setStatus(
        "current"
    )

ntxTrapA110021 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1756)
)
ntxTrapA110021.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110021.setStatus(
        "current"
    )

ntxTrapCheckingIfPortsOfRelevantServicesAreOpen = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1757)
)
ntxTrapCheckingIfPortsOfRelevantServicesAreOpen.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCheckingIfPortsOfRelevantServicesAreOpen.setStatus(
        "current"
    )

ntxTrapProtectedVMsMayNotBeRecoverable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1758)
)
ntxTrapProtectedVMsMayNotBeRecoverable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMsMayNotBeRecoverable.setStatus(
        "current"
    )

ntxTrapExternallyRegisteredAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1759)
)
ntxTrapExternallyRegisteredAlert.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapExternallyRegisteredAlert.setStatus(
        "current"
    )

ntxTrapInvalidBreakReplicationTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1760)
)
ntxTrapInvalidBreakReplicationTimeout.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInvalidBreakReplicationTimeout.setStatus(
        "current"
    )

ntxTrapBridgevSwitchConfigurationDoesNotMatchNSProtoInZookeeper = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1761)
)
ntxTrapBridgevSwitchConfigurationDoesNotMatchNSProtoInZookeeper.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapBridgevSwitchConfigurationDoesNotMatchNSProtoInZookeeper.setStatus(
        "current"
    )

ntxTrapActiveDirectoryDCsRunningOnCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1762)
)
ntxTrapActiveDirectoryDCsRunningOnCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapActiveDirectoryDCsRunningOnCluster.setStatus(
        "current"
    )

ntxTrapDNSServersRunningOnCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1763)
)
ntxTrapDNSServersRunningOnCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDNSServersRunningOnCluster.setStatus(
        "current"
    )

ntxTrapCPUUsageIsHighOnCVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1764)
)
ntxTrapCPUUsageIsHighOnCVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCPUUsageIsHighOnCVM.setStatus(
        "current"
    )

ntxTrapSMARTParametersOfDiskAreOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1765)
)
ntxTrapSMARTParametersOfDiskAreOutOfRange.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSMARTParametersOfDiskAreOutOfRange.setStatus(
        "current"
    )

ntxTrapMinimumNOSAndFoundationVersionsAreNotSatisfied = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1766)
)
ntxTrapMinimumNOSAndFoundationVersionsAreNotSatisfied.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMinimumNOSAndFoundationVersionsAreNotSatisfied.setStatus(
        "current"
    )

ntxTrapPCVMSystemRootPartitionSpaceUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1767)
)
ntxTrapPCVMSystemRootPartitionSpaceUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPCVMSystemRootPartitionSpaceUsageHigh.setStatus(
        "current"
    )

ntxTrapA300430 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1768)
)
ntxTrapA300430.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA300430.setStatus(
        "current"
    )

ntxTrapCVMPythonServicesRestartingFrequently = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1769)
)
ntxTrapCVMPythonServicesRestartingFrequently.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMPythonServicesRestartingFrequently.setStatus(
        "current"
    )

ntxTrapSnapshotReplicationToRemoteSiteIsLagging = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1770)
)
ntxTrapSnapshotReplicationToRemoteSiteIsLagging.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSnapshotReplicationToRemoteSiteIsLagging.setStatus(
        "current"
    )

ntxTrapSMARTParametersOfDiskhostAreOutOfRange = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1771)
)
ntxTrapSMARTParametersOfDiskhostAreOutOfRange.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSMARTParametersOfDiskhostAreOutOfRange.setStatus(
        "current"
    )

ntxTrapOneOrMoreCassandraNodesHaveInvalidTokens = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1772)
)
ntxTrapOneOrMoreCassandraNodesHaveInvalidTokens.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOneOrMoreCassandraNodesHaveInvalidTokens.setStatus(
        "current"
    )

ntxTrapSecureBootFeatureStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1773)
)
ntxTrapSecureBootFeatureStatus.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSecureBootFeatureStatus.setStatus(
        "current"
    )

ntxTrapVMHasBeenRecoveredAtAnAlternatePath = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1774)
)
ntxTrapVMHasBeenRecoveredAtAnAlternatePath.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMHasBeenRecoveredAtAnAlternatePath.setStatus(
        "current"
    )

ntxTrapInvalidHybridNodesConfigurationForErasureCoding = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1775)
)
ntxTrapInvalidHybridNodesConfigurationForErasureCoding.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInvalidHybridNodesConfigurationForErasureCoding.setStatus(
        "current"
    )

ntxTrapPlannedFailoverOrUnplannedFailoverOperationsWillFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1776)
)
ntxTrapPlannedFailoverOrUnplannedFailoverOperationsWillFail.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPlannedFailoverOrUnplannedFailoverOperationsWillFail.setStatus(
        "current"
    )

ntxTrapFileServerManagerUpgradeFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1777)
)
ntxTrapFileServerManagerUpgradeFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerManagerUpgradeFailed.setStatus(
        "current"
    )

ntxTrapSEDKeysUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1778)
)
ntxTrapSEDKeysUnavailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSEDKeysUnavailable.setStatus(
        "current"
    )

ntxTrapSWEncryptionKeysFromkmsnameAreUnavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1779)
)
ntxTrapSWEncryptionKeysFromkmsnameAreUnavailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSWEncryptionKeysFromkmsnameAreUnavailable.setStatus(
        "current"
    )

ntxTrapOVAUploadInterrupted = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1780)
)
ntxTrapOVAUploadInterrupted.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOVAUploadInterrupted.setStatus(
        "current"
    )

ntxTrapCVMOrPrismCentralVMRAMUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1781)
)
ntxTrapCVMOrPrismCentralVMRAMUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMOrPrismCentralVMRAMUsageHigh.setStatus(
        "current"
    )

ntxTrapPrismCentralVMCPULoadHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1782)
)
ntxTrapPrismCentralVMCPULoadHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralVMCPULoadHigh.setStatus(
        "current"
    )

ntxTrapPrismCentralVMDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1783)
)
ntxTrapPrismCentralVMDiskUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralVMDiskUsageHigh.setStatus(
        "current"
    )

ntxTrapPrismCentralVMSystemRootPartitionSpaceUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1784)
)
ntxTrapPrismCentralVMSystemRootPartitionSpaceUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralVMSystemRootPartitionSpaceUsageHigh.setStatus(
        "current"
    )

ntxTrapPrismCentralVMLimitCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1785)
)
ntxTrapPrismCentralVMLimitCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralVMLimitCheck.setStatus(
        "current"
    )

ntxTrapCoreDumpsAreEnabledOnThisCVMOrPrismCentralVM = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1786)
)
ntxTrapCoreDumpsAreEnabledOnThisCVMOrPrismCentralVM.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCoreDumpsAreEnabledOnThisCVMOrPrismCentralVM.setStatus(
        "current"
    )

ntxTrapClusterDoesNotSupportSynchronousReplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1787)
)
ntxTrapClusterDoesNotSupportSynchronousReplication.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterDoesNotSupportSynchronousReplication.setStatus(
        "current"
    )

ntxTrapPrismCentralVMHomePartitionDiskUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1788)
)
ntxTrapPrismCentralVMHomePartitionDiskUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralVMHomePartitionDiskUsageHigh.setStatus(
        "current"
    )

ntxTrapFilesLicenseInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1789)
)
ntxTrapFilesLicenseInvalid.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFilesLicenseInvalid.setStatus(
        "current"
    )

ntxTrapSATAControllerStatusIsBad = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1790)
)
ntxTrapSATAControllerStatusIsBad.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSATAControllerStatusIsBad.setStatus(
        "current"
    )

ntxTrapFileSystemInconsistenciesAreDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1791)
)
ntxTrapFileSystemInconsistenciesAreDetected.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileSystemInconsistenciesAreDetected.setStatus(
        "current"
    )

ntxTrapSameTimezoneCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1792)
)
ntxTrapSameTimezoneCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSameTimezoneCheck.setStatus(
        "current"
    )

ntxTrapStoragePoolSpaceUsageExceededTheConfiguredThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1793)
)
ntxTrapStoragePoolSpaceUsageExceededTheConfiguredThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStoragePoolSpaceUsageExceededTheConfiguredThreshold.setStatus(
        "current"
    )

ntxTrapHypervisorDiskUsageIsAboveTheRecommendedThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1794)
)
ntxTrapHypervisorDiskUsageIsAboveTheRecommendedThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHypervisorDiskUsageIsAboveTheRecommendedThreshold.setStatus(
        "current"
    )

ntxTrapInvalidSSDHDDDriveCombination = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1795)
)
ntxTrapInvalidSSDHDDDriveCombination.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInvalidSSDHDDDriveCombination.setStatus(
        "current"
    )

ntxTrapNodeMaintenanceModeFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1796)
)
ntxTrapNodeMaintenanceModeFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeMaintenanceModeFailure.setStatus(
        "current"
    )

ntxTrapDiskFailedMarkedOffline = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1797)
)
ntxTrapDiskFailedMarkedOffline.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDiskFailedMarkedOffline.setStatus(
        "current"
    )

ntxTrapVirtualIPCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1798)
)
ntxTrapVirtualIPCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVirtualIPCheck.setStatus(
        "current"
    )

ntxTrapInsufficientHostBandwidth = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1799)
)
ntxTrapInsufficientHostBandwidth.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInsufficientHostBandwidth.setStatus(
        "current"
    )

ntxTrapOrphanedVSSCopiesAreDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1800)
)
ntxTrapOrphanedVSSCopiesAreDetected.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapOrphanedVSSCopiesAreDetected.setStatus(
        "current"
    )

ntxTrapStorageContainerSpaceUsageExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1801)
)
ntxTrapStorageContainerSpaceUsageExceeded.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStorageContainerSpaceUsageExceeded.setStatus(
        "current"
    )

ntxTrapTwoNodeClusterStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1802)
)
ntxTrapTwoNodeClusterStateChanged.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTwoNodeClusterStateChanged.setStatus(
        "current"
    )

ntxTrapStateChangedForTwoNodeCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1803)
)
ntxTrapStateChangedForTwoNodeCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStateChangedForTwoNodeCluster.setStatus(
        "current"
    )

ntxTrapInsufficientSpaceForUVMsDeployedOnPC = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1804)
)
ntxTrapInsufficientSpaceForUVMsDeployedOnPC.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInsufficientSpaceForUVMsDeployedOnPC.setStatus(
        "current"
    )

ntxTrapLicensingWorkflowIsIncomplete = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1805)
)
ntxTrapLicensingWorkflowIsIncomplete.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLicensingWorkflowIsIncomplete.setStatus(
        "current"
    )

ntxTrapInconsistentBridgevSwitchConfiguration = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1806)
)
ntxTrapInconsistentBridgevSwitchConfiguration.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInconsistentBridgevSwitchConfiguration.setStatus(
        "current"
    )

ntxTrapPowerCycleVMsBeforePerformingUpgradeOrMigrateOperation = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1807)
)
ntxTrapPowerCycleVMsBeforePerformingUpgradeOrMigrateOperation.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPowerCycleVMsBeforePerformingUpgradeOrMigrateOperation.setStatus(
        "current"
    )

ntxTrapStorageContainersIsareNotMountedOnAllNodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1808)
)
ntxTrapStorageContainersIsareNotMountedOnAllNodes.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapStorageContainersIsareNotMountedOnAllNodes.setStatus(
        "current"
    )

ntxTrapVMRecoveryStorageContainersIsareNotMountedOnAllHosts = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1809)
)
ntxTrapVMRecoveryStorageContainersIsareNotMountedOnAllHosts.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRecoveryStorageContainersIsareNotMountedOnAllHosts.setStatus(
        "current"
    )

ntxTrapFlowPolicyhitLoggingIsNotFunctional = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1810)
)
ntxTrapFlowPolicyhitLoggingIsNotFunctional.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFlowPolicyhitLoggingIsNotFunctional.setStatus(
        "current"
    )

ntxTrapEpochSaaSServiceConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1811)
)
ntxTrapEpochSaaSServiceConnectivityLost.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEpochSaaSServiceConnectivityLost.setStatus(
        "current"
    )

ntxTrapIDFirewallLostConnectivityToDomainController = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1812)
)
ntxTrapIDFirewallLostConnectivityToDomainController.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIDFirewallLostConnectivityToDomainController.setStatus(
        "current"
    )

ntxTrapEpochDataCollectorUpgradeAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1813)
)
ntxTrapEpochDataCollectorUpgradeAvailable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEpochDataCollectorUpgradeAvailable.setStatus(
        "current"
    )

ntxTrapA803005 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1814)
)
ntxTrapA803005.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA803005.setStatus(
        "current"
    )

ntxTrapIDFirewallUnableToLocateMappedActiveDirectoryObject = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1815)
)
ntxTrapIDFirewallUnableToLocateMappedActiveDirectoryObject.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapIDFirewallUnableToLocateMappedActiveDirectoryObject.setStatus(
        "current"
    )

ntxTrapSkippedReplicationOfSnapshotForProtectionDomain = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1816)
)
ntxTrapSkippedReplicationOfSnapshotForProtectionDomain.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSkippedReplicationOfSnapshotForProtectionDomain.setStatus(
        "current"
    )

ntxTrapInconsistentFileGroupsInTheSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1817)
)
ntxTrapInconsistentFileGroupsInTheSystem.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInconsistentFileGroupsInTheSystem.setStatus(
        "current"
    )

ntxTrapVMRestorationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1818)
)
ntxTrapVMRestorationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRestorationFailed.setStatus(
        "current"
    )

ntxTrapMetadataServiceRestartingFrequentlyDueToLongGCPauses = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1819)
)
ntxTrapMetadataServiceRestartingFrequentlyDueToLongGCPauses.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetadataServiceRestartingFrequentlyDueToLongGCPauses.setStatus(
        "current"
    )

ntxTrapA130206 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1820)
)
ntxTrapA130206.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130206.setStatus(
        "current"
    )

ntxTrapSomeOfTheVMsInTheRecoveryPlanAreUnprotected = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1821)
)
ntxTrapSomeOfTheVMsInTheRecoveryPlanAreUnprotected.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSomeOfTheVMsInTheRecoveryPlanAreUnprotected.setStatus(
        "current"
    )

ntxTrapRemoteSiteIsIncompatibleForReplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1822)
)
ntxTrapRemoteSiteIsIncompatibleForReplication.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteIsIncompatibleForReplication.setStatus(
        "current"
    )

ntxTrapFileServerContainerHasUnexpectedFiles = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1823)
)
ntxTrapFileServerContainerHasUnexpectedFiles.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapFileServerContainerHasUnexpectedFiles.setStatus(
        "current"
    )

ntxTrapControllerVMTimeNotSynchronizedWithExternalServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1824)
)
ntxTrapControllerVMTimeNotSynchronizedWithExternalServers.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapControllerVMTimeNotSynchronizedWithExternalServers.setStatus(
        "current"
    )

ntxTrapHypervisorTimeNotSynchronisedWithAnyExternalServers = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1825)
)
ntxTrapHypervisorTimeNotSynchronisedWithAnyExternalServers.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHypervisorTimeNotSynchronisedWithAnyExternalServers.setStatus(
        "current"
    )

ntxTrapA110454 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1826)
)
ntxTrapA110454.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA110454.setStatus(
        "current"
    )

ntxTrapNearSyncReplicationOfProtectionDomainHasNotProgressed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1827)
)
ntxTrapNearSyncReplicationOfProtectionDomainHasNotProgressed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNearSyncReplicationOfProtectionDomainHasNotProgressed.setStatus(
        "current"
    )

ntxTrapPrismCentralVMTypeOrAnnotationNotSet = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1828)
)
ntxTrapPrismCentralVMTypeOrAnnotationNotSet.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralVMTypeOrAnnotationNotSet.setStatus(
        "current"
    )

ntxTrapA200309 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1829)
)
ntxTrapA200309.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA200309.setStatus(
        "current"
    )

ntxTrapPrismCentralVCPUAvailabilityCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1830)
)
ntxTrapPrismCentralVCPUAvailabilityCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralVCPUAvailabilityCheck.setStatus(
        "current"
    )

ntxTrapPrismCentralMemoryAvailabilityCheck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1831)
)
ntxTrapPrismCentralMemoryAvailabilityCheck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralMemoryAvailabilityCheck.setStatus(
        "current"
    )

ntxTrapPrismCentralUpgradesAreDisabledOncvmip = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1832)
)
ntxTrapPrismCentralUpgradesAreDisabledOncvmip.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapPrismCentralUpgradesAreDisabledOncvmip.setStatus(
        "current"
    )

ntxTrapHighNumberOfCorrectableUECCErrorsFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1833)
)
ntxTrapHighNumberOfCorrectableUECCErrorsFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHighNumberOfCorrectableUECCErrorsFound.setStatus(
        "current"
    )

ntxTrapTemperatureOfRAIDCardIsOutOfAboveThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1834)
)
ntxTrapTemperatureOfRAIDCardIsOutOfAboveThreshold.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTemperatureOfRAIDCardIsOutOfAboveThreshold.setStatus(
        "current"
    )

ntxTrapCVMIPAddressIsUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1835)
)
ntxTrapCVMIPAddressIsUnreachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapCVMIPAddressIsUnreachable.setStatus(
        "current"
    )

ntxTrapA1191 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1836)
)
ntxTrapA1191.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA1191.setStatus(
        "current"
    )

ntxTrapDegradedRecoveryPoint = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1837)
)
ntxTrapDegradedRecoveryPoint.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDegradedRecoveryPoint.setStatus(
        "current"
    )

ntxTrapDIMMHPPRFailureEventFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1838)
)
ntxTrapDIMMHPPRFailureEventFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDIMMHPPRFailureEventFound.setStatus(
        "current"
    )

ntxTrapM60GPUConfigurationIncorrectOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1839)
)
ntxTrapM60GPUConfigurationIncorrectOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapM60GPUConfigurationIncorrectOnTheNode.setStatus(
        "current"
    )

ntxTrapM10GPUConfigurationIncorrectOnTheNode = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1840)
)
ntxTrapM10GPUConfigurationIncorrectOnTheNode.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapM10GPUConfigurationIncorrectOnTheNode.setStatus(
        "current"
    )

ntxTrapHostBootDiskRequiresAttention = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1841)
)
ntxTrapHostBootDiskRequiresAttention.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapHostBootDiskRequiresAttention.setStatus(
        "current"
    )

ntxTrapA130177 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1842)
)
ntxTrapA130177.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130177.setStatus(
        "current"
    )

ntxTrapA130173 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1843)
)
ntxTrapA130173.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA130173.setStatus(
        "current"
    )

ntxTrapProtectionDomainActivationFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1844)
)
ntxTrapProtectionDomainActivationFailed.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectionDomainActivationFailed.setStatus(
        "current"
    )

ntxTrapAssociatedEntitiesAreNotProtectedTogether = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1845)
)
ntxTrapAssociatedEntitiesAreNotProtectedTogether.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapAssociatedEntitiesAreNotProtectedTogether.setStatus(
        "current"
    )

ntxTrapEntityConflictInConsistencyGroups = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1846)
)
ntxTrapEntityConflictInConsistencyGroups.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapEntityConflictInConsistencyGroups.setStatus(
        "current"
    )

ntxTrapVMSyncRepContainerNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1847)
)
ntxTrapVMSyncRepContainerNotFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMSyncRepContainerNotFound.setStatus(
        "current"
    )

ntxTrapRemoteSiteIsUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1848)
)
ntxTrapRemoteSiteIsUnreachable.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRemoteSiteIsUnreachable.setStatus(
        "current"
    )

ntxTrapNFSMetadataUsageHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1849)
)
ntxTrapNFSMetadataUsageHigh.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNFSMetadataUsageHigh.setStatus(
        "current"
    )

ntxTrapSSDTierSizeIsSmallOnOneOrMoreNodes = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1850)
)
ntxTrapSSDTierSizeIsSmallOnOneOrMoreNodes.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSSDTierSizeIsSmallOnOneOrMoreNodes.setStatus(
        "current"
    )

ntxTrapClusterIsSusceptibleToCopyUpBlockMapIssue = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1851)
)
ntxTrapClusterIsSusceptibleToCopyUpBlockMapIssue.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapClusterIsSusceptibleToCopyUpBlockMapIssue.setStatus(
        "current"
    )

ntxTrapMemoryOvercommitFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1852)
)
ntxTrapMemoryOvercommitFailure.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMemoryOvercommitFailure.setStatus(
        "current"
    )

ntxTrapProtectedVMIsNotCapableOfBackupAndRecovery = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1853)
)
ntxTrapProtectedVMIsNotCapableOfBackupAndRecovery.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMIsNotCapableOfBackupAndRecovery.setStatus(
        "current"
    )

ntxTrapProtectedVMsNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1854)
)
ntxTrapProtectedVMsNotFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapProtectedVMsNotFound.setStatus(
        "current"
    )

ntxTrapDuplicateDiskIDsPresentInDifferentNodesOfTheSameCluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1855)
)
ntxTrapDuplicateDiskIDsPresentInDifferentNodesOfTheSameCluster.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapDuplicateDiskIDsPresentInDifferentNodesOfTheSameCluster.setStatus(
        "current"
    )

ntxTrapRecoveryPointExpiredPriorToStartOfReplication = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1856)
)
ntxTrapRecoveryPointExpiredPriorToStartOfReplication.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapRecoveryPointExpiredPriorToStartOfReplication.setStatus(
        "current"
    )

ntxTrapTooManySnapshotsInTheSystem = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1857)
)
ntxTrapTooManySnapshotsInTheSystem.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapTooManySnapshotsInTheSystem.setStatus(
        "current"
    )

ntxTrapA150003 = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1858)
)
ntxTrapA150003.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapA150003.setStatus(
        "current"
    )

ntxTrapInvalidRoutesReceivedFromOnpremVPNGateway = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1859)
)
ntxTrapInvalidRoutesReceivedFromOnpremVPNGateway.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapInvalidRoutesReceivedFromOnpremVPNGateway.setStatus(
        "current"
    )

ntxTrapVMRenamedOnRestoration = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1860)
)
ntxTrapVMRenamedOnRestoration.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVMRenamedOnRestoration.setStatus(
        "current"
    )

ntxTrapSecondaryProtectionDomainsNotInSyncWithPrimary = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1861)
)
ntxTrapSecondaryProtectionDomainsNotInSyncWithPrimary.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapSecondaryProtectionDomainsNotInSyncWithPrimary.setStatus(
        "current"
    )

ntxTrapMetroConnectivityLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1862)
)
ntxTrapMetroConnectivityLost.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapMetroConnectivityLost.setStatus(
        "current"
    )

ntxTrapNodeRemovalStuck = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1863)
)
ntxTrapNodeRemovalStuck.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapNodeRemovalStuck.setStatus(
        "current"
    )

ntxTrapVGSyncRepContainerNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1864)
)
ntxTrapVGSyncRepContainerNotFound.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapVGSyncRepContainerNotFound.setStatus(
        "current"
    )

ntxTrapLatestSnapshotOfProtectionDomainIsMissingEntities = NotificationType(
    (1, 3, 6, 1, 4, 1, 41263, 1865)
)
ntxTrapLatestSnapshotOfProtectionDomainIsMissingEntities.setObjects(
      *(("NUTANIX-MIB", "ntxAlertCreationTime"),
        ("NUTANIX-MIB", "ntxAlertDisplayMsg"),
        ("NUTANIX-MIB", "ntxAlertTitle"),
        ("NUTANIX-MIB", "ntxAlertSeverity"),
        ("NUTANIX-MIB", "ntxAlertClusterName"),
        ("NUTANIX-MIB", "ntxAlertUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityUuid"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityName"),
        ("NUTANIX-MIB", "ntxAlertSourceEntityType"))
)
if mibBuilder.loadTexts:
    ntxTrapLatestSnapshotOfProtectionDomainIsMissingEntities.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NUTANIX-MIB",
    **{"nutanix": nutanix,
       "softwareVersionTable": softwareVersionTable,
       "svtEntry": svtEntry,
       "svtIndex": svtIndex,
       "svtControllerVMId": svtControllerVMId,
       "svtNutanixBootstrap": svtNutanixBootstrap,
       "svtNutanixInfrastructure": svtNutanixInfrastructure,
       "svtNutanixCore": svtNutanixCore,
       "svtNutanixToolchain": svtNutanixToolchain,
       "svtNutanixServiceability": svtNutanixServiceability,
       "svtLinuxKernel": svtLinuxKernel,
       "serviceStatusTable": serviceStatusTable,
       "sstEntry": sstEntry,
       "sstIndex": sstIndex,
       "sstControllerVMId": sstControllerVMId,
       "sstControllerVMStatus": sstControllerVMStatus,
       "sstZeusStatus": sstZeusStatus,
       "sstScavengerStatus": sstScavengerStatus,
       "sstMedusaStatus": sstMedusaStatus,
       "sstPithosStatus": sstPithosStatus,
       "sstStargateStatus": sstStargateStatus,
       "sstChronosStatus": sstChronosStatus,
       "sstCuratorStatus": sstCuratorStatus,
       "sstPrismStatus": sstPrismStatus,
       "sstAlertManagerStatus": sstAlertManagerStatus,
       "sstStatsAggregatorStatus": sstStatsAggregatorStatus,
       "sstSysStatCollectorStatus": sstSysStatCollectorStatus,
       "diskStatusTable": diskStatusTable,
       "dstEntry": dstEntry,
       "dstIndex": dstIndex,
       "dstDiskId": dstDiskId,
       "dstControllerVMId": dstControllerVMId,
       "dstSerial": dstSerial,
       "dstNumRawBytes": dstNumRawBytes,
       "dstNumTotalBytes": dstNumTotalBytes,
       "dstNumFreeBytes": dstNumFreeBytes,
       "dstNumTotalInodes": dstNumTotalInodes,
       "dstNumFreeInodes": dstNumFreeInodes,
       "dstAverageLatency": dstAverageLatency,
       "dstIOBandwidth": dstIOBandwidth,
       "dstNumberIops": dstNumberIops,
       "dstState": dstState,
       "controllerVMResourceTable": controllerVMResourceTable,
       "crtEntry": crtEntry,
       "crtIndex": crtIndex,
       "crtControllerVMId": crtControllerVMId,
       "crtMemory": crtMemory,
       "crtNumCpus": crtNumCpus,
       "crtName": crtName,
       "storagePoolInformationTable": storagePoolInformationTable,
       "spitEntry": spitEntry,
       "spitIndex": spitIndex,
       "spitStoragePoolId": spitStoragePoolId,
       "spitStoragePoolName": spitStoragePoolName,
       "spitTotalCapacity": spitTotalCapacity,
       "spitUsedCapacity": spitUsedCapacity,
       "spitIOPerSecond": spitIOPerSecond,
       "spitAvgLatencyUsecs": spitAvgLatencyUsecs,
       "spitIOBandwidth": spitIOBandwidth,
       "containerInformationTable": containerInformationTable,
       "citEntry": citEntry,
       "citIndex": citIndex,
       "citContainerId": citContainerId,
       "citContainerName": citContainerName,
       "citTotalCapacity": citTotalCapacity,
       "citUsedCapacity": citUsedCapacity,
       "citIOPerSecond": citIOPerSecond,
       "citAvgLatencyUsecs": citAvgLatencyUsecs,
       "citIOBandwidth": citIOBandwidth,
       "hypervisorInformationTable": hypervisorInformationTable,
       "hypervisorEntry": hypervisorEntry,
       "hypervisorIndex": hypervisorIndex,
       "hypervisorId": hypervisorId,
       "hypervisorName": hypervisorName,
       "hypervisorVmCount": hypervisorVmCount,
       "hypervisorCpuCount": hypervisorCpuCount,
       "hypervisorCpuUsagePercent": hypervisorCpuUsagePercent,
       "hypervisorMemory": hypervisorMemory,
       "hypervisorMemoryUsagePercent": hypervisorMemoryUsagePercent,
       "hypervisorReadIOPerSecond": hypervisorReadIOPerSecond,
       "hypervisorWriteIOPerSecond": hypervisorWriteIOPerSecond,
       "hypervisorAverageLatency": hypervisorAverageLatency,
       "hypervisorIOBandwidth": hypervisorIOBandwidth,
       "hypervisorRxBytes": hypervisorRxBytes,
       "hypervisorTxBytes": hypervisorTxBytes,
       "hypervisorRxDropCount": hypervisorRxDropCount,
       "hypervisorTxDropCount": hypervisorTxDropCount,
       "vmInformationTable": vmInformationTable,
       "vmEntry": vmEntry,
       "vmIndex": vmIndex,
       "vmId": vmId,
       "vmName": vmName,
       "vmHypervisorId": vmHypervisorId,
       "vmPowerState": vmPowerState,
       "vmCpuCount": vmCpuCount,
       "vmCpuUsagePercent": vmCpuUsagePercent,
       "vmMemory": vmMemory,
       "vmMemoryUsagePercent": vmMemoryUsagePercent,
       "vmReadIOPerSecond": vmReadIOPerSecond,
       "vmWriteIOPerSecond": vmWriteIOPerSecond,
       "vmAverageLatency": vmAverageLatency,
       "vmIOBandwidth": vmIOBandwidth,
       "vmRxBytes": vmRxBytes,
       "vmTxBytes": vmTxBytes,
       "vmRxDropCount": vmRxDropCount,
       "vmTxDropCount": vmTxDropCount,
       "controllerStatusTable": controllerStatusTable,
       "cstEntry": cstEntry,
       "cstIndex": cstIndex,
       "cstControllerVMId": cstControllerVMId,
       "cstControllerVMStatus": cstControllerVMStatus,
       "cstDataServiceStatus": cstDataServiceStatus,
       "cstMetadataServiceStatus": cstMetadataServiceStatus,
       "clusterName": clusterName,
       "clusterVersion": clusterVersion,
       "clusterStatus": clusterStatus,
       "clusterTotalStorageCapacity": clusterTotalStorageCapacity,
       "clusterUsedStorageCapacity": clusterUsedStorageCapacity,
       "clusterIops": clusterIops,
       "clusterLatency": clusterLatency,
       "clusterIOBandwidth": clusterIOBandwidth,
       "ntxTrap": ntxTrap,
       "ntxTrapName": ntxTrapName,
       "ntxTrapResolved": ntxTrapResolved,
       "ntxAlert": ntxAlert,
       "ntxAlertCreationTime": ntxAlertCreationTime,
       "ntxAlertDisplayMsg": ntxAlertDisplayMsg,
       "ntxAlertTitle": ntxAlertTitle,
       "ntxAlertSeverity": ntxAlertSeverity,
       "ntxAlertUuid": ntxAlertUuid,
       "ntxAlertResolvedTime": ntxAlertResolvedTime,
       "ntxAlertClusterName": ntxAlertClusterName,
       "ntxAlertSourceEntityUuid": ntxAlertSourceEntityUuid,
       "ntxAlertSourceEntityName": ntxAlertSourceEntityName,
       "ntxAlertSourceEntityType": ntxAlertSourceEntityType,
       "ntxTrapClusterRunningOutOfStorageCapacitylowRunway": ntxTrapClusterRunningOutOfStorageCapacitylowRunway,
       "ntxTrapClusterRunningOutOfCPUCapacitylowRunway": ntxTrapClusterRunningOutOfCPUCapacitylowRunway,
       "ntxTrapNodeRunningOutOfCPUCapacitylowRunway": ntxTrapNodeRunningOutOfCPUCapacitylowRunway,
       "ntxTrapClusterRunningOutOfMemoryCapacitylowRunway": ntxTrapClusterRunningOutOfMemoryCapacitylowRunway,
       "ntxTrapNodeRunningOutOfMemoryCapacitylowRunway": ntxTrapNodeRunningOutOfMemoryCapacitylowRunway,
       "ntxTrapStorageContainerRunningOutOfStorageCapacitylowRunway": ntxTrapStorageContainerRunningOutOfStorageCapacitylowRunway,
       "ntxTrapTestAlertTitle": ntxTrapTestAlertTitle,
       "ntxTrapMetadataDriveAutoAddDisabled": ntxTrapMetadataDriveAutoAddDisabled,
       "ntxTrapNodeDetachedFromMetadataRing": ntxTrapNodeDetachedFromMetadataRing,
       "ntxTrapMetadataDynamicRingChangeOperationStuck": ntxTrapMetadataDynamicRingChangeOperationStuck,
       "ntxTrapMetadataDynamicRingChangeOperationTooSlow": ntxTrapMetadataDynamicRingChangeOperationTooSlow,
       "ntxTrapMetadataDriveFailed": ntxTrapMetadataDriveFailed,
       "ntxTrapLargeMetadataSizeDetected": ntxTrapLargeMetadataSizeDetected,
       "ntxTrapMetadataDriveMarkedToBeAutoAdded": ntxTrapMetadataDriveMarkedToBeAutoAdded,
       "ntxTrapMetadataDriveDetached": ntxTrapMetadataDriveDetached,
       "ntxTrapMetadataRingImbalance": ntxTrapMetadataRingImbalance,
       "ntxTrapCassandraWaitingForDiskReplacement": ntxTrapCassandraWaitingForDiskReplacement,
       "ntxTrapCloudApplianceDeploymentFailed": ntxTrapCloudApplianceDeploymentFailed,
       "ntxTrapUnableToRemountDatastore": ntxTrapUnableToRemountDatastore,
       "ntxTrapRemountedDatastore": ntxTrapRemountedDatastore,
       "ntxTrapFailedToAllocateSnapshotReserveOnTheRemoteSite": ntxTrapFailedToAllocateSnapshotReserveOnTheRemoteSite,
       "ntxTrapFailedToAllocateSnapshotReserve": ntxTrapFailedToAllocateSnapshotReserve,
       "ntxTrapMetroTakeoverOldPrimarySiteIsHostingVMs": ntxTrapMetroTakeoverOldPrimarySiteIsHostingVMs,
       "ntxTrapProtectionDomainIsInDecoupledState": ntxTrapProtectionDomainIsInDecoupledState,
       "ntxTrapRemoteSiteLatencyIsHigh": ntxTrapRemoteSiteLatencyIsHigh,
       "ntxTrapFailedToUpdateMetroAvailabilityFailureHandling": ntxTrapFailedToUpdateMetroAvailabilityFailureHandling,
       "ntxTrapStretchConnectivityIsLost": ntxTrapStretchConnectivityIsLost,
       "ntxTrapVMRegistrationWarning": ntxTrapVMRegistrationWarning,
       "ntxTrapVMRenamedOnConversion": ntxTrapVMRenamedOnConversion,
       "ntxTrapAuthenticationFailedInWitness": ntxTrapAuthenticationFailedInWitness,
       "ntxTrapWitnessIsNotConfigured": ntxTrapWitnessIsNotConfigured,
       "ntxTrapWitnessIsNotReachable": ntxTrapWitnessIsNotReachable,
       "ntxTrapCuratorJobRunningTooLong": ntxTrapCuratorJobRunningTooLong,
       "ntxTrapCuratorScanFailure": ntxTrapCuratorScanFailure,
       "ntxTrapFileServerSpaceUsageHigh": ntxTrapFileServerSpaceUsageHigh,
       "ntxTrapFileServerSpaceUsageCritical": ntxTrapFileServerSpaceUsageCritical,
       "ntxTrapFileServerUnreachable": ntxTrapFileServerUnreachable,
       "ntxTrapFileServerStorageIsNotAvailable": ntxTrapFileServerStorageIsNotAvailable,
       "ntxTrapFileServerScaleoutFailed": ntxTrapFileServerScaleoutFailed,
       "ntxTrapFileServerCouldNotJoinTheADDomain": ntxTrapFileServerCouldNotJoinTheADDomain,
       "ntxTrapNodeFailedToJoinDomain": ntxTrapNodeFailedToJoinDomain,
       "ntxTrapFileServerTimeDifferenceHigh": ntxTrapFileServerTimeDifferenceHigh,
       "ntxTrapFileServerStorageCleanupFailed": ntxTrapFileServerStorageCleanupFailed,
       "ntxTrapFileServerCannotConnectWithADServer": ntxTrapFileServerCannotConnectWithADServer,
       "ntxTrapFileServerPerformanceOptimizationRecommended": ntxTrapFileServerPerformanceOptimizationRecommended,
       "ntxTrapAppropriateSiteNotFoundInActiveDirectory": ntxTrapAppropriateSiteNotFoundInActiveDirectory,
       "ntxTrapFileServerDNSUpdatesPending": ntxTrapFileServerDNSUpdatesPending,
       "ntxTrapUserQuotaAssignmentFailed": ntxTrapUserQuotaAssignmentFailed,
       "ntxTrapShareUtilizationReachedConfiguredLimit": ntxTrapShareUtilizationReachedConfiguredLimit,
       "ntxTrapFileServerFailedToGetUpdatedCVMIPAddress": ntxTrapFileServerFailedToGetUpdatedCVMIPAddress,
       "ntxTrapFileServerActivationFailed": ntxTrapFileServerActivationFailed,
       "ntxTrapFailedToSetVMtoVMAntiaffinityRule": ntxTrapFailedToSetVMtoVMAntiaffinityRule,
       "ntxTrapFileServerHomeShareCreationFailed": ntxTrapFileServerHomeShareCreationFailed,
       "ntxTrapDiscoveryOfISCSITargetsFailed": ntxTrapDiscoveryOfISCSITargetsFailed,
       "ntxTrapFileServerUpgradeFailed": ntxTrapFileServerUpgradeFailed,
       "ntxTrapIncompatibleFileServerActivated": ntxTrapIncompatibleFileServerActivated,
       "ntxTrapFileServerInHeterogeneousState": ntxTrapFileServerInHeterogeneousState,
       "ntxTrapFailedToCorrectFileServerDataAndMetaDataInconsistencies": ntxTrapFailedToCorrectFileServerDataAndMetaDataInconsistencies,
       "ntxTrapFileServerShareDeletionFailed": ntxTrapFileServerShareDeletionFailed,
       "ntxTrapFileServerCompatibilityCheckSkipped": ntxTrapFileServerCompatibilityCheckSkipped,
       "ntxTrapSnapshotInvalidForClone": ntxTrapSnapshotInvalidForClone,
       "ntxTrapFileServerAntiVirusICAPServerDown": ntxTrapFileServerAntiVirusICAPServerDown,
       "ntxTrapFileServerAntiVirusAllICAPServersDown": ntxTrapFileServerAntiVirusAllICAPServersDown,
       "ntxTrapClusterInReadOnlyMode": ntxTrapClusterInReadOnlyMode,
       "ntxTrapStorageContainerSpaceUsageExceededAOSCheck": ntxTrapStorageContainerSpaceUsageExceededAOSCheck,
       "ntxTrapDiskDiagnosticFailure": ntxTrapDiskDiagnosticFailure,
       "ntxTrapNodeFailure": ntxTrapNodeFailure,
       "ntxTrapNodeInMaintenanceMode": ntxTrapNodeInMaintenanceMode,
       "ntxTrapNonSelfEncryptionDriveDiskInserted": ntxTrapNonSelfEncryptionDriveDiskInserted,
       "ntxTrapPhysicalDiskAddedToSlot": ntxTrapPhysicalDiskAddedToSlot,
       "ntxTrapPhysicalDiskDriveHasFailed": ntxTrapPhysicalDiskDriveHasFailed,
       "ntxTrapPhysicalDiskRemovedFromSlot": ntxTrapPhysicalDiskRemovedFromSlot,
       "ntxTrapSelfEncryptingDriveOperationFailure": ntxTrapSelfEncryptingDriveOperationFailure,
       "ntxTrapUnsupportedConfigurationForRedundancyFactor3": ntxTrapUnsupportedConfigurationForRedundancyFactor3,
       "ntxTrapCannotRemovePasswordProtectedDisks": ntxTrapCannotRemovePasswordProtectedDisks,
       "ntxTrapDiskBad": ntxTrapDiskBad,
       "ntxTrapDuplicateIPAddressDetected": ntxTrapDuplicateIPAddressDetected,
       "ntxTrapIPAddressNotHosted": ntxTrapIPAddressNotHosted,
       "ntxTrapSMTPError": ntxTrapSMTPError,
       "ntxTrapProtectionDomainReplicationFailure": ntxTrapProtectionDomainReplicationFailure,
       "ntxTrapProtectionDomainSnapshotFailure": ntxTrapProtectionDomainSnapshotFailure,
       "ntxTrapNutanixGuestToolsAgentIsNotReachableOnTheVM": ntxTrapNutanixGuestToolsAgentIsNotReachableOnTheVM,
       "ntxTrapMetroAvailabilityIsPromoted": ntxTrapMetroAvailabilityIsPromoted,
       "ntxTrapEntityRestoreAborted": ntxTrapEntityRestoreAborted,
       "ntxTrapProtectionDomainReceiveSnapshotFailure": ntxTrapProtectionDomainReceiveSnapshotFailure,
       "ntxTrapSecureTunnelToRemoteSiteDown": ntxTrapSecureTunnelToRemoteSiteDown,
       "ntxTrapProtectedVolumeGroupNotFound": ntxTrapProtectedVolumeGroupNotFound,
       "ntxTrapProtectionDomainActivation": ntxTrapProtectionDomainActivation,
       "ntxTrapDuplicateRemoteClusterID": ntxTrapDuplicateRemoteClusterID,
       "ntxTrapCloudRemoteSiteFailedToStart": ntxTrapCloudRemoteSiteFailedToStart,
       "ntxTrapRemoteSiteremotenameNetworkMappingMissing": ntxTrapRemoteSiteremotenameNetworkMappingMissing,
       "ntxTrapOperationForwardedToCloudRemoteFailed": ntxTrapOperationForwardedToCloudRemoteFailed,
       "ntxTrapRecoveryPointObjectiveCannotBeMet": ntxTrapRecoveryPointObjectiveCannotBeMet,
       "ntxTrapVStoreSnapshotStatus": ntxTrapVStoreSnapshotStatus,
       "ntxTrapProtectionDomainSnapshotOperationSkipped": ntxTrapProtectionDomainSnapshotOperationSkipped,
       "ntxTrapSkippedReplicationOfTheSnapshot": ntxTrapSkippedReplicationOfTheSnapshot,
       "ntxTrapFailedToSnapshotEntities": ntxTrapFailedToSnapshotEntities,
       "ntxTrapIncorrectClusterInformationInRemoteSite": ntxTrapIncorrectClusterInformationInRemoteSite,
       "ntxTrapVStoreIsBeingReplicatedToBackupOnlyRemoteSite": ntxTrapVStoreIsBeingReplicatedToBackupOnlyRemoteSite,
       "ntxTrapFailedToChangeStateOfOneOrMoreVMs": ntxTrapFailedToChangeStateOfOneOrMoreVMs,
       "ntxTrapRegistrationOfOneOrMoreVMsFailed": ntxTrapRegistrationOfOneOrMoreVMsFailed,
       "ntxTrapSelfServiceRestoreOperationFailed": ntxTrapSelfServiceRestoreOperationFailed,
       "ntxTrapMetadataVolumeSnapshotPersistentFailure": ntxTrapMetadataVolumeSnapshotPersistentFailure,
       "ntxTrapMetroAvailabilityIsDisabled": ntxTrapMetroAvailabilityIsDisabled,
       "ntxTrapApplicationconsistentSnapshotNotTakenForTheVM": ntxTrapApplicationconsistentSnapshotNotTakenForTheVM,
       "ntxTrapInvalidConsistencyGroup": ntxTrapInvalidConsistencyGroup,
       "ntxTrapFailedToReconfigureNutanixGuestToolsForTheRecoveredVM": ntxTrapFailedToReconfigureNutanixGuestToolsForTheRecoveredVM,
       "ntxTrapNutanixGuestToolsNotInstalled": ntxTrapNutanixGuestToolsNotInstalled,
       "ntxTrapRemoteSiteremotenameNetworkMappingInvalid": ntxTrapRemoteSiteremotenameNetworkMappingInvalid,
       "ntxTrapVSSSnapshotFailed": ntxTrapVSSSnapshotFailed,
       "ntxTrapAlertRaisedOnCloudRemoteSiteremotenamealertmessage": ntxTrapAlertRaisedOnCloudRemoteSiteremotenamealertmessage,
       "ntxTrapProtectedVmsNotFound": ntxTrapProtectedVmsNotFound,
       "ntxTrapProtectionDomainContainsMoreThanSpecifiedVMs": ntxTrapProtectionDomainContainsMoreThanSpecifiedVMs,
       "ntxTrapRelatedEntityProtectionStatus": ntxTrapRelatedEntityProtectionStatus,
       "ntxTrapNutanixGuestToolsIsNotSupportedOnRemoteSite": ntxTrapNutanixGuestToolsIsNotSupportedOnRemoteSite,
       "ntxTrapRemoteSiteOperationModeReadOnly": ntxTrapRemoteSiteOperationModeReadOnly,
       "ntxTrapRemoteSiteIsUnhealthy": ntxTrapRemoteSiteIsUnhealthy,
       "ntxTrapEntitiesRestoredButUnprotected": ntxTrapEntitiesRestoredButUnprotected,
       "ntxTrapProtectionDomainFullReplicationPerformed": ntxTrapProtectionDomainFullReplicationPerformed,
       "ntxTrapProtectedVMIsNotNutanixBackupAndRecoveryCompliant": ntxTrapProtectedVMIsNotNutanixBackupAndRecoveryCompliant,
       "ntxTrapProtectedVMRenamedDuringClone": ntxTrapProtectedVMRenamedDuringClone,
       "ntxTrapProtectedVolumeGroupsNotFound": ntxTrapProtectedVolumeGroupsNotFound,
       "ntxTrapVMRegistrationFailed": ntxTrapVMRegistrationFailed,
       "ntxTrapProtectionDomainReplicationExpired": ntxTrapProtectionDomainReplicationExpired,
       "ntxTrapVolumeGroupAttachmentsNotRestored": ntxTrapVolumeGroupAttachmentsNotRestored,
       "ntxTrapEntitiesSkippedDuringRestore": ntxTrapEntitiesSkippedDuringRestore,
       "ntxTrapProtectionDomainChangeModeFailure": ntxTrapProtectionDomainChangeModeFailure,
       "ntxTrapVSSSnapshotAborted": ntxTrapVSSSnapshotAborted,
       "ntxTrapExternalISCSIAttachmentsNotSnapshotted": ntxTrapExternalISCSIAttachmentsNotSnapshotted,
       "ntxTrapVMVirtualHardwareVersionNotCompatible": ntxTrapVMVirtualHardwareVersionNotCompatible,
       "ntxTrapVolumeGroupActionError": ntxTrapVolumeGroupActionError,
       "ntxTrapMetadataVolumeSnapshotTimeout": ntxTrapMetadataVolumeSnapshotTimeout,
       "ntxTrapSnapshotPartiallyCrashConsistent": ntxTrapSnapshotPartiallyCrashConsistent,
       "ntxTrapMetroAvailabilityPrechecksFailed": ntxTrapMetroAvailabilityPrechecksFailed,
       "ntxTrapProtectionDomainMightHaveSymlinks": ntxTrapProtectionDomainMightHaveSymlinks,
       "ntxTrapVSSSnapshotIsNotSupportedForTheVM": ntxTrapVSSSnapshotIsNotSupportedForTheVM,
       "ntxTrapSnapshotReserveOnSSDIsFull": ntxTrapSnapshotReserveOnSSDIsFull,
       "ntxTrapMetroAvailabilityConfigurationFailed": ntxTrapMetroAvailabilityConfigurationFailed,
       "ntxTrapStaleNFSMount": ntxTrapStaleNFSMount,
       "ntxTrapVSSSoftwareOrprefreezepostthawScriptsNotInstalled": ntxTrapVSSSoftwareOrprefreezepostthawScriptsNotInstalled,
       "ntxTrapProtectedVMNotFound": ntxTrapProtectedVMNotFound,
       "ntxTrapProtectionDomainTransitioningToLowerFrequencySnapshotting": ntxTrapProtectionDomainTransitioningToLowerFrequencySnapshotting,
       "ntxTrapSnapshotQueuedForReplicationsToRemoteSite": ntxTrapSnapshotQueuedForReplicationsToRemoteSite,
       "ntxTrapAgentVMRestorationFailure": ntxTrapAgentVMRestorationFailure,
       "ntxTrapCPSDeploymentEvaluationMode": ntxTrapCPSDeploymentEvaluationMode,
       "ntxTrapHAHostEvacuationFailure": ntxTrapHAHostEvacuationFailure,
       "ntxTrapFailureToRestartVMsForHAEvent": ntxTrapFailureToRestartVMsForHAEvent,
       "ntxTrapUpgradeBundleAvailable": ntxTrapUpgradeBundleAvailable,
       "ntxTrapVMActionError": ntxTrapVMActionError,
       "ntxTrapHAHealingFailure": ntxTrapHAHealingFailure,
       "ntxTrapVmHighAvailabilityFailure": ntxTrapVmHighAvailabilityFailure,
       "ntxTrapKerberosClockSkewFailure": ntxTrapKerberosClockSkewFailure,
       "ntxTrapStargateTemporarilyDown": ntxTrapStargateTemporarilyDown,
       "ntxTrapVMGroupSnapshotAndCurrentMismatch": ntxTrapVMGroupSnapshotAndCurrentMismatch,
       "ntxTrapCertificateCreationError": ntxTrapCertificateCreationError,
       "ntxTrapFingerprintingDisabled": ntxTrapFingerprintingDisabled,
       "ntxTrapSystemDefinedFlashModeUsageLimitExceeded": ntxTrapSystemDefinedFlashModeUsageLimitExceeded,
       "ntxTrapMetadataUsageHigh": ntxTrapMetadataUsageHigh,
       "ntxTrapNFSMetadataSizeOvershoot": ntxTrapNFSMetadataSizeOvershoot,
       "ntxTrapOnDiskDedupDisabled": ntxTrapOnDiskDedupDisabled,
       "ntxTrapSpaceReservationViolated": ntxTrapSpaceReservationViolated,
       "ntxTrapPossibleDegradedNode": ntxTrapPossibleDegradedNode,
       "ntxTrapDynamicSchedulingFailure": ntxTrapDynamicSchedulingFailure,
       "ntxTrapRecoveredVMDiskConfigurationUpdateFailed": ntxTrapRecoveredVMDiskConfigurationUpdateFailed,
       "ntxTrapISCSIConfigurationFailed": ntxTrapISCSIConfigurationFailed,
       "ntxTrapA130104": ntxTrapA130104,
       "ntxTrapExecutionOfThePostThawScriptFailed": ntxTrapExecutionOfThePostThawScriptFailed,
       "ntxTrapNutanixGuestToolsMountFailed": ntxTrapNutanixGuestToolsMountFailed,
       "ntxTrapVMForciblyPoweredOff": ntxTrapVMForciblyPoweredOff,
       "ntxTrapReportGenerationFailure": ntxTrapReportGenerationFailure,
       "ntxTrapSendReportThroughEmailFailure": ntxTrapSendReportThroughEmailFailure,
       "ntxTrapReportQuotaScanFailure": ntxTrapReportQuotaScanFailure,
       "ntxTrapCassandraServiceCrashed": ntxTrapCassandraServiceCrashed,
       "ntxTrapCassandraServiceIsRunningOutOfMemory": ntxTrapCassandraServiceIsRunningOutOfMemory,
       "ntxTrapMultipleCassandraNodesHaveSimilarTokens": ntxTrapMultipleCassandraNodesHaveSimilarTokens,
       "ntxTrapCloudClusterDoesNotHaveRecommendedConfigurationLocally": ntxTrapCloudClusterDoesNotHaveRecommendedConfigurationLocally,
       "ntxTrapAWSCloudInstanceNotConfiguredProperly": ntxTrapAWSCloudInstanceNotConfiguredProperly,
       "ntxTrapOldGenerationAWSInstanceConfigured": ntxTrapOldGenerationAWSInstanceConfigured,
       "ntxTrapAOSVersionOfCloudRemoteSiteIsLessThanSourceCluster": ntxTrapAOSVersionOfCloudRemoteSiteIsLessThanSourceCluster,
       "ntxTrapCloudClusterDoesNotHaveAllRecommendedGflagsSet": ntxTrapCloudClusterDoesNotHaveAllRecommendedGflagsSet,
       "ntxTrapEgroupCountOnCloudDiskIsHigherThanTheRecommendedThreshold": ntxTrapEgroupCountOnCloudDiskIsHigherThanTheRecommendedThreshold,
       "ntxTrapFileServerMutipleVMsOnSingleNodeCheck": ntxTrapFileServerMutipleVMsOnSingleNodeCheck,
       "ntxTrapFileServerServicesDownCheck": ntxTrapFileServerServicesDownCheck,
       "ntxTrapFileServerUnreachableCheck": ntxTrapFileServerUnreachableCheck,
       "ntxTrapFileServerDownCheck": ntxTrapFileServerDownCheck,
       "ntxTrapFileServerInvalidSnapshot": ntxTrapFileServerInvalidSnapshot,
       "ntxTrapFileServerEntitiesNotProtected": ntxTrapFileServerEntitiesNotProtected,
       "ntxTrapMultipleFileServerVersionsArePresentInTheCluster": ntxTrapMultipleFileServerVersionsArePresentInTheCluster,
       "ntxTrapFileServerUpgradeTaskHungForTooLong": ntxTrapFileServerUpgradeTaskHungForTooLong,
       "ntxTrapFileServerPDActivatesOnMultipleSites": ntxTrapFileServerPDActivatesOnMultipleSites,
       "ntxTrapFileServerPDEnabledOnNoncompatibleRemoteSite": ntxTrapFileServerPDEnabledOnNoncompatibleRemoteSite,
       "ntxTrapHardwareClockFailure": ntxTrapHardwareClockFailure,
       "ntxTrapWsmanConnectivityLost": ntxTrapWsmanConnectivityLost,
       "ntxTrapVMMigrationCompromised": ntxTrapVMMigrationCompromised,
       "ntxTrapCVMMemoryReservationIsIncorrectlyConfigured": ntxTrapCVMMemoryReservationIsIncorrectlyConfigured,
       "ntxTrapHostMissingCriticalWindowsUpdates": ntxTrapHostMissingCriticalWindowsUpdates,
       "ntxTrapHostdServiceNotRunning": ntxTrapHostdServiceNotRunning,
       "ntxTrapIncorrectKerberosSetup": ntxTrapIncorrectKerberosSetup,
       "ntxTrapUnableToConnectToVCenter": ntxTrapUnableToConnectToVCenter,
       "ntxTrapVMHasNonASCIIName": ntxTrapVMHasNonASCIIName,
       "ntxTrapFanSpeedLow": ntxTrapFanSpeedLow,
       "ntxTrapFanSpeedHigh": ntxTrapFanSpeedHigh,
       "ntxTrapRAMFault": ntxTrapRAMFault,
       "ntxTrapPowerSupplyDown": ntxTrapPowerSupplyDown,
       "ntxTrapCPUTemperatureHigh": ntxTrapCPUTemperatureHigh,
       "ntxTrapCPUTemperatureReadingError": ntxTrapCPUTemperatureReadingError,
       "ntxTrapCPUVoltageAbnormal": ntxTrapCPUVoltageAbnormal,
       "ntxTrapCPUVRMTemperatureHigh": ntxTrapCPUVRMTemperatureHigh,
       "ntxTrapRAMTemperatureHigh": ntxTrapRAMTemperatureHigh,
       "ntxTrapRAMVoltageAbnormal": ntxTrapRAMVoltageAbnormal,
       "ntxTrapRAMVRMTemperatureHigh": ntxTrapRAMVRMTemperatureHigh,
       "ntxTrapSystemTemperatureHigh": ntxTrapSystemTemperatureHigh,
       "ntxTrapGPUTemperatureHigh": ntxTrapGPUTemperatureHigh,
       "ntxTrapIPMIError": ntxTrapIPMIError,
       "ntxTrapGPUFault": ntxTrapGPUFault,
       "ntxTrapHighNumberOfCorrectableECCErrorsInLast1Day": ntxTrapHighNumberOfCorrectableECCErrorsInLast1Day,
       "ntxTrapHighNumberOfCorrectableECCErrorsInLast10Days": ntxTrapHighNumberOfCorrectableECCErrorsInLast10Days,
       "ntxTrapLicenseExpiry": ntxTrapLicenseExpiry,
       "ntxTrapLicenseFeatureViolation": ntxTrapLicenseFeatureViolation,
       "ntxTrapLicenseStandbyMode": ntxTrapLicenseStandbyMode,
       "ntxTrapLicenseNodeInvalid": ntxTrapLicenseNodeInvalid,
       "ntxTrapSecondaryPDsNotInSync": ntxTrapSecondaryPDsNotInSync,
       "ntxTrapNoCheckpointSnapshotsOnMetroPDInLastHour": ntxTrapNoCheckpointSnapshotsOnMetroPDInLastHour,
       "ntxTrapCVMTimeDifferenceHigh": ntxTrapCVMTimeDifferenceHigh,
       "ntxTrapIPMIIPNotReachable": ntxTrapIPMIIPNotReachable,
       "ntxTrapHostIPNotReachable": ntxTrapHostIPNotReachable,
       "ntxTrapCVMNICSpeedLow": ntxTrapCVMNICSpeedLow,
       "ntxTrapCVMNotUplinkedToActive10GbpsLink": ntxTrapCVMNotUplinkedToActive10GbpsLink,
       "ntxTrapNICErrorRateHigh": ntxTrapNICErrorRateHigh,
       "ntxTrapCVMHostSubnetMismatch": ntxTrapCVMHostSubnetMismatch,
       "ntxTrapNICLinkDown": ntxTrapNICLinkDown,
       "ntxTrapCVMIPAddressMismatch": ntxTrapCVMIPAddressMismatch,
       "ntxTrapZeusConfigMismatch": ntxTrapZeusConfigMismatch,
       "ntxTrapIPMIIPAddressMismatch": ntxTrapIPMIIPAddressMismatch,
       "ntxTrapJumboFramesEnabled": ntxTrapJumboFramesEnabled,
       "ntxTrapNICFlaps": ntxTrapNICFlaps,
       "ntxTrapIncorrectNTPConfiguration": ntxTrapIncorrectNTPConfiguration,
       "ntxTrapCVMIsUnreachable": ntxTrapCVMIsUnreachable,
       "ntxTrapNGTInstallationRequired": ntxTrapNGTInstallationRequired,
       "ntxTrapTooManyFilesInTheProtectionDomain": ntxTrapTooManyFilesInTheProtectionDomain,
       "ntxTrapTooManyFilesInTheConsistencyGroup": ntxTrapTooManyFilesInTheConsistencyGroup,
       "ntxTrapFoundOldClonesOnCluster": ntxTrapFoundOldClonesOnCluster,
       "ntxTrapTooManyClonesOnCluster": ntxTrapTooManyClonesOnCluster,
       "ntxTrapProtectingVMsThatAreUsingSharedVHDXDisksIsUnsupported": ntxTrapProtectingVMsThatAreUsingSharedVHDXDisksIsUnsupported,
       "ntxTrapSymlinksFoundOnMetrovstoreProtectedContainer": ntxTrapSymlinksFoundOnMetrovstoreProtectedContainer,
       "ntxTrapAgedThirdpartyBackupSnapshotsPresent": ntxTrapAgedThirdpartyBackupSnapshotsPresent,
       "ntxTrapProtectionDomainContainsMoreThanOneEntity": ntxTrapProtectionDomainContainsMoreThanOneEntity,
       "ntxTrapRemoteSiteConnectivityNotNormal": ntxTrapRemoteSiteConnectivityNotNormal,
       "ntxTrapCPUAverageLoadHighOnControllerVM": ntxTrapCPUAverageLoadHighOnControllerVM,
       "ntxTrapCPUAverageLoadCriticallyHighOnControllerVM": ntxTrapCPUAverageLoadCriticallyHighOnControllerVM,
       "ntxTrapControllerVMCertificateExpiring": ntxTrapControllerVMCertificateExpiring,
       "ntxTrapClusterCertificateExpiring": ntxTrapClusterCertificateExpiring,
       "ntxTrapRemoteSiteInsecure": ntxTrapRemoteSiteInsecure,
       "ntxTrapMixedSelfEncryptingDriveHardware": ntxTrapMixedSelfEncryptingDriveHardware,
       "ntxTrapKeyManagementServerUnavailable": ntxTrapKeyManagementServerUnavailable,
       "ntxTrapNumberOfOrphanedEgroupsIsOverTheRecommendedThreshold": ntxTrapNumberOfOrphanedEgroupsIsOverTheRecommendedThreshold,
       "ntxTrapCVMRAMUsageHigh": ntxTrapCVMRAMUsageHigh,
       "ntxTrapClusterServicesAreDown": ntxTrapClusterServicesAreDown,
       "ntxTrapKernelMemoryUsageHigh": ntxTrapKernelMemoryUsageHigh,
       "ntxTrapCVMServicesRestartingFrequently": ntxTrapCVMServicesRestartingFrequently,
       "ntxTrapClusterServiceRestartingFrequently": ntxTrapClusterServiceRestartingFrequently,
       "ntxTrapCVMConnectivityFailure": ntxTrapCVMConnectivityFailure,
       "ntxTrapStorageContainerReplicationFactorLow": ntxTrapStorageContainerReplicationFactorLow,
       "ntxTrapCVMRebooted": ntxTrapCVMRebooted,
       "ntxTrapRemoteSupportEnabled": ntxTrapRemoteSupportEnabled,
       "ntxTrapDatastoreVMCountHigh": ntxTrapDatastoreVMCountHigh,
       "ntxTrapHighVDiskCountInTheCluster": ntxTrapHighVDiskCountInTheCluster,
       "ntxTrapAllFlashNodesMixedWithNonallflashNodes": ntxTrapAllFlashNodesMixedWithNonallflashNodes,
       "ntxTrapHaswellAndBroadwellCPUsAreInTheSameChassis": ntxTrapHaswellAndBroadwellCPUsAreInTheSameChassis,
       "ntxTrapTimeSinceLastCuratorScanIsBeyondThreshold": ntxTrapTimeSinceLastCuratorScanIsBeyondThreshold,
       "ntxTrapSnapshotChainHeightExceedsThreshold": ntxTrapSnapshotChainHeightExceedsThreshold,
       "ntxTrapDIMMsOfDifferentTypesInOneMemoryChannel": ntxTrapDIMMsOfDifferentTypesInOneMemoryChannel,
       "ntxTrapZookeeperNotActiveOnAllCVMs": ntxTrapZookeeperNotActiveOnAllCVMs,
       "ntxTrapM60GPUConfigurationWrongOnTheNode": ntxTrapM60GPUConfigurationWrongOnTheNode,
       "ntxTrapM10GPUConfigurationWrongOnTheNode": ntxTrapM10GPUConfigurationWrongOnTheNode,
       "ntxTrapM10AndM60GPUsInstalledOnTheSameNode": ntxTrapM10AndM60GPUsInstalledOnTheSameNode,
       "ntxTrapPCVCPUAvailabilityCheck": ntxTrapPCVCPUAvailabilityCheck,
       "ntxTrapPCSufficientDiskSpaceCheck": ntxTrapPCSufficientDiskSpaceCheck,
       "ntxTrapPCMemoryAvailabilityCheck": ntxTrapPCMemoryAvailabilityCheck,
       "ntxTrapPCVMLimitCheck": ntxTrapPCVMLimitCheck,
       "ntxTrapStoragePoolSpaceUsageExceeded": ntxTrapStoragePoolSpaceUsageExceeded,
       "ntxTrapDiskInodeUsageHigh": ntxTrapDiskInodeUsageHigh,
       "ntxTrapDiskUnused": ntxTrapDiskUnused,
       "ntxTrapFusionIOWearHigh": ntxTrapFusionIOWearHigh,
       "ntxTrapFusionIOTemperatureHigh": ntxTrapFusionIOTemperatureHigh,
       "ntxTrapFusionIOReserveLow": ntxTrapFusionIOReserveLow,
       "ntxTrapFusionIODiskFailed": ntxTrapFusionIODiskFailed,
       "ntxTrapStorageContainerSpaceUsageExceededNCCCheck": ntxTrapStorageContainerSpaceUsageExceededNCCCheck,
       "ntxTrapDataDiskSpaceUsageHigh": ntxTrapDataDiskSpaceUsageHigh,
       "ntxTrapSystemPartitionsSpaceUsageHigh": ntxTrapSystemPartitionsSpaceUsageHigh,
       "ntxTrapStorageDeviceHealthBad": ntxTrapStorageDeviceHealthBad,
       "ntxTrapIntelSSDWearHigh": ntxTrapIntelSSDWearHigh,
       "ntxTrapIntelSSDTemperatureHigh": ntxTrapIntelSSDTemperatureHigh,
       "ntxTrapCVMBootRaidDegraded": ntxTrapCVMBootRaidDegraded,
       "ntxTrapAbnormalHostBootRAIDState": ntxTrapAbnormalHostBootRAIDState,
       "ntxTrapHypervisorDiskSpaceUsageHigh": ntxTrapHypervisorDiskSpaceUsageHigh,
       "ntxTrapInvalidDriveConfiguration": ntxTrapInvalidDriveConfiguration,
       "ntxTrapSATADOMHasFailed": ntxTrapSATADOMHasFailed,
       "ntxTrapSATADOMNotReachable": ntxTrapSATADOMNotReachable,
       "ntxTrapSATADOMHasWornOut": ntxTrapSATADOMHasWornOut,
       "ntxTrapSATADOMSL3IE3HasHighWear": ntxTrapSATADOMSL3IE3HasHighWear,
       "ntxTrapSATADOMNeedsFirmwareVersionUpgradeToS170119": ntxTrapSATADOMNeedsFirmwareVersionUpgradeToS170119,
       "ntxTrapmodelFirmwareVersionIsNotTheLatestFirmwareVersion": ntxTrapmodelFirmwareVersionIsNotTheLatestFirmwareVersion,
       "ntxTrapSATADOMHasGuestVM": ntxTrapSATADOMHasGuestVM,
       "ntxTrapSASConnectivityNotNormal": ntxTrapSASConnectivityNotNormal,
       "ntxTrapSamsungPM1633DriveHasWornOut": ntxTrapSamsungPM1633DriveHasWornOut,
       "ntxTrapToshibaPM3DriveHasWornOut": ntxTrapToshibaPM3DriveHasWornOut,
       "ntxTrapToshibaPM4DriveHasWornOut": ntxTrapToshibaPM4DriveHasWornOut,
       "ntxTrapSM863DriveHasWornOut": ntxTrapSM863DriveHasWornOut,
       "ntxTrapMicron5100DriveHasWornOut": ntxTrapMicron5100DriveHasWornOut,
       "ntxTrapIntelSSDS3610OnipaddressHasConfigurationProblems": ntxTrapIntelSSDS3610OnipaddressHasConfigurationProblems,
       "ntxTrapOfflineDiskInACluster": ntxTrapOfflineDiskInACluster,
       "ntxTrapNVMeDriveHasErrors": ntxTrapNVMeDriveHasErrors,
       "ntxTrapHypervisorBootDriveWearHigh": ntxTrapHypervisorBootDriveWearHigh,
       "ntxTrapVMIsProtectedInMultiplePDs": ntxTrapVMIsProtectedInMultiplePDs,
       "ntxTrapProtectedVMsNotOnNutanixStorage": ntxTrapProtectedVMsNotOnNutanixStorage,
       "ntxTrapClusterConnectivityStatus": ntxTrapClusterConnectivityStatus,
       "ntxTrapHighGarbageDueToErasureCoding": ntxTrapHighGarbageDueToErasureCoding,
       "ntxTrapA1175": ntxTrapA1175,
       "ntxTrapInvalidErasureCodeDelayParameter": ntxTrapInvalidErasureCodeDelayParameter,
       "ntxTrapFlashModeUsageLimitExceeded": ntxTrapFlashModeUsageLimitExceeded,
       "ntxTrapFlashmodeenabledVMPowerStatus": ntxTrapFlashmodeenabledVMPowerStatus,
       "ntxTrapStoragePoolFlashModeConfiguration": ntxTrapStoragePoolFlashModeConfiguration,
       "ntxTrapTestNotificationTitle": ntxTrapTestNotificationTitle,
       "ntxTrapIncompatibleFileServer": ntxTrapIncompatibleFileServer,
       "ntxTrapA1202": ntxTrapA1202,
       "ntxTrapFirmwareVersionOfSamsungPM1633DrivesIsOld": ntxTrapFirmwareVersionOfSamsungPM1633DrivesIsOld,
       "ntxTrapMoreThanOneTypeOfToshibaPM4DrivesInstalledOnTheNode": ntxTrapMoreThanOneTypeOfToshibaPM4DrivesInstalledOnTheNode,
       "ntxTrapA1200": ntxTrapA1200,
       "ntxTrapFirmwareVersionOfToshibaPM4DrivesIsOld": ntxTrapFirmwareVersionOfToshibaPM4DrivesIsOld,
       "ntxTrapFirmwareVersionOfSM863DrivesIsOld": ntxTrapFirmwareVersionOfSM863DrivesIsOld,
       "ntxTrapFewerThanTwoNonSamsungPM863aDrivesInstalledOnTheNode": ntxTrapFewerThanTwoNonSamsungPM863aDrivesInstalledOnTheNode,
       "ntxTrapFirmwareVersionOfPM863aDrivesIsOld": ntxTrapFirmwareVersionOfPM863aDrivesIsOld,
       "ntxTrapPM863aDriveHasWornOut": ntxTrapPM863aDriveHasWornOut,
       "ntxTrapOfflineDiskInCluster": ntxTrapOfflineDiskInCluster,
       "ntxTrapMetadataDisksNotMountedOnCVM": ntxTrapMetadataDisksNotMountedOnCVM,
       "ntxTrapFileServerUpgradeTaskIsNotProgressing": ntxTrapFileServerUpgradeTaskIsNotProgressing,
       "ntxTrapA130129": ntxTrapA130129,
       "ntxTrapA130118": ntxTrapA130118,
       "ntxTrapFileServerCloneFailed": ntxTrapFileServerCloneFailed,
       "ntxTrapFileServerRenameFailed": ntxTrapFileServerRenameFailed,
       "ntxTrapA130097": ntxTrapA130097,
       "ntxTrapA130095": ntxTrapA130095,
       "ntxTrapA130131": ntxTrapA130131,
       "ntxTrapA130137": ntxTrapA130137,
       "ntxTrapA106030": ntxTrapA106030,
       "ntxTrapA106033": ntxTrapA106033,
       "ntxTrapA111047": ntxTrapA111047,
       "ntxTrapA110219": ntxTrapA110219,
       "ntxTrapA110251": ntxTrapA110251,
       "ntxTrapA111044": ntxTrapA111044,
       "ntxTrapMaximumConnectionsLimitReachedOnAFileServerVM": ntxTrapMaximumConnectionsLimitReachedOnAFileServerVM,
       "ntxTrapFailedToAddOneOrMoreFileServerAdministratorUsersOrGroups": ntxTrapFailedToAddOneOrMoreFileServerAdministratorUsersOrGroups,
       "ntxTrapUserDefinedAlert": ntxTrapUserDefinedAlert,
       "ntxTrapFileServerNetworkChangeFailed": ntxTrapFileServerNetworkChangeFailed,
       "ntxTrapSnapshotCreationDelayed": ntxTrapSnapshotCreationDelayed,
       "ntxTrapA130146": ntxTrapA130146,
       "ntxTrapA130143": ntxTrapA130143,
       "ntxTrapA130144": ntxTrapA130144,
       "ntxTrapFoundationVersionsInconsistent": ntxTrapFoundationVersionsInconsistent,
       "ntxTrapMetadataDiskUsageIsHigherThanTheSpecifiedLimit": ntxTrapMetadataDiskUsageIsHigherThanTheSpecifiedLimit,
       "ntxTrapVolumeGroupSpaceUsageExceeded": ntxTrapVolumeGroupSpaceUsageExceeded,
       "ntxTrapVSSContainersHaveHighFileCount": ntxTrapVSSContainersHaveHighFileCount,
       "ntxTrapCVMIpAddressIsUnreachable": ntxTrapCVMIpAddressIsUnreachable,
       "ntxTrapIncorrectClusterInformationInTheRemoteSite": ntxTrapIncorrectClusterInformationInTheRemoteSite,
       "ntxTrapProtectionDomainActivationMayFailAsConflictingFilesExist": ntxTrapProtectionDomainActivationMayFailAsConflictingFilesExist,
       "ntxTrapVNUMAVMPinningFailure": ntxTrapVNUMAVMPinningFailure,
       "ntxTrapGuestPowerOperationThroughNGTFailed": ntxTrapGuestPowerOperationThroughNGTFailed,
       "ntxTrapMellanoxNICNotInstalledOrWithWrongTypeOnHostMachine": ntxTrapMellanoxNICNotInstalledOrWithWrongTypeOnHostMachine,
       "ntxTrapNonComplianceWithHostAffinityPolicies": ntxTrapNonComplianceWithHostAffinityPolicies,
       "ntxTrapPolicyNotApplicableToAnyHost": ntxTrapPolicyNotApplicableToAnyHost,
       "ntxTrapTheClusterIsNotSynchronizingTimeWithAnyExternalServers": ntxTrapTheClusterIsNotSynchronizingTimeWithAnyExternalServers,
       "ntxTrapTheHypervisorIsNotSynchronizingTimeWithAnyExternalServers": ntxTrapTheHypervisorIsNotSynchronizingTimeWithAnyExternalServers,
       "ntxTrapProtectionDomainActivationOrMigrationFailure": ntxTrapProtectionDomainActivationOrMigrationFailure,
       "ntxTrapProtectionDomainContainsMoreThanTheSpecifiedVMs": ntxTrapProtectionDomainContainsMoreThanTheSpecifiedVMs,
       "ntxTrapSATADOMML3SEHasHighWear": ntxTrapSATADOMML3SEHasHighWear,
       "ntxTrapFileServerAntiVirusScanQueueFullOnFSVM": ntxTrapFileServerAntiVirusScanQueueFullOnFSVM,
       "ntxTrapFileServerAntiVirusScanQueuePilingUpOnFSVM": ntxTrapFileServerAntiVirusScanQueuePilingUpOnFSVM,
       "ntxTrapFileServerAntiVirusExcessiveQuarantinedUnquarantinedFiles": ntxTrapFileServerAntiVirusExcessiveQuarantinedUnquarantinedFiles,
       "ntxTrapA160048": ntxTrapA160048,
       "ntxTrapFailedToTakeTheApplicationconsistentSnapshotForTheVM": ntxTrapFailedToTakeTheApplicationconsistentSnapshotForTheVM,
       "ntxTrapRemovalOfTheTemporaryHypervisorSnapshotFailedForTheVM": ntxTrapRemovalOfTheTemporaryHypervisorSnapshotFailedForTheVM,
       "ntxTrapCloudDiskUsageIsNearingTheThreshold": ntxTrapCloudDiskUsageIsNearingTheThreshold,
       "ntxTrapDIMMsHaveInvalidPartNumber": ntxTrapDIMMsHaveInvalidPartNumber,
       "ntxTrapAzureCloudControllerVMHasSmallerDisks": ntxTrapAzureCloudControllerVMHasSmallerDisks,
       "ntxTrapFirmwareVersionOfSM863OrSM863aDrivesIsOld": ntxTrapFirmwareVersionOfSM863OrSM863aDrivesIsOld,
       "ntxTrapM2Micron5100HostBootDriveHasWornOut": ntxTrapM2Micron5100HostBootDriveHasWornOut,
       "ntxTrapM2IntelS3520HostBootDriveHasWornOut": ntxTrapM2IntelS3520HostBootDriveHasWornOut,
       "ntxTrapClusterInOverrideMode": ntxTrapClusterInOverrideMode,
       "ntxTrapMultipleVcentersDiscovered": ntxTrapMultipleVcentersDiscovered,
       "ntxTrapProtectionRuleTestAlertTitle": ntxTrapProtectionRuleTestAlertTitle,
       "ntxTrapExternalClientAuthentication": ntxTrapExternalClientAuthentication,
       "ntxTrapTwoNodeClusterStateChangeToclusteroperationmode": ntxTrapTwoNodeClusterStateChangeToclusteroperationmode,
       "ntxTrapWitnessIsUnreachableFromNode": ntxTrapWitnessIsUnreachableFromNode,
       "ntxTrapTwoNodeClusterChangedStateToStandaloneMode": ntxTrapTwoNodeClusterChangedStateToStandaloneMode,
       "ntxTrapTwoNodeClusterStateChangeTostate": ntxTrapTwoNodeClusterStateChangeTostate,
       "ntxTrapTwoNodeClusterStateChangeToStandaloneMode": ntxTrapTwoNodeClusterStateChangeToStandaloneMode,
       "ntxTrapRecoveryPlanExecutionFailed": ntxTrapRecoveryPlanExecutionFailed,
       "ntxTrapXiPaymentMissed": ntxTrapXiPaymentMissed,
       "ntxTrapFreeXiAccountExpired": ntxTrapFreeXiAccountExpired,
       "ntxTrapXiSubscriptionExpired": ntxTrapXiSubscriptionExpired,
       "ntxTrapEntitySyncFailure": ntxTrapEntitySyncFailure,
       "ntxTrapNucalmInternalServiceHasStoppedWorking": ntxTrapNucalmInternalServiceHasStoppedWorking,
       "ntxTrapEpsilonInternalServiceHasStoppedWorking": ntxTrapEpsilonInternalServiceHasStoppedWorking,
       "ntxTrapProtectionRuleConflictOccurred": ntxTrapProtectionRuleConflictOccurred,
       "ntxTrapDomainFaultToleranceIsReducedForMetadata": ntxTrapDomainFaultToleranceIsReducedForMetadata,
       "ntxTrapVMProtectionFailed": ntxTrapVMProtectionFailed,
       "ntxTrapVMRecoveryPointReplicationFailed": ntxTrapVMRecoveryPointReplicationFailed,
       "ntxTrapVMRecoveryPointCreationFailed": ntxTrapVMRecoveryPointCreationFailed,
       "ntxTrapMicrosegmentationControlPlaneFailed": ntxTrapMicrosegmentationControlPlaneFailed,
       "ntxTrapMicrosegmentationRuleFailed": ntxTrapMicrosegmentationRuleFailed,
       "ntxTrapDriveRemovalStuck": ntxTrapDriveRemovalStuck,
       "ntxTrapFileServerNTPServersConnectivityFailure": ntxTrapFileServerNTPServersConnectivityFailure,
       "ntxTrapFileServerTimeIsOutOfSyncWithTheActiveDirectory": ntxTrapFileServerTimeIsOutOfSyncWithTheActiveDirectory,
       "ntxTrapFileServerDNSResolverIPConnectivityFailure": ntxTrapFileServerDNSResolverIPConnectivityFailure,
       "ntxTrapFileServerUserManagementConfigurationFailed": ntxTrapFileServerUserManagementConfigurationFailed,
       "ntxTraphomePartitionUsageOnAFileServerVMHigherThanThreshold": ntxTraphomePartitionUsageOnAFileServerVMHigherThanThreshold,
       "ntxTrapFileServerDNSRecordsCannotBeRefreshed": ntxTrapFileServerDNSRecordsCannotBeRefreshed,
       "ntxTrapFileServerShareBackupDiffPathTranslationFailed": ntxTrapFileServerShareBackupDiffPathTranslationFailed,
       "ntxTrapFileServerPartnerServerConnectivityDown": ntxTrapFileServerPartnerServerConnectivityDown,
       "ntxTrapFileServerPDActionToIncompatibleRemoteSiteAOS": ntxTrapFileServerPDActionToIncompatibleRemoteSiteAOS,
       "ntxTrapFileServerServicesGotInterrupted": ntxTrapFileServerServicesGotInterrupted,
       "ntxTrapCommonPortGroupBetweenESXiHostsIsAbsent": ntxTrapCommonPortGroupBetweenESXiHostsIsAbsent,
       "ntxTrapFailedToReceiveSnapshotForTheProtectionDomain": ntxTrapFailedToReceiveSnapshotForTheProtectionDomain,
       "ntxTrapHostNetworkUplinkConfigurationFailed": ntxTrapHostNetworkUplinkConfigurationFailed,
       "ntxTrapRestartVMsBeforePerformingUpgradeOrMigrateOperation": ntxTrapRestartVMsBeforePerformingUpgradeOrMigrateOperation,
       "ntxTrapOplogEpisodeCountCheck": ntxTrapOplogEpisodeCountCheck,
       "ntxTrapCerebroStatsCollectorFailed": ntxTrapCerebroStatsCollectorFailed,
       "ntxTrapLatencyBetweenCVMsIsHigh": ntxTrapLatencyBetweenCVMsIsHigh,
       "ntxTrapLicenseInvalid": ntxTrapLicenseInvalid,
       "ntxTrapRemoteSiteAOSNotCompatibleWithFileServerVersion": ntxTrapRemoteSiteAOSNotCompatibleWithFileServerVersion,
       "ntxTrapA106043": ntxTrapA106043,
       "ntxTrapFirmwareVersionOfIntelS4600DrivesIsOld": ntxTrapFirmwareVersionOfIntelS4600DrivesIsOld,
       "ntxTrapIntelS4600DriveHasWornOut": ntxTrapIntelS4600DriveHasWornOut,
       "ntxTrapHostBootDiskSerialNumberHasChanged": ntxTrapHostBootDiskSerialNumberHasChanged,
       "ntxTrapSataControllerStatusIsBad": ntxTrapSataControllerStatusIsBad,
       "ntxTrapSamsung863Or863aOnipaddressHasConfigurationProblems": ntxTrapSamsung863Or863aOnipaddressHasConfigurationProblems,
       "ntxTrapHypervisorBootDriveRAIDIsInAnUnhealthyState": ntxTrapHypervisorBootDriveRAIDIsInAnUnhealthyState,
       "ntxTrapCVMPortGroupRenamed": ntxTrapCVMPortGroupRenamed,
       "ntxTrapA106453": ntxTrapA106453,
       "ntxTrapActiveDirectoryDCsAndorDNSServersRunningOnCluster": ntxTrapActiveDirectoryDCsAndorDNSServersRunningOnCluster,
       "ntxTrappowersourceDown": ntxTrappowersourceDown,
       "ntxTrapCPUTemperatureLow": ntxTrapCPUTemperatureLow,
       "ntxTrapRAMTemperatureLow": ntxTrapRAMTemperatureLow,
       "ntxTrapSystemTemperatureLow": ntxTrapSystemTemperatureLow,
       "ntxTrapIPMISELLogFetchFail": ntxTrapIPMISELLogFetchFail,
       "ntxTrapIPMISELLogPowerFailure": ntxTrapIPMISELLogPowerFailure,
       "ntxTrapAggressiveBreakReplicationTimeout": ntxTrapAggressiveBreakReplicationTimeout,
       "ntxTrapCVMOrPCVMRAMUsageHigh": ntxTrapCVMOrPCVMRAMUsageHigh,
       "ntxTrapCVMOrPCVMCPULoadHigh": ntxTrapCVMOrPCVMCPULoadHigh,
       "ntxTrapCVMRenamedIncorrectly": ntxTrapCVMRenamedIncorrectly,
       "ntxTrapPCVMDiskUsageHigh": ntxTrapPCVMDiskUsageHigh,
       "ntxTrapvmtypeVirtualIPCheck": ntxTrapvmtypeVirtualIPCheck,
       "ntxTrapvmtypeSameTimezoneCheck": ntxTrapvmtypeSameTimezoneCheck,
       "ntxTrapDIMMConfigurationIsWrong": ntxTrapDIMMConfigurationIsWrong,
       "ntxTrapP40GPUConfigurationWrongOnTheNode": ntxTrapP40GPUConfigurationWrongOnTheNode,
       "ntxTrapP40GPUBMCVersionIsOldOnTheNode": ntxTrapP40GPUBMCVersionIsOldOnTheNode,
       "ntxTrapMemoryConfigurationInconsistent": ntxTrapMemoryConfigurationInconsistent,
       "ntxTrapEntityCountExceededTheMaximumLimit": ntxTrapEntityCountExceededTheMaximumLimit,
       "ntxTrapAOSUpgradesAreDisabledOncvmip": ntxTrapAOSUpgradesAreDisabledOncvmip,
       "ntxTrapFirmwareUpgradesAreDisabledOncvmip": ntxTrapFirmwareUpgradesAreDisabledOncvmip,
       "ntxTrapHypervisorDiskdevnameSpaceUsageHigh": ntxTrapHypervisorDiskdevnameSpaceUsageHigh,
       "ntxTrapCVMPasswordlessSSHToHost": ntxTrapCVMPasswordlessSSHToHost,
       "ntxTrapCPUsOfDifferentTypesOrModelsAreInTheSameChassis": ntxTrapCPUsOfDifferentTypesOrModelsAreInTheSameChassis,
       "ntxTrapRecoveryPointReplicationSkipped": ntxTrapRecoveryPointReplicationSkipped,
       "ntxTrapNetworkCreationFailureForRecoveryPlan": ntxTrapNetworkCreationFailureForRecoveryPlan,
       "ntxTrapVirtualIPAddressNotConfiguredOnTheRemoteCluster": ntxTrapVirtualIPAddressNotConfiguredOnTheRemoteCluster,
       "ntxTrapEntityCountExceedDiscovered": ntxTrapEntityCountExceedDiscovered,
       "ntxTrapVMReplicationFailure": ntxTrapVMReplicationFailure,
       "ntxTrapVMReplicationExpired": ntxTrapVMReplicationExpired,
       "ntxTrapApplicationConsistentRecoveryPointFailed": ntxTrapApplicationConsistentRecoveryPointFailed,
       "ntxTrapReplicationTimeExceededTheRPOLimit": ntxTrapReplicationTimeExceededTheRPOLimit,
       "ntxTrapNGTOnVMvmnameWasNotReachable": ntxTrapNGTOnVMvmnameWasNotReachable,
       "ntxTrapVMReplicationHasNotProgressed": ntxTrapVMReplicationHasNotProgressed,
       "ntxTrapVSSProviderOrprefreezepostthawScriptsNotInstalled": ntxTrapVSSProviderOrprefreezepostthawScriptsNotInstalled,
       "ntxTrapPartialRecoveryPoint": ntxTrapPartialRecoveryPoint,
       "ntxTrapPulseCannotConnectToRESTServerEndpoint": ntxTrapPulseCannotConnectToRESTServerEndpoint,
       "ntxTrapJumboFramesEnabledForNICnicnameOnservicevmexternalip": ntxTrapJumboFramesEnabledForNICnicnameOnservicevmexternalip,
       "ntxTrapUnableToRetrieveTheAvailabilityZoneEndpoint": ntxTrapUnableToRetrieveTheAvailabilityZoneEndpoint,
       "ntxTrapRecoveryPointReplicationFailed": ntxTrapRecoveryPointReplicationFailed,
       "ntxTrapUnableToCommunicateWithTheDataCenterManager": ntxTrapUnableToCommunicateWithTheDataCenterManager,
       "ntxTrapRemoteSiteInSameVCenterDatacenter": ntxTrapRemoteSiteInSameVCenterDatacenter,
       "ntxTrapV100GPUConfigurationWrongOnTheNode": ntxTrapV100GPUConfigurationWrongOnTheNode,
       "ntxTrapApplicationsArchiveReadyForDownload": ntxTrapApplicationsArchiveReadyForDownload,
       "ntxTrapMoreThanOneTypeOfGPUsInstalledOnTheSameNode": ntxTrapMoreThanOneTypeOfGPUsInstalledOnTheSameNode,
       "ntxTrapVmRegisteredWithoutNetwork": ntxTrapVmRegisteredWithoutNetwork,
       "ntxTrapAlertEmailFailure": ntxTrapAlertEmailFailure,
       "ntxTrapNICRXCRCErrorRateHigh": ntxTrapNICRXCRCErrorRateHigh,
       "ntxTrapNICRXMissedErrorRateHigh": ntxTrapNICRXMissedErrorRateHigh,
       "ntxTrapEntityUnprotectionFailed": ntxTrapEntityUnprotectionFailed,
       "ntxTrapAvailabilityZoneValidationFailed": ntxTrapAvailabilityZoneValidationFailed,
       "ntxTrapInvalidNetworkMappingForRecoveryPlanrecoveryplanname": ntxTrapInvalidNetworkMappingForRecoveryPlanrecoveryplanname,
       "ntxTrapDataProtectionTasksAreNotProgressing": ntxTrapDataProtectionTasksAreNotProgressing,
       "ntxTrapIncorrectClusterInformationInTheRemoteSiteremotename": ntxTrapIncorrectClusterInformationInTheRemoteSiteremotename,
       "ntxTrapVCenterNotRegistered": ntxTrapVCenterNotRegistered,
       "ntxTrapNGTUpdateAvailable": ntxTrapNGTUpdateAvailable,
       "ntxTrapDuplicateCVMIPAddressDetected": ntxTrapDuplicateCVMIPAddressDetected,
       "ntxTrapMTUConfigurationAcrossControllerVMsIsNotConsistent": ntxTrapMTUConfigurationAcrossControllerVMsIsNotConsistent,
       "ntxTrapMultipleCpuunblockProcessesRunning": ntxTrapMultipleCpuunblockProcessesRunning,
       "ntxTrapRecoveryLocationOperationChangedToReadOnlyMode": ntxTrapRecoveryLocationOperationChangedToReadOnlyMode,
       "ntxTrapA130181": ntxTrapA130181,
       "ntxTrapAvailabilityZoneConnectionFailure": ntxTrapAvailabilityZoneConnectionFailure,
       "ntxTrapPEPCConnectionFailure": ntxTrapPEPCConnectionFailure,
       "ntxTrapNutanixGuestToolsNotUpgraded": ntxTrapNutanixGuestToolsNotUpgraded,
       "ntxTrapFileServerMultipleVMsOnSingleNodeCheck": ntxTrapFileServerMultipleVMsOnSingleNodeCheck,
       "ntxTrapShareUsageReachingToConfiguredLimit": ntxTrapShareUsageReachingToConfiguredLimit,
       "ntxTrapProtectedVMsNotRecoverable": ntxTrapProtectedVMsNotRecoverable,
       "ntxTrapEntitySyncFailureForProtectionRule": ntxTrapEntitySyncFailureForProtectionRule,
       "ntxTrapEntitySyncFailureForRecoveryPlan": ntxTrapEntitySyncFailureForRecoveryPlan,
       "ntxTrapDataAtRestEncryptionKeyBackupWarning": ntxTrapDataAtRestEncryptionKeyBackupWarning,
       "ntxTrapLocalKeyManagerMasterKeyRotationWarning": ntxTrapLocalKeyManagerMasterKeyRotationWarning,
       "ntxTrapPulseCannotConnectToRESTServerEndpointOnFileServer": ntxTrapPulseCannotConnectToRESTServerEndpointOnFileServer,
       "ntxTrapDetectedIncompatibleAHVVersion": ntxTrapDetectedIncompatibleAHVVersion,
       "ntxTrapNucalmLicenseIsOvershooting": ntxTrapNucalmLicenseIsOvershooting,
       "ntxTrapA300409": ntxTrapA300409,
       "ntxTrapValidationFailedForRecoveryPlanrecoveryplanname": ntxTrapValidationFailedForRecoveryPlanrecoveryplanname,
       "ntxTrapoperationtypeFailedForRecoveryPlanrecoveryplanname": ntxTrapoperationtypeFailedForRecoveryPlanrecoveryplanname,
       "ntxTrapA300402": ntxTrapA300402,
       "ntxTrapEntitySyncFailureForAvailabilityZone": ntxTrapEntitySyncFailureForAvailabilityZone,
       "ntxTrapRemoteAvailabilityZoneLatencyIsHigh": ntxTrapRemoteAvailabilityZoneLatencyIsHigh,
       "ntxTrapTheFrequencyOfCPUcpuidOnHosthostipIsExtremelyLow": ntxTrapTheFrequencyOfCPUcpuidOnHosthostipIsExtremelyLow,
       "ntxTrapCalmLicenseExpiry": ntxTrapCalmLicenseExpiry,
       "ntxTrapPCVMCPULoadHigh": ntxTrapPCVMCPULoadHigh,
       "ntxTrapNodeMarkedToBeAutoAddedToMetadataRing": ntxTrapNodeMarkedToBeAutoAddedToMetadataRing,
       "ntxTrapAutomaticAdditionOfNodeToMetadataRingDisabled": ntxTrapAutomaticAdditionOfNodeToMetadataRingDisabled,
       "ntxTrapNodeMarkedToBeDetachedFromMetadataRing": ntxTrapNodeMarkedToBeDetachedFromMetadataRing,
       "ntxTrapNodeForwardingMetadataRequests": ntxTrapNodeForwardingMetadataRequests,
       "ntxTrapRecoveryPlansHaveConflictingNetworkMappings": ntxTrapRecoveryPlansHaveConflictingNetworkMappings,
       "ntxTrapVMRecoveryMayFail": ntxTrapVMRecoveryMayFail,
       "ntxTrapNutanixCalmLicenseViolation": ntxTrapNutanixCalmLicenseViolation,
       "ntxTrapTranslatedAddressesRetrievalFailureInNGT": ntxTrapTranslatedAddressesRetrievalFailureInNGT,
       "ntxTrapStoragePoolUsageReachingItsLimit": ntxTrapStoragePoolUsageReachingItsLimit,
       "ntxTrapTargetCouldNotBeFoundForReplication": ntxTrapTargetCouldNotBeFoundForReplication,
       "ntxTrapClusterJoinToDomainFailure": ntxTrapClusterJoinToDomainFailure,
       "ntxTrapUnplannedFailoverAndFailbackCanCauseFullReplication": ntxTrapUnplannedFailoverAndFailbackCanCauseFullReplication,
       "ntxTrapEntitySyncFailureForTheProtectionPolicy": ntxTrapEntitySyncFailureForTheProtectionPolicy,
       "ntxTrapEntitySyncFailureForTheRecoveryPlan": ntxTrapEntitySyncFailureForTheRecoveryPlan,
       "ntxTrapEntitySyncFailureForTheAvailabilityZone": ntxTrapEntitySyncFailureForTheAvailabilityZone,
       "ntxTrapDeleteTheFailedOverVMsOnThePrimaryLocation": ntxTrapDeleteTheFailedOverVMsOnThePrimaryLocation,
       "ntxTrapVMvmnameMemoryOverprovisioned": ntxTrapVMvmnameMemoryOverprovisioned,
       "ntxTrapVMvmnameMemoryConstrained": ntxTrapVMvmnameMemoryConstrained,
       "ntxTrapVMvmnameCPUOverprovisioned": ntxTrapVMvmnameCPUOverprovisioned,
       "ntxTrapVMvmnameCPUConstrained": ntxTrapVMvmnameCPUConstrained,
       "ntxTrapVMvmnameInactive": ntxTrapVMvmnameInactive,
       "ntxTrapVMBullyvmname": ntxTrapVMBullyvmname,
       "ntxTrapNutanixGuestToolsFailedToInitiateVMReboot": ntxTrapNutanixGuestToolsFailedToInitiateVMReboot,
       "ntxTrapMultipleRecoveryPlansHaveCategorycategory": ntxTrapMultipleRecoveryPlansHaveCategorycategory,
       "ntxTrapFloatingIPfloatingipIsAssociatedWithMultipleVMs": ntxTrapFloatingIPfloatingipIsAssociatedWithMultipleVMs,
       "ntxTrapRemoteReplicationIsLaggingForProtectionDomainSnapshot": ntxTrapRemoteReplicationIsLaggingForProtectionDomainSnapshot,
       "ntxTrapSameVMsPresentInMultipleStagesOfTheRecoveryPlan": ntxTrapSameVMsPresentInMultipleStagesOfTheRecoveryPlan,
       "ntxTrapZookeeperAliasIsIncorrectlyConfiguredInTheCluster": ntxTrapZookeeperAliasIsIncorrectlyConfiguredInTheCluster,
       "ntxTrapValidationFailedForTheRecoveryPlan": ntxTrapValidationFailedForTheRecoveryPlan,
       "ntxTrapNetworkCreationFailureForTheRecoveryPlan": ntxTrapNetworkCreationFailureForTheRecoveryPlan,
       "ntxTrapValidationFailedForTheRecoveryPlanrecoveryplanname": ntxTrapValidationFailedForTheRecoveryPlanrecoveryplanname,
       "ntxTrapVirtualIPAddressNotConfiguredOnTheCluster": ntxTrapVirtualIPAddressNotConfiguredOnTheCluster,
       "ntxTrapNGTOnVMvmnameIsNotReachable": ntxTrapNGTOnVMvmnameIsNotReachable,
       "ntxTrapCVMNICLinkDown": ntxTrapCVMNICLinkDown,
       "ntxTrapA300417": ntxTrapA300417,
       "ntxTrapConflictingNgtPolicies": ntxTrapConflictingNgtPolicies,
       "ntxTrapSystemTemperatureReadingError": ntxTrapSystemTemperatureReadingError,
       "ntxTrapMultipleRecoveryPlansAreAssociatedWithCategorycategory": ntxTrapMultipleRecoveryPlansAreAssociatedWithCategorycategory,
       "ntxTrapA300412": ntxTrapA300412,
       "ntxTrapA110401": ntxTrapA110401,
       "ntxTrapA300418": ntxTrapA300418,
       "ntxTrapA300416": ntxTrapA300416,
       "ntxTrapVMsArePartOfMultipleStagesInTheRecoveryPlanrecoveryplan": ntxTrapVMsArePartOfMultipleStagesInTheRecoveryPlanrecoveryplan,
       "ntxTrapA300414": ntxTrapA300414,
       "ntxTrapKaranServicesAreUnreachable": ntxTrapKaranServicesAreUnreachable,
       "ntxTrapDataserviceIPIsUnreachable": ntxTrapDataserviceIPIsUnreachable,
       "ntxTrapUSBBootDeviceMissingOnNode": ntxTrapUSBBootDeviceMissingOnNode,
       "ntxTrapVSSSnapshotOfContainerShareFailed": ntxTrapVSSSnapshotOfContainerShareFailed,
       "ntxTrapPrismIsRestartingFrequently": ntxTrapPrismIsRestartingFrequently,
       "ntxTrapRecoveryPlanValidationFailedWithWarnings": ntxTrapRecoveryPlanValidationFailedWithWarnings,
       "ntxTrapRecoveryPlanValidationFailedWithErrors": ntxTrapRecoveryPlanValidationFailedWithErrors,
       "ntxTrapRecoveryPlanExecutionFailureDueToValidationErrors": ntxTrapRecoveryPlanExecutionFailureDueToValidationErrors,
       "ntxTrapInvalidNetworkSettingsForTheRecoveryPlan": ntxTrapInvalidNetworkSettingsForTheRecoveryPlan,
       "ntxTrapRecoveryPlanExecutionFailure": ntxTrapRecoveryPlanExecutionFailure,
       "ntxTrapSubnetsDeletionFailureForTheRecoveryPlan": ntxTrapSubnetsDeletionFailureForTheRecoveryPlan,
       "ntxTrapFloatingIPsDeallocationFailed": ntxTrapFloatingIPsDeallocationFailed,
       "ntxTrapSubnetCreationFailureForTheRecoveryPlan": ntxTrapSubnetCreationFailureForTheRecoveryPlan,
       "ntxTrapFloatingIPsAllocationFailed": ntxTrapFloatingIPsAllocationFailed,
       "ntxTrapFailoverOrFailbackOperationsAreNotPossible": ntxTrapFailoverOrFailbackOperationsAreNotPossible,
       "ntxTrapValidationWarningsFoundDuringRecoveryPlanExecution": ntxTrapValidationWarningsFoundDuringRecoveryPlanExecution,
       "ntxTrapNodeRemovalFailure": ntxTrapNodeRemovalFailure,
       "ntxTrapConflictingNGTPolicies": ntxTrapConflictingNGTPolicies,
       "ntxTrapVmRestorationFailed": ntxTrapVmRestorationFailed,
       "ntxTrapRecoveryLocationIsInReadOnlyMode": ntxTrapRecoveryLocationIsInReadOnlyMode,
       "ntxTrapNGTOnVMIsNotReachable": ntxTrapNGTOnVMIsNotReachable,
       "ntxTrapNutanixGuestToolsNotInstalledOnTheVM": ntxTrapNutanixGuestToolsNotInstalledOnTheVM,
       "ntxTrapFullReplicationStartedForTheVM": ntxTrapFullReplicationStartedForTheVM,
       "ntxTrapReplicationTimeExceededTheRPO": ntxTrapReplicationTimeExceededTheRPO,
       "ntxTrapNutanixVSSProviderOrprefreezepostthawScriptsNotInstalled": ntxTrapNutanixVSSProviderOrprefreezepostthawScriptsNotInstalled,
       "ntxTrapFailedToFindTheTargetClusterForReplication": ntxTrapFailedToFindTheTargetClusterForReplication,
       "ntxTrapVMVirtualHardwareVersionIncompatible": ntxTrapVMVirtualHardwareVersionIncompatible,
       "ntxTrapVMMigrationFailed": ntxTrapVMMigrationFailed,
       "ntxTrapVMRegisteredWithoutAnyNetwork": ntxTrapVMRegisteredWithoutAnyNetwork,
       "ntxTrapProtectedVMNotRecoverable": ntxTrapProtectedVMNotRecoverable,
       "ntxTrapBackgroundEncryptionStuck": ntxTrapBackgroundEncryptionStuck,
       "ntxTrapMaximumConnectionsLimitAboutToReachOnAFileServerVM": ntxTrapMaximumConnectionsLimitAboutToReachOnAFileServerVM,
       "ntxTrapVSSSnapshotIsNotSupportedForSomeVMs": ntxTrapVSSSnapshotIsNotSupportedForSomeVMs,
       "ntxTrapA110262": ntxTrapA110262,
       "ntxTrapIncorrectvmtypeNTPConfiguration": ntxTrapIncorrectvmtypeNTPConfiguration,
       "ntxTrapThevmtypeIsNotSynchronizingTimeWithAnyExternalServers": ntxTrapThevmtypeIsNotSynchronizingTimeWithAnyExternalServers,
       "ntxTrapA103095": ntxTrapA103095,
       "ntxTrapFirmwareVersionOfIntelS4600DrivesIsOldOrInvalid": ntxTrapFirmwareVersionOfIntelS4600DrivesIsOldOrInvalid,
       "ntxTrapRemotenameConnectivityStatus": ntxTrapRemotenameConnectivityStatus,
       "ntxTrapIncompleteMetroSetup": ntxTrapIncompleteMetroSetup,
       "ntxTrapA101047": ntxTrapA101047,
       "ntxTrapP4GPUConfigurationWrongOnTheNode": ntxTrapP4GPUConfigurationWrongOnTheNode,
       "ntxTrapPCVMTypeOrAnnotationNotSet": ntxTrapPCVMTypeOrAnnotationNotSet,
       "ntxTrapFailedToConfigureHostForAtlasNetworking": ntxTrapFailedToConfigureHostForAtlasNetworking,
       "ntxTrapFailedToReserveHostMemoryForAtlasNetworking": ntxTrapFailedToReserveHostMemoryForAtlasNetworking,
       "ntxTrapRecoveryPlanExecutionExceededTheTimeLimit": ntxTrapRecoveryPlanExecutionExceededTheTimeLimit,
       "ntxTrapAHVPrismElementDetached": ntxTrapAHVPrismElementDetached,
       "ntxTrapBeamIsNotReachable": ntxTrapBeamIsNotReachable,
       "ntxTrapAHVPrismElementAttached": ntxTrapAHVPrismElementAttached,
       "ntxTrapVPNIPSECTunnelBetweenOnpremAndXiDatacenterIsDown": ntxTrapVPNIPSECTunnelBetweenOnpremAndXiDatacenterIsDown,
       "ntxTrapEBGPSessionBetweenOnpremAndXiDatacenterIsDown": ntxTrapEBGPSessionBetweenOnpremAndXiDatacenterIsDown,
       "ntxTrapMaximumVPNBGPRouteLimitReached": ntxTrapMaximumVPNBGPRouteLimitReached,
       "ntxTrapDomainFaultToleranceIsLowForMetadata": ntxTrapDomainFaultToleranceIsLowForMetadata,
       "ntxTrapRecoveryLocationIsNotInGoodState": ntxTrapRecoveryLocationIsNotInGoodState,
       "ntxTrapA110264": ntxTrapA110264,
       "ntxTrapFlowControlPlaneFailed": ntxTrapFlowControlPlaneFailed,
       "ntxTrapFlowRuleFailed": ntxTrapFlowRuleFailed,
       "ntxTrapAnalyticsVMComponentFailure": ntxTrapAnalyticsVMComponentFailure,
       "ntxTrapAnalyticsVMHighCPUUsage": ntxTrapAnalyticsVMHighCPUUsage,
       "ntxTrapAnalyticsVMHighDiskUsage": ntxTrapAnalyticsVMHighDiskUsage,
       "ntxTrapAnalyticsVMLowMemoryAvailable": ntxTrapAnalyticsVMLowMemoryAvailable,
       "ntxTrapDuplicateIPAddressDetectedForAFileServerVM": ntxTrapDuplicateIPAddressDetectedForAFileServerVM,
       "ntxTrapFileServerUniqueFsidFailure": ntxTrapFileServerUniqueFsidFailure,
       "ntxTrapUnequalDiskSizeOfPCVMs": ntxTrapUnequalDiskSizeOfPCVMs,
       "ntxTrapHighTimeDifferenceBetweenPCAndRegisteredPEs": ntxTrapHighTimeDifferenceBetweenPCAndRegisteredPEs,
       "ntxTrapPrismCentralVersionEOL": ntxTrapPrismCentralVersionEOL,
       "ntxTrapPEPCIncompatibleAOSVersions": ntxTrapPEPCIncompatibleAOSVersions,
       "ntxTrapAplosGatewayIsDown": ntxTrapAplosGatewayIsDown,
       "ntxTrapAplosEngineIsDown": ntxTrapAplosEngineIsDown,
       "ntxTrapStorageContainersAreNotMountedOnAllNodes": ntxTrapStorageContainersAreNotMountedOnAllNodes,
       "ntxTrapOldEntityCentricThirdPartyBackupSnapshotsPresent": ntxTrapOldEntityCentricThirdPartyBackupSnapshotsPresent,
       "ntxTrapUnsupportedSFPIsInstalledOnHostMachine": ntxTrapUnsupportedSFPIsInstalledOnHostMachine,
       "ntxTrapMultipleRecoveryPlansAssociatedWithACategory": ntxTrapMultipleRecoveryPlansAssociatedWithACategory,
       "ntxTrapVMsArePartOfMultipleStagesInRecoveryPlan": ntxTrapVMsArePartOfMultipleStagesInRecoveryPlan,
       "ntxTrapTestFailoverOnRecoveryPlanHasNotBeenExecutedRecently": ntxTrapTestFailoverOnRecoveryPlanHasNotBeenExecutedRecently,
       "ntxTrapNumberOfVMsInRecoveryPlanExceedsTheThreshold": ntxTrapNumberOfVMsInRecoveryPlanExceedsTheThreshold,
       "ntxTrapSATADOMNeedsFirmwareUpgrade": ntxTrapSATADOMNeedsFirmwareUpgrade,
       "ntxTrapVCenterServerNotRegistered": ntxTrapVCenterServerNotRegistered,
       "ntxTrapDetectedOlderAHVVersion": ntxTrapDetectedOlderAHVVersion,
       "ntxTrapNoProtectionPolicyFoundForVMsInRecoveryPlan": ntxTrapNoProtectionPolicyFoundForVMsInRecoveryPlan,
       "ntxTrapVMsNotCleanedUpFollowingTheTestFailoverForRecoveryPlan": ntxTrapVMsNotCleanedUpFollowingTheTestFailoverForRecoveryPlan,
       "ntxTrapPowerSupplyStatusUnavailable": ntxTrapPowerSupplyStatusUnavailable,
       "ntxTrapCVMTimeAndIPMISELTimeDoNotMatch": ntxTrapCVMTimeAndIPMISELTimeDoNotMatch,
       "ntxTrapProtectionPolicyMaxVMsPerCategoryCheckFailed": ntxTrapProtectionPolicyMaxVMsPerCategoryCheckFailed,
       "ntxTrapPulseIsDisabled": ntxTrapPulseIsDisabled,
       "ntxTrapAOSVersionEOL": ntxTrapAOSVersionEOL,
       "ntxTrapDIMMsOfDifferentManufacturersInOneMemoryChannel": ntxTrapDIMMsOfDifferentManufacturersInOneMemoryChannel,
       "ntxTrapPrismCentralUsingDefaultPassword": ntxTrapPrismCentralUsingDefaultPassword,
       "ntxTrapCVMUsingDefaultPassword": ntxTrapCVMUsingDefaultPassword,
       "ntxTrapHostUsingDefaultPassword": ntxTrapHostUsingDefaultPassword,
       "ntxTrapIPMIUsingDefaultPassword": ntxTrapIPMIUsingDefaultPassword,
       "ntxTrapSM883DriveHasWornOut": ntxTrapSM883DriveHasWornOut,
       "ntxTrapFewerThanTwoNonSamsungPM883DrivesInstalledOnTheNode": ntxTrapFewerThanTwoNonSamsungPM883DrivesInstalledOnTheNode,
       "ntxTrapPM883DriveHasWornOut": ntxTrapPM883DriveHasWornOut,
       "ntxTrapCalmVersionMismatch": ntxTrapCalmVersionMismatch,
       "ntxTrapEpsilonVersionMismatch": ntxTrapEpsilonVersionMismatch,
       "ntxTrapCalmShowbackIsUnableToReachBeamService": ntxTrapCalmShowbackIsUnableToReachBeamService,
       "ntxTrapFileAnalyticsVMComponentFailure": ntxTrapFileAnalyticsVMComponentFailure,
       "ntxTrapFileAnalyticsVMHighCPUUsage": ntxTrapFileAnalyticsVMHighCPUUsage,
       "ntxTrapFileAnalyticsVMHighDiskUsage": ntxTrapFileAnalyticsVMHighDiskUsage,
       "ntxTrapFileAnalyticsVMLowMemoryAvailable": ntxTrapFileAnalyticsVMLowMemoryAvailable,
       "ntxTrapFileServerVMTimeDriftFromNTPServers": ntxTrapFileServerVMTimeDriftFromNTPServers,
       "ntxTrapFileServerServiceInCrashLoop": ntxTrapFileServerServiceInCrashLoop,
       "ntxTrapFileServerUpgradeTaskStuck": ntxTrapFileServerUpgradeTaskStuck,
       "ntxTrapFilesClusterHATakeoverFailure": ntxTrapFilesClusterHATakeoverFailure,
       "ntxTrapFileServerAlert": ntxTrapFileServerAlert,
       "ntxTrapFlowModeChangeFailed": ntxTrapFlowModeChangeFailed,
       "ntxTrapOVSServiceRestart": ntxTrapOVSServiceRestart,
       "ntxTrapRemoteSubnetIsNotConfiguredAppropriately": ntxTrapRemoteSubnetIsNotConfiguredAppropriately,
       "ntxTrapA130204": ntxTrapA130204,
       "ntxTrapA130205": ntxTrapA130205,
       "ntxTrapHostingOfVirtualIPOfTheNetworkSegmentationDRServiceFailed": ntxTrapHostingOfVirtualIPOfTheNetworkSegmentationDRServiceFailed,
       "ntxTrapFailureToCopyImageToCluster": ntxTrapFailureToCopyImageToCluster,
       "ntxTrapIDFirewallConnectivityaccessLossToAD": ntxTrapIDFirewallConnectivityaccessLossToAD,
       "ntxTrapEpochSaaSConnectivityIsLost": ntxTrapEpochSaaSConnectivityIsLost,
       "ntxTrapIDFirewallUnableToLocateMappedADObject": ntxTrapIDFirewallUnableToLocateMappedADObject,
       "ntxTrapSecurityPlanningIsDisabled": ntxTrapSecurityPlanningIsDisabled,
       "ntxTrapEpochDataCollectorNeedsUpgrade": ntxTrapEpochDataCollectorNeedsUpgrade,
       "ntxTrapIDFirewallUnableToRecoverStateFromADAfterDisconnect": ntxTrapIDFirewallUnableToRecoverStateFromADAfterDisconnect,
       "ntxTrapNGTCDROMNotUnmountedOnTheVM": ntxTrapNGTCDROMNotUnmountedOnTheVM,
       "ntxTrapFloatingIPsDeallocationFailedAfterFailbackFromXi": ntxTrapFloatingIPsDeallocationFailedAfterFailbackFromXi,
       "ntxTrapTomcatIsRestartingFrequently": ntxTrapTomcatIsRestartingFrequently,
       "ntxTrapExternalRepositoryAccessFailure": ntxTrapExternalRepositoryAccessFailure,
       "ntxTrapIOFailuresToADataSourceInAnExternalRepository": ntxTrapIOFailuresToADataSourceInAnExternalRepository,
       "ntxTrapUnequalDiskSizeOfPrismCentralVMs": ntxTrapUnequalDiskSizeOfPrismCentralVMs,
       "ntxTrapPCUpgradesAreDisabledOncvmip": ntxTrapPCUpgradesAreDisabledOncvmip,
       "ntxTrapCalmTrialLicenseExpiry": ntxTrapCalmTrialLicenseExpiry,
       "ntxTrapSystemNonRootPartitionsSpaceUsageHigh": ntxTrapSystemNonRootPartitionsSpaceUsageHigh,
       "ntxTrapSystemRootPartitionSpaceUsageHigh": ntxTrapSystemRootPartitionSpaceUsageHigh,
       "ntxTrapscratchLocationSpaceUsageIsHigh": ntxTrapscratchLocationSpaceUsageIsHigh,
       "ntxTrapFreeBlockCountOfSATADOMHasGoneBelowThreshold": ntxTrapFreeBlockCountOfSATADOMHasGoneBelowThreshold,
       "ntxTrapToshibaPM5DriveHasWornOut": ntxTrapToshibaPM5DriveHasWornOut,
       "ntxTrapMoreThanOneTypeOfToshibaPM5DrivesInstalledOnTheNode": ntxTrapMoreThanOneTypeOfToshibaPM5DrivesInstalledOnTheNode,
       "ntxTrapBootDriveIsInDegradedState": ntxTrapBootDriveIsInDegradedState,
       "ntxTrapTemperatureOfM2DiskIsOutOfRange": ntxTrapTemperatureOfM2DiskIsOutOfRange,
       "ntxTrapM2DiskReturnedUECCErrors": ntxTrapM2DiskReturnedUECCErrors,
       "ntxTrapM2DiskHasWornOut": ntxTrapM2DiskHasWornOut,
       "ntxTrapFirmwareOfRaidM2DiskNeedsToBeUpgraded": ntxTrapFirmwareOfRaidM2DiskNeedsToBeUpgraded,
       "ntxTrapRAIDCardBIOSOrFirmwareOrBootLoaderNeedsToBeUpdated": ntxTrapRAIDCardBIOSOrFirmwareOrBootLoaderNeedsToBeUpdated,
       "ntxTrapDiskFirmwareNeedsUpgrade": ntxTrapDiskFirmwareNeedsUpgrade,
       "ntxTrapFlowPolicyhitLoggingDisabled": ntxTrapFlowPolicyhitLoggingDisabled,
       "ntxTrapLatencyBetweenvmtypes": ntxTrapLatencyBetweenvmtypes,
       "ntxTrapCVMdestipIsUnreachable": ntxTrapCVMdestipIsUnreachable,
       "ntxTrapComputeonlyMinimumBandwidthCheck": ntxTrapComputeonlyMinimumBandwidthCheck,
       "ntxTrapFileServerVMDownCheck": ntxTrapFileServerVMDownCheck,
       "ntxTrapFileServerVMHardwareClockTimezoneNotSupported": ntxTrapFileServerVMHardwareClockTimezoneNotSupported,
       "ntxTrapNutanixFilesVersionEOL": ntxTrapNutanixFilesVersionEOL,
       "ntxTrapFileServerContainerDedupCheck": ntxTrapFileServerContainerDedupCheck,
       "ntxTrapCheckingIfTargetClusterVersionIsGreaterThan512": ntxTrapCheckingIfTargetClusterVersionIsGreaterThan512,
       "ntxTrapCheckingIfPortsOfRelevantServicesAreOpenOrNot": ntxTrapCheckingIfPortsOfRelevantServicesAreOpenOrNot,
       "ntxTrapA110022": ntxTrapA110022,
       "ntxTrapCheckingIfDRServicesAreReachableOrNot": ntxTrapCheckingIfDRServicesAreReachableOrNot,
       "ntxTrapHighNumberOfCorrectableECCErrorsFound": ntxTrapHighNumberOfCorrectableECCErrorsFound,
       "ntxTrapPowerSuppliesOfDifferentTypesDetectedOnANode": ntxTrapPowerSuppliesOfDifferentTypesDetectedOnANode,
       "ntxTrapPowerSupplyStatusDownUnretrievable": ntxTrapPowerSupplyStatusDownUnretrievable,
       "ntxTrapProtectedVMNameTooLongOrContainsRestrictedCharacters": ntxTrapProtectedVMNameTooLongOrContainsRestrictedCharacters,
       "ntxTrapDetectedSnapshotsOnClusterWithHighDensityNodes": ntxTrapDetectedSnapshotsOnClusterWithHighDensityNodes,
       "ntxTrapDataProtectionIsConfiguredOnClusterWithHighDensityNodes": ntxTrapDataProtectionIsConfiguredOnClusterWithHighDensityNodes,
       "ntxTrapA110452": ntxTrapA110452,
       "ntxTrapA110453": ntxTrapA110453,
       "ntxTrapNetworkIsNotProperlyConfiguredOnTheHost": ntxTrapNetworkIsNotProperlyConfiguredOnTheHost,
       "ntxTrapDisconnectedAvailabilityZonesAreAffectingSomeEntities": ntxTrapDisconnectedAvailabilityZonesAreAffectingSomeEntities,
       "ntxTrapRecoveryPlanHasMultipleAvailabilityZoneOrders": ntxTrapRecoveryPlanHasMultipleAvailabilityZoneOrders,
       "ntxTrapRecoveryPlanContainsVMsWithUnsupportedCHDRVMConfiguration": ntxTrapRecoveryPlanContainsVMsWithUnsupportedCHDRVMConfiguration,
       "ntxTrapA300426": ntxTrapA300426,
       "ntxTrapA300428": ntxTrapA300428,
       "ntxTrapvmtypeRebooted": ntxTrapvmtypeRebooted,
       "ntxTrapNodeIsInDegradedState": ntxTrapNodeIsInDegradedState,
       "ntxTrapComputeonlyClusterSizingHyperconvergedNodeCountCheck": ntxTrapComputeonlyClusterSizingHyperconvergedNodeCountCheck,
       "ntxTrapA405001": ntxTrapA405001,
       "ntxTrapComputeonlyClusterSizingCVMSizeCheck": ntxTrapComputeonlyClusterSizingCVMSizeCheck,
       "ntxTrapCalmContainersAreUnhealthy": ntxTrapCalmContainersAreUnhealthy,
       "ntxTrapHealthWarningsDetectedInMetadataService": ntxTrapHealthWarningsDetectedInMetadataService,
       "ntxTrapProtectedVMsNotCBRCapable": ntxTrapProtectedVMsNotCBRCapable,
       "ntxTrapAutoSupportCheckFails": ntxTrapAutoSupportCheckFails,
       "ntxTrapCoreDumpsAreEnabledOnThisCVMOrPCVM": ntxTrapCoreDumpsAreEnabledOnThisCVMOrPCVM,
       "ntxTrapUnequalMetadataPartitionSizesAcrossPrismCentralVMs": ntxTrapUnequalMetadataPartitionSizesAcrossPrismCentralVMs,
       "ntxTrapFileServerCloneGracePeriodCheck": ntxTrapFileServerCloneGracePeriodCheck,
       "ntxTrapVMRecoveryStorageContainerIsNotMountedOnAllHosts": ntxTrapVMRecoveryStorageContainerIsNotMountedOnAllHosts,
       "ntxTrapOpenflowTableGettingFull": ntxTrapOpenflowTableGettingFull,
       "ntxTrapNumberOfDatastoresConfiguredIsHigherThanESXiMaxConnPerIP": ntxTrapNumberOfDatastoresConfiguredIsHigherThanESXiMaxConnPerIP,
       "ntxTrapA110021": ntxTrapA110021,
       "ntxTrapCheckingIfPortsOfRelevantServicesAreOpen": ntxTrapCheckingIfPortsOfRelevantServicesAreOpen,
       "ntxTrapProtectedVMsMayNotBeRecoverable": ntxTrapProtectedVMsMayNotBeRecoverable,
       "ntxTrapExternallyRegisteredAlert": ntxTrapExternallyRegisteredAlert,
       "ntxTrapInvalidBreakReplicationTimeout": ntxTrapInvalidBreakReplicationTimeout,
       "ntxTrapBridgevSwitchConfigurationDoesNotMatchNSProtoInZookeeper": ntxTrapBridgevSwitchConfigurationDoesNotMatchNSProtoInZookeeper,
       "ntxTrapActiveDirectoryDCsRunningOnCluster": ntxTrapActiveDirectoryDCsRunningOnCluster,
       "ntxTrapDNSServersRunningOnCluster": ntxTrapDNSServersRunningOnCluster,
       "ntxTrapCPUUsageIsHighOnCVM": ntxTrapCPUUsageIsHighOnCVM,
       "ntxTrapSMARTParametersOfDiskAreOutOfRange": ntxTrapSMARTParametersOfDiskAreOutOfRange,
       "ntxTrapMinimumNOSAndFoundationVersionsAreNotSatisfied": ntxTrapMinimumNOSAndFoundationVersionsAreNotSatisfied,
       "ntxTrapPCVMSystemRootPartitionSpaceUsageHigh": ntxTrapPCVMSystemRootPartitionSpaceUsageHigh,
       "ntxTrapA300430": ntxTrapA300430,
       "ntxTrapCVMPythonServicesRestartingFrequently": ntxTrapCVMPythonServicesRestartingFrequently,
       "ntxTrapSnapshotReplicationToRemoteSiteIsLagging": ntxTrapSnapshotReplicationToRemoteSiteIsLagging,
       "ntxTrapSMARTParametersOfDiskhostAreOutOfRange": ntxTrapSMARTParametersOfDiskhostAreOutOfRange,
       "ntxTrapOneOrMoreCassandraNodesHaveInvalidTokens": ntxTrapOneOrMoreCassandraNodesHaveInvalidTokens,
       "ntxTrapSecureBootFeatureStatus": ntxTrapSecureBootFeatureStatus,
       "ntxTrapVMHasBeenRecoveredAtAnAlternatePath": ntxTrapVMHasBeenRecoveredAtAnAlternatePath,
       "ntxTrapInvalidHybridNodesConfigurationForErasureCoding": ntxTrapInvalidHybridNodesConfigurationForErasureCoding,
       "ntxTrapPlannedFailoverOrUnplannedFailoverOperationsWillFail": ntxTrapPlannedFailoverOrUnplannedFailoverOperationsWillFail,
       "ntxTrapFileServerManagerUpgradeFailed": ntxTrapFileServerManagerUpgradeFailed,
       "ntxTrapSEDKeysUnavailable": ntxTrapSEDKeysUnavailable,
       "ntxTrapSWEncryptionKeysFromkmsnameAreUnavailable": ntxTrapSWEncryptionKeysFromkmsnameAreUnavailable,
       "ntxTrapOVAUploadInterrupted": ntxTrapOVAUploadInterrupted,
       "ntxTrapCVMOrPrismCentralVMRAMUsageHigh": ntxTrapCVMOrPrismCentralVMRAMUsageHigh,
       "ntxTrapPrismCentralVMCPULoadHigh": ntxTrapPrismCentralVMCPULoadHigh,
       "ntxTrapPrismCentralVMDiskUsageHigh": ntxTrapPrismCentralVMDiskUsageHigh,
       "ntxTrapPrismCentralVMSystemRootPartitionSpaceUsageHigh": ntxTrapPrismCentralVMSystemRootPartitionSpaceUsageHigh,
       "ntxTrapPrismCentralVMLimitCheck": ntxTrapPrismCentralVMLimitCheck,
       "ntxTrapCoreDumpsAreEnabledOnThisCVMOrPrismCentralVM": ntxTrapCoreDumpsAreEnabledOnThisCVMOrPrismCentralVM,
       "ntxTrapClusterDoesNotSupportSynchronousReplication": ntxTrapClusterDoesNotSupportSynchronousReplication,
       "ntxTrapPrismCentralVMHomePartitionDiskUsageHigh": ntxTrapPrismCentralVMHomePartitionDiskUsageHigh,
       "ntxTrapFilesLicenseInvalid": ntxTrapFilesLicenseInvalid,
       "ntxTrapSATAControllerStatusIsBad": ntxTrapSATAControllerStatusIsBad,
       "ntxTrapFileSystemInconsistenciesAreDetected": ntxTrapFileSystemInconsistenciesAreDetected,
       "ntxTrapSameTimezoneCheck": ntxTrapSameTimezoneCheck,
       "ntxTrapStoragePoolSpaceUsageExceededTheConfiguredThreshold": ntxTrapStoragePoolSpaceUsageExceededTheConfiguredThreshold,
       "ntxTrapHypervisorDiskUsageIsAboveTheRecommendedThreshold": ntxTrapHypervisorDiskUsageIsAboveTheRecommendedThreshold,
       "ntxTrapInvalidSSDHDDDriveCombination": ntxTrapInvalidSSDHDDDriveCombination,
       "ntxTrapNodeMaintenanceModeFailure": ntxTrapNodeMaintenanceModeFailure,
       "ntxTrapDiskFailedMarkedOffline": ntxTrapDiskFailedMarkedOffline,
       "ntxTrapVirtualIPCheck": ntxTrapVirtualIPCheck,
       "ntxTrapInsufficientHostBandwidth": ntxTrapInsufficientHostBandwidth,
       "ntxTrapOrphanedVSSCopiesAreDetected": ntxTrapOrphanedVSSCopiesAreDetected,
       "ntxTrapStorageContainerSpaceUsageExceeded": ntxTrapStorageContainerSpaceUsageExceeded,
       "ntxTrapTwoNodeClusterStateChanged": ntxTrapTwoNodeClusterStateChanged,
       "ntxTrapStateChangedForTwoNodeCluster": ntxTrapStateChangedForTwoNodeCluster,
       "ntxTrapInsufficientSpaceForUVMsDeployedOnPC": ntxTrapInsufficientSpaceForUVMsDeployedOnPC,
       "ntxTrapLicensingWorkflowIsIncomplete": ntxTrapLicensingWorkflowIsIncomplete,
       "ntxTrapInconsistentBridgevSwitchConfiguration": ntxTrapInconsistentBridgevSwitchConfiguration,
       "ntxTrapPowerCycleVMsBeforePerformingUpgradeOrMigrateOperation": ntxTrapPowerCycleVMsBeforePerformingUpgradeOrMigrateOperation,
       "ntxTrapStorageContainersIsareNotMountedOnAllNodes": ntxTrapStorageContainersIsareNotMountedOnAllNodes,
       "ntxTrapVMRecoveryStorageContainersIsareNotMountedOnAllHosts": ntxTrapVMRecoveryStorageContainersIsareNotMountedOnAllHosts,
       "ntxTrapFlowPolicyhitLoggingIsNotFunctional": ntxTrapFlowPolicyhitLoggingIsNotFunctional,
       "ntxTrapEpochSaaSServiceConnectivityLost": ntxTrapEpochSaaSServiceConnectivityLost,
       "ntxTrapIDFirewallLostConnectivityToDomainController": ntxTrapIDFirewallLostConnectivityToDomainController,
       "ntxTrapEpochDataCollectorUpgradeAvailable": ntxTrapEpochDataCollectorUpgradeAvailable,
       "ntxTrapA803005": ntxTrapA803005,
       "ntxTrapIDFirewallUnableToLocateMappedActiveDirectoryObject": ntxTrapIDFirewallUnableToLocateMappedActiveDirectoryObject,
       "ntxTrapSkippedReplicationOfSnapshotForProtectionDomain": ntxTrapSkippedReplicationOfSnapshotForProtectionDomain,
       "ntxTrapInconsistentFileGroupsInTheSystem": ntxTrapInconsistentFileGroupsInTheSystem,
       "ntxTrapVMRestorationFailed": ntxTrapVMRestorationFailed,
       "ntxTrapMetadataServiceRestartingFrequentlyDueToLongGCPauses": ntxTrapMetadataServiceRestartingFrequentlyDueToLongGCPauses,
       "ntxTrapA130206": ntxTrapA130206,
       "ntxTrapSomeOfTheVMsInTheRecoveryPlanAreUnprotected": ntxTrapSomeOfTheVMsInTheRecoveryPlanAreUnprotected,
       "ntxTrapRemoteSiteIsIncompatibleForReplication": ntxTrapRemoteSiteIsIncompatibleForReplication,
       "ntxTrapFileServerContainerHasUnexpectedFiles": ntxTrapFileServerContainerHasUnexpectedFiles,
       "ntxTrapControllerVMTimeNotSynchronizedWithExternalServers": ntxTrapControllerVMTimeNotSynchronizedWithExternalServers,
       "ntxTrapHypervisorTimeNotSynchronisedWithAnyExternalServers": ntxTrapHypervisorTimeNotSynchronisedWithAnyExternalServers,
       "ntxTrapA110454": ntxTrapA110454,
       "ntxTrapNearSyncReplicationOfProtectionDomainHasNotProgressed": ntxTrapNearSyncReplicationOfProtectionDomainHasNotProgressed,
       "ntxTrapPrismCentralVMTypeOrAnnotationNotSet": ntxTrapPrismCentralVMTypeOrAnnotationNotSet,
       "ntxTrapA200309": ntxTrapA200309,
       "ntxTrapPrismCentralVCPUAvailabilityCheck": ntxTrapPrismCentralVCPUAvailabilityCheck,
       "ntxTrapPrismCentralMemoryAvailabilityCheck": ntxTrapPrismCentralMemoryAvailabilityCheck,
       "ntxTrapPrismCentralUpgradesAreDisabledOncvmip": ntxTrapPrismCentralUpgradesAreDisabledOncvmip,
       "ntxTrapHighNumberOfCorrectableUECCErrorsFound": ntxTrapHighNumberOfCorrectableUECCErrorsFound,
       "ntxTrapTemperatureOfRAIDCardIsOutOfAboveThreshold": ntxTrapTemperatureOfRAIDCardIsOutOfAboveThreshold,
       "ntxTrapCVMIPAddressIsUnreachable": ntxTrapCVMIPAddressIsUnreachable,
       "ntxTrapA1191": ntxTrapA1191,
       "ntxTrapDegradedRecoveryPoint": ntxTrapDegradedRecoveryPoint,
       "ntxTrapDIMMHPPRFailureEventFound": ntxTrapDIMMHPPRFailureEventFound,
       "ntxTrapM60GPUConfigurationIncorrectOnTheNode": ntxTrapM60GPUConfigurationIncorrectOnTheNode,
       "ntxTrapM10GPUConfigurationIncorrectOnTheNode": ntxTrapM10GPUConfigurationIncorrectOnTheNode,
       "ntxTrapHostBootDiskRequiresAttention": ntxTrapHostBootDiskRequiresAttention,
       "ntxTrapA130177": ntxTrapA130177,
       "ntxTrapA130173": ntxTrapA130173,
       "ntxTrapProtectionDomainActivationFailed": ntxTrapProtectionDomainActivationFailed,
       "ntxTrapAssociatedEntitiesAreNotProtectedTogether": ntxTrapAssociatedEntitiesAreNotProtectedTogether,
       "ntxTrapEntityConflictInConsistencyGroups": ntxTrapEntityConflictInConsistencyGroups,
       "ntxTrapVMSyncRepContainerNotFound": ntxTrapVMSyncRepContainerNotFound,
       "ntxTrapRemoteSiteIsUnreachable": ntxTrapRemoteSiteIsUnreachable,
       "ntxTrapNFSMetadataUsageHigh": ntxTrapNFSMetadataUsageHigh,
       "ntxTrapSSDTierSizeIsSmallOnOneOrMoreNodes": ntxTrapSSDTierSizeIsSmallOnOneOrMoreNodes,
       "ntxTrapClusterIsSusceptibleToCopyUpBlockMapIssue": ntxTrapClusterIsSusceptibleToCopyUpBlockMapIssue,
       "ntxTrapMemoryOvercommitFailure": ntxTrapMemoryOvercommitFailure,
       "ntxTrapProtectedVMIsNotCapableOfBackupAndRecovery": ntxTrapProtectedVMIsNotCapableOfBackupAndRecovery,
       "ntxTrapProtectedVMsNotFound": ntxTrapProtectedVMsNotFound,
       "ntxTrapDuplicateDiskIDsPresentInDifferentNodesOfTheSameCluster": ntxTrapDuplicateDiskIDsPresentInDifferentNodesOfTheSameCluster,
       "ntxTrapRecoveryPointExpiredPriorToStartOfReplication": ntxTrapRecoveryPointExpiredPriorToStartOfReplication,
       "ntxTrapTooManySnapshotsInTheSystem": ntxTrapTooManySnapshotsInTheSystem,
       "ntxTrapA150003": ntxTrapA150003,
       "ntxTrapInvalidRoutesReceivedFromOnpremVPNGateway": ntxTrapInvalidRoutesReceivedFromOnpremVPNGateway,
       "ntxTrapVMRenamedOnRestoration": ntxTrapVMRenamedOnRestoration,
       "ntxTrapSecondaryProtectionDomainsNotInSyncWithPrimary": ntxTrapSecondaryProtectionDomainsNotInSyncWithPrimary,
       "ntxTrapMetroConnectivityLost": ntxTrapMetroConnectivityLost,
       "ntxTrapNodeRemovalStuck": ntxTrapNodeRemovalStuck,
       "ntxTrapVGSyncRepContainerNotFound": ntxTrapVGSyncRepContainerNotFound,
       "ntxTrapLatestSnapshotOfProtectionDomainIsMissingEntities": ntxTrapLatestSnapshotOfProtectionDomainIsMissingEntities}
)
