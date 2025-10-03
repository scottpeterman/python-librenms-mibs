# SNMP MIB module (FIBROLAN-MIB-ACM110) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fibrolan\FIBROLAN-MIB-ACM110
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

(flMsChassisModuleMvIndex,
 flMsChassisMvIndex) = mibBuilder.importSymbols(
    "FIBROLAN-MIB-METRO-STAR-MV",
    "flMsChassisModuleMvIndex",
    "flMsChassisMvIndex")

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

flAcm110Mv = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120)
)


# Types definitions



class EntryStatus(Integer32):
    """Custom type EntryStatus based on Integer32"""
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
        *(("valid", 1),
          ("createRequest", 2),
          ("underCreation", 3),
          ("invalid", 4))
    )




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
_FlAcm110MIBConformance_ObjectIdentity = ObjectIdentity
flAcm110MIBConformance = _FlAcm110MIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1)
)
_FlAcm110MIBCompliances_ObjectIdentity = ObjectIdentity
flAcm110MIBCompliances = _FlAcm110MIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 1)
)
_FlAcm110MIBGroups_ObjectIdentity = ObjectIdentity
flAcm110MIBGroups = _FlAcm110MIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2)
)
_FlAcm110MvGlobal_ObjectIdentity = ObjectIdentity
flAcm110MvGlobal = _FlAcm110MvGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10)
)
_FlAcm110MvGlobalConfigTable_Object = MibTable
flAcm110MvGlobalConfigTable = _FlAcm110MvGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1)
)
if mibBuilder.loadTexts:
    flAcm110MvGlobalConfigTable.setStatus("current")
_FlAcm110MvGlobalConfigEntry_Object = MibTableRow
flAcm110MvGlobalConfigEntry = _FlAcm110MvGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1)
)
flAcm110MvGlobalConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvGlobalConfigIndex"),
)
if mibBuilder.loadTexts:
    flAcm110MvGlobalConfigEntry.setStatus("current")


class _FlAcm110MvGlobalConfigIndex_Type(Integer32):
    """Custom type flAcm110MvGlobalConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FlAcm110MvGlobalConfigIndex_Type.__name__ = "Integer32"
_FlAcm110MvGlobalConfigIndex_Object = MibTableColumn
flAcm110MvGlobalConfigIndex = _FlAcm110MvGlobalConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 1),
    _FlAcm110MvGlobalConfigIndex_Type()
)
flAcm110MvGlobalConfigIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvGlobalConfigIndex.setStatus("current")


class _FlAcm110MvGlobalBufferShare_Type(Integer32):
    """Custom type flAcm110MvGlobalBufferShare based on Integer32"""
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


_FlAcm110MvGlobalBufferShare_Type.__name__ = "Integer32"
_FlAcm110MvGlobalBufferShare_Object = MibTableColumn
flAcm110MvGlobalBufferShare = _FlAcm110MvGlobalBufferShare_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 2),
    _FlAcm110MvGlobalBufferShare_Type()
)
flAcm110MvGlobalBufferShare.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvGlobalBufferShare.setStatus("current")


class _FlAcm110MvGlobalMulticastProtect_Type(Integer32):
    """Custom type flAcm110MvGlobalMulticastProtect based on Integer32"""
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


_FlAcm110MvGlobalMulticastProtect_Type.__name__ = "Integer32"
_FlAcm110MvGlobalMulticastProtect_Object = MibTableColumn
flAcm110MvGlobalMulticastProtect = _FlAcm110MvGlobalMulticastProtect_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 3),
    _FlAcm110MvGlobalMulticastProtect_Type()
)
flAcm110MvGlobalMulticastProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvGlobalMulticastProtect.setStatus("current")


class _FlAcm110MvGlobalBroadcastRate_Type(Integer32):
    """Custom type flAcm110MvGlobalBroadcastRate based on Integer32"""
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
        *(("pct5", 1),
          ("pct10", 2),
          ("pct15", 3),
          ("pct20", 4),
          ("pct25", 5))
    )


_FlAcm110MvGlobalBroadcastRate_Type.__name__ = "Integer32"
_FlAcm110MvGlobalBroadcastRate_Object = MibTableColumn
flAcm110MvGlobalBroadcastRate = _FlAcm110MvGlobalBroadcastRate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 4),
    _FlAcm110MvGlobalBroadcastRate_Type()
)
flAcm110MvGlobalBroadcastRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvGlobalBroadcastRate.setStatus("current")


class _FlAcm110MvGlobalMaxPacketSize_Type(Integer32):
    """Custom type flAcm110MvGlobalMaxPacketSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bytes1522", 1),
          ("bytes1536", 2),
          ("bytes1916", 3))
    )


_FlAcm110MvGlobalMaxPacketSize_Type.__name__ = "Integer32"
_FlAcm110MvGlobalMaxPacketSize_Object = MibTableColumn
flAcm110MvGlobalMaxPacketSize = _FlAcm110MvGlobalMaxPacketSize_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 5),
    _FlAcm110MvGlobalMaxPacketSize_Type()
)
flAcm110MvGlobalMaxPacketSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvGlobalMaxPacketSize.setStatus("current")


class _FlAcm110MvGlobalSleLogic_Type(Integer32):
    """Custom type flAcm110MvGlobalSleLogic based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("or", 1),
          ("and", 2))
    )


_FlAcm110MvGlobalSleLogic_Type.__name__ = "Integer32"
_FlAcm110MvGlobalSleLogic_Object = MibTableColumn
flAcm110MvGlobalSleLogic = _FlAcm110MvGlobalSleLogic_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 6),
    _FlAcm110MvGlobalSleLogic_Type()
)
flAcm110MvGlobalSleLogic.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvGlobalSleLogic.setStatus("current")


class _FlAcm110MvGlobalSlePort1_Type(Integer32):
    """Custom type flAcm110MvGlobalSlePort1 based on Integer32"""
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


_FlAcm110MvGlobalSlePort1_Type.__name__ = "Integer32"
_FlAcm110MvGlobalSlePort1_Object = MibTableColumn
flAcm110MvGlobalSlePort1 = _FlAcm110MvGlobalSlePort1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 7),
    _FlAcm110MvGlobalSlePort1_Type()
)
flAcm110MvGlobalSlePort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvGlobalSlePort1.setStatus("current")


class _FlAcm110MvGlobalSlePort2_Type(Integer32):
    """Custom type flAcm110MvGlobalSlePort2 based on Integer32"""
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


_FlAcm110MvGlobalSlePort2_Type.__name__ = "Integer32"
_FlAcm110MvGlobalSlePort2_Object = MibTableColumn
flAcm110MvGlobalSlePort2 = _FlAcm110MvGlobalSlePort2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 8),
    _FlAcm110MvGlobalSlePort2_Type()
)
flAcm110MvGlobalSlePort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvGlobalSlePort2.setStatus("current")


class _FlAcm110MvGlobalSlePort3_Type(Integer32):
    """Custom type flAcm110MvGlobalSlePort3 based on Integer32"""
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


_FlAcm110MvGlobalSlePort3_Type.__name__ = "Integer32"
_FlAcm110MvGlobalSlePort3_Object = MibTableColumn
flAcm110MvGlobalSlePort3 = _FlAcm110MvGlobalSlePort3_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 9),
    _FlAcm110MvGlobalSlePort3_Type()
)
flAcm110MvGlobalSlePort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvGlobalSlePort3.setStatus("current")


class _FlAcm110MvGlobalSlePort4_Type(Integer32):
    """Custom type flAcm110MvGlobalSlePort4 based on Integer32"""
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


_FlAcm110MvGlobalSlePort4_Type.__name__ = "Integer32"
_FlAcm110MvGlobalSlePort4_Object = MibTableColumn
flAcm110MvGlobalSlePort4 = _FlAcm110MvGlobalSlePort4_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 10, 1, 1, 10),
    _FlAcm110MvGlobalSlePort4_Type()
)
flAcm110MvGlobalSlePort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvGlobalSlePort4.setStatus("current")
_FlAcm110MvPorts_ObjectIdentity = ObjectIdentity
flAcm110MvPorts = _FlAcm110MvPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20)
)
_FlAcm110MvPortConfigTable_Object = MibTable
flAcm110MvPortConfigTable = _FlAcm110MvPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1)
)
if mibBuilder.loadTexts:
    flAcm110MvPortConfigTable.setStatus("current")
_FlAcm110MvPortConfigEntry_Object = MibTableRow
flAcm110MvPortConfigEntry = _FlAcm110MvPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1)
)
flAcm110MvPortConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvPortConfigEntry.setStatus("current")


class _FlAcm110MvPortNumber_Type(Integer32):
    """Custom type flAcm110MvPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FlAcm110MvPortNumber_Type.__name__ = "Integer32"
_FlAcm110MvPortNumber_Object = MibTableColumn
flAcm110MvPortNumber = _FlAcm110MvPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 1),
    _FlAcm110MvPortNumber_Type()
)
flAcm110MvPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvPortNumber.setStatus("current")


class _FlAcm110MvPortType_Type(Integer32):
    """Custom type flAcm110MvPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              9999)
        )
    )
    namedValues = NamedValues(
        *(("tp", 1),
          ("fo", 2),
          ("other", 9999))
    )


_FlAcm110MvPortType_Type.__name__ = "Integer32"
_FlAcm110MvPortType_Object = MibTableColumn
flAcm110MvPortType = _FlAcm110MvPortType_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 2),
    _FlAcm110MvPortType_Type()
)
flAcm110MvPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvPortType.setStatus("current")


class _FlAcm110MvPortLink_Type(Integer32):
    """Custom type flAcm110MvPortLink based on Integer32"""
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
          ("kld", 3))
    )


_FlAcm110MvPortLink_Type.__name__ = "Integer32"
_FlAcm110MvPortLink_Object = MibTableColumn
flAcm110MvPortLink = _FlAcm110MvPortLink_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 3),
    _FlAcm110MvPortLink_Type()
)
flAcm110MvPortLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvPortLink.setStatus("current")
_FlAcm110MvPortDescription_Type = DisplayString
_FlAcm110MvPortDescription_Object = MibTableColumn
flAcm110MvPortDescription = _FlAcm110MvPortDescription_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 4),
    _FlAcm110MvPortDescription_Type()
)
flAcm110MvPortDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortDescription.setStatus("current")


class _FlAcm110MvPortAutoNego_Type(Integer32):
    """Custom type flAcm110MvPortAutoNego based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_FlAcm110MvPortAutoNego_Type.__name__ = "Integer32"
_FlAcm110MvPortAutoNego_Object = MibTableColumn
flAcm110MvPortAutoNego = _FlAcm110MvPortAutoNego_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 5),
    _FlAcm110MvPortAutoNego_Type()
)
flAcm110MvPortAutoNego.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortAutoNego.setStatus("current")


class _FlAcm110MvPortDuplex_Type(Integer32):
    """Custom type flAcm110MvPortDuplex based on Integer32"""
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


_FlAcm110MvPortDuplex_Type.__name__ = "Integer32"
_FlAcm110MvPortDuplex_Object = MibTableColumn
flAcm110MvPortDuplex = _FlAcm110MvPortDuplex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 6),
    _FlAcm110MvPortDuplex_Type()
)
flAcm110MvPortDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortDuplex.setStatus("current")


class _FlAcm110MvPortDatarate_Type(Integer32):
    """Custom type flAcm110MvPortDatarate based on Integer32"""
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


