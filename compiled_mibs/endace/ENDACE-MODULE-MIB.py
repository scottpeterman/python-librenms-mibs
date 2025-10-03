# SNMP MIB module (ENDACE-MODULE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\endace\ENDACE-MODULE-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:39:58 2025
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

(endace,) = mibBuilder.importSymbols(
    "ENDACE-MIB",
    "endace")

(EndaceModuleType,) = mibBuilder.importSymbols(
    "ENDACEModuleType-MIB",
    "EndaceModuleType")

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

shogunModuleMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2)
)
if mibBuilder.loadTexts:
    shogunModuleMIB.setRevisions(
        ("2019-05-01 00:37",
         "2014-02-20 01:11",
         "2013-10-07 04:08",
         "2013-01-22 00:53",
         "2012-09-24 21:31",
         "2009-10-05 00:00",
         "2009-08-05 00:00",
         "2007-05-23 00:00",
         "2007-04-23 00:00",
         "2007-04-09 00:00",
         "2007-03-29 00:00",
         "2007-01-27 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EndaceifType(TextualConvention, Integer32):
    status = "current"
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
        *(("ethernet", 1),
          ("sonet", 2),
          ("pdh", 3),
          ("ethernetLan", 4),
          ("ethernetWan", 5))
    )



class InterfaceIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


class ModuleIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


# MIB Managed Objects in the order of their OIDs

_ModuleMIBObjects_ObjectIdentity = ObjectIdentity
moduleMIBObjects = _ModuleMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1)
)
_ModuleTable_Object = MibTable
moduleTable = _ModuleTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1)
)
if mibBuilder.loadTexts:
    moduleTable.setStatus("current")
_ModuleTableEntry_Object = MibTableRow
moduleTableEntry = _ModuleTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1)
)
moduleTableEntry.setIndexNames(
    (0, "ENDACE-MODULE-MIB", "moduleIndex"),
)
if mibBuilder.loadTexts:
    moduleTableEntry.setStatus("current")
_ModuleIndex_Type = ModuleIndex
_ModuleIndex_Object = MibTableColumn
moduleIndex = _ModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1, 1),
    _ModuleIndex_Type()
)
moduleIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleIndex.setStatus("current")


class _ModuleName_Type(DisplayString):
    """Custom type moduleName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModuleName_Type.__name__ = "DisplayString"
_ModuleName_Object = MibTableColumn
moduleName = _ModuleName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1, 2),
    _ModuleName_Type()
)
moduleName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleName.setStatus("current")
_ModuleType_Type = EndaceModuleType
_ModuleType_Object = MibTableColumn
moduleType = _ModuleType_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1, 3),
    _ModuleType_Type()
)
moduleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleType.setStatus("current")
_ModuleActiveFirmware_Type = DisplayString
_ModuleActiveFirmware_Object = MibTableColumn
moduleActiveFirmware = _ModuleActiveFirmware_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1, 4),
    _ModuleActiveFirmware_Type()
)
moduleActiveFirmware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleActiveFirmware.setStatus("current")


class _ModuleOperStatus_Type(Integer32):
    """Custom type moduleOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_ModuleOperStatus_Type.__name__ = "Integer32"
