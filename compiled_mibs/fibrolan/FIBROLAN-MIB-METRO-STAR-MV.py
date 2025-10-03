# SNMP MIB module (FIBROLAN-MIB-METRO-STAR-MV) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-METRO-STAR-MV
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:19 2025
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

flMetroStarMv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500)
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
_FlMsSnmpMIBConformance_ObjectIdentity = ObjectIdentity
flMsSnmpMIBConformance = _FlMsSnmpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 1)
)
_FlMsSnmpMIBCompliances_ObjectIdentity = ObjectIdentity
flMsSnmpMIBCompliances = _FlMsSnmpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 1, 1)
)
_FlMsSnmpMIBGroups_ObjectIdentity = ObjectIdentity
flMsSnmpMIBGroups = _FlMsSnmpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 1, 2)
)
_FlMsChassisMv_ObjectIdentity = ObjectIdentity
flMsChassisMv = _FlMsChassisMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10)
)
_FlMsChassisPsuMvTable_Object = MibTable
flMsChassisPsuMvTable = _FlMsChassisPsuMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 10)
)
if mibBuilder.loadTexts:
    flMsChassisPsuMvTable.setStatus("current")
_FlMsChassisPsuMvEntry_Object = MibTableRow
flMsChassisPsuMvEntry = _FlMsChassisPsuMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 10, 1)
)
flMsChassisPsuMvEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisPsuMvIndex"),
)
if mibBuilder.loadTexts:
    flMsChassisPsuMvEntry.setStatus("current")


class _FlMsChassisPsuMvIndex_Type(Integer32):
    """Custom type flMsChassisPsuMvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FlMsChassisPsuMvIndex_Type.__name__ = "Integer32"
_FlMsChassisPsuMvIndex_Object = MibTableColumn
flMsChassisPsuMvIndex = _FlMsChassisPsuMvIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 10, 1, 1),
    _FlMsChassisPsuMvIndex_Type()
)
flMsChassisPsuMvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisPsuMvIndex.setStatus("current")


class _FlMsChassisPsuMvStatus_Type(Integer32):
    """Custom type flMsChassisPsuMvStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("ok", 2),
          ("notInstalled", 3))
    )


_FlMsChassisPsuMvStatus_Type.__name__ = "Integer32"
_FlMsChassisPsuMvStatus_Object = MibTableColumn
flMsChassisPsuMvStatus = _FlMsChassisPsuMvStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 10, 1, 2),
    _FlMsChassisPsuMvStatus_Type()
)
flMsChassisPsuMvStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisPsuMvStatus.setStatus("current")
_FlMsChassisModuleMvTable_Object = MibTable
flMsChassisModuleMvTable = _FlMsChassisModuleMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20)
)
if mibBuilder.loadTexts:
    flMsChassisModuleMvTable.setStatus("current")
_FlMsChassisModuleMvEntry_Object = MibTableRow
flMsChassisModuleMvEntry = _FlMsChassisModuleMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1)
)
flMsChassisModuleMvEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
)
if mibBuilder.loadTexts:
    flMsChassisModuleMvEntry.setStatus("current")


class _FlMsChassisModuleMvIndex_Type(Integer32):
    """Custom type flMsChassisModuleMvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_FlMsChassisModuleMvIndex_Type.__name__ = "Integer32"
_FlMsChassisModuleMvIndex_Object = MibTableColumn
flMsChassisModuleMvIndex = _FlMsChassisModuleMvIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 1),
    _FlMsChassisModuleMvIndex_Type()
)
flMsChassisModuleMvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleMvIndex.setStatus("current")


class _FlMsChassisModuleMvType_Type(Integer32):
    """Custom type flMsChassisModuleMvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              29,
              30,
              31,
              32,
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
              9999)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("mcm100-02", 1),
          ("mcm110-02", 2),
          ("mcm100-01", 3),
          ("mcm1000s", 4),
          ("mcm1000t", 5),
          ("mcm110-01", 6),
          ("acm110-12", 7),
          ("acm110-14", 8),
          ("mcm100-rl", 9),
          ("msm100u", 10),
          ("mcm100-1e1", 11),
          ("mcm100-2e1", 12),
          ("mdx41", 13),
          ("mdx81", 14),
          ("msm622u", 15),
          ("pcm110-8e1", 16),
          ("pcm110-4e1", 17),
          ("pcm110-8t1", 18),
          ("pcm110-4t1", 19),
          ("mcm1000x-rl", 20),
          ("mcm1000x", 21),
          ("mcm100-1t1", 22),
          ("mcm100-2t1", 23),
          ("msm2500u", 24),
          ("mcm1000x-rl-4e1", 25),
          ("mcm1000x-rl-4t1", 26),
          ("mdx21", 27),
          ("mddx51", 28),
          ("mdx81-e", 29),
          ("mdx41-sfa", 30),
          ("mdx41-sfb", 31),
          ("fadm1-47", 32),
          ("fadm1-49", 33),
          ("fadm1-51", 34),
          ("fadm1-53", 35),
          ("fadm1-55", 36),
          ("fadm1-57", 37),
          ("fadm1-59", 38),
          ("fadm1-61", 39),
          ("fadm2-47", 40),
          ("fadm2-49", 41),
          ("fadm2-51", 42),
          ("fadm2-53", 43),
          ("fadm2-55", 44),
          ("fadm2-57", 45),
          ("fadm2-59", 46),
          ("fadm2-61", 47),
          ("none", 9999))
    )