_FlAcm110MvPortDatarate_Type.__name__ = "Integer32"
_FlAcm110MvPortDatarate_Object = MibTableColumn
flAcm110MvPortDatarate = _FlAcm110MvPortDatarate_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 7),
    _FlAcm110MvPortDatarate_Type()
)
flAcm110MvPortDatarate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortDatarate.setStatus("current")


class _FlAcm110MvPortEnabled_Type(Integer32):
    """Custom type flAcm110MvPortEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_FlAcm110MvPortEnabled_Type.__name__ = "Integer32"
_FlAcm110MvPortEnabled_Object = MibTableColumn
flAcm110MvPortEnabled = _FlAcm110MvPortEnabled_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 8),
    _FlAcm110MvPortEnabled_Type()
)
flAcm110MvPortEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortEnabled.setStatus("current")


class _FlAcm110MvPortAutoCross_Type(Integer32):
    """Custom type flAcm110MvPortAutoCross based on Integer32"""
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


_FlAcm110MvPortAutoCross_Type.__name__ = "Integer32"
_FlAcm110MvPortAutoCross_Object = MibTableColumn
flAcm110MvPortAutoCross = _FlAcm110MvPortAutoCross_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 9),
    _FlAcm110MvPortAutoCross_Type()
)
flAcm110MvPortAutoCross.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortAutoCross.setStatus("current")


class _FlAcm110MvPortMdix_Type(Integer32):
    """Custom type flAcm110MvPortMdix based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2))
    )


_FlAcm110MvPortMdix_Type.__name__ = "Integer32"
_FlAcm110MvPortMdix_Object = MibTableColumn
flAcm110MvPortMdix = _FlAcm110MvPortMdix_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 10),
    _FlAcm110MvPortMdix_Type()
)
flAcm110MvPortMdix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortMdix.setStatus("current")


class _FlAcm110MvPortFef_Type(Integer32):
    """Custom type flAcm110MvPortFef based on Integer32"""
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


_FlAcm110MvPortFef_Type.__name__ = "Integer32"
_FlAcm110MvPortFef_Object = MibTableColumn
flAcm110MvPortFef = _FlAcm110MvPortFef_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 11),
    _FlAcm110MvPortFef_Type()
)
flAcm110MvPortFef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortFef.setStatus("current")


class _FlAcm110MvPortReset_Type(Integer32):
    """Custom type flAcm110MvPortReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("reset", 2))
    )


_FlAcm110MvPortReset_Type.__name__ = "Integer32"
_FlAcm110MvPortReset_Object = MibTableColumn
flAcm110MvPortReset = _FlAcm110MvPortReset_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 12),
    _FlAcm110MvPortReset_Type()
)
flAcm110MvPortReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortReset.setStatus("current")


class _FlAcm110MvPortBroadcastProtect_Type(Integer32):
    """Custom type flAcm110MvPortBroadcastProtect based on Integer32"""
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


_FlAcm110MvPortBroadcastProtect_Type.__name__ = "Integer32"
_FlAcm110MvPortBroadcastProtect_Object = MibTableColumn
flAcm110MvPortBroadcastProtect = _FlAcm110MvPortBroadcastProtect_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 1, 1, 13),
    _FlAcm110MvPortBroadcastProtect_Type()
)
flAcm110MvPortBroadcastProtect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortBroadcastProtect.setStatus("current")
_FlAcm110MvPortBwConfigTable_Object = MibTable
flAcm110MvPortBwConfigTable = _FlAcm110MvPortBwConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2)
)
if mibBuilder.loadTexts:
    flAcm110MvPortBwConfigTable.setStatus("current")
_FlAcm110MvPortBwConfigEntry_Object = MibTableRow
flAcm110MvPortBwConfigEntry = _FlAcm110MvPortBwConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2, 1)
)
flAcm110MvPortBwConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvPortBwConfigEntry.setStatus("current")


class _FlAcm110MvPortRxHighBw_Type(Integer32):
    """Custom type flAcm110MvPortRxHighBw based on Integer32"""
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


_FlAcm110MvPortRxHighBw_Type.__name__ = "Integer32"
_FlAcm110MvPortRxHighBw_Object = MibTableColumn
flAcm110MvPortRxHighBw = _FlAcm110MvPortRxHighBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2, 1, 1),
    _FlAcm110MvPortRxHighBw_Type()
)
flAcm110MvPortRxHighBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortRxHighBw.setStatus("current")


class _FlAcm110MvPortTxHighBw_Type(Integer32):
    """Custom type flAcm110MvPortTxHighBw based on Integer32"""
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


_FlAcm110MvPortTxHighBw_Type.__name__ = "Integer32"
_FlAcm110MvPortTxHighBw_Object = MibTableColumn
flAcm110MvPortTxHighBw = _FlAcm110MvPortTxHighBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2, 1, 2),
    _FlAcm110MvPortTxHighBw_Type()
)
flAcm110MvPortTxHighBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortTxHighBw.setStatus("current")


class _FlAcm110MvPortRxLowBw_Type(Integer32):
    """Custom type flAcm110MvPortRxLowBw based on Integer32"""
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


_FlAcm110MvPortRxLowBw_Type.__name__ = "Integer32"
_FlAcm110MvPortRxLowBw_Object = MibTableColumn
flAcm110MvPortRxLowBw = _FlAcm110MvPortRxLowBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2, 1, 3),
    _FlAcm110MvPortRxLowBw_Type()
)
flAcm110MvPortRxLowBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortRxLowBw.setStatus("current")


class _FlAcm110MvPortTxLowBw_Type(Integer32):
    """Custom type flAcm110MvPortTxLowBw based on Integer32"""
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


_FlAcm110MvPortTxLowBw_Type.__name__ = "Integer32"
_FlAcm110MvPortTxLowBw_Object = MibTableColumn
flAcm110MvPortTxLowBw = _FlAcm110MvPortTxLowBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2, 1, 4),
    _FlAcm110MvPortTxLowBw_Type()
)
flAcm110MvPortTxLowBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortTxLowBw.setStatus("current")


class _FlAcm110MvPortRxDiffBw_Type(Integer32):
    """Custom type flAcm110MvPortRxDiffBw based on Integer32"""
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


_FlAcm110MvPortRxDiffBw_Type.__name__ = "Integer32"
_FlAcm110MvPortRxDiffBw_Object = MibTableColumn
flAcm110MvPortRxDiffBw = _FlAcm110MvPortRxDiffBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2, 1, 5),
    _FlAcm110MvPortRxDiffBw_Type()
)
flAcm110MvPortRxDiffBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortRxDiffBw.setStatus("current")


class _FlAcm110MvPortRxHighFlowControl_Type(Integer32):
    """Custom type flAcm110MvPortRxHighFlowControl based on Integer32"""
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


_FlAcm110MvPortRxHighFlowControl_Type.__name__ = "Integer32"
_FlAcm110MvPortRxHighFlowControl_Object = MibTableColumn
flAcm110MvPortRxHighFlowControl = _FlAcm110MvPortRxHighFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2, 1, 6),
    _FlAcm110MvPortRxHighFlowControl_Type()
)
flAcm110MvPortRxHighFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortRxHighFlowControl.setStatus("current")


class _FlAcm110MvPortRxLowFlowControl_Type(Integer32):
    """Custom type flAcm110MvPortRxLowFlowControl based on Integer32"""
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


_FlAcm110MvPortRxLowFlowControl_Type.__name__ = "Integer32"
_FlAcm110MvPortRxLowFlowControl_Object = MibTableColumn
flAcm110MvPortRxLowFlowControl = _FlAcm110MvPortRxLowFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2, 1, 7),
    _FlAcm110MvPortRxLowFlowControl_Type()
)
flAcm110MvPortRxLowFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortRxLowFlowControl.setStatus("current")


class _FlAcm110MvPortTxDiffBw_Type(Integer32):
    """Custom type flAcm110MvPortTxDiffBw based on Integer32"""
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


_FlAcm110MvPortTxDiffBw_Type.__name__ = "Integer32"
_FlAcm110MvPortTxDiffBw_Object = MibTableColumn
flAcm110MvPortTxDiffBw = _FlAcm110MvPortTxDiffBw_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 20, 2, 1, 8),
    _FlAcm110MvPortTxDiffBw_Type()
)
flAcm110MvPortTxDiffBw.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortTxDiffBw.setStatus("current")
_FlAcm110MvVlan_ObjectIdentity = ObjectIdentity
flAcm110MvVlan = _FlAcm110MvVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30)
)
_FlAcm110MvGlobalVlanConfigTable_Object = MibTable
flAcm110MvGlobalVlanConfigTable = _FlAcm110MvGlobalVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 1)
)
if mibBuilder.loadTexts:
    flAcm110MvGlobalVlanConfigTable.setStatus("current")
_FlAcm110MvGlobalVlanConfigEntry_Object = MibTableRow
flAcm110MvGlobalVlanConfigEntry = _FlAcm110MvGlobalVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 1, 1)
)
flAcm110MvGlobalVlanConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvVlanConfigIndex"),
)
if mibBuilder.loadTexts:
    flAcm110MvGlobalVlanConfigEntry.setStatus("current")


class _FlAcm110MvVlanConfigIndex_Type(Integer32):
    """Custom type flAcm110MvVlanConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_FlAcm110MvVlanConfigIndex_Type.__name__ = "Integer32"
_FlAcm110MvVlanConfigIndex_Object = MibTableColumn
flAcm110MvVlanConfigIndex = _FlAcm110MvVlanConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 1, 1, 1),
    _FlAcm110MvVlanConfigIndex_Type()
)
flAcm110MvVlanConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanConfigIndex.setStatus("current")


class _FlAcm110MvVlan8021q_Type(Integer32):
    """Custom type flAcm110MvVlan8021q based on Integer32"""
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


_FlAcm110MvVlan8021q_Type.__name__ = "Integer32"
_FlAcm110MvVlan8021q_Object = MibTableColumn
flAcm110MvVlan8021q = _FlAcm110MvVlan8021q_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 1, 1, 2),
    _FlAcm110MvVlan8021q_Type()
)
flAcm110MvVlan8021q.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlan8021q.setStatus("current")


class _FlAcm110MvVlanNullVidReplace_Type(Integer32):
    """Custom type flAcm110MvVlanNullVidReplace based on Integer32"""
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


_FlAcm110MvVlanNullVidReplace_Type.__name__ = "Integer32"
_FlAcm110MvVlanNullVidReplace_Object = MibTableColumn
flAcm110MvVlanNullVidReplace = _FlAcm110MvVlanNullVidReplace_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 1, 1, 3),
    _FlAcm110MvVlanNullVidReplace_Type()
)
flAcm110MvVlanNullVidReplace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanNullVidReplace.setStatus("current")


class _FlAcm110MvCreateDefaultVlans_Type(Integer32):
    """Custom type flAcm110MvCreateDefaultVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("create", 2))
    )


_FlAcm110MvCreateDefaultVlans_Type.__name__ = "Integer32"
_FlAcm110MvCreateDefaultVlans_Object = MibTableColumn
flAcm110MvCreateDefaultVlans = _FlAcm110MvCreateDefaultVlans_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 1, 1, 4),
    _FlAcm110MvCreateDefaultVlans_Type()
)
flAcm110MvCreateDefaultVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvCreateDefaultVlans.setStatus("current")


class _FlAcm110MvDeleteAllVlans_Type(Integer32):
    """Custom type flAcm110MvDeleteAllVlans based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("delete", 2))
    )


