# SNMP MIB module (FSC-SERVERCONTROL2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\fujitsu\FSC-SERVERCONTROL2-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:47:12 2025
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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions



class PhysAddress(OctetString):
    """Custom type PhysAddress based on OctetString"""




class TrueFalse(Integer32):
    """Custom type TrueFalse based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("false", 1),
          ("true", 2))
    )





class TrueFalseUnknown(Integer32):
    """Custom type TrueFalseUnknown based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("false", 2),
          ("true", 3))
    )





class UnitClass(Integer32):
    """Custom type UnitClass based on Integer32"""
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
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("standardServer", 2),
          ("storageExtension", 3),
          ("bladeServerChassis", 4),
          ("bladeServer", 5),
          ("clusterNode", 6),
          ("multiNodeChassis", 7),
          ("multiNodeServer", 8),
          ("virtualServer", 9),
          ("virtualPartition", 10),
          ("systemboardInPartition", 11),
          ("virtualServerVmware", 20),
          ("virtualServerHyperV", 21),
          ("virtualServerXen", 22),
          ("virtualServerPan", 23))
    )





class CompStatus(Integer32):
    """Custom type CompStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("warning", 2),
          ("error", 3),
          ("unknown", 5),
          ("notPresent", 6),
          ("notManageable", 7))
    )





class LogSeverity(Integer32):
    """Custom type LogSeverity based on Integer32"""
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
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )





class OsLogSeverity(Integer32):
    """Custom type OsLogSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("warning", 2),
          ("error", 3))
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Enterprises_ObjectIdentity = ObjectIdentity
enterprises = _Enterprises_ObjectIdentity(
    (1, 3, 6, 1, 4, 1)
)
_Sni_ObjectIdentity = ObjectIdentity
sni = _Sni_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231)
)
_SniProductMibs_ObjectIdentity = ObjectIdentity
sniProductMibs = _SniProductMibs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2)
)
_SniExtensions_ObjectIdentity = ObjectIdentity
sniExtensions = _SniExtensions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10)
)
_SniServerMgmt_ObjectIdentity = ObjectIdentity
sniServerMgmt = _SniServerMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2)
)
_SniInventory_ObjectIdentity = ObjectIdentity
sniInventory = _SniInventory_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 1)
)
_SniCommon_ObjectIdentity = ObjectIdentity
sniCommon = _SniCommon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2)
)
_FscServerControl2_ObjectIdentity = ObjectIdentity
fscServerControl2 = _FscServerControl2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10)
)
_Sc2AgentInfo_ObjectIdentity = ObjectIdentity
sc2AgentInfo = _Sc2AgentInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 1)
)
_Sc2AgentId_Type = DisplayString
_Sc2AgentId_Object = MibScalar
sc2AgentId = _Sc2AgentId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 1, 1),
    _Sc2AgentId_Type()
)
sc2AgentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2AgentId.setStatus("mandatory")
_Sc2AgentCompany_Type = DisplayString
_Sc2AgentCompany_Object = MibScalar
sc2AgentCompany = _Sc2AgentCompany_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 1, 2),
    _Sc2AgentCompany_Type()
)
sc2AgentCompany.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2AgentCompany.setStatus("mandatory")
_Sc2AgentVersion_Type = DisplayString
_Sc2AgentVersion_Object = MibScalar
sc2AgentVersion = _Sc2AgentVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 1, 3),
    _Sc2AgentVersion_Type()
)
sc2AgentVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2AgentVersion.setStatus("mandatory")
_Sc2AgentBuild_Type = DisplayString
_Sc2AgentBuild_Object = MibScalar
sc2AgentBuild = _Sc2AgentBuild_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 1, 4),
    _Sc2AgentBuild_Type()
)
sc2AgentBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2AgentBuild.setStatus("mandatory")


class _Sc2AgentWriteAllowed_Type(Integer32):
    """Custom type sc2AgentWriteAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("write-not-allowed", 2),
          ("write-allowed", 3))
    )


_Sc2AgentWriteAllowed_Type.__name__ = "Integer32"
_Sc2AgentWriteAllowed_Object = MibScalar
sc2AgentWriteAllowed = _Sc2AgentWriteAllowed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 1, 5),
    _Sc2AgentWriteAllowed_Type()
)
sc2AgentWriteAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2AgentWriteAllowed.setStatus("mandatory")


class _Sc2AgentShutdownAllowed_Type(Integer32):
    """Custom type sc2AgentShutdownAllowed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("shutdown-not-allowed", 2),
          ("shutdown-allowed", 3))
    )


_Sc2AgentShutdownAllowed_Type.__name__ = "Integer32"
_Sc2AgentShutdownAllowed_Object = MibScalar
sc2AgentShutdownAllowed = _Sc2AgentShutdownAllowed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 1, 6),
    _Sc2AgentShutdownAllowed_Type()
)
sc2AgentShutdownAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2AgentShutdownAllowed.setStatus("mandatory")
_Sc2UnitInformation_ObjectIdentity = ObjectIdentity
sc2UnitInformation = _Sc2UnitInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2)
)
_Sc2LocalServerUnitId_Type = Integer32
_Sc2LocalServerUnitId_Object = MibScalar
sc2LocalServerUnitId = _Sc2LocalServerUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 1),
    _Sc2LocalServerUnitId_Type()
)
sc2LocalServerUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2LocalServerUnitId.setStatus("mandatory")
_Sc2NumberUnits_Type = Integer32
_Sc2NumberUnits_Object = MibScalar
sc2NumberUnits = _Sc2NumberUnits_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 2),
    _Sc2NumberUnits_Type()
)
sc2NumberUnits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2NumberUnits.setStatus("mandatory")
_Sc2UnitTable_Object = MibTable
sc2UnitTable = _Sc2UnitTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3)
)
if mibBuilder.loadTexts:
    sc2UnitTable.setStatus("mandatory")
_Sc2Units_Object = MibTableRow
sc2Units = _Sc2Units_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1)
)
sc2Units.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2uUnitId"),
)
if mibBuilder.loadTexts:
    sc2Units.setStatus("mandatory")
_Sc2uUnitId_Type = Integer32
_Sc2uUnitId_Object = MibTableColumn
sc2uUnitId = _Sc2uUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 1),
    _Sc2uUnitId_Type()
)
sc2uUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2uUnitId.setStatus("mandatory")
_Sc2UnitClass_Type = UnitClass
_Sc2UnitClass_Object = MibTableColumn
sc2UnitClass = _Sc2UnitClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 2),
    _Sc2UnitClass_Type()
)
sc2UnitClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitClass.setStatus("mandatory")
_Sc2UnitCabinetNr_Type = Integer32
_Sc2UnitCabinetNr_Object = MibTableColumn
sc2UnitCabinetNr = _Sc2UnitCabinetNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 3),
    _Sc2UnitCabinetNr_Type()
)
sc2UnitCabinetNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitCabinetNr.setStatus("mandatory")
_Sc2UnitDesignation_Type = DisplayString
_Sc2UnitDesignation_Object = MibTableColumn
sc2UnitDesignation = _Sc2UnitDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 4),
    _Sc2UnitDesignation_Type()
)
sc2UnitDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitDesignation.setStatus("mandatory")
_Sc2UnitModelName_Type = DisplayString
_Sc2UnitModelName_Object = MibTableColumn
sc2UnitModelName = _Sc2UnitModelName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 5),
    _Sc2UnitModelName_Type()
)
sc2UnitModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitModelName.setStatus("mandatory")
_Sc2UnitManufacturer_Type = DisplayString
_Sc2UnitManufacturer_Object = MibTableColumn
sc2UnitManufacturer = _Sc2UnitManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 6),
    _Sc2UnitManufacturer_Type()
)
sc2UnitManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitManufacturer.setStatus("mandatory")
_Sc2UnitSerialNumber_Type = DisplayString
_Sc2UnitSerialNumber_Object = MibTableColumn
sc2UnitSerialNumber = _Sc2UnitSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 7),
    _Sc2UnitSerialNumber_Type()
)
sc2UnitSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitSerialNumber.setStatus("mandatory")
_Sc2UnitLocation_Type = DisplayString
_Sc2UnitLocation_Object = MibTableColumn
sc2UnitLocation = _Sc2UnitLocation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 8),
    _Sc2UnitLocation_Type()
)
sc2UnitLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitLocation.setStatus("mandatory")
_Sc2UnitContact_Type = DisplayString
_Sc2UnitContact_Object = MibTableColumn
sc2UnitContact = _Sc2UnitContact_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 9),
    _Sc2UnitContact_Type()
)
sc2UnitContact.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitContact.setStatus("mandatory")
_Sc2UnitAdminURL_Type = DisplayString
_Sc2UnitAdminURL_Object = MibTableColumn
sc2UnitAdminURL = _Sc2UnitAdminURL_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 10),
    _Sc2UnitAdminURL_Type()
)
sc2UnitAdminURL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitAdminURL.setStatus("mandatory")


class _Sc2FrontDoorStatus_Type(Integer32):
    """Custom type sc2FrontDoorStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("open", 2),
          ("closed", 3))
    )


_Sc2FrontDoorStatus_Type.__name__ = "Integer32"
_Sc2FrontDoorStatus_Object = MibTableColumn
sc2FrontDoorStatus = _Sc2FrontDoorStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 11),
    _Sc2FrontDoorStatus_Type()
)
sc2FrontDoorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2FrontDoorStatus.setStatus("mandatory")


class _Sc2HousingOpenStatus_Type(Integer32):
    """Custom type sc2HousingOpenStatus based on Integer32"""
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
        *(("unknown", 1),
          ("open", 2),
          ("closed", 3),
          ("opened-and-closed", 4))
    )


_Sc2HousingOpenStatus_Type.__name__ = "Integer32"
_Sc2HousingOpenStatus_Object = MibTableColumn
sc2HousingOpenStatus = _Sc2HousingOpenStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 12),
    _Sc2HousingOpenStatus_Type()
)
sc2HousingOpenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2HousingOpenStatus.setStatus("mandatory")
_Sc2MsgLogLanguages_Type = DisplayString
_Sc2MsgLogLanguages_Object = MibTableColumn
sc2MsgLogLanguages = _Sc2MsgLogLanguages_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 13),
    _Sc2MsgLogLanguages_Type()
)
sc2MsgLogLanguages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2MsgLogLanguages.setStatus("mandatory")
_Sc2UnitWorldWideName_Type = DisplayString
_Sc2UnitWorldWideName_Object = MibTableColumn
sc2UnitWorldWideName = _Sc2UnitWorldWideName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 14),
    _Sc2UnitWorldWideName_Type()
)
sc2UnitWorldWideName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitWorldWideName.setStatus("mandatory")
_Sc2RemcsId_Type = DisplayString
_Sc2RemcsId_Object = MibTableColumn
sc2RemcsId = _Sc2RemcsId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 15),
    _Sc2RemcsId_Type()
)
sc2RemcsId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2RemcsId.setStatus("mandatory")
_Sc2AssetTag_Type = DisplayString
_Sc2AssetTag_Object = MibTableColumn
sc2AssetTag = _Sc2AssetTag_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 16),
    _Sc2AssetTag_Type()
)
sc2AssetTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2AssetTag.setStatus("mandatory")
_Sc2MsgLogAvailable_Type = TrueFalse
_Sc2MsgLogAvailable_Object = MibTableColumn
sc2MsgLogAvailable = _Sc2MsgLogAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 17),
    _Sc2MsgLogAvailable_Type()
)
sc2MsgLogAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2MsgLogAvailable.setStatus("mandatory")
_Sc2ManagementIpAddress_Type = DisplayString
_Sc2ManagementIpAddress_Object = MibTableColumn
sc2ManagementIpAddress = _Sc2ManagementIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 18),
    _Sc2ManagementIpAddress_Type()
)
sc2ManagementIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2ManagementIpAddress.setStatus("mandatory")
_Sc2HasUefiFirmware_Type = TrueFalse
_Sc2HasUefiFirmware_Object = MibTableColumn
sc2HasUefiFirmware = _Sc2HasUefiFirmware_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 19),
    _Sc2HasUefiFirmware_Type()
)
sc2HasUefiFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2HasUefiFirmware.setStatus("mandatory")
_Sc2ManagementIpAddressV6_Type = DisplayString
_Sc2ManagementIpAddressV6_Object = MibTableColumn
sc2ManagementIpAddressV6 = _Sc2ManagementIpAddressV6_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 3, 1, 20),
    _Sc2ManagementIpAddressV6_Type()
)
sc2ManagementIpAddressV6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2ManagementIpAddressV6.setStatus("mandatory")
_Sc2UnitTableUpdateCount_Type = Counter32
_Sc2UnitTableUpdateCount_Object = MibScalar
sc2UnitTableUpdateCount = _Sc2UnitTableUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 4),
    _Sc2UnitTableUpdateCount_Type()
)
sc2UnitTableUpdateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitTableUpdateCount.setStatus("mandatory")
_Sc2UnitParentTable_Object = MibTable
sc2UnitParentTable = _Sc2UnitParentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 5)
)
if mibBuilder.loadTexts:
    sc2UnitParentTable.setStatus("mandatory")
_Sc2UnitParents_Object = MibTableRow
sc2UnitParents = _Sc2UnitParents_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 5, 1)
)
sc2UnitParents.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2pUnitId"),
)
if mibBuilder.loadTexts:
    sc2UnitParents.setStatus("mandatory")
_Sc2pUnitId_Type = Integer32
_Sc2pUnitId_Object = MibTableColumn
sc2pUnitId = _Sc2pUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 5, 1, 1),
    _Sc2pUnitId_Type()
)
sc2pUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pUnitId.setStatus("mandatory")
_Sc2ParentUnit_Type = Integer32
_Sc2ParentUnit_Object = MibTableColumn
sc2ParentUnit = _Sc2ParentUnit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 5, 1, 2),
    _Sc2ParentUnit_Type()
)
sc2ParentUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2ParentUnit.setStatus("mandatory")
_Sc2ParentUnitClass_Type = UnitClass
_Sc2ParentUnitClass_Object = MibTableColumn
sc2ParentUnitClass = _Sc2ParentUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 5, 1, 3),
    _Sc2ParentUnitClass_Type()
)
sc2ParentUnitClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2ParentUnitClass.setStatus("mandatory")
_Sc2UnitChildTable_Object = MibTable
sc2UnitChildTable = _Sc2UnitChildTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 6)
)
if mibBuilder.loadTexts:
    sc2UnitChildTable.setStatus("mandatory")
_Sc2UnitChilds_Object = MibTableRow
sc2UnitChilds = _Sc2UnitChilds_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 6, 1)
)
sc2UnitChilds.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2cUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2cChildNr"),
)
if mibBuilder.loadTexts:
    sc2UnitChilds.setStatus("mandatory")
_Sc2cUnitId_Type = Integer32
_Sc2cUnitId_Object = MibTableColumn
sc2cUnitId = _Sc2cUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 6, 1, 1),
    _Sc2cUnitId_Type()
)
sc2cUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cUnitId.setStatus("mandatory")
_Sc2cChildNr_Type = Integer32
_Sc2cChildNr_Object = MibTableColumn
sc2cChildNr = _Sc2cChildNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 6, 1, 2),
    _Sc2cChildNr_Type()
)
sc2cChildNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cChildNr.setStatus("mandatory")
_Sc2ChildUnit_Type = Integer32
_Sc2ChildUnit_Object = MibTableColumn
sc2ChildUnit = _Sc2ChildUnit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 6, 1, 3),
    _Sc2ChildUnit_Type()
)
sc2ChildUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2ChildUnit.setStatus("mandatory")
_Sc2ChildUnitClass_Type = UnitClass
_Sc2ChildUnitClass_Object = MibTableColumn
sc2ChildUnitClass = _Sc2ChildUnitClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 2, 6, 1, 4),
    _Sc2ChildUnitClass_Type()
)
sc2ChildUnitClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2ChildUnitClass.setStatus("mandatory")
_Sc2Management_ObjectIdentity = ObjectIdentity
sc2Management = _Sc2Management_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3)
)
_Sc2ManagementNodeTable_Object = MibTable
sc2ManagementNodeTable = _Sc2ManagementNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1)
)
if mibBuilder.loadTexts:
    sc2ManagementNodeTable.setStatus("mandatory")
_Sc2ManagementNodes_Object = MibTableRow
sc2ManagementNodes = _Sc2ManagementNodes_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1)
)
sc2ManagementNodes.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2mnUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2mnNodeNr"),
)
if mibBuilder.loadTexts:
    sc2ManagementNodes.setStatus("mandatory")
_Sc2mnUnitId_Type = Integer32
_Sc2mnUnitId_Object = MibTableColumn
sc2mnUnitId = _Sc2mnUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 1),
    _Sc2mnUnitId_Type()
)
sc2mnUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2mnUnitId.setStatus("mandatory")
_Sc2mnNodeNr_Type = Integer32
_Sc2mnNodeNr_Object = MibTableColumn
sc2mnNodeNr = _Sc2mnNodeNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 2),
    _Sc2mnNodeNr_Type()
)
sc2mnNodeNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2mnNodeNr.setStatus("mandatory")


class _Sc2UnitNodeIfType_Type(Integer32):
    """Custom type sc2UnitNodeIfType based on Integer32"""
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
        *(("unknown", 1),
          ("ip", 2),
          ("ipx", 3),
          ("ip-v6", 4))
    )


_Sc2UnitNodeIfType_Type.__name__ = "Integer32"
_Sc2UnitNodeIfType_Object = MibTableColumn
sc2UnitNodeIfType = _Sc2UnitNodeIfType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 3),
    _Sc2UnitNodeIfType_Type()
)
sc2UnitNodeIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeIfType.setStatus("mandatory")
_Sc2UnitNodeAddress_Type = DisplayString
_Sc2UnitNodeAddress_Object = MibTableColumn
sc2UnitNodeAddress = _Sc2UnitNodeAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 4),
    _Sc2UnitNodeAddress_Type()
)
sc2UnitNodeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeAddress.setStatus("mandatory")
_Sc2UnitNodeIpNetmask_Type = DisplayString
_Sc2UnitNodeIpNetmask_Object = MibTableColumn
sc2UnitNodeIpNetmask = _Sc2UnitNodeIpNetmask_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 5),
    _Sc2UnitNodeIpNetmask_Type()
)
sc2UnitNodeIpNetmask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeIpNetmask.setStatus("mandatory")
_Sc2UnitNodeGateway_Type = DisplayString
_Sc2UnitNodeGateway_Object = MibTableColumn
sc2UnitNodeGateway = _Sc2UnitNodeGateway_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 6),
    _Sc2UnitNodeGateway_Type()
)
sc2UnitNodeGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeGateway.setStatus("mandatory")
_Sc2UnitNodeName_Type = DisplayString
_Sc2UnitNodeName_Object = MibTableColumn
sc2UnitNodeName = _Sc2UnitNodeName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 7),
    _Sc2UnitNodeName_Type()
)
sc2UnitNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeName.setStatus("mandatory")


class _Sc2UnitNodeClass_Type(Integer32):
    """Custom type sc2UnitNodeClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("primary", 2),
          ("secondary", 3),
          ("management-blade", 4),
          ("secondary-remote", 5),
          ("secondary-remote-backup", 6),
          ("baseboard-controller", 7))
    )


_Sc2UnitNodeClass_Type.__name__ = "Integer32"
_Sc2UnitNodeClass_Object = MibTableColumn
sc2UnitNodeClass = _Sc2UnitNodeClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 8),
    _Sc2UnitNodeClass_Type()
)
sc2UnitNodeClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeClass.setStatus("mandatory")
_Sc2UnitNodeMacAddress_Type = PhysAddress
_Sc2UnitNodeMacAddress_Object = MibTableColumn
sc2UnitNodeMacAddress = _Sc2UnitNodeMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 9),
    _Sc2UnitNodeMacAddress_Type()
)
sc2UnitNodeMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeMacAddress.setStatus("mandatory")


class _Sc2UnitNodeUseDHCP_Type(Integer32):
    """Custom type sc2UnitNodeUseDHCP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("use-fixed-address", 2),
          ("use-dhcp", 3))
    )


_Sc2UnitNodeUseDHCP_Type.__name__ = "Integer32"
_Sc2UnitNodeUseDHCP_Object = MibTableColumn
sc2UnitNodeUseDHCP = _Sc2UnitNodeUseDHCP_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 10),
    _Sc2UnitNodeUseDHCP_Type()
)
sc2UnitNodeUseDHCP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeUseDHCP.setStatus("mandatory")
_Sc2UnitNodeControllerType_Type = DisplayString
_Sc2UnitNodeControllerType_Object = MibTableColumn
sc2UnitNodeControllerType = _Sc2UnitNodeControllerType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 11),
    _Sc2UnitNodeControllerType_Type()
)
sc2UnitNodeControllerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeControllerType.setStatus("mandatory")
_Sc2UnitNodeControllerModel_Type = DisplayString
_Sc2UnitNodeControllerModel_Object = MibTableColumn
sc2UnitNodeControllerModel = _Sc2UnitNodeControllerModel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 12),
    _Sc2UnitNodeControllerModel_Type()
)
sc2UnitNodeControllerModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeControllerModel.setStatus("mandatory")
_Sc2UnitNodeControllerFWVersion_Type = DisplayString
_Sc2UnitNodeControllerFWVersion_Object = MibTableColumn
sc2UnitNodeControllerFWVersion = _Sc2UnitNodeControllerFWVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 13),
    _Sc2UnitNodeControllerFWVersion_Type()
)
sc2UnitNodeControllerFWVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeControllerFWVersion.setStatus("mandatory")


class _Sc2UnitNodeControllerStorage_Type(Integer32):
    """Custom type sc2UnitNodeControllerStorage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("not-available", 2),
          ("available-sdcard", 3))
    )


_Sc2UnitNodeControllerStorage_Type.__name__ = "Integer32"
_Sc2UnitNodeControllerStorage_Object = MibTableColumn
sc2UnitNodeControllerStorage = _Sc2UnitNodeControllerStorage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 14),
    _Sc2UnitNodeControllerStorage_Type()
)
sc2UnitNodeControllerStorage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeControllerStorage.setStatus("mandatory")
_Sc2UnitNodeSNMPEnabled_Type = TrueFalseUnknown
_Sc2UnitNodeSNMPEnabled_Object = MibTableColumn
sc2UnitNodeSNMPEnabled = _Sc2UnitNodeSNMPEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 15),
    _Sc2UnitNodeSNMPEnabled_Type()
)
sc2UnitNodeSNMPEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeSNMPEnabled.setStatus("mandatory")
_Sc2UnitNodeCIMEnabled_Type = TrueFalseUnknown
_Sc2UnitNodeCIMEnabled_Object = MibTableColumn
sc2UnitNodeCIMEnabled = _Sc2UnitNodeCIMEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 16),
    _Sc2UnitNodeCIMEnabled_Type()
)
sc2UnitNodeCIMEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeCIMEnabled.setStatus("mandatory")
_Sc2UnitNodeRemoteIPMIEnabled_Type = TrueFalseUnknown
_Sc2UnitNodeRemoteIPMIEnabled_Object = MibTableColumn
sc2UnitNodeRemoteIPMIEnabled = _Sc2UnitNodeRemoteIPMIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 1, 1, 17),
    _Sc2UnitNodeRemoteIPMIEnabled_Type()
)
sc2UnitNodeRemoteIPMIEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UnitNodeRemoteIPMIEnabled.setStatus("mandatory")
_Sc2NodeTableUpdateCount_Type = Counter32
_Sc2NodeTableUpdateCount_Object = MibScalar
sc2NodeTableUpdateCount = _Sc2NodeTableUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 2),
    _Sc2NodeTableUpdateCount_Type()
)
sc2NodeTableUpdateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2NodeTableUpdateCount.setStatus("mandatory")


class _Sc2ManagementChannelType_Type(Integer32):
    """Custom type sc2ManagementChannelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("primary", 2),
          ("secondary", 3))
    )


_Sc2ManagementChannelType_Type.__name__ = "Integer32"
_Sc2ManagementChannelType_Object = MibScalar
sc2ManagementChannelType = _Sc2ManagementChannelType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 3),
    _Sc2ManagementChannelType_Type()
)
sc2ManagementChannelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2ManagementChannelType.setStatus("mandatory")
_Sc2ManagementProcessorTable_Object = MibTable
sc2ManagementProcessorTable = _Sc2ManagementProcessorTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4)
)
if mibBuilder.loadTexts:
    sc2ManagementProcessorTable.setStatus("mandatory")
_Sc2ManagementProcessors_Object = MibTableRow
sc2ManagementProcessors = _Sc2ManagementProcessors_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1)
)
sc2ManagementProcessors.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2spUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2spProcessorNr"),
)
if mibBuilder.loadTexts:
    sc2ManagementProcessors.setStatus("mandatory")
_Sc2spUnitId_Type = Integer32
_Sc2spUnitId_Object = MibTableColumn
sc2spUnitId = _Sc2spUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1, 1),
    _Sc2spUnitId_Type()
)
sc2spUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2spUnitId.setStatus("mandatory")
_Sc2spProcessorNr_Type = Integer32
_Sc2spProcessorNr_Object = MibTableColumn
sc2spProcessorNr = _Sc2spProcessorNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1, 2),
    _Sc2spProcessorNr_Type()
)
sc2spProcessorNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2spProcessorNr.setStatus("mandatory")
_Sc2spModelName_Type = DisplayString
_Sc2spModelName_Object = MibTableColumn
sc2spModelName = _Sc2spModelName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1, 3),
    _Sc2spModelName_Type()
)
sc2spModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2spModelName.setStatus("mandatory")
_Sc2spFirmwareVersion_Type = DisplayString
_Sc2spFirmwareVersion_Object = MibTableColumn
sc2spFirmwareVersion = _Sc2spFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1, 4),
    _Sc2spFirmwareVersion_Type()
)
sc2spFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2spFirmwareVersion.setStatus("mandatory")


class _Sc2spBatteryStatus_Type(Integer32):
    """Custom type sc2spBatteryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("not-present", 2),
          ("ok", 3),
          ("on-battery", 4),
          ("recharging", 5),
          ("failed", 6),
          ("discharging", 7))
    )


_Sc2spBatteryStatus_Type.__name__ = "Integer32"
_Sc2spBatteryStatus_Object = MibTableColumn
sc2spBatteryStatus = _Sc2spBatteryStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1, 5),
    _Sc2spBatteryStatus_Type()
)
sc2spBatteryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2spBatteryStatus.setStatus("mandatory")
_Sc2spBatteryDischargeTime_Type = Integer32
_Sc2spBatteryDischargeTime_Object = MibTableColumn
sc2spBatteryDischargeTime = _Sc2spBatteryDischargeTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1, 6),
    _Sc2spBatteryDischargeTime_Type()
)
sc2spBatteryDischargeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2spBatteryDischargeTime.setStatus("mandatory")
_Sc2spTimeOnBattery_Type = Counter32
_Sc2spTimeOnBattery_Object = MibTableColumn
sc2spTimeOnBattery = _Sc2spTimeOnBattery_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1, 7),
    _Sc2spTimeOnBattery_Type()
)
sc2spTimeOnBattery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2spTimeOnBattery.setStatus("mandatory")
_Sc2spDoBatteryChargeCycle_Type = Integer32
_Sc2spDoBatteryChargeCycle_Object = MibTableColumn
sc2spDoBatteryChargeCycle = _Sc2spDoBatteryChargeCycle_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1, 8),
    _Sc2spDoBatteryChargeCycle_Type()
)
sc2spDoBatteryChargeCycle.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2spDoBatteryChargeCycle.setStatus("mandatory")
_Sc2spBatteryChargeLevel_Type = Gauge32
_Sc2spBatteryChargeLevel_Object = MibTableColumn
sc2spBatteryChargeLevel = _Sc2spBatteryChargeLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 4, 1, 9),
    _Sc2spBatteryChargeLevel_Type()
)
sc2spBatteryChargeLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2spBatteryChargeLevel.setStatus("mandatory")
_Sc2ManagedUpsNodeTable_Object = MibTable
sc2ManagedUpsNodeTable = _Sc2ManagedUpsNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 5)
)
if mibBuilder.loadTexts:
    sc2ManagedUpsNodeTable.setStatus("mandatory")
_Sc2ManagedUpsNodes_Object = MibTableRow
sc2ManagedUpsNodes = _Sc2ManagedUpsNodes_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 5, 1)
)
sc2ManagedUpsNodes.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2upsUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2upsNr"),
)
if mibBuilder.loadTexts:
    sc2ManagedUpsNodes.setStatus("mandatory")