_ModuleOperStatus_Object = MibTableColumn
moduleOperStatus = _ModuleOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1, 5),
    _ModuleOperStatus_Type()
)
moduleOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleOperStatus.setStatus("current")
_ModuleLastChange_Type = TimeTicks
_ModuleLastChange_Object = MibTableColumn
moduleLastChange = _ModuleLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1, 6),
    _ModuleLastChange_Type()
)
moduleLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleLastChange.setStatus("current")
_ModuleSnapLen_Type = Unsigned32
_ModuleSnapLen_Object = MibTableColumn
moduleSnapLen = _ModuleSnapLen_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1, 7),
    _ModuleSnapLen_Type()
)
moduleSnapLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleSnapLen.setStatus("obsolete")
_ModuleTemperature_Type = Unsigned32
_ModuleTemperature_Object = MibTableColumn
moduleTemperature = _ModuleTemperature_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1, 8),
    _ModuleTemperature_Type()
)
moduleTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    moduleTemperature.setStatus("current")
_ModuleVoltage_Type = Unsigned32
_ModuleVoltage_Object = MibTableColumn
moduleVoltage = _ModuleVoltage_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 1, 1, 9),
    _ModuleVoltage_Type()
)
moduleVoltage.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    moduleVoltage.setStatus("deprecated")
_ModuleInterfaces_ObjectIdentity = ObjectIdentity
moduleInterfaces = _ModuleInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2)
)
_ModifTable_Object = MibTable
modifTable = _ModifTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    modifTable.setStatus("current")
_ModifEntry_Object = MibTableRow
modifEntry = _ModifEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1)
)
modifEntry.setIndexNames(
    (0, "ENDACE-MODULE-MIB", "modifModIndex"),
)
if mibBuilder.loadTexts:
    modifEntry.setStatus("current")
_ModifModIndex_Type = InterfaceIndex
_ModifModIndex_Object = MibTableColumn
modifModIndex = _ModifModIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 1),
    _ModifModIndex_Type()
)
modifModIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifModIndex.setStatus("current")


class _ModifPortLabel_Type(DisplayString):
    """Custom type modifPortLabel based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_ModifPortLabel_Type.__name__ = "DisplayString"
_ModifPortLabel_Object = MibTableColumn
modifPortLabel = _ModifPortLabel_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 2),
    _ModifPortLabel_Type()
)
modifPortLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifPortLabel.setStatus("current")
_ModifModule_Type = Integer32
_ModifModule_Object = MibTableColumn
modifModule = _ModifModule_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 3),
    _ModifModule_Type()
)
modifModule.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifModule.setStatus("current")


class _ModifName_Type(DisplayString):
    """Custom type modifName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_ModifName_Type.__name__ = "DisplayString"
_ModifName_Object = MibTableColumn
modifName = _ModifName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 4),
    _ModifName_Type()
)
modifName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifName.setStatus("current")
_ModifType_Type = EndaceifType
_ModifType_Object = MibTableColumn
modifType = _ModifType_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 5),
    _ModifType_Type()
)
modifType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifType.setStatus("current")
_ModifMtu_Type = Integer32
_ModifMtu_Object = MibTableColumn
modifMtu = _ModifMtu_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 6),
    _ModifMtu_Type()
)
modifMtu.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifMtu.setStatus("current")


class _ModifInAdminStatus_Type(Integer32):
    """Custom type modifInAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_ModifInAdminStatus_Type.__name__ = "Integer32"
_ModifInAdminStatus_Object = MibTableColumn
modifInAdminStatus = _ModifInAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 7),
    _ModifInAdminStatus_Type()
)
modifInAdminStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifInAdminStatus.setStatus("current")


class _ModifInOperStatus_Type(Integer32):
    """Custom type modifInOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("unknown", 3))
    )


_ModifInOperStatus_Type.__name__ = "Integer32"
_ModifInOperStatus_Object = MibTableColumn
modifInOperStatus = _ModifInOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 8),
    _ModifInOperStatus_Type()
)
modifInOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifInOperStatus.setStatus("current")
_ModifLastChange_Type = TimeTicks
_ModifLastChange_Object = MibTableColumn
modifLastChange = _ModifLastChange_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 9),
    _ModifLastChange_Type()
)
modifLastChange.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modifLastChange.setStatus("deprecated")