_FlAcm110MvDeleteAllVlans_Type.__name__ = "Integer32"
_FlAcm110MvDeleteAllVlans_Object = MibTableColumn
flAcm110MvDeleteAllVlans = _FlAcm110MvDeleteAllVlans_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 1, 1, 5),
    _FlAcm110MvDeleteAllVlans_Type()
)
flAcm110MvDeleteAllVlans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvDeleteAllVlans.setStatus("current")
_FlAcm110MvVlanTable_Object = MibTable
flAcm110MvVlanTable = _FlAcm110MvVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10)
)
if mibBuilder.loadTexts:
    flAcm110MvVlanTable.setStatus("current")
_FlAcm110MvVlanEntry_Object = MibTableRow
flAcm110MvVlanEntry = _FlAcm110MvVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1)
)
flAcm110MvVlanEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvVlanFid"),
)
if mibBuilder.loadTexts:
    flAcm110MvVlanEntry.setStatus("current")


class _FlAcm110MvVlanFid_Type(Integer32):
    """Custom type flAcm110MvVlanFid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FlAcm110MvVlanFid_Type.__name__ = "Integer32"
_FlAcm110MvVlanFid_Object = MibTableColumn
flAcm110MvVlanFid = _FlAcm110MvVlanFid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1, 1),
    _FlAcm110MvVlanFid_Type()
)
flAcm110MvVlanFid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvVlanFid.setStatus("current")


class _FlAcm110MvVlanVid_Type(Integer32):
    """Custom type flAcm110MvVlanVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_FlAcm110MvVlanVid_Type.__name__ = "Integer32"
_FlAcm110MvVlanVid_Object = MibTableColumn
flAcm110MvVlanVid = _FlAcm110MvVlanVid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1, 2),
    _FlAcm110MvVlanVid_Type()
)
flAcm110MvVlanVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanVid.setStatus("current")
_FlAcm110MvVlanName_Type = DisplayString
_FlAcm110MvVlanName_Object = MibTableColumn
flAcm110MvVlanName = _FlAcm110MvVlanName_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1, 3),
    _FlAcm110MvVlanName_Type()
)
flAcm110MvVlanName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanName.setStatus("current")


class _FlAcm110MvVlanPort1Member_Type(Integer32):
    """Custom type flAcm110MvVlanPort1Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlAcm110MvVlanPort1Member_Type.__name__ = "Integer32"
_FlAcm110MvVlanPort1Member_Object = MibTableColumn
flAcm110MvVlanPort1Member = _FlAcm110MvVlanPort1Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1, 4),
    _FlAcm110MvVlanPort1Member_Type()
)
flAcm110MvVlanPort1Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanPort1Member.setStatus("current")


class _FlAcm110MvVlanPort2Member_Type(Integer32):
    """Custom type flAcm110MvVlanPort2Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlAcm110MvVlanPort2Member_Type.__name__ = "Integer32"
_FlAcm110MvVlanPort2Member_Object = MibTableColumn
flAcm110MvVlanPort2Member = _FlAcm110MvVlanPort2Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1, 5),
    _FlAcm110MvVlanPort2Member_Type()
)
flAcm110MvVlanPort2Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanPort2Member.setStatus("current")


class _FlAcm110MvVlanPort3Member_Type(Integer32):
    """Custom type flAcm110MvVlanPort3Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlAcm110MvVlanPort3Member_Type.__name__ = "Integer32"
_FlAcm110MvVlanPort3Member_Object = MibTableColumn
flAcm110MvVlanPort3Member = _FlAcm110MvVlanPort3Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1, 6),
    _FlAcm110MvVlanPort3Member_Type()
)
flAcm110MvVlanPort3Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanPort3Member.setStatus("current")


class _FlAcm110MvVlanPort4Member_Type(Integer32):
    """Custom type flAcm110MvVlanPort4Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlAcm110MvVlanPort4Member_Type.__name__ = "Integer32"
_FlAcm110MvVlanPort4Member_Object = MibTableColumn
flAcm110MvVlanPort4Member = _FlAcm110MvVlanPort4Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1, 7),
    _FlAcm110MvVlanPort4Member_Type()
)
flAcm110MvVlanPort4Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanPort4Member.setStatus("current")


class _FlAcm110MvVlanPort5Member_Type(Integer32):
    """Custom type flAcm110MvVlanPort5Member based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("native", 2),
          ("tagged", 3))
    )


_FlAcm110MvVlanPort5Member_Type.__name__ = "Integer32"
_FlAcm110MvVlanPort5Member_Object = MibTableColumn
flAcm110MvVlanPort5Member = _FlAcm110MvVlanPort5Member_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1, 8),
    _FlAcm110MvVlanPort5Member_Type()
)
flAcm110MvVlanPort5Member.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanPort5Member.setStatus("current")
_FlAcm110MvVlanTableStatus_Type = EntryStatus
_FlAcm110MvVlanTableStatus_Object = MibTableColumn
flAcm110MvVlanTableStatus = _FlAcm110MvVlanTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 10, 1, 9),
    _FlAcm110MvVlanTableStatus_Type()
)
flAcm110MvVlanTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvVlanTableStatus.setStatus("current")
_FlAcm110MvPortVlanConfigTable_Object = MibTable
flAcm110MvPortVlanConfigTable = _FlAcm110MvPortVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 20)
)
if mibBuilder.loadTexts:
    flAcm110MvPortVlanConfigTable.setStatus("current")
_FlAcm110MvPortVlanConfigEntry_Object = MibTableRow
flAcm110MvPortVlanConfigEntry = _FlAcm110MvPortVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 20, 1)
)
flAcm110MvPortVlanConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvPortVlanConfigEntry.setStatus("current")


class _FlAcm110MvPortIngressFilter_Type(Integer32):
    """Custom type flAcm110MvPortIngressFilter based on Integer32"""
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


_FlAcm110MvPortIngressFilter_Type.__name__ = "Integer32"
_FlAcm110MvPortIngressFilter_Object = MibTableColumn
flAcm110MvPortIngressFilter = _FlAcm110MvPortIngressFilter_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 20, 1, 1),
    _FlAcm110MvPortIngressFilter_Type()
)
flAcm110MvPortIngressFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortIngressFilter.setStatus("current")


class _FlAcm110MvPortTagInsertion_Type(Integer32):
    """Custom type flAcm110MvPortTagInsertion based on Integer32"""
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


_FlAcm110MvPortTagInsertion_Type.__name__ = "Integer32"
_FlAcm110MvPortTagInsertion_Object = MibTableColumn
flAcm110MvPortTagInsertion = _FlAcm110MvPortTagInsertion_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 20, 1, 2),
    _FlAcm110MvPortTagInsertion_Type()
)
flAcm110MvPortTagInsertion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortTagInsertion.setStatus("current")


class _FlAcm110MvPortTagRemoval_Type(Integer32):
    """Custom type flAcm110MvPortTagRemoval based on Integer32"""
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


_FlAcm110MvPortTagRemoval_Type.__name__ = "Integer32"
_FlAcm110MvPortTagRemoval_Object = MibTableColumn
flAcm110MvPortTagRemoval = _FlAcm110MvPortTagRemoval_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 20, 1, 3),
    _FlAcm110MvPortTagRemoval_Type()
)
flAcm110MvPortTagRemoval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortTagRemoval.setStatus("current")


class _FlAcm110MvPortVid_Type(Integer32):
    """Custom type flAcm110MvPortVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_FlAcm110MvPortVid_Type.__name__ = "Integer32"
_FlAcm110MvPortVid_Object = MibTableColumn
flAcm110MvPortVid = _FlAcm110MvPortVid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 20, 1, 4),
    _FlAcm110MvPortVid_Type()
)
flAcm110MvPortVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortVid.setStatus("current")


class _FlAcm110MvPortDiscardNonPvid_Type(Integer32):
    """Custom type flAcm110MvPortDiscardNonPvid based on Integer32"""
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


_FlAcm110MvPortDiscardNonPvid_Type.__name__ = "Integer32"
_FlAcm110MvPortDiscardNonPvid_Object = MibTableColumn
flAcm110MvPortDiscardNonPvid = _FlAcm110MvPortDiscardNonPvid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 30, 20, 1, 5),
    _FlAcm110MvPortDiscardNonPvid_Type()
)
flAcm110MvPortDiscardNonPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortDiscardNonPvid.setStatus("current")
_FlAcm110MvPriority_ObjectIdentity = ObjectIdentity
flAcm110MvPriority = _FlAcm110MvPriority_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40)
)
_FlAcm110MvPriorityConfigTable_Object = MibTable
flAcm110MvPriorityConfigTable = _FlAcm110MvPriorityConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 1)
)
if mibBuilder.loadTexts:
    flAcm110MvPriorityConfigTable.setStatus("current")
_FlAcm110MvPriorityConfigEntry_Object = MibTableRow
flAcm110MvPriorityConfigEntry = _FlAcm110MvPriorityConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 1, 1)
)
flAcm110MvPriorityConfigEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPriorityIndex"),
)
if mibBuilder.loadTexts:
    flAcm110MvPriorityConfigEntry.setStatus("current")


class _FlAcm110MvPriorityIndex_Type(Integer32):
    """Custom type flAcm110MvPriorityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FlAcm110MvPriorityIndex_Type.__name__ = "Integer32"
_FlAcm110MvPriorityIndex_Object = MibTableColumn
flAcm110MvPriorityIndex = _FlAcm110MvPriorityIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 1, 1, 1),
    _FlAcm110MvPriorityIndex_Type()
)
flAcm110MvPriorityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPriorityIndex.setStatus("current")


class _FlAcm110Mv8021pBase_Type(Integer32):
    """Custom type flAcm110Mv8021pBase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FlAcm110Mv8021pBase_Type.__name__ = "Integer32"
_FlAcm110Mv8021pBase_Object = MibTableColumn
flAcm110Mv8021pBase = _FlAcm110Mv8021pBase_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 1, 1, 2),
    _FlAcm110Mv8021pBase_Type()
)
flAcm110Mv8021pBase.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110Mv8021pBase.setStatus("current")


class _FlAcm110MvPriorityRatio_Type(Integer32):
    """Custom type flAcm110MvPriorityRatio based on Integer32"""
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
        *(("alwaysHi", 1),
          ("ratio10-1", 2),
          ("ratio5-1", 3),
          ("ratio2-1", 4))
    )


_FlAcm110MvPriorityRatio_Type.__name__ = "Integer32"
_FlAcm110MvPriorityRatio_Object = MibTableColumn
flAcm110MvPriorityRatio = _FlAcm110MvPriorityRatio_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 1, 1, 3),
    _FlAcm110MvPriorityRatio_Type()
)
flAcm110MvPriorityRatio.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPriorityRatio.setStatus("current")
_FlAcm110MvDscpTable_Object = MibTable
flAcm110MvDscpTable = _FlAcm110MvDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 10)
)
if mibBuilder.loadTexts:
    flAcm110MvDscpTable.setStatus("current")
_FlAcm110MvDscpEntry_Object = MibTableRow
flAcm110MvDscpEntry = _FlAcm110MvDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 10, 1)
)
flAcm110MvDscpEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvDscpCode"),
)
if mibBuilder.loadTexts:
    flAcm110MvDscpEntry.setStatus("current")


