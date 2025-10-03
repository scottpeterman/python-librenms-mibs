# SNMP MIB module (SLE-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\dasan\SLE-CONFIG-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:34:21 2025
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

(dasan,) = mibBuilder.importSymbols(
    "DASAN-SMI",
    "dasan")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

sleMibConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1)
)


# Types definitions



class SleVersionType(Integer32):
    """Custom type SleVersionType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("undef", 0),
          ("one", 1),
          ("two", 2),
          ("three", 3),
          ("four", 4),
          ("five", 5),
          ("six", 6),
          ("seven", 7))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SleConfigMgmt_ObjectIdentity = ObjectIdentity
sleConfigMgmt = _SleConfigMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 100)
)
if mibBuilder.loadTexts:
    sleConfigMgmt.setStatus("current")
_SleMibConfInfo_ObjectIdentity = ObjectIdentity
sleMibConfInfo = _SleMibConfInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 1)
)
_SleMibConfInfoTable_Object = MibTable
sleMibConfInfoTable = _SleMibConfInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 1, 1)
)
if mibBuilder.loadTexts:
    sleMibConfInfoTable.setStatus("current")
_SleMibConfInfoEntry_Object = MibTableRow
sleMibConfInfoEntry = _SleMibConfInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 1, 1, 1)
)
sleMibConfInfoEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleMibConfIndex"),
)
if mibBuilder.loadTexts:
    sleMibConfInfoEntry.setStatus("current")


class _SleMibConfIndex_Type(Integer32):
    """Custom type sleMibConfIndex based on Integer32"""
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
              11,
              12,
              13,
              14,
              20,
              21,
              22,
              99)
        )
    )
    namedValues = NamedValues(
        *(("systemManagement", 1),
          ("device", 2),
          ("bridge", 3),
          ("faultManagement", 4),
          ("performanceManagement", 5),
          ("dhcp", 6),
          ("security", 7),
          ("snmp", 8),
          ("rmon", 9),
          ("qos", 10),
          ("network", 11),
          ("multicast", 12),
          ("dhcpSnooping", 13),
          ("mvQos", 14),
          ("epon", 20),
          ("sFlow", 21),
          ("red", 22),
          ("debug", 99))
    )


_SleMibConfIndex_Type.__name__ = "Integer32"
_SleMibConfIndex_Object = MibTableColumn
sleMibConfIndex = _SleMibConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 1, 1, 1, 1),
    _SleMibConfIndex_Type()
)
sleMibConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMibConfIndex.setStatus("current")
_SleMibConfVersion_Type = SleVersionType
_SleMibConfVersion_Object = MibTableColumn
sleMibConfVersion = _SleMibConfVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 1, 1, 1, 2),
    _SleMibConfVersion_Type()
)
sleMibConfVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMibConfVersion.setStatus("current")


class _SleMibConfDescription_Type(OctetString):
    """Custom type sleMibConfDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SleMibConfDescription_Type.__name__ = "OctetString"
_SleMibConfDescription_Object = MibTableColumn
sleMibConfDescription = _SleMibConfDescription_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 1, 1, 1, 3),
    _SleMibConfDescription_Type()
)
sleMibConfDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMibConfDescription.setStatus("current")
_SleMibConfDirectory_Type = ObjectIdentifier
_SleMibConfDirectory_Object = MibTableColumn
sleMibConfDirectory = _SleMibConfDirectory_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 1, 1, 1, 4),
    _SleMibConfDirectory_Type()
)
sleMibConfDirectory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMibConfDirectory.setStatus("current")
_SleModuleInfo_ObjectIdentity = ObjectIdentity
sleModuleInfo = _SleModuleInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2)
)
_SleSystemModuleTable_Object = MibTable
sleSystemModuleTable = _SleSystemModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 1)
)
if mibBuilder.loadTexts:
    sleSystemModuleTable.setStatus("current")
_SleSystemModuleEntry_Object = MibTableRow
sleSystemModuleEntry = _SleSystemModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 1, 1)
)
sleSystemModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleSystemModuleIndex"),
)
if mibBuilder.loadTexts:
    sleSystemModuleEntry.setStatus("current")


class _SleSystemModuleIndex_Type(Integer32):
    """Custom type sleSystemModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              21,
              31,
              32,
              33,
              41,
              42,
              43,
              51,
              52,
              53,
              54,
              55,
              56,
              61,
              62,
              71,
              81,
              82,
              91,
              101)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("login", 11),
          ("process", 12),
          ("backup", 21),
          ("syslogConf", 31),
          ("syslogHistVol", 32),
          ("syslogHistNVol", 33),
          ("dnsServer", 41),
          ("ntpServer", 42),
          ("sshRemote", 43),
          ("autoCLI", 51),
          ("autoCliScript", 52),
          ("autoCliSchedule", 53),
          ("autoCliProfile", 54),
          ("autoCliProfileServer", 55),
          ("autoCliOutputMemory", 56),
          ("autoResetPing", 61),
          ("autoResetMemoryleak", 62),
          ("coreDump", 71),
          ("sysService", 81),
          ("sysUser", 82),
          ("parameter", 91),
          ("watchDog", 101))
    )


_SleSystemModuleIndex_Type.__name__ = "Integer32"
_SleSystemModuleIndex_Object = MibTableColumn
sleSystemModuleIndex = _SleSystemModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 1, 1, 1),
    _SleSystemModuleIndex_Type()
)
sleSystemModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemModuleIndex.setStatus("current")
_SleSystemModuleVersion_Type = SleVersionType
_SleSystemModuleVersion_Object = MibTableColumn
sleSystemModuleVersion = _SleSystemModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 1, 1, 2),
    _SleSystemModuleVersion_Type()
)
sleSystemModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemModuleVersion.setStatus("current")
_SleSystemModuleObjectId_Type = ObjectIdentifier
_SleSystemModuleObjectId_Object = MibTableColumn
sleSystemModuleObjectId = _SleSystemModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 1, 1, 3),
    _SleSystemModuleObjectId_Type()
)
sleSystemModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSystemModuleObjectId.setStatus("current")
_SleDeviceModuleTable_Object = MibTable
sleDeviceModuleTable = _SleDeviceModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 2)
)
if mibBuilder.loadTexts:
    sleDeviceModuleTable.setStatus("current")
_SleDeviceModuleEntry_Object = MibTableRow
sleDeviceModuleEntry = _SleDeviceModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 2, 1)
)
sleDeviceModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleDeviceModuleIndex"),
)
if mibBuilder.loadTexts:
    sleDeviceModuleEntry.setStatus("current")


class _SleDeviceModuleIndex_Type(Integer32):
    """Custom type sleDeviceModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              21,
              22,
              23,
              24,
              31,
              41,
              51)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("ethernetPort", 11),
          ("power", 21),
          ("fanModule", 22),
          ("fanUnit", 23),
          ("temperature", 24),
          ("battery", 31),
          ("door", 41),
          ("cpu", 51))
    )