class _ModifLinkUpDownTrapEnable_Type(Integer32):
    """Custom type modifLinkUpDownTrapEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_ModifLinkUpDownTrapEnable_Type.__name__ = "Integer32"
_ModifLinkUpDownTrapEnable_Object = MibTableColumn
modifLinkUpDownTrapEnable = _ModifLinkUpDownTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 10),
    _ModifLinkUpDownTrapEnable_Type()
)
modifLinkUpDownTrapEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifLinkUpDownTrapEnable.setStatus("current")
_ModifLinkDropThreshold_Type = Gauge32
_ModifLinkDropThreshold_Object = MibTableColumn
modifLinkDropThreshold = _ModifLinkDropThreshold_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 11),
    _ModifLinkDropThreshold_Type()
)
modifLinkDropThreshold.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modifLinkDropThreshold.setStatus("deprecated")
_ModifSpeed_Type = Gauge32
_ModifSpeed_Object = MibTableColumn
modifSpeed = _ModifSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 12),
    _ModifSpeed_Type()
)
modifSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifSpeed.setStatus("current")
if mibBuilder.loadTexts:
    modifSpeed.setUnits("Mbps")
_ModifHighSpeed_Type = Gauge32
_ModifHighSpeed_Object = MibTableColumn
modifHighSpeed = _ModifHighSpeed_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 13),
    _ModifHighSpeed_Type()
)
modifHighSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifHighSpeed.setStatus("obsolete")
_ModifInOctets_Type = Counter32
_ModifInOctets_Object = MibTableColumn
modifInOctets = _ModifInOctets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 14),
    _ModifInOctets_Type()
)
modifInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifInOctets.setStatus("deprecated")
_ModifInPackets_Type = Counter32
_ModifInPackets_Object = MibTableColumn
modifInPackets = _ModifInPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 15),
    _ModifInPackets_Type()
)
modifInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifInPackets.setStatus("deprecated")
_ModifInDropPackets_Type = Counter32
_ModifInDropPackets_Object = MibTableColumn
modifInDropPackets = _ModifInDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 16),
    _ModifInDropPackets_Type()
)
modifInDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifInDropPackets.setStatus("deprecated")
_ModifOutOctets_Type = Counter32
_ModifOutOctets_Object = MibTableColumn
modifOutOctets = _ModifOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 17),
    _ModifOutOctets_Type()
)
modifOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifOutOctets.setStatus("deprecated")
_ModifOutPackets_Type = Counter32
_ModifOutPackets_Object = MibTableColumn
modifOutPackets = _ModifOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 18),
    _ModifOutPackets_Type()
)
modifOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifOutPackets.setStatus("deprecated")
_ModifHCInOctets_Type = Counter64
_ModifHCInOctets_Object = MibTableColumn
modifHCInOctets = _ModifHCInOctets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 19),
    _ModifHCInOctets_Type()
)
modifHCInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifHCInOctets.setStatus("current")
_ModifHCInPackets_Type = Counter64
_ModifHCInPackets_Object = MibTableColumn
modifHCInPackets = _ModifHCInPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 20),
    _ModifHCInPackets_Type()
)
modifHCInPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifHCInPackets.setStatus("current")
_ModifHCInDropPackets_Type = Counter64
_ModifHCInDropPackets_Object = MibTableColumn
modifHCInDropPackets = _ModifHCInDropPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 21),
    _ModifHCInDropPackets_Type()
)
modifHCInDropPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifHCInDropPackets.setStatus("current")
_ModifHCOutOctets_Type = Counter64
_ModifHCOutOctets_Object = MibTableColumn
modifHCOutOctets = _ModifHCOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 22),
    _ModifHCOutOctets_Type()
)
modifHCOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifHCOutOctets.setStatus("current")
_ModifHCOutPackets_Type = Counter64
_ModifHCOutPackets_Object = MibTableColumn
modifHCOutPackets = _ModifHCOutPackets_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 23),
    _ModifHCOutPackets_Type()
)
modifHCOutPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifHCOutPackets.setStatus("current")
_ModifCounterDiscontinuityTime_Type = TimeTicks
_ModifCounterDiscontinuityTime_Object = MibTableColumn
modifCounterDiscontinuityTime = _ModifCounterDiscontinuityTime_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 24),
    _ModifCounterDiscontinuityTime_Type()
)
modifCounterDiscontinuityTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifCounterDiscontinuityTime.setStatus("current")
_ModifHCInErrors_Type = Counter64
_ModifHCInErrors_Object = MibTableColumn
modifHCInErrors = _ModifHCInErrors_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 25),
    _ModifHCInErrors_Type()
)
modifHCInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifHCInErrors.setStatus("current")
_ModifUserLabel_Type = DisplayString
_ModifUserLabel_Object = MibTableColumn
modifUserLabel = _ModifUserLabel_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 26),
    _ModifUserLabel_Type()
)
modifUserLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifUserLabel.setStatus("current")


class _ModifPhysAddr_Type(PhysAddress):
    """Custom type modifPhysAddr based on PhysAddress"""
    subtypeSpec = PhysAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 18),
    )


_ModifPhysAddr_Type.__name__ = "PhysAddress"
_ModifPhysAddr_Object = MibTableColumn
modifPhysAddr = _ModifPhysAddr_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 1, 1, 27),
    _ModifPhysAddr_Type()
)
modifPhysAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modifPhysAddr.setStatus("current")
_ModoptTable_Object = MibTable
modoptTable = _ModoptTable_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3)
)
if mibBuilder.loadTexts:
    modoptTable.setStatus("current")
_ModoptEntry_Object = MibTableRow
modoptEntry = _ModoptEntry_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1)
)
modoptEntry.setIndexNames(
    (0, "ENDACE-MODULE-MIB", "modoptIndex"),
)
if mibBuilder.loadTexts:
    modoptEntry.setStatus("current")
_ModoptIndex_Type = Unsigned32
_ModoptIndex_Object = MibTableColumn
modoptIndex = _ModoptIndex_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 1),
    _ModoptIndex_Type()
)
modoptIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    modoptIndex.setStatus("current")
_ModoptName_Type = DisplayString
_ModoptName_Object = MibTableColumn
modoptName = _ModoptName_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 2),
    _ModoptName_Type()
)
modoptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptName.setStatus("current")
_ModoptDetect_Type = TruthValue
_ModoptDetect_Object = MibTableColumn
modoptDetect = _ModoptDetect_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 3),
    _ModoptDetect_Type()
)
modoptDetect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptDetect.setStatus("current")
_ModoptLOS_Type = TruthValue
_ModoptLOS_Object = MibTableColumn
modoptLOS = _ModoptLOS_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 4),
    _ModoptLOS_Type()
)
modoptLOS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptLOS.setStatus("current")
_ModoptRxPower_Type = DisplayString
_ModoptRxPower_Object = MibTableColumn
modoptRxPower = _ModoptRxPower_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 5),
    _ModoptRxPower_Type()
)
modoptRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptRxPower.setStatus("current")
_ModoptRxPowerOk_Type = TruthValue
_ModoptRxPowerOk_Object = MibTableColumn
modoptRxPowerOk = _ModoptRxPowerOk_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 6),
    _ModoptRxPowerOk_Type()
)
modoptRxPowerOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptRxPowerOk.setStatus("current")
_ModoptTxPower_Type = DisplayString
_ModoptTxPower_Object = MibTableColumn
modoptTxPower = _ModoptTxPower_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 7),
    _ModoptTxPower_Type()
)
modoptTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptTxPower.setStatus("current")
_ModoptTxPowerOk_Type = TruthValue
_ModoptTxPowerOk_Object = MibTableColumn
modoptTxPowerOk = _ModoptTxPowerOk_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 8),
    _ModoptTxPowerOk_Type()
)
modoptTxPowerOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptTxPowerOk.setStatus("current")
_ModoptTemp_Type = DisplayString
_ModoptTemp_Object = MibTableColumn
modoptTemp = _ModoptTemp_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 9),
    _ModoptTemp_Type()
)
modoptTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptTemp.setStatus("current")
_ModoptTempOk_Type = TruthValue
_ModoptTempOk_Object = MibTableColumn
modoptTempOk = _ModoptTempOk_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 10),
    _ModoptTempOk_Type()
)
modoptTempOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptTempOk.setStatus("current")
_ModoptVolt_Type = DisplayString
_ModoptVolt_Object = MibTableColumn
modoptVolt = _ModoptVolt_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 11),
    _ModoptVolt_Type()
)
modoptVolt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptVolt.setStatus("current")
_ModoptVoltOk_Type = TruthValue
_ModoptVoltOk_Object = MibTableColumn
modoptVoltOk = _ModoptVoltOk_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 12),
    _ModoptVoltOk_Type()
)
modoptVoltOk.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptVoltOk.setStatus("current")
_ModoptCompliance_Type = DisplayString
_ModoptCompliance_Object = MibTableColumn
modoptCompliance = _ModoptCompliance_Object(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 2, 3, 1, 13),
    _ModoptCompliance_Type()
)
modoptCompliance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    modoptCompliance.setStatus("current")
_ModuleTraps1_ObjectIdentity = ObjectIdentity
moduleTraps1 = _ModuleTraps1_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3)
)
_ModuleConformance_ObjectIdentity = ObjectIdentity
moduleConformance = _ModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2)
)
_ModuleGroups_ObjectIdentity = ObjectIdentity
moduleGroups = _ModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1)
)
_ModuleCompliances_ObjectIdentity = ObjectIdentity
moduleCompliances = _ModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 2)
)

# Managed Objects groups

moduleControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 1)
)
moduleControlGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "moduleIndex"),
        ("ENDACE-MODULE-MIB", "moduleName"),
        ("ENDACE-MODULE-MIB", "moduleType"),
        ("ENDACE-MODULE-MIB", "moduleActiveFirmware"),
        ("ENDACE-MODULE-MIB", "moduleOperStatus"),
        ("ENDACE-MODULE-MIB", "moduleLastChange"))
)
if mibBuilder.loadTexts:
    moduleControlGroup.setStatus("current")

ifControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 2)
)
ifControlGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "modifInAdminStatus"),
        ("ENDACE-MODULE-MIB", "modifInOperStatus"),
        ("ENDACE-MODULE-MIB", "modifLinkUpDownTrapEnable"),
        ("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifModule"),
        ("ENDACE-MODULE-MIB", "modifMtu"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifPortLabel"),
        ("ENDACE-MODULE-MIB", "modifSpeed"),
        ("ENDACE-MODULE-MIB", "modifType"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "modifPhysAddr"))
)
if mibBuilder.loadTexts:
    ifControlGroup.setStatus("current")

ifInPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 3)
)
ifInPacketGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "modifInOctets"),
        ("ENDACE-MODULE-MIB", "modifInPackets"),
        ("ENDACE-MODULE-MIB", "modifInDropPackets"))
)
if mibBuilder.loadTexts:
    ifInPacketGroup.setStatus("deprecated")

ifOutPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 4)
)
ifOutPacketGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "modifOutPackets"),
        ("ENDACE-MODULE-MIB", "modifOutOctets"))
)
if mibBuilder.loadTexts:
    ifOutPacketGroup.setStatus("deprecated")

ifInHCPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 5)
)
ifInHCPacketGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "modifHCInOctets"),
        ("ENDACE-MODULE-MIB", "modifHCInPackets"),
        ("ENDACE-MODULE-MIB", "modifHCInDropPackets"),
        ("ENDACE-MODULE-MIB", "modifHCInErrors"))
)
if mibBuilder.loadTexts:
    ifInHCPacketGroup.setStatus("current")

ifOutHCPacketGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 6)
)
ifOutHCPacketGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "modifHCOutOctets"),
        ("ENDACE-MODULE-MIB", "modifHCOutPackets"))
)
if mibBuilder.loadTexts:
    ifOutHCPacketGroup.setStatus("current")

ifModCounterDiscontinuityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 7)
)
ifModCounterDiscontinuityGroup.setObjects(
    ("ENDACE-MODULE-MIB", "modifCounterDiscontinuityTime")
)
if mibBuilder.loadTexts:
    ifModCounterDiscontinuityGroup.setStatus("current")

modoptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 11)
)
modoptGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "modoptCompliance"),
        ("ENDACE-MODULE-MIB", "modoptDetect"),
        ("ENDACE-MODULE-MIB", "modoptLOS"),
        ("ENDACE-MODULE-MIB", "modoptName"),
        ("ENDACE-MODULE-MIB", "modoptRxPower"),
        ("ENDACE-MODULE-MIB", "modoptRxPowerOk"),
        ("ENDACE-MODULE-MIB", "modoptTemp"),
        ("ENDACE-MODULE-MIB", "modoptTempOk"),
        ("ENDACE-MODULE-MIB", "modoptTxPower"),
        ("ENDACE-MODULE-MIB", "modoptTxPowerOk"),
        ("ENDACE-MODULE-MIB", "modoptVolt"),
        ("ENDACE-MODULE-MIB", "modoptVoltOk"))
)
if mibBuilder.loadTexts:
    modoptGroup.setStatus("current")

modulePhysStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 16)
)
modulePhysStatusGroup.setObjects(
    ("ENDACE-MODULE-MIB", "moduleTemperature")
)
if mibBuilder.loadTexts:
    modulePhysStatusGroup.setStatus("current")

obsoleteGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 18)
)
obsoleteGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "modifHighSpeed"),
        ("ENDACE-MODULE-MIB", "moduleSnapLen"))
)
if mibBuilder.loadTexts:
    obsoleteGroup.setStatus("obsolete")


# Notification objects

modlinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 1)
)
modlinkUp.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    modlinkUp.setStatus(
        "current"
    )

modlinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 2)
)
modlinkDown.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    modlinkDown.setStatus(
        "current"
    )

dropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 5)
)
dropFault.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    dropFault.setStatus(
        "current"
    )

dropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 6)
)
dropNormal.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    dropNormal.setStatus(
        "current"
    )

fcsFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 7)
)
fcsFault.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    fcsFault.setStatus(
        "current"
    )

fcsNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 8)
)
fcsNormal.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    fcsNormal.setStatus(
        "current"
    )

remoteFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 9)
)
remoteFault.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    remoteFault.setStatus(
        "current"
    )

timestampConvDropFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 10)
)
timestampConvDropFault.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    timestampConvDropFault.setStatus(
        "obsolete"
    )

timestampConvDropNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 11)
)
timestampConvDropNormal.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    timestampConvDropNormal.setStatus(
        "obsolete"
    )

syncLoss = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 13)
)
syncLoss.setObjects(
      *(("ENDACE-MODULE-MIB", "moduleIndex"),
        ("ENDACE-MODULE-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    syncLoss.setStatus(
        "current"
    )

syncReturn = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 14)
)
syncReturn.setObjects(
      *(("ENDACE-MODULE-MIB", "moduleIndex"),
        ("ENDACE-MODULE-MIB", "moduleName"))
)
if mibBuilder.loadTexts:
    syncReturn.setStatus(
        "current"
    )

inErrorFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 15)
)
inErrorFault.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    inErrorFault.setStatus(
        "current"
    )

inErrorNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 18418, 2, 1, 3, 16)
)
inErrorNormal.setObjects(
      *(("ENDACE-MODULE-MIB", "modifModIndex"),
        ("ENDACE-MODULE-MIB", "modifName"),
        ("ENDACE-MODULE-MIB", "modifUserLabel"),
        ("ENDACE-MODULE-MIB", "moduleIndex"))
)
if mibBuilder.loadTexts:
    inErrorNormal.setStatus(
        "current"
    )


# Notifications groups

linkTrapsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 8)
)
linkTrapsGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "modlinkUp"),
        ("ENDACE-MODULE-MIB", "modlinkDown"))
)
if mibBuilder.loadTexts:
    linkTrapsGroup.setStatus(
        "current"
    )

linkTrapsDrop = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 9)
)
linkTrapsDrop.setObjects(
      *(("ENDACE-MODULE-MIB", "dropFault"),
        ("ENDACE-MODULE-MIB", "dropNormal"))
)
if mibBuilder.loadTexts:
    linkTrapsDrop.setStatus(
        "current"
    )

linkTrapsErrors = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 10)
)
linkTrapsErrors.setObjects(
      *(("ENDACE-MODULE-MIB", "fcsFault"),
        ("ENDACE-MODULE-MIB", "fcsNormal"),
        ("ENDACE-MODULE-MIB", "remoteFault"),
        ("ENDACE-MODULE-MIB", "syncLoss"),
        ("ENDACE-MODULE-MIB", "syncReturn"))
)
if mibBuilder.loadTexts:
    linkTrapsErrors.setStatus(
        "current"
    )

moduleTrapsState = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 12)
)
moduleTrapsState.setObjects(
      *(("ENDACE-MODULE-MIB", "inErrorFault"),
        ("ENDACE-MODULE-MIB", "inErrorNormal"))
)
if mibBuilder.loadTexts:
    moduleTrapsState.setStatus(
        "current"
    )

timestampConvertNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 1, 17)
)
timestampConvertNotifyGroup.setObjects(
      *(("ENDACE-MODULE-MIB", "timestampConvDropFault"),
        ("ENDACE-MODULE-MIB", "timestampConvDropNormal"))
)
if mibBuilder.loadTexts:
    timestampConvertNotifyGroup.setStatus(
        "obsolete"
    )


# Agent capabilities


# Module compliance

moduleCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 18418, 2, 2, 2, 1)
)
moduleCompliance1.setObjects(
      *(("ENDACE-MODULE-MIB", "ifControlGroup"),
        ("ENDACE-MODULE-MIB", "ifInHCPacketGroup"),
        ("ENDACE-MODULE-MIB", "ifOutHCPacketGroup"),
        ("ENDACE-MODULE-MIB", "linkTrapsDrop"),
        ("ENDACE-MODULE-MIB", "linkTrapsGroup"),
        ("ENDACE-MODULE-MIB", "moduleControlGroup"),
        ("ENDACE-MODULE-MIB", "obsoleteGroup"),
        ("ENDACE-MODULE-MIB", "moduleTrapsState"),
        ("ENDACE-MODULE-MIB", "linkTrapsErrors"),
        ("ENDACE-MODULE-MIB", "ifModCounterDiscontinuityGroup"),
        ("ENDACE-MODULE-MIB", "timestampConvertNotifyGroup"))
)
if mibBuilder.loadTexts:
    moduleCompliance1.setStatus(
        "obsolete"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENDACE-MODULE-MIB",
    **{"EndaceifType": EndaceifType,
       "InterfaceIndex": InterfaceIndex,
       "ModuleIndex": ModuleIndex,
       "shogunModuleMIB": shogunModuleMIB,
       "moduleMIBObjects": moduleMIBObjects,
       "moduleTable": moduleTable,
       "moduleTableEntry": moduleTableEntry,
       "moduleIndex": moduleIndex,
       "moduleName": moduleName,
       "moduleType": moduleType,
       "moduleActiveFirmware": moduleActiveFirmware,
       "moduleOperStatus": moduleOperStatus,
       "moduleLastChange": moduleLastChange,
       "moduleSnapLen": moduleSnapLen,
       "moduleTemperature": moduleTemperature,
       "moduleVoltage": moduleVoltage,
       "moduleInterfaces": moduleInterfaces,
       "modifTable": modifTable,
       "modifEntry": modifEntry,
       "modifModIndex": modifModIndex,
       "modifPortLabel": modifPortLabel,
       "modifModule": modifModule,
       "modifName": modifName,
       "modifType": modifType,
       "modifMtu": modifMtu,
       "modifInAdminStatus": modifInAdminStatus,
       "modifInOperStatus": modifInOperStatus,
       "modifLastChange": modifLastChange,
       "modifLinkUpDownTrapEnable": modifLinkUpDownTrapEnable,
       "modifLinkDropThreshold": modifLinkDropThreshold,
       "modifSpeed": modifSpeed,
       "modifHighSpeed": modifHighSpeed,
       "modifInOctets": modifInOctets,
       "modifInPackets": modifInPackets,
       "modifInDropPackets": modifInDropPackets,
       "modifOutOctets": modifOutOctets,
       "modifOutPackets": modifOutPackets,
       "modifHCInOctets": modifHCInOctets,
       "modifHCInPackets": modifHCInPackets,
       "modifHCInDropPackets": modifHCInDropPackets,
       "modifHCOutOctets": modifHCOutOctets,
       "modifHCOutPackets": modifHCOutPackets,
       "modifCounterDiscontinuityTime": modifCounterDiscontinuityTime,
       "modifHCInErrors": modifHCInErrors,
       "modifUserLabel": modifUserLabel,
       "modifPhysAddr": modifPhysAddr,
       "modoptTable": modoptTable,
       "modoptEntry": modoptEntry,
       "modoptIndex": modoptIndex,
       "modoptName": modoptName,
       "modoptDetect": modoptDetect,
       "modoptLOS": modoptLOS,
       "modoptRxPower": modoptRxPower,
       "modoptRxPowerOk": modoptRxPowerOk,
       "modoptTxPower": modoptTxPower,
       "modoptTxPowerOk": modoptTxPowerOk,
       "modoptTemp": modoptTemp,
       "modoptTempOk": modoptTempOk,
       "modoptVolt": modoptVolt,
       "modoptVoltOk": modoptVoltOk,
       "modoptCompliance": modoptCompliance,
       "moduleTraps1": moduleTraps1,
       "modlinkUp": modlinkUp,
       "modlinkDown": modlinkDown,
       "dropFault": dropFault,
       "dropNormal": dropNormal,
       "fcsFault": fcsFault,
       "fcsNormal": fcsNormal,
       "remoteFault": remoteFault,
       "timestampConvDropFault": timestampConvDropFault,
       "timestampConvDropNormal": timestampConvDropNormal,
       "syncLoss": syncLoss,
       "syncReturn": syncReturn,
       "inErrorFault": inErrorFault,
       "inErrorNormal": inErrorNormal,
       "moduleConformance": moduleConformance,
       "moduleGroups": moduleGroups,
       "moduleControlGroup": moduleControlGroup,
       "ifControlGroup": ifControlGroup,
       "ifInPacketGroup": ifInPacketGroup,
       "ifOutPacketGroup": ifOutPacketGroup,
       "ifInHCPacketGroup": ifInHCPacketGroup,
       "ifOutHCPacketGroup": ifOutHCPacketGroup,
       "ifModCounterDiscontinuityGroup": ifModCounterDiscontinuityGroup,
       "linkTrapsGroup": linkTrapsGroup,
       "linkTrapsDrop": linkTrapsDrop,
       "linkTrapsErrors": linkTrapsErrors,
       "modoptGroup": modoptGroup,
       "moduleTrapsState": moduleTrapsState,
       "modulePhysStatusGroup": modulePhysStatusGroup,
       "timestampConvertNotifyGroup": timestampConvertNotifyGroup,
       "obsoleteGroup": obsoleteGroup,
       "moduleCompliances": moduleCompliances,
       "moduleCompliance1": moduleCompliance1}
)
