# SNMP MIB module (FIBROLAN-MIB-MCM1xx) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-MCM1xx
# Produced by pysmi-1.6.2 at Thu Oct  2 11:44:25 2025
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

(flMsModuleMvChannelEntry,
 flMsModuleMvLinkEntry) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-MSMODULE",
    "flMsModuleMvChannelEntry",
    "flMsModuleMvLinkEntry")

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

flMcm1xxMv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100)
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
_FlMsMcm1xxMIBConformance_ObjectIdentity = ObjectIdentity
flMsMcm1xxMIBConformance = _FlMsMcm1xxMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 1)
)
_FlMsMcm1xxMIBCompliances_ObjectIdentity = ObjectIdentity
flMsMcm1xxMIBCompliances = _FlMsMcm1xxMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 1, 1)
)
_FlMsMcm1xxMIBGroups_ObjectIdentity = ObjectIdentity
flMsMcm1xxMIBGroups = _FlMsMcm1xxMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 1, 2)
)
_FlMcm1xxModuleMv_ObjectIdentity = ObjectIdentity
flMcm1xxModuleMv = _FlMcm1xxModuleMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 10)
)
_FlMcm1xxModuleExtMvTable_Object = MibTable
flMcm1xxModuleExtMvTable = _FlMcm1xxModuleExtMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 10, 1)
)
if mibBuilder.loadTexts:
    flMcm1xxModuleExtMvTable.setStatus("current")
_FlMcm1xxModuleExtMvEntry_Object = MibTableRow
flMcm1xxModuleExtMvEntry = _FlMcm1xxModuleExtMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 10, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm1xxModuleExtMvEntry.setStatus("current")


class _FlMcm1xxModuleExtMvRedundantMod_Type(Integer32):
    """Custom type flMcm1xxModuleExtMvRedundantMod based on Integer32"""
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


_FlMcm1xxModuleExtMvRedundantMod_Type.__name__ = "Integer32"
_FlMcm1xxModuleExtMvRedundantMod_Object = MibTableColumn
flMcm1xxModuleExtMvRedundantMod = _FlMcm1xxModuleExtMvRedundantMod_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 10, 1, 1, 1),
    _FlMcm1xxModuleExtMvRedundantMod_Type()
)
flMcm1xxModuleExtMvRedundantMod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxModuleExtMvRedundantMod.setStatus("current")
_FlMcm1xxChannelsMv_ObjectIdentity = ObjectIdentity
flMcm1xxChannelsMv = _FlMcm1xxChannelsMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20)
)
_FlMcm1xxChannelExtMvTable_Object = MibTable
flMcm1xxChannelExtMvTable = _FlMcm1xxChannelExtMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1)
)
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvTable.setStatus("current")
_FlMcm1xxChannelExtMvEntry_Object = MibTableRow
flMcm1xxChannelExtMvEntry = _FlMcm1xxChannelExtMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvEntry.setStatus("current")


class _FlMcm1xxChannelExtMvTpLink_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvTpLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2),
          ("killed", 3))
    )


_FlMcm1xxChannelExtMvTpLink_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvTpLink_Object = MibTableColumn
flMcm1xxChannelExtMvTpLink = _FlMcm1xxChannelExtMvTpLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 1),
    _FlMcm1xxChannelExtMvTpLink_Type()
)
flMcm1xxChannelExtMvTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvTpLink.setStatus("current")