_FlMsChassisModuleMvType_Type.__name__ = "Integer32"
_FlMsChassisModuleMvType_Object = MibTableColumn
flMsChassisModuleMvType = _FlMsChassisModuleMvType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 2),
    _FlMsChassisModuleMvType_Type()
)
flMsChassisModuleMvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleMvType.setStatus("current")
_FlMsChassisModuleMvRevision_Type = DisplayString
_FlMsChassisModuleMvRevision_Object = MibTableColumn
flMsChassisModuleMvRevision = _FlMsChassisModuleMvRevision_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 3),
    _FlMsChassisModuleMvRevision_Type()
)
flMsChassisModuleMvRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleMvRevision.setStatus("current")


class _FlMsChassisModuleMvReset_Type(Integer32):
    """Custom type flMsChassisModuleMvReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("reset", 2))
    )


_FlMsChassisModuleMvReset_Type.__name__ = "Integer32"
_FlMsChassisModuleMvReset_Object = MibTableColumn
flMsChassisModuleMvReset = _FlMsChassisModuleMvReset_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 4),
    _FlMsChassisModuleMvReset_Type()
)
flMsChassisModuleMvReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisModuleMvReset.setStatus("current")


class _FlMsChassisModuleMvRestoreDef_Type(Integer32):
    """Custom type flMsChassisModuleMvRestoreDef based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("restoreDefaults", 2))
    )


_FlMsChassisModuleMvRestoreDef_Type.__name__ = "Integer32"
_FlMsChassisModuleMvRestoreDef_Object = MibTableColumn
flMsChassisModuleMvRestoreDef = _FlMsChassisModuleMvRestoreDef_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 5),
    _FlMsChassisModuleMvRestoreDef_Type()
)
flMsChassisModuleMvRestoreDef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisModuleMvRestoreDef.setStatus("current")
_FlMsChassisModuleMvSerialNumber_Type = DisplayString
_FlMsChassisModuleMvSerialNumber_Object = MibTableColumn
flMsChassisModuleMvSerialNumber = _FlMsChassisModuleMvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 6),
    _FlMsChassisModuleMvSerialNumber_Type()
)
flMsChassisModuleMvSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleMvSerialNumber.setStatus("current")
_FlMsChassisModuleMvDeviceType_Type = DisplayString
_FlMsChassisModuleMvDeviceType_Object = MibTableColumn
flMsChassisModuleMvDeviceType = _FlMsChassisModuleMvDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 7),
    _FlMsChassisModuleMvDeviceType_Type()
)
flMsChassisModuleMvDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleMvDeviceType.setStatus("current")
_FlMsChassisModuleMvHwRevision_Type = DisplayString
_FlMsChassisModuleMvHwRevision_Object = MibTableColumn
flMsChassisModuleMvHwRevision = _FlMsChassisModuleMvHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 8),
    _FlMsChassisModuleMvHwRevision_Type()
)
flMsChassisModuleMvHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleMvHwRevision.setStatus("current")
_FlMsChassisModuleMvFoDescription1_Type = DisplayString
_FlMsChassisModuleMvFoDescription1_Object = MibTableColumn
flMsChassisModuleMvFoDescription1 = _FlMsChassisModuleMvFoDescription1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 9),
    _FlMsChassisModuleMvFoDescription1_Type()
)
flMsChassisModuleMvFoDescription1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleMvFoDescription1.setStatus("current")
_FlMsChassisModuleMvFoDescription2_Type = DisplayString
_FlMsChassisModuleMvFoDescription2_Object = MibTableColumn
flMsChassisModuleMvFoDescription2 = _FlMsChassisModuleMvFoDescription2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 20, 1, 10),
    _FlMsChassisModuleMvFoDescription2_Type()
)
flMsChassisModuleMvFoDescription2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisModuleMvFoDescription2.setStatus("current")
_FlMsChassisMvConfirm_Type = DisplayString
_FlMsChassisMvConfirm_Object = MibScalar
flMsChassisMvConfirm = _FlMsChassisMvConfirm_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 1000),
    _FlMsChassisMvConfirm_Type()
)
flMsChassisMvConfirm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisMvConfirm.setStatus("current")