_SleDeviceModuleIndex_Type.__name__ = "Integer32"
_SleDeviceModuleIndex_Object = MibTableColumn
sleDeviceModuleIndex = _SleDeviceModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 2, 1, 1),
    _SleDeviceModuleIndex_Type()
)
sleDeviceModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceModuleIndex.setStatus("current")
_SleDeviceModuleVersion_Type = SleVersionType
_SleDeviceModuleVersion_Object = MibTableColumn
sleDeviceModuleVersion = _SleDeviceModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 2, 1, 2),
    _SleDeviceModuleVersion_Type()
)
sleDeviceModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceModuleVersion.setStatus("current")
_SleDeviceModuleObjectId_Type = ObjectIdentifier
_SleDeviceModuleObjectId_Object = MibTableColumn
sleDeviceModuleObjectId = _SleDeviceModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 2, 1, 3),
    _SleDeviceModuleObjectId_Type()
)
sleDeviceModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDeviceModuleObjectId.setStatus("current")
_SleBridgeModuleTable_Object = MibTable
sleBridgeModuleTable = _SleBridgeModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 3)
)
if mibBuilder.loadTexts:
    sleBridgeModuleTable.setStatus("current")
_SleBridgeModuleEntry_Object = MibTableRow
sleBridgeModuleEntry = _SleBridgeModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 3, 1)
)
sleBridgeModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleBridgeModuleIndex"),
)
if mibBuilder.loadTexts:
    sleBridgeModuleEntry.setStatus("current")


class _SleBridgeModuleIndex_Type(Integer32):
    """Custom type sleBridgeModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              21,
              22,
              23,
              24,
              31,
              32,
              41,
              51,
              52,
              53,
              61,
              62,
              63,
              71,
              81,
              82,
              83,
              91,
              92,
              101,
              102,
              111,
              121)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("bridgePort", 11),
          ("vlan", 21),
          ("vlanMap", 22),
          ("subnetBasedVlan", 23),
          ("protocolBasedVlan", 24),
          ("fdb", 31),
          ("mfdb", 32),
          ("stackDevice", 41),
          ("stp", 51),
          ("stpInstance", 52),
          ("stpInstancePort", 53),
          ("lag", 61),
          ("lagLacp", 62),
          ("lagLacpPort", 63),
          ("erpDomain", 71),
          ("lldpPort", 81),
          ("lldpRemote", 82),
          ("lldpStatistics", 83),
          ("igmpSnoopConf", 91),
          ("igmpSnoopGroup", 92),
          ("portSecurity", 101),
          ("portSecurityFdb", 102),
          ("floodGuard", 111),
          ("vlanTranslation", 121))
    )


_SleBridgeModuleIndex_Type.__name__ = "Integer32"
_SleBridgeModuleIndex_Object = MibTableColumn
sleBridgeModuleIndex = _SleBridgeModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 3, 1, 1),
    _SleBridgeModuleIndex_Type()
)
sleBridgeModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBridgeModuleIndex.setStatus("current")
_SleBridgeModuleVersion_Type = SleVersionType
_SleBridgeModuleVersion_Object = MibTableColumn
sleBridgeModuleVersion = _SleBridgeModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 3, 1, 2),
    _SleBridgeModuleVersion_Type()
)
sleBridgeModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBridgeModuleVersion.setStatus("current")
_SleBridgeModuleObjectId_Type = ObjectIdentifier
_SleBridgeModuleObjectId_Object = MibTableColumn
sleBridgeModuleObjectId = _SleBridgeModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 3, 1, 3),
    _SleBridgeModuleObjectId_Type()
)
sleBridgeModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleBridgeModuleObjectId.setStatus("current")
_SleFaultMgmtModuleTable_Object = MibTable
sleFaultMgmtModuleTable = _SleFaultMgmtModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 4)
)
if mibBuilder.loadTexts:
    sleFaultMgmtModuleTable.setStatus("current")
_SleFaultMgmtModuleEntry_Object = MibTableRow
sleFaultMgmtModuleEntry = _SleFaultMgmtModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 4, 1)
)
sleFaultMgmtModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleFaultMgmtModuleIndex"),
)
if mibBuilder.loadTexts:
    sleFaultMgmtModuleEntry.setStatus("current")


class _SleFaultMgmtModuleIndex_Type(Integer32):
    """Custom type sleFaultMgmtModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13,
              21,
              31,
              32,
              33,
              34,
              35)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("alarmSeverity", 11),
          ("alarmReport", 12),
          ("alarmHistory", 13),
          ("efmOam", 21),
          ("advaSystem", 31),
          ("advaGeneral", 32),
          ("advaModule", 33),
          ("advaOptical", 34),
          ("advaOam", 35))
    )


_SleFaultMgmtModuleIndex_Type.__name__ = "Integer32"
_SleFaultMgmtModuleIndex_Object = MibTableColumn
sleFaultMgmtModuleIndex = _SleFaultMgmtModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 4, 1, 1),
    _SleFaultMgmtModuleIndex_Type()
)
sleFaultMgmtModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFaultMgmtModuleIndex.setStatus("current")
_SleFaultMgmtModuleVersion_Type = SleVersionType
_SleFaultMgmtModuleVersion_Object = MibTableColumn
sleFaultMgmtModuleVersion = _SleFaultMgmtModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 4, 1, 2),
    _SleFaultMgmtModuleVersion_Type()
)
sleFaultMgmtModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFaultMgmtModuleVersion.setStatus("current")
_SleFaultMgmtModuleObjectId_Type = ObjectIdentifier
_SleFaultMgmtModuleObjectId_Object = MibTableColumn
sleFaultMgmtModuleObjectId = _SleFaultMgmtModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 4, 1, 3),
    _SleFaultMgmtModuleObjectId_Type()
)
sleFaultMgmtModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleFaultMgmtModuleObjectId.setStatus("current")
_SlePerfMgmtModuleTable_Object = MibTable
slePerfMgmtModuleTable = _SlePerfMgmtModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 5)
)
if mibBuilder.loadTexts:
    slePerfMgmtModuleTable.setStatus("current")
