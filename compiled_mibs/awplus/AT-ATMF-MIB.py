# SNMP MIB module (AT-ATMF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs\awplus\AT-ATMF-MIB
# Produced by pysmi-1.6.2 at Thu Oct  2 11:20:21 2025
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

(DisplayStringUnsized,
 modules) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "DisplayStringUnsized",
    "modules")

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

atmf = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603)
)
if mibBuilder.loadTexts:
    atmf.setRevisions(
        ("2014-10-07 12:00",
         "2014-07-04 12:00",
         "2014-05-07 12:00",
         "2013-07-15 12:00",
         "2013-05-27 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AtAtmfTraps_ObjectIdentity = ObjectIdentity
atAtmfTraps = _AtAtmfTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0)
)
_AtAtmfTrapVariable_ObjectIdentity = ObjectIdentity
atAtmfTrapVariable = _AtAtmfTrapVariable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1)
)


class _AtAtmfTrapNodeName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapNodeName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfTrapNodeName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapNodeName_Object = MibScalar
atAtmfTrapNodeName = _AtAtmfTrapNodeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 1),
    _AtAtmfTrapNodeName_Type()
)
atAtmfTrapNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapNodeName.setStatus("current")


class _AtAtmfTrapMasterNodeName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapMasterNodeName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfTrapMasterNodeName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapMasterNodeName_Object = MibScalar
atAtmfTrapMasterNodeName = _AtAtmfTrapMasterNodeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 2),
    _AtAtmfTrapMasterNodeName_Type()
)
atAtmfTrapMasterNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapMasterNodeName.setStatus("current")


class _AtAtmfTrapNetworkName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapNetworkName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AtAtmfTrapNetworkName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapNetworkName_Object = MibScalar
atAtmfTrapNetworkName = _AtAtmfTrapNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 3),
    _AtAtmfTrapNetworkName_Type()
)
atAtmfTrapNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapNetworkName.setStatus("current")


class _AtAtmfTrapInterfaceName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapInterfaceName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AtAtmfTrapInterfaceName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapInterfaceName_Object = MibScalar
atAtmfTrapInterfaceName = _AtAtmfTrapInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 4),
    _AtAtmfTrapInterfaceName_Type()
)
atAtmfTrapInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapInterfaceName.setStatus("current")


class _AtAtmfTrapBackupStatus_Type(Integer32):
    """Custom type atAtmfTrapBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AtAtmfTrapBackupStatus_Type.__name__ = "Integer32"
_AtAtmfTrapBackupStatus_Object = MibScalar
atAtmfTrapBackupStatus = _AtAtmfTrapBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 5),
    _AtAtmfTrapBackupStatus_Type()
)
atAtmfTrapBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapBackupStatus.setStatus("current")


class _AtAtmfTrapNodeStatusChange_Type(Integer32):
    """Custom type atAtmfTrapNodeStatusChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("left", 1),
          ("joined", 2))
    )


_AtAtmfTrapNodeStatusChange_Type.__name__ = "Integer32"
_AtAtmfTrapNodeStatusChange_Object = MibScalar
atAtmfTrapNodeStatusChange = _AtAtmfTrapNodeStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 6),
    _AtAtmfTrapNodeStatusChange_Type()
)
atAtmfTrapNodeStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapNodeStatusChange.setStatus("current")


class _AtAtmfTrapInterfaceStatusChange_Type(Integer32):
    """Custom type atAtmfTrapInterfaceStatusChange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("forwarding", 2))
    )


_AtAtmfTrapInterfaceStatusChange_Type.__name__ = "Integer32"
_AtAtmfTrapInterfaceStatusChange_Object = MibScalar
atAtmfTrapInterfaceStatusChange = _AtAtmfTrapInterfaceStatusChange_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 7),
    _AtAtmfTrapInterfaceStatusChange_Type()
)
atAtmfTrapInterfaceStatusChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapInterfaceStatusChange.setStatus("current")


class _AtAtmfTrapNodeRecoveryStatus_Type(Integer32):
    """Custom type atAtmfTrapNodeRecoveryStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AtAtmfTrapNodeRecoveryStatus_Type.__name__ = "Integer32"
_AtAtmfTrapNodeRecoveryStatus_Object = MibScalar
atAtmfTrapNodeRecoveryStatus = _AtAtmfTrapNodeRecoveryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 8),
    _AtAtmfTrapNodeRecoveryStatus_Type()
)
atAtmfTrapNodeRecoveryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapNodeRecoveryStatus.setStatus("current")