class _FlMcm1xxChannelExtMvFoLink_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvFoLink based on Integer32"""
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


_FlMcm1xxChannelExtMvFoLink_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvFoLink_Object = MibTableColumn
flMcm1xxChannelExtMvFoLink = _FlMcm1xxChannelExtMvFoLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 2),
    _FlMcm1xxChannelExtMvFoLink_Type()
)
flMcm1xxChannelExtMvFoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvFoLink.setStatus("current")
_FlMcm1xxChannelExtMvPortDescription_Type = DisplayString
_FlMcm1xxChannelExtMvPortDescription_Object = MibTableColumn
flMcm1xxChannelExtMvPortDescription = _FlMcm1xxChannelExtMvPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 3),
    _FlMcm1xxChannelExtMvPortDescription_Type()
)
flMcm1xxChannelExtMvPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvPortDescription.setStatus("current")


class _FlMcm1xxChannelExtMvDuplex_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hdx", 1),
          ("fdx", 2),
          ("n-a", 3))
    )


_FlMcm1xxChannelExtMvDuplex_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvDuplex_Object = MibTableColumn
flMcm1xxChannelExtMvDuplex = _FlMcm1xxChannelExtMvDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 4),
    _FlMcm1xxChannelExtMvDuplex_Type()
)
flMcm1xxChannelExtMvDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvDuplex.setStatus("current")


class _FlMcm1xxChannelExtMvEnableTpPort_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvEnableTpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlMcm1xxChannelExtMvEnableTpPort_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvEnableTpPort_Object = MibTableColumn
flMcm1xxChannelExtMvEnableTpPort = _FlMcm1xxChannelExtMvEnableTpPort_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 5),
    _FlMcm1xxChannelExtMvEnableTpPort_Type()
)
flMcm1xxChannelExtMvEnableTpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvEnableTpPort.setStatus("current")


class _FlMcm1xxChannelExtMvTp2FoFp_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvTp2FoFp based on Integer32"""
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


_FlMcm1xxChannelExtMvTp2FoFp_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvTp2FoFp_Object = MibTableColumn
flMcm1xxChannelExtMvTp2FoFp = _FlMcm1xxChannelExtMvTp2FoFp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 6),
    _FlMcm1xxChannelExtMvTp2FoFp_Type()
)
flMcm1xxChannelExtMvTp2FoFp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvTp2FoFp.setStatus("current")


class _FlMcm1xxChannelExtMvFo2TpFp_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvFo2TpFp based on Integer32"""
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


_FlMcm1xxChannelExtMvFo2TpFp_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvFo2TpFp_Object = MibTableColumn
flMcm1xxChannelExtMvFo2TpFp = _FlMcm1xxChannelExtMvFo2TpFp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 7),
    _FlMcm1xxChannelExtMvFo2TpFp_Type()
)
flMcm1xxChannelExtMvFo2TpFp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvFo2TpFp.setStatus("current")


class _FlMcm1xxChannelExtMvAutoNego_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvAutoNego based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_FlMcm1xxChannelExtMvAutoNego_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvAutoNego_Object = MibTableColumn
flMcm1xxChannelExtMvAutoNego = _FlMcm1xxChannelExtMvAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 8),
    _FlMcm1xxChannelExtMvAutoNego_Type()
)
flMcm1xxChannelExtMvAutoNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvAutoNego.setStatus("current")


class _FlMcm1xxChannelExtMvDatarate_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvDatarate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("m10", 1),
          ("m100", 2),
          ("n-a", 3))
    )


_FlMcm1xxChannelExtMvDatarate_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvDatarate_Object = MibTableColumn
flMcm1xxChannelExtMvDatarate = _FlMcm1xxChannelExtMvDatarate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 9),
    _FlMcm1xxChannelExtMvDatarate_Type()
)
flMcm1xxChannelExtMvDatarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvDatarate.setStatus("current")


class _FlMcm1xxChannelExtMvTpBckp2Main_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvTpBckp2Main based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sec0", 1),
          ("sec1", 2),
          ("sec5", 3),
          ("sec10", 4),
          ("sec20", 5),
          ("never", 7))
    )


_FlMcm1xxChannelExtMvTpBckp2Main_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvTpBckp2Main_Object = MibTableColumn
flMcm1xxChannelExtMvTpBckp2Main = _FlMcm1xxChannelExtMvTpBckp2Main_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 10),
    _FlMcm1xxChannelExtMvTpBckp2Main_Type()
)
flMcm1xxChannelExtMvTpBckp2Main.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvTpBckp2Main.setStatus("current")


class _FlMcm1xxChannelExtMvFoBckp2Main_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvFoBckp2Main based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("sec0", 1),
          ("sec1", 2),
          ("sec5", 3),
          ("sec10", 4),
          ("sec20", 5),
          ("never", 7))
    )


_FlMcm1xxChannelExtMvFoBckp2Main_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvFoBckp2Main_Object = MibTableColumn
flMcm1xxChannelExtMvFoBckp2Main = _FlMcm1xxChannelExtMvFoBckp2Main_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 11),
    _FlMcm1xxChannelExtMvFoBckp2Main_Type()
)
flMcm1xxChannelExtMvFoBckp2Main.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvFoBckp2Main.setStatus("current")


class _FlMcm1xxChannelExtMvForceTp_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvForceTp based on Integer32"""
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