_Sc2upsUnitId_Type = Integer32
_Sc2upsUnitId_Object = MibTableColumn
sc2upsUnitId = _Sc2upsUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 5, 1, 1),
    _Sc2upsUnitId_Type()
)
sc2upsUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2upsUnitId.setStatus("mandatory")
_Sc2upsNr_Type = Integer32
_Sc2upsNr_Object = MibTableColumn
sc2upsNr = _Sc2upsNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 5, 1, 2),
    _Sc2upsNr_Type()
)
sc2upsNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2upsNr.setStatus("mandatory")
_Sc2upsVendorName_Type = DisplayString
_Sc2upsVendorName_Object = MibTableColumn
sc2upsVendorName = _Sc2upsVendorName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 5, 1, 3),
    _Sc2upsVendorName_Type()
)
sc2upsVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2upsVendorName.setStatus("mandatory")
_Sc2upsModelName_Type = DisplayString
_Sc2upsModelName_Object = MibTableColumn
sc2upsModelName = _Sc2upsModelName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 5, 1, 4),
    _Sc2upsModelName_Type()
)
sc2upsModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2upsModelName.setStatus("mandatory")
_Sc2upsMgmtAddress_Type = DisplayString
_Sc2upsMgmtAddress_Object = MibTableColumn
sc2upsMgmtAddress = _Sc2upsMgmtAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 5, 1, 5),
    _Sc2upsMgmtAddress_Type()
)
sc2upsMgmtAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2upsMgmtAddress.setStatus("mandatory")
_Sc2upsMibRoot_Type = DisplayString
_Sc2upsMibRoot_Object = MibTableColumn
sc2upsMibRoot = _Sc2upsMibRoot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 5, 1, 6),
    _Sc2upsMibRoot_Type()
)
sc2upsMibRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2upsMibRoot.setStatus("mandatory")
_Sc2upsSnmpCommunity_Type = DisplayString
_Sc2upsSnmpCommunity_Object = MibTableColumn
sc2upsSnmpCommunity = _Sc2upsSnmpCommunity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 5, 1, 7),
    _Sc2upsSnmpCommunity_Type()
)
sc2upsSnmpCommunity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2upsSnmpCommunity.setStatus("mandatory")
_Sc2UpsNodeTableUpdateCount_Type = Counter32
_Sc2UpsNodeTableUpdateCount_Object = MibScalar
sc2UpsNodeTableUpdateCount = _Sc2UpsNodeTableUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 3, 6),
    _Sc2UpsNodeTableUpdateCount_Type()
)
sc2UpsNodeTableUpdateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2UpsNodeTableUpdateCount.setStatus("mandatory")
_Sc2ServerInformation_ObjectIdentity = ObjectIdentity
sc2ServerInformation = _Sc2ServerInformation_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4)
)
_Sc2ServerTable_Object = MibTable
sc2ServerTable = _Sc2ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1)
)
if mibBuilder.loadTexts:
    sc2ServerTable.setStatus("mandatory")
_Sc2Servers_Object = MibTableRow
sc2Servers = _Sc2Servers_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1)
)
sc2Servers.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2srvUnitId"),
)
if mibBuilder.loadTexts:
    sc2Servers.setStatus("mandatory")
_Sc2srvUnitId_Type = Integer32
_Sc2srvUnitId_Object = MibTableColumn
sc2srvUnitId = _Sc2srvUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 1),
    _Sc2srvUnitId_Type()
)
sc2srvUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvUnitId.setStatus("mandatory")
_Sc2srvPhysicalMemory_Type = Integer32
_Sc2srvPhysicalMemory_Object = MibTableColumn
sc2srvPhysicalMemory = _Sc2srvPhysicalMemory_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 2),
    _Sc2srvPhysicalMemory_Type()
)
sc2srvPhysicalMemory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvPhysicalMemory.setStatus("mandatory")


class _Sc2srvLastBootResult_Type(Integer32):
    """Custom type sc2srvLastBootResult based on Integer32"""
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
        *(("unknown", 1),
          ("os-boot-successful", 2),
          ("diagnostic-boot-successful", 3),
          ("no-boot-cpu", 4),
          ("no-bootable-media", 5),
          ("os-failed-to-load", 6),
          ("diagnostic-boot-failed", 7),
          ("hardware-failure", 8))
    )


_Sc2srvLastBootResult_Type.__name__ = "Integer32"
_Sc2srvLastBootResult_Object = MibTableColumn
sc2srvLastBootResult = _Sc2srvLastBootResult_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 3),
    _Sc2srvLastBootResult_Type()
)
sc2srvLastBootResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvLastBootResult.setStatus("mandatory")


class _Sc2srvCurrentBootStatus_Type(Integer32):
    """Custom type sc2srvCurrentBootStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("off", 2),
          ("no-boot-cpu", 3),
          ("self-test", 4),
          ("setup", 5),
          ("os-boot", 6),
          ("diagnostic-boot", 7),
          ("os-running", 8),
          ("diagnostic-running", 9),
          ("os-shutdown", 10),
          ("diagnostic-shutdown", 11),
          ("reset", 12))
    )


_Sc2srvCurrentBootStatus_Type.__name__ = "Integer32"
_Sc2srvCurrentBootStatus_Object = MibTableColumn
sc2srvCurrentBootStatus = _Sc2srvCurrentBootStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 4),
    _Sc2srvCurrentBootStatus_Type()
)
sc2srvCurrentBootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvCurrentBootStatus.setStatus("mandatory")


class _Sc2srvShutdownCommand_Type(Integer32):
    """Custom type sc2srvShutdownCommand based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("power-off", 2),
          ("power-on", 3),
          ("power-cycle", 4),
          ("shutdown-and-off", 5),
          ("shutdown-and-reset", 6),
          ("shutdown-and-power-cycle", 7),
          ("raise-nmi", 8),
          ("abort-pending-command", 9),
          ("reset", 10))
    )


_Sc2srvShutdownCommand_Type.__name__ = "Integer32"
_Sc2srvShutdownCommand_Object = MibTableColumn
sc2srvShutdownCommand = _Sc2srvShutdownCommand_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 5),
    _Sc2srvShutdownCommand_Type()
)
sc2srvShutdownCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2srvShutdownCommand.setStatus("mandatory")
_Sc2srvShutdownDelay_Type = Integer32
_Sc2srvShutdownDelay_Object = MibTableColumn
sc2srvShutdownDelay = _Sc2srvShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 6),
    _Sc2srvShutdownDelay_Type()
)
sc2srvShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2srvShutdownDelay.setStatus("mandatory")
_Sc2srvUUID_Type = DisplayString
_Sc2srvUUID_Object = MibTableColumn
sc2srvUUID = _Sc2srvUUID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 7),
    _Sc2srvUUID_Type()
)
sc2srvUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvUUID.setStatus("mandatory")
_Sc2srvPhysicalMemoryOs_Type = Integer32
_Sc2srvPhysicalMemoryOs_Object = MibTableColumn
sc2srvPhysicalMemoryOs = _Sc2srvPhysicalMemoryOs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 8),
    _Sc2srvPhysicalMemoryOs_Type()
)
sc2srvPhysicalMemoryOs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvPhysicalMemoryOs.setStatus("mandatory")
_Sc2srvUUIDWireFormat_Type = DisplayString
_Sc2srvUUIDWireFormat_Object = MibTableColumn
sc2srvUUIDWireFormat = _Sc2srvUUIDWireFormat_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 9),
    _Sc2srvUUIDWireFormat_Type()
)
sc2srvUUIDWireFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvUUIDWireFormat.setStatus("mandatory")


class _Sc2srvOsPlatform_Type(Integer32):
    """Custom type sc2srvOsPlatform based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("intel-x86", 2),
          ("intel-x64", 3))
    )


_Sc2srvOsPlatform_Type.__name__ = "Integer32"
_Sc2srvOsPlatform_Object = MibTableColumn
sc2srvOsPlatform = _Sc2srvOsPlatform_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 10),
    _Sc2srvOsPlatform_Type()
)
sc2srvOsPlatform.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvOsPlatform.setStatus("mandatory")
_Sc2srvBiosVersion_Type = DisplayString
_Sc2srvBiosVersion_Object = MibTableColumn
sc2srvBiosVersion = _Sc2srvBiosVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 11),
    _Sc2srvBiosVersion_Type()
)
sc2srvBiosVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvBiosVersion.setStatus("mandatory")
_Sc2srvHasEncryptedPartitions_Type = TrueFalseUnknown
_Sc2srvHasEncryptedPartitions_Object = MibTableColumn
sc2srvHasEncryptedPartitions = _Sc2srvHasEncryptedPartitions_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 12),
    _Sc2srvHasEncryptedPartitions_Type()
)
sc2srvHasEncryptedPartitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvHasEncryptedPartitions.setStatus("mandatory")
_Sc2srvTrustedExecutionTechnologyEnabled_Type = TrueFalseUnknown
_Sc2srvTrustedExecutionTechnologyEnabled_Object = MibTableColumn
sc2srvTrustedExecutionTechnologyEnabled = _Sc2srvTrustedExecutionTechnologyEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 1, 1, 13),
    _Sc2srvTrustedExecutionTechnologyEnabled_Type()
)
sc2srvTrustedExecutionTechnologyEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2srvTrustedExecutionTechnologyEnabled.setStatus("mandatory")
_Sc2UnitPowerOnOffTable_Object = MibTable
sc2UnitPowerOnOffTable = _Sc2UnitPowerOnOffTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2)
)
if mibBuilder.loadTexts:
    sc2UnitPowerOnOffTable.setStatus("mandatory")
_Sc2UnitPowerOnOff_Object = MibTableRow
sc2UnitPowerOnOff = _Sc2UnitPowerOnOff_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1)
)
sc2UnitPowerOnOff.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2ooUnitId"),
)
if mibBuilder.loadTexts:
    sc2UnitPowerOnOff.setStatus("mandatory")
_Sc2ooUnitId_Type = Integer32
_Sc2ooUnitId_Object = MibTableColumn
sc2ooUnitId = _Sc2ooUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 1),
    _Sc2ooUnitId_Type()
)
sc2ooUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2ooUnitId.setStatus("mandatory")


class _Sc2PowerOnOffStatus_Type(Integer32):
    """Custom type sc2PowerOnOffStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("off", 2),
          ("on", 3))
    )


_Sc2PowerOnOffStatus_Type.__name__ = "Integer32"
_Sc2PowerOnOffStatus_Object = MibTableColumn
sc2PowerOnOffStatus = _Sc2PowerOnOffStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 2),
    _Sc2PowerOnOffStatus_Type()
)
sc2PowerOnOffStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerOnOffStatus.setStatus("mandatory")


class _Sc2LastPowerOffSource_Type(Integer32):
    """Custom type sc2LastPowerOffSource based on Integer32"""
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
              23,
              24,
              25,
              26,
              29,
              31,
              32,
              33,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              242,
              243)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("swoff-command", 2),
          ("power-button", 3),
          ("ac-fail", 4),
          ("clock", 5),
          ("fan-fail", 6),
          ("temperature-critical", 7),
          ("temperature-damage", 8),
          ("power-supply-failure", 9),
          ("watchdog", 10),
          ("remote-off", 11),
          ("hardware-fail", 12),
          ("peripheral-bus-error", 13),
          ("cpu-error", 14),
          ("nmi", 20),
          ("hardware-reset", 23),
          ("warmstart", 24),
          ("reset-button", 25),
          ("ac-fail-reboot", 26),
          ("keyboard", 29),
          ("remote-manager", 31),
          ("remote-manager-reset", 32),
          ("power-cycle", 33),
          ("power-limiting", 35),
          ("mmb-continuous-operation", 36),
          ("watchdog-power-cycle", 37),
          ("viom-inventory-board", 38),
          ("viom-init-boot", 39),
          ("repeated-fan-fail", 40),
          ("repeated-temperature-critical", 41),
          ("firmware-restart", 242),
          ("housing-opened", 243))
    )


_Sc2LastPowerOffSource_Type.__name__ = "Integer32"
_Sc2LastPowerOffSource_Object = MibTableColumn
sc2LastPowerOffSource = _Sc2LastPowerOffSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 3),
    _Sc2LastPowerOffSource_Type()
)
sc2LastPowerOffSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2LastPowerOffSource.setStatus("mandatory")


class _Sc2LastPowerOnSource_Type(Integer32):
    """Custom type sc2LastPowerOnSource based on Integer32"""
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
              38,
              39,
              242,
              243)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("swon-command", 2),
          ("power-button", 3),
          ("ac-fail", 4),
          ("clock", 5),
          ("fan-fail", 6),
          ("temperature-critical", 7),
          ("temperature-damage", 8),
          ("power-supply-failure", 9),
          ("watchdog", 10),
          ("remote-on", 11),
          ("hardware-fail", 12),
          ("peripheral-bus-error", 13),
          ("cpu-error", 14),
          ("nmi", 20),
          ("hardware-reset", 23),
          ("warmstart", 24),
          ("reset-button", 25),
          ("ac-fail-reboot", 26),
          ("mgmt-processor-fail", 27),
          ("pci-pme", 28),
          ("keyboard", 29),
          ("chipcard-reader", 30),
          ("remote-manager", 31),
          ("remote-manager-reset", 32),
          ("power-cycle", 33),
          ("viom-inventory-board", 38),
          ("viom-init-boot", 39),
          ("firmware-restart", 242),
          ("housing-closed", 243))
    )


_Sc2LastPowerOnSource_Type.__name__ = "Integer32"
_Sc2LastPowerOnSource_Object = MibTableColumn
sc2LastPowerOnSource = _Sc2LastPowerOnSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 4),
    _Sc2LastPowerOnSource_Type()
)
sc2LastPowerOnSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2LastPowerOnSource.setStatus("mandatory")
_Sc2LastPowerOnTime_Type = Integer32
_Sc2LastPowerOnTime_Object = MibTableColumn
sc2LastPowerOnTime = _Sc2LastPowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 5),
    _Sc2LastPowerOnTime_Type()
)
sc2LastPowerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2LastPowerOnTime.setStatus("mandatory")
_Sc2PowerOnCounts_Type = Integer32
_Sc2PowerOnCounts_Object = MibTableColumn
sc2PowerOnCounts = _Sc2PowerOnCounts_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 6),
    _Sc2PowerOnCounts_Type()
)
sc2PowerOnCounts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerOnCounts.setStatus("mandatory")
_Sc2PowerOnDuration_Type = Integer32
_Sc2PowerOnDuration_Object = MibTableColumn
sc2PowerOnDuration = _Sc2PowerOnDuration_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 7),
    _Sc2PowerOnDuration_Type()
)
sc2PowerOnDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerOnDuration.setStatus("mandatory")
_Sc2PowerOffDuration_Type = Integer32
_Sc2PowerOffDuration_Object = MibTableColumn
sc2PowerOffDuration = _Sc2PowerOffDuration_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 8),
    _Sc2PowerOffDuration_Type()
)
sc2PowerOffDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerOffDuration.setStatus("mandatory")


class _Sc2PowerFailRecovery_Type(Integer32):
    """Custom type sc2PowerFailRecovery based on Integer32"""
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
        *(("unknown", 1),
          ("not-available", 2),
          ("as-before", 3),
          ("remain-off", 4),
          ("switch-on", 5))
    )


_Sc2PowerFailRecovery_Type.__name__ = "Integer32"
_Sc2PowerFailRecovery_Object = MibTableColumn
sc2PowerFailRecovery = _Sc2PowerFailRecovery_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 9),
    _Sc2PowerFailRecovery_Type()
)
sc2PowerFailRecovery.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerFailRecovery.setStatus("mandatory")


class _Sc2PowerCommand_Type(Integer32):
    """Custom type sc2PowerCommand based on Integer32"""
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
        *(("unknown", 1),
          ("off", 2),
          ("on", 3),
          ("power-cycle", 4))
    )


_Sc2PowerCommand_Type.__name__ = "Integer32"
_Sc2PowerCommand_Object = MibTableColumn
sc2PowerCommand = _Sc2PowerCommand_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 10),
    _Sc2PowerCommand_Type()
)
sc2PowerCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2PowerCommand.setStatus("mandatory")
_Sc2PowerSupplyRedundancy_Type = TrueFalseUnknown
_Sc2PowerSupplyRedundancy_Object = MibTableColumn
sc2PowerSupplyRedundancy = _Sc2PowerSupplyRedundancy_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 11),
    _Sc2PowerSupplyRedundancy_Type()
)
sc2PowerSupplyRedundancy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerSupplyRedundancy.setStatus("mandatory")


class _Sc2PowerSupplyMatchStatus_Type(Integer32):
    """Custom type sc2PowerSupplyMatchStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("ok", 2),
          ("mismatch", 3))
    )


_Sc2PowerSupplyMatchStatus_Type.__name__ = "Integer32"
_Sc2PowerSupplyMatchStatus_Object = MibTableColumn
sc2PowerSupplyMatchStatus = _Sc2PowerSupplyMatchStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 2, 1, 12),
    _Sc2PowerSupplyMatchStatus_Type()
)
sc2PowerSupplyMatchStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerSupplyMatchStatus.setStatus("mandatory")
_Sc2PerformanceTable_Object = MibTable
sc2PerformanceTable = _Sc2PerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 3)
)
if mibBuilder.loadTexts:
    sc2PerformanceTable.setStatus("mandatory")
_Sc2Performance_Object = MibTableRow
sc2Performance = _Sc2Performance_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 3, 1)
)
sc2Performance.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2perfUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2perfNr"),
)
if mibBuilder.loadTexts:
    sc2Performance.setStatus("mandatory")
_Sc2perfUnitId_Type = Integer32
_Sc2perfUnitId_Object = MibTableColumn
sc2perfUnitId = _Sc2perfUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 3, 1, 1),
    _Sc2perfUnitId_Type()
)
sc2perfUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2perfUnitId.setStatus("mandatory")
_Sc2perfNr_Type = Integer32
_Sc2perfNr_Object = MibTableColumn
sc2perfNr = _Sc2perfNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 3, 1, 2),
    _Sc2perfNr_Type()
)
sc2perfNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2perfNr.setStatus("mandatory")


class _Sc2PerformanceType_Type(Integer32):
    """Custom type sc2PerformanceType based on Integer32"""
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
        *(("cpu", 1),
          ("cpu-overall", 2),
          ("pci-load", 3),
          ("pci-efficiency", 4),
          ("pci-transfer", 5),
          ("memory-physical", 6),
          ("memory-total", 7),
          ("memory-percent", 8))
    )


_Sc2PerformanceType_Type.__name__ = "Integer32"
_Sc2PerformanceType_Object = MibTableColumn
sc2PerformanceType = _Sc2PerformanceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 3, 1, 3),
    _Sc2PerformanceType_Type()
)
sc2PerformanceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PerformanceType.setStatus("mandatory")
_Sc2PerformanceObjectNr_Type = Integer32
_Sc2PerformanceObjectNr_Object = MibTableColumn
sc2PerformanceObjectNr = _Sc2PerformanceObjectNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 3, 1, 4),
    _Sc2PerformanceObjectNr_Type()
)
sc2PerformanceObjectNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PerformanceObjectNr.setStatus("mandatory")
_Sc2PerformanceName_Type = DisplayString
_Sc2PerformanceName_Object = MibTableColumn
sc2PerformanceName = _Sc2PerformanceName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 3, 1, 5),
    _Sc2PerformanceName_Type()
)
sc2PerformanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PerformanceName.setStatus("mandatory")
_Sc2PerformanceValue_Type = Gauge32
_Sc2PerformanceValue_Object = MibTableColumn
sc2PerformanceValue = _Sc2PerformanceValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 3, 1, 6),
    _Sc2PerformanceValue_Type()
)
sc2PerformanceValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PerformanceValue.setStatus("mandatory")
_Sc2TimerOnOffTable_Object = MibTable
sc2TimerOnOffTable = _Sc2TimerOnOffTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 4)
)
if mibBuilder.loadTexts:
    sc2TimerOnOffTable.setStatus("mandatory")
_Sc2TimerOnOff_Object = MibTableRow
sc2TimerOnOff = _Sc2TimerOnOff_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 4, 1)
)
sc2TimerOnOff.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2tooUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2tooDayOfWeek"),
)
if mibBuilder.loadTexts:
    sc2TimerOnOff.setStatus("mandatory")
_Sc2tooUnitId_Type = Integer32
_Sc2tooUnitId_Object = MibTableColumn
sc2tooUnitId = _Sc2tooUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 4, 1, 1),
    _Sc2tooUnitId_Type()
)
sc2tooUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tooUnitId.setStatus("mandatory")
_Sc2tooDayOfWeek_Type = Integer32
_Sc2tooDayOfWeek_Object = MibTableColumn
sc2tooDayOfWeek = _Sc2tooDayOfWeek_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 4, 1, 2),
    _Sc2tooDayOfWeek_Type()
)
sc2tooDayOfWeek.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tooDayOfWeek.setStatus("mandatory")
_Sc2OnTime_Type = Integer32
_Sc2OnTime_Object = MibTableColumn
sc2OnTime = _Sc2OnTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 4, 1, 3),
    _Sc2OnTime_Type()
)
sc2OnTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2OnTime.setStatus("mandatory")
_Sc2OffTime_Type = Integer32
_Sc2OffTime_Object = MibTableColumn
sc2OffTime = _Sc2OffTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 4, 1, 4),
    _Sc2OffTime_Type()
)
sc2OffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2OffTime.setStatus("mandatory")
_Sc2PowerMonitoringTable_Object = MibTable
sc2PowerMonitoringTable = _Sc2PowerMonitoringTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5)
)
if mibBuilder.loadTexts:
    sc2PowerMonitoringTable.setStatus("mandatory")
_Sc2PowerMonitoring_Object = MibTableRow
sc2PowerMonitoring = _Sc2PowerMonitoring_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1)
)
sc2PowerMonitoring.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2pmUnitId"),
)
if mibBuilder.loadTexts:
    sc2PowerMonitoring.setStatus("mandatory")
_Sc2pmUnitId_Type = Integer32
_Sc2pmUnitId_Object = MibTableColumn
sc2pmUnitId = _Sc2pmUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 1),
    _Sc2pmUnitId_Type()
)
sc2pmUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmUnitId.setStatus("mandatory")
_Sc2pmCurrentPowerMonitoringAvailable_Type = TrueFalse
_Sc2pmCurrentPowerMonitoringAvailable_Object = MibTableColumn
sc2pmCurrentPowerMonitoringAvailable = _Sc2pmCurrentPowerMonitoringAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 2),
    _Sc2pmCurrentPowerMonitoringAvailable_Type()
)
sc2pmCurrentPowerMonitoringAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmCurrentPowerMonitoringAvailable.setStatus("mandatory")
_Sc2pmCurrentPowerMonitoringEnabled_Type = TrueFalse
_Sc2pmCurrentPowerMonitoringEnabled_Object = MibTableColumn
sc2pmCurrentPowerMonitoringEnabled = _Sc2pmCurrentPowerMonitoringEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 3),
    _Sc2pmCurrentPowerMonitoringEnabled_Type()
)
sc2pmCurrentPowerMonitoringEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmCurrentPowerMonitoringEnabled.setStatus("mandatory")
_Sc2pmNominalPowerConsumption_Type = Integer32
_Sc2pmNominalPowerConsumption_Object = MibTableColumn
sc2pmNominalPowerConsumption = _Sc2pmNominalPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 4),
    _Sc2pmNominalPowerConsumption_Type()
)
sc2pmNominalPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmNominalPowerConsumption.setStatus("mandatory")
_Sc2pmCurrentPowerConsumption_Type = Gauge32
_Sc2pmCurrentPowerConsumption_Object = MibTableColumn
sc2pmCurrentPowerConsumption = _Sc2pmCurrentPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 5),
    _Sc2pmCurrentPowerConsumption_Type()
)
sc2pmCurrentPowerConsumption.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmCurrentPowerConsumption.setStatus("mandatory")


class _Sc2pmCurrentPowerControl_Type(Integer32):
    """Custom type sc2pmCurrentPowerControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disabled", 2),
          ("best-performance", 3),
          ("minimum-power", 4),
          ("automatic", 5),
          ("limited", 7),
          ("low-noise", 8))
    )


_Sc2pmCurrentPowerControl_Type.__name__ = "Integer32"
_Sc2pmCurrentPowerControl_Object = MibTableColumn
sc2pmCurrentPowerControl = _Sc2pmCurrentPowerControl_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 6),
    _Sc2pmCurrentPowerControl_Type()
)
sc2pmCurrentPowerControl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmCurrentPowerControl.setStatus("mandatory")


class _Sc2pmPowerLimitStatus_Type(Integer32):
    """Custom type sc2pmPowerLimitStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("warning", 3),
          ("error", 4),
          ("disabled", 5))
    )


_Sc2pmPowerLimitStatus_Type.__name__ = "Integer32"
_Sc2pmPowerLimitStatus_Object = MibTableColumn
sc2pmPowerLimitStatus = _Sc2pmPowerLimitStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 7),
    _Sc2pmPowerLimitStatus_Type()
)
sc2pmPowerLimitStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmPowerLimitStatus.setStatus("mandatory")
_Sc2pmPowerLimitThreshold_Type = Integer32
_Sc2pmPowerLimitThreshold_Object = MibTableColumn
sc2pmPowerLimitThreshold = _Sc2pmPowerLimitThreshold_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 8),
    _Sc2pmPowerLimitThreshold_Type()
)
sc2pmPowerLimitThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmPowerLimitThreshold.setStatus("mandatory")
_Sc2pmPowerLimitWarning_Type = Integer32
_Sc2pmPowerLimitWarning_Object = MibTableColumn
sc2pmPowerLimitWarning = _Sc2pmPowerLimitWarning_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 9),
    _Sc2pmPowerLimitWarning_Type()
)
sc2pmPowerLimitWarning.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmPowerLimitWarning.setStatus("mandatory")
_Sc2pmRedundancyCritLevel_Type = Integer32
_Sc2pmRedundancyCritLevel_Object = MibTableColumn
sc2pmRedundancyCritLevel = _Sc2pmRedundancyCritLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 10),
    _Sc2pmRedundancyCritLevel_Type()
)
sc2pmRedundancyCritLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmRedundancyCritLevel.setStatus("mandatory")


class _Sc2pmPowerControlMode_Type(Integer32):
    """Custom type sc2pmPowerControlMode based on Integer32"""
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
        *(("unknown", 1),
          ("disabled", 2),
          ("best-performance", 3),
          ("minimum-power", 4),
          ("automatic", 5),
          ("scheduled", 6),
          ("limited", 7),
          ("low-noise", 8))
    )


_Sc2pmPowerControlMode_Type.__name__ = "Integer32"
_Sc2pmPowerControlMode_Object = MibTableColumn
sc2pmPowerControlMode = _Sc2pmPowerControlMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 11),
    _Sc2pmPowerControlMode_Type()
)
sc2pmPowerControlMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmPowerControlMode.setStatus("mandatory")


class _Sc2pmPowerDisplayUnit_Type(Integer32):
    """Custom type sc2pmPowerDisplayUnit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("watt", 2),
          ("btu", 3))
    )


_Sc2pmPowerDisplayUnit_Type.__name__ = "Integer32"
_Sc2pmPowerDisplayUnit_Object = MibTableColumn
sc2pmPowerDisplayUnit = _Sc2pmPowerDisplayUnit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 5, 1, 12),
    _Sc2pmPowerDisplayUnit_Type()
)
sc2pmPowerDisplayUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2pmPowerDisplayUnit.setStatus("mandatory")
_Sc2UtilizationHistoryTable_Object = MibTable
sc2UtilizationHistoryTable = _Sc2UtilizationHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 6)
)
if mibBuilder.loadTexts:
    sc2UtilizationHistoryTable.setStatus("mandatory")
_Sc2UtilizationHistory_Object = MibTableRow
sc2UtilizationHistory = _Sc2UtilizationHistory_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 6, 1)
)
sc2UtilizationHistory.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2uthUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2uthEntity"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2uthTimeStamp"),
)
if mibBuilder.loadTexts:
    sc2UtilizationHistory.setStatus("mandatory")
_Sc2uthUnitId_Type = Integer32
_Sc2uthUnitId_Object = MibTableColumn
sc2uthUnitId = _Sc2uthUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 6, 1, 1),
    _Sc2uthUnitId_Type()
)
sc2uthUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2uthUnitId.setStatus("mandatory")