class _AtAtmfTrapMediaType_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapMediaType based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_AtAtmfTrapMediaType_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapMediaType_Object = MibScalar
atAtmfTrapMediaType = _AtAtmfTrapMediaType_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 9),
    _AtAtmfTrapMediaType_Type()
)
atAtmfTrapMediaType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapMediaType.setStatus("current")
_AtAtmfTrapMediaTotal_Type = Integer32
_AtAtmfTrapMediaTotal_Object = MibScalar
atAtmfTrapMediaTotal = _AtAtmfTrapMediaTotal_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 10),
    _AtAtmfTrapMediaTotal_Type()
)
atAtmfTrapMediaTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapMediaTotal.setStatus("current")
_AtAtmfTrapMediaFree_Type = Integer32
_AtAtmfTrapMediaFree_Object = MibScalar
atAtmfTrapMediaFree = _AtAtmfTrapMediaFree_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 11),
    _AtAtmfTrapMediaFree_Type()
)
atAtmfTrapMediaFree.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapMediaFree.setStatus("current")


class _AtAtmfTrapRollingRebootStatus_Type(Integer32):
    """Custom type atAtmfTrapRollingRebootStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AtAtmfTrapRollingRebootStatus_Type.__name__ = "Integer32"
_AtAtmfTrapRollingRebootStatus_Object = MibScalar
atAtmfTrapRollingRebootStatus = _AtAtmfTrapRollingRebootStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 12),
    _AtAtmfTrapRollingRebootStatus_Type()
)
atAtmfTrapRollingRebootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRollingRebootStatus.setStatus("current")


class _AtAtmfTrapRollingRebootReleaseName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapRollingRebootReleaseName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AtAtmfTrapRollingRebootReleaseName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapRollingRebootReleaseName_Object = MibScalar
atAtmfTrapRollingRebootReleaseName = _AtAtmfTrapRollingRebootReleaseName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 13),
    _AtAtmfTrapRollingRebootReleaseName_Type()
)
atAtmfTrapRollingRebootReleaseName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRollingRebootReleaseName.setStatus("current")


class _AtAtmfTrapRollingRebootReleaseStatus_Type(Integer32):
    """Custom type atAtmfTrapRollingRebootReleaseStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("failed", 1),
          ("passed", 2))
    )


_AtAtmfTrapRollingRebootReleaseStatus_Type.__name__ = "Integer32"
_AtAtmfTrapRollingRebootReleaseStatus_Object = MibScalar
atAtmfTrapRollingRebootReleaseStatus = _AtAtmfTrapRollingRebootReleaseStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 14),
    _AtAtmfTrapRollingRebootReleaseStatus_Type()
)
atAtmfTrapRollingRebootReleaseStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRollingRebootReleaseStatus.setStatus("current")
_AtAtmfTrapRemoteBackupServerId_Type = Integer32
_AtAtmfTrapRemoteBackupServerId_Object = MibScalar
atAtmfTrapRemoteBackupServerId = _AtAtmfTrapRemoteBackupServerId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 15),
    _AtAtmfTrapRemoteBackupServerId_Type()
)
atAtmfTrapRemoteBackupServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRemoteBackupServerId.setStatus("current")


class _AtAtmfTrapRemoteBackupServerName_Type(DisplayStringUnsized):
    """Custom type atAtmfTrapRemoteBackupServerName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfTrapRemoteBackupServerName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfTrapRemoteBackupServerName_Object = MibScalar
atAtmfTrapRemoteBackupServerName = _AtAtmfTrapRemoteBackupServerName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 16),
    _AtAtmfTrapRemoteBackupServerName_Type()
)
atAtmfTrapRemoteBackupServerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRemoteBackupServerName.setStatus("current")


class _AtAtmfTrapRemoteServerStatus_Type(Integer32):
    """Custom type atAtmfTrapRemoteServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unavailable", 1),
          ("available", 2))
    )


