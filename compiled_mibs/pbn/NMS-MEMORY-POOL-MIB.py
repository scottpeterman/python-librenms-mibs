# SNMP MIB module (NMS-MEMORY-POOL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\pbn\NMS-MEMORY-POOL-MIB.mib
# Produced by pysmi-1.6.2 at Thu Oct  2 12:20:33 2025
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

(Percent,) = mibBuilder.importSymbols(
    "NMS-QOS-PIB-MIB",
    "Percent")

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

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


# MODULE-IDENTITY

nmsMemoryPoolMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48)
)
if mibBuilder.loadTexts:
    nmsMemoryPoolMIB.setRevisions(
        ("2003-10-16 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NmsMemoryPoolUtilization_Type = Percent
_NmsMemoryPoolUtilization_Object = MibScalar
nmsMemoryPoolUtilization = _NmsMemoryPoolUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 1),
    _NmsMemoryPoolUtilization_Type()
)
nmsMemoryPoolUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMemoryPoolUtilization.setStatus("current")
_NmsMemoryPoolTotalMemorySize_Type = Unsigned32
_NmsMemoryPoolTotalMemorySize_Object = MibScalar
nmsMemoryPoolTotalMemorySize = _NmsMemoryPoolTotalMemorySize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 2),
    _NmsMemoryPoolTotalMemorySize_Type()
)
nmsMemoryPoolTotalMemorySize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMemoryPoolTotalMemorySize.setStatus("current")
_NmsMemoryPoolImageRatio_Type = Percent
_NmsMemoryPoolImageRatio_Object = MibScalar
nmsMemoryPoolImageRatio = _NmsMemoryPoolImageRatio_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 3),
    _NmsMemoryPoolImageRatio_Type()
)
nmsMemoryPoolImageRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMemoryPoolImageRatio.setStatus("current")
_NmsMemoryPoolRegionRatio_Type = Percent
_NmsMemoryPoolRegionRatio_Object = MibScalar
nmsMemoryPoolRegionRatio = _NmsMemoryPoolRegionRatio_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 4),
    _NmsMemoryPoolRegionRatio_Type()
)
nmsMemoryPoolRegionRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMemoryPoolRegionRatio.setStatus("current")
_NmsMemoryPoolHeapRatio_Type = Percent
_NmsMemoryPoolHeapRatio_Object = MibScalar
nmsMemoryPoolHeapRatio = _NmsMemoryPoolHeapRatio_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 5),
    _NmsMemoryPoolHeapRatio_Type()
)
nmsMemoryPoolHeapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMemoryPoolHeapRatio.setStatus("current")
_NmsMemoryPoolHeapUtilization_Type = Percent
_NmsMemoryPoolHeapUtilization_Object = MibScalar
nmsMemoryPoolHeapUtilization = _NmsMemoryPoolHeapUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 6),
    _NmsMemoryPoolHeapUtilization_Type()
)
nmsMemoryPoolHeapUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMemoryPoolHeapUtilization.setStatus("current")
_NmsMemoryPoolMessageBufferRatio_Type = Percent
_NmsMemoryPoolMessageBufferRatio_Object = MibScalar
nmsMemoryPoolMessageBufferRatio = _NmsMemoryPoolMessageBufferRatio_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 7),
    _NmsMemoryPoolMessageBufferRatio_Type()
)
nmsMemoryPoolMessageBufferRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMemoryPoolMessageBufferRatio.setStatus("current")
_NmsMemoryPoolMessageBufferUtilization_Type = Percent
_NmsMemoryPoolMessageBufferUtilization_Object = MibScalar
nmsMemoryPoolMessageBufferUtilization = _NmsMemoryPoolMessageBufferUtilization_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 8),
    _NmsMemoryPoolMessageBufferUtilization_Type()
)
nmsMemoryPoolMessageBufferUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMemoryPoolMessageBufferUtilization.setStatus("current")
_NmsMemoryPoolTotalFlashSize_Type = Percent
_NmsMemoryPoolTotalFlashSize_Object = MibScalar
nmsMemoryPoolTotalFlashSize = _NmsMemoryPoolTotalFlashSize_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 9),
    _NmsMemoryPoolTotalFlashSize_Type()
)
nmsMemoryPoolTotalFlashSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nmsMemoryPoolTotalFlashSize.setStatus("current")
_NmsMemoryPoolNotifications_ObjectIdentity = ObjectIdentity
nmsMemoryPoolNotifications = _NmsMemoryPoolNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 20)
)
_NmsMemoryPoolConformance_ObjectIdentity = ObjectIdentity
nmsMemoryPoolConformance = _NmsMemoryPoolConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 21)
)
_NmsMemoryPoolCompliances_ObjectIdentity = ObjectIdentity
nmsMemoryPoolCompliances = _NmsMemoryPoolCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 21, 1)
)
_NmsMemoryPoolGroups_ObjectIdentity = ObjectIdentity
nmsMemoryPoolGroups = _NmsMemoryPoolGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 21, 2)
)