class _FlAcm110MvDscpCode_Type(Integer32):
    """Custom type flAcm110MvDscpCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_FlAcm110MvDscpCode_Type.__name__ = "Integer32"
_FlAcm110MvDscpCode_Object = MibTableColumn
flAcm110MvDscpCode = _FlAcm110MvDscpCode_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 10, 1, 1),
    _FlAcm110MvDscpCode_Type()
)
flAcm110MvDscpCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvDscpCode.setStatus("current")


class _FlAcm110MvDscpCodePriority_Type(Integer32):
    """Custom type flAcm110MvDscpCodePriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_FlAcm110MvDscpCodePriority_Type.__name__ = "Integer32"
_FlAcm110MvDscpCodePriority_Object = MibTableColumn
flAcm110MvDscpCodePriority = _FlAcm110MvDscpCodePriority_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 10, 1, 2),
    _FlAcm110MvDscpCodePriority_Type()
)
flAcm110MvDscpCodePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvDscpCodePriority.setStatus("current")
_FlAcm110MvPortPriorityTable_Object = MibTable
flAcm110MvPortPriorityTable = _FlAcm110MvPortPriorityTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 20)
)
if mibBuilder.loadTexts:
    flAcm110MvPortPriorityTable.setStatus("current")
_FlAcm110MvPortPriorityEntry_Object = MibTableRow
flAcm110MvPortPriorityEntry = _FlAcm110MvPortPriorityEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 20, 1)
)
flAcm110MvPortPriorityEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvPortPriorityEntry.setStatus("current")


class _FlAcm110MvPortPriority_Type(Integer32):
    """Custom type flAcm110MvPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("low", 1),
          ("high", 2))
    )


_FlAcm110MvPortPriority_Type.__name__ = "Integer32"
_FlAcm110MvPortPriority_Object = MibTableColumn
flAcm110MvPortPriority = _FlAcm110MvPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 20, 1, 1),
    _FlAcm110MvPortPriority_Type()
)
flAcm110MvPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortPriority.setStatus("current")


class _FlAcm110MvPort8021pClassific_Type(Integer32):
    """Custom type flAcm110MvPort8021pClassific based on Integer32"""
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


_FlAcm110MvPort8021pClassific_Type.__name__ = "Integer32"
_FlAcm110MvPort8021pClassific_Object = MibTableColumn
flAcm110MvPort8021pClassific = _FlAcm110MvPort8021pClassific_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 20, 1, 2),
    _FlAcm110MvPort8021pClassific_Type()
)
flAcm110MvPort8021pClassific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPort8021pClassific.setStatus("current")


class _FlAcm110MvPortDiffServClassific_Type(Integer32):
    """Custom type flAcm110MvPortDiffServClassific based on Integer32"""
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


_FlAcm110MvPortDiffServClassific_Type.__name__ = "Integer32"
_FlAcm110MvPortDiffServClassific_Object = MibTableColumn
flAcm110MvPortDiffServClassific = _FlAcm110MvPortDiffServClassific_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 20, 1, 3),
    _FlAcm110MvPortDiffServClassific_Type()
)
flAcm110MvPortDiffServClassific.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortDiffServClassific.setStatus("current")


class _FlAcm110MvPortUserPriority_Type(Integer32):
    """Custom type flAcm110MvPortUserPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FlAcm110MvPortUserPriority_Type.__name__ = "Integer32"
_FlAcm110MvPortUserPriority_Object = MibTableColumn
flAcm110MvPortUserPriority = _FlAcm110MvPortUserPriority_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 40, 20, 1, 4),
    _FlAcm110MvPortUserPriority_Type()
)
flAcm110MvPortUserPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvPortUserPriority.setStatus("current")
_FlAcm110MvMac_ObjectIdentity = ObjectIdentity
flAcm110MvMac = _FlAcm110MvMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50)
)
_FlAcm110MvGlobalMacTable_Object = MibTable
flAcm110MvGlobalMacTable = _FlAcm110MvGlobalMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 1)
)
if mibBuilder.loadTexts:
    flAcm110MvGlobalMacTable.setStatus("current")
_FlAcm110MvGlobalMacEntry_Object = MibTableRow
flAcm110MvGlobalMacEntry = _FlAcm110MvGlobalMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 1, 1)
)
flAcm110MvGlobalMacEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvGlobalMacIndex"),
)
if mibBuilder.loadTexts:
    flAcm110MvGlobalMacEntry.setStatus("current")


class _FlAcm110MvGlobalMacIndex_Type(Integer32):
    """Custom type flAcm110MvGlobalMacIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_FlAcm110MvGlobalMacIndex_Type.__name__ = "Integer32"
_FlAcm110MvGlobalMacIndex_Object = MibTableColumn
flAcm110MvGlobalMacIndex = _FlAcm110MvGlobalMacIndex_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 1, 1, 1),
    _FlAcm110MvGlobalMacIndex_Type()
)
flAcm110MvGlobalMacIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvGlobalMacIndex.setStatus("current")


class _FlAcm110MvClearDynamicMacTable_Type(Integer32):
    """Custom type flAcm110MvClearDynamicMacTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlAcm110MvClearDynamicMacTable_Type.__name__ = "Integer32"
_FlAcm110MvClearDynamicMacTable_Object = MibTableColumn
flAcm110MvClearDynamicMacTable = _FlAcm110MvClearDynamicMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 1, 1, 2),
    _FlAcm110MvClearDynamicMacTable_Type()
)
flAcm110MvClearDynamicMacTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvClearDynamicMacTable.setStatus("current")


class _FlAcm110MvClearStaticMacTable_Type(Integer32):
    """Custom type flAcm110MvClearStaticMacTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlAcm110MvClearStaticMacTable_Type.__name__ = "Integer32"
_FlAcm110MvClearStaticMacTable_Object = MibTableColumn
flAcm110MvClearStaticMacTable = _FlAcm110MvClearStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 1, 1, 3),
    _FlAcm110MvClearStaticMacTable_Type()
)
flAcm110MvClearStaticMacTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvClearStaticMacTable.setStatus("current")
_FlAcm110MvDynamicMacTable_Object = MibTable
flAcm110MvDynamicMacTable = _FlAcm110MvDynamicMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 10)
)
if mibBuilder.loadTexts:
    flAcm110MvDynamicMacTable.setStatus("current")
_FlAcm110MvDynamicMacEntry_Object = MibTableRow
flAcm110MvDynamicMacEntry = _FlAcm110MvDynamicMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 10, 1)
)
flAcm110MvDynamicMacEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvDynamicEntryNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvDynamicMacEntry.setStatus("current")


class _FlAcm110MvDynamicEntryNumber_Type(Integer32):
    """Custom type flAcm110MvDynamicEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FlAcm110MvDynamicEntryNumber_Type.__name__ = "Integer32"
_FlAcm110MvDynamicEntryNumber_Object = MibTableColumn
flAcm110MvDynamicEntryNumber = _FlAcm110MvDynamicEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 10, 1, 1),
    _FlAcm110MvDynamicEntryNumber_Type()
)
flAcm110MvDynamicEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvDynamicEntryNumber.setStatus("current")
_FlAcm110MvDynamicMacAddress_Type = DisplayString
_FlAcm110MvDynamicMacAddress_Object = MibTableColumn
flAcm110MvDynamicMacAddress = _FlAcm110MvDynamicMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 10, 1, 2),
    _FlAcm110MvDynamicMacAddress_Type()
)
flAcm110MvDynamicMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvDynamicMacAddress.setStatus("current")
_FlAcm110MvDynamicSrcPort_Type = Integer32
_FlAcm110MvDynamicSrcPort_Object = MibTableColumn
flAcm110MvDynamicSrcPort = _FlAcm110MvDynamicSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 10, 1, 3),
    _FlAcm110MvDynamicSrcPort_Type()
)
flAcm110MvDynamicSrcPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvDynamicSrcPort.setStatus("current")


class _FlAcm110MvDynamicFid_Type(Integer32):
    """Custom type flAcm110MvDynamicFid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FlAcm110MvDynamicFid_Type.__name__ = "Integer32"
_FlAcm110MvDynamicFid_Object = MibTableColumn
flAcm110MvDynamicFid = _FlAcm110MvDynamicFid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 10, 1, 4),
    _FlAcm110MvDynamicFid_Type()
)
flAcm110MvDynamicFid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvDynamicFid.setStatus("current")
_FlAcm110MvStaticMacTable_Object = MibTable
flAcm110MvStaticMacTable = _FlAcm110MvStaticMacTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20)
)
if mibBuilder.loadTexts:
    flAcm110MvStaticMacTable.setStatus("current")
_FlAcm110MvStaticMacEntry_Object = MibTableRow
flAcm110MvStaticMacEntry = _FlAcm110MvStaticMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1)
)
flAcm110MvStaticMacEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvStaticEntryNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvStaticMacEntry.setStatus("current")


class _FlAcm110MvStaticEntryNumber_Type(Integer32):
    """Custom type flAcm110MvStaticEntryNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FlAcm110MvStaticEntryNumber_Type.__name__ = "Integer32"
_FlAcm110MvStaticEntryNumber_Object = MibTableColumn
flAcm110MvStaticEntryNumber = _FlAcm110MvStaticEntryNumber_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 1),
    _FlAcm110MvStaticEntryNumber_Type()
)
flAcm110MvStaticEntryNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvStaticEntryNumber.setStatus("current")
_FlAcm110MvStaticMacAddress_Type = DisplayString
_FlAcm110MvStaticMacAddress_Object = MibTableColumn
flAcm110MvStaticMacAddress = _FlAcm110MvStaticMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 2),
    _FlAcm110MvStaticMacAddress_Type()
)
flAcm110MvStaticMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvStaticMacAddress.setStatus("current")


class _FlAcm110MvFwdPort1_Type(Integer32):
    """Custom type flAcm110MvFwdPort1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlAcm110MvFwdPort1_Type.__name__ = "Integer32"
_FlAcm110MvFwdPort1_Object = MibTableColumn
flAcm110MvFwdPort1 = _FlAcm110MvFwdPort1_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 3),
    _FlAcm110MvFwdPort1_Type()
)
flAcm110MvFwdPort1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvFwdPort1.setStatus("current")


class _FlAcm110MvFwdPort2_Type(Integer32):
    """Custom type flAcm110MvFwdPort2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlAcm110MvFwdPort2_Type.__name__ = "Integer32"
_FlAcm110MvFwdPort2_Object = MibTableColumn
flAcm110MvFwdPort2 = _FlAcm110MvFwdPort2_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 4),
    _FlAcm110MvFwdPort2_Type()
)
flAcm110MvFwdPort2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvFwdPort2.setStatus("current")


class _FlAcm110MvFwdPort3_Type(Integer32):
    """Custom type flAcm110MvFwdPort3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlAcm110MvFwdPort3_Type.__name__ = "Integer32"
_FlAcm110MvFwdPort3_Object = MibTableColumn
flAcm110MvFwdPort3 = _FlAcm110MvFwdPort3_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 5),
    _FlAcm110MvFwdPort3_Type()
)
flAcm110MvFwdPort3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvFwdPort3.setStatus("current")


class _FlAcm110MvFwdPort4_Type(Integer32):
    """Custom type flAcm110MvFwdPort4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlAcm110MvFwdPort4_Type.__name__ = "Integer32"
_FlAcm110MvFwdPort4_Object = MibTableColumn
flAcm110MvFwdPort4 = _FlAcm110MvFwdPort4_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 6),
    _FlAcm110MvFwdPort4_Type()
)
flAcm110MvFwdPort4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvFwdPort4.setStatus("current")