_FlMcm1xxChannelExtMvForceTp_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvForceTp_Object = MibTableColumn
flMcm1xxChannelExtMvForceTp = _FlMcm1xxChannelExtMvForceTp_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 12),
    _FlMcm1xxChannelExtMvForceTp_Type()
)
flMcm1xxChannelExtMvForceTp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvForceTp.setStatus("current")


class _FlMcm1xxChannelExtMvForceFo_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvForceFo based on Integer32"""
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


_FlMcm1xxChannelExtMvForceFo_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvForceFo_Object = MibTableColumn
flMcm1xxChannelExtMvForceFo = _FlMcm1xxChannelExtMvForceFo_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 13),
    _FlMcm1xxChannelExtMvForceFo_Type()
)
flMcm1xxChannelExtMvForceFo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvForceFo.setStatus("current")


class _FlMcm1xxChannelExtMvBckpTpUnused_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvBckpTpUnused based on Integer32"""
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


_FlMcm1xxChannelExtMvBckpTpUnused_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvBckpTpUnused_Object = MibTableColumn
flMcm1xxChannelExtMvBckpTpUnused = _FlMcm1xxChannelExtMvBckpTpUnused_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 14),
    _FlMcm1xxChannelExtMvBckpTpUnused_Type()
)
flMcm1xxChannelExtMvBckpTpUnused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvBckpTpUnused.setStatus("current")


class _FlMcm1xxChannelExtMvBckpFoUnused_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvBckpFoUnused based on Integer32"""
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


_FlMcm1xxChannelExtMvBckpFoUnused_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvBckpFoUnused_Object = MibTableColumn
flMcm1xxChannelExtMvBckpFoUnused = _FlMcm1xxChannelExtMvBckpFoUnused_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 15),
    _FlMcm1xxChannelExtMvBckpFoUnused_Type()
)
flMcm1xxChannelExtMvBckpFoUnused.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvBckpFoUnused.setStatus("current")


class _FlMcm1xxChannelExtMvActiveTpLink_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvActiveTpLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("killed", 2),
          ("bckp", 3),
          ("fBckp", 4),
          ("main", 5))
    )


_FlMcm1xxChannelExtMvActiveTpLink_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvActiveTpLink_Object = MibTableColumn
flMcm1xxChannelExtMvActiveTpLink = _FlMcm1xxChannelExtMvActiveTpLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 16),
    _FlMcm1xxChannelExtMvActiveTpLink_Type()
)
flMcm1xxChannelExtMvActiveTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvActiveTpLink.setStatus("current")


class _FlMcm1xxChannelExtMvActiveFoLink_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvActiveFoLink based on Integer32"""
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
        *(("down", 1),
          ("bckp", 2),
          ("fBckp", 3),
          ("main", 4))
    )


_FlMcm1xxChannelExtMvActiveFoLink_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvActiveFoLink_Object = MibTableColumn
flMcm1xxChannelExtMvActiveFoLink = _FlMcm1xxChannelExtMvActiveFoLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 17),
    _FlMcm1xxChannelExtMvActiveFoLink_Type()
)
flMcm1xxChannelExtMvActiveFoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvActiveFoLink.setStatus("current")