_SlePerfMgmtModuleEntry_Object = MibTableRow
slePerfMgmtModuleEntry = _SlePerfMgmtModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 5, 1)
)
slePerfMgmtModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "slePerfMgmtModuleIndex"),
)
if mibBuilder.loadTexts:
    slePerfMgmtModuleEntry.setStatus("current")


class _SlePerfMgmtModuleIndex_Type(Integer32):
    """Custom type slePerfMgmtModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("portThreshold", 11),
          ("portRate", 12),
          ("portStatistics", 13),
          ("cpuStatistics", 14))
    )


_SlePerfMgmtModuleIndex_Type.__name__ = "Integer32"
_SlePerfMgmtModuleIndex_Object = MibTableColumn
slePerfMgmtModuleIndex = _SlePerfMgmtModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 5, 1, 1),
    _SlePerfMgmtModuleIndex_Type()
)
slePerfMgmtModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePerfMgmtModuleIndex.setStatus("current")
_SlePerfMgmtModuleVersion_Type = SleVersionType
_SlePerfMgmtModuleVersion_Object = MibTableColumn
slePerfMgmtModuleVersion = _SlePerfMgmtModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 5, 1, 2),
    _SlePerfMgmtModuleVersion_Type()
)
slePerfMgmtModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePerfMgmtModuleVersion.setStatus("current")
_SlePerfMgmtModuleObjectId_Type = ObjectIdentifier
_SlePerfMgmtModuleObjectId_Object = MibTableColumn
slePerfMgmtModuleObjectId = _SlePerfMgmtModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 5, 1, 3),
    _SlePerfMgmtModuleObjectId_Type()
)
slePerfMgmtModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slePerfMgmtModuleObjectId.setStatus("current")
_SleDhcpModuleTable_Object = MibTable
sleDhcpModuleTable = _SleDhcpModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 6)
)
if mibBuilder.loadTexts:
    sleDhcpModuleTable.setStatus("current")
_SleDhcpModuleEntry_Object = MibTableRow
sleDhcpModuleEntry = _SleDhcpModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 6, 1)
)
sleDhcpModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleDhcpModuleIndex"),
)
if mibBuilder.loadTexts:
    sleDhcpModuleEntry.setStatus("current")


class _SleDhcpModuleIndex_Type(Integer32):
    """Custom type sleDhcpModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              31,
              32,
              33,
              34,
              35,
              36,
              41,
              42,
              43,
              51,
              52,
              53,
              61,
              62,
              63,
              64,
              71,
              72,
              81,
              82,
              91)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("pool", 11),
          ("network", 12),
          ("range", 13),
          ("fixedAddress", 14),
          ("dnsOption", 15),
          ("defaultGwOption", 16),
          ("serverOptions", 17),
          ("dhcp4Logs", 18),
          ("dhcp4Ntp", 19),
          ("dhcp4PE", 20),
          ("option82Port", 31),
          ("option82Remote", 32),
          ("option82Circuit", 33),
          ("option82Class", 34),
          ("option82ClassMap", 35),
          ("option82ClassRange", 36),
          ("filterPort", 41),
          ("filterAddress", 42),
          ("illegal", 43),
          ("packetStats", 51),
          ("leased", 52),
          ("packetStatsPort", 53),
          ("snopping", 61),
          ("snoopVlan", 62),
          ("snoopPort", 63),
          ("snoopBindings", 64),
          ("relayInterface", 71),
          ("relayHelper", 72),
          ("clientInterface", 81),
          ("clientOptions", 82),
          ("dhcp4PortLease", 91))
    )


_SleDhcpModuleIndex_Type.__name__ = "Integer32"
_SleDhcpModuleIndex_Object = MibTableColumn
sleDhcpModuleIndex = _SleDhcpModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 6, 1, 1),
    _SleDhcpModuleIndex_Type()
)
sleDhcpModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpModuleIndex.setStatus("current")
_SleDhcpModuleVersion_Type = SleVersionType
_SleDhcpModuleVersion_Object = MibTableColumn
sleDhcpModuleVersion = _SleDhcpModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 6, 1, 2),
    _SleDhcpModuleVersion_Type()
)
sleDhcpModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpModuleVersion.setStatus("current")
_SleDhcpModuleObjectId_Type = ObjectIdentifier
_SleDhcpModuleObjectId_Object = MibTableColumn
sleDhcpModuleObjectId = _SleDhcpModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 6, 1, 3),
    _SleDhcpModuleObjectId_Type()
)
sleDhcpModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpModuleObjectId.setStatus("current")
_SleSecurityModuleTable_Object = MibTable
sleSecurityModuleTable = _SleSecurityModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 7)
)
if mibBuilder.loadTexts:
    sleSecurityModuleTable.setStatus("current")
_SleSecurityModuleEntry_Object = MibTableRow
sleSecurityModuleEntry = _SleSecurityModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 7, 1)
)
sleSecurityModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleSecurityModuleIndex"),
)
if mibBuilder.loadTexts:
    sleSecurityModuleEntry.setStatus("current")


class _SleSecurityModuleIndex_Type(Integer32):
    """Custom type sleSecurityModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13,
              21,
              31,
              32,
              41)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("aaa", 11),
          ("radiusServer", 12),
          ("tacacsServer", 13),
          ("acl", 21),
          ("dot1xPort", 31),
          ("dot1xStatistics", 32),
          ("arpInspection", 41))
    )


_SleSecurityModuleIndex_Type.__name__ = "Integer32"
_SleSecurityModuleIndex_Object = MibTableColumn
sleSecurityModuleIndex = _SleSecurityModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 7, 1, 1),
    _SleSecurityModuleIndex_Type()
)
sleSecurityModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityModuleIndex.setStatus("current")
_SleSecurityModuleVersion_Type = SleVersionType
_SleSecurityModuleVersion_Object = MibTableColumn
sleSecurityModuleVersion = _SleSecurityModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 7, 1, 2),
    _SleSecurityModuleVersion_Type()
)
sleSecurityModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityModuleVersion.setStatus("current")
_SleSecurityModuleObjectId_Type = ObjectIdentifier
_SleSecurityModuleObjectId_Object = MibTableColumn
sleSecurityModuleObjectId = _SleSecurityModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 7, 1, 3),
    _SleSecurityModuleObjectId_Type()
)
sleSecurityModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSecurityModuleObjectId.setStatus("current")
_SleSnmpModuleTable_Object = MibTable
sleSnmpModuleTable = _SleSnmpModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 8)
)
if mibBuilder.loadTexts:
    sleSnmpModuleTable.setStatus("current")
_SleSnmpModuleEntry_Object = MibTableRow
sleSnmpModuleEntry = _SleSnmpModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 8, 1)
)
sleSnmpModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleSnmpModuleIndex"),
)
if mibBuilder.loadTexts:
    sleSnmpModuleEntry.setStatus("current")


class _SleSnmpModuleIndex_Type(Integer32):
    """Custom type sleSnmpModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              21)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("com2Sec", 11),
          ("trapHost", 12),
          ("community", 13),
          ("viewTreeFamily", 14),
          ("access", 15),
          ("securityToGroup", 16),
          ("user", 17),
          ("agent", 18),
          ("snmpSeesion", 19),
          ("snmpTrap", 20),
          ("snmpTrapSource", 21))
    )