class _FlAcm110MvFwdPort5_Type(Integer32):
    """Custom type flAcm110MvFwdPort5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlAcm110MvFwdPort5_Type.__name__ = "Integer32"
_FlAcm110MvFwdPort5_Object = MibTableColumn
flAcm110MvFwdPort5 = _FlAcm110MvFwdPort5_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 7),
    _FlAcm110MvFwdPort5_Type()
)
flAcm110MvFwdPort5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvFwdPort5.setStatus("current")


class _FlAcm110MvFid_Type(Integer32):
    """Custom type flAcm110MvFid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_FlAcm110MvFid_Type.__name__ = "Integer32"
_FlAcm110MvFid_Object = MibTableColumn
flAcm110MvFid = _FlAcm110MvFid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 8),
    _FlAcm110MvFid_Type()
)
flAcm110MvFid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvFid.setStatus("current")


class _FlAcm110MvStaticUseFid_Type(Integer32):
    """Custom type flAcm110MvStaticUseFid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("no", 1),
          ("yes", 2))
    )


_FlAcm110MvStaticUseFid_Type.__name__ = "Integer32"
_FlAcm110MvStaticUseFid_Object = MibTableColumn
flAcm110MvStaticUseFid = _FlAcm110MvStaticUseFid_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 9),
    _FlAcm110MvStaticUseFid_Type()
)
flAcm110MvStaticUseFid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvStaticUseFid.setStatus("current")
_FlAcm110MvStaticTableStatus_Type = EntryStatus
_FlAcm110MvStaticTableStatus_Object = MibTableColumn
flAcm110MvStaticTableStatus = _FlAcm110MvStaticTableStatus_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 50, 20, 1, 10),
    _FlAcm110MvStaticTableStatus_Type()
)
flAcm110MvStaticTableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvStaticTableStatus.setStatus("current")
_FlAcm110MvStatistics_ObjectIdentity = ObjectIdentity
flAcm110MvStatistics = _FlAcm110MvStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60)
)
_FlAcm110MvRxErrorPacketsTable_Object = MibTable
flAcm110MvRxErrorPacketsTable = _FlAcm110MvRxErrorPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 10)
)
if mibBuilder.loadTexts:
    flAcm110MvRxErrorPacketsTable.setStatus("current")
_FlAcm110MvRxErrorPacketsEntry_Object = MibTableRow
flAcm110MvRxErrorPacketsEntry = _FlAcm110MvRxErrorPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 10, 1)
)
flAcm110MvRxErrorPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvRxErrorPacketsEntry.setStatus("current")
_FlAcm110MvRxUndersizePckt_Type = Counter32
_FlAcm110MvRxUndersizePckt_Object = MibTableColumn
flAcm110MvRxUndersizePckt = _FlAcm110MvRxUndersizePckt_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 10, 1, 1),
    _FlAcm110MvRxUndersizePckt_Type()
)
flAcm110MvRxUndersizePckt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxUndersizePckt.setStatus("current")
_FlAcm110MvRxFragmentPckt_Type = Counter32
_FlAcm110MvRxFragmentPckt_Object = MibTableColumn
flAcm110MvRxFragmentPckt = _FlAcm110MvRxFragmentPckt_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 10, 1, 2),
    _FlAcm110MvRxFragmentPckt_Type()
)
flAcm110MvRxFragmentPckt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxFragmentPckt.setStatus("current")
_FlAcm110MvRxOversizePckt_Type = Counter32
_FlAcm110MvRxOversizePckt_Object = MibTableColumn
flAcm110MvRxOversizePckt = _FlAcm110MvRxOversizePckt_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 10, 1, 3),
    _FlAcm110MvRxOversizePckt_Type()
)
flAcm110MvRxOversizePckt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxOversizePckt.setStatus("current")
_FlAcm110MvRxCrcErrorPckt_Type = Counter32
_FlAcm110MvRxCrcErrorPckt_Object = MibTableColumn
flAcm110MvRxCrcErrorPckt = _FlAcm110MvRxCrcErrorPckt_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 10, 1, 4),
    _FlAcm110MvRxCrcErrorPckt_Type()
)
flAcm110MvRxCrcErrorPckt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxCrcErrorPckt.setStatus("current")
_FlAcm110MvRxAlignmentErrorPckt_Type = Counter32
_FlAcm110MvRxAlignmentErrorPckt_Object = MibTableColumn
flAcm110MvRxAlignmentErrorPckt = _FlAcm110MvRxAlignmentErrorPckt_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 10, 1, 5),
    _FlAcm110MvRxAlignmentErrorPckt_Type()
)
flAcm110MvRxAlignmentErrorPckt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxAlignmentErrorPckt.setStatus("current")


class _FlAcm110MvRxRefreshCounters_Type(Integer32):
    """Custom type flAcm110MvRxRefreshCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlAcm110MvRxRefreshCounters_Type.__name__ = "Integer32"
_FlAcm110MvRxRefreshCounters_Object = MibTableColumn
flAcm110MvRxRefreshCounters = _FlAcm110MvRxRefreshCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 10, 1, 6),
    _FlAcm110MvRxRefreshCounters_Type()
)
flAcm110MvRxRefreshCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvRxRefreshCounters.setStatus("current")


class _FlAcm110MvRxClearCounters_Type(Integer32):
    """Custom type flAcm110MvRxClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlAcm110MvRxClearCounters_Type.__name__ = "Integer32"
_FlAcm110MvRxClearCounters_Object = MibTableColumn
flAcm110MvRxClearCounters = _FlAcm110MvRxClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 10, 1, 7),
    _FlAcm110MvRxClearCounters_Type()
)
flAcm110MvRxClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvRxClearCounters.setStatus("current")
_FlAcm110MvRxGoodPacketsTable_Object = MibTable
flAcm110MvRxGoodPacketsTable = _FlAcm110MvRxGoodPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 20)
)
if mibBuilder.loadTexts:
    flAcm110MvRxGoodPacketsTable.setStatus("current")
_FlAcm110MvRxGoodPacketsEntry_Object = MibTableRow
flAcm110MvRxGoodPacketsEntry = _FlAcm110MvRxGoodPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 20, 1)
)
flAcm110MvRxGoodPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvRxGoodPacketsEntry.setStatus("current")
_FlAcm110MvRxUnicastPackets_Type = Counter32
_FlAcm110MvRxUnicastPackets_Object = MibTableColumn
flAcm110MvRxUnicastPackets = _FlAcm110MvRxUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 20, 1, 1),
    _FlAcm110MvRxUnicastPackets_Type()
)
flAcm110MvRxUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxUnicastPackets.setStatus("current")
_FlAcm110MvRxMulticastPackets_Type = Counter32
_FlAcm110MvRxMulticastPackets_Object = MibTableColumn
flAcm110MvRxMulticastPackets = _FlAcm110MvRxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 20, 1, 2),
    _FlAcm110MvRxMulticastPackets_Type()
)
flAcm110MvRxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxMulticastPackets.setStatus("current")
_FlAcm110MvRxBroadcastPackets_Type = Counter32
_FlAcm110MvRxBroadcastPackets_Object = MibTableColumn
flAcm110MvRxBroadcastPackets = _FlAcm110MvRxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 20, 1, 3),
    _FlAcm110MvRxBroadcastPackets_Type()
)
flAcm110MvRxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxBroadcastPackets.setStatus("current")
_FlAcm110MvRxMacControlPackets_Type = Counter32
_FlAcm110MvRxMacControlPackets_Object = MibTableColumn
flAcm110MvRxMacControlPackets = _FlAcm110MvRxMacControlPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 20, 1, 4),
    _FlAcm110MvRxMacControlPackets_Type()
)
flAcm110MvRxMacControlPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxMacControlPackets.setStatus("current")
_FlAcm110MvRxPausePackets_Type = Counter32
_FlAcm110MvRxPausePackets_Object = MibTableColumn
flAcm110MvRxPausePackets = _FlAcm110MvRxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 20, 1, 5),
    _FlAcm110MvRxPausePackets_Type()
)
flAcm110MvRxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxPausePackets.setStatus("current")


class _FlAcm110MvRxGoodRefreshCounters_Type(Integer32):
    """Custom type flAcm110MvRxGoodRefreshCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlAcm110MvRxGoodRefreshCounters_Type.__name__ = "Integer32"
_FlAcm110MvRxGoodRefreshCounters_Object = MibTableColumn
flAcm110MvRxGoodRefreshCounters = _FlAcm110MvRxGoodRefreshCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 20, 1, 6),
    _FlAcm110MvRxGoodRefreshCounters_Type()
)
flAcm110MvRxGoodRefreshCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvRxGoodRefreshCounters.setStatus("current")


class _FlAcm110MvRxGoodClearCounters_Type(Integer32):
    """Custom type flAcm110MvRxGoodClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlAcm110MvRxGoodClearCounters_Type.__name__ = "Integer32"
_FlAcm110MvRxGoodClearCounters_Object = MibTableColumn
flAcm110MvRxGoodClearCounters = _FlAcm110MvRxGoodClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 20, 1, 7),
    _FlAcm110MvRxGoodClearCounters_Type()
)
flAcm110MvRxGoodClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvRxGoodClearCounters.setStatus("current")
_FlAcm110MvTxGoodPacketsTable_Object = MibTable
flAcm110MvTxGoodPacketsTable = _FlAcm110MvTxGoodPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 30)
)
if mibBuilder.loadTexts:
    flAcm110MvTxGoodPacketsTable.setStatus("current")
_FlAcm110MvTxGoodPacketsEntry_Object = MibTableRow
flAcm110MvTxGoodPacketsEntry = _FlAcm110MvTxGoodPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 30, 1)
)
flAcm110MvTxGoodPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvTxGoodPacketsEntry.setStatus("current")
_FlAcm110MvTxUnicastPackets_Type = Counter32
_FlAcm110MvTxUnicastPackets_Object = MibTableColumn
flAcm110MvTxUnicastPackets = _FlAcm110MvTxUnicastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 30, 1, 1),
    _FlAcm110MvTxUnicastPackets_Type()
)
flAcm110MvTxUnicastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxUnicastPackets.setStatus("current")
_FlAcm110MvTxMulticastPackets_Type = Counter32
_FlAcm110MvTxMulticastPackets_Object = MibTableColumn
flAcm110MvTxMulticastPackets = _FlAcm110MvTxMulticastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 30, 1, 2),
    _FlAcm110MvTxMulticastPackets_Type()
)
flAcm110MvTxMulticastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxMulticastPackets.setStatus("current")
_FlAcm110MvTxBroadcastPackets_Type = Counter32
_FlAcm110MvTxBroadcastPackets_Object = MibTableColumn
flAcm110MvTxBroadcastPackets = _FlAcm110MvTxBroadcastPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 30, 1, 3),
    _FlAcm110MvTxBroadcastPackets_Type()
)
flAcm110MvTxBroadcastPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxBroadcastPackets.setStatus("current")
_FlAcm110MvTxPausePackets_Type = Counter32
_FlAcm110MvTxPausePackets_Object = MibTableColumn
flAcm110MvTxPausePackets = _FlAcm110MvTxPausePackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 30, 1, 4),
    _FlAcm110MvTxPausePackets_Type()
)
flAcm110MvTxPausePackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxPausePackets.setStatus("current")


class _FlAcm110MvTxGoodRefreshCounters_Type(Integer32):
    """Custom type flAcm110MvTxGoodRefreshCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlAcm110MvTxGoodRefreshCounters_Type.__name__ = "Integer32"
