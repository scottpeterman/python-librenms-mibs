# SNMP MIB module (FIBROLAN-MIB-MSM622U) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-MSM622U
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:27 2025
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

(flMsChassisModuleMvEntry,) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-METRO-STAR-MV",
    "flMsChassisModuleMvEntry")

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

flMsm622UMv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 140)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fibrolan_ObjectIdentity = ObjectIdentity
fibrolan = _Fibrolan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467)
)
_FibrolanSNMP_ObjectIdentity = ObjectIdentity
fibrolanSNMP = _FibrolanSNMP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100)
)
_FlMetroStarMv_ObjectIdentity = ObjectIdentity
flMetroStarMv = _FlMetroStarMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500)
)
_FlMsChassisMv_ObjectIdentity = ObjectIdentity
flMsChassisMv = _FlMsChassisMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10)
)
_FlMsModuleMv_ObjectIdentity = ObjectIdentity
flMsModuleMv = _FlMsModuleMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30)
)
_FlMsm622UModuleMv_ObjectIdentity = ObjectIdentity
flMsm622UModuleMv = _FlMsm622UModuleMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 140, 1)
)
_FlMsm622UModuleExtMvTable_Object = MibTable
flMsm622UModuleExtMvTable = _FlMsm622UModuleExtMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 140, 1, 1)
)
if mibBuilder.loadTexts:
    flMsm622UModuleExtMvTable.setStatus("current")
_FlMcm100UModuleExtMvEntry_Object = MibTableRow
flMcm100UModuleExtMvEntry = _FlMcm100UModuleExtMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 140, 1, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm100UModuleExtMvEntry.setStatus("current")


class _FlMsm622UModuleExtMvSignalDetectP1_Type(Integer32):
    """Custom type flMsm622UModuleExtMvSignalDetectP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsm622UModuleExtMvSignalDetectP1_Type.__name__ = "Integer32"
_FlMsm622UModuleExtMvSignalDetectP1_Object = MibTableColumn
flMsm622UModuleExtMvSignalDetectP1 = _FlMsm622UModuleExtMvSignalDetectP1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 140, 1, 1, 1, 1),
    _FlMsm622UModuleExtMvSignalDetectP1_Type()
)
flMsm622UModuleExtMvSignalDetectP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsm622UModuleExtMvSignalDetectP1.setStatus("current")


class _FlMsm622UModuleExtMvSignalDetectP2_Type(Integer32):
    """Custom type flMsm622UModuleExtMvSignalDetectP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsm622UModuleExtMvSignalDetectP2_Type.__name__ = "Integer32"
_FlMsm622UModuleExtMvSignalDetectP2_Object = MibTableColumn
flMsm622UModuleExtMvSignalDetectP2 = _FlMsm622UModuleExtMvSignalDetectP2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 140, 1, 1, 1, 2),
    _FlMsm622UModuleExtMvSignalDetectP2_Type()
)
flMsm622UModuleExtMvSignalDetectP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsm622UModuleExtMvSignalDetectP2.setStatus("current")


class _FlMsm622UModuleExtMvLoopbackP1_Type(Integer32):
    """Custom type flMsm622UModuleExtMvLoopbackP1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsm622UModuleExtMvLoopbackP1_Type.__name__ = "Integer32"
_FlMsm622UModuleExtMvLoopbackP1_Object = MibTableColumn
flMsm622UModuleExtMvLoopbackP1 = _FlMsm622UModuleExtMvLoopbackP1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 140, 1, 1, 1, 3),
    _FlMsm622UModuleExtMvLoopbackP1_Type()
)
flMsm622UModuleExtMvLoopbackP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsm622UModuleExtMvLoopbackP1.setStatus("current")


class _FlMsm622UModuleExtMvLoopbackP2_Type(Integer32):
    """Custom type flMsm622UModuleExtMvLoopbackP2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsm622UModuleExtMvLoopbackP2_Type.__name__ = "Integer32"
_FlMsm622UModuleExtMvLoopbackP2_Object = MibTableColumn
flMsm622UModuleExtMvLoopbackP2 = _FlMsm622UModuleExtMvLoopbackP2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 140, 1, 1, 1, 4),
    _FlMsm622UModuleExtMvLoopbackP2_Type()
)
flMsm622UModuleExtMvLoopbackP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsm622UModuleExtMvLoopbackP2.setStatus("current")


class _FlMsm622UModuleExtMvEnableMode_Type(Integer32):
    """Custom type flMsm622UModuleExtMvEnableMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_FlMsm622UModuleExtMvEnableMode_Type.__name__ = "Integer32"
_FlMsm622UModuleExtMvEnableMode_Object = MibTableColumn
flMsm622UModuleExtMvEnableMode = _FlMsm622UModuleExtMvEnableMode_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 140, 1, 1, 1, 5),
    _FlMsm622UModuleExtMvEnableMode_Type()
)
flMsm622UModuleExtMvEnableMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsm622UModuleExtMvEnableMode.setStatus("current")
flMsChassisModuleMvEntry.registerAugmentions(
    ("FIBROLAN-MIB-MSM622U",
     "flMcm100UModuleExtMvEntry")
)
flMcm100UModuleExtMvEntry.setIndexNames(*flMsChassisModuleMvEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-MSM622U",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsChassisMv": flMsChassisMv,
       "flMsModuleMv": flMsModuleMv,
       "flMsm622UMv": flMsm622UMv,
       "flMsm622UModuleMv": flMsm622UModuleMv,
       "flMsm622UModuleExtMvTable": flMsm622UModuleExtMvTable,
       "flMcm100UModuleExtMvEntry": flMcm100UModuleExtMvEntry,
       "flMsm622UModuleExtMvSignalDetectP1": flMsm622UModuleExtMvSignalDetectP1,
       "flMsm622UModuleExtMvSignalDetectP2": flMsm622UModuleExtMvSignalDetectP2,
       "flMsm622UModuleExtMvLoopbackP1": flMsm622UModuleExtMvLoopbackP1,
       "flMsm622UModuleExtMvLoopbackP2": flMsm622UModuleExtMvLoopbackP2,
       "flMsm622UModuleExtMvEnableMode": flMsm622UModuleExtMvEnableMode}
)