_AtAtmfTrapRemoteServerStatus_Type.__name__ = "Integer32"
_AtAtmfTrapRemoteServerStatus_Object = MibScalar
atAtmfTrapRemoteServerStatus = _AtAtmfTrapRemoteServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 17),
    _AtAtmfTrapRemoteServerStatus_Type()
)
atAtmfTrapRemoteServerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRemoteServerStatus.setStatus("current")
_AtAtmfTrapRemoteServersAvailable_Type = Integer32
_AtAtmfTrapRemoteServersAvailable_Object = MibScalar
atAtmfTrapRemoteServersAvailable = _AtAtmfTrapRemoteServersAvailable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 1, 18),
    _AtAtmfTrapRemoteServersAvailable_Type()
)
atAtmfTrapRemoteServersAvailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfTrapRemoteServersAvailable.setStatus("current")
_AtAtmfSummary_ObjectIdentity = ObjectIdentity
atAtmfSummary = _AtAtmfSummary_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2)
)


class _AtAtmfSummaryNodeName_Type(DisplayStringUnsized):
    """Custom type atAtmfSummaryNodeName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfSummaryNodeName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfSummaryNodeName_Object = MibScalar
atAtmfSummaryNodeName = _AtAtmfSummaryNodeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 1),
    _AtAtmfSummaryNodeName_Type()
)
atAtmfSummaryNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryNodeName.setStatus("current")


class _AtAtmfSummaryStatus_Type(Integer32):
    """Custom type atAtmfSummaryStatus based on Integer32"""
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


_AtAtmfSummaryStatus_Type.__name__ = "Integer32"
_AtAtmfSummaryStatus_Object = MibScalar
atAtmfSummaryStatus = _AtAtmfSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 2),
    _AtAtmfSummaryStatus_Type()
)
atAtmfSummaryStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryStatus.setStatus("current")


class _AtAtmfSummaryRole_Type(Integer32):
    """Custom type atAtmfSummaryRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("member", 1),
          ("master", 2))
    )


_AtAtmfSummaryRole_Type.__name__ = "Integer32"
_AtAtmfSummaryRole_Object = MibScalar
atAtmfSummaryRole = _AtAtmfSummaryRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 3),
    _AtAtmfSummaryRole_Type()
)
atAtmfSummaryRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryRole.setStatus("current")


class _AtAtmfSummaryNetworkName_Type(DisplayStringUnsized):
    """Custom type atAtmfSummaryNetworkName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AtAtmfSummaryNetworkName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfSummaryNetworkName_Object = MibScalar
atAtmfSummaryNetworkName = _AtAtmfSummaryNetworkName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 4),
    _AtAtmfSummaryNetworkName_Type()
)
atAtmfSummaryNetworkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryNetworkName.setStatus("current")


class _AtAtmfSummaryParentName_Type(DisplayStringUnsized):
    """Custom type atAtmfSummaryParentName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfSummaryParentName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfSummaryParentName_Object = MibScalar
atAtmfSummaryParentName = _AtAtmfSummaryParentName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 5),
    _AtAtmfSummaryParentName_Type()
)
atAtmfSummaryParentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryParentName.setStatus("current")
_AtAtmfSummaryCoreDistance_Type = Integer32
_AtAtmfSummaryCoreDistance_Object = MibScalar
atAtmfSummaryCoreDistance = _AtAtmfSummaryCoreDistance_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 6),
    _AtAtmfSummaryCoreDistance_Type()
)
atAtmfSummaryCoreDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryCoreDistance.setStatus("current")
_AtAtmfSummaryDomainId_Type = Integer32
_AtAtmfSummaryDomainId_Object = MibScalar
atAtmfSummaryDomainId = _AtAtmfSummaryDomainId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 7),
    _AtAtmfSummaryDomainId_Type()
)
atAtmfSummaryDomainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryDomainId.setStatus("current")


class _AtAtmfSummaryRestrictedLogin_Type(Integer32):
    """Custom type atAtmfSummaryRestrictedLogin based on Integer32"""
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


_AtAtmfSummaryRestrictedLogin_Type.__name__ = "Integer32"
_AtAtmfSummaryRestrictedLogin_Object = MibScalar
atAtmfSummaryRestrictedLogin = _AtAtmfSummaryRestrictedLogin_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 8),
    _AtAtmfSummaryRestrictedLogin_Type()
)
atAtmfSummaryRestrictedLogin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryRestrictedLogin.setStatus("current")
_AtAtmfSummaryNodes_Type = Integer32
_AtAtmfSummaryNodes_Object = MibScalar
atAtmfSummaryNodes = _AtAtmfSummaryNodes_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 9),
    _AtAtmfSummaryNodes_Type()
)
atAtmfSummaryNodes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryNodes.setStatus("current")