_SleSnmpModuleIndex_Type.__name__ = "Integer32"
_SleSnmpModuleIndex_Object = MibTableColumn
sleSnmpModuleIndex = _SleSnmpModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 8, 1, 1),
    _SleSnmpModuleIndex_Type()
)
sleSnmpModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpModuleIndex.setStatus("current")
_SleSnmpModuleVersion_Type = SleVersionType
_SleSnmpModuleVersion_Object = MibTableColumn
sleSnmpModuleVersion = _SleSnmpModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 8, 1, 2),
    _SleSnmpModuleVersion_Type()
)
sleSnmpModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpModuleVersion.setStatus("current")
_SleSnmpModuleObjectId_Type = ObjectIdentifier
_SleSnmpModuleObjectId_Object = MibTableColumn
sleSnmpModuleObjectId = _SleSnmpModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 8, 1, 3),
    _SleSnmpModuleObjectId_Type()
)
sleSnmpModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSnmpModuleObjectId.setStatus("current")
_SleRmonModuleTable_Object = MibTable
sleRmonModuleTable = _SleRmonModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 9)
)
if mibBuilder.loadTexts:
    sleRmonModuleTable.setStatus("current")
_SleRmonModuleEntry_Object = MibTableRow
sleRmonModuleEntry = _SleRmonModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 9, 1)
)
sleRmonModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleRmonModuleIndex"),
)
if mibBuilder.loadTexts:
    sleRmonModuleEntry.setStatus("current")


class _SleRmonModuleIndex_Type(Integer32):
    """Custom type sleRmonModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13,
              21)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("event", 11),
          ("alarm", 12),
          ("history", 13),
          ("etherStats", 21))
    )


_SleRmonModuleIndex_Type.__name__ = "Integer32"
_SleRmonModuleIndex_Object = MibTableColumn
sleRmonModuleIndex = _SleRmonModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 9, 1, 1),
    _SleRmonModuleIndex_Type()
)
sleRmonModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonModuleIndex.setStatus("current")
_SleRmonModuleVersion_Type = SleVersionType
_SleRmonModuleVersion_Object = MibTableColumn
sleRmonModuleVersion = _SleRmonModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 9, 1, 2),
    _SleRmonModuleVersion_Type()
)
sleRmonModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonModuleVersion.setStatus("current")
_SleRmonModuleObjectId_Type = ObjectIdentifier
_SleRmonModuleObjectId_Object = MibTableColumn
sleRmonModuleObjectId = _SleRmonModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 9, 1, 3),
    _SleRmonModuleObjectId_Type()
)
sleRmonModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRmonModuleObjectId.setStatus("current")
_SleQosModuleTable_Object = MibTable
sleQosModuleTable = _SleQosModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 10)
)
if mibBuilder.loadTexts:
    sleQosModuleTable.setStatus("current")
_SleQosModuleEntry_Object = MibTableRow
sleQosModuleEntry = _SleQosModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 10, 1)
)
sleQosModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleQosModuleIndex"),
)
if mibBuilder.loadTexts:
    sleQosModuleEntry.setStatus("current")


class _SleQosModuleIndex_Type(Integer32):
    """Custom type sleQosModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              12,
              13,
              14,
              15,
              21,
              31,
              32,
              33,
              41,
              42,
              43,
              51,
              61,
              62,
              71,
              72,
              73,
              81,
              82)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("baseV4", 2),
          ("baseV6", 3),
          ("trafficeProfile", 11),
          ("portSchedule", 12),
          ("queue", 13),
          ("counter", 14),
          ("colorMarking", 15),
          ("userflow", 21),
          ("flow", 31),
          ("flowClassMap", 32),
          ("flowPolicyMap", 33),
          ("class", 41),
          ("classFlowMap", 42),
          ("classPolicyMap", 43),
          ("policer", 51),
          ("policy", 61),
          ("policyFCMap", 62),
          ("remark", 71),
          ("remarkL3", 72),
          ("remarkL2", 73),
          ("redProfile", 81),
          ("portRed", 82))
    )


_SleQosModuleIndex_Type.__name__ = "Integer32"
_SleQosModuleIndex_Object = MibTableColumn
sleQosModuleIndex = _SleQosModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 10, 1, 1),
    _SleQosModuleIndex_Type()
)
sleQosModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosModuleIndex.setStatus("current")
_SleQosModuleVersion_Type = SleVersionType
_SleQosModuleVersion_Object = MibTableColumn
sleQosModuleVersion = _SleQosModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 10, 1, 2),
    _SleQosModuleVersion_Type()
)
sleQosModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosModuleVersion.setStatus("current")
_SleQosModuleObjectId_Type = ObjectIdentifier
_SleQosModuleObjectId_Object = MibTableColumn
sleQosModuleObjectId = _SleQosModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 10, 1, 3),
    _SleQosModuleObjectId_Type()
)
sleQosModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleQosModuleObjectId.setStatus("current")
_SleNetworkModuleTable_Object = MibTable
sleNetworkModuleTable = _SleNetworkModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 11)
)
if mibBuilder.loadTexts:
    sleNetworkModuleTable.setStatus("current")
_SleNetworkModuleEntry_Object = MibTableRow
sleNetworkModuleEntry = _SleNetworkModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 11, 1)
)
sleNetworkModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleNetworkModuleIndex"),
)
if mibBuilder.loadTexts:
    sleNetworkModuleEntry.setStatus("current")