class _Sc2uthEntity_Type(Integer32):
    """Custom type sc2uthEntity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("powerConsumptionDay", 1),
          ("powerConsumptionMonth", 2),
          ("powerConsumptionYear", 3))
    )


_Sc2uthEntity_Type.__name__ = "Integer32"
_Sc2uthEntity_Object = MibTableColumn
sc2uthEntity = _Sc2uthEntity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 6, 1, 2),
    _Sc2uthEntity_Type()
)
sc2uthEntity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2uthEntity.setStatus("mandatory")
_Sc2uthTimeStamp_Type = Integer32
_Sc2uthTimeStamp_Object = MibTableColumn
sc2uthTimeStamp = _Sc2uthTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 6, 1, 3),
    _Sc2uthTimeStamp_Type()
)
sc2uthTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2uthTimeStamp.setStatus("mandatory")
_Sc2uthHardwareUUID_Type = DisplayString
_Sc2uthHardwareUUID_Object = MibTableColumn
sc2uthHardwareUUID = _Sc2uthHardwareUUID_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 6, 1, 4),
    _Sc2uthHardwareUUID_Type()
)
sc2uthHardwareUUID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2uthHardwareUUID.setStatus("mandatory")
_Sc2uthAverageValue_Type = Gauge32
_Sc2uthAverageValue_Object = MibTableColumn
sc2uthAverageValue = _Sc2uthAverageValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 6, 1, 5),
    _Sc2uthAverageValue_Type()
)
sc2uthAverageValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2uthAverageValue.setStatus("mandatory")
_Sc2uthMinValue_Type = Gauge32
_Sc2uthMinValue_Object = MibTableColumn
sc2uthMinValue = _Sc2uthMinValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 6, 1, 6),
    _Sc2uthMinValue_Type()
)
sc2uthMinValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2uthMinValue.setStatus("mandatory")
_Sc2uthMaxValue_Type = Gauge32
_Sc2uthMaxValue_Object = MibTableColumn
sc2uthMaxValue = _Sc2uthMaxValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 6, 1, 7),
    _Sc2uthMaxValue_Type()
)
sc2uthMaxValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2uthMaxValue.setStatus("mandatory")
_Sc2PowerSourceInformationTable_Object = MibTable
sc2PowerSourceInformationTable = _Sc2PowerSourceInformationTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 7)
)
if mibBuilder.loadTexts:
    sc2PowerSourceInformationTable.setStatus("mandatory")
_Sc2PowerSourceInformation_Object = MibTableRow
sc2PowerSourceInformation = _Sc2PowerSourceInformation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 7, 1)
)
sc2PowerSourceInformation.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2psiUnitId"),
)
if mibBuilder.loadTexts:
    sc2PowerSourceInformation.setStatus("mandatory")
_Sc2psiUnitId_Type = Integer32
_Sc2psiUnitId_Object = MibTableColumn
sc2psiUnitId = _Sc2psiUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 7, 1, 1),
    _Sc2psiUnitId_Type()
)
sc2psiUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2psiUnitId.setStatus("mandatory")
_Sc2psiPowerSourceType_Type = DisplayString
_Sc2psiPowerSourceType_Object = MibTableColumn
sc2psiPowerSourceType = _Sc2psiPowerSourceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 7, 1, 2),
    _Sc2psiPowerSourceType_Type()
)
sc2psiPowerSourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2psiPowerSourceType.setStatus("mandatory")


class _Sc2psiPowerSourcePhase_Type(Integer32):
    """Custom type sc2psiPowerSourcePhase based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("single-phase", 2),
          ("three-phase", 3))
    )


_Sc2psiPowerSourcePhase_Type.__name__ = "Integer32"
_Sc2psiPowerSourcePhase_Object = MibTableColumn
sc2psiPowerSourcePhase = _Sc2psiPowerSourcePhase_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 7, 1, 3),
    _Sc2psiPowerSourcePhase_Type()
)
sc2psiPowerSourcePhase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2psiPowerSourcePhase.setStatus("mandatory")
_Sc2psiPowerSourceVoltage_Type = Integer32
_Sc2psiPowerSourceVoltage_Object = MibTableColumn
sc2psiPowerSourceVoltage = _Sc2psiPowerSourceVoltage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 7, 1, 4),
    _Sc2psiPowerSourceVoltage_Type()
)
sc2psiPowerSourceVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2psiPowerSourceVoltage.setStatus("mandatory")
_Sc2VirtualIoManagerTable_Object = MibTable
sc2VirtualIoManagerTable = _Sc2VirtualIoManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 8)
)
if mibBuilder.loadTexts:
    sc2VirtualIoManagerTable.setStatus("mandatory")
_Sc2VirtualIoManager_Object = MibTableRow
sc2VirtualIoManager = _Sc2VirtualIoManager_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 8, 1)
)
sc2VirtualIoManager.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2viomUnitId"),
)
if mibBuilder.loadTexts:
    sc2VirtualIoManager.setStatus("mandatory")
_Sc2viomUnitId_Type = Integer32
_Sc2viomUnitId_Object = MibTableColumn
sc2viomUnitId = _Sc2viomUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 8, 1, 1),
    _Sc2viomUnitId_Type()
)
sc2viomUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2viomUnitId.setStatus("mandatory")
_Sc2viomCurrentManagerId_Type = DisplayString
_Sc2viomCurrentManagerId_Object = MibTableColumn
sc2viomCurrentManagerId = _Sc2viomCurrentManagerId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 8, 1, 2),
    _Sc2viomCurrentManagerId_Type()
)
sc2viomCurrentManagerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2viomCurrentManagerId.setStatus("mandatory")
_Sc2viomEnabled_Type = TrueFalseUnknown
_Sc2viomEnabled_Object = MibTableColumn
sc2viomEnabled = _Sc2viomEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 8, 1, 3),
    _Sc2viomEnabled_Type()
)
sc2viomEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2viomEnabled.setStatus("mandatory")
_Sc2viomBiosSupport_Type = TrueFalseUnknown
_Sc2viomBiosSupport_Object = MibTableColumn
sc2viomBiosSupport = _Sc2viomBiosSupport_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 8, 1, 4),
    _Sc2viomBiosSupport_Type()
)
sc2viomBiosSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2viomBiosSupport.setStatus("mandatory")
_Sc2viomConnectionStatus_Type = Integer32
_Sc2viomConnectionStatus_Object = MibTableColumn
sc2viomConnectionStatus = _Sc2viomConnectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 8, 1, 5),
    _Sc2viomConnectionStatus_Type()
)
sc2viomConnectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2viomConnectionStatus.setStatus("mandatory")
_Sc2PowerSupplyRedundancyConfigurationTable_Object = MibTable
sc2PowerSupplyRedundancyConfigurationTable = _Sc2PowerSupplyRedundancyConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9)
)
if mibBuilder.loadTexts:
    sc2PowerSupplyRedundancyConfigurationTable.setStatus("mandatory")
_Sc2PowerSupplyRedundancyConfiguration_Object = MibTableRow
sc2PowerSupplyRedundancyConfiguration = _Sc2PowerSupplyRedundancyConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9, 1)
)
sc2PowerSupplyRedundancyConfiguration.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2PSRedUnitId"),
)
if mibBuilder.loadTexts:
    sc2PowerSupplyRedundancyConfiguration.setStatus("mandatory")
_Sc2PSRedUnitId_Type = Integer32
_Sc2PSRedUnitId_Object = MibTableColumn
sc2PSRedUnitId = _Sc2PSRedUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9, 1, 1),
    _Sc2PSRedUnitId_Type()
)
sc2PSRedUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PSRedUnitId.setStatus("mandatory")


class _Sc2PSRedundancyMode_Type(Integer32):
    """Custom type sc2PSRedundancyMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              18,
              34)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("not-specified", 2),
          ("no-redundancy", 3),
          ("psu-redundancy", 4),
          ("dual-ac-redundancy", 18),
          ("triple-ac-redundancy", 34))
    )


_Sc2PSRedundancyMode_Type.__name__ = "Integer32"
_Sc2PSRedundancyMode_Object = MibTableColumn
sc2PSRedundancyMode = _Sc2PSRedundancyMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9, 1, 2),
    _Sc2PSRedundancyMode_Type()
)
sc2PSRedundancyMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PSRedundancyMode.setStatus("mandatory")


class _Sc2PSRedundancyModeConfig_Type(Integer32):
    """Custom type sc2PSRedundancyModeConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              19,
              35,
              36,
              51)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("no-redundancy", 2),
          ("redundancy-1-1", 19),
          ("redundancy-2-1", 35),
          ("redundancy-2-2", 36),
          ("redundancy-3-1", 51))
    )


_Sc2PSRedundancyModeConfig_Type.__name__ = "Integer32"
_Sc2PSRedundancyModeConfig_Object = MibTableColumn
sc2PSRedundancyModeConfig = _Sc2PSRedundancyModeConfig_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9, 1, 3),
    _Sc2PSRedundancyModeConfig_Type()
)
sc2PSRedundancyModeConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PSRedundancyModeConfig.setStatus("mandatory")
_Sc2PSRedundancyRequiredPowerSupplies_Type = Integer32
_Sc2PSRedundancyRequiredPowerSupplies_Object = MibTableColumn
sc2PSRedundancyRequiredPowerSupplies = _Sc2PSRedundancyRequiredPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9, 1, 4),
    _Sc2PSRedundancyRequiredPowerSupplies_Type()
)
sc2PSRedundancyRequiredPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PSRedundancyRequiredPowerSupplies.setStatus("mandatory")
_Sc2PSRedundancyPopulatedPowerSupplies_Type = Integer32
_Sc2PSRedundancyPopulatedPowerSupplies_Object = MibTableColumn
sc2PSRedundancyPopulatedPowerSupplies = _Sc2PSRedundancyPopulatedPowerSupplies_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9, 1, 5),
    _Sc2PSRedundancyPopulatedPowerSupplies_Type()
)
sc2PSRedundancyPopulatedPowerSupplies.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PSRedundancyPopulatedPowerSupplies.setStatus("mandatory")
_Sc2PSRedundancyConfigurationStatus_Type = CompStatus
_Sc2PSRedundancyConfigurationStatus_Object = MibTableColumn
sc2PSRedundancyConfigurationStatus = _Sc2PSRedundancyConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9, 1, 6),
    _Sc2PSRedundancyConfigurationStatus_Type()
)
sc2PSRedundancyConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PSRedundancyConfigurationStatus.setStatus("mandatory")
_Sc2PSRedundancyThresholdStatus_Type = CompStatus
_Sc2PSRedundancyThresholdStatus_Object = MibTableColumn
sc2PSRedundancyThresholdStatus = _Sc2PSRedundancyThresholdStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9, 1, 7),
    _Sc2PSRedundancyThresholdStatus_Type()
)
sc2PSRedundancyThresholdStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PSRedundancyThresholdStatus.setStatus("mandatory")


class _Sc2PSRedundancyStatus_Type(Integer32):
    """Custom type sc2PSRedundancyStatus based on Integer32"""
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
        *(("unknown", 1),
          ("not-available", 2),
          ("ok", 3),
          ("warning", 4),
          ("error", 5))
    )


_Sc2PSRedundancyStatus_Type.__name__ = "Integer32"
_Sc2PSRedundancyStatus_Object = MibTableColumn
sc2PSRedundancyStatus = _Sc2PSRedundancyStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 9, 1, 8),
    _Sc2PSRedundancyStatus_Type()
)
sc2PSRedundancyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PSRedundancyStatus.setStatus("mandatory")
_Sc2PerformanceValueTable_Object = MibTable
sc2PerformanceValueTable = _Sc2PerformanceValueTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 10)
)
if mibBuilder.loadTexts:
    sc2PerformanceValueTable.setStatus("mandatory")
_Sc2PerformanceValues_Object = MibTableRow
sc2PerformanceValues = _Sc2PerformanceValues_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 10, 1)
)
sc2PerformanceValues.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2PerfValUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2PerfValType"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2PerfValObjectNr"),
)
if mibBuilder.loadTexts:
    sc2PerformanceValues.setStatus("mandatory")
_Sc2PerfValUnitId_Type = Integer32
_Sc2PerfValUnitId_Object = MibTableColumn
sc2PerfValUnitId = _Sc2PerfValUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 10, 1, 1),
    _Sc2PerfValUnitId_Type()
)
sc2PerfValUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PerfValUnitId.setStatus("mandatory")


class _Sc2PerfValType_Type(Integer32):
    """Custom type sc2PerfValType based on Integer32"""
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
        *(("physicalMemoryUsageMb", 1),
          ("physicalMemoryUsagePercent", 2),
          ("totalMemoryUsageMb", 3),
          ("totalMemoryUsagePercent", 4),
          ("overallCpuUsagePercent", 5),
          ("logicalCpuUsagePercent", 6))
    )


_Sc2PerfValType_Type.__name__ = "Integer32"
_Sc2PerfValType_Object = MibTableColumn
sc2PerfValType = _Sc2PerfValType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 10, 1, 2),
    _Sc2PerfValType_Type()
)
sc2PerfValType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PerfValType.setStatus("mandatory")
_Sc2PerfValObjectNr_Type = Integer32
_Sc2PerfValObjectNr_Object = MibTableColumn
sc2PerfValObjectNr = _Sc2PerfValObjectNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 10, 1, 3),
    _Sc2PerfValObjectNr_Type()
)
sc2PerfValObjectNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PerfValObjectNr.setStatus("mandatory")
_Sc2PerfValName_Type = DisplayString
_Sc2PerfValName_Object = MibTableColumn
sc2PerfValName = _Sc2PerfValName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 10, 1, 4),
    _Sc2PerfValName_Type()
)
sc2PerfValName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PerfValName.setStatus("mandatory")
_Sc2PerfValCurrentValue_Type = Gauge32
_Sc2PerfValCurrentValue_Object = MibTableColumn
sc2PerfValCurrentValue = _Sc2PerfValCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 4, 10, 1, 5),
    _Sc2PerfValCurrentValue_Type()
)
sc2PerfValCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PerfValCurrentValue.setStatus("mandatory")
_Sc2Environment_ObjectIdentity = ObjectIdentity
sc2Environment = _Sc2Environment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5)
)
_Sc2TemperatureSensorTable_Object = MibTable
sc2TemperatureSensorTable = _Sc2TemperatureSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1)
)
if mibBuilder.loadTexts:
    sc2TemperatureSensorTable.setStatus("mandatory")
_Sc2TemperatureSensors_Object = MibTableRow
sc2TemperatureSensors = _Sc2TemperatureSensors_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1)
)
sc2TemperatureSensors.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2tempUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2tempSensorNr"),
)
if mibBuilder.loadTexts:
    sc2TemperatureSensors.setStatus("mandatory")
_Sc2tempUnitId_Type = Integer32
_Sc2tempUnitId_Object = MibTableColumn
sc2tempUnitId = _Sc2tempUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1, 1),
    _Sc2tempUnitId_Type()
)
sc2tempUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tempUnitId.setStatus("mandatory")
_Sc2tempSensorNr_Type = Integer32
_Sc2tempSensorNr_Object = MibTableColumn
sc2tempSensorNr = _Sc2tempSensorNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1, 2),
    _Sc2tempSensorNr_Type()
)
sc2tempSensorNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tempSensorNr.setStatus("mandatory")
_Sc2tempSensorDesignation_Type = DisplayString
_Sc2tempSensorDesignation_Object = MibTableColumn
sc2tempSensorDesignation = _Sc2tempSensorDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1, 3),
    _Sc2tempSensorDesignation_Type()
)
sc2tempSensorDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tempSensorDesignation.setStatus("mandatory")
_Sc2tempSensorIdentifier_Type = DisplayString
_Sc2tempSensorIdentifier_Object = MibTableColumn
sc2tempSensorIdentifier = _Sc2tempSensorIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1, 4),
    _Sc2tempSensorIdentifier_Type()
)
sc2tempSensorIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tempSensorIdentifier.setStatus("mandatory")


class _Sc2tempSensorStatus_Type(Integer32):
    """Custom type sc2tempSensorStatus based on Integer32"""
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
        *(("unknown", 1),
          ("not-available", 2),
          ("ok", 3),
          ("sensor-failed", 4),
          ("failed", 5),
          ("temperature-warning-toohot", 6),
          ("temperature-critical-toohot", 7),
          ("temperature-normal", 8),
          ("temperature-warning", 9))
    )


_Sc2tempSensorStatus_Type.__name__ = "Integer32"
_Sc2tempSensorStatus_Object = MibTableColumn
sc2tempSensorStatus = _Sc2tempSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1, 5),
    _Sc2tempSensorStatus_Type()
)
sc2tempSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tempSensorStatus.setStatus("mandatory")
_Sc2tempCurrentTemperature_Type = Gauge32
_Sc2tempCurrentTemperature_Object = MibTableColumn
sc2tempCurrentTemperature = _Sc2tempCurrentTemperature_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1, 6),
    _Sc2tempCurrentTemperature_Type()
)
sc2tempCurrentTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tempCurrentTemperature.setStatus("mandatory")
_Sc2tempWarningLevel_Type = Integer32
_Sc2tempWarningLevel_Object = MibTableColumn
sc2tempWarningLevel = _Sc2tempWarningLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1, 7),
    _Sc2tempWarningLevel_Type()
)
sc2tempWarningLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tempWarningLevel.setStatus("mandatory")
_Sc2tempCriticalLevel_Type = Integer32
_Sc2tempCriticalLevel_Object = MibTableColumn
sc2tempCriticalLevel = _Sc2tempCriticalLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1, 8),
    _Sc2tempCriticalLevel_Type()
)
sc2tempCriticalLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tempCriticalLevel.setStatus("mandatory")


class _Sc2tempCriticalReaction_Type(Integer32):
    """Custom type sc2tempCriticalReaction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("continue", 2),
          ("shutdown-and-poweroff", 3))
    )


_Sc2tempCriticalReaction_Type.__name__ = "Integer32"
_Sc2tempCriticalReaction_Object = MibTableColumn
sc2tempCriticalReaction = _Sc2tempCriticalReaction_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 1, 1, 9),
    _Sc2tempCriticalReaction_Type()
)
sc2tempCriticalReaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2tempCriticalReaction.setStatus("mandatory")
_Sc2FanTable_Object = MibTable
sc2FanTable = _Sc2FanTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2)
)
if mibBuilder.loadTexts:
    sc2FanTable.setStatus("mandatory")
_Sc2Fans_Object = MibTableRow
sc2Fans = _Sc2Fans_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1)
)
sc2Fans.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2fanUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2fanNr"),
)
if mibBuilder.loadTexts:
    sc2Fans.setStatus("mandatory")
_Sc2fanUnitId_Type = Integer32
_Sc2fanUnitId_Object = MibTableColumn
sc2fanUnitId = _Sc2fanUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 1),
    _Sc2fanUnitId_Type()
)
sc2fanUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fanUnitId.setStatus("mandatory")
_Sc2fanNr_Type = Integer32
_Sc2fanNr_Object = MibTableColumn
sc2fanNr = _Sc2fanNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 2),
    _Sc2fanNr_Type()
)
sc2fanNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fanNr.setStatus("mandatory")
_Sc2fanDesignation_Type = DisplayString
_Sc2fanDesignation_Object = MibTableColumn
sc2fanDesignation = _Sc2fanDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 3),
    _Sc2fanDesignation_Type()
)
sc2fanDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fanDesignation.setStatus("mandatory")
_Sc2fanIdentifier_Type = DisplayString
_Sc2fanIdentifier_Object = MibTableColumn
sc2fanIdentifier = _Sc2fanIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 4),
    _Sc2fanIdentifier_Type()
)
sc2fanIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fanIdentifier.setStatus("mandatory")


class _Sc2fanStatus_Type(Integer32):
    """Custom type sc2fanStatus based on Integer32"""
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
        *(("unknown", 1),
          ("disabled", 2),
          ("ok", 3),
          ("failed", 4),
          ("prefailure-predicted", 5),
          ("redundant-fan-failed", 6),
          ("not-manageable", 7),
          ("not-present", 8))
    )


_Sc2fanStatus_Type.__name__ = "Integer32"
_Sc2fanStatus_Object = MibTableColumn
sc2fanStatus = _Sc2fanStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 5),
    _Sc2fanStatus_Type()
)
sc2fanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fanStatus.setStatus("mandatory")
_Sc2fanCurrentSpeed_Type = Gauge32
_Sc2fanCurrentSpeed_Object = MibTableColumn
sc2fanCurrentSpeed = _Sc2fanCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 6),
    _Sc2fanCurrentSpeed_Type()
)
sc2fanCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fanCurrentSpeed.setStatus("mandatory")
_Sc2fanQuality_Type = Gauge32
_Sc2fanQuality_Object = MibTableColumn
sc2fanQuality = _Sc2fanQuality_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 7),
    _Sc2fanQuality_Type()
)
sc2fanQuality.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fanQuality.setStatus("mandatory")


class _Sc2fanFailReaction_Type(Integer32):
    """Custom type sc2fanFailReaction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("continue", 2),
          ("shutdown-and-poweroff", 3))
    )


_Sc2fanFailReaction_Type.__name__ = "Integer32"
_Sc2fanFailReaction_Object = MibTableColumn
sc2fanFailReaction = _Sc2fanFailReaction_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 8),
    _Sc2fanFailReaction_Type()
)
sc2fanFailReaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2fanFailReaction.setStatus("mandatory")
_Sc2fanFailShutdownDelay_Type = Integer32
_Sc2fanFailShutdownDelay_Object = MibTableColumn
sc2fanFailShutdownDelay = _Sc2fanFailShutdownDelay_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 9),
    _Sc2fanFailShutdownDelay_Type()
)
sc2fanFailShutdownDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2fanFailShutdownDelay.setStatus("mandatory")


class _Sc2fanCoolingDeviceType_Type(Integer32):
    """Custom type sc2fanCoolingDeviceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("fan", 2),
          ("liquid", 3))
    )


_Sc2fanCoolingDeviceType_Type.__name__ = "Integer32"
_Sc2fanCoolingDeviceType_Object = MibTableColumn
sc2fanCoolingDeviceType = _Sc2fanCoolingDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 2, 1, 10),
    _Sc2fanCoolingDeviceType_Type()
)
sc2fanCoolingDeviceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fanCoolingDeviceType.setStatus("mandatory")
_Sc2AirflowTable_Object = MibTable
sc2AirflowTable = _Sc2AirflowTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 3)
)
if mibBuilder.loadTexts:
    sc2AirflowTable.setStatus("mandatory")
_Sc2Airflow_Object = MibTableRow
sc2Airflow = _Sc2Airflow_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 3, 1)
)
sc2Airflow.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2afUnitId"),
)
if mibBuilder.loadTexts:
    sc2Airflow.setStatus("mandatory")
_Sc2afUnitId_Type = Integer32
_Sc2afUnitId_Object = MibTableColumn
sc2afUnitId = _Sc2afUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 3, 1, 1),
    _Sc2afUnitId_Type()
)
sc2afUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2afUnitId.setStatus("mandatory")
_Sc2afExhaustAirflowVolume_Type = Integer32
_Sc2afExhaustAirflowVolume_Object = MibTableColumn
sc2afExhaustAirflowVolume = _Sc2afExhaustAirflowVolume_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 3, 1, 2),
    _Sc2afExhaustAirflowVolume_Type()
)
sc2afExhaustAirflowVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2afExhaustAirflowVolume.setStatus("mandatory")
_Sc2afExhaustAirflowVolumeUnit_Type = DisplayString
_Sc2afExhaustAirflowVolumeUnit_Object = MibTableColumn
sc2afExhaustAirflowVolumeUnit = _Sc2afExhaustAirflowVolumeUnit_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 5, 3, 1, 3),
    _Sc2afExhaustAirflowVolumeUnit_Type()
)
sc2afExhaustAirflowVolumeUnit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2afExhaustAirflowVolumeUnit.setStatus("mandatory")
_Sc2Hardware_ObjectIdentity = ObjectIdentity
sc2Hardware = _Sc2Hardware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6)
)
_Sc2SystemBoardTable_Object = MibTable
sc2SystemBoardTable = _Sc2SystemBoardTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1)
)
if mibBuilder.loadTexts:
    sc2SystemBoardTable.setStatus("mandatory")
_Sc2SystemBoard_Object = MibTableRow
sc2SystemBoard = _Sc2SystemBoard_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1, 1)
)
sc2SystemBoard.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2sbUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2sbBoardNr"),
)
if mibBuilder.loadTexts:
    sc2SystemBoard.setStatus("mandatory")
_Sc2sbUnitId_Type = Integer32
_Sc2sbUnitId_Object = MibTableColumn
sc2sbUnitId = _Sc2sbUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1, 1, 1),
    _Sc2sbUnitId_Type()
)
sc2sbUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2sbUnitId.setStatus("mandatory")
_Sc2sbBoardNr_Type = Integer32
_Sc2sbBoardNr_Object = MibTableColumn
sc2sbBoardNr = _Sc2sbBoardNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1, 1, 2),
    _Sc2sbBoardNr_Type()
)
sc2sbBoardNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2sbBoardNr.setStatus("mandatory")
_Sc2SystemBoardModelName_Type = DisplayString
_Sc2SystemBoardModelName_Object = MibTableColumn
sc2SystemBoardModelName = _Sc2SystemBoardModelName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1, 1, 3),
    _Sc2SystemBoardModelName_Type()
)
sc2SystemBoardModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2SystemBoardModelName.setStatus("mandatory")
_Sc2SystemBoardProductNumber_Type = DisplayString
_Sc2SystemBoardProductNumber_Object = MibTableColumn
sc2SystemBoardProductNumber = _Sc2SystemBoardProductNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1, 1, 4),
    _Sc2SystemBoardProductNumber_Type()
)
sc2SystemBoardProductNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2SystemBoardProductNumber.setStatus("mandatory")
_Sc2SystemBoardRevision_Type = DisplayString
_Sc2SystemBoardRevision_Object = MibTableColumn
sc2SystemBoardRevision = _Sc2SystemBoardRevision_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1, 1, 5),
    _Sc2SystemBoardRevision_Type()
)
sc2SystemBoardRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2SystemBoardRevision.setStatus("mandatory")
_Sc2SystemBoardSerialNumber_Type = DisplayString
_Sc2SystemBoardSerialNumber_Object = MibTableColumn
sc2SystemBoardSerialNumber = _Sc2SystemBoardSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1, 1, 6),
    _Sc2SystemBoardSerialNumber_Type()
)
sc2SystemBoardSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2SystemBoardSerialNumber.setStatus("mandatory")
_Sc2SystemBoardDesignation_Type = DisplayString
_Sc2SystemBoardDesignation_Object = MibTableColumn
sc2SystemBoardDesignation = _Sc2SystemBoardDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1, 1, 7),
    _Sc2SystemBoardDesignation_Type()
)
sc2SystemBoardDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2SystemBoardDesignation.setStatus("mandatory")
_Sc2SystemBoardSDCardSlotPresent_Type = TrueFalseUnknown
_Sc2SystemBoardSDCardSlotPresent_Object = MibTableColumn
sc2SystemBoardSDCardSlotPresent = _Sc2SystemBoardSDCardSlotPresent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 1, 1, 8),
    _Sc2SystemBoardSDCardSlotPresent_Type()
)
sc2SystemBoardSDCardSlotPresent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2SystemBoardSDCardSlotPresent.setStatus("mandatory")
_Sc2PowerSupplyTable_Object = MibTable
sc2PowerSupplyTable = _Sc2PowerSupplyTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 2)
)
if mibBuilder.loadTexts:
    sc2PowerSupplyTable.setStatus("mandatory")
_Sc2PowerSupply_Object = MibTableRow
sc2PowerSupply = _Sc2PowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 2, 1)
)
sc2PowerSupply.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2psUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2psPowerSupplyNr"),
)
if mibBuilder.loadTexts:
    sc2PowerSupply.setStatus("mandatory")
_Sc2psUnitId_Type = Integer32
_Sc2psUnitId_Object = MibTableColumn
sc2psUnitId = _Sc2psUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 2, 1, 1),
    _Sc2psUnitId_Type()
)
sc2psUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2psUnitId.setStatus("mandatory")
_Sc2psPowerSupplyNr_Type = Integer32
_Sc2psPowerSupplyNr_Object = MibTableColumn
sc2psPowerSupplyNr = _Sc2psPowerSupplyNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 2, 1, 2),
    _Sc2psPowerSupplyNr_Type()
)
sc2psPowerSupplyNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2psPowerSupplyNr.setStatus("mandatory")
_Sc2PowerSupplyDesignation_Type = DisplayString
_Sc2PowerSupplyDesignation_Object = MibTableColumn
sc2PowerSupplyDesignation = _Sc2PowerSupplyDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 2, 1, 3),
    _Sc2PowerSupplyDesignation_Type()
)
sc2PowerSupplyDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerSupplyDesignation.setStatus("mandatory")
_Sc2PowerSupplyIdentifier_Type = DisplayString
_Sc2PowerSupplyIdentifier_Object = MibTableColumn
sc2PowerSupplyIdentifier = _Sc2PowerSupplyIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 2, 1, 4),
    _Sc2PowerSupplyIdentifier_Type()
)
sc2PowerSupplyIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerSupplyIdentifier.setStatus("mandatory")


class _Sc2PowerSupplyStatus_Type(Integer32):
    """Custom type sc2PowerSupplyStatus based on Integer32"""
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("not-present", 2),
          ("ok", 3),
          ("failed", 4),
          ("ac-fail", 5),
          ("dc-fail", 6),
          ("critical-temperature", 7),
          ("not-manageable", 8),
          ("fan-failure-predicted", 9),
          ("fan-failure", 10),
          ("power-safe-mode", 11),
          ("non-redundant-dc-fail", 12),
          ("non-redundant-ac-fail", 13))
    )


_Sc2PowerSupplyStatus_Type.__name__ = "Integer32"
_Sc2PowerSupplyStatus_Object = MibTableColumn
sc2PowerSupplyStatus = _Sc2PowerSupplyStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 2, 1, 5),
    _Sc2PowerSupplyStatus_Type()
)
sc2PowerSupplyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2PowerSupplyStatus.setStatus("mandatory")
_Sc2psPowerSupplyLoad_Type = Integer32
_Sc2psPowerSupplyLoad_Object = MibTableColumn
sc2psPowerSupplyLoad = _Sc2psPowerSupplyLoad_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 2, 1, 6),
    _Sc2psPowerSupplyLoad_Type()
)
sc2psPowerSupplyLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2psPowerSupplyLoad.setStatus("mandatory")
_Sc2psPowerSupplyNominal_Type = Integer32
_Sc2psPowerSupplyNominal_Object = MibTableColumn
sc2psPowerSupplyNominal = _Sc2psPowerSupplyNominal_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 2, 1, 7),
    _Sc2psPowerSupplyNominal_Type()
)
sc2psPowerSupplyNominal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2psPowerSupplyNominal.setStatus("mandatory")
_Sc2VoltageTable_Object = MibTable
sc2VoltageTable = _Sc2VoltageTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3)
)
if mibBuilder.loadTexts:
    sc2VoltageTable.setStatus("mandatory")
_Sc2Voltages_Object = MibTableRow
sc2Voltages = _Sc2Voltages_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1)
)
sc2Voltages.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2voUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2voSensorNr"),
)
if mibBuilder.loadTexts:
    sc2Voltages.setStatus("mandatory")
_Sc2voUnitId_Type = Integer32
_Sc2voUnitId_Object = MibTableColumn
sc2voUnitId = _Sc2voUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1, 1),
    _Sc2voUnitId_Type()
)
sc2voUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2voUnitId.setStatus("mandatory")
_Sc2voSensorNr_Type = Integer32
_Sc2voSensorNr_Object = MibTableColumn
sc2voSensorNr = _Sc2voSensorNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1, 2),
    _Sc2voSensorNr_Type()
)
sc2voSensorNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2voSensorNr.setStatus("mandatory")
_Sc2VoltageDesignation_Type = DisplayString
_Sc2VoltageDesignation_Object = MibTableColumn
sc2VoltageDesignation = _Sc2VoltageDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1, 3),
    _Sc2VoltageDesignation_Type()
)
sc2VoltageDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2VoltageDesignation.setStatus("mandatory")


class _Sc2VoltageStatus_Type(Integer32):
    """Custom type sc2VoltageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("not-available", 2),
          ("ok", 3),
          ("too-low", 4),
          ("too-high", 5),
          ("out-of-range", 6),
          ("warning", 7))
    )


