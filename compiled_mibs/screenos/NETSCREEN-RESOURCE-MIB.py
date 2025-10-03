# SNMP MIB module (NETSCREEN-RESOURCE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\screenos\NETSCREEN-RESOURCE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 12:25:34 2025
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

(netscreenResource,) = mibBuilder.importSymbols(
    "NETSCREEN-SMI",
    "netscreenResource")

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


# MODULE-IDENTITY

netscreenResourceMibModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 16, 0)
)
if mibBuilder.loadTexts:
    netscreenResourceMibModule.setRevisions(
        ("2004-05-03 00:00",
         "2004-03-03 00:00",
         "2003-11-10 00:00",
         "2002-05-05 00:00",
         "2001-04-30 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NsResCPU_ObjectIdentity = ObjectIdentity
nsResCPU = _NsResCPU_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1)
)
_NsResCpuAvg_Type = Integer32
_NsResCpuAvg_Object = MibScalar
nsResCpuAvg = _NsResCpuAvg_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1, 1),
    _NsResCpuAvg_Type()
)
nsResCpuAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResCpuAvg.setStatus("current")
_NsResCpuLast1Min_Type = Integer32
_NsResCpuLast1Min_Object = MibScalar
nsResCpuLast1Min = _NsResCpuLast1Min_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1, 2),
    _NsResCpuLast1Min_Type()
)
nsResCpuLast1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResCpuLast1Min.setStatus("current")
_NsResCpuLast5Min_Type = Integer32
_NsResCpuLast5Min_Object = MibScalar
nsResCpuLast5Min = _NsResCpuLast5Min_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1, 3),
    _NsResCpuLast5Min_Type()
)
nsResCpuLast5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResCpuLast5Min.setStatus("current")
_NsResCpuLast15Min_Type = Integer32
_NsResCpuLast15Min_Object = MibScalar
nsResCpuLast15Min = _NsResCpuLast15Min_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 1, 4),
    _NsResCpuLast15Min_Type()
)
nsResCpuLast15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResCpuLast15Min.setStatus("current")
_NsResMem_ObjectIdentity = ObjectIdentity
nsResMem = _NsResMem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 16, 2)
)
_NsResMemAllocate_Type = Integer32
_NsResMemAllocate_Object = MibScalar
nsResMemAllocate = _NsResMemAllocate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 2, 1),
    _NsResMemAllocate_Type()
)
nsResMemAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResMemAllocate.setStatus("current")
_NsResMemLeft_Type = Integer32
_NsResMemLeft_Object = MibScalar
nsResMemLeft = _NsResMemLeft_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 2, 2),
    _NsResMemLeft_Type()
)
nsResMemLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResMemLeft.setStatus("current")
_NsResMemFrag_Type = Integer32
_NsResMemFrag_Object = MibScalar
nsResMemFrag = _NsResMemFrag_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 2, 3),
    _NsResMemFrag_Type()
)
nsResMemFrag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResMemFrag.setStatus("current")
_NsResSession_ObjectIdentity = ObjectIdentity
nsResSession = _NsResSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3224, 16, 3)
)
_NsResSessAllocate_Type = Integer32
_NsResSessAllocate_Object = MibScalar
nsResSessAllocate = _NsResSessAllocate_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 3, 2),
    _NsResSessAllocate_Type()
)
nsResSessAllocate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResSessAllocate.setStatus("current")
_NsResSessMaxium_Type = Integer32
_NsResSessMaxium_Object = MibScalar
nsResSessMaxium = _NsResSessMaxium_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 3, 3),
    _NsResSessMaxium_Type()
)
nsResSessMaxium.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResSessMaxium.setStatus("current")
_NsResSessFailed_Type = Integer32
_NsResSessFailed_Object = MibScalar
nsResSessFailed = _NsResSessFailed_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 3, 4),
    _NsResSessFailed_Type()
)
nsResSessFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResSessFailed.setStatus("current")
_NsResModTable_Object = MibTable
nsResModTable = _NsResModTable_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4)
)
if mibBuilder.loadTexts:
    nsResModTable.setStatus("mandatory")
_NsResModEntry_Object = MibTableRow
nsResModEntry = _NsResModEntry_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1)
)
nsResModEntry.setIndexNames(
    (0, "NETSCREEN-RESOURCE-MIB", "nsResModModId"),
    (0, "NETSCREEN-RESOURCE-MIB", "nsResModCpuId"),
)
if mibBuilder.loadTexts:
    nsResModEntry.setStatus("mandatory")


class _NsResModModId_Type(Integer32):
    """Custom type nsResModModId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_NsResModModId_Type.__name__ = "Integer32"
_NsResModModId_Object = MibTableColumn
nsResModModId = _NsResModModId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 1),
    _NsResModModId_Type()
)
nsResModModId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModModId.setStatus("mandatory")


class _NsResModCpuId_Type(Integer32):
    """Custom type nsResModCpuId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_NsResModCpuId_Type.__name__ = "Integer32"
_NsResModCpuId_Object = MibTableColumn
nsResModCpuId = _NsResModCpuId_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 2),
    _NsResModCpuId_Type()
)
nsResModCpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModCpuId.setStatus("mandatory")


class _NsResModCpuCurr_Type(Integer32):
    """Custom type nsResModCpuCurr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NsResModCpuCurr_Type.__name__ = "Integer32"
_NsResModCpuCurr_Object = MibTableColumn
nsResModCpuCurr = _NsResModCpuCurr_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 3),
    _NsResModCpuCurr_Type()
)
nsResModCpuCurr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModCpuCurr.setStatus("mandatory")


class _NsResModCpuLast1Min_Type(Integer32):
    """Custom type nsResModCpuLast1Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NsResModCpuLast1Min_Type.__name__ = "Integer32"