class _FlMcm1xxChannelExtMvStbyTpLink_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvStbyTpLink based on Integer32"""
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
        *(("mainDown", 1),
          ("bckpDown", 2),
          ("mainUnused", 3),
          ("bckpUnused", 4),
          ("mainUp", 5),
          ("bckpUp", 6))
    )


_FlMcm1xxChannelExtMvStbyTpLink_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvStbyTpLink_Object = MibTableColumn
flMcm1xxChannelExtMvStbyTpLink = _FlMcm1xxChannelExtMvStbyTpLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 18),
    _FlMcm1xxChannelExtMvStbyTpLink_Type()
)
flMcm1xxChannelExtMvStbyTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvStbyTpLink.setStatus("current")


class _FlMcm1xxChannelExtMvStbyFoLink_Type(Integer32):
    """Custom type flMcm1xxChannelExtMvStbyFoLink based on Integer32"""
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
        *(("mainDown", 1),
          ("bckpDown", 2),
          ("mainUnused", 3),
          ("bckpUnused", 4),
          ("mainUp", 5),
          ("bckpUp", 6))
    )


_FlMcm1xxChannelExtMvStbyFoLink_Type.__name__ = "Integer32"
_FlMcm1xxChannelExtMvStbyFoLink_Object = MibTableColumn
flMcm1xxChannelExtMvStbyFoLink = _FlMcm1xxChannelExtMvStbyFoLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 20, 1, 1, 19),
    _FlMcm1xxChannelExtMvStbyFoLink_Type()
)
flMcm1xxChannelExtMvStbyFoLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1xxChannelExtMvStbyFoLink.setStatus("current")
_FlMcm1xxLinksMv_ObjectIdentity = ObjectIdentity
flMcm1xxLinksMv = _FlMcm1xxLinksMv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30)
)
_FlMcm1xxLinkExtMvTable_Object = MibTable
flMcm1xxLinkExtMvTable = _FlMcm1xxLinkExtMvTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30, 1)
)
if mibBuilder.loadTexts:
    flMcm1xxLinkExtMvTable.setStatus("current")
_FlMcm1xxLinkExtMvEntry_Object = MibTableRow
flMcm1xxLinkExtMvEntry = _FlMcm1xxLinkExtMvEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30, 1, 1)
)
if mibBuilder.loadTexts:
    flMcm1xxLinkExtMvEntry.setStatus("current")


class _FlMcm1xxLinkExtMvPause_Type(Integer32):
    """Custom type flMcm1xxLinkExtMvPause based on Integer32"""
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


_FlMcm1xxLinkExtMvPause_Type.__name__ = "Integer32"
_FlMcm1xxLinkExtMvPause_Object = MibTableColumn
flMcm1xxLinkExtMvPause = _FlMcm1xxLinkExtMvPause_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30, 1, 1, 1),
    _FlMcm1xxLinkExtMvPause_Type()
)
flMcm1xxLinkExtMvPause.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxLinkExtMvPause.setStatus("current")


class _FlMcm1xxLinkExtMvUpstreamBw_Type(Integer32):
    """Custom type flMcm1xxLinkExtMvUpstreamBw based on Integer32"""
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
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("m01", 1),
          ("m02", 2),
          ("m03", 3),
          ("m04", 4),
          ("m05", 5),
          ("m06", 6),
          ("m07", 7),
          ("m08", 8),
          ("m09", 9),
          ("m10", 10),
          ("m20", 20),
          ("m30", 30),
          ("m40", 40),
          ("m50", 50),
          ("m60", 60),
          ("m70", 70),
          ("m80", 80),
          ("m90", 90),
          ("m100", 100),
          ("k256", 129),
          ("k512", 130))
    )


_FlMcm1xxLinkExtMvUpstreamBw_Type.__name__ = "Integer32"
_FlMcm1xxLinkExtMvUpstreamBw_Object = MibTableColumn
flMcm1xxLinkExtMvUpstreamBw = _FlMcm1xxLinkExtMvUpstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30, 1, 1, 2),
    _FlMcm1xxLinkExtMvUpstreamBw_Type()
)
flMcm1xxLinkExtMvUpstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxLinkExtMvUpstreamBw.setStatus("current")


class _FlMcm1xxLinkExtMvDownstreamBw_Type(Integer32):
    """Custom type flMcm1xxLinkExtMvDownstreamBw based on Integer32"""
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
              20,
              30,
              40,
              50,
              60,
              70,
              80,
              90,
              100,
              129,
              130)
        )
    )
    namedValues = NamedValues(
        *(("m01", 1),
          ("m02", 2),
          ("m03", 3),
          ("m04", 4),
          ("m05", 5),
          ("m06", 6),
          ("m07", 7),
          ("m08", 8),
          ("m09", 9),
          ("m10", 10),
          ("m20", 20),
          ("m30", 30),
          ("m40", 40),
          ("m50", 50),
          ("m60", 60),
          ("m70", 70),
          ("m80", 80),
          ("m90", 90),
          ("m100", 100),
          ("k256", 129),
          ("k512", 130))
    )


_FlMcm1xxLinkExtMvDownstreamBw_Type.__name__ = "Integer32"
_FlMcm1xxLinkExtMvDownstreamBw_Object = MibTableColumn
flMcm1xxLinkExtMvDownstreamBw = _FlMcm1xxLinkExtMvDownstreamBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30, 1, 1, 3),
    _FlMcm1xxLinkExtMvDownstreamBw_Type()
)
flMcm1xxLinkExtMvDownstreamBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxLinkExtMvDownstreamBw.setStatus("current")


class _FlMcm1xxLinkExtMvUpSle_Type(Integer32):
    """Custom type flMcm1xxLinkExtMvUpSle based on Integer32"""
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


_FlMcm1xxLinkExtMvUpSle_Type.__name__ = "Integer32"
_FlMcm1xxLinkExtMvUpSle_Object = MibTableColumn
flMcm1xxLinkExtMvUpSle = _FlMcm1xxLinkExtMvUpSle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30, 1, 1, 4),
    _FlMcm1xxLinkExtMvUpSle_Type()
)
flMcm1xxLinkExtMvUpSle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxLinkExtMvUpSle.setStatus("current")


class _FlMcm1xxLinkExtMvDnSle_Type(Integer32):
    """Custom type flMcm1xxLinkExtMvDnSle based on Integer32"""
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


_FlMcm1xxLinkExtMvDnSle_Type.__name__ = "Integer32"
_FlMcm1xxLinkExtMvDnSle_Object = MibTableColumn
flMcm1xxLinkExtMvDnSle = _FlMcm1xxLinkExtMvDnSle_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30, 1, 1, 5),
    _FlMcm1xxLinkExtMvDnSle_Type()
)
flMcm1xxLinkExtMvDnSle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flMcm1xxLinkExtMvDnSle.setStatus("current")


class _FlMcm1xxLinkExtMvRemoteTpLink_Type(Integer32):
    """Custom type flMcm1xxLinkExtMvRemoteTpLink based on Integer32"""
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


_FlMcm1xxLinkExtMvRemoteTpLink_Type.__name__ = "Integer32"
_FlMcm1xxLinkExtMvRemoteTpLink_Object = MibTableColumn
flMcm1xxLinkExtMvRemoteTpLink = _FlMcm1xxLinkExtMvRemoteTpLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30, 1, 1, 6),
    _FlMcm1xxLinkExtMvRemoteTpLink_Type()
)
flMcm1xxLinkExtMvRemoteTpLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1xxLinkExtMvRemoteTpLink.setStatus("current")


class _FlMcm1xxLinkExtMvRlRemote_Type(Integer32):
    """Custom type flMcm1xxLinkExtMvRlRemote based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bckp", 1),
          ("main", 2))
    )


