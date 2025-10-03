# SNMP MIB module (FIBROLAN-MIB-MSM2500U) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-MSM2500U
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

flMsm2500UMv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 160)
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
_FlMsm2500UModuleMv_ObjectIdentity = ObjectIdentity
flMsm2500UModuleMv = _FlMsm2500UModuleMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 160, 1)
)
_FlMsm2500UModuleExtMvTable_Object = MibTable
flMsm2500UModuleExtMvTable = _FlMsm2500UModuleExtMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 160, 1, 1)
)
if mibBuilder.loadTexts:
    flMsm2500UModuleExtMvTable.setStatus("current")
_FlMcm2500UModuleExtMvEntry_Object = MibTableRow
flMcm2500UModuleExtMvEntry = _FlMcm2500UModuleExtMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 160, 1, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm2500UModuleExtMvEntry.setStatus("current")


class _FlMsm2500UModuleExtMvSignalDetectP1_Type(Integer32):
    """Custom type flMsm2500UModuleExtMvSignalDetectP1 based on Integer32"""
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


_FlMsm2500UModuleExtMvSignalDetectP1_Type.__name__ = "Integer32"
_FlMsm2500UModuleExtMvSignalDetectP1_Object = MibTableColumn
flMsm2500UModuleExtMvSignalDetectP1 = _FlMsm2500UModuleExtMvSignalDetectP1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 160, 1, 1, 1, 1),
    _FlMsm2500UModuleExtMvSignalDetectP1_Type()
)
flMsm2500UModuleExtMvSignalDetectP1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsm2500UModuleExtMvSignalDetectP1.setStatus("current")


class _FlMsm2500UModuleExtMvSignalDetectP2_Type(Integer32):
    """Custom type flMsm2500UModuleExtMvSignalDetectP2 based on Integer32"""
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


_FlMsm2500UModuleExtMvSignalDetectP2_Type.__name__ = "Integer32"
_FlMsm2500UModuleExtMvSignalDetectP2_Object = MibTableColumn
flMsm2500UModuleExtMvSignalDetectP2 = _FlMsm2500UModuleExtMvSignalDetectP2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 160, 1, 1, 1, 2),
    _FlMsm2500UModuleExtMvSignalDetectP2_Type()
)
flMsm2500UModuleExtMvSignalDetectP2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsm2500UModuleExtMvSignalDetectP2.setStatus("current")


class _FlMsm2500UModuleExtMvEnableModeP1_Type(Integer32):
    """Custom type flMsm2500UModuleExtMvEnableModeP1 based on Integer32"""
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


_FlMsm2500UModuleExtMvEnableModeP1_Type.__name__ = "Integer32"
_FlMsm2500UModuleExtMvEnableModeP1_Object = MibTableColumn
flMsm2500UModuleExtMvEnableModeP1 = _FlMsm2500UModuleExtMvEnableModeP1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 160, 1, 1, 1, 3),
    _FlMsm2500UModuleExtMvEnableModeP1_Type()
)
flMsm2500UModuleExtMvEnableModeP1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsm2500UModuleExtMvEnableModeP1.setStatus("current")


class _FlMsm2500UModuleExtMvEnableModeP2_Type(Integer32):
    """Custom type flMsm2500UModuleExtMvEnableModeP2 based on Integer32"""
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


_FlMsm2500UModuleExtMvEnableModeP2_Type.__name__ = "Integer32"
_FlMsm2500UModuleExtMvEnableModeP2_Object = MibTableColumn
flMsm2500UModuleExtMvEnableModeP2 = _FlMsm2500UModuleExtMvEnableModeP2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 160, 1, 1, 1, 4),
    _FlMsm2500UModuleExtMvEnableModeP2_Type()
)
flMsm2500UModuleExtMvEnableModeP2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsm2500UModuleExtMvEnableModeP2.setStatus("current")
_FlMsm2500UModuleExtMvDescription_Type = DisplayString
_FlMsm2500UModuleExtMvDescription_Object = MibTableColumn
flMsm2500UModuleExtMvDescription = _FlMsm2500UModuleExtMvDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 160, 1, 1, 1, 5),
    _FlMsm2500UModuleExtMvDescription_Type()
)
flMsm2500UModuleExtMvDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsm2500UModuleExtMvDescription.setStatus("current")
flMsChassisModuleMvEntry.registerAugmentions(
    ("FIBROLAN-MIB-MSM2500U",
     "flMcm2500UModuleExtMvEntry")
)
flMcm2500UModuleExtMvEntry.setIndexNames(*flMsChassisModuleMvEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-MSM2500U",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsChassisMv": flMsChassisMv,
       "flMsModuleMv": flMsModuleMv,
       "flMsm2500UMv": flMsm2500UMv,
       "flMsm2500UModuleMv": flMsm2500UModuleMv,
       "flMsm2500UModuleExtMvTable": flMsm2500UModuleExtMvTable,
       "flMcm2500UModuleExtMvEntry": flMcm2500UModuleExtMvEntry,
       "flMsm2500UModuleExtMvSignalDetectP1": flMsm2500UModuleExtMvSignalDetectP1,
       "flMsm2500UModuleExtMvSignalDetectP2": flMsm2500UModuleExtMvSignalDetectP2,
       "flMsm2500UModuleExtMvEnableModeP1": flMsm2500UModuleExtMvEnableModeP1,
       "flMsm2500UModuleExtMvEnableModeP2": flMsm2500UModuleExtMvEnableModeP2,
       "flMsm2500UModuleExtMvDescription": flMsm2500UModuleExtMvDescription}
)