class _SleNetworkModuleIndex_Type(Integer32):
    """Custom type sleNetworkModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13,
              21,
              31)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("interface", 11),
          ("ipAddress", 12),
          ("arp", 13),
          ("routing", 21),
          ("dhcpClient", 31))
    )


_SleNetworkModuleIndex_Type.__name__ = "Integer32"
_SleNetworkModuleIndex_Object = MibTableColumn
sleNetworkModuleIndex = _SleNetworkModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 11, 1, 1),
    _SleNetworkModuleIndex_Type()
)
sleNetworkModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetworkModuleIndex.setStatus("current")
_SleNetworkModuleVersion_Type = SleVersionType
_SleNetworkModuleVersion_Object = MibTableColumn
sleNetworkModuleVersion = _SleNetworkModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 11, 1, 2),
    _SleNetworkModuleVersion_Type()
)
sleNetworkModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetworkModuleVersion.setStatus("current")
_SleNetworkModuleObjectId_Type = ObjectIdentifier
_SleNetworkModuleObjectId_Object = MibTableColumn
sleNetworkModuleObjectId = _SleNetworkModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 11, 1, 3),
    _SleNetworkModuleObjectId_Type()
)
sleNetworkModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleNetworkModuleObjectId.setStatus("current")
_SleMulticastModuleTable_Object = MibTable
sleMulticastModuleTable = _SleMulticastModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 12)
)
if mibBuilder.loadTexts:
    sleMulticastModuleTable.setStatus("current")
_SleMulticastModuleEntry_Object = MibTableRow
sleMulticastModuleEntry = _SleMulticastModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 12, 1)
)
sleMulticastModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleMulticastModuleIndex"),
)
if mibBuilder.loadTexts:
    sleMulticastModuleEntry.setStatus("current")


class _SleMulticastModuleIndex_Type(Integer32):
    """Custom type sleMulticastModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13,
              14,
              21,
              22,
              31,
              32,
              41,
              42,
              43,
              44,
              51,
              52,
              53,
              54,
              55,
              56,
              61,
              62,
              63,
              71,
              72,
              81,
              91,
              101,
              111,
              121)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("mrouteBase", 11),
          ("mroute", 12),
          ("mrouteNextHop", 13),
          ("mrouteInterface", 14),
          ("igmpBase", 21),
          ("igmpSsmMapping", 22),
          ("igmpHelperVlan", 31),
          ("igmpHelperGroup", 32),
          ("igmpInterface", 41),
          ("igmpCache", 42),
          ("igmpSource", 43),
          ("igmpGroupState", 44),
          ("igmpSnoopVlan", 51),
          ("igmpSnoopGroup", 52),
          ("igmpSnoopSource", 53),
          ("igmpSnoopReport", 54),
          ("igmpSnoopPort", 55),
          ("igmpSnoopPortStats", 56),
          ("igmpProfile", 61),
          ("igmpProfileRange", 62),
          ("igmpFilterPort", 63),
          ("mvrPort", 71),
          ("mvrGroup", 72),
          ("pimBase", 81),
          ("pimSnoopVlan", 91),
          ("pimAgent", 101),
          ("igmpProxyBase", 111),
          ("igmpProxyInterface", 121))
    )


_SleMulticastModuleIndex_Type.__name__ = "Integer32"
_SleMulticastModuleIndex_Object = MibTableColumn
sleMulticastModuleIndex = _SleMulticastModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 12, 1, 1),
    _SleMulticastModuleIndex_Type()
)
sleMulticastModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMulticastModuleIndex.setStatus("current")
_SleMulticastModuleVersion_Type = SleVersionType
_SleMulticastModuleVersion_Object = MibTableColumn
sleMulticastModuleVersion = _SleMulticastModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 12, 1, 2),
    _SleMulticastModuleVersion_Type()
)
sleMulticastModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMulticastModuleVersion.setStatus("current")
_SleMulticastModuleObjectId_Type = ObjectIdentifier
_SleMulticastModuleObjectId_Object = MibTableColumn
sleMulticastModuleObjectId = _SleMulticastModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 12, 1, 3),
    _SleMulticastModuleObjectId_Type()
)
sleMulticastModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMulticastModuleObjectId.setStatus("current")
_SleDhcpSnoopModuleTable_Object = MibTable
sleDhcpSnoopModuleTable = _SleDhcpSnoopModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 13)
)
if mibBuilder.loadTexts:
    sleDhcpSnoopModuleTable.setStatus("current")
_SleDhcpSnoopModuleEntry_Object = MibTableRow
sleDhcpSnoopModuleEntry = _SleDhcpSnoopModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 13, 1)
)
sleDhcpSnoopModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleDhcpSnoopModuleIndex"),
)
if mibBuilder.loadTexts:
    sleDhcpSnoopModuleEntry.setStatus("current")


class _SleDhcpSnoopModuleIndex_Type(Integer32):
    """Custom type sleDhcpSnoopModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("portSrcGuardConf", 11),
          ("portSrcGuardAddress", 12))
    )


_SleDhcpSnoopModuleIndex_Type.__name__ = "Integer32"
_SleDhcpSnoopModuleIndex_Object = MibTableColumn
sleDhcpSnoopModuleIndex = _SleDhcpSnoopModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 13, 1, 1),
    _SleDhcpSnoopModuleIndex_Type()
)
sleDhcpSnoopModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSnoopModuleIndex.setStatus("current")
_SleDhcpSnoopModuleVersion_Type = SleVersionType
_SleDhcpSnoopModuleVersion_Object = MibTableColumn
sleDhcpSnoopModuleVersion = _SleDhcpSnoopModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 13, 1, 2),
    _SleDhcpSnoopModuleVersion_Type()
)
sleDhcpSnoopModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSnoopModuleVersion.setStatus("current")
_SleDhcpSnoopModuleObjectId_Type = ObjectIdentifier
_SleDhcpSnoopModuleObjectId_Object = MibTableColumn
sleDhcpSnoopModuleObjectId = _SleDhcpSnoopModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 13, 1, 3),
    _SleDhcpSnoopModuleObjectId_Type()
)
sleDhcpSnoopModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDhcpSnoopModuleObjectId.setStatus("current")
_SleMvQosModuleTable_Object = MibTable
sleMvQosModuleTable = _SleMvQosModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 14)
)
if mibBuilder.loadTexts:
    sleMvQosModuleTable.setStatus("current")
_SleMvQosModuleEntry_Object = MibTableRow
sleMvQosModuleEntry = _SleMvQosModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 14, 1)
)
sleMvQosModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleMvQosModuleIndex"),
)
if mibBuilder.loadTexts:
    sleMvQosModuleEntry.setStatus("current")


class _SleMvQosModuleIndex_Type(Integer32):
    """Custom type sleMvQosModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              21,
              31)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("baseV4", 2),
          ("baseV6", 3),
          ("bridgePort2Tc", 11),
          ("bridgeProtocol2Tc", 12),
          ("bridgeSubnet2Tc", 13),
          ("bridgeMac2Tc", 14),
          ("bridgeUp2TcEnable", 15),
          ("bridgeUp2Tc", 16),
          ("bridgeTc2Up", 17),
          ("bridgeUp2Dp", 18),
          ("inLifMark", 21),
          ("routerMark", 31))
    )