# Managed Objects groups

nmsMemoryPoolGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 21, 2, 1)
)
nmsMemoryPoolGroup.setObjects(
      *(("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolName"),
        ("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolAlternate"),
        ("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolValid"),
        ("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolUsed"),
        ("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolFree"),
        ("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolLargestFree"))
)
if mibBuilder.loadTexts:
    nmsMemoryPoolGroup.setStatus("current")

nmsMemoryPoolUtilizationGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 21, 2, 2)
)
nmsMemoryPoolUtilizationGroup.setObjects(
      *(("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolUtilization1Min"),
        ("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolUtilization5Min"),
        ("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolUtilization10Min"))
)
if mibBuilder.loadTexts:
    nmsMemoryPoolUtilizationGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nmsMemoryPoolCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 21, 1, 1)
)
nmsMemoryPoolCompliance.setObjects(
    ("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolGroup")
)
if mibBuilder.loadTexts:
    nmsMemoryPoolCompliance.setStatus(
        "deprecated"
    )

nmsMemoryPoolComplianceRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3320, 9, 48, 21, 1, 2)
)
nmsMemoryPoolComplianceRev1.setObjects(
      *(("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolGroup"),
        ("NMS-MEMORY-POOL-MIB", "nmsMemoryPoolUtilizationGroup"))
)
if mibBuilder.loadTexts:
    nmsMemoryPoolComplianceRev1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NMS-MEMORY-POOL-MIB",
    **{"nmsMemoryPoolMIB": nmsMemoryPoolMIB,
       "nmsMemoryPoolUtilization": nmsMemoryPoolUtilization,
       "nmsMemoryPoolTotalMemorySize": nmsMemoryPoolTotalMemorySize,
       "nmsMemoryPoolImageRatio": nmsMemoryPoolImageRatio,
       "nmsMemoryPoolRegionRatio": nmsMemoryPoolRegionRatio,
       "nmsMemoryPoolHeapRatio": nmsMemoryPoolHeapRatio,
       "nmsMemoryPoolHeapUtilization": nmsMemoryPoolHeapUtilization,
       "nmsMemoryPoolMessageBufferRatio": nmsMemoryPoolMessageBufferRatio,
       "nmsMemoryPoolMessageBufferUtilization": nmsMemoryPoolMessageBufferUtilization,
       "nmsMemoryPoolTotalFlashSize": nmsMemoryPoolTotalFlashSize,
       "nmsMemoryPoolNotifications": nmsMemoryPoolNotifications,
       "nmsMemoryPoolConformance": nmsMemoryPoolConformance,
       "nmsMemoryPoolCompliances": nmsMemoryPoolCompliances,
       "nmsMemoryPoolCompliance": nmsMemoryPoolCompliance,
       "nmsMemoryPoolComplianceRev1": nmsMemoryPoolComplianceRev1,
       "nmsMemoryPoolGroups": nmsMemoryPoolGroups,
       "nmsMemoryPoolGroup": nmsMemoryPoolGroup,
       "nmsMemoryPoolUtilizationGroup": nmsMemoryPoolUtilizationGroup}
)