_NsResModCpuLast1Min_Object = MibTableColumn
nsResModCpuLast1Min = _NsResModCpuLast1Min_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 4),
    _NsResModCpuLast1Min_Type()
)
nsResModCpuLast1Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModCpuLast1Min.setStatus("mandatory")


class _NsResModCpuLast5Min_Type(Integer32):
    """Custom type nsResModCpuLast5Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NsResModCpuLast5Min_Type.__name__ = "Integer32"
_NsResModCpuLast5Min_Object = MibTableColumn
nsResModCpuLast5Min = _NsResModCpuLast5Min_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 5),
    _NsResModCpuLast5Min_Type()
)
nsResModCpuLast5Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModCpuLast5Min.setStatus("mandatory")


class _NsResModCpuLast15Min_Type(Integer32):
    """Custom type nsResModCpuLast15Min based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_NsResModCpuLast15Min_Type.__name__ = "Integer32"
_NsResModCpuLast15Min_Object = MibTableColumn
nsResModCpuLast15Min = _NsResModCpuLast15Min_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 6),
    _NsResModCpuLast15Min_Type()
)
nsResModCpuLast15Min.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModCpuLast15Min.setStatus("mandatory")
_NsResModMemAllocated_Type = Integer32
_NsResModMemAllocated_Object = MibTableColumn
nsResModMemAllocated = _NsResModMemAllocated_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 7),
    _NsResModMemAllocated_Type()
)
nsResModMemAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModMemAllocated.setStatus("mandatory")
_NsResModMemLeft_Type = Integer32
_NsResModMemLeft_Object = MibTableColumn
nsResModMemLeft = _NsResModMemLeft_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 8),
    _NsResModMemLeft_Type()
)
nsResModMemLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModMemLeft.setStatus("mandatory")
_NsResModSessAllocated_Type = Integer32
_NsResModSessAllocated_Object = MibTableColumn
nsResModSessAllocated = _NsResModSessAllocated_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 9),
    _NsResModSessAllocated_Type()
)
nsResModSessAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModSessAllocated.setStatus("mandatory")
_NsResModSessMaximum_Type = Integer32
_NsResModSessMaximum_Object = MibTableColumn
nsResModSessMaximum = _NsResModSessMaximum_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 10),
    _NsResModSessMaximum_Type()
)
nsResModSessMaximum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModSessMaximum.setStatus("mandatory")
_NsResModSessFailed_Type = Integer32
_NsResModSessFailed_Object = MibTableColumn
nsResModSessFailed = _NsResModSessFailed_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 11),
    _NsResModSessFailed_Type()
)
nsResModSessFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModSessFailed.setStatus("mandatory")
_NsResModThresholdMem_Type = Integer32
_NsResModThresholdMem_Object = MibTableColumn
nsResModThresholdMem = _NsResModThresholdMem_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 12),
    _NsResModThresholdMem_Type()
)
nsResModThresholdMem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModThresholdMem.setStatus("mandatory")
_NsResModThresholdCpu_Type = Integer32
_NsResModThresholdCpu_Object = MibTableColumn
nsResModThresholdCpu = _NsResModThresholdCpu_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 13),
    _NsResModThresholdCpu_Type()
)
nsResModThresholdCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModThresholdCpu.setStatus("mandatory")
_NsResModThresholdSession_Type = Integer32
_NsResModThresholdSession_Object = MibTableColumn
nsResModThresholdSession = _NsResModThresholdSession_Object(
    (1, 3, 6, 1, 4, 1, 3224, 16, 4, 1, 14),
    _NsResModThresholdSession_Type()
)
nsResModThresholdSession.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nsResModThresholdSession.setStatus("mandatory")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETSCREEN-RESOURCE-MIB",
    **{"netscreenResourceMibModule": netscreenResourceMibModule,
       "nsResCPU": nsResCPU,
       "nsResCpuAvg": nsResCpuAvg,
       "nsResCpuLast1Min": nsResCpuLast1Min,
       "nsResCpuLast5Min": nsResCpuLast5Min,
       "nsResCpuLast15Min": nsResCpuLast15Min,
       "nsResMem": nsResMem,
       "nsResMemAllocate": nsResMemAllocate,
       "nsResMemLeft": nsResMemLeft,
       "nsResMemFrag": nsResMemFrag,
       "nsResSession": nsResSession,
       "nsResSessAllocate": nsResSessAllocate,
       "nsResSessMaxium": nsResSessMaxium,
       "nsResSessFailed": nsResSessFailed,
       "nsResModTable": nsResModTable,
       "nsResModEntry": nsResModEntry,
       "nsResModModId": nsResModModId,
       "nsResModCpuId": nsResModCpuId,
       "nsResModCpuCurr": nsResModCpuCurr,
       "nsResModCpuLast1Min": nsResModCpuLast1Min,
       "nsResModCpuLast5Min": nsResModCpuLast5Min,
       "nsResModCpuLast15Min": nsResModCpuLast15Min,
       "nsResModMemAllocated": nsResModMemAllocated,
       "nsResModMemLeft": nsResModMemLeft,
       "nsResModSessAllocated": nsResModSessAllocated,
       "nsResModSessMaximum": nsResModSessMaximum,
       "nsResModSessFailed": nsResModSessFailed,
       "nsResModThresholdMem": nsResModThresholdMem,
       "nsResModThresholdCpu": nsResModThresholdCpu,
       "nsResModThresholdSession": nsResModThresholdSession}
)