_SleMvQosModuleIndex_Type.__name__ = "Integer32"
_SleMvQosModuleIndex_Object = MibTableColumn
sleMvQosModuleIndex = _SleMvQosModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 14, 1, 1),
    _SleMvQosModuleIndex_Type()
)
sleMvQosModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMvQosModuleIndex.setStatus("current")
_SleMvQosModuleVersion_Type = SleVersionType
_SleMvQosModuleVersion_Object = MibTableColumn
sleMvQosModuleVersion = _SleMvQosModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 14, 1, 2),
    _SleMvQosModuleVersion_Type()
)
sleMvQosModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMvQosModuleVersion.setStatus("current")
_SleMvQosModuleObjectId_Type = ObjectIdentifier
_SleMvQosModuleObjectId_Object = MibTableColumn
sleMvQosModuleObjectId = _SleMvQosModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 14, 1, 3),
    _SleMvQosModuleObjectId_Type()
)
sleMvQosModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleMvQosModuleObjectId.setStatus("current")
_SleEponModuleTable_Object = MibTable
sleEponModuleTable = _SleEponModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 20)
)
if mibBuilder.loadTexts:
    sleEponModuleTable.setStatus("current")
_SleEponModuleEntry_Object = MibTableRow
sleEponModuleEntry = _SleEponModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 20, 1)
)
sleEponModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleEponModuleIndex"),
)
if mibBuilder.loadTexts:
    sleEponModuleEntry.setStatus("current")


class _SleEponModuleIndex_Type(Integer32):
    """Custom type sleEponModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              21,
              31,
              41,
              42,
              51,
              61,
              62)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("olt", 11),
          ("onu", 21),
          ("vlan", 31),
          ("profile", 41),
          ("profileQueue", 42),
          ("alarm", 51),
          ("oltStatistics", 61),
          ("onuStatistics", 62))
    )


_SleEponModuleIndex_Type.__name__ = "Integer32"
_SleEponModuleIndex_Object = MibTableColumn
sleEponModuleIndex = _SleEponModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 20, 1, 1),
    _SleEponModuleIndex_Type()
)
sleEponModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEponModuleIndex.setStatus("current")
_SleEponModuleVersion_Type = SleVersionType
_SleEponModuleVersion_Object = MibTableColumn
sleEponModuleVersion = _SleEponModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 20, 1, 2),
    _SleEponModuleVersion_Type()
)
sleEponModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEponModuleVersion.setStatus("current")
_SleEponModuleObjectId_Type = ObjectIdentifier
_SleEponModuleObjectId_Object = MibTableColumn
sleEponModuleObjectId = _SleEponModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 20, 1, 3),
    _SleEponModuleObjectId_Type()
)
sleEponModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleEponModuleObjectId.setStatus("current")
_SleSFlowModuleTable_Object = MibTable
sleSFlowModuleTable = _SleSFlowModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 21)
)
if mibBuilder.loadTexts:
    sleSFlowModuleTable.setStatus("current")
_SleSFlowModuleEntry_Object = MibTableRow
sleSFlowModuleEntry = _SleSFlowModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 21, 1)
)
sleSFlowModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleSFlowModuleIndex"),
)
if mibBuilder.loadTexts:
    sleSFlowModuleEntry.setStatus("current")


class _SleSFlowModuleIndex_Type(Integer32):
    """Custom type sleSFlowModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              11,
              12,
              13)
        )
    )
    namedValues = NamedValues(
        *(("base", 1),
          ("receiver", 11),
          ("flowSampler", 12),
          ("counterPoller", 13))
    )


_SleSFlowModuleIndex_Type.__name__ = "Integer32"
_SleSFlowModuleIndex_Object = MibTableColumn
sleSFlowModuleIndex = _SleSFlowModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 21, 1, 1),
    _SleSFlowModuleIndex_Type()
)
sleSFlowModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowModuleIndex.setStatus("current")
_SleSFlowModuleVersion_Type = SleVersionType
_SleSFlowModuleVersion_Object = MibTableColumn
sleSFlowModuleVersion = _SleSFlowModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 21, 1, 2),
    _SleSFlowModuleVersion_Type()
)
sleSFlowModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowModuleVersion.setStatus("current")
_SleSFlowModuleObjectId_Type = ObjectIdentifier
_SleSFlowModuleObjectId_Object = MibTableColumn
sleSFlowModuleObjectId = _SleSFlowModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 21, 1, 3),
    _SleSFlowModuleObjectId_Type()
)
sleSFlowModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleSFlowModuleObjectId.setStatus("current")
_SleRedModuleTable_Object = MibTable
sleRedModuleTable = _SleRedModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 22)
)
if mibBuilder.loadTexts:
    sleRedModuleTable.setStatus("current")
_SleRedModuleEntry_Object = MibTableRow
sleRedModuleEntry = _SleRedModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 22, 1)
)
sleRedModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleRedModuleIndex"),
)
if mibBuilder.loadTexts:
    sleRedModuleEntry.setStatus("current")


class _SleRedModuleIndex_Type(Integer32):
    """Custom type sleRedModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("base", 1)
    )


_SleRedModuleIndex_Type.__name__ = "Integer32"
_SleRedModuleIndex_Object = MibTableColumn
sleRedModuleIndex = _SleRedModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 22, 1, 1),
    _SleRedModuleIndex_Type()
)
sleRedModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedModuleIndex.setStatus("current")
_SleRedModuleVersion_Type = SleVersionType
_SleRedModuleVersion_Object = MibTableColumn
sleRedModuleVersion = _SleRedModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 22, 1, 2),
    _SleRedModuleVersion_Type()
)
sleRedModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedModuleVersion.setStatus("current")
_SleRedModuleObjectId_Type = ObjectIdentifier
_SleRedModuleObjectId_Object = MibTableColumn
sleRedModuleObjectId = _SleRedModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 22, 1, 3),
    _SleRedModuleObjectId_Type()
)
sleRedModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleRedModuleObjectId.setStatus("current")
_SleDebugModuleTable_Object = MibTable
sleDebugModuleTable = _SleDebugModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 99)
)
if mibBuilder.loadTexts:
    sleDebugModuleTable.setStatus("current")
_SleDebugModuleEntry_Object = MibTableRow
sleDebugModuleEntry = _SleDebugModuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 99, 1)
)
sleDebugModuleEntry.setIndexNames(
    (0, "SLE-CONFIG-MIB", "sleSFlowModuleIndex"),
)
if mibBuilder.loadTexts:
    sleDebugModuleEntry.setStatus("current")


class _SleDebugModuleIndex_Type(Integer32):
    """Custom type sleDebugModuleIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("debugBase", 1)
    )