_Sc2VoltageStatus_Type.__name__ = "Integer32"
_Sc2VoltageStatus_Object = MibTableColumn
sc2VoltageStatus = _Sc2VoltageStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1, 4),
    _Sc2VoltageStatus_Type()
)
sc2VoltageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2VoltageStatus.setStatus("mandatory")
_Sc2VoltageCurrentValue_Type = Gauge32
_Sc2VoltageCurrentValue_Object = MibTableColumn
sc2VoltageCurrentValue = _Sc2VoltageCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1, 5),
    _Sc2VoltageCurrentValue_Type()
)
sc2VoltageCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2VoltageCurrentValue.setStatus("mandatory")
_Sc2VoltageNominalValue_Type = Integer32
_Sc2VoltageNominalValue_Object = MibTableColumn
sc2VoltageNominalValue = _Sc2VoltageNominalValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1, 6),
    _Sc2VoltageNominalValue_Type()
)
sc2VoltageNominalValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2VoltageNominalValue.setStatus("mandatory")
_Sc2VoltageMinimumLevel_Type = Integer32
_Sc2VoltageMinimumLevel_Object = MibTableColumn
sc2VoltageMinimumLevel = _Sc2VoltageMinimumLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1, 7),
    _Sc2VoltageMinimumLevel_Type()
)
sc2VoltageMinimumLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2VoltageMinimumLevel.setStatus("mandatory")
_Sc2VoltageMaximumLevel_Type = Integer32
_Sc2VoltageMaximumLevel_Object = MibTableColumn
sc2VoltageMaximumLevel = _Sc2VoltageMaximumLevel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1, 8),
    _Sc2VoltageMaximumLevel_Type()
)
sc2VoltageMaximumLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2VoltageMaximumLevel.setStatus("mandatory")
_Sc2VoltageCurrentLoad_Type = Gauge32
_Sc2VoltageCurrentLoad_Object = MibTableColumn
sc2VoltageCurrentLoad = _Sc2VoltageCurrentLoad_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 3, 1, 9),
    _Sc2VoltageCurrentLoad_Type()
)
sc2VoltageCurrentLoad.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2VoltageCurrentLoad.setStatus("mandatory")
_Sc2CPUTable_Object = MibTable
sc2CPUTable = _Sc2CPUTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4)
)
if mibBuilder.loadTexts:
    sc2CPUTable.setStatus("mandatory")
_Sc2CPUs_Object = MibTableRow
sc2CPUs = _Sc2CPUs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1)
)
sc2CPUs.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2cpuUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2cpuNr"),
)
if mibBuilder.loadTexts:
    sc2CPUs.setStatus("mandatory")
_Sc2cpuUnitId_Type = Integer32
_Sc2cpuUnitId_Object = MibTableColumn
sc2cpuUnitId = _Sc2cpuUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 1),
    _Sc2cpuUnitId_Type()
)
sc2cpuUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuUnitId.setStatus("mandatory")
_Sc2cpuNr_Type = Integer32
_Sc2cpuNr_Object = MibTableColumn
sc2cpuNr = _Sc2cpuNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 2),
    _Sc2cpuNr_Type()
)
sc2cpuNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuNr.setStatus("mandatory")
_Sc2cpuDesignation_Type = DisplayString
_Sc2cpuDesignation_Object = MibTableColumn
sc2cpuDesignation = _Sc2cpuDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 3),
    _Sc2cpuDesignation_Type()
)
sc2cpuDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuDesignation.setStatus("mandatory")


class _Sc2cpuStatus_Type(Integer32):
    """Custom type sc2cpuStatus based on Integer32"""
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
        *(("unknown", 1),
          ("not-present", 2),
          ("ok", 3),
          ("disabled", 4),
          ("error", 5),
          ("failed", 6),
          ("missing-termination", 7),
          ("prefailure-warning", 8))
    )


_Sc2cpuStatus_Type.__name__ = "Integer32"
_Sc2cpuStatus_Object = MibTableColumn
sc2cpuStatus = _Sc2cpuStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 4),
    _Sc2cpuStatus_Type()
)
sc2cpuStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuStatus.setStatus("mandatory")
_Sc2cpuModelName_Type = DisplayString
_Sc2cpuModelName_Object = MibTableColumn
sc2cpuModelName = _Sc2cpuModelName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 5),
    _Sc2cpuModelName_Type()
)
sc2cpuModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuModelName.setStatus("mandatory")
_Sc2cpuManufacturer_Type = DisplayString
_Sc2cpuManufacturer_Object = MibTableColumn
sc2cpuManufacturer = _Sc2cpuManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 6),
    _Sc2cpuManufacturer_Type()
)
sc2cpuManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuManufacturer.setStatus("mandatory")
_Sc2cpuStep_Type = DisplayString
_Sc2cpuStep_Object = MibTableColumn
sc2cpuStep = _Sc2cpuStep_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 7),
    _Sc2cpuStep_Type()
)
sc2cpuStep.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuStep.setStatus("mandatory")
_Sc2cpuCurrentSpeed_Type = Integer32
_Sc2cpuCurrentSpeed_Object = MibTableColumn
sc2cpuCurrentSpeed = _Sc2cpuCurrentSpeed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 8),
    _Sc2cpuCurrentSpeed_Type()
)
sc2cpuCurrentSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuCurrentSpeed.setStatus("mandatory")
_Sc2cpuNumberLogicals_Type = Integer32
_Sc2cpuNumberLogicals_Object = MibTableColumn
sc2cpuNumberLogicals = _Sc2cpuNumberLogicals_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 9),
    _Sc2cpuNumberLogicals_Type()
)
sc2cpuNumberLogicals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuNumberLogicals.setStatus("mandatory")
_Sc2cpuCacheL1Size_Type = Integer32
_Sc2cpuCacheL1Size_Object = MibTableColumn
sc2cpuCacheL1Size = _Sc2cpuCacheL1Size_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 10),
    _Sc2cpuCacheL1Size_Type()
)
sc2cpuCacheL1Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuCacheL1Size.setStatus("mandatory")
_Sc2cpuCacheL2Size_Type = Integer32
_Sc2cpuCacheL2Size_Object = MibTableColumn
sc2cpuCacheL2Size = _Sc2cpuCacheL2Size_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 11),
    _Sc2cpuCacheL2Size_Type()
)
sc2cpuCacheL2Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuCacheL2Size.setStatus("mandatory")
_Sc2cpuCacheL3Size_Type = Integer32
_Sc2cpuCacheL3Size_Object = MibTableColumn
sc2cpuCacheL3Size = _Sc2cpuCacheL3Size_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 12),
    _Sc2cpuCacheL3Size_Type()
)
sc2cpuCacheL3Size.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuCacheL3Size.setStatus("mandatory")
_Sc2cpuNumberCores_Type = Integer32
_Sc2cpuNumberCores_Object = MibTableColumn
sc2cpuNumberCores = _Sc2cpuNumberCores_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 13),
    _Sc2cpuNumberCores_Type()
)
sc2cpuNumberCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuNumberCores.setStatus("mandatory")
_Sc2cpuFamily_Type = Integer32
_Sc2cpuFamily_Object = MibTableColumn
sc2cpuFamily = _Sc2cpuFamily_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 14),
    _Sc2cpuFamily_Type()
)
sc2cpuFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuFamily.setStatus("mandatory")
_Sc2cpuEnabledCores_Type = Integer32
_Sc2cpuEnabledCores_Object = MibTableColumn
sc2cpuEnabledCores = _Sc2cpuEnabledCores_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 15),
    _Sc2cpuEnabledCores_Type()
)
sc2cpuEnabledCores.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuEnabledCores.setStatus("mandatory")


class _Sc2cpuMultithreadingEnabled_Type(Integer32):
    """Custom type sc2cpuMultithreadingEnabled based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_Sc2cpuMultithreadingEnabled_Type.__name__ = "Integer32"
_Sc2cpuMultithreadingEnabled_Object = MibTableColumn
sc2cpuMultithreadingEnabled = _Sc2cpuMultithreadingEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 16),
    _Sc2cpuMultithreadingEnabled_Type()
)
sc2cpuMultithreadingEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuMultithreadingEnabled.setStatus("mandatory")


class _Sc2cpuConfigurationStatus_Type(Integer32):
    """Custom type sc2cpuConfigurationStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("normal", 2),
          ("disabledManually", 3),
          ("hotSpare", 4),
          ("mirror", 5),
          ("notUsable", 7),
          ("configurationError", 8))
    )


_Sc2cpuConfigurationStatus_Type.__name__ = "Integer32"
_Sc2cpuConfigurationStatus_Object = MibTableColumn
sc2cpuConfigurationStatus = _Sc2cpuConfigurationStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 17),
    _Sc2cpuConfigurationStatus_Type()
)
sc2cpuConfigurationStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuConfigurationStatus.setStatus("mandatory")
_Sc2cpuMCDRAMSize_Type = Integer32
_Sc2cpuMCDRAMSize_Object = MibTableColumn
sc2cpuMCDRAMSize = _Sc2cpuMCDRAMSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 18),
    _Sc2cpuMCDRAMSize_Type()
)
sc2cpuMCDRAMSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuMCDRAMSize.setStatus("mandatory")
_Sc2cpuMCDRAMSpeed_Type = Integer32
_Sc2cpuMCDRAMSpeed_Object = MibTableColumn
sc2cpuMCDRAMSpeed = _Sc2cpuMCDRAMSpeed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 19),
    _Sc2cpuMCDRAMSpeed_Type()
)
sc2cpuMCDRAMSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuMCDRAMSpeed.setStatus("mandatory")


class _Sc2cpuMCDRAMMode_Type(Integer32):
    """Custom type sc2cpuMCDRAMMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              3)
        )
    )
    namedValues = NamedValues(
        *(("undefined", 1),
          ("flat", 2),
          ("cache", 3),
          ("hybrid", 3))
    )


_Sc2cpuMCDRAMMode_Type.__name__ = "Integer32"
_Sc2cpuMCDRAMMode_Object = MibTableColumn
sc2cpuMCDRAMMode = _Sc2cpuMCDRAMMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 20),
    _Sc2cpuMCDRAMMode_Type()
)
sc2cpuMCDRAMMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuMCDRAMMode.setStatus("mandatory")
_Sc2cpuMCDRAMCacheSize_Type = Integer32
_Sc2cpuMCDRAMCacheSize_Object = MibTableColumn
sc2cpuMCDRAMCacheSize = _Sc2cpuMCDRAMCacheSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 21),
    _Sc2cpuMCDRAMCacheSize_Type()
)
sc2cpuMCDRAMCacheSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuMCDRAMCacheSize.setStatus("mandatory")


class _Sc2cpuMCDRAMMemoryModel_Type(Integer32):
    """Custom type sc2cpuMCDRAMMemoryModel based on Integer32"""
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
        *(("undefined", 1),
          ("all2all", 2),
          ("subNumaCluster2", 3),
          ("subNumaCluster4", 4),
          ("hemisphere", 5),
          ("quadrant", 6))
    )


_Sc2cpuMCDRAMMemoryModel_Type.__name__ = "Integer32"
_Sc2cpuMCDRAMMemoryModel_Object = MibTableColumn
sc2cpuMCDRAMMemoryModel = _Sc2cpuMCDRAMMemoryModel_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 4, 1, 22),
    _Sc2cpuMCDRAMMemoryModel_Type()
)
sc2cpuMCDRAMMemoryModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuMCDRAMMemoryModel.setStatus("mandatory")
_Sc2MemoryModuleTable_Object = MibTable
sc2MemoryModuleTable = _Sc2MemoryModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5)
)
if mibBuilder.loadTexts:
    sc2MemoryModuleTable.setStatus("mandatory")
_Sc2MemoryModules_Object = MibTableRow
sc2MemoryModules = _Sc2MemoryModules_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1)
)
sc2MemoryModules.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2memUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2memModuleNr"),
)
if mibBuilder.loadTexts:
    sc2MemoryModules.setStatus("mandatory")
_Sc2memUnitId_Type = Integer32
_Sc2memUnitId_Object = MibTableColumn
sc2memUnitId = _Sc2memUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 1),
    _Sc2memUnitId_Type()
)
sc2memUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memUnitId.setStatus("mandatory")
_Sc2memModuleNr_Type = Integer32
_Sc2memModuleNr_Object = MibTableColumn
sc2memModuleNr = _Sc2memModuleNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 2),
    _Sc2memModuleNr_Type()
)
sc2memModuleNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleNr.setStatus("mandatory")
_Sc2memModuleDesignation_Type = DisplayString
_Sc2memModuleDesignation_Object = MibTableColumn
sc2memModuleDesignation = _Sc2memModuleDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 3),
    _Sc2memModuleDesignation_Type()
)
sc2memModuleDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleDesignation.setStatus("mandatory")


class _Sc2memModuleStatus_Type(Integer32):
    """Custom type sc2memModuleStatus based on Integer32"""
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
              11)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("not-present", 2),
          ("ok", 3),
          ("disabled", 4),
          ("error", 5),
          ("failed", 6),
          ("prefailure-predicted", 7),
          ("hot-spare", 8),
          ("mirror", 9),
          ("raid", 10),
          ("hidden", 11))
    )


_Sc2memModuleStatus_Type.__name__ = "Integer32"
_Sc2memModuleStatus_Object = MibTableColumn
sc2memModuleStatus = _Sc2memModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 4),
    _Sc2memModuleStatus_Type()
)
sc2memModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleStatus.setStatus("mandatory")
_Sc2memModuleBank_Type = Integer32
_Sc2memModuleBank_Object = MibTableColumn
sc2memModuleBank = _Sc2memModuleBank_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 5),
    _Sc2memModuleBank_Type()
)
sc2memModuleBank.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleBank.setStatus("mandatory")
_Sc2memModuleCapacity_Type = Integer32
_Sc2memModuleCapacity_Object = MibTableColumn
sc2memModuleCapacity = _Sc2memModuleCapacity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 6),
    _Sc2memModuleCapacity_Type()
)
sc2memModuleCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleCapacity.setStatus("mandatory")
_Sc2memModuleStartAddress_Type = Integer32
_Sc2memModuleStartAddress_Object = MibTableColumn
sc2memModuleStartAddress = _Sc2memModuleStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 7),
    _Sc2memModuleStartAddress_Type()
)
sc2memModuleStartAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleStartAddress.setStatus("mandatory")
_Sc2memModuleForm_Type = DisplayString
_Sc2memModuleForm_Object = MibTableColumn
sc2memModuleForm = _Sc2memModuleForm_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 8),
    _Sc2memModuleForm_Type()
)
sc2memModuleForm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleForm.setStatus("mandatory")
_Sc2memModuleType_Type = DisplayString
_Sc2memModuleType_Object = MibTableColumn
sc2memModuleType = _Sc2memModuleType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 9),
    _Sc2memModuleType_Type()
)
sc2memModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleType.setStatus("mandatory")
_Sc2memModuleCorrErrors_Type = Counter32
_Sc2memModuleCorrErrors_Object = MibTableColumn
sc2memModuleCorrErrors = _Sc2memModuleCorrErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 10),
    _Sc2memModuleCorrErrors_Type()
)
sc2memModuleCorrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleCorrErrors.setStatus("mandatory")
_Sc2memModuleUncorrErrors_Type = Counter32
_Sc2memModuleUncorrErrors_Object = MibTableColumn
sc2memModuleUncorrErrors = _Sc2memModuleUncorrErrors_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 11),
    _Sc2memModuleUncorrErrors_Type()
)
sc2memModuleUncorrErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleUncorrErrors.setStatus("mandatory")


class _Sc2memModuleApproved_Type(Integer32):
    """Custom type sc2memModuleApproved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("no", 2),
          ("yes", 3))
    )


_Sc2memModuleApproved_Type.__name__ = "Integer32"
_Sc2memModuleApproved_Object = MibTableColumn
sc2memModuleApproved = _Sc2memModuleApproved_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 12),
    _Sc2memModuleApproved_Type()
)
sc2memModuleApproved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleApproved.setStatus("mandatory")


class _Sc2memModuleConfiguration_Type(Integer32):
    """Custom type sc2memModuleConfiguration based on Integer32"""
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
        *(("unknown", 1),
          ("normal", 2),
          ("disabled", 3),
          ("hotSpare", 4),
          ("mirror", 5),
          ("raid", 6),
          ("notUsable", 7),
          ("configurationError", 8))
    )


_Sc2memModuleConfiguration_Type.__name__ = "Integer32"
_Sc2memModuleConfiguration_Object = MibTableColumn
sc2memModuleConfiguration = _Sc2memModuleConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 13),
    _Sc2memModuleConfiguration_Type()
)
sc2memModuleConfiguration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleConfiguration.setStatus("mandatory")
_Sc2memModuleFrequency_Type = Integer32
_Sc2memModuleFrequency_Object = MibTableColumn
sc2memModuleFrequency = _Sc2memModuleFrequency_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 14),
    _Sc2memModuleFrequency_Type()
)
sc2memModuleFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleFrequency.setStatus("mandatory")
_Sc2memModuleMaxFrequency_Type = Integer32
_Sc2memModuleMaxFrequency_Object = MibTableColumn
sc2memModuleMaxFrequency = _Sc2memModuleMaxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 15),
    _Sc2memModuleMaxFrequency_Type()
)
sc2memModuleMaxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleMaxFrequency.setStatus("mandatory")
_Sc2memModuleVoltInterface_Type = DisplayString
_Sc2memModuleVoltInterface_Object = MibTableColumn
sc2memModuleVoltInterface = _Sc2memModuleVoltInterface_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 5, 1, 16),
    _Sc2memModuleVoltInterface_Type()
)
sc2memModuleVoltInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2memModuleVoltInterface.setStatus("mandatory")


class _Sc2cpuMultithreadEnable_Type(Integer32):
    """Custom type sc2cpuMultithreadEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_Sc2cpuMultithreadEnable_Type.__name__ = "Integer32"
_Sc2cpuMultithreadEnable_Object = MibScalar
sc2cpuMultithreadEnable = _Sc2cpuMultithreadEnable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 6),
    _Sc2cpuMultithreadEnable_Type()
)
sc2cpuMultithreadEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpuMultithreadEnable.setStatus("mandatory")
_Sc2ComponentPowerConsumptionTable_Object = MibTable
sc2ComponentPowerConsumptionTable = _Sc2ComponentPowerConsumptionTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 7)
)
if mibBuilder.loadTexts:
    sc2ComponentPowerConsumptionTable.setStatus("mandatory")
_Sc2ComponentPowerConsumption_Object = MibTableRow
sc2ComponentPowerConsumption = _Sc2ComponentPowerConsumption_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 7, 1)
)
sc2ComponentPowerConsumption.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2cpcUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2cpcComponentClass"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2cpcComponentIndex"),
)
if mibBuilder.loadTexts:
    sc2ComponentPowerConsumption.setStatus("mandatory")
_Sc2cpcUnitId_Type = Integer32
_Sc2cpcUnitId_Object = MibTableColumn
sc2cpcUnitId = _Sc2cpcUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 7, 1, 1),
    _Sc2cpcUnitId_Type()
)
sc2cpcUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpcUnitId.setStatus("mandatory")


class _Sc2cpcComponentClass_Type(Integer32):
    """Custom type sc2cpcComponentClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              7,
              8,
              9,
              10,
              11,
              23,
              24,
              26,
              29,
              30,
              32,
              224)
        )
    )
    namedValues = NamedValues(
        *(("processor", 3),
          ("disk", 4),
          ("system-board", 7),
          ("memory-unit", 8),
          ("processor-module", 9),
          ("power-supply", 10),
          ("gpu", 11),
          ("chassis", 23),
          ("sub-chassis", 24),
          ("disk-bay", 26),
          ("cooling-device", 29),
          ("cooling-unit", 30),
          ("memory-device", 32),
          ("total-power", 224))
    )


_Sc2cpcComponentClass_Type.__name__ = "Integer32"
_Sc2cpcComponentClass_Object = MibTableColumn
sc2cpcComponentClass = _Sc2cpcComponentClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 7, 1, 2),
    _Sc2cpcComponentClass_Type()
)
sc2cpcComponentClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpcComponentClass.setStatus("mandatory")
_Sc2cpcComponentIndex_Type = Integer32
_Sc2cpcComponentIndex_Object = MibTableColumn
sc2cpcComponentIndex = _Sc2cpcComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 7, 1, 3),
    _Sc2cpcComponentIndex_Type()
)
sc2cpcComponentIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpcComponentIndex.setStatus("mandatory")
_Sc2cpcDesignation_Type = DisplayString
_Sc2cpcDesignation_Object = MibTableColumn
sc2cpcDesignation = _Sc2cpcDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 7, 1, 4),
    _Sc2cpcDesignation_Type()
)
sc2cpcDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpcDesignation.setStatus("mandatory")
_Sc2cpcCurrentValue_Type = Integer32
_Sc2cpcCurrentValue_Object = MibTableColumn
sc2cpcCurrentValue = _Sc2cpcCurrentValue_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 7, 1, 5),
    _Sc2cpcCurrentValue_Type()
)
sc2cpcCurrentValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cpcCurrentValue.setStatus("mandatory")
_Sc2TrustedPlatformModuleTable_Object = MibTable
sc2TrustedPlatformModuleTable = _Sc2TrustedPlatformModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 8)
)
if mibBuilder.loadTexts:
    sc2TrustedPlatformModuleTable.setStatus("mandatory")
_Sc2TrustedPlatformModule_Object = MibTableRow
sc2TrustedPlatformModule = _Sc2TrustedPlatformModule_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 8, 1)
)
sc2TrustedPlatformModule.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2tpmUnitId"),
)
if mibBuilder.loadTexts:
    sc2TrustedPlatformModule.setStatus("mandatory")
_Sc2tpmUnitId_Type = Integer32
_Sc2tpmUnitId_Object = MibTableColumn
sc2tpmUnitId = _Sc2tpmUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 8, 1, 1),
    _Sc2tpmUnitId_Type()
)
sc2tpmUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tpmUnitId.setStatus("mandatory")
_Sc2tpmHardwareAvailable_Type = TrueFalseUnknown
_Sc2tpmHardwareAvailable_Object = MibTableColumn
sc2tpmHardwareAvailable = _Sc2tpmHardwareAvailable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 8, 1, 2),
    _Sc2tpmHardwareAvailable_Type()
)
sc2tpmHardwareAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tpmHardwareAvailable.setStatus("mandatory")
_Sc2tpmBiosEnabled_Type = TrueFalseUnknown
_Sc2tpmBiosEnabled_Object = MibTableColumn
sc2tpmBiosEnabled = _Sc2tpmBiosEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 8, 1, 3),
    _Sc2tpmBiosEnabled_Type()
)
sc2tpmBiosEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tpmBiosEnabled.setStatus("mandatory")
_Sc2tpmEnabled_Type = TrueFalseUnknown
_Sc2tpmEnabled_Object = MibTableColumn
sc2tpmEnabled = _Sc2tpmEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 8, 1, 4),
    _Sc2tpmEnabled_Type()
)
sc2tpmEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tpmEnabled.setStatus("mandatory")
_Sc2tpmActivated_Type = TrueFalseUnknown
_Sc2tpmActivated_Object = MibTableColumn
sc2tpmActivated = _Sc2tpmActivated_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 8, 1, 5),
    _Sc2tpmActivated_Type()
)
sc2tpmActivated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tpmActivated.setStatus("mandatory")
_Sc2tpmOwnership_Type = TrueFalseUnknown
_Sc2tpmOwnership_Object = MibTableColumn
sc2tpmOwnership = _Sc2tpmOwnership_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 8, 1, 6),
    _Sc2tpmOwnership_Type()
)
sc2tpmOwnership.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2tpmOwnership.setStatus("mandatory")
_Sc2PersistentMemoryModuleTable_Object = MibTable
sc2PersistentMemoryModuleTable = _Sc2PersistentMemoryModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9)
)
if mibBuilder.loadTexts:
    sc2PersistentMemoryModuleTable.setStatus("mandatory")
_Sc2PersistentMemoryModules_Object = MibTableRow
sc2PersistentMemoryModules = _Sc2PersistentMemoryModules_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1)
)
sc2PersistentMemoryModules.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2memUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2memModuleNr"),
)
if mibBuilder.loadTexts:
    sc2PersistentMemoryModules.setStatus("mandatory")