class _FlMsChassisMvRebootSystem_Type(Integer32):
    """Custom type flMsChassisMvRebootSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reboot", 2))
    )


_FlMsChassisMvRebootSystem_Type.__name__ = "Integer32"
_FlMsChassisMvRebootSystem_Object = MibScalar
flMsChassisMvRebootSystem = _FlMsChassisMvRebootSystem_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 1001),
    _FlMsChassisMvRebootSystem_Type()
)
flMsChassisMvRebootSystem.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisMvRebootSystem.setStatus("current")
_FlMsChassisMvTable_Object = MibTable
flMsChassisMvTable = _FlMsChassisMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 20)
)
if mibBuilder.loadTexts:
    flMsChassisMvTable.setStatus("current")
_FlMsChassisMvEntry_Object = MibTableRow
flMsChassisMvEntry = _FlMsChassisMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 20, 1)
)
flMsChassisMvEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
)
if mibBuilder.loadTexts:
    flMsChassisMvEntry.setStatus("current")


class _FlMsChassisMvIndex_Type(Integer32):
    """Custom type flMsChassisMvIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_FlMsChassisMvIndex_Type.__name__ = "Integer32"
_FlMsChassisMvIndex_Object = MibTableColumn
flMsChassisMvIndex = _FlMsChassisMvIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 20, 1, 1),
    _FlMsChassisMvIndex_Type()
)
flMsChassisMvIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisMvIndex.setStatus("current")


class _FlMsChassisMvType_Type(Integer32):
    """Custom type flMsChassisMvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("mmm01", 1),
          ("mmm02", 2),
          ("mmm03", 3),
          ("notAvailable", 9999))
    )


_FlMsChassisMvType_Type.__name__ = "Integer32"
_FlMsChassisMvType_Object = MibTableColumn
flMsChassisMvType = _FlMsChassisMvType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 20, 1, 2),
    _FlMsChassisMvType_Type()
)
flMsChassisMvType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisMvType.setStatus("current")


class _FlMsChassisMvRole_Type(Integer32):
    """Custom type flMsChassisMvRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("standAlone", 1),
          ("slave", 2),
          ("stanbyMaster", 3),
          ("activeMaster", 4),
          ("notAvailable", 9999))
    )


_FlMsChassisMvRole_Type.__name__ = "Integer32"
_FlMsChassisMvRole_Object = MibTableColumn
flMsChassisMvRole = _FlMsChassisMvRole_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 20, 1, 3),
    _FlMsChassisMvRole_Type()
)
flMsChassisMvRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisMvRole.setStatus("current")
_FlMsChassisMvTemperature_Type = Integer32
_FlMsChassisMvTemperature_Object = MibTableColumn
flMsChassisMvTemperature = _FlMsChassisMvTemperature_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 20, 1, 4),
    _FlMsChassisMvTemperature_Type()
)
flMsChassisMvTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisMvTemperature.setStatus("current")
_FlMsChassisMvSoftwareVer_Type = DisplayString
_FlMsChassisMvSoftwareVer_Object = MibTableColumn
flMsChassisMvSoftwareVer = _FlMsChassisMvSoftwareVer_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 20, 1, 5),
    _FlMsChassisMvSoftwareVer_Type()
)
flMsChassisMvSoftwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisMvSoftwareVer.setStatus("current")
_FlMsChassisMvSwDownloadTable_Object = MibTable
flMsChassisMvSwDownloadTable = _FlMsChassisMvSwDownloadTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30)
)
if mibBuilder.loadTexts:
    flMsChassisMvSwDownloadTable.setStatus("current")