_SleDebugModuleIndex_Type.__name__ = "Integer32"
_SleDebugModuleIndex_Object = MibTableColumn
sleDebugModuleIndex = _SleDebugModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 99, 1, 1),
    _SleDebugModuleIndex_Type()
)
sleDebugModuleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugModuleIndex.setStatus("current")
_SleDebugModuleVersion_Type = SleVersionType
_SleDebugModuleVersion_Object = MibTableColumn
sleDebugModuleVersion = _SleDebugModuleVersion_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 99, 1, 2),
    _SleDebugModuleVersion_Type()
)
sleDebugModuleVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugModuleVersion.setStatus("current")
_SleDebugModuleObjectId_Type = ObjectIdentifier
_SleDebugModuleObjectId_Object = MibTableColumn
sleDebugModuleObjectId = _SleDebugModuleObjectId_Object(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 2, 99, 1, 3),
    _SleDebugModuleObjectId_Type()
)
sleDebugModuleObjectId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sleDebugModuleObjectId.setStatus("current")

# Managed Objects groups

sleMibConfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6296, 100, 1, 3)
)
sleMibConfGroup.setObjects(
      *(("SLE-CONFIG-MIB", "sleMibConfIndex"),
        ("SLE-CONFIG-MIB", "sleMibConfVersion"),
        ("SLE-CONFIG-MIB", "sleMibConfDescription"),
        ("SLE-CONFIG-MIB", "sleMibConfDirectory"),
        ("SLE-CONFIG-MIB", "sleSystemModuleIndex"),
        ("SLE-CONFIG-MIB", "sleSystemModuleVersion"),
        ("SLE-CONFIG-MIB", "sleSystemModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleDeviceModuleIndex"),
        ("SLE-CONFIG-MIB", "sleDeviceModuleVersion"),
        ("SLE-CONFIG-MIB", "sleDeviceModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleBridgeModuleIndex"),
        ("SLE-CONFIG-MIB", "sleBridgeModuleVersion"),
        ("SLE-CONFIG-MIB", "sleBridgeModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleFaultMgmtModuleIndex"),
        ("SLE-CONFIG-MIB", "sleFaultMgmtModuleVersion"),
        ("SLE-CONFIG-MIB", "sleFaultMgmtModuleObjectId"),
        ("SLE-CONFIG-MIB", "slePerfMgmtModuleIndex"),
        ("SLE-CONFIG-MIB", "slePerfMgmtModuleVersion"),
        ("SLE-CONFIG-MIB", "slePerfMgmtModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleDhcpModuleIndex"),
        ("SLE-CONFIG-MIB", "sleDhcpModuleVersion"),
        ("SLE-CONFIG-MIB", "sleDhcpModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleSecurityModuleIndex"),
        ("SLE-CONFIG-MIB", "sleSecurityModuleVersion"),
        ("SLE-CONFIG-MIB", "sleSecurityModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleSnmpModuleIndex"),
        ("SLE-CONFIG-MIB", "sleSnmpModuleVersion"),
        ("SLE-CONFIG-MIB", "sleSnmpModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleRmonModuleIndex"),
        ("SLE-CONFIG-MIB", "sleRmonModuleVersion"),
        ("SLE-CONFIG-MIB", "sleRmonModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleQosModuleIndex"),
        ("SLE-CONFIG-MIB", "sleQosModuleVersion"),
        ("SLE-CONFIG-MIB", "sleQosModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleNetworkModuleIndex"),
        ("SLE-CONFIG-MIB", "sleNetworkModuleVersion"),
        ("SLE-CONFIG-MIB", "sleNetworkModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleMulticastModuleIndex"),
        ("SLE-CONFIG-MIB", "sleMulticastModuleVersion"),
        ("SLE-CONFIG-MIB", "sleMulticastModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleDhcpSnoopModuleIndex"),
        ("SLE-CONFIG-MIB", "sleDhcpSnoopModuleVersion"),
        ("SLE-CONFIG-MIB", "sleDhcpSnoopModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleSFlowModuleIndex"),
        ("SLE-CONFIG-MIB", "sleSFlowModuleVersion"),
        ("SLE-CONFIG-MIB", "sleDebugModuleIndex"),
        ("SLE-CONFIG-MIB", "sleDebugModuleVersion"),
        ("SLE-CONFIG-MIB", "sleDebugModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleRedModuleIndex"),
        ("SLE-CONFIG-MIB", "sleRedModuleVersion"),
        ("SLE-CONFIG-MIB", "sleRedModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleSFlowModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleMvQosModuleIndex"),
        ("SLE-CONFIG-MIB", "sleMvQosModuleVersion"),
        ("SLE-CONFIG-MIB", "sleMvQosModuleObjectId"),
        ("SLE-CONFIG-MIB", "sleEponModuleIndex"),
        ("SLE-CONFIG-MIB", "sleEponModuleVersion"),
        ("SLE-CONFIG-MIB", "sleEponModuleObjectId"))
)
if mibBuilder.loadTexts:
    sleMibConfGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SLE-CONFIG-MIB",
    **{"SleVersionType": SleVersionType,
       "sleConfigMgmt": sleConfigMgmt,
       "sleMibConfig": sleMibConfig,
       "sleMibConfInfo": sleMibConfInfo,
       "sleMibConfInfoTable": sleMibConfInfoTable,
       "sleMibConfInfoEntry": sleMibConfInfoEntry,
       "sleMibConfIndex": sleMibConfIndex,
       "sleMibConfVersion": sleMibConfVersion,
       "sleMibConfDescription": sleMibConfDescription,
       "sleMibConfDirectory": sleMibConfDirectory,
       "sleModuleInfo": sleModuleInfo,
       "sleSystemModuleTable": sleSystemModuleTable,
       "sleSystemModuleEntry": sleSystemModuleEntry,
       "sleSystemModuleIndex": sleSystemModuleIndex,
       "sleSystemModuleVersion": sleSystemModuleVersion,
       "sleSystemModuleObjectId": sleSystemModuleObjectId,
       "sleDeviceModuleTable": sleDeviceModuleTable,
       "sleDeviceModuleEntry": sleDeviceModuleEntry,
       "sleDeviceModuleIndex": sleDeviceModuleIndex,
       "sleDeviceModuleVersion": sleDeviceModuleVersion,
       "sleDeviceModuleObjectId": sleDeviceModuleObjectId,
       "sleBridgeModuleTable": sleBridgeModuleTable,
       "sleBridgeModuleEntry": sleBridgeModuleEntry,
       "sleBridgeModuleIndex": sleBridgeModuleIndex,
       "sleBridgeModuleVersion": sleBridgeModuleVersion,
       "sleBridgeModuleObjectId": sleBridgeModuleObjectId,
       "sleFaultMgmtModuleTable": sleFaultMgmtModuleTable,
       "sleFaultMgmtModuleEntry": sleFaultMgmtModuleEntry,
       "sleFaultMgmtModuleIndex": sleFaultMgmtModuleIndex,
       "sleFaultMgmtModuleVersion": sleFaultMgmtModuleVersion,
       "sleFaultMgmtModuleObjectId": sleFaultMgmtModuleObjectId,
       "slePerfMgmtModuleTable": slePerfMgmtModuleTable,
       "slePerfMgmtModuleEntry": slePerfMgmtModuleEntry,
       "slePerfMgmtModuleIndex": slePerfMgmtModuleIndex,
       "slePerfMgmtModuleVersion": slePerfMgmtModuleVersion,
       "slePerfMgmtModuleObjectId": slePerfMgmtModuleObjectId,
       "sleDhcpModuleTable": sleDhcpModuleTable,
       "sleDhcpModuleEntry": sleDhcpModuleEntry,
       "sleDhcpModuleIndex": sleDhcpModuleIndex,
       "sleDhcpModuleVersion": sleDhcpModuleVersion,
       "sleDhcpModuleObjectId": sleDhcpModuleObjectId,
       "sleSecurityModuleTable": sleSecurityModuleTable,
       "sleSecurityModuleEntry": sleSecurityModuleEntry,
       "sleSecurityModuleIndex": sleSecurityModuleIndex,
       "sleSecurityModuleVersion": sleSecurityModuleVersion,
       "sleSecurityModuleObjectId": sleSecurityModuleObjectId,
       "sleSnmpModuleTable": sleSnmpModuleTable,
       "sleSnmpModuleEntry": sleSnmpModuleEntry,
       "sleSnmpModuleIndex": sleSnmpModuleIndex,
       "sleSnmpModuleVersion": sleSnmpModuleVersion,
       "sleSnmpModuleObjectId": sleSnmpModuleObjectId,
       "sleRmonModuleTable": sleRmonModuleTable,
       "sleRmonModuleEntry": sleRmonModuleEntry,
       "sleRmonModuleIndex": sleRmonModuleIndex,
       "sleRmonModuleVersion": sleRmonModuleVersion,
       "sleRmonModuleObjectId": sleRmonModuleObjectId,
       "sleQosModuleTable": sleQosModuleTable,
       "sleQosModuleEntry": sleQosModuleEntry,
       "sleQosModuleIndex": sleQosModuleIndex,
       "sleQosModuleVersion": sleQosModuleVersion,
       "sleQosModuleObjectId": sleQosModuleObjectId,
       "sleNetworkModuleTable": sleNetworkModuleTable,
       "sleNetworkModuleEntry": sleNetworkModuleEntry,
       "sleNetworkModuleIndex": sleNetworkModuleIndex,
       "sleNetworkModuleVersion": sleNetworkModuleVersion,
       "sleNetworkModuleObjectId": sleNetworkModuleObjectId,
       "sleMulticastModuleTable": sleMulticastModuleTable,
       "sleMulticastModuleEntry": sleMulticastModuleEntry,
       "sleMulticastModuleIndex": sleMulticastModuleIndex,
       "sleMulticastModuleVersion": sleMulticastModuleVersion,
       "sleMulticastModuleObjectId": sleMulticastModuleObjectId,
       "sleDhcpSnoopModuleTable": sleDhcpSnoopModuleTable,
       "sleDhcpSnoopModuleEntry": sleDhcpSnoopModuleEntry,
       "sleDhcpSnoopModuleIndex": sleDhcpSnoopModuleIndex,
       "sleDhcpSnoopModuleVersion": sleDhcpSnoopModuleVersion,
       "sleDhcpSnoopModuleObjectId": sleDhcpSnoopModuleObjectId,
       "sleMvQosModuleTable": sleMvQosModuleTable,
       "sleMvQosModuleEntry": sleMvQosModuleEntry,
       "sleMvQosModuleIndex": sleMvQosModuleIndex,
       "sleMvQosModuleVersion": sleMvQosModuleVersion,
       "sleMvQosModuleObjectId": sleMvQosModuleObjectId,
       "sleEponModuleTable": sleEponModuleTable,
       "sleEponModuleEntry": sleEponModuleEntry,
       "sleEponModuleIndex": sleEponModuleIndex,
       "sleEponModuleVersion": sleEponModuleVersion,
       "sleEponModuleObjectId": sleEponModuleObjectId,
       "sleSFlowModuleTable": sleSFlowModuleTable,
       "sleSFlowModuleEntry": sleSFlowModuleEntry,
       "sleSFlowModuleIndex": sleSFlowModuleIndex,
       "sleSFlowModuleVersion": sleSFlowModuleVersion,
       "sleSFlowModuleObjectId": sleSFlowModuleObjectId,
       "sleRedModuleTable": sleRedModuleTable,
       "sleRedModuleEntry": sleRedModuleEntry,
       "sleRedModuleIndex": sleRedModuleIndex,
       "sleRedModuleVersion": sleRedModuleVersion,
       "sleRedModuleObjectId": sleRedModuleObjectId,
       "sleDebugModuleTable": sleDebugModuleTable,
       "sleDebugModuleEntry": sleDebugModuleEntry,
       "sleDebugModuleIndex": sleDebugModuleIndex,
       "sleDebugModuleVersion": sleDebugModuleVersion,
       "sleDebugModuleObjectId": sleDebugModuleObjectId,
       "sleMibConfGroup": sleMibConfGroup}
)