_FlMcm1xxLinkExtMvRlRemote_Type.__name__ = "Integer32"
_FlMcm1xxLinkExtMvRlRemote_Object = MibTableColumn
flMcm1xxLinkExtMvRlRemote = _FlMcm1xxLinkExtMvRlRemote_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 30, 1, 1, 7),
    _FlMcm1xxLinkExtMvRlRemote_Type()
)
flMcm1xxLinkExtMvRlRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flMcm1xxLinkExtMvRlRemote.setStatus("current")
flMsChassisModuleMvEntry.registerAugmentions(
    ("FIBROLAN-MIB-MCM1xx",
     "flMcm1xxModuleExtMvEntry")
)
flMcm1xxModuleExtMvEntry.setIndexNames(*flMsChassisModuleMvEntry.getIndexNames())
flMsModuleMvChannelEntry.registerAugmentions(
    ("FIBROLAN-MIB-MCM1xx",
     "flMcm1xxChannelExtMvEntry")
)
flMcm1xxChannelExtMvEntry.setIndexNames(*flMsModuleMvChannelEntry.getIndexNames())
flMsModuleMvLinkEntry.registerAugmentions(
    ("FIBROLAN-MIB-MCM1xx",
     "flMcm1xxLinkExtMvEntry")
)
flMcm1xxLinkExtMvEntry.setIndexNames(*flMsModuleMvLinkEntry.getIndexNames())