_FlAcm110MvTxGoodRefreshCounters_Object = MibTableColumn
flAcm110MvTxGoodRefreshCounters = _FlAcm110MvTxGoodRefreshCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 30, 1, 5),
    _FlAcm110MvTxGoodRefreshCounters_Type()
)
flAcm110MvTxGoodRefreshCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvTxGoodRefreshCounters.setStatus("current")


class _FlAcm110MvTxGoodClearCounters_Type(Integer32):
    """Custom type flAcm110MvTxGoodClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlAcm110MvTxGoodClearCounters_Type.__name__ = "Integer32"
_FlAcm110MvTxGoodClearCounters_Object = MibTableColumn
flAcm110MvTxGoodClearCounters = _FlAcm110MvTxGoodClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 30, 1, 6),
    _FlAcm110MvTxGoodClearCounters_Type()
)
flAcm110MvTxGoodClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvTxGoodClearCounters.setStatus("current")
_FlAcm110MvRxTotalPacketsTable_Object = MibTable
flAcm110MvRxTotalPacketsTable = _FlAcm110MvRxTotalPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40)
)
if mibBuilder.loadTexts:
    flAcm110MvRxTotalPacketsTable.setStatus("current")
_FlAcm110MvRxTotalPacketsEntry_Object = MibTableRow
flAcm110MvRxTotalPacketsEntry = _FlAcm110MvRxTotalPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1)
)
flAcm110MvRxTotalPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvRxTotalPacketsEntry.setStatus("current")
_FlAcm110MvRxDroppedPackets_Type = Counter32
_FlAcm110MvRxDroppedPackets_Object = MibTableColumn
flAcm110MvRxDroppedPackets = _FlAcm110MvRxDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1, 1),
    _FlAcm110MvRxDroppedPackets_Type()
)
flAcm110MvRxDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRxDroppedPackets.setStatus("current")
_FlAcm110MvRx64BytesPackets_Type = Counter32
_FlAcm110MvRx64BytesPackets_Object = MibTableColumn
flAcm110MvRx64BytesPackets = _FlAcm110MvRx64BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1, 2),
    _FlAcm110MvRx64BytesPackets_Type()
)
flAcm110MvRx64BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRx64BytesPackets.setStatus("current")
_FlAcm110MvRx65_127BytesPackets_Type = Counter32
_FlAcm110MvRx65_127BytesPackets_Object = MibTableColumn
flAcm110MvRx65_127BytesPackets = _FlAcm110MvRx65_127BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1, 3),
    _FlAcm110MvRx65_127BytesPackets_Type()
)
flAcm110MvRx65_127BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRx65_127BytesPackets.setStatus("current")
_FlAcm110MvRx128_255BytesPackets_Type = Counter32
_FlAcm110MvRx128_255BytesPackets_Object = MibTableColumn
flAcm110MvRx128_255BytesPackets = _FlAcm110MvRx128_255BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1, 4),
    _FlAcm110MvRx128_255BytesPackets_Type()
)
flAcm110MvRx128_255BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRx128_255BytesPackets.setStatus("current")
_FlAcm110MvRx256_511BytesPackets_Type = Counter32
_FlAcm110MvRx256_511BytesPackets_Object = MibTableColumn
flAcm110MvRx256_511BytesPackets = _FlAcm110MvRx256_511BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1, 5),
    _FlAcm110MvRx256_511BytesPackets_Type()
)
flAcm110MvRx256_511BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRx256_511BytesPackets.setStatus("current")
_FlAcm110MvRx512_1023BytesPackets_Type = Counter32
_FlAcm110MvRx512_1023BytesPackets_Object = MibTableColumn
flAcm110MvRx512_1023BytesPackets = _FlAcm110MvRx512_1023BytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1, 6),
    _FlAcm110MvRx512_1023BytesPackets_Type()
)
flAcm110MvRx512_1023BytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRx512_1023BytesPackets.setStatus("current")
_FlAcm110MvRx1024_MaxBytesPackets_Type = Counter32
_FlAcm110MvRx1024_MaxBytesPackets_Object = MibTableColumn
flAcm110MvRx1024_MaxBytesPackets = _FlAcm110MvRx1024_MaxBytesPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1, 7),
    _FlAcm110MvRx1024_MaxBytesPackets_Type()
)
flAcm110MvRx1024_MaxBytesPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvRx1024_MaxBytesPackets.setStatus("current")


class _FlAcm110MvRxTotalRefreshCounters_Type(Integer32):
    """Custom type flAcm110MvRxTotalRefreshCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlAcm110MvRxTotalRefreshCounters_Type.__name__ = "Integer32"
_FlAcm110MvRxTotalRefreshCounters_Object = MibTableColumn
flAcm110MvRxTotalRefreshCounters = _FlAcm110MvRxTotalRefreshCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1, 8),
    _FlAcm110MvRxTotalRefreshCounters_Type()
)
flAcm110MvRxTotalRefreshCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvRxTotalRefreshCounters.setStatus("current")


class _FlAcm110MvRxTotalClearCounters_Type(Integer32):
    """Custom type flAcm110MvRxTotalClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlAcm110MvRxTotalClearCounters_Type.__name__ = "Integer32"
_FlAcm110MvRxTotalClearCounters_Object = MibTableColumn
flAcm110MvRxTotalClearCounters = _FlAcm110MvRxTotalClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 40, 1, 9),
    _FlAcm110MvRxTotalClearCounters_Type()
)
flAcm110MvRxTotalClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvRxTotalClearCounters.setStatus("current")
_FlAcm110MvTxTotalPacketsTable_Object = MibTable
flAcm110MvTxTotalPacketsTable = _FlAcm110MvTxTotalPacketsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 50)
)
if mibBuilder.loadTexts:
    flAcm110MvTxTotalPacketsTable.setStatus("current")
_FlAcm110MvTxTotalPacketsEntry_Object = MibTableRow
flAcm110MvTxTotalPacketsEntry = _FlAcm110MvTxTotalPacketsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 50, 1)
)
flAcm110MvTxTotalPacketsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvTxTotalPacketsEntry.setStatus("current")
_FlAcm110MvTxDroppedPackets_Type = Counter32
_FlAcm110MvTxDroppedPackets_Object = MibTableColumn
flAcm110MvTxDroppedPackets = _FlAcm110MvTxDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 50, 1, 1),
    _FlAcm110MvTxDroppedPackets_Type()
)
flAcm110MvTxDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxDroppedPackets.setStatus("current")


class _FlAcm110MvTxTotalRefreshCounters_Type(Integer32):
    """Custom type flAcm110MvTxTotalRefreshCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlAcm110MvTxTotalRefreshCounters_Type.__name__ = "Integer32"
_FlAcm110MvTxTotalRefreshCounters_Object = MibTableColumn
flAcm110MvTxTotalRefreshCounters = _FlAcm110MvTxTotalRefreshCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 50, 1, 2),
    _FlAcm110MvTxTotalRefreshCounters_Type()
)
flAcm110MvTxTotalRefreshCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvTxTotalRefreshCounters.setStatus("current")


class _FlAcm110MvTxTotalClearCounters_Type(Integer32):
    """Custom type flAcm110MvTxTotalClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlAcm110MvTxTotalClearCounters_Type.__name__ = "Integer32"
_FlAcm110MvTxTotalClearCounters_Object = MibTableColumn
flAcm110MvTxTotalClearCounters = _FlAcm110MvTxTotalClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 50, 1, 3),
    _FlAcm110MvTxTotalClearCounters_Type()
)
flAcm110MvTxTotalClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvTxTotalClearCounters.setStatus("current")
_FlAcm110MvTxCollisionsTable_Object = MibTable
flAcm110MvTxCollisionsTable = _FlAcm110MvTxCollisionsTable_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 60)
)
if mibBuilder.loadTexts:
    flAcm110MvTxCollisionsTable.setStatus("current")
_FlAcm110MvTxCollisionsEntry_Object = MibTableRow
flAcm110MvTxCollisionsEntry = _FlAcm110MvTxCollisionsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 60, 1)
)
flAcm110MvTxCollisionsEntry.setIndexNames(
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisMvIndex"),
    (0, "FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModuleMvIndex"),
    (0, "FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
)
if mibBuilder.loadTexts:
    flAcm110MvTxCollisionsEntry.setStatus("current")
_FlAcm110MvTxTotalCols_Type = Counter32
_FlAcm110MvTxTotalCols_Object = MibTableColumn
flAcm110MvTxTotalCols = _FlAcm110MvTxTotalCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 60, 1, 1),
    _FlAcm110MvTxTotalCols_Type()
)
flAcm110MvTxTotalCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxTotalCols.setStatus("current")
_FlAcm110MvTxLateCols_Type = Counter32
_FlAcm110MvTxLateCols_Object = MibTableColumn
flAcm110MvTxLateCols = _FlAcm110MvTxLateCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 60, 1, 2),
    _FlAcm110MvTxLateCols_Type()
)
flAcm110MvTxLateCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxLateCols.setStatus("current")
_FlAcm110MvTxExcessiveCols_Type = Counter32
_FlAcm110MvTxExcessiveCols_Object = MibTableColumn
flAcm110MvTxExcessiveCols = _FlAcm110MvTxExcessiveCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 60, 1, 3),
    _FlAcm110MvTxExcessiveCols_Type()
)
flAcm110MvTxExcessiveCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxExcessiveCols.setStatus("current")
_FlAcm110MvTxSingleCols_Type = Counter32
_FlAcm110MvTxSingleCols_Object = MibTableColumn
flAcm110MvTxSingleCols = _FlAcm110MvTxSingleCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 60, 1, 4),
    _FlAcm110MvTxSingleCols_Type()
)
flAcm110MvTxSingleCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxSingleCols.setStatus("current")
_FlAcm110MvTxMultipleCols_Type = Counter32
_FlAcm110MvTxMultipleCols_Object = MibTableColumn
flAcm110MvTxMultipleCols = _FlAcm110MvTxMultipleCols_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 60, 1, 5),
    _FlAcm110MvTxMultipleCols_Type()
)
flAcm110MvTxMultipleCols.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flAcm110MvTxMultipleCols.setStatus("current")


class _FlAcm110MvTxColRefreshCounters_Type(Integer32):
    """Custom type flAcm110MvTxColRefreshCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("refresh", 2))
    )


_FlAcm110MvTxColRefreshCounters_Type.__name__ = "Integer32"
_FlAcm110MvTxColRefreshCounters_Object = MibTableColumn
flAcm110MvTxColRefreshCounters = _FlAcm110MvTxColRefreshCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 60, 1, 6),
    _FlAcm110MvTxColRefreshCounters_Type()
)
flAcm110MvTxColRefreshCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvTxColRefreshCounters.setStatus("current")