_FlMsChassisMvSwDownloadEntry_Object = MibTableRow
flMsChassisMvSwDownloadEntry = _FlMsChassisMvSwDownloadEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1)
)
flMsChassisMvSwDownloadEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadTableIndex"),
)
if mibBuilder.loadTexts:
    flMsChassisMvSwDownloadEntry.setStatus("current")


class _FlMsMvSwDownloadTableIndex_Type(Integer32):
    """Custom type flMsMvSwDownloadTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 11),
    )


_FlMsMvSwDownloadTableIndex_Type.__name__ = "Integer32"
_FlMsMvSwDownloadTableIndex_Object = MibTableColumn
flMsMvSwDownloadTableIndex = _FlMsMvSwDownloadTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 1),
    _FlMsMvSwDownloadTableIndex_Type()
)
flMsMvSwDownloadTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsMvSwDownloadTableIndex.setStatus("current")
_FlMsMvSwDownloadTftpServer_Type = IpAddress
_FlMsMvSwDownloadTftpServer_Object = MibTableColumn
flMsMvSwDownloadTftpServer = _FlMsMvSwDownloadTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 2),
    _FlMsMvSwDownloadTftpServer_Type()
)
flMsMvSwDownloadTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMvSwDownloadTftpServer.setStatus("current")
_FlMsMvSwDownloadCurrentVersion_Type = DisplayString
_FlMsMvSwDownloadCurrentVersion_Object = MibTableColumn
flMsMvSwDownloadCurrentVersion = _FlMsMvSwDownloadCurrentVersion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 3),
    _FlMsMvSwDownloadCurrentVersion_Type()
)
flMsMvSwDownloadCurrentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsMvSwDownloadCurrentVersion.setStatus("current")
_FlMsMvSwDownloadRollbackVersion_Type = DisplayString
_FlMsMvSwDownloadRollbackVersion_Object = MibTableColumn
flMsMvSwDownloadRollbackVersion = _FlMsMvSwDownloadRollbackVersion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 4),
    _FlMsMvSwDownloadRollbackVersion_Type()
)
flMsMvSwDownloadRollbackVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsMvSwDownloadRollbackVersion.setStatus("current")
_FlMsMvSwDownloadNewVersion_Type = DisplayString
_FlMsMvSwDownloadNewVersion_Object = MibTableColumn
flMsMvSwDownloadNewVersion = _FlMsMvSwDownloadNewVersion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 5),
    _FlMsMvSwDownloadNewVersion_Type()
)
flMsMvSwDownloadNewVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMvSwDownloadNewVersion.setStatus("current")
_FlMsMvSwDownloadRemoteFileName_Type = DisplayString
_FlMsMvSwDownloadRemoteFileName_Object = MibTableColumn
flMsMvSwDownloadRemoteFileName = _FlMsMvSwDownloadRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 6),
    _FlMsMvSwDownloadRemoteFileName_Type()
)
flMsMvSwDownloadRemoteFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsMvSwDownloadRemoteFileName.setStatus("current")
_FlMsMvSwDownloadRemotePath_Type = DisplayString
_FlMsMvSwDownloadRemotePath_Object = MibTableColumn
flMsMvSwDownloadRemotePath = _FlMsMvSwDownloadRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 7),
    _FlMsMvSwDownloadRemotePath_Type()
)
flMsMvSwDownloadRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMvSwDownloadRemotePath.setStatus("current")


class _FlMsMvSwDownloadAutoReboot_Type(Integer32):
    """Custom type flMsMvSwDownloadAutoReboot based on Integer32"""
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


_FlMsMvSwDownloadAutoReboot_Type.__name__ = "Integer32"
_FlMsMvSwDownloadAutoReboot_Object = MibTableColumn
flMsMvSwDownloadAutoReboot = _FlMsMvSwDownloadAutoReboot_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 8),
    _FlMsMvSwDownloadAutoReboot_Type()
)
flMsMvSwDownloadAutoReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMvSwDownloadAutoReboot.setStatus("current")


class _FlMsMvSwDownloadProcessBegin_Type(Integer32):
    """Custom type flMsMvSwDownloadProcessBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("upgrade", 2))
    )