# Managed Objects groups

flMsMcm1xxMvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 1, 2, 1)
)
flMsMcm1xxMvGroup.setObjects(
    ("FIBROLAN-MIB-MCM1xx", "flMcm1xxModuleExtMvRedundantMod")
)
if mibBuilder.loadTexts:
    flMsMcm1xxMvGroup.setStatus("current")

flMsMcm1xxMvChannelsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 1, 2, 2)
)
flMsMcm1xxMvChannelsGroup.setObjects(
      *(("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvTpLink"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvFoLink"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvPortDescription"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvDuplex"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvEnableTpPort"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvTp2FoFp"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvFo2TpFp"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvAutoNego"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvDatarate"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvTpBckp2Main"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvFoBckp2Main"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvForceTp"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvForceFo"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvBckpTpUnused"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvBckpFoUnused"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvActiveTpLink"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvActiveFoLink"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvStbyTpLink"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxChannelExtMvStbyFoLink"))
)
if mibBuilder.loadTexts:
    flMsMcm1xxMvChannelsGroup.setStatus("current")

flMsMcm1xxMvLinksGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 1, 2, 3)
)
flMsMcm1xxMvLinksGroup.setObjects(
      *(("FIBROLAN-MIB-MCM1xx", "flMcm1xxLinkExtMvPause"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxLinkExtMvUpstreamBw"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxLinkExtMvDownstreamBw"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxLinkExtMvUpSle"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxLinkExtMvDnSle"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxLinkExtMvRemoteTpLink"),
        ("FIBROLAN-MIB-MCM1xx", "flMcm1xxLinkExtMvRlRemote"))
)
if mibBuilder.loadTexts:
    flMsMcm1xxMvLinksGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flMsMcm1xxMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 100, 1, 1, 1)
)
flMsMcm1xxMIBCompliance.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisGroup"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModulesGroup"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvChannelsGroup"),
        ("FIBROLAN-MIB-MSMODULE", "flMsModuleMvLinksGroup"),
        ("FIBROLAN-MIB-MCM1xx", "flMsMcm1xxMvGroup"),
        ("FIBROLAN-MIB-MCM1xx", "flMsMcm1xxMvChannelsGroup"),
        ("FIBROLAN-MIB-MCM1xx", "flMsMcm1xxMvLinksGroup"))
)
if mibBuilder.loadTexts:
    flMsMcm1xxMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-MCM1xx",
    **{"fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsChassisMv": flMsChassisMv,
       "flMsModuleMv": flMsModuleMv,
       "flMcm1xxMv": flMcm1xxMv,
       "flMsMcm1xxMIBConformance": flMsMcm1xxMIBConformance,
       "flMsMcm1xxMIBCompliances": flMsMcm1xxMIBCompliances,
       "flMsMcm1xxMIBCompliance": flMsMcm1xxMIBCompliance,
       "flMsMcm1xxMIBGroups": flMsMcm1xxMIBGroups,
       "flMsMcm1xxMvGroup": flMsMcm1xxMvGroup,
       "flMsMcm1xxMvChannelsGroup": flMsMcm1xxMvChannelsGroup,
       "flMsMcm1xxMvLinksGroup": flMsMcm1xxMvLinksGroup,
       "flMcm1xxModuleMv": flMcm1xxModuleMv,
       "flMcm1xxModuleExtMvTable": flMcm1xxModuleExtMvTable,
       "flMcm1xxModuleExtMvEntry": flMcm1xxModuleExtMvEntry,
       "flMcm1xxModuleExtMvRedundantMod": flMcm1xxModuleExtMvRedundantMod,
       "flMcm1xxChannelsMv": flMcm1xxChannelsMv,
       "flMcm1xxChannelExtMvTable": flMcm1xxChannelExtMvTable,
       "flMcm1xxChannelExtMvEntry": flMcm1xxChannelExtMvEntry,
       "flMcm1xxChannelExtMvTpLink": flMcm1xxChannelExtMvTpLink,
       "flMcm1xxChannelExtMvFoLink": flMcm1xxChannelExtMvFoLink,
       "flMcm1xxChannelExtMvPortDescription": flMcm1xxChannelExtMvPortDescription,
       "flMcm1xxChannelExtMvDuplex": flMcm1xxChannelExtMvDuplex,
       "flMcm1xxChannelExtMvEnableTpPort": flMcm1xxChannelExtMvEnableTpPort,
       "flMcm1xxChannelExtMvTp2FoFp": flMcm1xxChannelExtMvTp2FoFp,
       "flMcm1xxChannelExtMvFo2TpFp": flMcm1xxChannelExtMvFo2TpFp,
       "flMcm1xxChannelExtMvAutoNego": flMcm1xxChannelExtMvAutoNego,
       "flMcm1xxChannelExtMvDatarate": flMcm1xxChannelExtMvDatarate,
       "flMcm1xxChannelExtMvTpBckp2Main": flMcm1xxChannelExtMvTpBckp2Main,
       "flMcm1xxChannelExtMvFoBckp2Main": flMcm1xxChannelExtMvFoBckp2Main,
       "flMcm1xxChannelExtMvForceTp": flMcm1xxChannelExtMvForceTp,
       "flMcm1xxChannelExtMvForceFo": flMcm1xxChannelExtMvForceFo,
       "flMcm1xxChannelExtMvBckpTpUnused": flMcm1xxChannelExtMvBckpTpUnused,
       "flMcm1xxChannelExtMvBckpFoUnused": flMcm1xxChannelExtMvBckpFoUnused,
       "flMcm1xxChannelExtMvActiveTpLink": flMcm1xxChannelExtMvActiveTpLink,
       "flMcm1xxChannelExtMvActiveFoLink": flMcm1xxChannelExtMvActiveFoLink,
       "flMcm1xxChannelExtMvStbyTpLink": flMcm1xxChannelExtMvStbyTpLink,
       "flMcm1xxChannelExtMvStbyFoLink": flMcm1xxChannelExtMvStbyFoLink,
       "flMcm1xxLinksMv": flMcm1xxLinksMv,
       "flMcm1xxLinkExtMvTable": flMcm1xxLinkExtMvTable,
       "flMcm1xxLinkExtMvEntry": flMcm1xxLinkExtMvEntry,
       "flMcm1xxLinkExtMvPause": flMcm1xxLinkExtMvPause,
       "flMcm1xxLinkExtMvUpstreamBw": flMcm1xxLinkExtMvUpstreamBw,
       "flMcm1xxLinkExtMvDownstreamBw": flMcm1xxLinkExtMvDownstreamBw,
       "flMcm1xxLinkExtMvUpSle": flMcm1xxLinkExtMvUpSle,
       "flMcm1xxLinkExtMvDnSle": flMcm1xxLinkExtMvDnSle,
       "flMcm1xxLinkExtMvRemoteTpLink": flMcm1xxLinkExtMvRemoteTpLink,
       "flMcm1xxLinkExtMvRlRemote": flMcm1xxLinkExtMvRlRemote}
)