class _FlAcm110MvTxColClearCounters_Type(Integer32):
    """Custom type flAcm110MvTxColClearCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("clear", 2))
    )


_FlAcm110MvTxColClearCounters_Type.__name__ = "Integer32"
_FlAcm110MvTxColClearCounters_Object = MibTableColumn
flAcm110MvTxColClearCounters = _FlAcm110MvTxColClearCounters_Object(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 60, 60, 1, 7),
    _FlAcm110MvTxColClearCounters_Type()
)
flAcm110MvTxColClearCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    flAcm110MvTxColClearCounters.setStatus("current")

# Managed Objects groups

flAcm110MvGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 1)
)
flAcm110MvGlobalGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalConfigIndex"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalBufferShare"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalMulticastProtect"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalBroadcastRate"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalMaxPacketSize"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalSleLogic"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalSlePort1"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalSlePort2"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalSlePort3"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalSlePort4"))
)
if mibBuilder.loadTexts:
    flAcm110MvGlobalGroup.setStatus("current")

flAcm110MvPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 2)
)
flAcm110MvPortsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvPortNumber"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortType"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortLink"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortDescription"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortAutoNego"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortDuplex"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortDatarate"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortEnabled"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortAutoCross"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortMdix"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortFef"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortReset"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortBroadcastProtect"))
)
if mibBuilder.loadTexts:
    flAcm110MvPortsGroup.setStatus("current")

flAcm110MvVlansDefGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 3)
)
flAcm110MvVlansDefGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvVlanConfigIndex"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlan8021q"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlanNullVidReplace"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvCreateDefaultVlans"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvDeleteAllVlans"))
)
if mibBuilder.loadTexts:
    flAcm110MvVlansDefGroup.setStatus("current")

flAcm110MvVlansTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 4)
)
flAcm110MvVlansTableGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvVlanFid"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlanVid"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlanName"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlanPort1Member"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlanPort2Member"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlanPort3Member"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlanPort4Member"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlanPort5Member"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlanTableStatus"))
)
if mibBuilder.loadTexts:
    flAcm110MvVlansTableGroup.setStatus("current")

flAcm110MvVlansPortsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 5)
)
flAcm110MvVlansPortsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvPortIngressFilter"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortTagInsertion"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortTagRemoval"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortVid"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortDiscardNonPvid"))
)
if mibBuilder.loadTexts:
    flAcm110MvVlansPortsGroup.setStatus("current")

flAcm110MvPrioritiesConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 6)
)
flAcm110MvPrioritiesConfigGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvPriorityIndex"),
        ("FIBROLAN-MIB-ACM110", "flAcm110Mv8021pBase"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPriorityRatio"))
)
if mibBuilder.loadTexts:
    flAcm110MvPrioritiesConfigGroup.setStatus("current")

flAcm110MvPriorityDscpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 7)
)
flAcm110MvPriorityDscpGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvDscpCode"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvDscpCodePriority"))
)
if mibBuilder.loadTexts:
    flAcm110MvPriorityDscpGroup.setStatus("current")

flAcm110MvPortPriorityTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 8)
)
flAcm110MvPortPriorityTableGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvPortPriority"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPort8021pClassific"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortDiffServClassific"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortUserPriority"))
)
if mibBuilder.loadTexts:
    flAcm110MvPortPriorityTableGroup.setStatus("current")

flAcm110MvGlobalMacsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 9)
)
flAcm110MvGlobalMacsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalMacIndex"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvClearDynamicMacTable"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvClearStaticMacTable"))
)
if mibBuilder.loadTexts:
    flAcm110MvGlobalMacsGroup.setStatus("current")

flAcm110MvDynamicMacsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 10)
)
flAcm110MvDynamicMacsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvDynamicEntryNumber"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvDynamicMacAddress"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvDynamicSrcPort"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvDynamicFid"))
)
if mibBuilder.loadTexts:
    flAcm110MvDynamicMacsGroup.setStatus("current")

flAcm110MvStaticMacsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 11)
)
flAcm110MvStaticMacsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvStaticEntryNumber"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvStaticMacAddress"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvFwdPort1"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvFwdPort2"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvFwdPort3"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvFwdPort4"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvFwdPort5"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvFid"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvStaticUseFid"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvStaticTableStatus"))
)
if mibBuilder.loadTexts:
    flAcm110MvStaticMacsGroup.setStatus("current")

flAcm110MvRxErrStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 12)
)
flAcm110MvRxErrStatisticsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvRxUndersizePckt"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxFragmentPckt"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxOversizePckt"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxCrcErrorPckt"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxAlignmentErrorPckt"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxRefreshCounters"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxClearCounters"))
)
if mibBuilder.loadTexts:
    flAcm110MvRxErrStatisticsGroup.setStatus("current")

flAcm110MvRxGoodStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 13)
)
flAcm110MvRxGoodStatisticsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvRxUnicastPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxMulticastPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxBroadcastPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxMacControlPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxPausePackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxGoodRefreshCounters"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxGoodClearCounters"))
)
if mibBuilder.loadTexts:
    flAcm110MvRxGoodStatisticsGroup.setStatus("current")

flAcm110MvTxGoodStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 14)
)
flAcm110MvTxGoodStatisticsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvTxUnicastPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxMulticastPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxBroadcastPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxPausePackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxGoodRefreshCounters"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxGoodClearCounters"))
)
if mibBuilder.loadTexts:
    flAcm110MvTxGoodStatisticsGroup.setStatus("current")

flAcm110MvRxTotalStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 15)
)
flAcm110MvRxTotalStatisticsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvRxDroppedPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRx64BytesPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRx65-127BytesPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRx128-255BytesPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRx256-511BytesPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRx512-1023BytesPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRx1024-MaxBytesPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxTotalRefreshCounters"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxTotalClearCounters"))
)
if mibBuilder.loadTexts:
    flAcm110MvRxTotalStatisticsGroup.setStatus("current")

flAcm110MvTxTotalStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 16)
)
flAcm110MvTxTotalStatisticsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvTxDroppedPackets"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxTotalRefreshCounters"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxTotalClearCounters"))
)
if mibBuilder.loadTexts:
    flAcm110MvTxTotalStatisticsGroup.setStatus("current")

flAcm110MvTxCollisionStatisticsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 2, 17)
)
flAcm110MvTxCollisionStatisticsGroup.setObjects(
      *(("FIBROLAN-MIB-ACM110", "flAcm110MvTxTotalCols"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxLateCols"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxExcessiveCols"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxSingleCols"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxMultipleCols"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxColRefreshCounters"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxColClearCounters"))
)
if mibBuilder.loadTexts:
    flAcm110MvTxCollisionStatisticsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flAcm110MIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4467, 100, 500, 10, 30, 120, 1, 1, 1)
)
flAcm110MIBCompliance.setObjects(
      *(("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisGroup"),
        ("FIBROLAN-MIB-METRO-STAR-MV", "flMsChassisModulesGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlansDefGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlansTableGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvVlansPortsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPrioritiesConfigGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPriorityDscpGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvPortPriorityTableGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvGlobalMacsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvDynamicMacsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvStaticMacsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxErrStatisticsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxGoodStatisticsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxGoodStatisticsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvRxTotalStatisticsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxTotalStatisticsGroup"),
        ("FIBROLAN-MIB-ACM110", "flAcm110MvTxCollisionStatisticsGroup"))
)
if mibBuilder.loadTexts:
    flAcm110MIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIBROLAN-MIB-ACM110",
    **{"EntryStatus": EntryStatus,
       "fibrolan": fibrolan,
       "fibrolanSNMP": fibrolanSNMP,
       "flMetroStarMv": flMetroStarMv,
       "flMsChassisMv": flMsChassisMv,
       "flMsModuleMv": flMsModuleMv,
       "flAcm110Mv": flAcm110Mv,
       "flAcm110MIBConformance": flAcm110MIBConformance,
       "flAcm110MIBCompliances": flAcm110MIBCompliances,
       "flAcm110MIBCompliance": flAcm110MIBCompliance,
       "flAcm110MIBGroups": flAcm110MIBGroups,
       "flAcm110MvGlobalGroup": flAcm110MvGlobalGroup,
       "flAcm110MvPortsGroup": flAcm110MvPortsGroup,
       "flAcm110MvVlansDefGroup": flAcm110MvVlansDefGroup,
       "flAcm110MvVlansTableGroup": flAcm110MvVlansTableGroup,
       "flAcm110MvVlansPortsGroup": flAcm110MvVlansPortsGroup,
       "flAcm110MvPrioritiesConfigGroup": flAcm110MvPrioritiesConfigGroup,
       "flAcm110MvPriorityDscpGroup": flAcm110MvPriorityDscpGroup,
       "flAcm110MvPortPriorityTableGroup": flAcm110MvPortPriorityTableGroup,
       "flAcm110MvGlobalMacsGroup": flAcm110MvGlobalMacsGroup,
       "flAcm110MvDynamicMacsGroup": flAcm110MvDynamicMacsGroup,
       "flAcm110MvStaticMacsGroup": flAcm110MvStaticMacsGroup,
       "flAcm110MvRxErrStatisticsGroup": flAcm110MvRxErrStatisticsGroup,
       "flAcm110MvRxGoodStatisticsGroup": flAcm110MvRxGoodStatisticsGroup,
       "flAcm110MvTxGoodStatisticsGroup": flAcm110MvTxGoodStatisticsGroup,
       "flAcm110MvRxTotalStatisticsGroup": flAcm110MvRxTotalStatisticsGroup,
       "flAcm110MvTxTotalStatisticsGroup": flAcm110MvTxTotalStatisticsGroup,
       "flAcm110MvTxCollisionStatisticsGroup": flAcm110MvTxCollisionStatisticsGroup,
       "flAcm110MvGlobal": flAcm110MvGlobal,
       "flAcm110MvGlobalConfigTable": flAcm110MvGlobalConfigTable,
       "flAcm110MvGlobalConfigEntry": flAcm110MvGlobalConfigEntry,
       "flAcm110MvGlobalConfigIndex": flAcm110MvGlobalConfigIndex,
       "flAcm110MvGlobalBufferShare": flAcm110MvGlobalBufferShare,
       "flAcm110MvGlobalMulticastProtect": flAcm110MvGlobalMulticastProtect,
       "flAcm110MvGlobalBroadcastRate": flAcm110MvGlobalBroadcastRate,
       "flAcm110MvGlobalMaxPacketSize": flAcm110MvGlobalMaxPacketSize,
       "flAcm110MvGlobalSleLogic": flAcm110MvGlobalSleLogic,
       "flAcm110MvGlobalSlePort1": flAcm110MvGlobalSlePort1,
       "flAcm110MvGlobalSlePort2": flAcm110MvGlobalSlePort2,
       "flAcm110MvGlobalSlePort3": flAcm110MvGlobalSlePort3,
       "flAcm110MvGlobalSlePort4": flAcm110MvGlobalSlePort4,
       "flAcm110MvPorts": flAcm110MvPorts,
       "flAcm110MvPortConfigTable": flAcm110MvPortConfigTable,
       "flAcm110MvPortConfigEntry": flAcm110MvPortConfigEntry,
       "flAcm110MvPortNumber": flAcm110MvPortNumber,
       "flAcm110MvPortType": flAcm110MvPortType,
       "flAcm110MvPortLink": flAcm110MvPortLink,
       "flAcm110MvPortDescription": flAcm110MvPortDescription,
       "flAcm110MvPortAutoNego": flAcm110MvPortAutoNego,
       "flAcm110MvPortDuplex": flAcm110MvPortDuplex,
       "flAcm110MvPortDatarate": flAcm110MvPortDatarate,
       "flAcm110MvPortEnabled": flAcm110MvPortEnabled,
       "flAcm110MvPortAutoCross": flAcm110MvPortAutoCross,
       "flAcm110MvPortMdix": flAcm110MvPortMdix,
       "flAcm110MvPortFef": flAcm110MvPortFef,
       "flAcm110MvPortReset": flAcm110MvPortReset,
       "flAcm110MvPortBroadcastProtect": flAcm110MvPortBroadcastProtect,
       "flAcm110MvPortBwConfigTable": flAcm110MvPortBwConfigTable,
       "flAcm110MvPortBwConfigEntry": flAcm110MvPortBwConfigEntry,
       "flAcm110MvPortRxHighBw": flAcm110MvPortRxHighBw,
       "flAcm110MvPortTxHighBw": flAcm110MvPortTxHighBw,
       "flAcm110MvPortRxLowBw": flAcm110MvPortRxLowBw,
       "flAcm110MvPortTxLowBw": flAcm110MvPortTxLowBw,
       "flAcm110MvPortRxDiffBw": flAcm110MvPortRxDiffBw,
       "flAcm110MvPortRxHighFlowControl": flAcm110MvPortRxHighFlowControl,
       "flAcm110MvPortRxLowFlowControl": flAcm110MvPortRxLowFlowControl,
       "flAcm110MvPortTxDiffBw": flAcm110MvPortTxDiffBw,
       "flAcm110MvVlan": flAcm110MvVlan,
       "flAcm110MvGlobalVlanConfigTable": flAcm110MvGlobalVlanConfigTable,
       "flAcm110MvGlobalVlanConfigEntry": flAcm110MvGlobalVlanConfigEntry,
       "flAcm110MvVlanConfigIndex": flAcm110MvVlanConfigIndex,
       "flAcm110MvVlan8021q": flAcm110MvVlan8021q,
       "flAcm110MvVlanNullVidReplace": flAcm110MvVlanNullVidReplace,
       "flAcm110MvCreateDefaultVlans": flAcm110MvCreateDefaultVlans,
       "flAcm110MvDeleteAllVlans": flAcm110MvDeleteAllVlans,
       "flAcm110MvVlanTable": flAcm110MvVlanTable,
       "flAcm110MvVlanEntry": flAcm110MvVlanEntry,
       "flAcm110MvVlanFid": flAcm110MvVlanFid,
       "flAcm110MvVlanVid": flAcm110MvVlanVid,
       "flAcm110MvVlanName": flAcm110MvVlanName,
       "flAcm110MvVlanPort1Member": flAcm110MvVlanPort1Member,
       "flAcm110MvVlanPort2Member": flAcm110MvVlanPort2Member,
       "flAcm110MvVlanPort3Member": flAcm110MvVlanPort3Member,
       "flAcm110MvVlanPort4Member": flAcm110MvVlanPort4Member,
       "flAcm110MvVlanPort5Member": flAcm110MvVlanPort5Member,
       "flAcm110MvVlanTableStatus": flAcm110MvVlanTableStatus,
       "flAcm110MvPortVlanConfigTable": flAcm110MvPortVlanConfigTable,
       "flAcm110MvPortVlanConfigEntry": flAcm110MvPortVlanConfigEntry,
       "flAcm110MvPortIngressFilter": flAcm110MvPortIngressFilter,
       "flAcm110MvPortTagInsertion": flAcm110MvPortTagInsertion,
       "flAcm110MvPortTagRemoval": flAcm110MvPortTagRemoval,
       "flAcm110MvPortVid": flAcm110MvPortVid,
       "flAcm110MvPortDiscardNonPvid": flAcm110MvPortDiscardNonPvid,
       "flAcm110MvPriority": flAcm110MvPriority,
       "flAcm110MvPriorityConfigTable": flAcm110MvPriorityConfigTable,
       "flAcm110MvPriorityConfigEntry": flAcm110MvPriorityConfigEntry,
       "flAcm110MvPriorityIndex": flAcm110MvPriorityIndex,
       "flAcm110Mv8021pBase": flAcm110Mv8021pBase,
       "flAcm110MvPriorityRatio": flAcm110MvPriorityRatio,
       "flAcm110MvDscpTable": flAcm110MvDscpTable,
       "flAcm110MvDscpEntry": flAcm110MvDscpEntry,
       "flAcm110MvDscpCode": flAcm110MvDscpCode,
       "flAcm110MvDscpCodePriority": flAcm110MvDscpCodePriority,
       "flAcm110MvPortPriorityTable": flAcm110MvPortPriorityTable,
       "flAcm110MvPortPriorityEntry": flAcm110MvPortPriorityEntry,
       "flAcm110MvPortPriority": flAcm110MvPortPriority,
       "flAcm110MvPort8021pClassific": flAcm110MvPort8021pClassific,
       "flAcm110MvPortDiffServClassific": flAcm110MvPortDiffServClassific,
       "flAcm110MvPortUserPriority": flAcm110MvPortUserPriority,
       "flAcm110MvMac": flAcm110MvMac,
       "flAcm110MvGlobalMacTable": flAcm110MvGlobalMacTable,
       "flAcm110MvGlobalMacEntry": flAcm110MvGlobalMacEntry,
       "flAcm110MvGlobalMacIndex": flAcm110MvGlobalMacIndex,
       "flAcm110MvClearDynamicMacTable": flAcm110MvClearDynamicMacTable,
       "flAcm110MvClearStaticMacTable": flAcm110MvClearStaticMacTable,
       "flAcm110MvDynamicMacTable": flAcm110MvDynamicMacTable,
       "flAcm110MvDynamicMacEntry": flAcm110MvDynamicMacEntry,
       "flAcm110MvDynamicEntryNumber": flAcm110MvDynamicEntryNumber,
       "flAcm110MvDynamicMacAddress": flAcm110MvDynamicMacAddress,
       "flAcm110MvDynamicSrcPort": flAcm110MvDynamicSrcPort,
       "flAcm110MvDynamicFid": flAcm110MvDynamicFid,
       "flAcm110MvStaticMacTable": flAcm110MvStaticMacTable,
       "flAcm110MvStaticMacEntry": flAcm110MvStaticMacEntry,
       "flAcm110MvStaticEntryNumber": flAcm110MvStaticEntryNumber,
       "flAcm110MvStaticMacAddress": flAcm110MvStaticMacAddress,
       "flAcm110MvFwdPort1": flAcm110MvFwdPort1,
       "flAcm110MvFwdPort2": flAcm110MvFwdPort2,
       "flAcm110MvFwdPort3": flAcm110MvFwdPort3,
       "flAcm110MvFwdPort4": flAcm110MvFwdPort4,
       "flAcm110MvFwdPort5": flAcm110MvFwdPort5,
       "flAcm110MvFid": flAcm110MvFid,
       "flAcm110MvStaticUseFid": flAcm110MvStaticUseFid,
       "flAcm110MvStaticTableStatus": flAcm110MvStaticTableStatus,
       "flAcm110MvStatistics": flAcm110MvStatistics,
       "flAcm110MvRxErrorPacketsTable": flAcm110MvRxErrorPacketsTable,
       "flAcm110MvRxErrorPacketsEntry": flAcm110MvRxErrorPacketsEntry,
       "flAcm110MvRxUndersizePckt": flAcm110MvRxUndersizePckt,
       "flAcm110MvRxFragmentPckt": flAcm110MvRxFragmentPckt,
       "flAcm110MvRxOversizePckt": flAcm110MvRxOversizePckt,
       "flAcm110MvRxCrcErrorPckt": flAcm110MvRxCrcErrorPckt,
       "flAcm110MvRxAlignmentErrorPckt": flAcm110MvRxAlignmentErrorPckt,
       "flAcm110MvRxRefreshCounters": flAcm110MvRxRefreshCounters,
       "flAcm110MvRxClearCounters": flAcm110MvRxClearCounters,
       "flAcm110MvRxGoodPacketsTable": flAcm110MvRxGoodPacketsTable,
       "flAcm110MvRxGoodPacketsEntry": flAcm110MvRxGoodPacketsEntry,
       "flAcm110MvRxUnicastPackets": flAcm110MvRxUnicastPackets,
       "flAcm110MvRxMulticastPackets": flAcm110MvRxMulticastPackets,
       "flAcm110MvRxBroadcastPackets": flAcm110MvRxBroadcastPackets,
       "flAcm110MvRxMacControlPackets": flAcm110MvRxMacControlPackets,
       "flAcm110MvRxPausePackets": flAcm110MvRxPausePackets,
       "flAcm110MvRxGoodRefreshCounters": flAcm110MvRxGoodRefreshCounters,
       "flAcm110MvRxGoodClearCounters": flAcm110MvRxGoodClearCounters,
       "flAcm110MvTxGoodPacketsTable": flAcm110MvTxGoodPacketsTable,
       "flAcm110MvTxGoodPacketsEntry": flAcm110MvTxGoodPacketsEntry,
       "flAcm110MvTxUnicastPackets": flAcm110MvTxUnicastPackets,
       "flAcm110MvTxMulticastPackets": flAcm110MvTxMulticastPackets,
       "flAcm110MvTxBroadcastPackets": flAcm110MvTxBroadcastPackets,
       "flAcm110MvTxPausePackets": flAcm110MvTxPausePackets,
       "flAcm110MvTxGoodRefreshCounters": flAcm110MvTxGoodRefreshCounters,
       "flAcm110MvTxGoodClearCounters": flAcm110MvTxGoodClearCounters,
       "flAcm110MvRxTotalPacketsTable": flAcm110MvRxTotalPacketsTable,
       "flAcm110MvRxTotalPacketsEntry": flAcm110MvRxTotalPacketsEntry,
       "flAcm110MvRxDroppedPackets": flAcm110MvRxDroppedPackets,
       "flAcm110MvRx64BytesPackets": flAcm110MvRx64BytesPackets,
       "flAcm110MvRx65-127BytesPackets": flAcm110MvRx65_127BytesPackets,
       "flAcm110MvRx128-255BytesPackets": flAcm110MvRx128_255BytesPackets,
       "flAcm110MvRx256-511BytesPackets": flAcm110MvRx256_511BytesPackets,
       "flAcm110MvRx512-1023BytesPackets": flAcm110MvRx512_1023BytesPackets,
       "flAcm110MvRx1024-MaxBytesPackets": flAcm110MvRx1024_MaxBytesPackets,
       "flAcm110MvRxTotalRefreshCounters": flAcm110MvRxTotalRefreshCounters,
       "flAcm110MvRxTotalClearCounters": flAcm110MvRxTotalClearCounters,
       "flAcm110MvTxTotalPacketsTable": flAcm110MvTxTotalPacketsTable,
       "flAcm110MvTxTotalPacketsEntry": flAcm110MvTxTotalPacketsEntry,
       "flAcm110MvTxDroppedPackets": flAcm110MvTxDroppedPackets,
       "flAcm110MvTxTotalRefreshCounters": flAcm110MvTxTotalRefreshCounters,
       "flAcm110MvTxTotalClearCounters": flAcm110MvTxTotalClearCounters,
       "flAcm110MvTxCollisionsTable": flAcm110MvTxCollisionsTable,
       "flAcm110MvTxCollisionsEntry": flAcm110MvTxCollisionsEntry,
       "flAcm110MvTxTotalCols": flAcm110MvTxTotalCols,
       "flAcm110MvTxLateCols": flAcm110MvTxLateCols,
       "flAcm110MvTxExcessiveCols": flAcm110MvTxExcessiveCols,
       "flAcm110MvTxSingleCols": flAcm110MvTxSingleCols,
       "flAcm110MvTxMultipleCols": flAcm110MvTxMultipleCols,
       "flAcm110MvTxColRefreshCounters": flAcm110MvTxColRefreshCounters,
       "flAcm110MvTxColClearCounters": flAcm110MvTxColClearCounters}
)