_Sc2nvmemMemoryModeEnabled_Type = TrueFalseUnknown
_Sc2nvmemMemoryModeEnabled_Object = MibTableColumn
sc2nvmemMemoryModeEnabled = _Sc2nvmemMemoryModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 1),
    _Sc2nvmemMemoryModeEnabled_Type()
)
sc2nvmemMemoryModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemMemoryModeEnabled.setStatus("mandatory")
_Sc2nvmemPersistentModeEnabled_Type = TrueFalseUnknown
_Sc2nvmemPersistentModeEnabled_Object = MibTableColumn
sc2nvmemPersistentModeEnabled = _Sc2nvmemPersistentModeEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 2),
    _Sc2nvmemPersistentModeEnabled_Type()
)
sc2nvmemPersistentModeEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemPersistentModeEnabled.setStatus("mandatory")
_Sc2nvmemPackageSparingCapable_Type = TrueFalseUnknown
_Sc2nvmemPackageSparingCapable_Object = MibTableColumn
sc2nvmemPackageSparingCapable = _Sc2nvmemPackageSparingCapable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 3),
    _Sc2nvmemPackageSparingCapable_Type()
)
sc2nvmemPackageSparingCapable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemPackageSparingCapable.setStatus("mandatory")
_Sc2nvmemEncryptionEnabled_Type = TrueFalseUnknown
_Sc2nvmemEncryptionEnabled_Object = MibTableColumn
sc2nvmemEncryptionEnabled = _Sc2nvmemEncryptionEnabled_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 4),
    _Sc2nvmemEncryptionEnabled_Type()
)
sc2nvmemEncryptionEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemEncryptionEnabled.setStatus("mandatory")
_Sc2nvmemFirmwareRevision_Type = DisplayString
_Sc2nvmemFirmwareRevision_Object = MibTableColumn
sc2nvmemFirmwareRevision = _Sc2nvmemFirmwareRevision_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 5),
    _Sc2nvmemFirmwareRevision_Type()
)
sc2nvmemFirmwareRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemFirmwareRevision.setStatus("mandatory")
_Sc2nvmemTotalSize_Type = Integer32
_Sc2nvmemTotalSize_Object = MibTableColumn
sc2nvmemTotalSize = _Sc2nvmemTotalSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 6),
    _Sc2nvmemTotalSize_Type()
)
sc2nvmemTotalSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemTotalSize.setStatus("mandatory")
_Sc2nvmemRawCapacity_Type = Integer32
_Sc2nvmemRawCapacity_Object = MibTableColumn
sc2nvmemRawCapacity = _Sc2nvmemRawCapacity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 7),
    _Sc2nvmemRawCapacity_Type()
)
sc2nvmemRawCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemRawCapacity.setStatus("mandatory")
_Sc2nvmemVolatileCapacity_Type = Integer32
_Sc2nvmemVolatileCapacity_Object = MibTableColumn
sc2nvmemVolatileCapacity = _Sc2nvmemVolatileCapacity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 8),
    _Sc2nvmemVolatileCapacity_Type()
)
sc2nvmemVolatileCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemVolatileCapacity.setStatus("mandatory")
_Sc2nvmemPersistentCapacity_Type = Integer32
_Sc2nvmemPersistentCapacity_Object = MibTableColumn
sc2nvmemPersistentCapacity = _Sc2nvmemPersistentCapacity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 9),
    _Sc2nvmemPersistentCapacity_Type()
)
sc2nvmemPersistentCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemPersistentCapacity.setStatus("mandatory")
_Sc2nvmemVolatilePercent_Type = Integer32
_Sc2nvmemVolatilePercent_Object = MibTableColumn
sc2nvmemVolatilePercent = _Sc2nvmemVolatilePercent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 10),
    _Sc2nvmemVolatilePercent_Type()
)
sc2nvmemVolatilePercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemVolatilePercent.setStatus("mandatory")
_Sc2nvmemPersistentPercent_Type = Integer32
_Sc2nvmemPersistentPercent_Object = MibTableColumn
sc2nvmemPersistentPercent = _Sc2nvmemPersistentPercent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 11),
    _Sc2nvmemPersistentPercent_Type()
)
sc2nvmemPersistentPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemPersistentPercent.setStatus("mandatory")
_Sc2nvmemVolatileStart_Type = DisplayString
_Sc2nvmemVolatileStart_Object = MibTableColumn
sc2nvmemVolatileStart = _Sc2nvmemVolatileStart_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 12),
    _Sc2nvmemVolatileStart_Type()
)
sc2nvmemVolatileStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemVolatileStart.setStatus("mandatory")
_Sc2nvmemPersistentStart_Type = DisplayString
_Sc2nvmemPersistentStart_Object = MibTableColumn
sc2nvmemPersistentStart = _Sc2nvmemPersistentStart_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 13),
    _Sc2nvmemPersistentStart_Type()
)
sc2nvmemPersistentStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemPersistentStart.setStatus("mandatory")
_Sc2nvmemHealthStatusNonCritical_Type = TrueFalseUnknown
_Sc2nvmemHealthStatusNonCritical_Object = MibTableColumn
sc2nvmemHealthStatusNonCritical = _Sc2nvmemHealthStatusNonCritical_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 14),
    _Sc2nvmemHealthStatusNonCritical_Type()
)
sc2nvmemHealthStatusNonCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemHealthStatusNonCritical.setStatus("mandatory")
_Sc2nvmemHealthStatusCritical_Type = TrueFalseUnknown
_Sc2nvmemHealthStatusCritical_Object = MibTableColumn
sc2nvmemHealthStatusCritical = _Sc2nvmemHealthStatusCritical_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 15),
    _Sc2nvmemHealthStatusCritical_Type()
)
sc2nvmemHealthStatusCritical.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemHealthStatusCritical.setStatus("mandatory")
_Sc2nvmemHealthStatusFatal_Type = TrueFalseUnknown
_Sc2nvmemHealthStatusFatal_Object = MibTableColumn
sc2nvmemHealthStatusFatal = _Sc2nvmemHealthStatusFatal_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 16),
    _Sc2nvmemHealthStatusFatal_Type()
)
sc2nvmemHealthStatusFatal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemHealthStatusFatal.setStatus("mandatory")
_Sc2nvmemPowerOnTime_Type = Counter32
_Sc2nvmemPowerOnTime_Object = MibTableColumn
sc2nvmemPowerOnTime = _Sc2nvmemPowerOnTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 17),
    _Sc2nvmemPowerOnTime_Type()
)
sc2nvmemPowerOnTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemPowerOnTime.setStatus("mandatory")
_Sc2nvmemUpTime_Type = Counter32
_Sc2nvmemUpTime_Object = MibTableColumn
sc2nvmemUpTime = _Sc2nvmemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 18),
    _Sc2nvmemUpTime_Type()
)
sc2nvmemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemUpTime.setStatus("mandatory")
_Sc2nvmemLiftetimeRemaining_Type = Integer32
_Sc2nvmemLiftetimeRemaining_Object = MibTableColumn
sc2nvmemLiftetimeRemaining = _Sc2nvmemLiftetimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 19),
    _Sc2nvmemLiftetimeRemaining_Type()
)
sc2nvmemLiftetimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemLiftetimeRemaining.setStatus("mandatory")
_Sc2nvmemAveragePowerBudget_Type = Integer32
_Sc2nvmemAveragePowerBudget_Object = MibTableColumn
sc2nvmemAveragePowerBudget = _Sc2nvmemAveragePowerBudget_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 20),
    _Sc2nvmemAveragePowerBudget_Type()
)
sc2nvmemAveragePowerBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemAveragePowerBudget.setStatus("mandatory")
_Sc2nvmemPeakPowerBudget_Type = Integer32
_Sc2nvmemPeakPowerBudget_Object = MibTableColumn
sc2nvmemPeakPowerBudget = _Sc2nvmemPeakPowerBudget_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 6, 9, 1, 21),
    _Sc2nvmemPeakPowerBudget_Type()
)
sc2nvmemPeakPowerBudget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2nvmemPeakPowerBudget.setStatus("mandatory")
_Sc2Recovery_ObjectIdentity = ObjectIdentity
sc2Recovery = _Sc2Recovery_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7)
)
_Sc2MessageLogTable_Object = MibTable
sc2MessageLogTable = _Sc2MessageLogTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 1)
)
if mibBuilder.loadTexts:
    sc2MessageLogTable.setStatus("mandatory")
_Sc2MessageLogs_Object = MibTableRow
sc2MessageLogs = _Sc2MessageLogs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 1, 1)
)
sc2MessageLogs.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2msgUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2msgLogEntryNr"),
)
if mibBuilder.loadTexts:
    sc2MessageLogs.setStatus("mandatory")
_Sc2msgUnitId_Type = Integer32
_Sc2msgUnitId_Object = MibTableColumn
sc2msgUnitId = _Sc2msgUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 1, 1, 1),
    _Sc2msgUnitId_Type()
)
sc2msgUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgUnitId.setStatus("mandatory")
_Sc2msgLogEntryNr_Type = Integer32
_Sc2msgLogEntryNr_Object = MibTableColumn
sc2msgLogEntryNr = _Sc2msgLogEntryNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 1, 1, 2),
    _Sc2msgLogEntryNr_Type()
)
sc2msgLogEntryNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgLogEntryNr.setStatus("mandatory")
_Sc2msgLogEntryData_Type = OctetString
_Sc2msgLogEntryData_Object = MibTableColumn
sc2msgLogEntryData = _Sc2msgLogEntryData_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 1, 1, 3),
    _Sc2msgLogEntryData_Type()
)
sc2msgLogEntryData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgLogEntryData.setStatus("mandatory")
_Sc2WatchdogTable_Object = MibTable
sc2WatchdogTable = _Sc2WatchdogTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 2)
)
if mibBuilder.loadTexts:
    sc2WatchdogTable.setStatus("mandatory")
_Sc2Watchdogs_Object = MibTableRow
sc2Watchdogs = _Sc2Watchdogs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 2, 1)
)
sc2Watchdogs.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2wdUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2WatchdogType"),
)
if mibBuilder.loadTexts:
    sc2Watchdogs.setStatus("mandatory")
_Sc2wdUnitId_Type = Integer32
_Sc2wdUnitId_Object = MibTableColumn
sc2wdUnitId = _Sc2wdUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 2, 1, 1),
    _Sc2wdUnitId_Type()
)
sc2wdUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2wdUnitId.setStatus("mandatory")


class _Sc2WatchdogType_Type(Integer32):
    """Custom type sc2WatchdogType based on Integer32"""
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
        *(("other", 1),
          ("hardware", 2),
          ("software", 3),
          ("bios", 4),
          ("boot", 5),
          ("management-controller", 6),
          ("remote-management-controller", 7),
          ("cpu", 8))
    )


_Sc2WatchdogType_Type.__name__ = "Integer32"
_Sc2WatchdogType_Object = MibTableColumn
sc2WatchdogType = _Sc2WatchdogType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 2, 1, 2),
    _Sc2WatchdogType_Type()
)
sc2WatchdogType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2WatchdogType.setStatus("mandatory")


class _Sc2WatchdogStatus_Type(Integer32):
    """Custom type sc2WatchdogStatus based on Integer32"""
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
        *(("unknown", 1),
          ("disabled", 2),
          ("enabled", 3),
          ("not-available", 4))
    )


_Sc2WatchdogStatus_Type.__name__ = "Integer32"
_Sc2WatchdogStatus_Object = MibTableColumn
sc2WatchdogStatus = _Sc2WatchdogStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 2, 1, 3),
    _Sc2WatchdogStatus_Type()
)
sc2WatchdogStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2WatchdogStatus.setStatus("mandatory")
_Sc2WatchdogTime_Type = Integer32
_Sc2WatchdogTime_Object = MibTableColumn
sc2WatchdogTime = _Sc2WatchdogTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 2, 1, 4),
    _Sc2WatchdogTime_Type()
)
sc2WatchdogTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2WatchdogTime.setStatus("mandatory")


class _Sc2WatchdogAction_Type(Integer32):
    """Custom type sc2WatchdogAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("continue", 2),
          ("reset", 4),
          ("nmi", 5),
          ("power-cycle", 6))
    )


_Sc2WatchdogAction_Type.__name__ = "Integer32"
_Sc2WatchdogAction_Object = MibTableColumn
sc2WatchdogAction = _Sc2WatchdogAction_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 2, 1, 5),
    _Sc2WatchdogAction_Type()
)
sc2WatchdogAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2WatchdogAction.setStatus("mandatory")
_Sc2RecoverySettingTable_Object = MibTable
sc2RecoverySettingTable = _Sc2RecoverySettingTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 3)
)
if mibBuilder.loadTexts:
    sc2RecoverySettingTable.setStatus("mandatory")
_Sc2RecoverySettings_Object = MibTableRow
sc2RecoverySettings = _Sc2RecoverySettings_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 3, 1)
)
sc2RecoverySettings.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2asrUnitId"),
)
if mibBuilder.loadTexts:
    sc2RecoverySettings.setStatus("mandatory")
_Sc2asrUnitId_Type = Integer32
_Sc2asrUnitId_Object = MibTableColumn
sc2asrUnitId = _Sc2asrUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 3, 1, 1),
    _Sc2asrUnitId_Type()
)
sc2asrUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2asrUnitId.setStatus("mandatory")
_Sc2asrNrRebootRetries_Type = Integer32
_Sc2asrNrRebootRetries_Object = MibTableColumn
sc2asrNrRebootRetries = _Sc2asrNrRebootRetries_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 3, 1, 2),
    _Sc2asrNrRebootRetries_Type()
)
sc2asrNrRebootRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2asrNrRebootRetries.setStatus("mandatory")
_Sc2asrDefaultRebootRetries_Type = Integer32
_Sc2asrDefaultRebootRetries_Object = MibTableColumn
sc2asrDefaultRebootRetries = _Sc2asrDefaultRebootRetries_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 3, 1, 3),
    _Sc2asrDefaultRebootRetries_Type()
)
sc2asrDefaultRebootRetries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2asrDefaultRebootRetries.setStatus("mandatory")


class _Sc2asrNextBootSource_Type(Integer32):
    """Custom type sc2asrNextBootSource based on Integer32"""
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
        *(("unknown", 1),
          ("operating-system", 2),
          ("reserved", 3),
          ("diag-system", 4),
          ("remote-disk", 5))
    )


_Sc2asrNextBootSource_Type.__name__ = "Integer32"
_Sc2asrNextBootSource_Object = MibTableColumn
sc2asrNextBootSource = _Sc2asrNextBootSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 3, 1, 4),
    _Sc2asrNextBootSource_Type()
)
sc2asrNextBootSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2asrNextBootSource.setStatus("mandatory")


class _Sc2asrRebootFailAction_Type(Integer32):
    """Custom type sc2asrRebootFailAction based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("switch-off", 2),
          ("boot-diag-system", 3),
          ("no-diag-system", 4),
          ("remote-image-disk", 5),
          ("pxe", 6),
          ("rsb-usb", 7),
          ("remote-storage", 8),
          ("stop-reboot", 9),
          ("diag-interrupt-assert", 10))
    )


_Sc2asrRebootFailAction_Type.__name__ = "Integer32"
_Sc2asrRebootFailAction_Object = MibTableColumn
sc2asrRebootFailAction = _Sc2asrRebootFailAction_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 3, 1, 5),
    _Sc2asrRebootFailAction_Type()
)
sc2asrRebootFailAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2asrRebootFailAction.setStatus("mandatory")
_Sc2asrRestartDelay_Type = Integer32
_Sc2asrRestartDelay_Object = MibTableColumn
sc2asrRestartDelay = _Sc2asrRestartDelay_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 3, 1, 6),
    _Sc2asrRestartDelay_Type()
)
sc2asrRestartDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2asrRestartDelay.setStatus("mandatory")


class _Sc2asrPostErrorHalt_Type(Integer32):
    """Custom type sc2asrPostErrorHalt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("halt-on-any-error", 2),
          ("no-halt-on-any-error", 3),
          ("other", 9))
    )


_Sc2asrPostErrorHalt_Type.__name__ = "Integer32"
_Sc2asrPostErrorHalt_Object = MibTableColumn
sc2asrPostErrorHalt = _Sc2asrPostErrorHalt_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 3, 1, 7),
    _Sc2asrPostErrorHalt_Type()
)
sc2asrPostErrorHalt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2asrPostErrorHalt.setStatus("mandatory")
_Sc2MessageTextLogTable_Object = MibTable
sc2MessageTextLogTable = _Sc2MessageTextLogTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4)
)
if mibBuilder.loadTexts:
    sc2MessageTextLogTable.setStatus("mandatory")
_Sc2MessageTextLogs_Object = MibTableRow
sc2MessageTextLogs = _Sc2MessageTextLogs_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4, 1)
)
sc2MessageTextLogs.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2msgTextLogUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2msgTextLogLanguage"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2msgTextLogSeqNr"),
)
if mibBuilder.loadTexts:
    sc2MessageTextLogs.setStatus("mandatory")
_Sc2msgTextLogUnitId_Type = Integer32
_Sc2msgTextLogUnitId_Object = MibTableColumn
sc2msgTextLogUnitId = _Sc2msgTextLogUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4, 1, 1),
    _Sc2msgTextLogUnitId_Type()
)
sc2msgTextLogUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgTextLogUnitId.setStatus("mandatory")
_Sc2msgTextLogLanguage_Type = Integer32
_Sc2msgTextLogLanguage_Object = MibTableColumn
sc2msgTextLogLanguage = _Sc2msgTextLogLanguage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4, 1, 2),
    _Sc2msgTextLogLanguage_Type()
)
sc2msgTextLogLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgTextLogLanguage.setStatus("mandatory")
_Sc2msgTextLogSeqNr_Type = Integer32
_Sc2msgTextLogSeqNr_Object = MibTableColumn
sc2msgTextLogSeqNr = _Sc2msgTextLogSeqNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4, 1, 3),
    _Sc2msgTextLogSeqNr_Type()
)
sc2msgTextLogSeqNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgTextLogSeqNr.setStatus("mandatory")
_Sc2msgTextLogTimestamp_Type = Integer32
_Sc2msgTextLogTimestamp_Object = MibTableColumn
sc2msgTextLogTimestamp = _Sc2msgTextLogTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4, 1, 4),
    _Sc2msgTextLogTimestamp_Type()
)
sc2msgTextLogTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgTextLogTimestamp.setStatus("mandatory")
_Sc2msgTextLogMessage_Type = DisplayString
_Sc2msgTextLogMessage_Object = MibTableColumn
sc2msgTextLogMessage = _Sc2msgTextLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4, 1, 5),
    _Sc2msgTextLogMessage_Type()
)
sc2msgTextLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgTextLogMessage.setStatus("mandatory")
_Sc2msgTextLogErrorCode_Type = Integer32
_Sc2msgTextLogErrorCode_Object = MibTableColumn
sc2msgTextLogErrorCode = _Sc2msgTextLogErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4, 1, 6),
    _Sc2msgTextLogErrorCode_Type()
)
sc2msgTextLogErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgTextLogErrorCode.setStatus("mandatory")


class _Sc2msgTextLogSeverity_Type(Integer32):
    """Custom type sc2msgTextLogSeverity based on Integer32"""
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
          ("minor", 2),
          ("major", 3),
          ("critical", 4))
    )


_Sc2msgTextLogSeverity_Type.__name__ = "Integer32"
_Sc2msgTextLogSeverity_Object = MibTableColumn
sc2msgTextLogSeverity = _Sc2msgTextLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4, 1, 7),
    _Sc2msgTextLogSeverity_Type()
)
sc2msgTextLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgTextLogSeverity.setStatus("mandatory")
_Sc2msgTextLogCSSComponent_Type = TrueFalse
_Sc2msgTextLogCSSComponent_Object = MibTableColumn
sc2msgTextLogCSSComponent = _Sc2msgTextLogCSSComponent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 4, 1, 8),
    _Sc2msgTextLogCSSComponent_Type()
)
sc2msgTextLogCSSComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2msgTextLogCSSComponent.setStatus("mandatory")
_Sc2MessageLogActionHintTable_Object = MibTable
sc2MessageLogActionHintTable = _Sc2MessageLogActionHintTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 5)
)
if mibBuilder.loadTexts:
    sc2MessageLogActionHintTable.setStatus("mandatory")
_Sc2MessageLogActionHints_Object = MibTableRow
sc2MessageLogActionHints = _Sc2MessageLogActionHints_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 5, 1)
)
sc2MessageLogActionHints.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2mlaLanguage"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2mlaErrorCode"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2mlaType"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2mlaIndex"),
)
if mibBuilder.loadTexts:
    sc2MessageLogActionHints.setStatus("mandatory")
_Sc2mlaLanguage_Type = Integer32
_Sc2mlaLanguage_Object = MibTableColumn
sc2mlaLanguage = _Sc2mlaLanguage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 5, 1, 1),
    _Sc2mlaLanguage_Type()
)
sc2mlaLanguage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2mlaLanguage.setStatus("mandatory")
_Sc2mlaErrorCode_Type = Integer32
_Sc2mlaErrorCode_Object = MibTableColumn
sc2mlaErrorCode = _Sc2mlaErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 5, 1, 2),
    _Sc2mlaErrorCode_Type()
)
sc2mlaErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2mlaErrorCode.setStatus("mandatory")


class _Sc2mlaType_Type(Integer32):
    """Custom type sc2mlaType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("summary", 1),
          ("cause", 2),
          ("resolution", 3))
    )


_Sc2mlaType_Type.__name__ = "Integer32"
_Sc2mlaType_Object = MibTableColumn
sc2mlaType = _Sc2mlaType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 5, 1, 3),
    _Sc2mlaType_Type()
)
sc2mlaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2mlaType.setStatus("mandatory")
_Sc2mlaIndex_Type = Integer32
_Sc2mlaIndex_Object = MibTableColumn
sc2mlaIndex = _Sc2mlaIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 5, 1, 4),
    _Sc2mlaIndex_Type()
)
sc2mlaIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2mlaIndex.setStatus("mandatory")
_Sc2mlaMessage_Type = DisplayString
_Sc2mlaMessage_Object = MibTableColumn
sc2mlaMessage = _Sc2mlaMessage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 7, 5, 1, 5),
    _Sc2mlaMessage_Type()
)
sc2mlaMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2mlaMessage.setStatus("mandatory")
_Sc2Status_ObjectIdentity = ObjectIdentity
sc2Status = _Sc2Status_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8)
)
_Sc2AgentStatus_Type = CompStatus
_Sc2AgentStatus_Object = MibScalar
sc2AgentStatus = _Sc2AgentStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 1),
    _Sc2AgentStatus_Type()
)
sc2AgentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2AgentStatus.setStatus("mandatory")
_Sc2StatusComponentTable_Object = MibTable
sc2StatusComponentTable = _Sc2StatusComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2)
)
if mibBuilder.loadTexts:
    sc2StatusComponentTable.setStatus("mandatory")
_Sc2StatusComponents_Object = MibTableRow
sc2StatusComponents = _Sc2StatusComponents_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1)
)
sc2StatusComponents.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2csUnitId"),
)
if mibBuilder.loadTexts:
    sc2StatusComponents.setStatus("mandatory")
_Sc2csUnitId_Type = Integer32
_Sc2csUnitId_Object = MibTableColumn
sc2csUnitId = _Sc2csUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1, 1),
    _Sc2csUnitId_Type()
)
sc2csUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2csUnitId.setStatus("mandatory")
_Sc2csStatusOverall_Type = CompStatus
_Sc2csStatusOverall_Object = MibTableColumn
sc2csStatusOverall = _Sc2csStatusOverall_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1, 2),
    _Sc2csStatusOverall_Type()
)
sc2csStatusOverall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2csStatusOverall.setStatus("mandatory")
_Sc2csStatusBoot_Type = CompStatus
_Sc2csStatusBoot_Object = MibTableColumn
sc2csStatusBoot = _Sc2csStatusBoot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1, 3),
    _Sc2csStatusBoot_Type()
)
sc2csStatusBoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2csStatusBoot.setStatus("mandatory")
_Sc2csStatusPowerSupply_Type = CompStatus
_Sc2csStatusPowerSupply_Object = MibTableColumn
sc2csStatusPowerSupply = _Sc2csStatusPowerSupply_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1, 4),
    _Sc2csStatusPowerSupply_Type()
)
sc2csStatusPowerSupply.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2csStatusPowerSupply.setStatus("mandatory")
_Sc2csStatusTemperature_Type = CompStatus
_Sc2csStatusTemperature_Object = MibTableColumn
sc2csStatusTemperature = _Sc2csStatusTemperature_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1, 5),
    _Sc2csStatusTemperature_Type()
)
sc2csStatusTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2csStatusTemperature.setStatus("mandatory")
_Sc2csStatusFans_Type = CompStatus
_Sc2csStatusFans_Object = MibTableColumn
sc2csStatusFans = _Sc2csStatusFans_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1, 6),
    _Sc2csStatusFans_Type()
)
sc2csStatusFans.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2csStatusFans.setStatus("mandatory")
_Sc2csStatusVoltages_Type = CompStatus
_Sc2csStatusVoltages_Object = MibTableColumn
sc2csStatusVoltages = _Sc2csStatusVoltages_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1, 7),
    _Sc2csStatusVoltages_Type()
)
sc2csStatusVoltages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2csStatusVoltages.setStatus("mandatory")
_Sc2csStatusCpu_Type = CompStatus
_Sc2csStatusCpu_Object = MibTableColumn
sc2csStatusCpu = _Sc2csStatusCpu_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1, 8),
    _Sc2csStatusCpu_Type()
)
sc2csStatusCpu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2csStatusCpu.setStatus("mandatory")
_Sc2csStatusMemoryModule_Type = CompStatus
_Sc2csStatusMemoryModule_Object = MibTableColumn
sc2csStatusMemoryModule = _Sc2csStatusMemoryModule_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 2, 1, 9),
    _Sc2csStatusMemoryModule_Type()
)
sc2csStatusMemoryModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2csStatusMemoryModule.setStatus("mandatory")
_Sc2ComponentStatusSensorTable_Object = MibTable
sc2ComponentStatusSensorTable = _Sc2ComponentStatusSensorTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3)
)
if mibBuilder.loadTexts:
    sc2ComponentStatusSensorTable.setStatus("mandatory")
_Sc2ComponentStatusSensors_Object = MibTableRow
sc2ComponentStatusSensors = _Sc2ComponentStatusSensors_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1)
)
sc2ComponentStatusSensors.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2cssUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2cssSensorNumber"),
)
if mibBuilder.loadTexts:
    sc2ComponentStatusSensors.setStatus("mandatory")
_Sc2cssUnitId_Type = Integer32
_Sc2cssUnitId_Object = MibTableColumn
sc2cssUnitId = _Sc2cssUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1, 1),
    _Sc2cssUnitId_Type()
)
sc2cssUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssUnitId.setStatus("mandatory")
_Sc2cssSensorNumber_Type = Integer32
_Sc2cssSensorNumber_Object = MibTableColumn
sc2cssSensorNumber = _Sc2cssSensorNumber_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1, 2),
    _Sc2cssSensorNumber_Type()
)
sc2cssSensorNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssSensorNumber.setStatus("mandatory")
_Sc2cssSensorDesignation_Type = DisplayString
_Sc2cssSensorDesignation_Object = MibTableColumn
sc2cssSensorDesignation = _Sc2cssSensorDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1, 3),
    _Sc2cssSensorDesignation_Type()
)
sc2cssSensorDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssSensorDesignation.setStatus("mandatory")
_Sc2cssSensorDevice_Type = DisplayString
_Sc2cssSensorDevice_Object = MibTableColumn
sc2cssSensorDevice = _Sc2cssSensorDevice_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1, 4),
    _Sc2cssSensorDevice_Type()
)
sc2cssSensorDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssSensorDevice.setStatus("mandatory")
_Sc2cssSensorDeviceInstance_Type = Integer32
_Sc2cssSensorDeviceInstance_Object = MibTableColumn
sc2cssSensorDeviceInstance = _Sc2cssSensorDeviceInstance_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1, 5),
    _Sc2cssSensorDeviceInstance_Type()
)
sc2cssSensorDeviceInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssSensorDeviceInstance.setStatus("mandatory")
_Sc2cssSensorPhysicalLed_Type = TrueFalse
_Sc2cssSensorPhysicalLed_Object = MibTableColumn
sc2cssSensorPhysicalLed = _Sc2cssSensorPhysicalLed_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1, 6),
    _Sc2cssSensorPhysicalLed_Type()
)
sc2cssSensorPhysicalLed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssSensorPhysicalLed.setStatus("mandatory")
_Sc2cssSensorCssComponent_Type = TrueFalse
_Sc2cssSensorCssComponent_Object = MibTableColumn
sc2cssSensorCssComponent = _Sc2cssSensorCssComponent_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1, 7),
    _Sc2cssSensorCssComponent_Type()
)
sc2cssSensorCssComponent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssSensorCssComponent.setStatus("mandatory")


class _Sc2cssSensorStatus_Type(Integer32):
    """Custom type sc2cssSensorStatus based on Integer32"""
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
        *(("unknown", 1),
          ("ok", 2),
          ("identify", 3),
          ("prefailure-warning", 4),
          ("failure", 5),
          ("not-present", 6))
    )


_Sc2cssSensorStatus_Type.__name__ = "Integer32"
_Sc2cssSensorStatus_Object = MibTableColumn
sc2cssSensorStatus = _Sc2cssSensorStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1, 8),
    _Sc2cssSensorStatus_Type()
)
sc2cssSensorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssSensorStatus.setStatus("mandatory")
_Sc2cssComponentServicePartId_Type = DisplayString
_Sc2cssComponentServicePartId_Object = MibTableColumn
sc2cssComponentServicePartId = _Sc2cssComponentServicePartId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 3, 1, 9),
    _Sc2cssComponentServicePartId_Type()
)
sc2cssComponentServicePartId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssComponentServicePartId.setStatus("mandatory")
_Sc2cssTableSize_Type = Integer32
_Sc2cssTableSize_Object = MibScalar
sc2cssTableSize = _Sc2cssTableSize_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 8, 4),
    _Sc2cssTableSize_Type()
)
sc2cssTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2cssTableSize.setStatus("mandatory")
_Sc2Maintenance_ObjectIdentity = ObjectIdentity
sc2Maintenance = _Sc2Maintenance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9)
)
_Sc2MaintenanceObjectTable_Object = MibTable
sc2MaintenanceObjectTable = _Sc2MaintenanceObjectTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 1)
)
if mibBuilder.loadTexts:
    sc2MaintenanceObjectTable.setStatus("mandatory")