_FlMsMvSwDownloadProcessBegin_Type.__name__ = "Integer32"
_FlMsMvSwDownloadProcessBegin_Object = MibTableColumn
flMsMvSwDownloadProcessBegin = _FlMsMvSwDownloadProcessBegin_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 9),
    _FlMsMvSwDownloadProcessBegin_Type()
)
flMsMvSwDownloadProcessBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMvSwDownloadProcessBegin.setStatus("current")


class _FlMsMvSwDownloadRollback_Type(Integer32):
    """Custom type flMsMvSwDownloadRollback based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("rollback", 2))
    )


_FlMsMvSwDownloadRollback_Type.__name__ = "Integer32"
_FlMsMvSwDownloadRollback_Object = MibTableColumn
flMsMvSwDownloadRollback = _FlMsMvSwDownloadRollback_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 10),
    _FlMsMvSwDownloadRollback_Type()
)
flMsMvSwDownloadRollback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsMvSwDownloadRollback.setStatus("current")


class _FlMsMvSwDownloadProcessStatus_Type(Integer32):
    """Custom type flMsMvSwDownloadProcessStatus based on Integer32"""
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
        *(("notStarted", 1),
          ("upgradeFailed", 2),
          ("upgradeComplete", 3),
          ("retrievingFile", 4),
          ("erasingFlash", 5),
          ("programmingFlash", 6),
          ("verifyingFlash", 7),
          ("rollbackInProgress", 8),
          ("rollbackComplete", 9))
    )


_FlMsMvSwDownloadProcessStatus_Type.__name__ = "Integer32"
_FlMsMvSwDownloadProcessStatus_Object = MibTableColumn
flMsMvSwDownloadProcessStatus = _FlMsMvSwDownloadProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 30, 1, 11),
    _FlMsMvSwDownloadProcessStatus_Type()
)
flMsMvSwDownloadProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsMvSwDownloadProcessStatus.setStatus("current")
_FlMsChassisMvConfigUploadTable_Object = MibTable
flMsChassisMvConfigUploadTable = _FlMsChassisMvConfigUploadTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 40)
)
if mibBuilder.loadTexts:
    flMsChassisMvConfigUploadTable.setStatus("current")
_FlMsChassisMvConfigUploadEntry_Object = MibTableRow
flMsChassisMvConfigUploadEntry = _FlMsChassisMvConfigUploadEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 40, 1)
)
flMsChassisMvConfigUploadEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvConfigUploadIndex"),
)
if mibBuilder.loadTexts:
    flMsChassisMvConfigUploadEntry.setStatus("current")


class _FlMsChassisMvConfigUploadIndex_Type(Integer32):
    """Custom type flMsChassisMvConfigUploadIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_FlMsChassisMvConfigUploadIndex_Type.__name__ = "Integer32"
_FlMsChassisMvConfigUploadIndex_Object = MibTableColumn
flMsChassisMvConfigUploadIndex = _FlMsChassisMvConfigUploadIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 40, 1, 1),
    _FlMsChassisMvConfigUploadIndex_Type()
)
flMsChassisMvConfigUploadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisMvConfigUploadIndex.setStatus("current")
_FlMsChassisMvUploadTftpServer_Type = IpAddress
_FlMsChassisMvUploadTftpServer_Object = MibTableColumn
flMsChassisMvUploadTftpServer = _FlMsChassisMvUploadTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 40, 1, 2),
    _FlMsChassisMvUploadTftpServer_Type()
)
flMsChassisMvUploadTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisMvUploadTftpServer.setStatus("current")
_FlMsChassisMvUploadFileName_Type = DisplayString
_FlMsChassisMvUploadFileName_Object = MibTableColumn
flMsChassisMvUploadFileName = _FlMsChassisMvUploadFileName_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 40, 1, 3),
    _FlMsChassisMvUploadFileName_Type()
)
flMsChassisMvUploadFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisMvUploadFileName.setStatus("current")


class _FlMsChassisMvUploadFileStatus_Type(Integer32):
    """Custom type flMsChassisMvUploadFileStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notLoaded", 1),
          ("loaded", 2))
    )


_FlMsChassisMvUploadFileStatus_Type.__name__ = "Integer32"
_FlMsChassisMvUploadFileStatus_Object = MibTableColumn
flMsChassisMvUploadFileStatus = _FlMsChassisMvUploadFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 40, 1, 4),
    _FlMsChassisMvUploadFileStatus_Type()
)
flMsChassisMvUploadFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisMvUploadFileStatus.setStatus("current")
_FlMsChassisMvUploadRemotePath_Type = DisplayString
_FlMsChassisMvUploadRemotePath_Object = MibTableColumn
flMsChassisMvUploadRemotePath = _FlMsChassisMvUploadRemotePath_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 40, 1, 5),
    _FlMsChassisMvUploadRemotePath_Type()
)
flMsChassisMvUploadRemotePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisMvUploadRemotePath.setStatus("current")


class _FlMsChassisMvUploadProcessBegin_Type(Integer32):
    """Custom type flMsChassisMvUploadProcessBegin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("uploadConfig", 2))
    )