class _AtAtmfSummaryAreaName_Type(DisplayStringUnsized):
    """Custom type atAtmfSummaryAreaName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AtAtmfSummaryAreaName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfSummaryAreaName_Object = MibScalar
atAtmfSummaryAreaName = _AtAtmfSummaryAreaName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 10),
    _AtAtmfSummaryAreaName_Type()
)
atAtmfSummaryAreaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryAreaName.setStatus("current")


class _AtAtmfSummaryControllerRole_Type(Integer32):
    """Custom type atAtmfSummaryControllerRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("non-controller", 1),
          ("controller", 2))
    )


_AtAtmfSummaryControllerRole_Type.__name__ = "Integer32"
_AtAtmfSummaryControllerRole_Object = MibScalar
atAtmfSummaryControllerRole = _AtAtmfSummaryControllerRole_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 2, 11),
    _AtAtmfSummaryControllerRole_Type()
)
atAtmfSummaryControllerRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfSummaryControllerRole.setStatus("current")
_AtAtmfNodeTable_Object = MibTable
atAtmfNodeTable = _AtAtmfNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 3)
)
if mibBuilder.loadTexts:
    atAtmfNodeTable.setStatus("current")
_AtAtmfNodeEntry_Object = MibTableRow
atAtmfNodeEntry = _AtAtmfNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 3, 1)
)
atAtmfNodeEntry.setIndexNames(
    (0, "AT-ATMF-MIB", "atAtmfNodeName"),
)
if mibBuilder.loadTexts:
    atAtmfNodeEntry.setStatus("current")


class _AtAtmfNodeName_Type(DisplayStringUnsized):
    """Custom type atAtmfNodeName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AtAtmfNodeName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfNodeName_Object = MibTableColumn
atAtmfNodeName = _AtAtmfNodeName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 3, 1, 1),
    _AtAtmfNodeName_Type()
)
atAtmfNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfNodeName.setStatus("current")
_AtAtmfControllerAreaTable_Object = MibTable
atAtmfControllerAreaTable = _AtAtmfControllerAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 4)
)
if mibBuilder.loadTexts:
    atAtmfControllerAreaTable.setStatus("current")
_AtAtmfControllerAreaEntry_Object = MibTableRow
atAtmfControllerAreaEntry = _AtAtmfControllerAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 4, 1)
)
atAtmfControllerAreaEntry.setIndexNames(
    (0, "AT-ATMF-MIB", "atAtmfControllerAreaId"),
)
if mibBuilder.loadTexts:
    atAtmfControllerAreaEntry.setStatus("current")


class _AtAtmfControllerAreaId_Type(Integer32):
    """Custom type atAtmfControllerAreaId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 126),
    )


_AtAtmfControllerAreaId_Type.__name__ = "Integer32"
_AtAtmfControllerAreaId_Object = MibTableColumn
atAtmfControllerAreaId = _AtAtmfControllerAreaId_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 4, 1, 1),
    _AtAtmfControllerAreaId_Type()
)
atAtmfControllerAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfControllerAreaId.setStatus("current")


class _AtAtmfControllerAreaName_Type(DisplayStringUnsized):
    """Custom type atAtmfControllerAreaName based on DisplayStringUnsized"""
    subtypeSpec = DisplayStringUnsized.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_AtAtmfControllerAreaName_Type.__name__ = "DisplayStringUnsized"
_AtAtmfControllerAreaName_Object = MibTableColumn
atAtmfControllerAreaName = _AtAtmfControllerAreaName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 4, 1, 2),
    _AtAtmfControllerAreaName_Type()
)
atAtmfControllerAreaName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfControllerAreaName.setStatus("current")