_Sc2MaintenanceObjects_Object = MibTableRow
sc2MaintenanceObjects = _Sc2MaintenanceObjects_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 1, 1)
)
sc2MaintenanceObjects.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2mtUnitId"),
)
if mibBuilder.loadTexts:
    sc2MaintenanceObjects.setStatus("mandatory")
_Sc2mtUnitId_Type = Integer32
_Sc2mtUnitId_Object = MibTableColumn
sc2mtUnitId = _Sc2mtUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 1, 1, 1),
    _Sc2mtUnitId_Type()
)
sc2mtUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2mtUnitId.setStatus("mandatory")
_Sc2ErrorCounterStartTime_Type = Integer32
_Sc2ErrorCounterStartTime_Object = MibTableColumn
sc2ErrorCounterStartTime = _Sc2ErrorCounterStartTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 1, 1, 2),
    _Sc2ErrorCounterStartTime_Type()
)
sc2ErrorCounterStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2ErrorCounterStartTime.setStatus("mandatory")
_Sc2SendTestTrap_Type = Integer32
_Sc2SendTestTrap_Object = MibTableColumn
sc2SendTestTrap = _Sc2SendTestTrap_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 1, 1, 3),
    _Sc2SendTestTrap_Type()
)
sc2SendTestTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2SendTestTrap.setStatus("mandatory")
_Sc2AddTrapDestination_Type = IpAddress
_Sc2AddTrapDestination_Object = MibTableColumn
sc2AddTrapDestination = _Sc2AddTrapDestination_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 1, 1, 4),
    _Sc2AddTrapDestination_Type()
)
sc2AddTrapDestination.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2AddTrapDestination.setStatus("mandatory")
_Sc2FirmwareVersionTable_Object = MibTable
sc2FirmwareVersionTable = _Sc2FirmwareVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 2)
)
if mibBuilder.loadTexts:
    sc2FirmwareVersionTable.setStatus("mandatory")
_Sc2FirmwareVersions_Object = MibTableRow
sc2FirmwareVersions = _Sc2FirmwareVersions_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 2, 1)
)
sc2FirmwareVersions.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2fwUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2fwType"),
)
if mibBuilder.loadTexts:
    sc2FirmwareVersions.setStatus("mandatory")
_Sc2fwUnitId_Type = Integer32
_Sc2fwUnitId_Object = MibTableColumn
sc2fwUnitId = _Sc2fwUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 2, 1, 1),
    _Sc2fwUnitId_Type()
)
sc2fwUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fwUnitId.setStatus("mandatory")


class _Sc2fwType_Type(Integer32):
    """Custom type sc2fwType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("bios", 1),
          ("management-controller", 2),
          ("remote-management-controller", 3))
    )


_Sc2fwType_Type.__name__ = "Integer32"
_Sc2fwType_Object = MibTableColumn
sc2fwType = _Sc2fwType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 2, 1, 2),
    _Sc2fwType_Type()
)
sc2fwType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fwType.setStatus("mandatory")
_Sc2fwModelName_Type = DisplayString
_Sc2fwModelName_Object = MibTableColumn
sc2fwModelName = _Sc2fwModelName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 2, 1, 3),
    _Sc2fwModelName_Type()
)
sc2fwModelName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fwModelName.setStatus("mandatory")
_Sc2fwVersion_Type = DisplayString
_Sc2fwVersion_Object = MibTableColumn
sc2fwVersion = _Sc2fwVersion_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 9, 2, 1, 4),
    _Sc2fwVersion_Type()
)
sc2fwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2fwVersion.setStatus("mandatory")
_Sc2Deployment_ObjectIdentity = ObjectIdentity
sc2Deployment = _Sc2Deployment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10)
)
_Sc2DeployInfoTable_Object = MibTable
sc2DeployInfoTable = _Sc2DeployInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1)
)
if mibBuilder.loadTexts:
    sc2DeployInfoTable.setStatus("mandatory")
_Sc2DeployInfo_Object = MibTableRow
sc2DeployInfo = _Sc2DeployInfo_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1)
)
sc2DeployInfo.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2dplInfoUnitId"),
)
if mibBuilder.loadTexts:
    sc2DeployInfo.setStatus("mandatory")
_Sc2dplInfoUnitId_Type = Integer32
_Sc2dplInfoUnitId_Object = MibTableColumn
sc2dplInfoUnitId = _Sc2dplInfoUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 1),
    _Sc2dplInfoUnitId_Type()
)
sc2dplInfoUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2dplInfoUnitId.setStatus("mandatory")
_Sc2DeployInfoChassisId_Type = DisplayString
_Sc2DeployInfoChassisId_Object = MibTableColumn
sc2DeployInfoChassisId = _Sc2DeployInfoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 2),
    _Sc2DeployInfoChassisId_Type()
)
sc2DeployInfoChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2DeployInfoChassisId.setStatus("mandatory")
_Sc2DeployInfoMacAddr1_Type = PhysAddress
_Sc2DeployInfoMacAddr1_Object = MibTableColumn
sc2DeployInfoMacAddr1 = _Sc2DeployInfoMacAddr1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 3),
    _Sc2DeployInfoMacAddr1_Type()
)
sc2DeployInfoMacAddr1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2DeployInfoMacAddr1.setStatus("mandatory")
_Sc2DeployInfoMacAddr2_Type = PhysAddress
_Sc2DeployInfoMacAddr2_Object = MibTableColumn
sc2DeployInfoMacAddr2 = _Sc2DeployInfoMacAddr2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 4),
    _Sc2DeployInfoMacAddr2_Type()
)
sc2DeployInfoMacAddr2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2DeployInfoMacAddr2.setStatus("mandatory")
_Sc2DeployInfoMacAddr3_Type = PhysAddress
_Sc2DeployInfoMacAddr3_Object = MibTableColumn
sc2DeployInfoMacAddr3 = _Sc2DeployInfoMacAddr3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 5),
    _Sc2DeployInfoMacAddr3_Type()
)
sc2DeployInfoMacAddr3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2DeployInfoMacAddr3.setStatus("mandatory")
_Sc2DeployInfoMacAddr4_Type = PhysAddress
_Sc2DeployInfoMacAddr4_Object = MibTableColumn
sc2DeployInfoMacAddr4 = _Sc2DeployInfoMacAddr4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 6),
    _Sc2DeployInfoMacAddr4_Type()
)
sc2DeployInfoMacAddr4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2DeployInfoMacAddr4.setStatus("mandatory")
_Sc2DeployInfoIpAddr1_Type = IpAddress
_Sc2DeployInfoIpAddr1_Object = MibTableColumn
sc2DeployInfoIpAddr1 = _Sc2DeployInfoIpAddr1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 7),
    _Sc2DeployInfoIpAddr1_Type()
)
sc2DeployInfoIpAddr1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoIpAddr1.setStatus("mandatory")
_Sc2DeployInfoIpAddr2_Type = IpAddress
_Sc2DeployInfoIpAddr2_Object = MibTableColumn
sc2DeployInfoIpAddr2 = _Sc2DeployInfoIpAddr2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 8),
    _Sc2DeployInfoIpAddr2_Type()
)
sc2DeployInfoIpAddr2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoIpAddr2.setStatus("mandatory")
_Sc2DeployInfoIpAddr3_Type = IpAddress
_Sc2DeployInfoIpAddr3_Object = MibTableColumn
sc2DeployInfoIpAddr3 = _Sc2DeployInfoIpAddr3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 9),
    _Sc2DeployInfoIpAddr3_Type()
)
sc2DeployInfoIpAddr3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoIpAddr3.setStatus("mandatory")
_Sc2DeployInfoIpAddr4_Type = IpAddress
_Sc2DeployInfoIpAddr4_Object = MibTableColumn
sc2DeployInfoIpAddr4 = _Sc2DeployInfoIpAddr4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 10),
    _Sc2DeployInfoIpAddr4_Type()
)
sc2DeployInfoIpAddr4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoIpAddr4.setStatus("mandatory")
_Sc2DeployInfoNetMask1_Type = IpAddress
_Sc2DeployInfoNetMask1_Object = MibTableColumn
sc2DeployInfoNetMask1 = _Sc2DeployInfoNetMask1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 11),
    _Sc2DeployInfoNetMask1_Type()
)
sc2DeployInfoNetMask1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoNetMask1.setStatus("mandatory")
_Sc2DeployInfoNetMask2_Type = IpAddress
_Sc2DeployInfoNetMask2_Object = MibTableColumn
sc2DeployInfoNetMask2 = _Sc2DeployInfoNetMask2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 12),
    _Sc2DeployInfoNetMask2_Type()
)
sc2DeployInfoNetMask2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoNetMask2.setStatus("mandatory")
_Sc2DeployInfoNetMask3_Type = IpAddress
_Sc2DeployInfoNetMask3_Object = MibTableColumn
sc2DeployInfoNetMask3 = _Sc2DeployInfoNetMask3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 13),
    _Sc2DeployInfoNetMask3_Type()
)
sc2DeployInfoNetMask3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoNetMask3.setStatus("mandatory")
_Sc2DeployInfoNetMask4_Type = IpAddress
_Sc2DeployInfoNetMask4_Object = MibTableColumn
sc2DeployInfoNetMask4 = _Sc2DeployInfoNetMask4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 14),
    _Sc2DeployInfoNetMask4_Type()
)
sc2DeployInfoNetMask4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoNetMask4.setStatus("mandatory")
_Sc2DeployInfoGateway1_Type = IpAddress
_Sc2DeployInfoGateway1_Object = MibTableColumn
sc2DeployInfoGateway1 = _Sc2DeployInfoGateway1_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 15),
    _Sc2DeployInfoGateway1_Type()
)
sc2DeployInfoGateway1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoGateway1.setStatus("mandatory")
_Sc2DeployInfoGateway2_Type = IpAddress
_Sc2DeployInfoGateway2_Object = MibTableColumn
sc2DeployInfoGateway2 = _Sc2DeployInfoGateway2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 16),
    _Sc2DeployInfoGateway2_Type()
)
sc2DeployInfoGateway2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoGateway2.setStatus("mandatory")
_Sc2DeployInfoGateway3_Type = IpAddress
_Sc2DeployInfoGateway3_Object = MibTableColumn
sc2DeployInfoGateway3 = _Sc2DeployInfoGateway3_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 17),
    _Sc2DeployInfoGateway3_Type()
)
sc2DeployInfoGateway3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoGateway3.setStatus("mandatory")
_Sc2DeployInfoGateway4_Type = IpAddress
_Sc2DeployInfoGateway4_Object = MibTableColumn
sc2DeployInfoGateway4 = _Sc2DeployInfoGateway4_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 18),
    _Sc2DeployInfoGateway4_Type()
)
sc2DeployInfoGateway4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoGateway4.setStatus("mandatory")
_Sc2DeployInfoHostname_Type = DisplayString
_Sc2DeployInfoHostname_Object = MibTableColumn
sc2DeployInfoHostname = _Sc2DeployInfoHostname_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 19),
    _Sc2DeployInfoHostname_Type()
)
sc2DeployInfoHostname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoHostname.setStatus("mandatory")
_Sc2DeployInfoMasterImageReference_Type = DisplayString
_Sc2DeployInfoMasterImageReference_Object = MibTableColumn
sc2DeployInfoMasterImageReference = _Sc2DeployInfoMasterImageReference_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 20),
    _Sc2DeployInfoMasterImageReference_Type()
)
sc2DeployInfoMasterImageReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoMasterImageReference.setStatus("mandatory")


class _Sc2DeployInfoStatusOfBlade_Type(Integer32):
    """Custom type sc2DeployInfoStatusOfBlade based on Integer32"""
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
        *(("unknown", 1),
          ("power-down", 2),
          ("standby", 3),
          ("system-boot-failure", 4),
          ("bios-setup", 5),
          ("booting", 6))
    )


_Sc2DeployInfoStatusOfBlade_Type.__name__ = "Integer32"
_Sc2DeployInfoStatusOfBlade_Object = MibTableColumn
sc2DeployInfoStatusOfBlade = _Sc2DeployInfoStatusOfBlade_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 21),
    _Sc2DeployInfoStatusOfBlade_Type()
)
sc2DeployInfoStatusOfBlade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoStatusOfBlade.setStatus("mandatory")


class _Sc2DeployInfoLanStatusOfSlot_Type(Integer32):
    """Custom type sc2DeployInfoLanStatusOfSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("false", 2),
          ("true", 3))
    )


_Sc2DeployInfoLanStatusOfSlot_Type.__name__ = "Integer32"
_Sc2DeployInfoLanStatusOfSlot_Object = MibTableColumn
sc2DeployInfoLanStatusOfSlot = _Sc2DeployInfoLanStatusOfSlot_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 22),
    _Sc2DeployInfoLanStatusOfSlot_Type()
)
sc2DeployInfoLanStatusOfSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoLanStatusOfSlot.setStatus("mandatory")


class _Sc2DeployInfoAutomaticRecovery_Type(Integer32):
    """Custom type sc2DeployInfoAutomaticRecovery based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("false", 2),
          ("true", 3))
    )


_Sc2DeployInfoAutomaticRecovery_Type.__name__ = "Integer32"
_Sc2DeployInfoAutomaticRecovery_Object = MibTableColumn
sc2DeployInfoAutomaticRecovery = _Sc2DeployInfoAutomaticRecovery_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 23),
    _Sc2DeployInfoAutomaticRecovery_Type()
)
sc2DeployInfoAutomaticRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoAutomaticRecovery.setStatus("mandatory")


class _Sc2DeployInfoStatusOfCloning_Type(Integer32):
    """Custom type sc2DeployInfoStatusOfCloning based on Integer32"""
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
        *(("unknown", 1),
          ("not-cloned", 2),
          ("cloning", 3),
          ("cloned", 4))
    )


_Sc2DeployInfoStatusOfCloning_Type.__name__ = "Integer32"
_Sc2DeployInfoStatusOfCloning_Object = MibTableColumn
sc2DeployInfoStatusOfCloning = _Sc2DeployInfoStatusOfCloning_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 24),
    _Sc2DeployInfoStatusOfCloning_Type()
)
sc2DeployInfoStatusOfCloning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoStatusOfCloning.setStatus("mandatory")


class _Sc2DeployInfoBootMode_Type(Integer32):
    """Custom type sc2DeployInfoBootMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("normal", 2),
          ("pxeBiosSetup", 3),
          ("pxeLan0", 4),
          ("pxeLan1", 5),
          ("pxeLan2", 6),
          ("pxeLan3", 7))
    )


_Sc2DeployInfoBootMode_Type.__name__ = "Integer32"
_Sc2DeployInfoBootMode_Object = MibTableColumn
sc2DeployInfoBootMode = _Sc2DeployInfoBootMode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 1, 1, 25),
    _Sc2DeployInfoBootMode_Type()
)
sc2DeployInfoBootMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2DeployInfoBootMode.setStatus("mandatory")
_Sc2OemDeployInfoTable_Object = MibTable
sc2OemDeployInfoTable = _Sc2OemDeployInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 2)
)
if mibBuilder.loadTexts:
    sc2OemDeployInfoTable.setStatus("mandatory")
_Sc2OemDeployInfo_Object = MibTableRow
sc2OemDeployInfo = _Sc2OemDeployInfo_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 2, 1)
)
sc2OemDeployInfo.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2odplInfoUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2odplParamId"),
)
if mibBuilder.loadTexts:
    sc2OemDeployInfo.setStatus("mandatory")
_Sc2odplInfoUnitId_Type = Integer32
_Sc2odplInfoUnitId_Object = MibTableColumn
sc2odplInfoUnitId = _Sc2odplInfoUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 2, 1, 1),
    _Sc2odplInfoUnitId_Type()
)
sc2odplInfoUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2odplInfoUnitId.setStatus("mandatory")
_Sc2odplParamId_Type = Integer32
_Sc2odplParamId_Object = MibTableColumn
sc2odplParamId = _Sc2odplParamId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 2, 1, 2),
    _Sc2odplParamId_Type()
)
sc2odplParamId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2odplParamId.setStatus("mandatory")
_Sc2OemDeployInfoParamData_Type = DisplayString
_Sc2OemDeployInfoParamData_Object = MibTableColumn
sc2OemDeployInfoParamData = _Sc2OemDeployInfoParamData_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 2, 1, 3),
    _Sc2OemDeployInfoParamData_Type()
)
sc2OemDeployInfoParamData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2OemDeployInfoParamData.setStatus("mandatory")
_Sc2DeployLanInterfaceTable_Object = MibTable
sc2DeployLanInterfaceTable = _Sc2DeployLanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 3)
)
if mibBuilder.loadTexts:
    sc2DeployLanInterfaceTable.setStatus("mandatory")
_Sc2DeployLanInterfaces_Object = MibTableRow
sc2DeployLanInterfaces = _Sc2DeployLanInterfaces_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 3, 1)
)
sc2DeployLanInterfaces.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2dplLanUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2dplLanInterfaceNr"),
)
if mibBuilder.loadTexts:
    sc2DeployLanInterfaces.setStatus("mandatory")
_Sc2dplLanUnitId_Type = Integer32
_Sc2dplLanUnitId_Object = MibTableColumn
sc2dplLanUnitId = _Sc2dplLanUnitId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 3, 1, 1),
    _Sc2dplLanUnitId_Type()
)
sc2dplLanUnitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2dplLanUnitId.setStatus("mandatory")
_Sc2dplLanInterfaceNr_Type = Integer32
_Sc2dplLanInterfaceNr_Object = MibTableColumn
sc2dplLanInterfaceNr = _Sc2dplLanInterfaceNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 3, 1, 2),
    _Sc2dplLanInterfaceNr_Type()
)
sc2dplLanInterfaceNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2dplLanInterfaceNr.setStatus("mandatory")
_Sc2dplLanMacAddress_Type = PhysAddress
_Sc2dplLanMacAddress_Object = MibTableColumn
sc2dplLanMacAddress = _Sc2dplLanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 10, 3, 1, 3),
    _Sc2dplLanMacAddress_Type()
)
sc2dplLanMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2dplLanMacAddress.setStatus("mandatory")
_Sc2DriverMonitoring_ObjectIdentity = ObjectIdentity
sc2DriverMonitoring = _Sc2DriverMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11)
)
_Sc2DriverMonitorComponentTable_Object = MibTable
sc2DriverMonitorComponentTable = _Sc2DriverMonitorComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1)
)
if mibBuilder.loadTexts:
    sc2DriverMonitorComponentTable.setStatus("mandatory")
_Sc2DriverMonitorComponents_Object = MibTableRow
sc2DriverMonitorComponents = _Sc2DriverMonitorComponents_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1)
)
sc2DriverMonitorComponents.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2uUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2drvmonCompClass"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2drvmonCompIndex"),
)
if mibBuilder.loadTexts:
    sc2DriverMonitorComponents.setStatus("mandatory")


class _Sc2drvmonCompClass_Type(Integer32):
    """Custom type sc2drvmonCompClass based on Integer32"""
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
        *(("other", 1),
          ("software", 2),
          ("network", 3),
          ("storage", 4))
    )


_Sc2drvmonCompClass_Type.__name__ = "Integer32"
_Sc2drvmonCompClass_Object = MibTableColumn
sc2drvmonCompClass = _Sc2drvmonCompClass_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1, 1),
    _Sc2drvmonCompClass_Type()
)
sc2drvmonCompClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonCompClass.setStatus("mandatory")
_Sc2drvmonCompIndex_Type = Integer32
_Sc2drvmonCompIndex_Object = MibTableColumn
sc2drvmonCompIndex = _Sc2drvmonCompIndex_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1, 2),
    _Sc2drvmonCompIndex_Type()
)
sc2drvmonCompIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonCompIndex.setStatus("mandatory")
_Sc2drvmonCompName_Type = DisplayString
_Sc2drvmonCompName_Object = MibTableColumn
sc2drvmonCompName = _Sc2drvmonCompName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1, 3),
    _Sc2drvmonCompName_Type()
)
sc2drvmonCompName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonCompName.setStatus("mandatory")