_FlMsChassisMvUploadProcessBegin_Type.__name__ = "Integer32"
_FlMsChassisMvUploadProcessBegin_Object = MibTableColumn
flMsChassisMvUploadProcessBegin = _FlMsChassisMvUploadProcessBegin_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 40, 1, 6),
    _FlMsChassisMvUploadProcessBegin_Type()
)
flMsChassisMvUploadProcessBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMsChassisMvUploadProcessBegin.setStatus("current")


class _FlMsChassisMvUploadProcessStatus_Type(Integer32):
    """Custom type flMsChassisMvUploadProcessStatus based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("uploadNotStarted", 1),
          ("fileLoadInProcess", 2),
          ("fileLoadFailed", 3),
          ("fileLoadComplete", 4),
          ("configInProgress", 5),
          ("configLoadedOk", 6),
          ("partiallyConfigured", 7),
          ("configFailed", 8))
    )


_FlMsChassisMvUploadProcessStatus_Type.__name__ = "Integer32"
_FlMsChassisMvUploadProcessStatus_Object = MibTableColumn
flMsChassisMvUploadProcessStatus = _FlMsChassisMvUploadProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 40, 1, 7),
    _FlMsChassisMvUploadProcessStatus_Type()
)
flMsChassisMvUploadProcessStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMsChassisMvUploadProcessStatus.setStatus("current")

# Managed Objects groups

flMsChassisGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 1, 2, 1)
)
flMsChassisGroup.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvType"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvRole"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvTemperature"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvSoftwareVer"))
)
if mibBuilder.loadTexts:
    flMsChassisGroup.setStatus("current")

flMsChassisPsuGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 1, 2, 2)
)
flMsChassisPsuGroup.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisPsuMvIndex"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisPsuMvStatus"))
)
if mibBuilder.loadTexts:
    flMsChassisPsuGroup.setStatus("current")

flMsChassisModulesGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 1, 2, 3)
)
flMsChassisModulesGroup.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvType"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvRevision"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvReset"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvRestoreDef"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvSerialNumber"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvDeviceType"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvHwRevision"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvFoDescription1"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvFoDescription2"))
)
if mibBuilder.loadTexts:
    flMsChassisModulesGroup.setStatus("current")

flMsChassisSwUpgradeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 1, 2, 4)
)
flMsChassisSwUpgradeGroup.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadTableIndex"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadTftpServer"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadCurrentVersion"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadRollbackVersion"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadNewVersion"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadRemoteFileName"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadRemotePath"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadAutoReboot"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadProcessBegin"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadRollback"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsMvSwDownloadProcessStatus"))
)
if mibBuilder.loadTexts:
    flMsChassisSwUpgradeGroup.setStatus("current")

flMsChassisUploadConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 1, 2, 5)
)
flMsChassisUploadConfigGroup.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvConfigUploadIndex"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvUploadTftpServer"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvUploadFileName"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvUploadFileStatus"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvUploadRemotePath"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvUploadProcessBegin"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvUploadProcessStatus"))
)
if mibBuilder.loadTexts:
    flMsChassisUploadConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flMsSnmpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 1, 1, 1)
)
flMsSnmpMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisGroup"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisPsuGroup"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModulesGroup"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisSwUpgradeGroup"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisUploadConfigGroup"))
)
if mibBuilder.loadTexts:
    flMsSnmpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-METRO-STAR-MV",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsSnmpMIBConformance": flMsSnmpMIBConformance,
       "flMsSnmpMIBCompliances": flMsSnmpMIBCompliances,
       "flMsSnmpMIBCompliance": flMsSnmpMIBCompliance,
       "flMsSnmpMIBGroups": flMsSnmpMIBGroups,
       "flMsChassisGroup": flMsChassisGroup,
       "flMsChassisPsuGroup": flMsChassisPsuGroup,
       "flMsChassisModulesGroup": flMsChassisModulesGroup,
       "flMsChassisSwUpgradeGroup": flMsChassisSwUpgradeGroup,
       "flMsChassisUploadConfigGroup": flMsChassisUploadConfigGroup,
       "flMsChassisMv": flMsChassisMv,
       "flMsChassisPsuMvTable": flMsChassisPsuMvTable,
       "flMsChassisPsuMvEntry": flMsChassisPsuMvEntry,
       "flMsChassisPsuMvIndex": flMsChassisPsuMvIndex,
       "flMsChassisPsuMvStatus": flMsChassisPsuMvStatus,
       "flMsChassisModuleMvTable": flMsChassisModuleMvTable,
       "flMsChassisModuleMvEntry": flMsChassisModuleMvEntry,
       "flMsChassisModuleMvIndex": flMsChassisModuleMvIndex,
       "flMsChassisModuleMvType": flMsChassisModuleMvType,
       "flMsChassisModuleMvRevision": flMsChassisModuleMvRevision,
       "flMsChassisModuleMvReset": flMsChassisModuleMvReset,
       "flMsChassisModuleMvRestoreDef": flMsChassisModuleMvRestoreDef,
       "flMsChassisModuleMvSerialNumber": flMsChassisModuleMvSerialNumber,
       "flMsChassisModuleMvDeviceType": flMsChassisModuleMvDeviceType,
       "flMsChassisModuleMvHwRevision": flMsChassisModuleMvHwRevision,
       "flMsChassisModuleMvFoDescription1": flMsChassisModuleMvFoDescription1,
       "flMsChassisModuleMvFoDescription2": flMsChassisModuleMvFoDescription2,
       "flMsChassisMvConfirm": flMsChassisMvConfirm,
       "flMsChassisMvRebootSystem": flMsChassisMvRebootSystem,
       "flMsChassisMvTable": flMsChassisMvTable,
       "flMsChassisMvEntry": flMsChassisMvEntry,
       "flMsChassisMvIndex": flMsChassisMvIndex,
       "flMsChassisMvType": flMsChassisMvType,
       "flMsChassisMvRole": flMsChassisMvRole,
       "flMsChassisMvTemperature": flMsChassisMvTemperature,
       "flMsChassisMvSoftwareVer": flMsChassisMvSoftwareVer,
       "flMsChassisMvSwDownloadTable": flMsChassisMvSwDownloadTable,
       "flMsChassisMvSwDownloadEntry": flMsChassisMvSwDownloadEntry,
       "flMsMvSwDownloadTableIndex": flMsMvSwDownloadTableIndex,
       "flMsMvSwDownloadTftpServer": flMsMvSwDownloadTftpServer,
       "flMsMvSwDownloadCurrentVersion": flMsMvSwDownloadCurrentVersion,
       "flMsMvSwDownloadRollbackVersion": flMsMvSwDownloadRollbackVersion,
       "flMsMvSwDownloadNewVersion": flMsMvSwDownloadNewVersion,
       "flMsMvSwDownloadRemoteFileName": flMsMvSwDownloadRemoteFileName,
       "flMsMvSwDownloadRemotePath": flMsMvSwDownloadRemotePath,
       "flMsMvSwDownloadAutoReboot": flMsMvSwDownloadAutoReboot,
       "flMsMvSwDownloadProcessBegin": flMsMvSwDownloadProcessBegin,
       "flMsMvSwDownloadRollback": flMsMvSwDownloadRollback,
       "flMsMvSwDownloadProcessStatus": flMsMvSwDownloadProcessStatus,
       "flMsChassisMvConfigUploadTable": flMsChassisMvConfigUploadTable,
       "flMsChassisMvConfigUploadEntry": flMsChassisMvConfigUploadEntry,
       "flMsChassisMvConfigUploadIndex": flMsChassisMvConfigUploadIndex,
       "flMsChassisMvUploadTftpServer": flMsChassisMvUploadTftpServer,
       "flMsChassisMvUploadFileName": flMsChassisMvUploadFileName,
       "flMsChassisMvUploadFileStatus": flMsChassisMvUploadFileStatus,
       "flMsChassisMvUploadRemotePath": flMsChassisMvUploadRemotePath,
       "flMsChassisMvUploadProcessBegin": flMsChassisMvUploadProcessBegin,
       "flMsChassisMvUploadProcessStatus": flMsChassisMvUploadProcessStatus}
)