class _AtAtmfControllerAreaStatus_Type(Integer32):
    """Custom type atAtmfControllerAreaStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unreachable", 1),
          ("reachable", 2))
    )


_AtAtmfControllerAreaStatus_Type.__name__ = "Integer32"
_AtAtmfControllerAreaStatus_Object = MibTableColumn
atAtmfControllerAreaStatus = _AtAtmfControllerAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 4, 1, 3),
    _AtAtmfControllerAreaStatus_Type()
)
atAtmfControllerAreaStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfControllerAreaStatus.setStatus("current")
_AtAtmfControllerAreaMemberCount_Type = Integer32
_AtAtmfControllerAreaMemberCount_Object = MibTableColumn
atAtmfControllerAreaMemberCount = _AtAtmfControllerAreaMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 4, 1, 4),
    _AtAtmfControllerAreaMemberCount_Type()
)
atAtmfControllerAreaMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atAtmfControllerAreaMemberCount.setStatus("current")

# Managed Objects groups


# Notification objects

atAtmfBackupStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 1)
)
atAtmfBackupStatusTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapBackupStatus"))
)
if mibBuilder.loadTexts:
    atAtmfBackupStatusTrap.setStatus(
        "current"
    )

atAtmfNodeStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 2)
)
atAtmfNodeStatusChangeTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapNodeStatusChange"),
        ("AT-ATMF-MIB", "atAtmfTrapNetworkName"))
)
if mibBuilder.loadTexts:
    atAtmfNodeStatusChangeTrap.setStatus(
        "current"
    )

atAtmfNodeRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 3)
)
atAtmfNodeRecoveryTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapNodeRecoveryStatus"))
)
if mibBuilder.loadTexts:
    atAtmfNodeRecoveryTrap.setStatus(
        "current"
    )

atAtmfInterfaceStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 4)
)
atAtmfInterfaceStatusChangeTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapInterfaceName"),
        ("AT-ATMF-MIB", "atAtmfTrapInterfaceStatusChange"))
)
if mibBuilder.loadTexts:
    atAtmfInterfaceStatusChangeTrap.setStatus(
        "current"
    )

atAtmfExternalMediaLowMemoryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 5)
)
atAtmfExternalMediaLowMemoryTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapMediaType"),
        ("AT-ATMF-MIB", "atAtmfTrapMediaTotal"),
        ("AT-ATMF-MIB", "atAtmfTrapMediaFree"))
)
if mibBuilder.loadTexts:
    atAtmfExternalMediaLowMemoryTrap.setStatus(
        "current"
    )

atAtmfRollingRebootCompleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 6)
)
atAtmfRollingRebootCompleteTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapRollingRebootStatus"))
)
if mibBuilder.loadTexts:
    atAtmfRollingRebootCompleteTrap.setStatus(
        "current"
    )

atAtmfRollingRebootReleaseCompleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 7)
)
atAtmfRollingRebootReleaseCompleteTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapRollingRebootStatus"),
        ("AT-ATMF-MIB", "atAtmfTrapRollingRebootReleaseName"),
        ("AT-ATMF-MIB", "atAtmfTrapRollingRebootReleaseStatus"))
)
if mibBuilder.loadTexts:
    atAtmfRollingRebootReleaseCompleteTrap.setStatus(
        "current"
    )

atAtmfRemoteBackupStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 8)
)
atAtmfRemoteBackupStatusTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapRemoteBackupServerId"),
        ("AT-ATMF-MIB", "atAtmfTrapRemoteBackupServerName"),
        ("AT-ATMF-MIB", "atAtmfTrapRemoteServerStatus"),
        ("AT-ATMF-MIB", "atAtmfTrapRemoteServersAvailable"))
)
if mibBuilder.loadTexts:
    atAtmfRemoteBackupStatusTrap.setStatus(
        "current"
    )

atAtmfControllerAreaStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 9)
)
atAtmfControllerAreaStatusChangeTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfControllerAreaName"),
        ("AT-ATMF-MIB", "atAtmfControllerAreaStatus"))
)
if mibBuilder.loadTexts:
    atAtmfControllerAreaStatusChangeTrap.setStatus(
        "current"
    )

atAtmfControllerAreaRemoteBackupStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 603, 0, 10)
)
atAtmfControllerAreaRemoteBackupStatusTrap.setObjects(
      *(("AT-ATMF-MIB", "atAtmfTrapNodeName"),
        ("AT-ATMF-MIB", "atAtmfControllerAreaName"),
        ("AT-ATMF-MIB", "atAtmfTrapMasterNodeName"),
        ("AT-ATMF-MIB", "atAtmfTrapBackupStatus"))
)
if mibBuilder.loadTexts:
    atAtmfControllerAreaRemoteBackupStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-ATMF-MIB",
    **{"atmf": atmf,
       "atAtmfTraps": atAtmfTraps,
       "atAtmfBackupStatusTrap": atAtmfBackupStatusTrap,
       "atAtmfNodeStatusChangeTrap": atAtmfNodeStatusChangeTrap,
       "atAtmfNodeRecoveryTrap": atAtmfNodeRecoveryTrap,
       "atAtmfInterfaceStatusChangeTrap": atAtmfInterfaceStatusChangeTrap,
       "atAtmfExternalMediaLowMemoryTrap": atAtmfExternalMediaLowMemoryTrap,
       "atAtmfRollingRebootCompleteTrap": atAtmfRollingRebootCompleteTrap,
       "atAtmfRollingRebootReleaseCompleteTrap": atAtmfRollingRebootReleaseCompleteTrap,
       "atAtmfRemoteBackupStatusTrap": atAtmfRemoteBackupStatusTrap,
       "atAtmfControllerAreaStatusChangeTrap": atAtmfControllerAreaStatusChangeTrap,
       "atAtmfControllerAreaRemoteBackupStatusTrap": atAtmfControllerAreaRemoteBackupStatusTrap,
       "atAtmfTrapVariable": atAtmfTrapVariable,
       "atAtmfTrapNodeName": atAtmfTrapNodeName,
       "atAtmfTrapMasterNodeName": atAtmfTrapMasterNodeName,
       "atAtmfTrapNetworkName": atAtmfTrapNetworkName,
       "atAtmfTrapInterfaceName": atAtmfTrapInterfaceName,
       "atAtmfTrapBackupStatus": atAtmfTrapBackupStatus,
       "atAtmfTrapNodeStatusChange": atAtmfTrapNodeStatusChange,
       "atAtmfTrapInterfaceStatusChange": atAtmfTrapInterfaceStatusChange,
       "atAtmfTrapNodeRecoveryStatus": atAtmfTrapNodeRecoveryStatus,
       "atAtmfTrapMediaType": atAtmfTrapMediaType,
       "atAtmfTrapMediaTotal": atAtmfTrapMediaTotal,
       "atAtmfTrapMediaFree": atAtmfTrapMediaFree,
       "atAtmfTrapRollingRebootStatus": atAtmfTrapRollingRebootStatus,
       "atAtmfTrapRollingRebootReleaseName": atAtmfTrapRollingRebootReleaseName,
       "atAtmfTrapRollingRebootReleaseStatus": atAtmfTrapRollingRebootReleaseStatus,
       "atAtmfTrapRemoteBackupServerId": atAtmfTrapRemoteBackupServerId,
       "atAtmfTrapRemoteBackupServerName": atAtmfTrapRemoteBackupServerName,
       "atAtmfTrapRemoteServerStatus": atAtmfTrapRemoteServerStatus,
       "atAtmfTrapRemoteServersAvailable": atAtmfTrapRemoteServersAvailable,
       "atAtmfSummary": atAtmfSummary,
       "atAtmfSummaryNodeName": atAtmfSummaryNodeName,
       "atAtmfSummaryStatus": atAtmfSummaryStatus,
       "atAtmfSummaryRole": atAtmfSummaryRole,
       "atAtmfSummaryNetworkName": atAtmfSummaryNetworkName,
       "atAtmfSummaryParentName": atAtmfSummaryParentName,
       "atAtmfSummaryCoreDistance": atAtmfSummaryCoreDistance,
       "atAtmfSummaryDomainId": atAtmfSummaryDomainId,
       "atAtmfSummaryRestrictedLogin": atAtmfSummaryRestrictedLogin,
       "atAtmfSummaryNodes": atAtmfSummaryNodes,
       "atAtmfSummaryAreaName": atAtmfSummaryAreaName,
       "atAtmfSummaryControllerRole": atAtmfSummaryControllerRole,
       "atAtmfNodeTable": atAtmfNodeTable,
       "atAtmfNodeEntry": atAtmfNodeEntry,
       "atAtmfNodeName": atAtmfNodeName,
       "atAtmfControllerAreaTable": atAtmfControllerAreaTable,
       "atAtmfControllerAreaEntry": atAtmfControllerAreaEntry,
       "atAtmfControllerAreaId": atAtmfControllerAreaId,
       "atAtmfControllerAreaName": atAtmfControllerAreaName,
       "atAtmfControllerAreaStatus": atAtmfControllerAreaStatus,
       "atAtmfControllerAreaMemberCount": atAtmfControllerAreaMemberCount}
)