class _Sc2drvmonCompType_Type(Integer32):
    """Custom type sc2drvmonCompType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("pci", 2),
          ("usb", 3))
    )


_Sc2drvmonCompType_Type.__name__ = "Integer32"
_Sc2drvmonCompType_Object = MibTableColumn
sc2drvmonCompType = _Sc2drvmonCompType_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1, 4),
    _Sc2drvmonCompType_Type()
)
sc2drvmonCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonCompType.setStatus("mandatory")
_Sc2drvmonCompDriverName_Type = DisplayString
_Sc2drvmonCompDriverName_Object = MibTableColumn
sc2drvmonCompDriverName = _Sc2drvmonCompDriverName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1, 5),
    _Sc2drvmonCompDriverName_Type()
)
sc2drvmonCompDriverName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonCompDriverName.setStatus("mandatory")
_Sc2drvmonCompLocationDesignation_Type = DisplayString
_Sc2drvmonCompLocationDesignation_Object = MibTableColumn
sc2drvmonCompLocationDesignation = _Sc2drvmonCompLocationDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1, 6),
    _Sc2drvmonCompLocationDesignation_Type()
)
sc2drvmonCompLocationDesignation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonCompLocationDesignation.setStatus("mandatory")
_Sc2drvmonCompLocationKey_Type = DisplayString
_Sc2drvmonCompLocationKey_Object = MibTableColumn
sc2drvmonCompLocationKey = _Sc2drvmonCompLocationKey_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1, 7),
    _Sc2drvmonCompLocationKey_Type()
)
sc2drvmonCompLocationKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonCompLocationKey.setStatus("mandatory")
_Sc2drvmonCompStatus_Type = CompStatus
_Sc2drvmonCompStatus_Object = MibTableColumn
sc2drvmonCompStatus = _Sc2drvmonCompStatus_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1, 8),
    _Sc2drvmonCompStatus_Type()
)
sc2drvmonCompStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonCompStatus.setStatus("mandatory")
_Sc2drvmonCompErrorAcknowledge_Type = Integer32
_Sc2drvmonCompErrorAcknowledge_Object = MibTableColumn
sc2drvmonCompErrorAcknowledge = _Sc2drvmonCompErrorAcknowledge_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 1, 1, 9),
    _Sc2drvmonCompErrorAcknowledge_Type()
)
sc2drvmonCompErrorAcknowledge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sc2drvmonCompErrorAcknowledge.setStatus("mandatory")
_Sc2DriverMonitorMessageTable_Object = MibTable
sc2DriverMonitorMessageTable = _Sc2DriverMonitorMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2)
)
if mibBuilder.loadTexts:
    sc2DriverMonitorMessageTable.setStatus("mandatory")
_Sc2DriverMonitorMessages_Object = MibTableRow
sc2DriverMonitorMessages = _Sc2DriverMonitorMessages_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1)
)
sc2DriverMonitorMessages.setIndexNames(
    (0, "FSC-SERVERCONTROL2-MIB", "sc2uUnitId"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2msgTextLogLanguage"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2drvmonCompClass"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2drvmonCompIndex"),
    (0, "FSC-SERVERCONTROL2-MIB", "sc2msgTextLogSeqNr"),
)
if mibBuilder.loadTexts:
    sc2DriverMonitorMessages.setStatus("mandatory")
_Sc2drvmonMsgSeqNr_Type = Integer32
_Sc2drvmonMsgSeqNr_Object = MibTableColumn
sc2drvmonMsgSeqNr = _Sc2drvmonMsgSeqNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 1),
    _Sc2drvmonMsgSeqNr_Type()
)
sc2drvmonMsgSeqNr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonMsgSeqNr.setStatus("mandatory")
_Sc2drvmonMsgTimestamp_Type = Integer32
_Sc2drvmonMsgTimestamp_Object = MibTableColumn
sc2drvmonMsgTimestamp = _Sc2drvmonMsgTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 2),
    _Sc2drvmonMsgTimestamp_Type()
)
sc2drvmonMsgTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonMsgTimestamp.setStatus("mandatory")
_Sc2drvmonMsgMessage_Type = DisplayString
_Sc2drvmonMsgMessage_Object = MibTableColumn
sc2drvmonMsgMessage = _Sc2drvmonMsgMessage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 3),
    _Sc2drvmonMsgMessage_Type()
)
sc2drvmonMsgMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonMsgMessage.setStatus("mandatory")
_Sc2drvmonMsgEventId_Type = Integer32
_Sc2drvmonMsgEventId_Object = MibTableColumn
sc2drvmonMsgEventId = _Sc2drvmonMsgEventId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 4),
    _Sc2drvmonMsgEventId_Type()
)
sc2drvmonMsgEventId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonMsgEventId.setStatus("mandatory")
_Sc2drvmonMsgSeverity_Type = OsLogSeverity
_Sc2drvmonMsgSeverity_Object = MibTableColumn
sc2drvmonMsgSeverity = _Sc2drvmonMsgSeverity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 5),
    _Sc2drvmonMsgSeverity_Type()
)
sc2drvmonMsgSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonMsgSeverity.setStatus("mandatory")
_Sc2drvmonMsgErrorCode_Type = Integer32
_Sc2drvmonMsgErrorCode_Object = MibTableColumn
sc2drvmonMsgErrorCode = _Sc2drvmonMsgErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 6),
    _Sc2drvmonMsgErrorCode_Type()
)
sc2drvmonMsgErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonMsgErrorCode.setStatus("mandatory")
_Sc2drvmonOrigLogMessage_Type = DisplayString
_Sc2drvmonOrigLogMessage_Object = MibTableColumn
sc2drvmonOrigLogMessage = _Sc2drvmonOrigLogMessage_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 7),
    _Sc2drvmonOrigLogMessage_Type()
)
sc2drvmonOrigLogMessage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonOrigLogMessage.setStatus("mandatory")
_Sc2drvmonOrigLogSource_Type = DisplayString
_Sc2drvmonOrigLogSource_Object = MibTableColumn
sc2drvmonOrigLogSource = _Sc2drvmonOrigLogSource_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 8),
    _Sc2drvmonOrigLogSource_Type()
)
sc2drvmonOrigLogSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonOrigLogSource.setStatus("mandatory")
_Sc2drvmonOrigLogId_Type = Integer32
_Sc2drvmonOrigLogId_Object = MibTableColumn
sc2drvmonOrigLogId = _Sc2drvmonOrigLogId_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 9),
    _Sc2drvmonOrigLogId_Type()
)
sc2drvmonOrigLogId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonOrigLogId.setStatus("mandatory")
_Sc2drvmonOrigLogSeverity_Type = OsLogSeverity
_Sc2drvmonOrigLogSeverity_Object = MibTableColumn
sc2drvmonOrigLogSeverity = _Sc2drvmonOrigLogSeverity_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 2, 1, 10),
    _Sc2drvmonOrigLogSeverity_Type()
)
sc2drvmonOrigLogSeverity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonOrigLogSeverity.setStatus("mandatory")
_Sc2drvmonTableUpdateCount_Type = Counter32
_Sc2drvmonTableUpdateCount_Object = MibScalar
sc2drvmonTableUpdateCount = _Sc2drvmonTableUpdateCount_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 11, 3),
    _Sc2drvmonTableUpdateCount_Type()
)
sc2drvmonTableUpdateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sc2drvmonTableUpdateCount.setStatus("mandatory")
_Sc2Notifications_ObjectIdentity = ObjectIdentity
sc2Notifications = _Sc2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20)
)
_Sc2NotificationsTrapInfo_ObjectIdentity = ObjectIdentity
sc2NotificationsTrapInfo = _Sc2NotificationsTrapInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 1)
)
_Sc2TrapInfoServerName_Type = DisplayString
_Sc2TrapInfoServerName_Object = MibScalar
sc2TrapInfoServerName = _Sc2TrapInfoServerName_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 1, 1),
    _Sc2TrapInfoServerName_Type()
)
sc2TrapInfoServerName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sc2TrapInfoServerName.setStatus("mandatory")
_Sc2TrapInfoTime_Type = Integer32
_Sc2TrapInfoTime_Object = MibScalar
sc2TrapInfoTime = _Sc2TrapInfoTime_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 1, 2),
    _Sc2TrapInfoTime_Type()
)
sc2TrapInfoTime.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sc2TrapInfoTime.setStatus("mandatory")
_Sc2TrapInfoCabinetNr_Type = Integer32
_Sc2TrapInfoCabinetNr_Object = MibScalar
sc2TrapInfoCabinetNr = _Sc2TrapInfoCabinetNr_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 1, 3),
    _Sc2TrapInfoCabinetNr_Type()
)
sc2TrapInfoCabinetNr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sc2TrapInfoCabinetNr.setStatus("mandatory")
_Sc2TrapInfoObjectDesignation_Type = DisplayString
_Sc2TrapInfoObjectDesignation_Object = MibScalar
sc2TrapInfoObjectDesignation = _Sc2TrapInfoObjectDesignation_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 1, 4),
    _Sc2TrapInfoObjectDesignation_Type()
)
sc2TrapInfoObjectDesignation.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sc2TrapInfoObjectDesignation.setStatus("mandatory")
_Sc2TrapInfoString_Type = DisplayString
_Sc2TrapInfoString_Object = MibScalar
sc2TrapInfoString = _Sc2TrapInfoString_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 1, 5),
    _Sc2TrapInfoString_Type()
)
sc2TrapInfoString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sc2TrapInfoString.setStatus("mandatory")
_Sc2TrapInfoInteger_Type = Integer32
_Sc2TrapInfoInteger_Object = MibScalar
sc2TrapInfoInteger = _Sc2TrapInfoInteger_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 1, 6),
    _Sc2TrapInfoInteger_Type()
)
sc2TrapInfoInteger.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sc2TrapInfoInteger.setStatus("mandatory")
_Sc2TrapInfoInteger2_Type = Integer32
_Sc2TrapInfoInteger2_Object = MibScalar
sc2TrapInfoInteger2 = _Sc2TrapInfoInteger2_Object(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 1, 7),
    _Sc2TrapInfoInteger2_Type()
)
sc2TrapInfoInteger2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sc2TrapInfoInteger2.setStatus("mandatory")

# Managed Objects groups


# Notification objects

sc2TrapTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2000)
)
sc2TrapTest.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapTest.setStatus(
        ""
    )

sc2TrapCommunicationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2001)
)
sc2TrapCommunicationFailure.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapCommunicationFailure.setStatus(
        ""
    )

sc2TrapCommunicationEstablished = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2002)
)
sc2TrapCommunicationEstablished.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapCommunicationEstablished.setStatus(
        ""
    )

sc2TrapControllerSelftestWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2003)
)
sc2TrapControllerSelftestWarning.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapControllerSelftestWarning.setStatus(
        ""
    )

sc2TrapControllerSelftestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2004)
)
sc2TrapControllerSelftestError.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapControllerSelftestError.setStatus(
        ""
    )

sc2TrapBiosSelftestError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2005)
)
sc2TrapBiosSelftestError.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapBiosSelftestError.setStatus(
        ""
    )

sc2TrapSevereSystemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2006)
)
sc2TrapSevereSystemError.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapSevereSystemError.setStatus(
        ""
    )

sc2TrapFanAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2010)
)
sc2TrapFanAdded.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapFanAdded.setStatus(
        ""
    )

sc2TrapFanRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2011)
)
sc2TrapFanRemoved.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapFanRemoved.setStatus(
        ""
    )

sc2TrapFanOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2012)
)
sc2TrapFanOk.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapFanOk.setStatus(
        ""
    )

sc2TrapFanCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2013)
)
sc2TrapFanCritical.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapFanCritical.setStatus(
        ""
    )

sc2TrapFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2014)
)
sc2TrapFanFailed.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapFanFailed.setStatus(
        ""
    )

sc2TrapRedundantFanFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2015)
)
sc2TrapRedundantFanFailed.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapRedundantFanFailed.setStatus(
        ""
    )

sc2TrapTempOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2020)
)
sc2TrapTempOk.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapTempOk.setStatus(
        ""
    )

sc2TrapTempWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2021)
)
sc2TrapTempWarning.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapTempWarning.setStatus(
        ""
    )

sc2TrapTempCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2022)
)
sc2TrapTempCritical.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapTempCritical.setStatus(
        ""
    )

sc2TrapTempSensorOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2023)
)
sc2TrapTempSensorOk.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapTempSensorOk.setStatus(
        ""
    )

sc2TrapTempSensorBroken = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2024)
)
sc2TrapTempSensorBroken.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapTempSensorBroken.setStatus(
        ""
    )

sc2TrapPowerSupplyAdded = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2030)
)
sc2TrapPowerSupplyAdded.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerSupplyAdded.setStatus(
        ""
    )

sc2TrapPowerSupplyRemoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2031)
)
sc2TrapPowerSupplyRemoved.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerSupplyRemoved.setStatus(
        ""
    )

sc2TrapPowerSupplyOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2032)
)
sc2TrapPowerSupplyOk.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerSupplyOk.setStatus(
        ""
    )

sc2TrapPowerSupplyCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2033)
)
sc2TrapPowerSupplyCritical.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerSupplyCritical.setStatus(
        ""
    )

sc2TrapPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2034)
)
sc2TrapPowerSupplyFailed.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerSupplyFailed.setStatus(
        ""
    )

sc2TrapRedundantPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2035)
)
sc2TrapRedundantPowerSupplyFailed.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapRedundantPowerSupplyFailed.setStatus(
        ""
    )

sc2TrapPowerSupplyRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2036)
)
sc2TrapPowerSupplyRedundancyLost.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerSupplyRedundancyLost.setStatus(
        ""
    )

sc2TrapPowerSupplyCriticalTemperature = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2037)
)
sc2TrapPowerSupplyCriticalTemperature.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerSupplyCriticalTemperature.setStatus(
        ""
    )

sc2TrapPowerSupplyFanFailurePrediction = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2038)
)
sc2TrapPowerSupplyFanFailurePrediction.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerSupplyFanFailurePrediction.setStatus(
        ""
    )

sc2TrapPowerSupplyFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2039)
)
sc2TrapPowerSupplyFanFailure.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerSupplyFanFailure.setStatus(
        ""
    )

sc2TrapAcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2040)
)
sc2TrapAcFail.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapAcFail.setStatus(
        ""
    )

sc2TrapDcFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2041)
)
sc2TrapDcFail.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapDcFail.setStatus(
        ""
    )

sc2TrapOnBattery = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2042)
)
sc2TrapOnBattery.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoInteger"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoInteger2"))
)
if mibBuilder.loadTexts:
    sc2TrapOnBattery.setStatus(
        ""
    )

sc2TrapOnMains = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2043)
)
sc2TrapOnMains.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapOnMains.setStatus(
        ""
    )

sc2TrapVoltageOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2050)
)
sc2TrapVoltageOk.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapVoltageOk.setStatus(
        ""
    )

sc2TrapVoltageTooLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2051)
)
sc2TrapVoltageTooLow.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapVoltageTooLow.setStatus(
        ""
    )

sc2TrapVoltageTooHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2052)
)
sc2TrapVoltageTooHigh.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapVoltageTooHigh.setStatus(
        ""
    )

sc2TrapVoltageFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2053)
)
sc2TrapVoltageFailed.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapVoltageFailed.setStatus(
        ""
    )

sc2TrapBatteryVoltagePrefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2054)
)
sc2TrapBatteryVoltagePrefail.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapBatteryVoltagePrefail.setStatus(
        ""
    )

sc2TrapCorrectableMemErrorAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2060)
)
sc2TrapCorrectableMemErrorAddr.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoInteger"))
)
if mibBuilder.loadTexts:
    sc2TrapCorrectableMemErrorAddr.setStatus(
        ""
    )

sc2TrapUncorrectableMemErrorAddr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2061)
)
sc2TrapUncorrectableMemErrorAddr.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoInteger"))
)
if mibBuilder.loadTexts:
    sc2TrapUncorrectableMemErrorAddr.setStatus(
        ""
    )

sc2TrapCorrectableMemErrorBank = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2062)
)
sc2TrapCorrectableMemErrorBank.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapCorrectableMemErrorBank.setStatus(
        ""
    )

sc2TrapUncorrectableMemErrorBank = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2063)
)
sc2TrapUncorrectableMemErrorBank.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapUncorrectableMemErrorBank.setStatus(
        ""
    )

sc2TrapCorrectableMemErrorModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2064)
)
sc2TrapCorrectableMemErrorModule.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapCorrectableMemErrorModule.setStatus(
        ""
    )

sc2TrapUncorrectableMemErrorModule = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2065)
)
sc2TrapUncorrectableMemErrorModule.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapUncorrectableMemErrorModule.setStatus(
        ""
    )

sc2TrapCorrectableMemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2066)
)
sc2TrapCorrectableMemError.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapCorrectableMemError.setStatus(
        ""
    )

sc2TrapUncorrectableMemError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2067)
)
sc2TrapUncorrectableMemError.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapUncorrectableMemError.setStatus(
        ""
    )

sc2TrapMemErrorModulePrefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2068)
)
sc2TrapMemErrorModulePrefail.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapMemErrorModulePrefail.setStatus(
        ""
    )

sc2TrapMemErrorModuleFailing = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2069)
)
sc2TrapMemErrorModuleFailing.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapMemErrorModuleFailing.setStatus(
        ""
    )

sc2TrapMemErrorModuleReplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2070)
)
sc2TrapMemErrorModuleReplaced.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapMemErrorModuleReplaced.setStatus(
        ""
    )

sc2TrapMemErrorLoggingDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2071)
)
sc2TrapMemErrorLoggingDisabled.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapMemErrorLoggingDisabled.setStatus(
        ""
    )

sc2TrapMemErrorLoggingEnabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2072)
)
sc2TrapMemErrorLoggingEnabled.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapMemErrorLoggingEnabled.setStatus(
        ""
    )

sc2TrapMemErrorAnyModuleReplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2073)
)
sc2TrapMemErrorAnyModuleReplaced.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapMemErrorAnyModuleReplaced.setStatus(
        ""
    )

sc2TrapMemErrorRedundancyLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2074)
)
sc2TrapMemErrorRedundancyLost.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapMemErrorRedundancyLost.setStatus(
        ""
    )

sc2TrapMemNVDIMMLifetime = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2075)
)
sc2TrapMemNVDIMMLifetime.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoInteger"))
)
if mibBuilder.loadTexts:
    sc2TrapMemNVDIMMLifetime.setStatus(
        ""
    )

sc2TrapCpuSpeedChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2080)
)
sc2TrapCpuSpeedChanged.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoInteger"))
)
if mibBuilder.loadTexts:
    sc2TrapCpuSpeedChanged.setStatus(
        ""
    )

sc2TrapCpuPrefail = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2081)
)
sc2TrapCpuPrefail.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapCpuPrefail.setStatus(
        ""
    )

sc2TrapCpuIerr = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2082)
)
sc2TrapCpuIerr.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapCpuIerr.setStatus(
        ""
    )

sc2TrapCpuDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2083)
)
sc2TrapCpuDisabled.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapCpuDisabled.setStatus(
        ""
    )

sc2TrapCabinetSwitchedOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2090)
)
sc2TrapCabinetSwitchedOff.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoString"))
)
if mibBuilder.loadTexts:
    sc2TrapCabinetSwitchedOff.setStatus(
        ""
    )

sc2TrapCabinetSwitchedOn = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2091)
)
sc2TrapCabinetSwitchedOn.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoString"))
)
if mibBuilder.loadTexts:
    sc2TrapCabinetSwitchedOn.setStatus(
        ""
    )

sc2TrapPowerOffTimeReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2092)
)
sc2TrapPowerOffTimeReached.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoInteger"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerOffTimeReached.setStatus(
        ""
    )

sc2TrapServerShutdown = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2093)
)
sc2TrapServerShutdown.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoString"))
)
if mibBuilder.loadTexts:
    sc2TrapServerShutdown.setStatus(
        ""
    )

sc2TrapShutdownCancelled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2094)
)
sc2TrapShutdownCancelled.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapShutdownCancelled.setStatus(
        ""
    )

sc2TrapBootRetryCountZero = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2095)
)
sc2TrapBootRetryCountZero.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapBootRetryCountZero.setStatus(
        ""
    )

sc2TrapServerBoot = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2096)
)
sc2TrapServerBoot.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapServerBoot.setStatus(
        ""
    )

sc2TrapServerStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2097)
)
sc2TrapServerStandby.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapServerStandby.setStatus(
        ""
    )

sc2TrapServerSuspend = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2098)
)
sc2TrapServerSuspend.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapServerSuspend.setStatus(
        ""
    )

sc2TrapServerResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2099)
)
sc2TrapServerResumed.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapServerResumed.setStatus(
        ""
    )

sc2TrapMessageLogFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2100)
)
sc2TrapMessageLogFull.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapMessageLogFull.setStatus(
        ""
    )

sc2TrapMessageLogWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2101)
)
sc2TrapMessageLogWarning.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoInteger"))
)
if mibBuilder.loadTexts:
    sc2TrapMessageLogWarning.setStatus(
        ""
    )

sc2TrapBootMessageLogEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2102)
)
sc2TrapBootMessageLogEntry.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapBootMessageLogEntry.setStatus(
        ""
    )

sc2TrapIntrusionAssertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2110)
)
sc2TrapIntrusionAssertion.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapIntrusionAssertion.setStatus(
        ""
    )

sc2TrapIntrusionDeassertion = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2111)
)
sc2TrapIntrusionDeassertion.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapIntrusionDeassertion.setStatus(
        ""
    )

sc2TrapIntrusionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2112)
)
sc2TrapIntrusionChanged.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapIntrusionChanged.setStatus(
        ""
    )

sc2TrapPciBusError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2113)
)
sc2TrapPciBusError.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapPciBusError.setStatus(
        ""
    )

sc2TrapPowerOnTimeReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2114)
)
sc2TrapPowerOnTimeReached.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoInteger"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerOnTimeReached.setStatus(
        ""
    )

sc2TrapCssWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2120)
)
sc2TrapCssWarning.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapCssWarning.setStatus(
        ""
    )

sc2TrapCssFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2121)
)
sc2TrapCssFail.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapCssFail.setStatus(
        ""
    )

sc2TrapCssWarningServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2122)
)
sc2TrapCssWarningServer.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapCssWarningServer.setStatus(
        ""
    )

sc2TrapCssFailServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2123)
)
sc2TrapCssFailServer.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoObjectDesignation"))
)
if mibBuilder.loadTexts:
    sc2TrapCssFailServer.setStatus(
        ""
    )

sc2TrapPowerLimitOk = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2130)
)
sc2TrapPowerLimitOk.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerLimitOk.setStatus(
        ""
    )

sc2TrapPowerLimitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2131)
)
sc2TrapPowerLimitWarning.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerLimitWarning.setStatus(
        ""
    )

sc2TrapPowerLimitCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2132)
)
sc2TrapPowerLimitCritical.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerLimitCritical.setStatus(
        ""
    )

sc2TrapPowerLimitDisabled = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2133)
)
sc2TrapPowerLimitDisabled.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoCabinetNr"))
)
if mibBuilder.loadTexts:
    sc2TrapPowerLimitDisabled.setStatus(
        ""
    )

sc2TrapViomInitiateCommunication = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2140)
)
sc2TrapViomInitiateCommunication.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapViomInitiateCommunication.setStatus(
        ""
    )

sc2TrapViomStatusChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2141)
)
sc2TrapViomStatusChanged.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"))
)
if mibBuilder.loadTexts:
    sc2TrapViomStatusChanged.setStatus(
        ""
    )

sc2TrapDrvMonEventMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2150)
)
sc2TrapDrvMonEventMessage.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoString"))
)
if mibBuilder.loadTexts:
    sc2TrapDrvMonEventMessage.setStatus(
        ""
    )

sc2TrapDrvMonEventWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2151)
)
sc2TrapDrvMonEventWarning.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoString"))
)
if mibBuilder.loadTexts:
    sc2TrapDrvMonEventWarning.setStatus(
        ""
    )

sc2TrapDrvMonEventError = NotificationType(
    (1, 3, 6, 1, 4, 1, 231, 2, 10, 2, 2, 10, 20, 0, 2152)
)
sc2TrapDrvMonEventError.setObjects(
      *(("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoServerName"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoTime"),
        ("FSC-SERVERCONTROL2-MIB", "sc2TrapInfoString"))
)
if mibBuilder.loadTexts:
    sc2TrapDrvMonEventError.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FSC-SERVERCONTROL2-MIB",
    **{"PhysAddress": PhysAddress,
       "TrueFalse": TrueFalse,
       "TrueFalseUnknown": TrueFalseUnknown,
       "UnitClass": UnitClass,
       "CompStatus": CompStatus,
       "LogSeverity": LogSeverity,
       "OsLogSeverity": OsLogSeverity,
       "enterprises": enterprises,
       "sni": sni,
       "sniProductMibs": sniProductMibs,
       "sniExtensions": sniExtensions,
       "sniServerMgmt": sniServerMgmt,
       "sniInventory": sniInventory,
       "sniCommon": sniCommon,
       "fscServerControl2": fscServerControl2,
       "sc2AgentInfo": sc2AgentInfo,
       "sc2AgentId": sc2AgentId,
       "sc2AgentCompany": sc2AgentCompany,
       "sc2AgentVersion": sc2AgentVersion,
       "sc2AgentBuild": sc2AgentBuild,
       "sc2AgentWriteAllowed": sc2AgentWriteAllowed,
       "sc2AgentShutdownAllowed": sc2AgentShutdownAllowed,
       "sc2UnitInformation": sc2UnitInformation,
       "sc2LocalServerUnitId": sc2LocalServerUnitId,
       "sc2NumberUnits": sc2NumberUnits,
       "sc2UnitTable": sc2UnitTable,
       "sc2Units": sc2Units,
       "sc2uUnitId": sc2uUnitId,
       "sc2UnitClass": sc2UnitClass,
       "sc2UnitCabinetNr": sc2UnitCabinetNr,
       "sc2UnitDesignation": sc2UnitDesignation,
       "sc2UnitModelName": sc2UnitModelName,
       "sc2UnitManufacturer": sc2UnitManufacturer,
       "sc2UnitSerialNumber": sc2UnitSerialNumber,
       "sc2UnitLocation": sc2UnitLocation,
       "sc2UnitContact": sc2UnitContact,
       "sc2UnitAdminURL": sc2UnitAdminURL,
       "sc2FrontDoorStatus": sc2FrontDoorStatus,
       "sc2HousingOpenStatus": sc2HousingOpenStatus,
       "sc2MsgLogLanguages": sc2MsgLogLanguages,
       "sc2UnitWorldWideName": sc2UnitWorldWideName,
       "sc2RemcsId": sc2RemcsId,
       "sc2AssetTag": sc2AssetTag,
       "sc2MsgLogAvailable": sc2MsgLogAvailable,
       "sc2ManagementIpAddress": sc2ManagementIpAddress,
       "sc2HasUefiFirmware": sc2HasUefiFirmware,
       "sc2ManagementIpAddressV6": sc2ManagementIpAddressV6,
       "sc2UnitTableUpdateCount": sc2UnitTableUpdateCount,
       "sc2UnitParentTable": sc2UnitParentTable,
       "sc2UnitParents": sc2UnitParents,
       "sc2pUnitId": sc2pUnitId,
       "sc2ParentUnit": sc2ParentUnit,
       "sc2ParentUnitClass": sc2ParentUnitClass,
       "sc2UnitChildTable": sc2UnitChildTable,
       "sc2UnitChilds": sc2UnitChilds,
       "sc2cUnitId": sc2cUnitId,
       "sc2cChildNr": sc2cChildNr,
       "sc2ChildUnit": sc2ChildUnit,
       "sc2ChildUnitClass": sc2ChildUnitClass,
       "sc2Management": sc2Management,
       "sc2ManagementNodeTable": sc2ManagementNodeTable,
       "sc2ManagementNodes": sc2ManagementNodes,
       "sc2mnUnitId": sc2mnUnitId,
       "sc2mnNodeNr": sc2mnNodeNr,
       "sc2UnitNodeIfType": sc2UnitNodeIfType,
       "sc2UnitNodeAddress": sc2UnitNodeAddress,
       "sc2UnitNodeIpNetmask": sc2UnitNodeIpNetmask,
       "sc2UnitNodeGateway": sc2UnitNodeGateway,
       "sc2UnitNodeName": sc2UnitNodeName,
       "sc2UnitNodeClass": sc2UnitNodeClass,
       "sc2UnitNodeMacAddress": sc2UnitNodeMacAddress,
       "sc2UnitNodeUseDHCP": sc2UnitNodeUseDHCP,
       "sc2UnitNodeControllerType": sc2UnitNodeControllerType,
       "sc2UnitNodeControllerModel": sc2UnitNodeControllerModel,
       "sc2UnitNodeControllerFWVersion": sc2UnitNodeControllerFWVersion,
       "sc2UnitNodeControllerStorage": sc2UnitNodeControllerStorage,
       "sc2UnitNodeSNMPEnabled": sc2UnitNodeSNMPEnabled,
       "sc2UnitNodeCIMEnabled": sc2UnitNodeCIMEnabled,
       "sc2UnitNodeRemoteIPMIEnabled": sc2UnitNodeRemoteIPMIEnabled,
       "sc2NodeTableUpdateCount": sc2NodeTableUpdateCount,
       "sc2ManagementChannelType": sc2ManagementChannelType,
       "sc2ManagementProcessorTable": sc2ManagementProcessorTable,
       "sc2ManagementProcessors": sc2ManagementProcessors,
       "sc2spUnitId": sc2spUnitId,
       "sc2spProcessorNr": sc2spProcessorNr,
       "sc2spModelName": sc2spModelName,
       "sc2spFirmwareVersion": sc2spFirmwareVersion,
       "sc2spBatteryStatus": sc2spBatteryStatus,
       "sc2spBatteryDischargeTime": sc2spBatteryDischargeTime,
       "sc2spTimeOnBattery": sc2spTimeOnBattery,
       "sc2spDoBatteryChargeCycle": sc2spDoBatteryChargeCycle,
       "sc2spBatteryChargeLevel": sc2spBatteryChargeLevel,
       "sc2ManagedUpsNodeTable": sc2ManagedUpsNodeTable,
       "sc2ManagedUpsNodes": sc2ManagedUpsNodes,
       "sc2upsUnitId": sc2upsUnitId,
       "sc2upsNr": sc2upsNr,
       "sc2upsVendorName": sc2upsVendorName,
       "sc2upsModelName": sc2upsModelName,
       "sc2upsMgmtAddress": sc2upsMgmtAddress,
       "sc2upsMibRoot": sc2upsMibRoot,
       "sc2upsSnmpCommunity": sc2upsSnmpCommunity,
       "sc2UpsNodeTableUpdateCount": sc2UpsNodeTableUpdateCount,
       "sc2ServerInformation": sc2ServerInformation,
       "sc2ServerTable": sc2ServerTable,
       "sc2Servers": sc2Servers,
       "sc2srvUnitId": sc2srvUnitId,
       "sc2srvPhysicalMemory": sc2srvPhysicalMemory,
       "sc2srvLastBootResult": sc2srvLastBootResult,
       "sc2srvCurrentBootStatus": sc2srvCurrentBootStatus,
       "sc2srvShutdownCommand": sc2srvShutdownCommand,
       "sc2srvShutdownDelay": sc2srvShutdownDelay,
       "sc2srvUUID": sc2srvUUID,
       "sc2srvPhysicalMemoryOs": sc2srvPhysicalMemoryOs,
       "sc2srvUUIDWireFormat": sc2srvUUIDWireFormat,
       "sc2srvOsPlatform": sc2srvOsPlatform,
       "sc2srvBiosVersion": sc2srvBiosVersion,
       "sc2srvHasEncryptedPartitions": sc2srvHasEncryptedPartitions,
       "sc2srvTrustedExecutionTechnologyEnabled": sc2srvTrustedExecutionTechnologyEnabled,
       "sc2UnitPowerOnOffTable": sc2UnitPowerOnOffTable,
       "sc2UnitPowerOnOff": sc2UnitPowerOnOff,
       "sc2ooUnitId": sc2ooUnitId,
       "sc2PowerOnOffStatus": sc2PowerOnOffStatus,
       "sc2LastPowerOffSource": sc2LastPowerOffSource,
       "sc2LastPowerOnSource": sc2LastPowerOnSource,
       "sc2LastPowerOnTime": sc2LastPowerOnTime,
       "sc2PowerOnCounts": sc2PowerOnCounts,
       "sc2PowerOnDuration": sc2PowerOnDuration,
       "sc2PowerOffDuration": sc2PowerOffDuration,
       "sc2PowerFailRecovery": sc2PowerFailRecovery,
       "sc2PowerCommand": sc2PowerCommand,
       "sc2PowerSupplyRedundancy": sc2PowerSupplyRedundancy,
       "sc2PowerSupplyMatchStatus": sc2PowerSupplyMatchStatus,
       "sc2PerformanceTable": sc2PerformanceTable,
       "sc2Performance": sc2Performance,
       "sc2perfUnitId": sc2perfUnitId,
       "sc2perfNr": sc2perfNr,
       "sc2PerformanceType": sc2PerformanceType,
       "sc2PerformanceObjectNr": sc2PerformanceObjectNr,
       "sc2PerformanceName": sc2PerformanceName,
       "sc2PerformanceValue": sc2PerformanceValue,
       "sc2TimerOnOffTable": sc2TimerOnOffTable,
       "sc2TimerOnOff": sc2TimerOnOff,
       "sc2tooUnitId": sc2tooUnitId,
       "sc2tooDayOfWeek": sc2tooDayOfWeek,
       "sc2OnTime": sc2OnTime,
       "sc2OffTime": sc2OffTime,
       "sc2PowerMonitoringTable": sc2PowerMonitoringTable,
       "sc2PowerMonitoring": sc2PowerMonitoring,
       "sc2pmUnitId": sc2pmUnitId,
       "sc2pmCurrentPowerMonitoringAvailable": sc2pmCurrentPowerMonitoringAvailable,
       "sc2pmCurrentPowerMonitoringEnabled": sc2pmCurrentPowerMonitoringEnabled,
       "sc2pmNominalPowerConsumption": sc2pmNominalPowerConsumption,
       "sc2pmCurrentPowerConsumption": sc2pmCurrentPowerConsumption,
       "sc2pmCurrentPowerControl": sc2pmCurrentPowerControl,
       "sc2pmPowerLimitStatus": sc2pmPowerLimitStatus,
       "sc2pmPowerLimitThreshold": sc2pmPowerLimitThreshold,
       "sc2pmPowerLimitWarning": sc2pmPowerLimitWarning,
       "sc2pmRedundancyCritLevel": sc2pmRedundancyCritLevel,
       "sc2pmPowerControlMode": sc2pmPowerControlMode,
       "sc2pmPowerDisplayUnit": sc2pmPowerDisplayUnit,
       "sc2UtilizationHistoryTable": sc2UtilizationHistoryTable,
       "sc2UtilizationHistory": sc2UtilizationHistory,
       "sc2uthUnitId": sc2uthUnitId,
       "sc2uthEntity": sc2uthEntity,
       "sc2uthTimeStamp": sc2uthTimeStamp,
       "sc2uthHardwareUUID": sc2uthHardwareUUID,
       "sc2uthAverageValue": sc2uthAverageValue,
       "sc2uthMinValue": sc2uthMinValue,
       "sc2uthMaxValue": sc2uthMaxValue,
       "sc2PowerSourceInformationTable": sc2PowerSourceInformationTable,
       "sc2PowerSourceInformation": sc2PowerSourceInformation,
       "sc2psiUnitId": sc2psiUnitId,
       "sc2psiPowerSourceType": sc2psiPowerSourceType,
       "sc2psiPowerSourcePhase": sc2psiPowerSourcePhase,
       "sc2psiPowerSourceVoltage": sc2psiPowerSourceVoltage,
       "sc2VirtualIoManagerTable": sc2VirtualIoManagerTable,
       "sc2VirtualIoManager": sc2VirtualIoManager,
       "sc2viomUnitId": sc2viomUnitId,
       "sc2viomCurrentManagerId": sc2viomCurrentManagerId,
       "sc2viomEnabled": sc2viomEnabled,
       "sc2viomBiosSupport": sc2viomBiosSupport,
       "sc2viomConnectionStatus": sc2viomConnectionStatus,
       "sc2PowerSupplyRedundancyConfigurationTable": sc2PowerSupplyRedundancyConfigurationTable,
       "sc2PowerSupplyRedundancyConfiguration": sc2PowerSupplyRedundancyConfiguration,
       "sc2PSRedUnitId": sc2PSRedUnitId,
       "sc2PSRedundancyMode": sc2PSRedundancyMode,
       "sc2PSRedundancyModeConfig": sc2PSRedundancyModeConfig,
       "sc2PSRedundancyRequiredPowerSupplies": sc2PSRedundancyRequiredPowerSupplies,
       "sc2PSRedundancyPopulatedPowerSupplies": sc2PSRedundancyPopulatedPowerSupplies,
       "sc2PSRedundancyConfigurationStatus": sc2PSRedundancyConfigurationStatus,
       "sc2PSRedundancyThresholdStatus": sc2PSRedundancyThresholdStatus,
       "sc2PSRedundancyStatus": sc2PSRedundancyStatus,
       "sc2PerformanceValueTable": sc2PerformanceValueTable,
       "sc2PerformanceValues": sc2PerformanceValues,
       "sc2PerfValUnitId": sc2PerfValUnitId,
       "sc2PerfValType": sc2PerfValType,
       "sc2PerfValObjectNr": sc2PerfValObjectNr,
       "sc2PerfValName": sc2PerfValName,
       "sc2PerfValCurrentValue": sc2PerfValCurrentValue,
       "sc2Environment": sc2Environment,
       "sc2TemperatureSensorTable": sc2TemperatureSensorTable,
       "sc2TemperatureSensors": sc2TemperatureSensors,
       "sc2tempUnitId": sc2tempUnitId,
       "sc2tempSensorNr": sc2tempSensorNr,
       "sc2tempSensorDesignation": sc2tempSensorDesignation,
       "sc2tempSensorIdentifier": sc2tempSensorIdentifier,
       "sc2tempSensorStatus": sc2tempSensorStatus,
       "sc2tempCurrentTemperature": sc2tempCurrentTemperature,
       "sc2tempWarningLevel": sc2tempWarningLevel,
       "sc2tempCriticalLevel": sc2tempCriticalLevel,
       "sc2tempCriticalReaction": sc2tempCriticalReaction,
       "sc2FanTable": sc2FanTable,
       "sc2Fans": sc2Fans,
       "sc2fanUnitId": sc2fanUnitId,
       "sc2fanNr": sc2fanNr,
       "sc2fanDesignation": sc2fanDesignation,
       "sc2fanIdentifier": sc2fanIdentifier,
       "sc2fanStatus": sc2fanStatus,
       "sc2fanCurrentSpeed": sc2fanCurrentSpeed,
       "sc2fanQuality": sc2fanQuality,
       "sc2fanFailReaction": sc2fanFailReaction,
       "sc2fanFailShutdownDelay": sc2fanFailShutdownDelay,
       "sc2fanCoolingDeviceType": sc2fanCoolingDeviceType,
       "sc2AirflowTable": sc2AirflowTable,
       "sc2Airflow": sc2Airflow,
       "sc2afUnitId": sc2afUnitId,
       "sc2afExhaustAirflowVolume": sc2afExhaustAirflowVolume,
       "sc2afExhaustAirflowVolumeUnit": sc2afExhaustAirflowVolumeUnit,
       "sc2Hardware": sc2Hardware,
       "sc2SystemBoardTable": sc2SystemBoardTable,
       "sc2SystemBoard": sc2SystemBoard,
       "sc2sbUnitId": sc2sbUnitId,
       "sc2sbBoardNr": sc2sbBoardNr,
       "sc2SystemBoardModelName": sc2SystemBoardModelName,
       "sc2SystemBoardProductNumber": sc2SystemBoardProductNumber,
       "sc2SystemBoardRevision": sc2SystemBoardRevision,
       "sc2SystemBoardSerialNumber": sc2SystemBoardSerialNumber,
       "sc2SystemBoardDesignation": sc2SystemBoardDesignation,
       "sc2SystemBoardSDCardSlotPresent": sc2SystemBoardSDCardSlotPresent,
       "sc2PowerSupplyTable": sc2PowerSupplyTable,
       "sc2PowerSupply": sc2PowerSupply,
       "sc2psUnitId": sc2psUnitId,
       "sc2psPowerSupplyNr": sc2psPowerSupplyNr,
       "sc2PowerSupplyDesignation": sc2PowerSupplyDesignation,
       "sc2PowerSupplyIdentifier": sc2PowerSupplyIdentifier,
       "sc2PowerSupplyStatus": sc2PowerSupplyStatus,
       "sc2psPowerSupplyLoad": sc2psPowerSupplyLoad,
       "sc2psPowerSupplyNominal": sc2psPowerSupplyNominal,
       "sc2VoltageTable": sc2VoltageTable,
       "sc2Voltages": sc2Voltages,
       "sc2voUnitId": sc2voUnitId,
       "sc2voSensorNr": sc2voSensorNr,
       "sc2VoltageDesignation": sc2VoltageDesignation,
       "sc2VoltageStatus": sc2VoltageStatus,
       "sc2VoltageCurrentValue": sc2VoltageCurrentValue,
       "sc2VoltageNominalValue": sc2VoltageNominalValue,
       "sc2VoltageMinimumLevel": sc2VoltageMinimumLevel,
       "sc2VoltageMaximumLevel": sc2VoltageMaximumLevel,
       "sc2VoltageCurrentLoad": sc2VoltageCurrentLoad,
       "sc2CPUTable": sc2CPUTable,
       "sc2CPUs": sc2CPUs,
       "sc2cpuUnitId": sc2cpuUnitId,
       "sc2cpuNr": sc2cpuNr,
       "sc2cpuDesignation": sc2cpuDesignation,
       "sc2cpuStatus": sc2cpuStatus,
       "sc2cpuModelName": sc2cpuModelName,
       "sc2cpuManufacturer": sc2cpuManufacturer,
       "sc2cpuStep": sc2cpuStep,
       "sc2cpuCurrentSpeed": sc2cpuCurrentSpeed,
       "sc2cpuNumberLogicals": sc2cpuNumberLogicals,
       "sc2cpuCacheL1Size": sc2cpuCacheL1Size,
       "sc2cpuCacheL2Size": sc2cpuCacheL2Size,
       "sc2cpuCacheL3Size": sc2cpuCacheL3Size,
       "sc2cpuNumberCores": sc2cpuNumberCores,
       "sc2cpuFamily": sc2cpuFamily,
       "sc2cpuEnabledCores": sc2cpuEnabledCores,
       "sc2cpuMultithreadingEnabled": sc2cpuMultithreadingEnabled,
       "sc2cpuConfigurationStatus": sc2cpuConfigurationStatus,
       "sc2cpuMCDRAMSize": sc2cpuMCDRAMSize,
       "sc2cpuMCDRAMSpeed": sc2cpuMCDRAMSpeed,
       "sc2cpuMCDRAMMode": sc2cpuMCDRAMMode,
       "sc2cpuMCDRAMCacheSize": sc2cpuMCDRAMCacheSize,
       "sc2cpuMCDRAMMemoryModel": sc2cpuMCDRAMMemoryModel,
       "sc2MemoryModuleTable": sc2MemoryModuleTable,
       "sc2MemoryModules": sc2MemoryModules,
       "sc2memUnitId": sc2memUnitId,
       "sc2memModuleNr": sc2memModuleNr,
       "sc2memModuleDesignation": sc2memModuleDesignation,
       "sc2memModuleStatus": sc2memModuleStatus,
       "sc2memModuleBank": sc2memModuleBank,
       "sc2memModuleCapacity": sc2memModuleCapacity,
       "sc2memModuleStartAddress": sc2memModuleStartAddress,
       "sc2memModuleForm": sc2memModuleForm,
       "sc2memModuleType": sc2memModuleType,
       "sc2memModuleCorrErrors": sc2memModuleCorrErrors,
       "sc2memModuleUncorrErrors": sc2memModuleUncorrErrors,
       "sc2memModuleApproved": sc2memModuleApproved,
       "sc2memModuleConfiguration": sc2memModuleConfiguration,
       "sc2memModuleFrequency": sc2memModuleFrequency,
       "sc2memModuleMaxFrequency": sc2memModuleMaxFrequency,
       "sc2memModuleVoltInterface": sc2memModuleVoltInterface,
       "sc2cpuMultithreadEnable": sc2cpuMultithreadEnable,
       "sc2ComponentPowerConsumptionTable": sc2ComponentPowerConsumptionTable,
       "sc2ComponentPowerConsumption": sc2ComponentPowerConsumption,
       "sc2cpcUnitId": sc2cpcUnitId,
       "sc2cpcComponentClass": sc2cpcComponentClass,
       "sc2cpcComponentIndex": sc2cpcComponentIndex,
       "sc2cpcDesignation": sc2cpcDesignation,
       "sc2cpcCurrentValue": sc2cpcCurrentValue,
       "sc2TrustedPlatformModuleTable": sc2TrustedPlatformModuleTable,
       "sc2TrustedPlatformModule": sc2TrustedPlatformModule,
       "sc2tpmUnitId": sc2tpmUnitId,
       "sc2tpmHardwareAvailable": sc2tpmHardwareAvailable,
       "sc2tpmBiosEnabled": sc2tpmBiosEnabled,
       "sc2tpmEnabled": sc2tpmEnabled,
       "sc2tpmActivated": sc2tpmActivated,
       "sc2tpmOwnership": sc2tpmOwnership,
       "sc2PersistentMemoryModuleTable": sc2PersistentMemoryModuleTable,
       "sc2PersistentMemoryModules": sc2PersistentMemoryModules,
       "sc2nvmemMemoryModeEnabled": sc2nvmemMemoryModeEnabled,
       "sc2nvmemPersistentModeEnabled": sc2nvmemPersistentModeEnabled,
       "sc2nvmemPackageSparingCapable": sc2nvmemPackageSparingCapable,
       "sc2nvmemEncryptionEnabled": sc2nvmemEncryptionEnabled,
       "sc2nvmemFirmwareRevision": sc2nvmemFirmwareRevision,
       "sc2nvmemTotalSize": sc2nvmemTotalSize,
       "sc2nvmemRawCapacity": sc2nvmemRawCapacity,
       "sc2nvmemVolatileCapacity": sc2nvmemVolatileCapacity,
       "sc2nvmemPersistentCapacity": sc2nvmemPersistentCapacity,
       "sc2nvmemVolatilePercent": sc2nvmemVolatilePercent,
       "sc2nvmemPersistentPercent": sc2nvmemPersistentPercent,
       "sc2nvmemVolatileStart": sc2nvmemVolatileStart,
       "sc2nvmemPersistentStart": sc2nvmemPersistentStart,
       "sc2nvmemHealthStatusNonCritical": sc2nvmemHealthStatusNonCritical,
       "sc2nvmemHealthStatusCritical": sc2nvmemHealthStatusCritical,
       "sc2nvmemHealthStatusFatal": sc2nvmemHealthStatusFatal,
       "sc2nvmemPowerOnTime": sc2nvmemPowerOnTime,
       "sc2nvmemUpTime": sc2nvmemUpTime,
       "sc2nvmemLiftetimeRemaining": sc2nvmemLiftetimeRemaining,
       "sc2nvmemAveragePowerBudget": sc2nvmemAveragePowerBudget,
       "sc2nvmemPeakPowerBudget": sc2nvmemPeakPowerBudget,
       "sc2Recovery": sc2Recovery,
       "sc2MessageLogTable": sc2MessageLogTable,
       "sc2MessageLogs": sc2MessageLogs,
       "sc2msgUnitId": sc2msgUnitId,
       "sc2msgLogEntryNr": sc2msgLogEntryNr,
       "sc2msgLogEntryData": sc2msgLogEntryData,
       "sc2WatchdogTable": sc2WatchdogTable,
       "sc2Watchdogs": sc2Watchdogs,
       "sc2wdUnitId": sc2wdUnitId,
       "sc2WatchdogType": sc2WatchdogType,
       "sc2WatchdogStatus": sc2WatchdogStatus,
       "sc2WatchdogTime": sc2WatchdogTime,
       "sc2WatchdogAction": sc2WatchdogAction,
       "sc2RecoverySettingTable": sc2RecoverySettingTable,
       "sc2RecoverySettings": sc2RecoverySettings,
       "sc2asrUnitId": sc2asrUnitId,
       "sc2asrNrRebootRetries": sc2asrNrRebootRetries,
       "sc2asrDefaultRebootRetries": sc2asrDefaultRebootRetries,
       "sc2asrNextBootSource": sc2asrNextBootSource,
       "sc2asrRebootFailAction": sc2asrRebootFailAction,
       "sc2asrRestartDelay": sc2asrRestartDelay,
       "sc2asrPostErrorHalt": sc2asrPostErrorHalt,
       "sc2MessageTextLogTable": sc2MessageTextLogTable,
       "sc2MessageTextLogs": sc2MessageTextLogs,
       "sc2msgTextLogUnitId": sc2msgTextLogUnitId,
       "sc2msgTextLogLanguage": sc2msgTextLogLanguage,
       "sc2msgTextLogSeqNr": sc2msgTextLogSeqNr,
       "sc2msgTextLogTimestamp": sc2msgTextLogTimestamp,
       "sc2msgTextLogMessage": sc2msgTextLogMessage,
       "sc2msgTextLogErrorCode": sc2msgTextLogErrorCode,
       "sc2msgTextLogSeverity": sc2msgTextLogSeverity,
       "sc2msgTextLogCSSComponent": sc2msgTextLogCSSComponent,
       "sc2MessageLogActionHintTable": sc2MessageLogActionHintTable,
       "sc2MessageLogActionHints": sc2MessageLogActionHints,
       "sc2mlaLanguage": sc2mlaLanguage,
       "sc2mlaErrorCode": sc2mlaErrorCode,
       "sc2mlaType": sc2mlaType,
       "sc2mlaIndex": sc2mlaIndex,
       "sc2mlaMessage": sc2mlaMessage,
       "sc2Status": sc2Status,
       "sc2AgentStatus": sc2AgentStatus,
       "sc2StatusComponentTable": sc2StatusComponentTable,
       "sc2StatusComponents": sc2StatusComponents,
       "sc2csUnitId": sc2csUnitId,
       "sc2csStatusOverall": sc2csStatusOverall,
       "sc2csStatusBoot": sc2csStatusBoot,
       "sc2csStatusPowerSupply": sc2csStatusPowerSupply,
       "sc2csStatusTemperature": sc2csStatusTemperature,
       "sc2csStatusFans": sc2csStatusFans,
       "sc2csStatusVoltages": sc2csStatusVoltages,
       "sc2csStatusCpu": sc2csStatusCpu,
       "sc2csStatusMemoryModule": sc2csStatusMemoryModule,
       "sc2ComponentStatusSensorTable": sc2ComponentStatusSensorTable,
       "sc2ComponentStatusSensors": sc2ComponentStatusSensors,
       "sc2cssUnitId": sc2cssUnitId,
       "sc2cssSensorNumber": sc2cssSensorNumber,
       "sc2cssSensorDesignation": sc2cssSensorDesignation,
       "sc2cssSensorDevice": sc2cssSensorDevice,
       "sc2cssSensorDeviceInstance": sc2cssSensorDeviceInstance,
       "sc2cssSensorPhysicalLed": sc2cssSensorPhysicalLed,
       "sc2cssSensorCssComponent": sc2cssSensorCssComponent,
       "sc2cssSensorStatus": sc2cssSensorStatus,
       "sc2cssComponentServicePartId": sc2cssComponentServicePartId,
       "sc2cssTableSize": sc2cssTableSize,
       "sc2Maintenance": sc2Maintenance,
       "sc2MaintenanceObjectTable": sc2MaintenanceObjectTable,
       "sc2MaintenanceObjects": sc2MaintenanceObjects,
       "sc2mtUnitId": sc2mtUnitId,
       "sc2ErrorCounterStartTime": sc2ErrorCounterStartTime,
       "sc2SendTestTrap": sc2SendTestTrap,
       "sc2AddTrapDestination": sc2AddTrapDestination,
       "sc2FirmwareVersionTable": sc2FirmwareVersionTable,
       "sc2FirmwareVersions": sc2FirmwareVersions,
       "sc2fwUnitId": sc2fwUnitId,
       "sc2fwType": sc2fwType,
       "sc2fwModelName": sc2fwModelName,
       "sc2fwVersion": sc2fwVersion,
       "sc2Deployment": sc2Deployment,
       "sc2DeployInfoTable": sc2DeployInfoTable,
       "sc2DeployInfo": sc2DeployInfo,
       "sc2dplInfoUnitId": sc2dplInfoUnitId,
       "sc2DeployInfoChassisId": sc2DeployInfoChassisId,
       "sc2DeployInfoMacAddr1": sc2DeployInfoMacAddr1,
       "sc2DeployInfoMacAddr2": sc2DeployInfoMacAddr2,
       "sc2DeployInfoMacAddr3": sc2DeployInfoMacAddr3,
       "sc2DeployInfoMacAddr4": sc2DeployInfoMacAddr4,
       "sc2DeployInfoIpAddr1": sc2DeployInfoIpAddr1,
       "sc2DeployInfoIpAddr2": sc2DeployInfoIpAddr2,
       "sc2DeployInfoIpAddr3": sc2DeployInfoIpAddr3,
       "sc2DeployInfoIpAddr4": sc2DeployInfoIpAddr4,
       "sc2DeployInfoNetMask1": sc2DeployInfoNetMask1,
       "sc2DeployInfoNetMask2": sc2DeployInfoNetMask2,
       "sc2DeployInfoNetMask3": sc2DeployInfoNetMask3,
       "sc2DeployInfoNetMask4": sc2DeployInfoNetMask4,
       "sc2DeployInfoGateway1": sc2DeployInfoGateway1,
       "sc2DeployInfoGateway2": sc2DeployInfoGateway2,
       "sc2DeployInfoGateway3": sc2DeployInfoGateway3,
       "sc2DeployInfoGateway4": sc2DeployInfoGateway4,
       "sc2DeployInfoHostname": sc2DeployInfoHostname,
       "sc2DeployInfoMasterImageReference": sc2DeployInfoMasterImageReference,
       "sc2DeployInfoStatusOfBlade": sc2DeployInfoStatusOfBlade,
       "sc2DeployInfoLanStatusOfSlot": sc2DeployInfoLanStatusOfSlot,
       "sc2DeployInfoAutomaticRecovery": sc2DeployInfoAutomaticRecovery,
       "sc2DeployInfoStatusOfCloning": sc2DeployInfoStatusOfCloning,
       "sc2DeployInfoBootMode": sc2DeployInfoBootMode,
       "sc2OemDeployInfoTable": sc2OemDeployInfoTable,
       "sc2OemDeployInfo": sc2OemDeployInfo,
       "sc2odplInfoUnitId": sc2odplInfoUnitId,
       "sc2odplParamId": sc2odplParamId,
       "sc2OemDeployInfoParamData": sc2OemDeployInfoParamData,
       "sc2DeployLanInterfaceTable": sc2DeployLanInterfaceTable,
       "sc2DeployLanInterfaces": sc2DeployLanInterfaces,
       "sc2dplLanUnitId": sc2dplLanUnitId,
       "sc2dplLanInterfaceNr": sc2dplLanInterfaceNr,
       "sc2dplLanMacAddress": sc2dplLanMacAddress,
       "sc2DriverMonitoring": sc2DriverMonitoring,
       "sc2DriverMonitorComponentTable": sc2DriverMonitorComponentTable,
       "sc2DriverMonitorComponents": sc2DriverMonitorComponents,
       "sc2drvmonCompClass": sc2drvmonCompClass,
       "sc2drvmonCompIndex": sc2drvmonCompIndex,
       "sc2drvmonCompName": sc2drvmonCompName,
       "sc2drvmonCompType": sc2drvmonCompType,
       "sc2drvmonCompDriverName": sc2drvmonCompDriverName,
       "sc2drvmonCompLocationDesignation": sc2drvmonCompLocationDesignation,
       "sc2drvmonCompLocationKey": sc2drvmonCompLocationKey,
       "sc2drvmonCompStatus": sc2drvmonCompStatus,
       "sc2drvmonCompErrorAcknowledge": sc2drvmonCompErrorAcknowledge,
       "sc2DriverMonitorMessageTable": sc2DriverMonitorMessageTable,
       "sc2DriverMonitorMessages": sc2DriverMonitorMessages,
       "sc2drvmonMsgSeqNr": sc2drvmonMsgSeqNr,
       "sc2drvmonMsgTimestamp": sc2drvmonMsgTimestamp,
       "sc2drvmonMsgMessage": sc2drvmonMsgMessage,
       "sc2drvmonMsgEventId": sc2drvmonMsgEventId,
       "sc2drvmonMsgSeverity": sc2drvmonMsgSeverity,
       "sc2drvmonMsgErrorCode": sc2drvmonMsgErrorCode,
       "sc2drvmonOrigLogMessage": sc2drvmonOrigLogMessage,
       "sc2drvmonOrigLogSource": sc2drvmonOrigLogSource,
       "sc2drvmonOrigLogId": sc2drvmonOrigLogId,
       "sc2drvmonOrigLogSeverity": sc2drvmonOrigLogSeverity,
       "sc2drvmonTableUpdateCount": sc2drvmonTableUpdateCount,
       "sc2Notifications": sc2Notifications,
       "sc2TrapTest": sc2TrapTest,
       "sc2TrapCommunicationFailure": sc2TrapCommunicationFailure,
       "sc2TrapCommunicationEstablished": sc2TrapCommunicationEstablished,
       "sc2TrapControllerSelftestWarning": sc2TrapControllerSelftestWarning,
       "sc2TrapControllerSelftestError": sc2TrapControllerSelftestError,
       "sc2TrapBiosSelftestError": sc2TrapBiosSelftestError,
       "sc2TrapSevereSystemError": sc2TrapSevereSystemError,
       "sc2TrapFanAdded": sc2TrapFanAdded,
       "sc2TrapFanRemoved": sc2TrapFanRemoved,
       "sc2TrapFanOk": sc2TrapFanOk,
       "sc2TrapFanCritical": sc2TrapFanCritical,
       "sc2TrapFanFailed": sc2TrapFanFailed,
       "sc2TrapRedundantFanFailed": sc2TrapRedundantFanFailed,
       "sc2TrapTempOk": sc2TrapTempOk,
       "sc2TrapTempWarning": sc2TrapTempWarning,
       "sc2TrapTempCritical": sc2TrapTempCritical,
       "sc2TrapTempSensorOk": sc2TrapTempSensorOk,
       "sc2TrapTempSensorBroken": sc2TrapTempSensorBroken,
       "sc2TrapPowerSupplyAdded": sc2TrapPowerSupplyAdded,
       "sc2TrapPowerSupplyRemoved": sc2TrapPowerSupplyRemoved,
       "sc2TrapPowerSupplyOk": sc2TrapPowerSupplyOk,
       "sc2TrapPowerSupplyCritical": sc2TrapPowerSupplyCritical,
       "sc2TrapPowerSupplyFailed": sc2TrapPowerSupplyFailed,
       "sc2TrapRedundantPowerSupplyFailed": sc2TrapRedundantPowerSupplyFailed,
       "sc2TrapPowerSupplyRedundancyLost": sc2TrapPowerSupplyRedundancyLost,
       "sc2TrapPowerSupplyCriticalTemperature": sc2TrapPowerSupplyCriticalTemperature,
       "sc2TrapPowerSupplyFanFailurePrediction": sc2TrapPowerSupplyFanFailurePrediction,
       "sc2TrapPowerSupplyFanFailure": sc2TrapPowerSupplyFanFailure,
       "sc2TrapAcFail": sc2TrapAcFail,
       "sc2TrapDcFail": sc2TrapDcFail,
       "sc2TrapOnBattery": sc2TrapOnBattery,
       "sc2TrapOnMains": sc2TrapOnMains,
       "sc2TrapVoltageOk": sc2TrapVoltageOk,
       "sc2TrapVoltageTooLow": sc2TrapVoltageTooLow,
       "sc2TrapVoltageTooHigh": sc2TrapVoltageTooHigh,
       "sc2TrapVoltageFailed": sc2TrapVoltageFailed,
       "sc2TrapBatteryVoltagePrefail": sc2TrapBatteryVoltagePrefail,
       "sc2TrapCorrectableMemErrorAddr": sc2TrapCorrectableMemErrorAddr,
       "sc2TrapUncorrectableMemErrorAddr": sc2TrapUncorrectableMemErrorAddr,
       "sc2TrapCorrectableMemErrorBank": sc2TrapCorrectableMemErrorBank,
       "sc2TrapUncorrectableMemErrorBank": sc2TrapUncorrectableMemErrorBank,
       "sc2TrapCorrectableMemErrorModule": sc2TrapCorrectableMemErrorModule,
       "sc2TrapUncorrectableMemErrorModule": sc2TrapUncorrectableMemErrorModule,
       "sc2TrapCorrectableMemError": sc2TrapCorrectableMemError,
       "sc2TrapUncorrectableMemError": sc2TrapUncorrectableMemError,
       "sc2TrapMemErrorModulePrefail": sc2TrapMemErrorModulePrefail,
       "sc2TrapMemErrorModuleFailing": sc2TrapMemErrorModuleFailing,
       "sc2TrapMemErrorModuleReplaced": sc2TrapMemErrorModuleReplaced,
       "sc2TrapMemErrorLoggingDisabled": sc2TrapMemErrorLoggingDisabled,
       "sc2TrapMemErrorLoggingEnabled": sc2TrapMemErrorLoggingEnabled,
       "sc2TrapMemErrorAnyModuleReplaced": sc2TrapMemErrorAnyModuleReplaced,
       "sc2TrapMemErrorRedundancyLost": sc2TrapMemErrorRedundancyLost,
       "sc2TrapMemNVDIMMLifetime": sc2TrapMemNVDIMMLifetime,
       "sc2TrapCpuSpeedChanged": sc2TrapCpuSpeedChanged,
       "sc2TrapCpuPrefail": sc2TrapCpuPrefail,
       "sc2TrapCpuIerr": sc2TrapCpuIerr,
       "sc2TrapCpuDisabled": sc2TrapCpuDisabled,
       "sc2TrapCabinetSwitchedOff": sc2TrapCabinetSwitchedOff,
       "sc2TrapCabinetSwitchedOn": sc2TrapCabinetSwitchedOn,
       "sc2TrapPowerOffTimeReached": sc2TrapPowerOffTimeReached,
       "sc2TrapServerShutdown": sc2TrapServerShutdown,
       "sc2TrapShutdownCancelled": sc2TrapShutdownCancelled,
       "sc2TrapBootRetryCountZero": sc2TrapBootRetryCountZero,
       "sc2TrapServerBoot": sc2TrapServerBoot,
       "sc2TrapServerStandby": sc2TrapServerStandby,
       "sc2TrapServerSuspend": sc2TrapServerSuspend,
       "sc2TrapServerResumed": sc2TrapServerResumed,
       "sc2TrapMessageLogFull": sc2TrapMessageLogFull,
       "sc2TrapMessageLogWarning": sc2TrapMessageLogWarning,
       "sc2TrapBootMessageLogEntry": sc2TrapBootMessageLogEntry,
       "sc2TrapIntrusionAssertion": sc2TrapIntrusionAssertion,
       "sc2TrapIntrusionDeassertion": sc2TrapIntrusionDeassertion,
       "sc2TrapIntrusionChanged": sc2TrapIntrusionChanged,
       "sc2TrapPciBusError": sc2TrapPciBusError,
       "sc2TrapPowerOnTimeReached": sc2TrapPowerOnTimeReached,
       "sc2TrapCssWarning": sc2TrapCssWarning,
       "sc2TrapCssFail": sc2TrapCssFail,
       "sc2TrapCssWarningServer": sc2TrapCssWarningServer,
       "sc2TrapCssFailServer": sc2TrapCssFailServer,
       "sc2TrapPowerLimitOk": sc2TrapPowerLimitOk,
       "sc2TrapPowerLimitWarning": sc2TrapPowerLimitWarning,
       "sc2TrapPowerLimitCritical": sc2TrapPowerLimitCritical,
       "sc2TrapPowerLimitDisabled": sc2TrapPowerLimitDisabled,
       "sc2TrapViomInitiateCommunication": sc2TrapViomInitiateCommunication,
       "sc2TrapViomStatusChanged": sc2TrapViomStatusChanged,
       "sc2TrapDrvMonEventMessage": sc2TrapDrvMonEventMessage,
       "sc2TrapDrvMonEventWarning": sc2TrapDrvMonEventWarning,
       "sc2TrapDrvMonEventError": sc2TrapDrvMonEventError,
       "sc2NotificationsTrapInfo": sc2NotificationsTrapInfo,
       "sc2TrapInfoServerName": sc2TrapInfoServerName,
       "sc2TrapInfoTime": sc2TrapInfoTime,
       "sc2TrapInfoCabinetNr": sc2TrapInfoCabinetNr,
       "sc2TrapInfoObjectDesignation": sc2TrapInfoObjectDesignation,
       "sc2TrapInfoString": sc2TrapInfoString,
       "sc2TrapInfoInteger": sc2TrapInfoInteger,
       "sc2TrapInfoInteger2": sc2TrapInfoInteger2}
)
